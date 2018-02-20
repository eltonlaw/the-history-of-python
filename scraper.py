# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=dangerous-default-value
import requests
import html2text
from bs4 import BeautifulSoup


def get_post_urls(urls=[], page="http://python-history.blogspot.ca/"):
    """ Recursively parse through each page """
    response = requests.get(page)
    soup = BeautifulSoup(response.content)
    titles = soup.find_all("h3", {"class": "post-title entry-title"})
    urls.extend([title.a["href"] for title in titles])

    try:
        # Look for an `Older Posts` button
        next_page = soup.find("a", {"class": "blog-pager-older-link"})["href"]
        return get_post_urls(urls=urls, page=next_page)
    except TypeError:
        return urls

def parse_url(response):
    soup = BeautifulSoup(response.content)
    date = soup.find("h2", {"class": "date-header"}).span.text
    post = soup.find("div", {"class": "post"})
    title = post.find("h3", {"class": "post-title"}).text.strip()
    body = post.find("div", {"class": "post-body"}).text
    parsed = {
        "date": date,
        "html": soup,
        "post": post,
        "title": title,
        "body": body
    }
    return parsed

if __name__ == "__main__":
    urls = get_post_urls()
    responses = [requests.get(url) for url in urls]
    assert len(urls) == 31
    data = [parse_url(res) for res in responses]
    handler = html2text.HTML2Text()
    for data_i in data:
        handler.handle(str(data_i["post"]))
