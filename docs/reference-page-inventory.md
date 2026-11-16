# Reference Website Page Inventory & Functional Specification

## 1. Inventory Overview

This page inventory details every verified page, post, and functional section discovered on the reference Blogger website (`https://librarymmit.blogspot.com/`), mapped to its corresponding implementation within the **Government Polytechnic Madhogarh Central Library** Django portal.

---

## 2. Complete Page-by-Page Inventory

### 2.1 Homepage
- **Reference URL:** `https://librarymmit.blogspot.com/` (and `?m=1`)
- **Original Content:** Basic Blogger homepage containing blog posts, sidebar widgets (About Me, Blog Archive, Popular Posts), and a top navigation menu.
- **Original Issues:** Heavy Blogger branding, lack of clear visual hierarchy, no prominent search bar, unstructured layout, lack of institutional authority.
- **Django Implementation:**
  - **Route:** `/` (`core:home`)
  - **Template:** `templates/core/home.html`
  - **Improvements:**
    1. Institutional Academic Hero with prominent live multi-category search bar (Books, Question Papers, Notes, Syllabus, Notices).
    2. Quick Access Cards grid linking directly to major resources.
    3. Urgent Notice Ticker and latest circulars with priority tags.
    4. Verified National Digital Portals grid (NDLI, e-KUMBH, e-Granthalaya 4.0, SWAYAM).
    5. Department Resource Hub cards for the 3 active branches (CSE, EE, ECE).
    6. Fresh Acquisitions carousel / grid showing available book copies.
    7. Live institutional statistics counter (Physical Copies, Book Titles, Digital Resources, Departments).
    8. Infrastructure highlights and student action triggers.

### 2.2 About Library
- **Reference URL:** `https://librarymmit.blogspot.com/p/about-library.html`
- **Original Content:** Text paragraph about library formation, reading room timings, e-Granthalaya automation, and basic purpose.
- **Django Implementation:**
  - **Route:** `/about/` (`pages:about`)
  - **Template:** `templates/pages/about.html`
  - **Improvements:**
    1. Formally structured institutional overview mapped to Government Polytechnic Madhogarh, Jalaun.
    2. Infrastructure & Key Features checklist with icons.
    3. Clear, responsive timings table for working days, reading halls, and holidays.
    4. Sidebar featuring Officer In-Charge profile and quick links.

### 2.3 Vision, Mission & Goals
- **Reference URL:** Inlined within About Library post on reference site.
- **Original Content:** Brief sentences stating the aim to provide library facilities to polytechnic students.
- **Django Implementation:**
  - **Route:** `/about/vision-mission/` (`pages:vision_mission`)
  - **Template:** `templates/pages/vision_mission.html`
  - **Improvements:**
    1. Distinct Vision and Mission cards with color-coded institutional branding.
    2. Core strategic objectives: Curricula Alignment, Book Bank Inclusivity, Digital Literacy, and Examination Support.

### 2.4 Rules & Regulations (Circulation Policy)
- **Reference URL:** `https://librarymmit.blogspot.com/p/rules-regulations.html`
- **Original Content:** List of general rules: identity cards required, mobile silent mode, book borrowing limits (students: 2 books for 14 days; teachers: 5 books for 30 days).
- **Django Implementation:**
  - **Route:** `/rules/` (`pages:rules`)
  - **Template:** `templates/pages/rules.html`
  - **Improvements:**
    1. Structured borrowing entitlement table (Category, Number of Books, Loan Duration, Renewal Allowance).
    2. Clear section on Overdue Fines & Lost Book Policy.
    3. Conduct & Reading Room Regulations.
    4. No-Dues clearance requirements.

### 2.5 Library Staff & Advisory Committee Directory
- **Reference URL:** Scattered across posts and widget credits on Blogger.
- **Original Content:** Mention of Librarian Shri Abhinav Shesha and occasional faculty book donors.
- **Django Implementation:**
  - **Route:** `/staff/` (`pages:staff`)
  - **Template:** `templates/pages/staff.html`
  - **Improvements:**
    1. Verified institutional directory featuring Principal Shri O. P. Yadav and Librarian Mrs. Priyanka Singh Dangi.
    2. Direct official contact channels (phone, email, qualification, designation).
    3. Institutional Library Advisory Committee (LAC) composition table with faculty representatives for CSE, EE, and ECE.

### 2.6 Facilities & Reading Hall
- **Reference URL:** Inlined within About page text.
- **Original Content:** Mention of reading hall and computers.
- **Django Implementation:**
  - **Route:** `/facilities/` (`pages:facilities`)
  - **Template:** `templates/pages/facilities.html`
  - **Improvements:**
    1. Interactive facility cards detailing capacity, timings, and feature lists.
    2. Covers: Central Reading Hall (100 seats), Digital Lab & E-Resource Center, Reference Stack Area, Book Bank Section, Periodicals & Newspaper Corner.

### 2.7 Student Help & FAQs
- **Reference URL:** None on Blogger (students had to contact manually).
- **Original Content:** Not implemented on reference.
- **Django Implementation:**
  - **Route:** `/faq/` (`pages:faq`)
  - **Template:** `templates/pages/faq.html`
  - **Improvements:**
    1. Searchable and categorized accordion FAQs covering General Timings, Membership, Borrowing/Fines, Digital Library/NDLI, and No-Dues Clearance.

### 2.8 Online Public Access Catalogue (OPAC Search)
- **Reference URL:** Linked to an external Google Sheet / Google Apps Script web app on Blogger.
- **Original Issues:** Unstable external script, no facet filtering, slow loading, zero database constraints, exposed raw spreadsheet.
- **Django Implementation:**
  - **Route:** `/catalog/` (`catalog:search`)
  - **Template:** `templates/catalog/catalog_search.html`
  - **Improvements:**
    1. Fully native Django ORM search across Title, Author, ISBN, Publisher, Subject, and Department.
    2. Facet filters by Academic Department and Availability status.
    3. Detailed book views with accession numbers, physical rack/shelf locations, and live availability badges.

### 2.9 New Arrivals & Acquisitions
- **Reference URL:** Unorganized blog post list.
- **Django Implementation:**
  - **Route:** `/catalog/new-arrivals/` (`catalog:new_arrivals`)
  - **Template:** `templates/catalog/new_arrivals.html`
  - **Improvements:** Filterable grid of newly acquired technical textbooks and reference volumes.

### 2.10 Book Donations & Donor Roll
- **Reference URL:** Post titled "List of Donated Books" acknowledging faculty book donations.
- **Django Implementation:**
  - **Route:** `/catalog/donations/` (`catalog:donations`)
  - **Template:** `templates/catalog/donations.html`
  - **Improvements:** Structured table honoring donors, donor department, book title, author, and date of donation.

### 2.11 Digital Library Portal & Gateway
- **Reference URL:** `/p/digital-library.html` (Returned 404 on reference).
- **Django Implementation:**
  - **Route:** `/digital-library/` (`digital_library:home`)
  - **Template:** `templates/resources/digital_library.html`
  - **Improvements:** Complete portal with NDLI Club guidance, e-KUMBH portal access, NIC e-Granthalaya integration, and SWAYAM / NPTEL resources.

### 2.12 National Educational Portals Directory
- **Reference URL:** Scattered outbound links in sidebar widgets.
- **Django Implementation:**
  - **Route:** `/digital-library/portals/` (`digital_library:portals`)
  - **Template:** `templates/resources/digital_portals.html`
  - **Improvements:** Curated directory with official logos/icons, portal descriptions, and direct access links.

### 2.13 NDLI Club Registration & Passkey Guide
- **Reference URL:** Blog post detailing NDLI club registration instructions.
- **Original Content:** Preserved the Joint Directorate directive from Bundelkhand / UP Technical Education and step-by-step instructions.
- **Django Implementation:**
  - **Route:** `/services/ndli-club/` (`services:ndli_club`)
  - **Template:** `templates/services/ndli_club.html`
  - **Improvements:** 2-step visual walkthrough, official Hindi directive alert, and clear institutional club identifier (`GPM-JALAUN-NDLI-3318`).

### 2.14 Previous Year Question Papers (BTEUP)
- **Reference URL:** Outbound hyperlink to a Google Drive folder.
- **Original Issues:** Unsorted Google Drive, no indexing by semester or subject code, broken permissions for unauthenticated users.
- **Django Implementation:**
  - **Route:** `/resources/question-papers/` (`resources:question_papers`)
  - **Template:** `templates/resources/question_papers.html`
  - **Improvements:** Native database storage with branch filtering, semester filtering (1 to 6), academic year tags, and one-click direct PDF downloads.

### 2.15 BTEUP Diploma Syllabus
- **Reference URL:** Hyperlink to BTEUP official syllabus page.
- **Django Implementation:**
  - **Route:** `/resources/syllabus/` (`resources:syllabus`)
  - **Template:** `templates/resources/syllabus_list.html`
  - **Improvements:** Branch-wise curriculum outlines and downloadable syllabus documents for CSE (355), EE (328), and ECE (330).

### 2.16 Faculty Lecture Notes & Handouts
- **Reference URL:** Dead link (`#`) on reference menu.
- **Django Implementation:**
  - **Route:** `/resources/lecture-notes/` (`resources:lecture_notes`)
  - **Template:** `templates/resources/lecture_notes.html`
  - **Improvements:** Working faculty presentation and lecture notes repository indexed by department, semester, and topic.

### 2.17 Department Resource Hubs
- **Reference URL:** Not implemented on Blogger.
- **Django Implementation:**
  - **Routes:**
    - Hub index: `/departments/` (`departments:department_list`)
    - CSE Hub: `/departments/computer-science-engineering/`
    - EE Hub: `/departments/electrical-engineering/`
    - ECE Hub: `/departments/electronics-engineering/`
  - **Improvements:** Dedicated branch portals consolidating textbooks, syllabus, past examination papers, and lecture notes for each of the three active departments.

### 2.18 Library Services Overview
- **Reference URL:** `https://librarymmit.blogspot.com/p/library-services.html`
- **Original Content:** Bullet list of services (Circulation, Reference, Periodicals, Orientation).
- **Django Implementation:**
  - **Route:** `/services/` (`services:service_list`)
  - **Template:** `templates/services/service_list.html`
  - **Improvements:** Comprehensive grid detailing 8 core services, rules, and direct links to online application workflows.

### 2.19 Online Library Membership Application
- **Reference URL:** Hyperlink to a Google Form.
- **Django Implementation:**
  - **Route:** `/services/membership/` (`services:membership`)
  - **Template:** `templates/services/membership_apply.html`
  - **Improvements:** Validated Django ModelForm collecting student roll number, URISE enrollment, branch, semester, contact info, and ID card photo. Stored directly in the database with status tracking.

### 2.20 Book Recommendation System
- **Reference URL:** Not available on Blogger.
- **Django Implementation:**
  - **Route:** `/services/book-recommendation/` (`services:book_recommend`)
  - **Template:** `templates/services/book_recommend.html`
  - **Improvements:** Formal procurement request submission allowing students and faculty to recommend titles with justification.

### 2.21 Missing Resource Request
- **Reference URL:** Not available on Blogger.
- **Django Implementation:**
  - **Route:** `/services/resource-request/` (`services:resource_request`)
  - **Template:** `templates/services/resource_request.html`
  - **Improvements:** Mechanism for students to request specific past exam papers, lecture notes, or syllabus copies.

### 2.22 No-Dues Clearance Guidelines & Voucher
- **Reference URL:** Brief mention in Rules text.
- **Django Implementation:**
  - **Route:** `/services/no-dues/` (`services:no_dues`)
  - **Template:** `templates/services/no_dues.html`
  - **Improvements:** Step-by-step checklist for diploma completion clearance and direct PDF voucher download.

### 2.23 Downloadable Official Forms
- **Reference URL:** External links scattered in posts.
- **Django Implementation:**
  - **Route:** `/services/forms/` (`services:forms`)
  - **Template:** `templates/services/forms_list.html`
  - **Improvements:** Centralized listing of all official PDF forms (Membership, Book Bank, No-Dues, Book Recommendation).

### 2.24 Notices, Circulars & Announcements
- **Reference URL:** Standard Blogger chronological post list.
- **Django Implementation:**
  - **Route:** `/notices/` (`notices:notice_list`)
  - **Detail Route:** `/notices/<slug>/` (`notices:notice_detail`)
  - **Improvements:** Filterable circulars by category (Orientation, Circulation, Exam, Book Bank, Digital), priority badges, pinned notices, and PDF attachments.

### 2.25 Events & Orientations
- **Reference URL:** Post titled "Orientation Programme 2026-27".
- **Django Implementation:**
  - **Route:** `/events/` (`events:event_list`)
  - **Detail Route:** `/events/<slug>/` (`events:event_detail`)
  - **Improvements:** Dedicated event cards with date, time, venue, organizer, and target audience badges.

### 2.26 Photo Gallery
- **Reference URL:** `/2026/07/photo-gallery.html` (Returned 404).
- **Django Implementation:**
  - **Route:** `/events/gallery/` (`events:gallery_list`)
  - **Template:** `templates/events/gallery_list.html`
  - **Improvements:** Responsive photo grid categorized by Reading Hall, Book Stacks, Orientations, and Events.

### 2.27 Feedback & Suggestion Portal
- **Reference URL:** Not available on Blogger.
- **Django Implementation:**
  - **Route:** `/feedback/` (`feedback:feedback`)
  - **Template:** `templates/feedback/feedback_form.html`
  - **Improvements:** Category-specific feedback submission with 1-5 star ratings and message storage.

### 2.28 Contact & Location Information
- **Reference URL:** Bottom footer anchor (`#contact-section`).
- **Django Implementation:**
  - **Route:** `/contact/` (`core:contact`)
  - **Template:** `templates/core/contact.html`
  - **Improvements:** Interactive Google Map embed for Kailor, Madhogarh, District Jalaun; helpline numbers; email directory; operating schedule; and Librarian contact card.

### 2.29 Staff Administration Dashboard
- **Reference URL:** Blogger backend (restricted to Google account owner; no role management).
- **Django Implementation:**
  - **Routes:** `/dashboard/` and associated sub-routes (`dashboard:*`)
  - **Improvements:** Custom-built role-based dashboard for cataloging books, importing/exporting CSVs, managing notices, reviewing membership applications, and handling resource requests.

