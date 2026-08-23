from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Project, Book, Article


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
            "home",
            "about",
            "projects",
            "books",
            "articles",
            "gallery",
            "resume",
            "contact",
        ]

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return Project.objects.all().order_by("id")

    def location(self, obj):
        return reverse(
            "project_details",
            kwargs={"project_id": obj.id},
        )


class BookSitemap(Sitemap):
    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return Book.objects.all().order_by("id")

    def location(self, obj):
        return reverse(
            "book_reader",
            kwargs={"book_id": obj.id},
        )


class ArticleSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return Article.objects.all().order_by("id")

    def location(self, obj):
        return reverse(
            "article_details",
            kwargs={"slug": obj.slug},
        )