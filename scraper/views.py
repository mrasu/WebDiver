import datetime
import re
from bs4 import BeautifulSoup
from django.db import transaction
from django.http import HttpResponse
import requests
from viewer.models import WebPage, IgnoreLink, VisitedLink, NewDiscoverLink, NewDiscover


def yodobashi(req):
    yodobashi_page = WebPage.objects.get(pk=1)
    r = requests.get(yodobashi_page.url)
    soup = BeautifulSoup(r.text)
    links = [link for link in soup.find_all("a") if link.get("href")]

    for ignore_regex in IgnoreLink.objects.filter(page=yodobashi_page):
        pattern = re.compile(ignore_regex.regex)
        links = [link for link in links if not pattern.search(link.get("href"))]

    past_discoverd_url = {link.link for link in VisitedLink.objects.filter(page=yodobashi_page).all()}
    discoverd_url = {link.get("href") for link in links}

    new_discovered = discoverd_url - past_discoverd_url

    new_discovered = [link for link in links if link.get("href") in new_discovered]

    if new_discovered:
        new_visited = [
            VisitedLink(
                link=url.get("href"),
                page=yodobashi_page,
                name=url.string,
                img_link=url.find("img").get("src") if url.find("img") else None)
            for url in new_discovered
        ]
        [visited.save() for visited in new_visited]
        discover = NewDiscover(name='ヨドバシカメラ', time=datetime.datetime.now())
        discover.save()
        NewDiscoverLink.objects.bulk_create([NewDiscoverLink(discover=discover, link=link) for link in new_visited])

    return HttpResponse(new_discovered)