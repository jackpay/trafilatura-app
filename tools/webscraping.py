from trafilatura import extract

"""
Container class for all web scraping methods/tools
"""

"""
Uses the trafilatura toolkit to discover the main content/article on a page. This works best with pages containing large 
bodies of text; such as new articles.
"""
def scrape_main_content(raw_html, progress_callback):
    progress_callback()
    return extract(raw_html, include_links=True)
