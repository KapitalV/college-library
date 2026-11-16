# Government Polytechnic Madhogarh Library Portal: Reference & Modernized Sitemap

This document maps the original reference navigation paths from the Blogger website to the modernized, unified Django web application architecture customized for **Government Polytechnic Madhogarh**, Kailor, District Jalaun, Uttar Pradesh (Institution Code: **3318**).

---

## 1. Reference Site URL Mapping

| Reference Section / Title | Reference URL / Target | Status on Blogger | Modernized Django Route | Django App / View |
|---|---|---|---|---|
| **Homepage** | `https://librarymmit.blogspot.com/` | Active Blog Feed | `/` | `apps.core:home` |
| **College Website** | `http://bteup.ac.in` | External Link | Configurable Link in Topbar | `SiteSettings.college_website_url` |
| **About Library** | `/p/about-library.html` | Static Blogger Page | `/about/` | `apps.pages:about` |
| **Vision & Mission** | Embedded in About | Text snippet | `/about/vision-mission/` | `apps.pages:vision_mission` |
| **Rules & Regulations** | `/p/rules-regulations.html` | Static Blogger Page | `/rules/` | `apps.pages:rules` |
| **Library Services** | `/p/library-services.html` | Static Blogger Page | `/services/` | `apps.library_services:service_list` |
| **Library Facilities** | Embedded in About/Services | Fragment | `/facilities/` | `apps.pages:facilities` |
| **Library Staff & Committee** | Mentioned in Donation Post | Blog text | `/staff/` | `apps.pages:staff` |
| **OPAC Catalogue Search** | Google Apps Script URL | External Script | `/catalog/` | `apps.catalog:catalog_search` |
| **Book Detail View** | None (Raw Google Sheet) | Missing | `/catalog/<slug:slug>/` | `apps.catalog:book_detail` |
| **New Arrivals** | Blogger Widget Post | Fragment | `/catalog/new-arrivals/` | `apps.catalog:new_arrivals` |
| **Digital Library** | `/p/digital-library.html` | HTTP 404 (Broken) | `/digital-library/` | `apps.resources:digital_library` |
| **External Portals (NDLI, Swayam, e-KUMBH)** | In navigation and widgets | External Links | `/digital-library/portals/` | `apps.resources:digital_portals` |
| **NDLI Club Registration** | Modal / External link | Inline script | `/services/ndli-club/` | `apps.library_services:ndli_club` |
| **Question Papers** | Google Drive URL | External folder | `/resources/question-papers/` | `apps.resources:question_papers` |
| **Syllabus** | BTEUP Webapp URL | External site | `/resources/syllabus/` | `apps.resources:syllabus` |
| **Faculty Notes & PPTs** | `#` (Empty Link) | Dead link | `/resources/lecture-notes/` | `apps.resources:lecture_notes` |
| **Department Resources** | None (Unorganized) | Missing | `/departments/` & `/departments/<slug>/` | `apps.departments:department_detail` |
| **Photo Gallery** | `/2026/07/photo-gallery.html` | HTTP 404 (Broken) | `/gallery/` & `/events/` | `apps.events:gallery_list` |
| **Orientation 2026-27 Post** | `/2026/08/welcome-...` | Blog Post | `/events/orientation-2026/` | `apps.events:event_detail` |
| **Student's Guide to Library** | `/2026/10/a-students-...` | Blog Post | `/notices/students-guide/` | `apps.notices:notice_detail` |
| **Library Notices** | Mixed in Blog Feed | Feed items | `/notices/` | `apps.notices:notice_list` |
| **Library Membership** | Google Form link | External Form | `/services/membership/` | `apps.library_services:membership_apply` |
| **Book Recommendation** | Not present | Missing | `/services/book-recommendation/` | `apps.library_services:book_recommend` |
| **Resource Request** | Not present | Missing | `/services/resource-request/` | `apps.library_services:resource_request` |
| **Contact Us** | `#contact-section` | In-page bookmark | `/contact/` | `apps.core:contact` |
| **Feedback Form** | None | Missing | `/feedback/` | `apps.feedback:feedback_form` |
| **FAQ Page** | None | Missing | `/faq/` | `apps.pages:faq` |
| **Staff Login** | None | Missing | `/accounts/login/` | `apps.accounts:login` |
| **Librarian Dashboard** | None (Blogger Dashboard) | Third-party | `/dashboard/` | `apps.dashboard:overview` |

---

## 2. Information Architecture Hierarchy (Django Application)

```text
[INSTITUTIONAL PORTAL ROOT: /]
│
├── [HOME] (/)
│   ├── Hero & Live Catalogue Search
│   ├── Quick Access Action Tiles
│   ├── Latest Notices & Circulars (with PDF downloads)
│   ├── Digital Library Access Portals (NDLI, e-Granthalaya, e-KUMBH, Swayam)
│   ├── Department Resource Portals
│   ├── New Arrivals & Recent Acquisitions
│   ├── Library At A Glance (Real-time live statistics)
│   └── Facilities & Quick Help
│
├── [ABOUT LIBRARY] (/about/)
│   ├── Overview & Infrastructure (/about/)
│   ├── Vision, Mission & Goals (/about/vision-mission/)
│   ├── Library Rules & Circulation Policy (/rules/)
│   ├── Staff & Advisory Committee (/staff/)
│   ├── Facilities & Reading Hall (/facilities/)
│   └── FAQ & Student Guide (/faq/)
│
├── [LIBRARY CATALOGUE - OPAC] (/catalog/)
│   ├── Live Search & Multi-filter Engine (Title, Author, Subject, Department, ISBN)
│   ├── Book Details & Copy Availability (/catalog/<slug>/)
│   ├── New Arrivals Section (/catalog/new-arrivals/)
│   └── Subject / Department Browsing
│
├── [DIGITAL LIBRARY & OER] (/digital-library/)
│   ├── Verified National Portals (NDLI, e-KUMBH, NPTEL, SWAYAM, DOAJ)
│   ├── E-Books Directory (/digital-library/ebooks/)
│   ├── E-Journals & Magazines (/digital-library/journals/)
│   └── NDLI Club Information & Registration Guide (/services/ndli-club/)
│
├── [ACADEMIC RESOURCES] (/resources/)
│   ├── Department Directory (/departments/)
│   │   ├── Computer Science and Engineering (Branch 355 / Lateral 389) (/departments/computer-science-engineering/)
│   │   ├── Electrical Engineering (Branch 328 / Lateral 378) (/departments/electrical-engineering/)
│   │   └── Electronics Engineering (Branch 330 / Lateral 380) (/departments/electronics-engineering/)
│   ├── Previous Year BTEUP Question Papers (/resources/question-papers/)
│   ├── BTEUP Diploma Curriculum & Syllabus (/resources/syllabus/)
│   └── Faculty Lecture Notes & Handouts (/resources/lecture-notes/)
│
├── [LIBRARY SERVICES] (/services/)
│   ├── Service Overview & Circulation Terms (/services/)
│   ├── Apply for Library Membership (Validated Django Form) (/services/membership/)
│   ├── Recommend a Book (/services/book-recommendation/)
│   ├── Request a Digital / Physical Resource (/services/resource-request/)
│   ├── Clearance & No-Dues Instructions (/services/no-dues/)
│   └── Downloadable Library Forms (/services/forms/)
│
├── [NEWS, EVENTS & NOTICES] (/notices/)
│   ├── Active Library Notices & Circulars (/notices/)
│   ├── Notice Detail with Attachments (/notices/<slug>/)
│   ├── Library Orientation & Events (/events/)
│   └── Campus & Library Photo Gallery (/gallery/)
│
├── [HELP & CONTACT] (/contact/)
│   ├── Contact Librarian & Location Map (/contact/)
│   ├── Student & Faculty Feedback (/feedback/)
│   └── Frequently Asked Questions (/faq/)
│
└── [STAFF & MANAGEMENT PORTAL] (/dashboard/)
    ├── Secure Authentication (/accounts/login/)
    ├── Librarian Executive Dashboard (/dashboard/)
    ├── Book & Inventory Management (CRUD, Copies, CSV Import/Export)
    ├── Digital Resources Management (Uploads, Categorization)
    ├── Notices & Circulars Management
    ├── Service Requests & Feedback Review
    └── Site Settings & Menu Configuration
```

