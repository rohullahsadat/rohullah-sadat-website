from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
class Project(models.Model):

    CATEGORY_CHOICES = [
        ("frontend", "Frontend Development"),
        ("backend", "Backend Development"),
        ("fullstack", "Full Stack Development"),
        ("python", "Python"),
        ("django", "Django"),
        ("ai", "Artificial Intelligence"),
        ("other", "Other"),
    ]

    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    STATUS_CHOICES = [
        ("completed", "Completed"),
        ("in_progress", "In Progress"),
        ("planned", "Planned"),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="other"
    )

    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default="beginner"
    )

    technologies = models.CharField(
        max_length=500,
        help_text="Separate technologies with commas."
    )

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

    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    @property
    def technology_list(self):
        return [
            tech.strip()
            for tech in self.technologies.split(",")
            if tech.strip()
        ]

    def __str__(self):
        return self.title


class ProjectDetail(models.Model):

    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name="detail"
    )

    overview = models.TextField(blank=True)

    role = models.CharField(
        max_length=200,
        blank=True
    )

    features = models.TextField(
        blank=True,
        help_text="Write each feature on a new line."
    )

    challenges = models.TextField(
        blank=True
    )

    what_i_learned = models.TextField(
        blank=True
    )

    future_improvements = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Details - {self.project.title}"
    



    @receiver(post_save, sender=Project)
    def create_project_detail(sender, instance, created, **kwargs):
     if created:
        ProjectDetail.objects.create(project=instance)
        
# About Section 

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
    
# Book Section

class Book(models.Model):

    CATEGORY_CHOICES = [
        ("programming", "Programming"),
        ("technology", "Technology"),
        ("business", "Business"),
        ("personal_development", "Personal Development"),
        ("fiction", "Fiction"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("published", "Published"),
        ("reading", "Currently Reading"),
        ("planned", "Planned"),
        ("coming_soon", "Coming Soon"),
    ]

    ACCESS_CHOICES = [
        ("free", "Free"),
        ("paid", "Paid"),
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
    
# article section
class Article(models.Model):

    CATEGORY_CHOICES = [
        ("programming", "Programming"),
        ("web_development", "Web Development"),
        ("python", "Python"),
        ("django", "Django"),
        ("javascript", "JavaScript"),
        ("ai", "Artificial Intelligence"),
        ("technology", "Technology"),
        ("career", "Career"),
        ("other", "Other"),
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
        
        # =========================
# Gallery Section
# =========================

class GalleryImage(models.Model):

    CATEGORY_CHOICES = [
        ("personal", "Personal"),
        ("projects", "Projects"),
        ("events", "Events"),
        ("programming", "Programming"),
        ("education", "Education"),
        ("technology", "Technology"),
        ("other", "Other"),
        ("certificates", "Certificates"),
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
    
    # video
class GalleryVideo(models.Model):

    CATEGORY_CHOICES = [
        ("programming", "Programming"),
        ("projects", "Projects"),
        ("education", "Education"),
        ("technology", "Technology"),
        ("events", "Events"),
        ("other", "Other"),
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
    
    #resuem section
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