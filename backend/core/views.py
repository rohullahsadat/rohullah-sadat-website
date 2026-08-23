from django.shortcuts import render, get_object_or_404
from .models import Project, AboutProfile, Book, Article,  GalleryImage,  GalleryVideo, Certification

from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
import base64

import resend


def home(request):
  return render(request, "site/index.html")

#بخش About 

def about(request):
    about_profile = AboutProfile.objects.first()

    return render(
        request,
        "site/about.html",
        {
            "about_profile": about_profile,
        }
    )
    
    # بخش کتاب ها 
def books(request):

    published_books = Book.objects.filter(
        is_published=True,
        status="published"
    ).order_by(
        "display_order",
        "-created_at"
    )
    

    reading_books = Book.objects.filter(
        is_published=True,
        status="reading"
    ).order_by(
        "display_order",
        "-created_at"
    )

    planned_books = Book.objects.filter(
        is_published=True,
        status="planned"
    ).order_by(
        "display_order",
        "-created_at"
    )

    coming_soon_books = Book.objects.filter(
        is_published=True,
        status="coming_soon"
    ).order_by(
        "display_order",
        "-created_at"
    )

    favorite_books = Book.objects.filter(
        is_published=True,
        is_favorite=True
    ).order_by(
        "display_order",
        "-created_at"
    )

    context = {
        "published_books": published_books,
        "reading_books": reading_books,
        "planned_books": planned_books,
        "coming_soon_books": coming_soon_books,
        "favorite_books": favorite_books,

        # Dynamic statistics
        "published_count": published_books.count(),
        "reading_count": reading_books.count(),
        "planned_count": planned_books.count(),
        "coming_soon_count": coming_soon_books.count(),
        "favorite_count": favorite_books.count(),
    }

    return render(
        request,
        "site/books.html",
        context
    )
def book_reader(request, book_id):
    book = get_object_or_404(
        Book,
        id=book_id,
        is_published=True
    )

    return render(
        request,
        "site/book_reader.html",
        {
            "book": book,
        }
    )
    
#articles section
def articles(request):

    articles = Article.objects.filter(
        is_published=True
    ).order_by(
        "display_order",
        "-published_at",
        "-created_at"
    )

    featured_articles = articles.filter(
        is_featured=True
    )

    return render(
        request,
        "site/articles.html",
        {
            "articles": articles,
            "featured_articles": featured_articles,
        }
    )
    
def article_details(request, slug):

    article = get_object_or_404(
        Article,
        slug=slug,
        is_published=True
    )

    return render(
        request,
        "site/article_details.html",
        {
            "article": article,
        }
    )
    
 
# =========================
# GALLERY
# =========================
def gallery(request):

    gallery_images = GalleryImage.objects.filter(
        is_published=True
    ).order_by(
        "display_order",
        "-created_at"
    )

    gallery_videos = GalleryVideo.objects.filter(
        is_published=True
    ).order_by(
        "display_order",
        "-created_at"
    )

    return render(
        request,
        "site/gallery.html",
        {
            "gallery_images": gallery_images,
            "gallery_videos": gallery_videos,
        }
    )

# resuem section
def resume(request):

    certifications = Certification.objects.filter(
        is_published=True
    ).order_by(
        "display_order",
        "-issued_date"
    )

    return render(
        request,
        "site/resume.html",
        {
            "certifications": certifications,
        }
    )
    
# =========================================================
# CONTACT
# =========================================================

def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            attachment = form.cleaned_data.get("attachment")

            email_body = f"""
Name: {name}

Email: {email}

Subject: {subject}

Message:
{message}
"""

            try:

                # -------------------------------------------------
                # Resend API Key
                # -------------------------------------------------

                resend.api_key = settings.RESEND_API_KEY


                # -------------------------------------------------
                # Email Data
                # -------------------------------------------------

                email_data = {

                    "from": "onboarding@resend.dev",

                    "to": [
                        settings.CONTACT_EMAIL
                    ],

                    "subject": (
                        f"Portfolio Contact: {subject}"
                    ),

                    "text": email_body,

                    "reply_to": email,
                }


                # -------------------------------------------------
                # Optional Attachment
                # -------------------------------------------------

                if attachment:

                    file_content = base64.b64encode(
                        attachment.read()
                    ).decode("utf-8")


                    email_data["attachments"] = [

                        {
                            "filename": attachment.name,

                            "content": file_content,
                        }

                    ]


                # -------------------------------------------------
                # Send Email
                # -------------------------------------------------

                response = resend.Emails.send(
                    email_data
                )


              
              

            except Exception as error:

            
                messages.error(
                    request,
                    "Failed to send message. Please try again."
                )


            else:

                # -------------------------------------------------
                # User Success Message
                # -------------------------------------------------

                messages.success(
                    request,
                    "Your message has been sent successfully!"
                )


                # Reset Form

                form = ContactForm()


    else:

        form = ContactForm()


    # -------------------------------------------------------------
    # Render Contact Page
    # -------------------------------------------------------------

    return render(

        request,

        "site/contact.html",

        {
            "form": form,
        }

    )
# بخش پروژه‌ها و جزئیات پروژه‌ها

def projects(request):
    projects = Project.objects.filter(
        is_published=True
    ).order_by("-created_at")

    return render(
        request,
        "site/projects.html",
        {"projects": projects}
    )

def project_details(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    challenges = [
        challenge.strip()
        for challenge in project.detail.challenges.splitlines()
        if challenge.strip()
    ]

    project_videos = project.gallery_videos.filter(
        is_published=True
    ).order_by(
        "display_order",
        "-created_at"
    )

    return render(
        request,
        "site/project_details.html",
        {
            "project": project,
            "challenges": challenges,
            "project_videos": project_videos,
        }
    )