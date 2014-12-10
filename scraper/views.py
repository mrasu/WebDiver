import datetime
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from django.http import HttpResponse
import requests
from viewer.models import WebPage, IgnoreLink, VisitedLink, NewDiscoverLink, NewDiscover


def scrape_all(request):
    new_discovers = []
    for page in WebPage.objects.all():
        news = scrape_page(page)
        if news:
            new_discovers.extend(news)

    return HttpResponse(new_discovers)


def scrape_page(page):
    r = requests.get(page.url)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text)
    links = [link for link in soup.find_all("a") if link.get("href")]

    for ignore_regex in IgnoreLink.objects.filter(page=page):
        pattern = re.compile(ignore_regex.regex)
        links = [link for link in links if not pattern.search(link.get("href"))]

    past_discovered_url = {link.link for link in VisitedLink.objects.filter(page=page).all()}
    discovered_url = {link.get("href") for link in links}

    new_discovered = discovered_url - past_discovered_url

    new_discovered = [link for link in links if link.get("href") in new_discovered]

    if new_discovered:
        new_visited = [
            VisitedLink(
                link=url.get("href"),
                abs_link=urljoin(page.url, url.get("href")),
                page=page,
                name=url.string,
                img_link=urljoin(page.url, url.find("img").get("src")) if url.find("img") else None)
            for url in new_discovered
        ]
        [visited.save() for visited in new_visited]
        discover = NewDiscover(name=page.name, time=datetime.datetime.now())
        discover.save()
        NewDiscoverLink.objects.bulk_create([NewDiscoverLink(discover=discover, link=link) for link in new_visited])

    return new_discovered