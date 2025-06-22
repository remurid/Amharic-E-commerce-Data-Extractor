# Amharic E-commerce Data Extractor

This project provides tools for extracting, cleaning, and processing Amharic and English e-commerce data, especially from Telegram channels. It includes scripts for scraping Telegram messages, normalizing Amharic text, and preparing datasets for analysis or machine learning.

## Features

- **Telegram Scraper:** Collects messages and media from a list of Telegram channels using the Telethon library.
- **Amharic Text Normalization:** Standardizes variations of Amharic Unicode characters for consistent analysis.
- **Text Cleaning:** Removes URLs, Telegram links, mentions, hashtags, and unwanted symbols while preserving Amharic, English, numbers, and basic punctuation.
- **CSV Processing:** Loads raw scraped data, applies preprocessing, and saves cleaned results.
- **Sample Output:** Provides a preview of original vs. processed text for quality assurance.

## Project Structure

- `src/` – Source code for data extraction and cleaning
  - `services/telegram_scraper.py` – Telegram scraping script
  - `utils/data_cleaning.py` – Text normalization and cleaning functions
- `data/` – Place your raw and processed data files here
- `notebooks/` – Jupyter notebooks for exploration and analysis
- `scripts/` – Utility scripts
- `photos/` – Downloaded media from Telegram
- `processed_amharic_data.csv` – Output file with cleaned data

## Installation

1. Clone the repository.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Scrape Telegram Channels

Edit the list of channels in `src/services/telegram_scraper.py` as needed. Add your Telegram API credentials to a `.env` file:

```
TELEGRAM_APP_ID=your_app_id
TELEGRAM_APP_HASH=your_app_hash
```

Run the scraper:

```bash
python src/services/telegram_scraper.py
```

This will create `telegram_data.csv` and download media to the `photos/` directory.

### 2. Clean and Normalize Data

Run the data cleaning script:

```bash
python src/utils/data_cleaning.py
```

This will generate `processed_amharic_data.csv` with cleaned and normalized text.

## Example Output

A typical row after processing:

| Message Text | processed_text |
|--------------|---------------|
| ዋጋ፦ 200 ብር ... | ዋጋ 200 ብር ... |

## Requirements

- Python 3.8+
- pandas
- telethon
- python-dotenv

## License

Add your license information here.

---
For more details, see the code and documentation in the repository.
