import os
import sys

# Activate the crawler:
if len(sys.argv) <= 1:
    os.system("scrapy crawl broad -o crawled.json")
else:
    domain = sys.argv[1]
    os.system(f"scrapy crawl broad -a domain={domain} -o crawled.json")
# Combine the text from every page:
os.system("python combine.py")
# Format the data for Elasticsearch:
os.system("cat combined.json | ./format > formatted.json")

# Add an empty line to the end of the file:
os.system("echo '' >> formatted.json")
# Upload the data to the Elasticsearch domain:
os.system(f"curl -XPOST ENDPOINT/_bulk --data-binary @formatted.json -H 'Content-Type: application/json'")