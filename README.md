# bse-stock-address-extractor
 A collection of overly engineered automation scripts that go on Google, search for a BSE (or NSE) company, take a screenshot of the results, and then hand that screenshot to an LLM to magically extract the company's address and state — because why settle for simple when you can make it ridiculously complicated?

## Overview
The BSE Stock Address Extractor is a collection of automation scripts designed to extract company addresses and states from the Bombay Stock Exchange (BSE) or National Stock Exchange (NSE) websites. This process involves:

### Scraping: Automating web searches for company address.
### Screenshotting: Capturing the search results.
### Parsing: Utilizing LLMs to parse the relevant address and state details from the screenshots.

Note: This tool aims to complicate data collection. (honestly an api call would have worked too but I was too deep into the rabbit hole).

## Getting Started

git clone https://github.com/nayanbhatia311/bse-stock-address-extractor.git 

pip install pandas openpyxl requests pillow ollama pytesseract 

Run the Apple Script bse-stock-screenshot.scpt (**need mac os**) 

python stock_address_parser.py 
