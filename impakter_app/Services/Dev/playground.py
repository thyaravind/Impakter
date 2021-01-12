from urllib.parse import urlparse


article_url = "https://apple.com/2020/291210304284"

source_url = urlparse(article_url).netloc

if not source_url.startswith("www."):
    source_url = "www."+source_url

print(source_url)
