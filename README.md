📈 Yahoo Finance Stocks Scraper

📋 Project Overview

Yahoo Finance Stocks Scraper is a 🎯 lightweight, efficient Python web scraping solution designed to extract real-time stock market data from Yahoo Finance. This project demonstrates practical web automation, data cleaning, and financial data engineering techniques suitable for market research, portfolio tracking, and data analysis.

🎯 Purpose

📊 Extract stock listing data (name, symbol, price, change, volume, market cap, PE ratio) from Yahoo Finance for market analysis, investment research, and portfolio demonstration. Built with clean code practices and efficient data processing.

✨ What Makes It Different

 Lightweight & Fast: Minimal dependencies, quick execution

 Real-Time Data: Extract live stock market information

 Dual Pipeline: Separate scraper and cleaning modules for clarity

 Smart Data Processing: Advanced cleaning with value normalization

 Portfolio Ready: Clean code, proper documentation, production-grade

📊 Key Features

✅ Efficient Stock Data Extraction 📈
 Page-by-page pagination through market listings

 Structured table parsing with CSS selectors

 Robust element waiting with WebDriverWait

 Graceful pagination detection (next button handling)

✅ Smart Data Extraction 🎯

 Stock symbol and name extraction

 Price data capture

 Volume and market capitalization

 PE ratio and percentage change tracking

 Real-time market data

✅ Comprehensive Data Cleaning 🧹

 String normalization (trim, lowercase)

 Price conversion to numeric format

 Volume formatting (M suffix handling, multiplication)

 Market cap parsing (B, T suffix conversion)

 PE ratio validation with fallback values

 Duplicate removal

✅ Production-Grade Code 💻

 Try-catch error handling

 WebDriverWait for dynamic content

 Graceful degradation on missing elements

 Clean OOP architecture with methods

🛠️ Tech Stack

| 🔧 Technology   | 📌 Version | 🎯 Purpose                  |
| --------------- | ---------- | --------------------------- |
| 🐍 Python       | 3.8+       | Core language               |
| 🌐 Selenium     | 4.x        | Browser automation          |
| 📊 pandas       | 2.0+       | Data processing & cleaning  |
| 🎭 ActionChains | Selenium   | User interaction simulation |
📁 Project Structure

text
yahoo-finance-stocks-scraper/
├── 📄 README.md
├── 📄 requirements.txt
├──  yahoo_scraper.py
├──  clean_yahoo_data.py
├── 📁 data/
│   ├── yaho_fininces_stocks.csv
│   └── yaho_fininces_stocks_data.csv
└── 📁 docs/
    └── data_sample.csv
    
🚀 Quick Start

 Prerequisites

 Python 3.8+ (3.9+ recommended)

 Google Chrome (latest version)

 ChromeDriver (automatically managed by Selenium)

 pip & Git

## 🔧 Installation
 1️⃣ Clone Repository
bash
git clone https://github.com/ketandas-codes/yahoo-finance-stocks-scraper.git
cd yahoo-finance-stocks-scraper
2️⃣ Create Virtual Environment
bash
 macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

 Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
3️⃣ Install Dependencies
bash
pip install -r requirements.txt
requirements.txt:

text
selenium==4.15.2
pandas==2.1.4
4️⃣ Verify Chrome Installation ✅
bash
 macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version

 Linux
google-chrome --version

 Windows
"C:\Program Files\Google\Chrome\Application\chrome.exe" --version

💻 Usage

 Run the Scraper
bash
python yahoo_scraper.py
What it does:

 Opens Yahoo Finance Most Active Stocks page

 Waits for page to load completely

 Scrapes all visible stock data

 Navigates through pagination pages

 Saves raw data to yaho_fininces_stocks.csv

Output: yaho_fininces_stocks.csv (raw, unprocessed data)

text
name | symbol | price | change | volume | market_cap | pe_ratio
Apple | AAPL | 195.23 | +2.45% | 45.2m | 3.2t | 28.5
Microsoft | MSFT | 425.16 | +1.82% | 18.5m | 3.15t | 35.2

▶️ Run the Data Cleaner

bash
python clean_yahoo_data.py
What it does:

 Reads raw CSV data

 Removes duplicates and normalizes strings

 Converts price to numeric format

 Processes volume (handles M suffix, multiplies by 1M)

 Parses market cap (B = billions, T = trillions)

 Validates PE ratio with fallback "--"

 Exports cleaned data to yaho_fininces_stocks_data.csv

Output: yaho_fininces_stocks_data.csv (cleaned, normalized data)

text
name | symbol | price | change | volume | market_cap | pe_ratio
apple | aapl | 195.23 | +2.45% | 45200000 | 3200000000000 | 28.5
microsoft | msft | 425.16 | +1.82% | 18500000 | 3150000000000 | 35.2
🔧 Configuration & Customization

⚙️ Adjust Scraper Parameters

Edit values in yahoo_scraper.py:

 TIMEOUT: Increase if page loads slowly (default: 10s)

 MAX_PAGES: Limit pagination (default: all pages)

 BASE_URL: Change to different stock filter pages

 WINDOW_SIZE: Adjust browser resolution

🌍 Custom Stock Pages

Modify the __main__ section to scrape different stock lists:

python
 Most Active Stocks
URL = "https://finance.yahoo.com/markets/stocks/most-active/"

 Gainers
URL = "https://finance.yahoo.com/markets/stocks/gainers/"

 Losers
URL = "https://finance.yahoo.com/markets/stocks/losers/"

 By market cap
URL = "https://finance.yahoo.com/markets/stocks/by-market-cap/"

## 📝 Data Cleaning Details

Price Cleaning
Converts string to numeric format

Handles currency symbols (auto-stripped)

Coerces errors to NaN

Volume Cleaning
Removes "m" (millions) suffix

Strips whitespace

Multiplies by 1,000,000 for actual volume

Example: 45.2m → 45200000

Market Cap Cleaning
Handles "B" (billions) suffix

Handles "T" (trillions) suffix

Converts to actual numeric values

Example: 3.2t → 3200000000000

PE Ratio Cleaning
Converts to numeric format

Fills missing values with "--"

Handles N/A and invalid values

📊 Common Use Cases

1.  Market Trend Analysis
Scrape stock data regularly to analyze market trends, identify gainers/losers, and track market movements.

2.  Investment Research
Extract stock fundamentals (PE ratio, market cap) for investment screening and due diligence.

3.  Portfolio Monitoring
Track specific stocks over time and build historical price databases for analysis.

4.  Learning Project
Understand web scraping, data cleaning, and financial data processing with real market data.

⚠️ Important Notes & Best Practices
🔗 Chrome Driver Setup
Selenium automatically manages ChromeDriver. If issues occur:

bash
## Update Selenium to latest
pip install --upgrade selenium
🚦 Rate Limiting & Ethical Scraping
⚡ Yahoo Finance's servers handle significant traffic. Be responsible:

🕐 Don't scrape during heavy market hours if possible

⏳ Add delays between requests (already implemented)

📊 Respect robots.txt guidelines

🧪 Test on small dataset first

🔄 Don't scrape more than necessary

## ✅ Best Practices

### ✅ DO:

⏳ Use WebDriverWait for dynamic content

🎯 Handle pagination correctly

🛡️ Implement error handling

🧹 Clean and normalize data properly

📊 Store raw data separately from cleaned data

### ❌ DON'T:

🚫 Hammer the server with rapid requests

🚫 Ignore page loading signals

🚫 Store sensitive user information

🚫 Violate terms of service

🚫 Skip data validation

📜 License
📋 MIT License — See LICENSE file for details.

✅ In plain English:

✅ Use commercially

✅ Modify freely

✅ Distribute

⚠️ Include original license

⚠️ No warranty provided

📧 Contact & Support
👨‍💻 Author: Ketan Das
🔖 Title: Python Developer | Web Scraping & Automation

📧 Email: ketankumar.codes@gmail.com
🐙 GitHub: @ketandas-codes
💼 Portfolio: [Your Portfolio Link]

💬 Questions or Issues?
🐛 Report bugs: GitHub Issues

💭 Discuss ideas: GitHub Discussions

📬 Email for commercial inquiries

🎓 Learning Resources
📚 Related Concepts:

Selenium Documentation

Pandas Data Processing

Yahoo Finance API

Web Scraping Best Practices

## 🙌 Acknowledgments
 Selenium project for robust browser automation

 pandas community for data manipulation tools

 Yahoo Finance for providing market data

📈 Project Stats

⭐ Star this repo if you found it useful!

🐛 Report issues to help improve

🔄 Fork and adapt for your use case

💡 Share your improvements


🔗 Quick Links
🚀 Installation

💻 Usage

⚙️ Configuration

📬 Contact
