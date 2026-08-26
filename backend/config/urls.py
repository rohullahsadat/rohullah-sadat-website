from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from core.sitemaps import (
    StaticViewSitemap,
    ProjectSitemap,
    BookSitemap,
    ArticleSitemap,
)

from core.views import (
    home,
    about,
    projects,
    books,
    articles,
    gallery,
    resume,
    contact,
    project_details,
    book_reader,
    article_details,
)


# =========================================================
# BASE URLS
# =========================================================

urlpatterns = [
    # -----------------------------------------------------
    # Admin
    # -----------------------------------------------------
    path(
        "admin/",
        admin.site.urls,
    ),

    # -----------------------------------------------------
    # Sitemap
    # -----------------------------------------------------
    path(
        "sitemap.xml",
        sitemap,
        {
            "sitemaps": {
                "static": StaticViewSitemap,
                "projects": ProjectSitemap,
                "books": BookSitemap,
                "articles": ArticleSitemap,
            }
        },
        name="sitemap",
    ),

    # -----------------------------------------------------
    # Robots
    # -----------------------------------------------------
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain",
        ),
        name="robots",
    ),

    # -----------------------------------------------------
    # Media Files
    # -----------------------------------------------------
    #
    # این route عمداً خارج از DEBUG قرار گرفته تا در
    # Production با DEBUG=False نیز فایل‌های Media
    # مانند تصاویر پروژه‌ها، گالری و کتاب‌ها نمایش داده شوند.
    #
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]


# =========================================================
# INTERNATIONALIZED URLS
# =========================================================

urlpatterns += i18n_patterns(

    # -----------------------------------------------------
    # Main Pages
    # -----------------------------------------------------
    path(
        "",
        home,
        name="home",
    ),

    path(
        "about/",
        about,
        name="about",
    ),

    path(
        "projects/",
        projects,
        name="projects",
    ),

    path(
        "books/",
        books,
        name="books",
    ),

    path(
        "articles/",
        articles,
        name="articles",
    ),

    path(
        "gallery/",
        gallery,
        name="gallery",
    ),

    path(
        "resume/",
        resume,
        name="resume",
    ),

    path(
        "contact/",
        contact,
        name="contact",
    ),

    # -----------------------------------------------------
    # Books
    # -----------------------------------------------------
    path(
        "book-reader/<int:book_id>/",
        book_reader,
        name="book_reader",
    ),

    # -----------------------------------------------------
    # Articles
    # -----------------------------------------------------
    path(
        "articles/<slug:slug>/",
        article_details,
        name="article_details",
    ),

    # -----------------------------------------------------
    # Projects
    # -----------------------------------------------------
    path(
        "project-details/<int:project_id>/",
        project_details,
        name="project_details",
    ),
)