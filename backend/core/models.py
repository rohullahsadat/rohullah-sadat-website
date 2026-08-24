from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# =========================================================
# PROJECT
# =========================================================

class Project(models.Model):

    CATEGORY_CHOICES = [
        ("frontend", _("Frontend Development")),
        ("backend", _("Backend Development")),
        ("fullstack", _("Full Stack Development")),
        ("python", _("Python")),
        ("django", _("Django")),
        ("ai", _("Artificial Intelligence")),
        ("other", _("Other")),
    ]

    LEVEL_CHOICES = [
        ("beginner", _("Beginner")),
        ("intermediate", _("Intermediate")),
        ("advanced", _("Advanced")),
    ]

    STATUS_CHOICES = [
        ("completed", _("Completed")),
        ("in_progress", _("In Progress")),
        ("planned", _("Planned")),
    ]

    # -----------------------------------------------------
    # Basic Information
    # -----------------------------------------------------

    title = models.CharField(
        max_length=200
    )

    title_fa = models.CharField(
        max_length=200,
        blank=True
    )

    description = models.TextField()

    description_fa = models.TextField(
        blank=True
    )

    # -----------------------------------------------------
    # Image
    # -----------------------------------------------------

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    # -----------------------------------------------------
    # Category
    # -----------------------------------------------------

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="other"
    )

    # -----------------------------------------------------
    # Level
    # -----------------------------------------------------

    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default="beginner"
    )

    # -----------------------------------------------------
    # Technologies
    # -----------------------------------------------------

    technologies = models.CharField(
        max_length=500,
        help_text=_(
            "Separate technologies with commas."
        )
    )

    # -----------------------------------------------------
    # Project Information
    # -----------------------------------------------------

    year = models.PositiveIntegerField(
        default=2026
    )

    duration = models.CharField(
        max_length=100,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="completed"
    )

    # -----------------------------------------------------
    # Links
    # -----------------------------------------------------

    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    # -----------------------------------------------------
    # Publishing
    # -----------------------------------------------------

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    # -----------------------------------------------------
    # Timestamps
    # -----------------------------------------------------

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # -----------------------------------------------------
    # Technology List
    # -----------------------------------------------------

    @property
    def technology_list(self):
        return [
            tech.strip()
            for tech in self.technologies.split(",")
            if tech.strip()
        ]

    # -----------------------------------------------------
    # String
    # -----------------------------------------------------

    def __str__(self):
        return self.title


# =========================================================
# PROJECT DETAIL
# =========================================================

class ProjectDetail(models.Model):

    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name="detail"
    )

    # -----------------------------------------------------
    # Overview
    # -----------------------------------------------------

    overview = models.TextField(
        blank=True
    )

    overview_fa = models.TextField(
        blank=True
    )

    # -----------------------------------------------------
    # Role
    # -----------------------------------------------------

    role = models.CharField(
        max_length=200,
        blank=True
    )

    role_fa = models.CharField(
        max_length=200,
        blank=True
    )

    # -----------------------------------------------------
    # Features
    # -----------------------------------------------------

    features = models.TextField(
        blank=True,
        help_text=_(
            "Write each feature on a new line."
        )
    )

    features_fa = models.TextField(
        blank=True,
        help_text=_(
            "Write each feature in Persian, one per line."
        )
    )

    # -----------------------------------------------------
    # Challenges
    # -----------------------------------------------------

    challenges = models.TextField(
        blank=True
    )

    challenges_fa = models.TextField(
        blank=True
    )

    # -----------------------------------------------------
    # What I Learned
    # -----------------------------------------------------

    what_i_learned = models.TextField(
        blank=True
    )

    what_i_learned_fa = models.TextField(
        blank=True
    )

    # -----------------------------------------------------
    # Future Improvements
    # -----------------------------------------------------

    future_improvements = models.TextField(
        blank=True
    )

    future_improvements_fa = models.TextField(
        blank=True
    )

    # -----------------------------------------------------
    # Timestamps
    # -----------------------------------------------------

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # -----------------------------------------------------
    # String
    # -----------------------------------------------------

    def __str__(self):
        return f"Details - {self.project.title}"


# =========================================================
# CREATE PROJECT DETAIL AUTOMATICALLY
# =========================================================

@receiver(post_save, sender=Project)
def create_project_detail(
    sender,
    instance,
    created,
    **kwargs
):

    if created:
        ProjectDetail.objects.create(
            project=instance
        )


# =========================================================
# ABOUT SECTION
# =========================================================

class AboutProfile(models.Model):

    name = models.CharField(
        max_length=100
    )

    professional_title = models.CharField(
        max_length=200
    )

    image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True
    )

    introduction = models.TextField()

    mission = models.TextField()

    vision = models.TextField()

    values = models.TextField()

    def __str__(self):
        return self.name


# =========================================================
# BOOK SECTION
# =========================================================

class Book(models.Model):

    CATEGORY_CHOICES = [
        ("programming", _("Programming")),
        ("technology", _("Technology")),
        ("business", _("Business")),
        (
            "personal_development",
            _("Personal Development")
        ),
        ("fiction", _("Fiction")),
        ("other", _("Other")),
    ]

    STATUS_CHOICES = [
        ("published", _("Published")),
        ("reading", _("Currently Reading")),
        ("planned", _("Planned")),
        ("coming_soon", _("Coming Soon")),
    ]

    ACCESS_CHOICES = [
        ("free", _("Free")),
        ("paid", _("Paid")),
    ]

    title = models.CharField(
        max_length=200
    )

    author = models.CharField(
        max_length=200,
        blank=True
    )

    cover = models.ImageField(
        upload_to="books/covers/",
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="other"
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="planned"
    )

    access_type = models.CharField(
        max_length=10,
        choices=ACCESS_CHOICES,
        default="free"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    currency = models.CharField(
        max_length=10,
        default="USD"
    )

    pdf_file = models.FileField(
        upload_to="books/pdfs/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    is_favorite = models.BooleanField(
        default=False
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title


# =========================================================
# ARTICLE SECTION
# =========================================================

class Article(models.Model):

    CATEGORY_CHOICES = [
        ("programming", _("Programming")),
        ("web_development", _("Web Development")),
        ("python", _("Python")),
        ("django", _("Django")),
        ("javascript", _("JavaScript")),
        ("ai", _("Artificial Intelligence")),
        ("technology", _("Technology")),
        ("career", _("Career")),
        ("other", _("Other")),
    ]

    title = models.CharField(
        max_length=250
    )

    slug = models.SlugField(
        max_length=250,
        unique=True,
        blank=True
    )

    author = models.CharField(
        max_length=200,
        default="Rohullah Sadat"
    )

    cover = models.ImageField(
        upload_to="articles/covers/",
        blank=True,
        null=True
    )

    excerpt = models.TextField(
        blank=True
    )

    content = models.TextField(
        blank=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="other"
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(
                self.title,
                allow_unicode=True
            )

        super().save(*args, **kwargs)


# =========================================================
# GALLERY IMAGE
# =========================================================

class GalleryImage(models.Model):

    CATEGORY_CHOICES = [
        ("personal", _("Personal")),
        ("projects", _("Projects")),
        ("events", _("Events")),
        ("programming", _("Programming")),
        ("education", _("Education")),
        ("technology", _("Technology")),
        ("other", _("Other")),
        ("certificates", _("Certificates")),
    ]

    title = models.CharField(
        max_length=250,
        blank=True
    )

    image = models.ImageField(
        upload_to="gallery/"
    )

    description = models.TextField(
        blank=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="other"
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title or f"Gallery Image {self.id}"


# =========================================================
# GALLERY VIDEO
# =========================================================

class GalleryVideo(models.Model):

    CATEGORY_CHOICES = [
        ("programming", _("Programming")),
        ("projects", _("Projects")),
        ("education", _("Education")),
        ("technology", _("Technology")),
        ("events", _("Events")),
        ("other", _("Other")),
    ]

    title = models.CharField(
        max_length=250,
        blank=True
    )

    video = models.FileField(
        upload_to="gallery/videos/"
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="gallery_videos"
    )

    description = models.TextField(
        blank=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="other"
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title or f"Gallery Video {self.id}"


# =========================================================
# CERTIFICATION
# =========================================================

class Certification(models.Model):

    title = models.CharField(
        max_length=250
    )

    organization = models.CharField(
        max_length=200
    )

    platform = models.CharField(
        max_length=100,
        blank=True
    )

    issued_date = models.DateField(
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True
    )

    gallery_image = models.ForeignKey(
        GalleryImage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="certifications"
    )

    pdf = models.FileField(
        upload_to="certifications/",
        blank=True,
        null=True
    )

    verification_url = models.URLField(
        blank=True
    )

    is_published = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title