# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=dangerous-default-value
import os
import time
import datetime
import subprocess
import requests
import html2text
from bs4 import BeautifulSoup


def get_post_urls(urls=None, page="http://python-history.blogspot.ca/"):
    """ Recursively parse through each page. Returns a list of links """
    if urls is None:
        urls = []
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
    """ Parses each response for post data"""
    soup = BeautifulSoup(response.content)
    post = soup.find("div", {"class": "post"})

    date = soup.find("h2", {"class": "date-header"}).span.text
    date_tag = soup.new_tag("h5")
    date_tag.string = date
    post.insert(1, date_tag)

    unix = time.mktime(datetime.datetime.strptime(date, "%A, %B %d, %Y").timetuple())

    title = post.find("h3", {"class": "post-title"}).text.strip()
    body = post.find("div", {"class": "post-body"}).text

    hr_tag = soup.new_tag("hr")
    post.insert(1, hr_tag)

    parsed = {
        "date": date,
        "unix": unix,
        "html": soup,
        "post": post,
        "title": title,
        "body": body
    }
    return parsed

def filename_reformat(title):
    """ Reformat title to make it a better filename """
    return title.replace(",", "").replace(" ", "-").lower() + ".md"


if __name__ == "__main__":
    urls = get_post_urls()
    responses = [requests.get(url) for url in urls]
    assert len(urls) == 31

    handler = html2text.HTML2Text()
    data_unordered = [parse_url(res) for res in responses]
    # Sort posts by unix time
    data = sorted(data_unordered, key=lambda k: k["unix"])

    subprocess.call(["mkdir", "-p", "markdown"])
    for data_i in data:
        post = data_i["post"]

        md = handler.handle(str(post))
        filename = filename_reformat(data_i["title"])
        with open(os.path.join("markdown", filename), "w") as f:
            f.write(md)

    os.system("pandoc markdown/*.md -f markdown -o the-history-of-python.pdf")
