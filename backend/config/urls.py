from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

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


urlpatterns = [

    # Admin
    path("admin/", admin.site.urls),

    # Main pages
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("projects/", projects, name="projects"),
    path("books/", books, name="books"),
    path("articles/", articles, name="articles"),
    path("gallery/", gallery, name="gallery"),
    path("resume/", resume, name="resume"),
    path("contact/", contact, name="contact"),

    # Books
    path(
        "book-reader/<int:book_id>/",
        book_reader,
        name="book_reader",
    ),

    # Articles
    path(
        "articles/<slug:slug>/",
        article_details,
        name="article_details",
    ),

    # Projects
    path(
        "project-details/<int:project_id>/",
        project_details,
        name="project_details",
    ),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )