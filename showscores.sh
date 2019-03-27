#!/usr/bin/env bash

# Run webscraper and discard output
scrapy runspider scrape.py -o output.json &> /dev/null

# Output json
python3 output.py output.json

# Remove output
rm output.json