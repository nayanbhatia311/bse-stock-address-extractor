# bse-stock-address-extractor
 A collection of overly engineered automation scripts that go on Google, search for a BSE (or NSE) company, take a screenshot of the results, and then hand that screenshot to an LLM to magically extract the company's address and state — because why settle for simple when you can make it ridiculously complicated?

# Why is this needed?
## Purpose

- **Legal Compliance**: Ensuring adherence to regulatory requirements by maintaining up-to-date company records.

- **Official Communication**: Facilitating the delivery of legal documents and official correspondence to the correct company address.

- **Due Diligence**: Assisting in verifying company details during financial analyses, audits, or legal proceedings.

- **Share Transmission**: Streamlining the process of transferring shares by providing necessary address information for legal heirs or representatives.


This tool was inspired by a personal need: my family holds few old stocks, and the process of share transmission often requires accurate registered office addresses for legal communication. My dad, who is an advocate, made me write this tool so that he can proceed with the share transmission process.


## Overview
The BSE Stock Address Extractor is a collection of automation scripts designed to extract company addresses and states from the Bombay Stock Exchange (BSE) or National Stock Exchange (NSE) websites. This process involves:

### Scraping: Automating web searches for company address.
### Screenshotting: Capturing the search results.
### Parsing: Utilizing LLMs to parse the relevant address and state details from the screenshots.

Note: This tool aims to complicate data collection. (honestly an api call would have worked too but I was too deep into the rabbit hole).

## Getting Started

```bash
git clone https://github.com/nayanbhatia311/bse-stock-address-extractor.git 

pip install pandas openpyxl requests pillow ollama pytesseract 

osascript bse-stock-screenshot.scpt (**need mac os**) 

python stock_address_parser.py
```
