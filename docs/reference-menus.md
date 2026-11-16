# Reference Website Menus and Navigation Audit

## 1. Reference Website Navigation Tree (Blogger)

On `librarymmit.blogspot.com`, the navigation bar was defined statically within the blog template:

```text
├── HOME (/)
├── COLLEGE WEBSITE (http://bteup.ac.in)
├── MMIT LIBRARY 🔽 (#)
│   ├── About Library (/p/about-library.html)
│   ├── Rules & Regulations (/p/rules-regulations.html)
│   └── Library Services (/p/library-services.html)
├── DIGITAL LIBRARY 🔽 (#)
│   ├── e-Granthalaya (EG4) (http://eg4.nic.in/)
│   ├── National Digital Library (https://ndl.iitkgp.ac.in/)
│   ├── SWAYAM / NPTEL (https://swayam.gov.in/)
│   └── e-KUMBH Portal (https://ekumbh.aicte-india.org/)
├── QUESTION PAPERS (Google Drive folder link)
├── SYLLABUS (https://bteup.ac.in/webapp/SYLLABUS.aspx?type=19)
├── E-LEARNING CORNER 🔽 (#)
│   ├── Faculty PPTs & Notes (# - dead link)
│   ├── Video Lectures (# - dead link)
│   └── E-Books & Study Material (# - dead link)
├── PHOTO GALLERY (/2026/07/photo-gallery.html - 404 broken)
└── CONTACT US (#contact-section)
```

### Additional Floating / Sidebar Links
- 📝 Apply for Library Membership (Google Form: `https://forms.gle/wXdbRSzHQgPoT82s8`)
- 🌐 NDLI Club Membership Registration (JavaScript Modal linking to `https://ndl.iitkgp.ac.in/account/registration` and `https://club.ndl.iitkgp.ac.in/sign-up`)
- 🔍 Search Library Catalogue (OPAC) (External Google Apps Script endpoint)
- 📚 Digital Library (Broken Blogger page `/p/digital-library.html` - 404)

---

## 2. Issues with Reference Navigation

1. **Broken/Dead Links:** 
   - `Faculty PPTs & Notes`, `Video Lectures`, and `E-Books & Study Material` all had `href="#"`.
   - `/p/digital-library.html` and `/2026/07/photo-gallery.html` were 404 dead endpoints.
2. **External Traps:**
   - Clicking OPAC search or question papers immediately leaves the institutional domain, breaking user trust and losing analytics.
3. **No Database Control:**
   - Nav items were hardcoded in HTML. Adding or removing a menu item required editing raw Blogger XML templates.
4. **Poor Mobile Usability:**
   - Dropdown menus on mobile did not collapse into an accessible accordion or offcanvas drawer, leading to accidental clicks and truncated menu labels.
5. **Lack of Breadcrumbs:**
   - Deep pages did not indicate navigational context or parent category.

---

## 3. Modernized Dynamic Institutional Menu Architecture

The new Django platform implements a database-driven `MenuItem` model hierarchy (`core.MenuItem`) with support for parent-child mega menus, order sorting, active state indicators, role visibility, and accessibility attributes (`aria-expanded`, `aria-haspopup`).

### Complete Django Menu Hierarchy

```text
[TOP UTILITY BAR]
├── College Portal: BTEUP (External Safe Link)
├── Hours: Mon-Sat 10:00 AM - 5:00 PM
├── Phone: +91-9450342615 | Email: ppl.mmitmati@gmail.com
├── Hindi / English Quick Toggle
└── Staff Portal / Login (/accounts/login/)

[PRIMARY MAIN NAVIGATION]
├── 1. HOME (/): Gateway, live catalogue search, statistics, quick cards.
│
├── 2. ABOUT LIBRARY (/about/) [Dropdown]
│   ├── Library Overview & Infrastructure (/about/)
│   ├── Vision & Mission (/about/vision-mission/)
│   ├── Rules & Regulations (/rules/)
│   ├── Library Staff & Committee (/staff/)
│   ├── Facilities & Reading Hall (/facilities/)
│   └── Frequently Asked Questions (/faq/)
│
├── 3. LIBRARY CATALOGUE (/catalog/) [Dropdown]
│   ├── Search Catalogue (OPAC) (/catalog/)
│   ├── New Arrivals (/catalog/new-arrivals/)
│   ├── Books by Department (/departments/)
│   └── Book Donation Records (/catalog/donations/)
│
├── 4. DIGITAL LIBRARY (/digital-library/) [Dropdown]
│   ├── Digital Portal Directory (/digital-library/)
│   ├── National Digital Library (NDLI) Info & Club (/services/ndli-club/)
│   ├── AICTE e-KUMBH Portal (/digital-library/ekumbh/)
│   ├── SWAYAM / NPTEL MOOCs (/digital-library/swayam/)
│   └── Open Access Journals & Books (/digital-library/open-access/)
│
├── 5. ACADEMIC RESOURCES (/resources/) [Mega Menu]
│   ├── Department Hubs:
│   │   ├── Computer Science & Engineering (/departments/cse/)
│   │   ├── Civil Engineering (/departments/civil/)
│   │   ├── Electronics Engineering (/departments/ece/)
│   │   └── Applied Sciences & Humanities (/departments/ash/)
│   └── Resource Categories:
│       ├── BTEUP Question Papers (/resources/question-papers/)
│       ├── Diploma Syllabus & Curriculum (/resources/syllabus/)
│       └── Faculty Notes & PPTs (/resources/lecture-notes/)
│
├── 6. LIBRARY SERVICES (/services/) [Dropdown]
│   ├── Services & Borrowing Rules (/services/)
│   ├── Apply for Membership (/services/membership/)
│   ├── Recommend a Book (/services/book-recommendation/)
│   ├── Request a Resource (/services/resource-request/)
│   ├── Library Clearance (No-Dues) (/services/no-dues/)
│   └── Downloadable Forms (/services/forms/)
│
├── 7. NOTICES & EVENTS (/notices/) [Dropdown]
│   ├── Latest Notices & Circulars (/notices/)
│   ├── Orientation & Events (/events/)
│   └── Library Photo Gallery (/gallery/)
│
└── 8. CONTACT & HELP (/contact/)
    ├── Contact Librarian & Location (/contact/)
    └── Student Feedback (/feedback/)
```

