# Reference Website Content Inventory

This document provides an exhaustive inventory of every verified text snippet, notice, contact datum, and external link extracted from `https://librarymmit.blogspot.com/`.

---

## 1. Verified Institutional Information

| Field | Extracted Data | Verification Status | Source Reference |
|---|---|---|---|
| **College Name** | Mahamaya Polytechnic of Information Technology (MMIT) | Verified | Banner / Title / About Page |
| **Location / Address** | Akbarpur, Kanpur Dehat, Uttar Pradesh - 209101 | Verified | Contact Section & Posts |
| **Affiliating Board** | Board of Technical Education Uttar Pradesh (BTEUP) | Verified | Header Link & Syllabus Page |
| **Principal Email** | `ppl.mmitmati@gmail.com` | Verified | Contact Section |
| **Official Phone** | `+91-9450342615` | Verified | Contact Section |
| **Librarian In-Charge** | Shri Abhinav Shesha | Verified | Book Donation Notice |
| **Operating Hours** | Mon - Sat: 10:00 AM – 05:00 PM; Sun & Gazetted Holidays: Closed | Verified | About Page Table |
| **Integrated System Mentioned** | e-Granthalaya 4.0 (EG4), NIC | Verified | About Library & Services |

---

## 2. Verified Policies & Rules

### 2.1 Borrowing Entitlement Table
- **Diploma Students:** 2 Books, 14 Days loan period
- **Faculty / Teaching Staff:** 5 Books, 30 Days loan period
- **Non-Teaching Staff:** 2 Books, 14 Days loan period

### 2.2 Conduct & Disciplinary Rules
- College Identity Card mandatory at entrance.
- Strict silence in reading hall and stack rooms.
- Mobile phones must remain on silent mode.
- Personal bags and print material must be placed at the property counter.
- Food, beverages, and smoking strictly prohibited.
- Lost or damaged items must be replaced with the latest edition or reimbursed.
- No-Dues certificate issued only upon return of all books and clearance of fines.

---

## 3. Verified Posts & Announcements

### Post 1: A Student's Guide to MMIT Library
- **Published Date:** October 08, 2026
- **Summary:** Outlines how students can search the OPAC catalogue, follow library etiquette, borrow books, access digital resources, and register with the NDLI Club.

### Post 2: Orientation Programme (Session 2026-27)
- **Target Audience:** Newly admitted 1st Year (Freshers) Diploma Students
- **Dates:** August 01 to August 14, 2026
- **Venue:** Seminar Hall, MMIT Campus
- **Motto:** *Dream • Learn • Achieve*
- **Key Sessions:** Campus & Lab visits, Library book issue rules & e-library access, BTEUP syllabus and exam rules, Hostel & anti-ragging policies.

### Post 3: Faculty Book Donations & New Arrivals
- **Acknowledgement:** Gratitude extended to faculty donors:
  - Shri Siddharth Singh (Mathematics)
  - Shri Suraj Pratap Singh (Civil Engineering)
  - Shri Ravi Rajak (Chemistry)
  - Shri Abhinav Shesha (Librarian)

### Post 4: NDLI Club Registration Guidelines
- **Joint Directorate Circular:** Bundelkhand & Kanpur Region directive regarding mandatory student NDLI registration.
- **Process:** Register at `https://ndl.iitkgp.ac.in/account/registration`, then join institutional club using college passkey at `https://club.ndl.iitkgp.ac.in/sign-up`.

---

## 4. Verified Academic Disciplines (BTEUP Diploma)

Based on reference posts and syllabus links:
1. **Computer Science & Engineering / Information Technology**
   - Core Subjects: Programming in C/Python, Data Structures, Database Management, Operating Systems, Web Development, Computer Networks.
2. **Civil Engineering**
   - Core Subjects: Building Materials, Surveying, Mechanics of Structures, Concrete Technology, Highway & Environmental Engineering.
3. **Electronics Engineering**
   - Core Subjects: Electronic Devices & Circuits, Digital Electronics, Microprocessors, Signals & Systems, Communication Engineering.
4. **Electrical Engineering**
   - Core Subjects: Basic Electrical Engineering, Electrical Machines, Power Systems, Control Systems, Electrical Measurements.
5. **Applied Sciences & Humanities**
   - Core Subjects: Applied Mathematics I & II, Applied Physics I & II, Applied Chemistry, Communication Skills (English & Hindi).

---

## 5. Unverified / Missing Reference Data & Modern Substitutions

| Reference Item | Original Limitation | Modern Django Implementation |
|---|---|---|
| **Book Catalogue Data** | Stored in an external Google Sheet; not publicly browseable directly on site. | Native Django `Book` and `BookCopy` database with over 30 initial realistic academic books mapped to BTEUP syllabus. |
| **Question Papers** | Unsorted Google Drive folder link. | Structured `DigitalResource` records with downloadable PDFs categorized by branch, semester, and year (2022-2025). |
| **Membership Form** | External Google Form (`https://forms.gle/wXdbRSzHQgPoT82s8`). | Native Django form with validation, student roll number, branch, photo/ID upload, and librarian approval workflow. |
| **Photo Gallery** | 404 dead link on Blogger (`/2026/07/photo-gallery.html`). | Native Django `LibraryEvent` and `GalleryImage` models with responsive lightbox image gallery. |
| **Search Function** | External Google Apps Script modal. | Full ORM search bar on homepage and catalog page searching Title, Author, ISBN, Subject, and Department. |

