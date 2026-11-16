# MMIT Library Portal: Comprehensive Redesign Plan

## 1. Project Vision

Transform the grassroots Blogger site (`librarymmit.blogspot.com`) into an institutional-grade, modern, secure, and fully self-contained Web Portal using **Python 3.12+ and Django 5.x**.

The new portal will serve three distinct user audiences:
1. **Diploma Students:** Instant mobile-friendly OPAC search, syllabus downloads, previous year question paper archives, lecture notes, membership registration, and notice updates.
2. **Faculty Members:** Course reading lists, book recommendation requests, resource uploads, and academic portal shortcuts.
3. **Library Staff (Librarians & Admins):** Intuitive web-based cataloguing, copy/accession tracking, notice management, service request triage, CSV inventory imports, and site configuration without writing code.

---

## 2. Design System & Tokens

### Color Palette
- **Primary Navy:** `#102A43` (Header, Primary CTAs, Dark Text Accents)
- **Primary Navy Hover:** `#0B1D30`
- **Secondary Teal:** `#0F766E` (Badges, Active Tabs, Secondary Buttons)
- **Teal Accent Light:** `#CCFBF1`
- **Academic Gold:** `#D6A443` (Accents, Stars, Highlights, Institutional Seals)
- **Background:** `#F8FAFC` (Slate neutral background)
- **Surface / Card:** `#FFFFFF` (Clean elevated containers)
- **Text Main:** `#0F172A` (Slate 900)
- **Text Muted:** `#475569` (Slate 600)
- **Border / Divider:** `#E2E8F0` (Slate 200)

### Typography
- **Headings & English Body:** `Inter`, `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `sans-serif`
- **Hindi / Devanagari Scripts:** `Noto Sans Devanagari`, `system-ui`, `sans-serif`
- **Monospace (Acc. Nos, ISBN):** `SFMono-Regular`, `Menlo`, `Monaco`, `Consolas`, monospace

---

## 3. Django Modular Application Architecture

The project will be organized under the modular `apps/` directory with clear domain separation:

```text
Library/
├── manage.py
├── requirements.txt
├── .env.example
├── README.md
├── college_library/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── core/               # SiteSettings, Home view, Search dispatcher, Menu system
│   ├── accounts/           # Custom User model / Staff profile, Role-based auth
│   ├── catalog/            # Book, BookCopy, Subject, Category, OPAC views, CSV import/export
│   ├── resources/          # DigitalResource, QuestionPaper, Syllabus, LectureNote
│   ├── departments/        # Department, DepartmentDetail, Semester curriculum
│   ├── notices/            # Notice, Circulars, Priority banners
│   ├── library_services/   # Membership, BookRecommendation, ResourceRequest, NoDues
│   ├── events/             # LibraryEvent, GalleryImage, Orientation posts
│   ├── pages/              # About, Vision/Mission, Rules, Facilities, FAQ, Staff
│   ├── feedback/           # Feedback submission, ratings, review status
│   └── dashboard/          # Custom Librarian Dashboard & analytics
├── templates/
│   ├── base.html
│   ├── includes/           # navbar.html, footer.html, breadcrumbs.html, alerts.html
│   ├── core/
│   ├── catalog/
│   ├── resources/
│   ├── departments/
│   ├── notices/
│   ├── services/
│   ├── events/
│   ├── pages/
│   ├── feedback/
│   ├── accounts/
│   └── dashboard/
├── static/
│   ├── css/                # main.css, dashboard.css, print.css
│   ├── js/                 # main.js, search.js, dashboard.js
│   └── images/             # logo, hero, placeholders, default book covers
├── media/                  # uploads for books, notices, attachments, resources
├── tests/                  # unit and integration test suite
└── docs/                   # audit, architecture, sitemap, manuals
```

---

## 4. Database Schema Strategy

1. **`core.SiteSettings`**: College name, library title, affiliation (`BTEUP`), address, contact numbers, email, principal email, operating hours, social links, logo, favicon.
2. **`core.MenuItem`**: Hierarchical navigation items with label, URL/path, parent, display order, is_active, requires_auth.
3. **`catalog.Category` & `catalog.Subject`**: Classification for books and resources.
4. **`catalog.Book`**: Title, subtitle, author, ISBN, publisher, edition, publication year, department, subject, description, cover image, classification code.
5. **`catalog.BookCopy`**: Accession number (unique), book FK, shelf/rack location, acquisition date, status (`AVAILABLE`, `ISSUED`, `REFERENCE_ONLY`, `LOST`, `REPAIR`).
6. **`departments.Department`**: Branch name, code (`CSE`, `CIVIL`, `ECE`, `EE`, `ASH`), slug, description, image, order, is_active.
7. **`resources.DigitalResource`**: Title, description, category (`QUESTION_PAPER`, `SYLLABUS`, `NOTES`, `EBOOK`, `JOURNAL`), department, semester (`1` to `6`), subject, academic year, file upload, external link, access level (`PUBLIC`, `STUDENT_ONLY`).
8. **`notices.Notice`**: Title, slug, description, category, priority (`LOW`, `NORMAL`, `HIGH`, `URGENT`), attachment (PDF), publish date, expiration date, is_active.
9. **`library_services.MembershipApplication`**: Student name, roll number, department, semester, mobile, email, id proof, status (`PENDING`, `APPROVED`, `REJECTED`).
10. **`library_services.BookRecommendation`**: Title, author, publisher, recommended by (student/faculty), department, reason, status.
11. **`library_services.ResourceRequest`**: Resource title, details, requester name, roll/staff id, department, status, librarian note.
12. **`feedback.Feedback`**: Name, email, category, rating, message, status (`NEW`, `REVIEWED`).
13. **`events.LibraryEvent` & `events.GalleryImage`**: Orientation sessions, book fairs, workshop events, gallery photos.

---

## 5. Security and Quality Assurance Plan

- Django 5.x CSRF protection on all forms.
- Role-based permissions:
  - Superuser: full system settings and staff administration.
  - Librarian: cataloguing, inventory, copy management, resource uploads, notices, request approvals.
  - Public / Student: read access to catalogue, digital resources, notices, submission of request forms.
- File upload sanitization: strict mime-type check, extension validation (PDF, JPG, PNG, WEBP), file size limits (max 15MB).
- Production deployment configuration: `DEBUG=False`, secure cookies, HTTPS redirection, Nginx reverse proxy configuration, systemd service unit.
- Full test suite covering models, views, forms, authentication, OPAC search, and permissions.

