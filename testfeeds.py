import feedparser
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


feed = feedparser.parse("http://rss.cnn.com/rss/edition.rss")

for entry in feed.entries:

    if entry.description:
        print(entry.description)
    else:
        entry.description = ''






