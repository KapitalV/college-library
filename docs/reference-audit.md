# Reference Website Audit: MMIT Library (Blogger)

**Inspected URL:** https://librarymmit.blogspot.com/?m=1 and https://librarymmit.blogspot.com/  
**Inspection Date:** November 2026  
**Auditor:** Autonomous Senior Django Full-Stack Architect & Library Information Specialist  
**Target Entity:** Mahamaya Polytechnic of Information Technology (MMIT), Akbarpur, Kanpur Dehat, Uttar Pradesh  
**Affiliation:** Board of Technical Education Uttar Pradesh (BTEUP)  

---

## 1. Executive Summary

The reference site `librarymmit.blogspot.com` is hosted on Google's Blogger platform. While it served as an initial, commendable grassroots effort to provide online library links and notices for polytechnic diploma students in Kanpur Dehat, it suffers from severe platform limitations typical of Blogger sites:

1. **Fragmented Architecture:** Essential features (catalogue search, question papers, membership forms) are outsourced to external third-party services:
   - OPAC search is redirected to a Google Apps Script / Google Sheet endpoint.
   - Question papers are stored on an external Google Drive folder.
   - Membership registration is hosted on a Google Forms URL.
   - Digital library portals are merely external outbound hyperlinks.
2. **Broken and Missing Links:** Several navigation links in the menu point to empty fragments (`#`), or return HTTP 404 errors (e.g., `/p/digital-library.html`, `/2026/07/photo-gallery.html`).
3. **No True Relational Database:** There is no persistent database model for books, physical copies (accession numbers), departments, subjects, semesters, or student service requests.
4. **No Security or Role-Based Administration:** No authentication exists for librarians or content managers; all edits must be done via Blogger's blog post editor or widget settings.
5. **UI/UX and Accessibility Deficiencies:** The Blogger layout relies on default widget templates, inline CSS styles, raw marquee/pop-up alert scripts, inconsistent mobile responsiveness, and poor WCAG 2.2 accessibility.
6. **No Structured Department/Semester Resource Hierarchy:** Study materials and syllabus links are not systematically categorized by branch (e.g., Computer Science, Civil, Electronics) or semester (Semester 1 to 6).

---

## 2. Reference Site Inspection & Inventory

### 2.1 Identity and Institutional Branding
- **Institution:** Mahamaya Polytechnic of Information Technology (MMIT), Akbarpur, Kanpur Dehat, Uttar Pradesh - 209101
- **Governing / Board Authority:** Board of Technical Education Uttar Pradesh (BTEUP) (`http://bteup.ac.in`)
- **Key Contacts:**
  - Official Principal Email: `ppl.mmitmati@gmail.com`
  - Helpline / Contact Phone: `+91-9450342615`
  - Librarian: Shri Abhinav Shesha
  - Faculty Mentioned in Donors List: Shri Siddharth Singh (Mathematics), Shri Suraj Pratap Singh (Civil), Shri Ravi Rajak (Chemistry)
- **Library Operating Hours:** Monday – Saturday: 10:00 AM – 05:00 PM; Sunday & Gazetted Holidays: Closed.

### 2.2 Navigation Structure on Reference Site
- **Top Utility Links:** Home, College Website (BTEUP)
- **MMIT Library Dropdown:**
  - About Library (`/p/about-library.html`)
  - Rules & Regulations (`/p/rules-regulations.html`)
  - Library Services (`/p/library-services.html`)
- **Digital Library Dropdown:**
  - e-Granthalaya (EG4) (`http://eg4.nic.in/`)
  - National Digital Library of India (`https://ndl.iitkgp.ac.in/`)
  - SWAYAM / NPTEL (`https://swayam.gov.in/`)
  - e-KUMBH Portal (AICTE Hindi/regional engineering books, `https://ekumbh.aicte-india.org/`)
- **Academic Links:**
  - Question Papers (`Google Drive folder`)
  - Syllabus (`BTEUP syllabus portal`)
  - E-Learning Corner (Faculty PPTs, Video Lectures, E-Books - mostly dead links `#` on reference)
- **Utility / Gallery:**
  - Photo Gallery (`/2026/07/photo-gallery.html` - 404 on reference)
  - Contact Us (`#contact-section`)

### 2.3 Verified Content Assets
1. **About Library:** Details on reading hall, OPAC automation using e-Granthalaya 4.0, curriculum alignment with BTEUP, and working hours.
2. **Rules & Regulations:**
   - Identity Card mandatory.
   - Borrowing allowances: Diploma students (2 books, 14 days), Teaching Staff (5 books, 30 days), Non-Teaching Staff (2 books, 14 days).
   - Loss/Damage policy: replacement with latest edition or cost recovery.
   - No-dues clearance certificate policy.
3. **Library Services:** Circulation, OPAC discovery, reading hall, digital portals, question bank, newspapers & periodicals, current awareness service (CAS), orientation guidance.
4. **Recent Posts / Announcements:**
   - Orientation Programme (Session 2026-27) for newly admitted freshers (August 1–14, Seminar Hall).
   - A Student's Guide to MMIT Library (October 2026).
   - Faculty book donation notice acknowledging donations by Mathematics, Civil, Chemistry faculty and Librarian.
   - NDLI Club Registration instructions (Passkey entry, National Digital Library club membership).

---

## 3. Responsive Inspection Findings

| Viewport | Device Class | Reference Site Behavior | Issues Identified |
|---|---|---|---|
| **1440px** | Desktop / Laptop | Multi-column Blogger layout with right sidebar widgets. | Lots of empty whitespace, small non-contrasting fonts, unstyled external links, inline `<button>` styling with hardcoded `#0d6efd`. |
| **768px** | Tablet | Two-column stacked widgets. | Overlapping dropdown menus, awkward margins, misaligned search buttons. |
| **390px** | Mobile Smartphone | Single-column linear layout. | Dropdown navigation breaks into unindented list, tables in Rules and Regulations horizontally clip, modal popups for NDLI overflow small screens. |

---

## 4. Key Improvements Required in the Django Web Application

1. **Integrated In-House OPAC:** Implement full database models for `Book`, `BookCopy` (with accession numbers, shelf locations, and status), and `Category`. Provide multi-criteria public search (Title, Author, ISBN, Subject, Department) with zero external script dependency.
2. **Dedicated Department & Academic Resource Repository:** Model branches (Computer Science & Engineering, Civil Engineering, Electronics Engineering, Applied Sciences), semesters (1 to 6), subjects, and resource types (Previous Year Question Papers, Syllabus, Lecture Notes, E-Books, Project Reports).
3. **Integrated Services & Feedback:** Replace external Google Forms with validated Django ModelForms for Book Recommendations, Membership Applications, Resource Requests, and Feedback.
4. **Role-Based Staff Dashboard:** Built-in dashboard for Librarians and Content Editors to manage inventory, cataloguing, notices, events, resource uploads, and user requests securely.
5. **Native Notices & Event Management:** Priority banners, expiry dates, downloadable PDF circulars, and an interactive photo gallery.
6. **Modern Academic Theme & WCAG 2.2 AA Compliance:** Clean navy (`#102A43`), teal (`#0F766E`), and gold (`#D6A443`) palette, responsive typography (Inter & Noto Sans Devanagari), accessible touch targets, and mobile-first navigation.

