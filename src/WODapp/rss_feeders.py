import feedparser

def get_japanese_from_transparent_language():
    rss_entry = feedparser.parse("http://feeds.feedblitz.com/japanese-word-of-the-day")
    word = rss_entry['entries'][0]['title'].split(':')[0]
    definition = rss_entry['entries'][0]['title'].split(': ')[1]
    return word, definition

def get_english_from_wordsmith():
    rss_entry = feedparser.parse("http://wordsmith.org/awad/rss1.xml")
    definition = rss_entry['entries'][0]['summary']
    word = rss_entry['entries'][0]['title']
    return word, definition



