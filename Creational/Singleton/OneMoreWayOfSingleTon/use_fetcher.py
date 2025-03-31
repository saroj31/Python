import URLFetcher


for url in [
    "http://python.org",
    "https://planetpython.org/",
    "https://www.djangoproject.com/",
]:
    URLFetcher.fetcher.fetch(url)

print(f"Done URLs: {URLFetcher.fetcher.urls}")