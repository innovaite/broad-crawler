import json

# Import the scraped data:
with open("crawled.json") as fp:
    pages = json.load(fp)

url = []
text = []

for page in pages:
    # Check if the URL and text are empty:
    page_url = page["url"].strip()
    page_text = page["text"].strip()
    if len(page_url) >= 1:
        url.append(page_url)
    if len(page_text) >= 1:
        text.append(page_text)

# Combine the text from every page:
text = " ".join(text)

total = {"url": url, "text": text}
# Upload the combined data:
with open("combined.json", "w") as fp:
    json.dump(total, fp)

print("Combined all pages!")