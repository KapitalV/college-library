# Reference Website Navigation Architecture & Django Route Mapping

## 1. Overview and Structural Hierarchy

This document maps the information architecture and navigation patterns from the reference Blogger library portal (`librarymmit.blogspot.com`) to the modern, institutional Django implementation for **Government Polytechnic Madhogarh Central Library**, District Jalaun, Uttar Pradesh (Institution Code: **3318**).

---

## 2. Navigation Comparison Matrix

| Menu Category | Reference Site Item (Blogger) | Reference Destination | Django Implemented Route | HTTP Method & View Name | Status & Improvements |
|---|---|---|---|---|---|
| **Top Utility Bar** | Home | `/` | `/` | `GET` `core:home` | Professional institutional topbar with operating hours, phone, email, and live ERP link. |
| **Top Utility Bar** | College Website | `http://bteup.ac.in` | External: `https://gpmadhogarh.ac.in/` | `External Redirect` | Authoritative official college website link for Government Polytechnic Madhogarh. |
| **Top Utility Bar** | Library ERP | *(Not present on Blogger)* | `https://erp.bizby.io/` | `External Service Link` | Direct link to college ERP for student and faculty circulation records. |
| **Top Utility Bar** | Staff Login | *(None - unauthenticated)* | `/accounts/login/` | `GET/POST` `accounts:login` | Secure role-based staff and librarian authentication with CSRF protection. |
| **Main Header** | Brand Header | Raw text banner | Institutional Header | Global Template Include | Formal institutional title, AICTE approval, BTEUP affiliation, Jalaun location, Inst Code 3318. |
| **About Library** | About Library | `/p/about-library.html` | `/about/` | `GET` `pages:about` | Fully responsive overview with timings, infrastructure, collection details, and staff highlights. |
| **About Library** | Vision & Mission | *(Inlined in text)* | `/about/vision-mission/` | `GET` `pages:vision_mission` | Institutional vision, mission, and core polytechnic academic objectives. |
| **About Library** | Rules & Regulations | `/p/rules-regulations.html` | `/rules/` | `GET` `pages:rules` | Comprehensive borrowing rules table, loan periods, overdue fines, and no-dues clearance policies. |
| **About Library** | Library Staff | *(Scattered in posts)* | `/staff/` | `GET` `pages:staff` | Dedicated staff directory featuring Principal Shri O. P. Yadav & Librarian Mrs. Priyanka Singh Dangi. |
| **About Library** | Advisory Committee | *(Unstructured)* | `/staff/#committee` | `GET` `pages:staff` | Institutional Library Advisory Committee (LAC) composition and governance structure. |
| **About Library** | Facilities | *(Inlined in text)* | `/facilities/` | `GET` `pages:facilities` | Structured facility cards (Reading Hall, Digital Lab, Reference Stack, Book Bank). |
| **About Library** | Student FAQs | *(None)* | `/faq/` | `GET` `pages:faq` | Categorized accordion FAQs addressing cards, borrowing, renewals, digital access, and no-dues. |
| **Catalogue (OPAC)**| OPAC Search | Google Sheet redirect | `/catalog/` | `GET` `catalog:search` | High-performance in-house relational database search (Title, Author, ISBN, Subject, Department). |
| **Catalogue (OPAC)**| New Arrivals | Blog post feed | `/catalog/new-arrivals/` | `GET` `catalog:new_arrivals` | Showcase of recently cataloged physical textbooks and reference works with status badges. |
| **Catalogue (OPAC)**| Book Donations | Single blog post | `/catalog/donations/` | `GET` `catalog:donations` | Honor roll and list of donated textbooks acknowledging faculty and alumni donors. |
| **Digital Library** | Digital Gateway | `/p/digital-library.html` (404) | `/digital-library/` | `GET` `digital_library:home` | Integrated digital resource portal with instant gateway cards to national portals. |
| **Digital Library** | National Portals | External links | `/digital-library/portals/` | `GET` `digital_library:portals` | Curated listing of 8+ national academic repositories with description and direct access links. |
| **Digital Library** | NDLI Club | Blog announcement | `/services/ndli-club/` | `GET` `services:ndli_club` | 2-step registration walkthrough with official Bundelkhand circular notice and college Passkey. |
| **Digital Library** | e-Granthalaya 4.0| Outbound link | `http://eg4.nic.in/` | External Link | National Informatics Centre (NIC) cloud union catalogue. |
| **Digital Library** | AICTE e-KUMBH | Outbound link | `https://ekumbh.aicte-india.org/` | External Link | Indian language technical textbooks in Hindi for diploma courses. |
| **Digital Library** | NDLI Portal | Outbound link | `https://ndl.iitkgp.ac.in/` | External Link | IIT Kharagpur national repository (90M+ resources). |
| **Digital Library** | SWAYAM / NPTEL | Outbound link | `https://swayam.gov.in/` | External Link | Free MOOC video lectures and course material. |
| **Academic Resources**| Question Papers | Google Drive folder | `/resources/question-papers/`| `GET` `resources:question_papers`| Downloadable BTEUP semester question paper archives filtered by branch, semester, and year. |
| **Academic Resources**| Diploma Syllabus | BTEUP outbound link | `/resources/syllabus/` | `GET` `resources:syllabus` | Official semester-wise curriculum and course outlines for CSE, EE, and ECE. |
| **Academic Resources**| Lecture Notes & PPT| Dead link (`#`) | `/resources/lecture-notes/` | `GET` `resources:lecture_notes` | Verified faculty classroom presentations, hand-written notes, and study guides. |
| **Department Hubs** | Department Portals | *(None on Blogger)* | `/departments/` | `GET` `departments:department_list`| Active department hubs for Computer Science (355/389), Electrical (328/378), Electronics (330/380). |
| **Department Detail** | CSE Department Hub | *(None)* | `/departments/computer-science-engineering/` | `GET` `departments:department_detail` | Syllabi, textbooks, faculty notes, and past papers tailored strictly to Computer Science. |
| **Department Detail** | EE Department Hub | *(None)* | `/departments/electrical-engineering/` | `GET` `departments:department_detail` | Syllabi, textbooks, faculty notes, and past papers tailored strictly to Electrical Engineering. |
| **Department Detail** | ECE Department Hub | *(None)* | `/departments/electronics-engineering/` | `GET` `departments:department_detail` | Syllabi, textbooks, faculty notes, and past papers tailored strictly to Electronics Engineering. |
| **Library Services**| Services Overview | `/p/library-services.html` | `/services/` | `GET` `services:service_list` | Comprehensive service guide (Circulation, Book Bank, Inter-Library, Reference, Photocopying). |
| **Library Services**| Membership Apply | Google Forms | `/services/membership/` | `GET/POST` `services:membership` | Validated online membership registration form with photo upload and tracking. |
| **Library Services**| Recommend a Book | *(None)* | `/services/book-recommendation/` | `GET/POST` `services:book_recommend` | Faculty and student book procurement recommendation submission system. |
| **Library Services**| Resource Request | *(None)* | `/services/resource-request/` | `GET/POST` `services:resource_request` | Student request workflow for unavailable question papers, notes, or e-books. |
| **Library Services**| No-Dues Clearance | *(Scattered text)* | `/services/no-dues/` | `GET` `services:no_dues` | Step-by-step clearance instructions, requirements, and downloadable clearance voucher. |
| **Library Services**| Downloadable Forms | External PDFs | `/services/forms/` | `GET` `services:forms` | Centralized repository of printable PDF vouchers, membership forms, and declarations. |
| **Notices & Events**| Circulars & Notices| Uncategorized blog posts | `/notices/` | `GET` `notices:notice_list` | Categorized notices with priority badges (URGENT, HIGH, NORMAL), PDF attachments, and dates. |
| **Notices & Events**| Library Events | Uncategorized blog posts | `/events/` | `GET` `events:event_list` | Upcoming workshops, fresher orientations, book exhibitions, and webinars. |
| **Notices & Events**| Photo Gallery | Dead link (`404`) | `/events/gallery/` | `GET` `events:gallery_list` | Categorized visual showcase of library stacks, reading halls, events, and campus infrastructure. |
| **Feedback** | Feedback Form | *(None)* | `/feedback/` | `GET/POST` `feedback:feedback` | Student and faculty suggestion system with star ratings and categorized feedback channels. |
| **Contact** | Contact Section | `#contact-section` | `/contact/` | `GET` `core:contact` | Interactive campus map, phone, email, operating schedule, and Librarian officer in-charge card. |
| **Administration** | Dashboard Overview | *(None on Blogger)* | `/dashboard/` | `GET` `dashboard:overview` | Executive metrics, real-time counts, pending application counters, and quick actions. |
| **Administration** | Catalog Management | *(None)* | `/dashboard/books/` | `GET` `dashboard:book_list` | Staff management of titles, authors, categories, accession numbers, and stack locations. |
| **Administration** | CSV Book Import | *(None)* | `/dashboard/books/import-csv/` | `GET/POST` `dashboard:import_books_csv` | Bulk catalog upload supporting accession number lists and shelf assignments. |
| **Administration** | CSV Book Export | *(None)* | `/dashboard/books/export-csv/` | `GET` `dashboard:export_books_csv` | Complete catalog data export to standard CSV for institutional audits and accreditation. |

---

## 3. Department Structure Restrictions
As per authoritative institutional data from the official Government Polytechnic Madhogarh website (`gpmadhogarh.ac.in`) and URISE institutional profile (`urise.up.gov.in/poly/3318`):
- Active branches are strictly limited to the **three approved engineering departments**:
  1. Computer Science and Engineering (Branch Code: **355**, Lateral: **389**)
  2. Electrical Engineering (Branch Code: **328**, Lateral: **378**)
  3. Electronics Engineering (Branch Code: **330**, Lateral: **380**)
- Inactive / non-existent branches (Civil Engineering, Applied Sciences) are deactivated from public navigation and departmental listings.

