from scrapling import Fetcher

fetcher = Fetcher(auto_match=False)

# Do http GET request to a web page and create an Adaptor instance
page = fetcher.get('https://www.hk01.com/%E5%A4%A7%E5%9C%8B%E5%B0%8F%E4%BA%8B/1037902/%E6%B7%B1%E5%9C%B3%E5%8D%97%E5%B1%B1-%E5%9D%AA%E5%B1%B1%E5%8D%80%E8%A9%A6%E9%81%8B%E7%84%A1%E4%BA%BA%E9%A7%95%E9%A7%9B%E7%9A%84%E5%A3%AB-8%E5%85%AC%E9%87%8C%E5%84%AA%E6%83%A0%E5%83%B9%E5%83%858%E6%AF%AB%E5%AD%90', stealthy_headers=True)
# Get all text content from all HTML tags in the page except `script` and `style` tags
print(page.get_all_text(ignore_tags=('script', 'style')))