import datetime
from django.db import models


class WebPage(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class VisitedLink(models.Model):
    page = models.ForeignKey(WebPage)
    name = models.CharField(max_length=1000, null=True)
    link = models.CharField(max_length=200)
    abs_link = models.CharField(max_length=200)
    img_link = models.CharField(max_length=200, null=True)


class NewDiscover(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField()

    def discovers_today(self):
        return (datetime.datetime.now() - self.time.replace(tzinfo=None)).days < 1


class NewDiscoverLink(models.Model):
    discover = models.ForeignKey(NewDiscover, related_name="links")
    link = models.ForeignKey(VisitedLink)


class IgnoreLink(models.Model):
    page = models.ForeignKey(WebPage)
    regex = models.CharField(max_length=100)

    def __str__(self):
        return self.page.name + " : " + self.regex