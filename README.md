# Rohullah Sadat Portfolio

Official personal portfolio website of **Rohullah Sadat** — Full Stack Developer, Author, and Future AI Entrepreneur.

🌐 **Live Website:** https://rohullahsadat.com
💻 **GitHub Repository:** https://github.com/rohullahsadat1997/rohullah-sadat-website

---

## 👋 About

This is my official personal portfolio website, created to showcase my professional journey, technical projects, articles, books, certifications, skills, and achievements.

The project started as a modern frontend portfolio and was later expanded into a **Django-powered dynamic website** with content management through the Django Admin panel.

The website is designed with a focus on:

* Professional personal branding
* Responsive and modern UI
* Persian/English bilingual content
* SEO-friendly structure
* Dynamic content management
* Project and portfolio presentation
* Scalable architecture for future improvements

---

## 🚀 Features

### Portfolio

* Personal introduction and professional profile
* Skills and technologies
* Project showcase
* Detailed project pages
* Certifications and achievements
* Resume section
* About and professional background

### Content Management

The website uses **Django Admin** to manage dynamic content without modifying HTML manually.

From the Admin panel, I can manage:

* Projects
* Project details
* Articles
* Books
* Gallery images
* Gallery videos
* Certifications
* Profile information

This makes it possible to continuously add new projects, articles, books, certificates, and other content as the portfolio grows.

### Media

The backend supports media uploads for:

* Project images
* Gallery images
* Book files
* Article media
* Certification files
* Other portfolio assets

Persistent storage is configured for the production environment so uploaded content can remain available across deployments.

### SEO

The project includes SEO-focused features such as:

* Semantic HTML
* Responsive structure
* Sitemap
* `robots.txt`
* SEO-friendly URLs
* Structured content
* Search-engine-friendly page organization

### UI & UX

* Responsive design
* Mobile-friendly navigation
* Dark mode
* Modern animations
* Clean typography
* Accessible navigation
* Bilingual Persian/English experience

---

## 🛠️ Technologies

### Frontend

* HTML5
* CSS3
* JavaScript
* Responsive Web Design

### Backend

* Python
* Django
* Django Templates
* Django Admin

### Database & Storage

* SQLite
* Railway Persistent Volume

### Deployment & Infrastructure

* Railway
* Cloudflare
* Cloudflare DNS
* HTTPS / SSL
* GitHub

---

## 🏗️ Architecture

The production architecture currently follows this structure:

```text
                    rohullahsadat.com
                           │
                       Cloudflare
                           │
                         Railway
                           │
                         Django
                      ┌────┴────┐
                      │         │
                   SQLite    Media Files
                      │         │
                      └────┬────┘
                           │
                    Railway Volume
```

The architecture is intentionally simple at the current stage so the project can remain cost-effective while still supporting dynamic content and future growth.

---

## 📁 Project Structure

```text
rohullah-sadat-website/
│
├── backend/
│   ├── manage.py
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   │
│   ├── core/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── sitemaps.py
│   │   ├── templates/
│   │   └── ...
│   │
│   ├── templates/
│   ├── static/
│   ├── staticfiles/
│   ├── media/
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   └── ...
│
└── README.md
```

> The project originally began as a frontend website and was later integrated with Django to support dynamic content and administration.

---

## 🌐 Deployment

The production version is deployed using **Railway** and connected to the custom domain:

**https://rohullahsadat.com**

Cloudflare is used for:

* DNS management
* Domain routing
* HTTPS/SSL
* CDN and proxy capabilities
* Redirect management

Railway is used for:

* Django application hosting
* Production deployment
* Persistent application storage
* Backend execution

---

## 🔐 Admin Panel

The website includes a Django Admin panel for managing the portfolio content.

Through the Admin panel, new content can be added without editing source code manually.

Examples:

```text
Project
Article
Book
Certification
Gallery Image
Gallery Video
Profile
```

This allows the portfolio to evolve from a static website into a continuously updated personal platform.

---

## 📚 Content

The portfolio is designed to grow over time.

Future content can include:

* New software projects
* Programming articles
* Technical tutorials
* Books and publications
* AI projects
* Data Science projects
* Certifications
* Research work
* Educational resources
* Professional achievements

---

## 🔮 Future Improvements

Planned improvements include:

* PostgreSQL database migration
* Cloud object storage for large media files
* Cloudflare R2 integration
* More advanced Django Admin features
* Improved search functionality
* Advanced analytics
* Additional educational content
* AI-powered features
* More interactive projects
* API development
* Improved multilingual support

The current architecture is designed so these improvements can be introduced gradually without rebuilding the entire project.

---

## 📈 Project Goals

The long-term goal of this project is to build more than a traditional portfolio.

It is intended to become a central professional platform where visitors can discover:

```text
My Projects
     ↓
My Skills
     ↓
My Articles
     ↓
My Books
     ↓
My Certifications
     ↓
My Research
     ↓
My Future AI & Software Projects
```

---

## 👨‍💻 Author

**Rohullah Sadat**

Full Stack Developer | Author | Future AI Entrepreneur

I am continuously building my skills and projects in:

* Web Development
* Python
* Django
* Artificial Intelligence
* Data Science
* SEO
* Software Engineering

---

## 📄 License

This project is a personal portfolio website.

The source code is publicly available for learning and reference, while personal content, branding, images, written materials, and other original assets remain the property of their respective owner.

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub.

Thank you for visiting my portfolio.
