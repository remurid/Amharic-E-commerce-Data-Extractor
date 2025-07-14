import pandas as pd
import random
import ast

# Path to your CSV file
csv_path = '././processed_amharic_data.csv'
# Output TXT file
output_txt = '././random_50_tokens.txt'

# Read the CSV file
df = pd.read_csv(csv_path)

# Ensure required columns exist
if 'tokens' not in df.columns or 'Channel Username' not in df.columns:
    raise ValueError("CSV must contain 'tokens' and 'Channel Username' columns.")

# Group by channel and sample messages
channels = df['Channel Username'].unique()
sampled_rows = []

# Shuffle channels to ensure randomness
channels = list(channels)
random.shuffle(channels)

# Collect up to 50 unique messages from different channels
for channel in channels:
    channel_df = df[df['Channel Username'] == channel]
    if not channel_df.empty:
        sampled_row = channel_df.sample(n=1)
        sampled_rows.append(sampled_row)
        if len(sampled_rows) == 50:
            break

# If less than 50 channels, sample more from remaining data
if len(sampled_rows) < 50:
    remaining = 50 - len(sampled_rows)
    remaining_df = df.drop(pd.concat(sampled_rows).index)
    if not remaining_df.empty:
        extra_samples = remaining_df.sample(n=min(remaining, len(remaining_df)))
        sampled_rows.append(extra_samples)

# Concatenate all sampled rows
final_sample = pd.concat(sampled_rows).head(50)

# Write tokens to txt file in CoNLL format: one token per line, blank line after each message
with open(output_txt, 'w', encoding='utf-8') as f:
    for tokens in final_sample['tokens']:
        # Convert string representation of list to actual list if needed
        if isinstance(tokens, str):
            try:
                tokens_list = ast.literal_eval(tokens)
            except Exception:
                tokens_list = [tokens]
        else:
            tokens_list = tokens
        for token in tokens_list:
            f.write(str(token).strip() + '\n')
        f.write('\n')  # Blank line after each message

print(f"Random 50 messages' tokens saved to {output_txt} in CoNLL format.")