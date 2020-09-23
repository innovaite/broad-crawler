import scrapy

class Crawler(scrapy.Spider):
    name = "broad"

    def __init__(self, domain="innovaite"):
        self.start_urls = [f"https://www.{domain}.com/"]

    def parse(self, response):
        # Find the URLs on the current page:
        for url in response.css("a::attr(href)"):
            url_string = url.get()
            # Don't scrape the first URL more than once:
            if len(url_string) <= 0 or self.start_urls[0] == url_string:
                continue
            # Ensure that the URL leads to another page on the same domain:
            if url_string[0] == "/" or self.start_urls[0] in url_string:
                yield response.follow(url, callback=self.parse)

        # Return the page's URL and text:
        text = []
        for chunk in response.css("p::text, b::text, i::text, li::text"):
            chunk_text = chunk.get().strip()
            if len(chunk_text) >= 1:
                text.append(chunk_text)

        yield {
            "url": response.url,
            "text": " ".join(text)
        }