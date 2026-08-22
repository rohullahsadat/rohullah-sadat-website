from django.contrib import admin
from .models import Project, ProjectDetail, AboutProfile, Book, Article, GalleryImage,   GalleryVideo,Certification


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "level",
        "status",
        "year",
        "is_featured",
        "is_published",
    )

    list_filter = (
        "category",
        "level",
        "status",
        "is_featured",
        "is_published",
        "year",
    )

    search_fields = (
        "title",
        "description",
        "technologies",
    )

    list_editable = (
        "status",
        "is_featured",
        "is_published",
    )

    ordering = (
        "-created_at",
    )


@admin.register(ProjectDetail)
class ProjectDetailAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "role",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "project__title",
        "overview",
        "role",
        "features",
        "challenges",
        "what_i_learned",
    )

    ordering = (
        "-updated_at",
    )
    
#About Section
@admin.register(AboutProfile)
class AboutProfileAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "professional_title",
    )

    search_fields = (
        "name",
        "professional_title",
    )
    
# Book Section
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "category",
        "status",
        "access_type",
        "price",
        "is_featured",
        "is_favorite",
        "is_published",
        "display_order",
    )

    list_filter = (
        "category",
        "status",
        "access_type",
        "is_featured",
        "is_favorite",
        "is_published",
    )

    search_fields = (
        "title",
        "author",
        "description",
    )

    ordering = (
        "display_order",
        "-created_at",
    )
    
    #Article Section
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "category",
        "is_featured",
        "is_published",
        "published_at",
        "display_order",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "author",
        "excerpt",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "display_order",
        "-published_at",
        "-created_at",
    )
    
    # =========================
# Gallery Section
# =========================

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "is_featured",
        "is_published",
        "display_order",
        "created_at",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "display_order",
        "-created_at",
    )
    
@admin.register(GalleryVideo)
class GalleryVideoAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "project",
        "category",
        "is_featured",
        "is_published",
        "display_order",
        "created_at",
    )

    list_filter = (
        "project",
        "category",
        "is_featured",
        "is_published",
    )

    search_fields = (
        "title",
        "description",
        "project__title",
    )

    ordering = (
        "display_order",
        "-created_at",
    )
    
    #resuem section
@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "organization",
        "platform",
        "issued_date",
        "is_published",
        "display_order",
    )

    list_filter = (
        "organization",
        "platform",
        "is_published",
    )

    search_fields = (
        "title",
        "organization",
        "platform",
    )

    ordering = (
        "display_order",
        "-issued_date",
    )