# GOVERNMENT POLYTECHNIC MADHOGARH LIBRARY
## Central Library & Digital Resource Portal

**Institution:** Government Polytechnic Madhogarh, Kailor, District Jalaun, Uttar Pradesh – 285126, India  
**Institution Code:** 3318  
**Governing Authority:** Board of Technical Education Uttar Pradesh (BTEUP), Lucknow & AICTE, New Delhi  
**Official College Portal:** https://gpmadhogarh.ac.in/  
**Official URISE Profile:** https://urise.up.gov.in/poly/3318  
**College Library ERP:** https://erp.bizby.io/  
**Framework:** Python 3.12+ / Django 5.x & 6.x / Bootstrap 5.3 / PostgreSQL & SQLite  

---

## 1. Project Overview & Institutional Mission

This project is a complete, professional, production-ready **College Institutional Library Management and Digital Resource Portal** built with Python and Django for **Government Polytechnic Madhogarh**, Jalaun, Uttar Pradesh.

It modernizes the reference library design patterns of `librarymmit.blogspot.com`, replacing fragmented external Google Drive folders, Google Sheet scripts, and static blog posts with a unified, high-performance, and secure institutional web application mapped strictly to BTEUP curricula and AICTE standards.

### Three Verified Active Engineering Departments (Exclusively Approved)
As verified from official institutional records (`gpmadhogarh.ac.in` and URISE code `3318`), the institution actively runs **three diploma branches**:
1. **Computer Science and Engineering** (Branch Code: **355** | Lateral Entry Code: **389**)
2. **Electrical Engineering** (Branch Code: **328** | Lateral Entry Code: **378**)
3. **Electronics Engineering** (Branch Code: **330** | Lateral Entry Code: **380**)
*(Non-authorized departments such as Civil or Mechanical are deactivated and excluded from active public listings).*

---

## 2. Reference Comparison Matrix

| Feature / Dimension | Reference Blogger Site (`librarymmit.blogspot.com`) | New Institutional Django Web Application |
|---|---|---|
| **Architecture** | Free Blogger platform with fragmented external links | Monolithic Django 5.2/6.0 architecture with relational SQLite / PostgreSQL |
| **Institutional Branding** | Generic Blogger title bar with standard third-party theme | Custom academic brand header, AICTE approval, BTEUP affiliation, Jalaun location, Inst. Code 3318 |
| **External ERP Integration**| None | Direct integration with College Library ERP (`erp.bizby.io`) |
| **Catalogue Search (OPAC)** | External Google Apps Script modal redirecting to Google Sheets | Native in-house database OPAC with multi-field search (Title, Author, ISBN, Dept, Category, Accession) |
| **Physical Inventory** | No physical copy or rack tracking | `BookCopy` model tracking unique accession numbers (`GPM-B-xxxxx`), rack/shelf locations, and live availability |
| **Question Papers** | Uncurated Google Drive folder link | Structured BTEUP Previous Year Papers organized by branch, semester (1–6), and academic year with download counters |
| **Syllabus & Notes** | Broken dead links (`#`) or external portals | Dedicated department-wise repositories for BTEUP curricula, faculty PPTs, and chapter handouts |
| **Membership Form** | External Google Forms (`forms.gle/...`) | Validated Django ModelForm with enrollment verification, ID card upload, and librarian approval workflow |
| **Staff Administration** | Generic Blogger post editor; no role permissions | Custom Librarian Administration Dashboard + Django Admin with role-based security (`Librarian`, `Editor`, `Admin`) |
| **Notices & Orders** | Mixed in chronological blog feed | Categorized notices with priority badges (`URGENT`, `HIGH`), pinned announcement ticker, and PDF circular attachments |
| **Mobile UX / UI** | Horizontally clipping tables, uncollapsible menus | Mobile-first Bootstrap 5.3 + custom academic design tokens (`#102A43`, `#0F766E`, `#D6A443`) |
| **Data Portability** | None | One-click CSV Export and transactional CSV Bulk Import |

---

## 3. Technology Stack

- **Backend:** Python 3.12+, Django 5.x / 6.x, Django ORM, Django Auth, Django Forms
- **Frontend:** HTML5, CSS3, Bootstrap 5.3.3, Bootstrap Icons 1.11.3, Vanilla JavaScript
- **Database:** SQLite (development default) / PostgreSQL (production)
- **Deployment:** Gunicorn, Nginx, Systemd service, SSL/TLS, Environment-based `.env` configuration

---

## 4. Key Institutional Facts

| Fact | Value |
|---|---|
| **College Name** | Government Polytechnic Madhogarh |
| **Library Name** | Central Library |
| **Subtitle / Tagline** | Central Library & Digital Resource Portal |
| **District** | **Jalaun** (NOT Jalgaon), Uttar Pradesh |
| **Campus Location** | Kailor, Madhogarh, Jalaun, U.P. – 285126 |
| **Institution Code** | **3318** |
| **College Website** | `https://gpmadhogarh.ac.in/` |
| **Library ERP** | `https://erp.bizby.io/` |
| **Principal** | Shri O. P. Yadav |
| **Librarian** | Mrs. Priyanka Singh Dangi |
| **Official Email** | `govt.polytechnic.madhogarh@gmail.com` |
| **Helpline Phone** | `+91-9875151051` (Alt: `9140888062`) |

---

## 5. Quickstart & Installation

### Step 1: Clone and Set Up Virtual Environment
```bash
git clone <repository_url>
cd Library
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux / macOS
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run Database Migrations
```bash
python manage.py migrate
```

### Step 4: Run Idempotent Setup Command
To configure all institutional data, the 3 engineering branches, staff directory, notices, and initial catalog:
```bash
python manage.py setup_madhogarh
```

### Step 5: Start Development Server
```bash
python manage.py runserver 0.0.0.0:8000
```
Open [http://localhost:8000/](http://localhost:8000/) in your browser.

---

## 6. Default Administrative Credentials

- **Username:** `admin`
- **Password:** `Librarian@GPMadhogarh2026!`
- **Staff Dashboard:** [http://localhost:8000/dashboard/](http://localhost:8000/dashboard/)
- **Django Admin:** [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## 7. Testing & Verification

### Automated Unit & Integration Tests (16 Tests)
Run Django's test runner:
```bash
python manage.py test tests
```
*Result: 16 tests passing, validating models, Singleton SiteSettings, GP Madhogarh branding, department restrictions, OPAC search, membership submissions, feedback, and security authorization.*

### Automated Route & Endpoint Verification (50 Endpoints)
Run the route verification script:
```bash
python verify_routes.py
```
*Result: 100% of tested endpoints return HTTP 200 OK without errors.*

---

## 8. Production Deployment

Production deployment configurations and systemd services are provided under `deployment/`:
- **Nginx configuration:** `deployment/nginx_mmit_library.conf` (reverse proxy, static caching, gzip, security headers)
- **Gunicorn configuration:** `deployment/gunicorn_conf.py` (multi-worker WSGI server)
- **Systemd service:** `deployment/mmit_library.service`
- **Automated backup script:** `deployment/backup.sh`
- **Automated restore script:** `deployment/restore.sh`
- Detailed deployment manual: `docs/production-deployment.md`

---

## 9. Reference Audit Documentation

Comprehensive investigation documents are maintained under `docs/`:
- `docs/reference-audit.md`: Full architectural audit of the Blogger reference site.
- `docs/reference-sitemap.md`: Reference navigation mapping and modern Django routes.
- `docs/reference-navigation.md`: Comprehensive menu hierarchy and destination mapping.
- `docs/reference-page-inventory.md`: Page-by-page functional inventory and enhancements.
- `docs/reference-design-comparison.md`: Detailed visual, structural, and security comparison.
