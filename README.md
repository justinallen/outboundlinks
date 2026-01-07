# outboundlinks

Web scraper to crawl a website pulling down all outbound links

## Description

This is a simple Python web scraper using Scrapy to recursively crawl an entire website, gathering all outbound links and the pages they are listed on. The scraper outputs a two-column CSV file with the outbound links and the page URLs where the links are found on the site.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

To crawl a website and extract outbound links:

```bash
scrapy crawl outbound -a start_url=https://example.com -o outbound_links.csv
```

### Parameters

- `start_url`: The URL to start crawling from (required)
- `-o outbound_links.csv`: Output file name (CSV format with two columns: outbound_link, source_page)

### Example

```bash
scrapy crawl outbound -a start_url=https://www.python.org -o python_outbound_links.csv
```

This will:
1. Start crawling from https://www.python.org
2. Follow all internal links on the python.org domain
3. Extract all external (outbound) links found on each page
4. Save the results to `python_outbound_links.csv` with two columns:
   - `outbound_link`: The external URL found
   - `source_page`: The page on python.org where the link was found

## Output Format

The output CSV file contains two columns:
- **outbound_link**: The URL of the external link
- **source_page**: The URL of the page where the outbound link was found

## Features

- Recursive crawling of entire websites
- Respects robots.txt
- Polite crawling with delays between requests
- Extracts only outbound (external) links
- CSV output format for easy analysis

