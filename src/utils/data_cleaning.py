import pandas as pd
import re

# --- Function Definitions ---

def normalize_amharic(text):
    """
    Normalizes variations of Amharic characters to a standard form.
    """
    normalization_map = {
        'ሐ': 'ሀ', 'ሑ': 'ሁ', 'ሒ': 'ሂ', 'ሓ': 'ሃ', 'ሔ': 'ሄ', 'ሕ': 'ህ', 'ሖ': 'ሆ',
        'ኀ': 'ሀ', 'ኁ': 'ሁ', 'ኂ': 'ሂ', 'ኃ': 'ሃ', 'ኄ': 'ሄ', 'ኅ': 'ህ', 'ኆ': 'ሆ',
        'ሠ': 'ሰ', 'ሡ': 'ሱ', 'ሢ': 'ሲ', 'ሣ': 'ሳ', 'ሤ': 'ሴ', 'ሥ': 'ስ', 'ሦ': 'ሶ',
        'ዐ': 'አ', 'ዑ': 'ኡ', 'ዒ': 'ኢ', 'ዓ': 'ኣ', 'ዔ': 'ኤ', 'ዕ': 'እ', 'ዖ': 'ኦ',
        'ጸ': 'ፀ', 'ጹ': 'ፁ', 'ጺ': 'ፂ', 'ጻ': 'ፃ', 'ጼ': 'ፄ', 'ጽ': 'ፅ', 'ጾ': 'ፆ',
    }
    regex = re.compile("|".join(map(re.escape, normalization_map.keys())))
    return regex.sub(lambda match: normalization_map[match.group(0)], text)

def clean_text(text):
    """
    Cleans the text by removing URLs, mentions, hashtags, and unwanted characters,
    while keeping both Amharic and English text.
    """
    # Convert text to lowercase to treat 'Nike' and 'nike' the same
    text = text.lower()
    
    # 1. Remove URLs (e.g., http://... or www....)
    text = re.sub(r'http\S+|www\S+', '', text)

    # 2. Remove Telegram-specific links (e.g., t.me/...)
    text = re.sub(r't\.me\/\S+', '', text)

    # 3. Remove mentions and hashtags (e.g., @username, #sale)
    # Note: If you later decide to extract CONTACT_INFO like usernames, you'll need to adjust this.
    text = re.sub(r'@\w+|#\w+', '', text)

    # 4. Remove unwanted characters.
    # This regex now KEEPS Amharic, English (a-z), numbers, and basic punctuation.
    text = re.sub(r'[^\u1200-\u137fa-z\d\s።፡,.]', '', text)

    # 5. Remove extra whitespace, newlines, and tabs
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# --- Main Processing ---

# 1. Load Data
try:
    # Make sure to use your actual file name
    df = pd.read_csv('telegram_data.csv') 
    print("Successfully loaded data.")
except FileNotFoundError:
    print("Error: Make sure your CSV file is in the same directory or provide the full path.")
    exit()

# 2. Initialize processed_text column from 'Message Text'
# Ensure it's a string and handle empty messages
df['processed_text'] = df['Message Text'].fillna('').astype(str)

# 3. Apply Normalization
print("Normalizing text...")
df['processed_text'] = df['processed_text'].apply(normalize_amharic)

# 4. Apply Cleaning (the new and improved function)
print("Cleaning text (now keeping English)...")
df['processed_text'] = df['processed_text'].apply(clean_text)

# 5. Save the processed data to a new file
output_filename = 'processed_amharic_data.csv'
df.to_csv(output_filename, index=False, encoding='utf-8')

print(f"\nPreprocessing complete! The cleaned data has been saved to '{output_filename}'")
print("\nHere is a sample of your original vs. processed text:")
print(df[['Message Text', 'processed_text']].head(10).to_string())