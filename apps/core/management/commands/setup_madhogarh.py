import sys
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from apps.core.models import SiteSettings, MenuItem, HeroSlide
from apps.departments.models import Department, Subject
from apps.catalog.models import Category, Book, BookCopy
from apps.resources.models import DigitalResource
from apps.notices.models import Notice
from apps.events.models import LibraryEvent, GalleryImage
from apps.pages.models import LibraryStaff, LibraryCommitteeMember, Facility, FAQ
from apps.library_services.models import DownloadableForm
from apps.accounts.models import StaffProfile


class Command(BaseCommand):
    help = "Idempotently configure Government Polytechnic Madhogarh Library data, branding, departments, and staff."

    def handle(self, *args, **options):
        # ---------------------------------------------------------------------
        # 8. Hero Slideshow Slides
        # ---------------------------------------------------------------------
        slides_data = [
            ("Government Polytechnic Madhogarh Central Library", "Central repository of technical knowledge, diploma textbooks, BTEUP question banks, and digital resources for engineering scholars.", "Campus Overview", "hero_slides/slide1_campus.jpg", 1, "/about/"),
            ("Digital Library Gateway & NDLI Institutional Club", "24x7 online access to over 90+ million academic journals, e-Granthalaya OPAC, SWAYAM video lectures, and AICTE e-KUMBH portals.", "Digital Learning", "hero_slides/slide2_digital.jpg", 2, "/digital-library/"),
            ("Diploma Engineering Curriculum & BTEUP Question Banks", "Comprehensive technical collections for Computer Science (355), Electrical (328), and Electronics Engineering (330).", "Academic Collection", "hero_slides/slide3_academics.jpg", 3, "/catalog/"),
        ]
        for title, subtitle, badge, img_path, order, link_url in slides_data:
            HeroSlide.objects.get_or_create(
                title=title,
                defaults={
                    'subtitle': subtitle,
                    'badge_text': badge,
                    'image': img_path,
                    'order': order,
                    'link_url': link_url,
                    'link_text': 'Explore More',
                    'is_active': True,
                }
            )
        self.stdout.write(self.style.SUCCESS("✓ Seeded/verified responsive hero carousel slides."))

        self.stdout.write(self.style.SUCCESS("=" * 70))
        self.stdout.write(self.style.SUCCESS("Initializing Government Polytechnic Madhogarh Central Library Setup"))
        self.stdout.write(self.style.SUCCESS("Institution Code: 3318 | District: Jalaun, Uttar Pradesh"))
        # ---------------------------------------------------------------------
        # 8. Hero Slideshow Slides
        # ---------------------------------------------------------------------
        slides_data = [
            ("Government Polytechnic Madhogarh Central Library", "Central repository of technical knowledge, diploma textbooks, BTEUP question banks, and digital resources for engineering scholars.", "Campus Overview", "hero_slides/slide1_campus.jpg", 1, "/about/"),
            ("Digital Library Gateway & NDLI Institutional Club", "24x7 online access to over 90+ million academic journals, e-Granthalaya OPAC, SWAYAM video lectures, and AICTE e-KUMBH portals.", "Digital Learning", "hero_slides/slide2_digital.jpg", 2, "/digital-library/"),
            ("Diploma Engineering Curriculum & BTEUP Question Banks", "Comprehensive technical collections for Computer Science (355), Electrical (328), and Electronics Engineering (330).", "Academic Collection", "hero_slides/slide3_academics.jpg", 3, "/catalog/"),
        ]
        for title, subtitle, badge, img_path, order, link_url in slides_data:
            HeroSlide.objects.get_or_create(
                title=title,
                defaults={
                    'subtitle': subtitle,
                    'badge_text': badge,
                    'image': img_path,
                    'order': order,
                    'link_url': link_url,
                    'link_text': 'Explore More',
                    'is_active': True,
                }
            )
        self.stdout.write(self.style.SUCCESS("✓ Seeded/verified responsive hero carousel slides."))

        self.stdout.write(self.style.SUCCESS("=" * 70))

        # ---------------------------------------------------------------------
        # 1. Superuser / Admin Setup
        # ---------------------------------------------------------------------
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'govt.polytechnic.madhogarh@gmail.com',
                'first_name': 'Priyanka',
                'last_name': 'Singh Dangi',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        admin_user.email = 'govt.polytechnic.madhogarh@gmail.com'
        admin_user.first_name = 'Priyanka'
        admin_user.last_name = 'Singh Dangi'
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.set_password('Librarian@GPMadhogarh2026!')
        admin_user.save()

        profile, _ = StaffProfile.objects.get_or_create(user=admin_user)
        profile.role = 'ADMIN'
        profile.designation = 'Librarian & In-Charge Central Library'
        profile.phone = '9305574396'
        profile.save()
        self.stdout.write(self.style.SUCCESS("✓ Admin user configured: admin (Librarian@GPMadhogarh2026!)"))

        # ---------------------------------------------------------------------
        # 2. SiteSettings Configuration (Strictly GP Madhogarh Facts)
        # ---------------------------------------------------------------------
        settings = SiteSettings.load()
        settings.college_name = "Government Polytechnic Madhogarh"
        settings.library_name = "Central Library"
        settings.short_name = "GP Madhogarh Library"
        settings.institution_code = "3318"
        settings.affiliation_info = "Approved by AICTE New Delhi & Affiliated to Board of Technical Education Uttar Pradesh (BTEUP)"
        settings.tagline = "Central Library & Digital Resource Portal"
        
        settings.campus_location = "Kailor, Madhogarh"
        settings.district = "Jalaun"
        settings.state = "Uttar Pradesh"
        settings.postal_code = "285126"
        
        settings.contact_phone = "9305574396"
        settings.library_email = "govt.polytechnic.madhogarh@gmail.com"
        settings.logo = "site/gpm_logo.webp"
        settings.hero_image = "site/gpm_header_banner.png"
        settings.principal_email = "govt.polytechnic.madhogarh@gmail.com"
        settings.college_website_url = "https://gpmadhogarh.ac.in/"
        settings.erp_url = "https://erp.bizby.io/"
        
        settings.opening_hours_weekday = "Monday to Saturday: 10:00 AM – 05:00 PM"
        settings.opening_hours_weekend = "Sunday & Gazetted Holidays: Closed"
        settings.reading_hall_hours = "09:30 AM – 05:30 PM (Air-cooled Silent Study Zone)"
        
        settings.hero_title = "Welcome to Government Polytechnic Madhogarh Library"
        settings.hero_subtitle = (
            "Central Library & Digital Resource Portal empowering diploma engineers and technical "
            "scholars with academic collections, BTEUP question banks, syllabus, e-journals, and NDLI digital resources."
        )
        settings.footer_about = (
            "The Central Library of Government Polytechnic Madhogarh, Kailor, District Jalaun (Uttar Pradesh) "
            "serves as the primary academic repository and information center for diploma students and faculty, "
            "mapped strictly to the curriculum of the Board of Technical Education Uttar Pradesh (BTEUP)."
        )
        
        settings.egranthalaya_url = "http://eg4.nic.in/"
        settings.ndli_portal_url = "https://ndl.iitkgp.ac.in/"
        settings.ndli_club_reg_url = "https://club.ndl.iitkgp.ac.in/sign-up"
        settings.ekumbh_url = "https://ekumbh.aicte-india.org/"
        settings.swayam_url = "https://swayam.gov.in/"
        settings.save()
        self.stdout.write(self.style.SUCCESS("✓ SiteSettings configured with verified GP Madhogarh details."))

        # ---------------------------------------------------------------------
        # 3. Verified Engineering Departments (EXACTLY 3 Active Branches)
        # ---------------------------------------------------------------------
        # 1. Computer Science and Engineering (Code: CSE, Branch: 355, Lateral: 389)
        # 2. Electrical Engineering (Code: EE, Branch: 328, Lateral: 378)
        # 3. Electronics Engineering (Code: ECE, Branch: 330, Lateral: 380)
        # Explicit rule: Do NOT include Civil or Mechanical as active departments.
        # ---------------------------------------------------------------------
        dept_configs = [
            {
                'name': 'Computer Science and Engineering',
                'code': 'CSE',
                'slug': 'computer-science-engineering',
                'branch_code': '355',
                'lateral_code': '389',
                'icon': 'bi-laptop',
                'head_of_department': 'Department In-Charge (CSE)',
                'intake_capacity': 60,
                'display_order': 1,
                'description': (
                    "3-Year Diploma in Computer Science and Engineering (BTEUP Branch Code: 355 / Lateral Entry: 389). "
                    "Comprehensive curriculum covering Programming in C, Python, Data Structures, Operating Systems, "
                    "Database Management Systems (DBMS), Web Development, Computer Networks, Software Engineering, "
                    "and Cloud Technologies."
                )
            },
            {
                'name': 'Electrical Engineering',
                'code': 'EE',
                'slug': 'electrical-engineering',
                'branch_code': '328',
                'lateral_code': '378',
                'icon': 'bi-lightning-charge',
                'head_of_department': 'Department In-Charge (EE)',
                'intake_capacity': 60,
                'display_order': 2,
                'description': (
                    "3-Year Diploma in Electrical Engineering (BTEUP Branch Code: 328 / Lateral Entry: 378). "
                    "Core technical foundation in Electrical Machines, Power Transmission & Distribution, Circuit Theory, "
                    "Switchgear & Protection, Control Systems, Industrial Instrumentation, and Renewable Energy Systems."
                )
            },
            {
                'name': 'Electronics Engineering',
                'code': 'ECE',
                'slug': 'electronics-engineering',
                'branch_code': '330',
                'lateral_code': '380',
                'icon': 'bi-cpu',
                'head_of_department': 'Department In-Charge (ECE)',
                'intake_capacity': 60,
                'display_order': 3,
                'description': (
                    "3-Year Diploma in Electronics Engineering (BTEUP Branch Code: 330 / Lateral Entry: 380). "
                    "In-depth studies in Electronic Devices & Circuits, Digital Electronics, Microprocessors & Microcontrollers, "
                    "Communication Engineering, Signal Processing, IoT Devices, and VLSI basics."
                )
            },
        ]

        active_codes = []
        for d in dept_configs:
            dept_obj, _ = Department.objects.get_or_create(code=d['code'])
            dept_obj.name = d['name']
            dept_obj.slug = d['slug']
            dept_obj.branch_code = d['branch_code']
            dept_obj.lateral_code = d['lateral_code']
            dept_obj.icon = d['icon']
            dept_obj.head_of_department = d['head_of_department']
            dept_obj.intake_capacity = d['intake_capacity']
            dept_obj.display_order = d['display_order']
            dept_obj.description = d['description']
            dept_obj.is_active = True
            dept_obj.save()
            active_codes.append(d['code'])
            self.stdout.write(self.style.SUCCESS(f"  ✓ Active Branch: {d['name']} (Code: {d['branch_code']})"))

        # Deactivate any non-authorized departments (Civil, ASH, etc.)
        deactivated = Department.objects.exclude(code__in=active_codes).update(is_active=False)
        self.stdout.write(self.style.SUCCESS(f"  ✓ Deactivated {deactivated} non-authorized/ancillary departments."))

        # ---------------------------------------------------------------------
        # 4. Staff Directory & Advisory Committee
        # ---------------------------------------------------------------------
        LibraryStaff.objects.all().update(is_active=False)

        # 1. Principal & Patron
        p_staff, _ = LibraryStaff.objects.get_or_create(
            name="Shri O. P. Yadav",
            defaults={'role_type': 'ADVISOR'}
        )
        p_staff.designation = "Principal & Patron"
        p_staff.qualification = "M.Tech / Administrative Leadership"
        p_staff.role_type = "ADVISOR"
        p_staff.email = "govt.polytechnic.madhogarh@gmail.com"
        p_staff.phone = "+91-9875151051"
        p_staff.bio = (
            "Principal of Government Polytechnic Madhogarh, Jalaun (Uttar Pradesh). "
            "Guiding institutional vision, library digital transformation, and student technical excellence."
        )
        p_staff.display_order = 1
        p_staff.is_active = True
        p_staff.save()

        # 2. Librarian & In-Charge
        l_staff, _ = LibraryStaff.objects.get_or_create(
            name="Mrs. Priyanka Singh Dangi",
            defaults={'role_type': 'LIBRARIAN'}
        )
        l_staff.designation = "Librarian & In-Charge Central Library"
        l_staff.qualification = "M.Lib.I.Sc / UGC-NET"
        l_staff.role_type = "LIBRARIAN"
        l_staff.email = "govt.polytechnic.madhogarh@gmail.com"
        l_staff.phone = "+91-9875151051"
        l_staff.bio = (
            "Librarian and In-Charge of the Central Library & Digital Resource Portal at Government Polytechnic Madhogarh. "
            "Supervises OPAC cataloging, accessioning, BTEUP question banks, book bank allocations, and NDLI club registration."
        )
        l_staff.display_order = 2
        l_staff.is_active = True
        l_staff.save()

        # 3. Advisory Committee Members
        LibraryCommitteeMember.objects.all().delete()
        committee_data = [
            ("Shri O. P. Yadav", "Principal", "Institutional Administration", "Chairman (Principal)", 1),
            ("Mrs. Priyanka Singh Dangi", "Librarian", "Central Library", "Member Secretary (Librarian)", 2),
            ("Head of Department (CSE)", "Lecturer / HOD In-Charge", "Computer Science & Engineering", "Member (Faculty Representative)", 3),
            ("Head of Department (EE)", "Lecturer / HOD In-Charge", "Electrical Engineering", "Member (Faculty Representative)", 4),
            ("Head of Department (ECE)", "Lecturer / HOD In-Charge", "Electronics Engineering", "Member (Faculty Representative)", 5),
        ]
        for name, desig, dept, role, order in committee_data:
            LibraryCommitteeMember.objects.create(
                name=name,
                designation=desig,
                department=dept,
                committee_role=role,
                display_order=order
            )
        self.stdout.write(self.style.SUCCESS("✓ Configured Staff Directory & Library Advisory Committee."))

        # ---------------------------------------------------------------------
        # 5. Core Academic Subjects (Mapped to the 3 Branches)
        # ---------------------------------------------------------------------
        cse = Department.objects.get(code='CSE')
        ee = Department.objects.get(code='EE')
        ece = Department.objects.get(code='ECE')

        branch_subjects = [
            # CSE
            (cse, "Programming in C", "CS-101", 1),
            (cse, "Basics of Information Technology", "CS-102", 1),
            (cse, "Data Structures Using C", "CS-301", 3),
            (cse, "Digital Electronics & Microprocessors", "CS-302", 3),
            (cse, "Relational Database Management Systems", "CS-401", 4),
            (cse, "Operating Systems", "CS-402", 4),
            (cse, "Web Development and Java Programming", "CS-501", 5),
            (cse, "Computer Networks & Security", "CS-502", 5),
            (cse, "Cloud Computing & Python Programming", "CS-601", 6),
            # EE
            (ee, "Basic Electrical Engineering", "EE-101", 1),
            (ee, "Electrical & Electronics Engineering Materials", "EE-201", 2),
            (ee, "Electrical Machines - I", "EE-301", 3),
            (ee, "Electrical Measurement and Measuring Instruments", "EE-302", 3),
            (ee, "Electrical Machines - II", "EE-401", 4),
            (ee, "Transmission and Distribution of Electrical Power", "EE-402", 4),
            (ee, "Switchgear and Protection", "EE-501", 5),
            (ee, "Industrial Electronics and Control", "EE-502", 5),
            (ee, "Utilization of Electrical Energy & Traction", "EE-601", 6),
            # ECE
            (ece, "Electronic Components and Devices", "EC-101", 1),
            (ece, "Electronic Devices and Circuits", "EC-201", 2),
            (ece, "Digital Electronics", "EC-301", 3),
            (ece, "Network Filters and Transmission Lines", "EC-302", 3),
            (ece, "Communication Engineering - I", "EC-401", 4),
            (ece, "Microprocessors and Peripheral Devices", "EC-402", 4),
            (ece, "Optical Fiber & Microwave Communication", "EC-501", 5),
            (ece, "Consumer Electronics", "EC-502", 5),
            (ece, "Wireless & Mobile Communication", "EC-601", 6),
        ]

        created_sub_count = 0
        for dept, name, code, sem in branch_subjects:
            sub, created = Subject.objects.get_or_create(
                department=dept,
                code=code,
                semester=sem,
                defaults={'name': name, 'is_active': True}
            )
            if created:
                created_sub_count += 1
        self.stdout.write(self.style.SUCCESS(f"✓ Checked/added {len(branch_subjects)} syllabus subjects."))

        # ---------------------------------------------------------------------
        # 6. Academic Notices (Tailored for GP Madhogarh)
        # ---------------------------------------------------------------------
        notice_samples = [
            (
                "Welcome to Central Library - Academic Session 2026-27 Orientation",
                "Official orientation and library card distribution schedule for newly admitted diploma engineering students at Government Polytechnic Madhogarh.",
                (
                    "All first-year diploma students admitted to Computer Science & Engineering (355), "
                    "Electrical Engineering (328), and Electronics Engineering (330) are informed that library "
                    "orientation sessions and membership card issuance will commence from Monday. Students must bring "
                    "their URISE registration receipt and 2 passport size photographs to the Central Library circulation desk."
                ),
                "CIRCULATION",
                "HIGH",
                True
            ),
            (
                "National Digital Library of India (NDLI) Institutional Club Registration",
                "Register for GP Madhogarh NDLI Club using passkey to access 90+ million academic resources and journals.",
                (
                    "All students and faculty of Government Polytechnic Madhogarh are encouraged to enroll in our college's "
                    "National Digital Library of India (NDLI) Club. Gain free 24x7 remote access to diploma textbooks, "
                    "monographs, audiobooks, video lectures from IITs/NITs, and research papers. Visit the NDLI portal link in the top menu."
                ),
                "DIGITAL",
                "URGENT",
                True
            ),
            (
                "BTEUP Semester Board Examination Question Papers Bank Available",
                "Previous 10-year BTEUP diploma examination papers archived in Central Library digital portal.",
                (
                    "The Central Library has completed digitization of previous year BTEUP question papers for CSE, "
                    "Electrical, and Electronics Engineering branches. Students can browse by department, semester, and year "
                    "or download PDF copies directly from our portal."
                ),
                "EXAM",
                "NORMAL",
                False
            ),
            (
                "Book Bank Scheme Allocation for Even Semester",
                "Eligible SC/ST and general category students can apply for full-semester textbook sets under the institutional Book Bank.",
                (
                    "Applications are invited for textbook allocations under the Government Polytechnic Madhogarh Library Book Bank. "
                    "Under this scheme, eligible students receive complete textbook sets for the entire academic term. "
                    "Download the application form from our Library Services section."
                ),
                "BOOK_BANK",
                "HIGH",
                False
            ),
        ]

        for title, summary, content, cat, priority, pinned in notice_samples:
            Notice.objects.get_or_create(
                title=title,
                defaults={
                    'short_summary': summary,
                    'content': content,
                    'category': cat,
                    'priority': priority,
                    'is_pinned': pinned,
                    'is_active': True,
                    'publish_date': timezone.now().date(),
                }
            )
        self.stdout.write(self.style.SUCCESS("✓ Seeded/verified GP Madhogarh library notices."))

        # ---------------------------------------------------------------------
        # 7. Downloadable Forms
        # ---------------------------------------------------------------------
        forms = [
            ("Library Membership Application Form", "Official application form for student and faculty library card issuance.", 1),
            ("Book Bank Scheme Application Form", "Prescribed form for applying to semester-long textbook lending under Book Bank.", 2),
            ("Library No-Dues Clearance Certificate Form", "Clearance voucher required for diploma completion, transcript, and TC issuance.", 3),
            ("Book Recommendation Form for Faculty & Students", "Form to propose new technical reference books, standards, and journal titles.", 4),
        ]
        for title, desc, order in forms:
            DownloadableForm.objects.get_or_create(
                title=title,
                defaults={
                    'description': desc,
                    'order': order,
                    'is_active': True,
                }
            )
        self.stdout.write(self.style.SUCCESS("✓ Seeded/verified downloadable official forms."))

        # ---------------------------------------------------------------------
        # 8. Hero Slideshow Slides
        # ---------------------------------------------------------------------
        slides_data = [
            ("Government Polytechnic Madhogarh Central Library", "Central repository of technical knowledge, diploma textbooks, BTEUP question banks, and digital resources for engineering scholars.", "Campus Overview", "hero_slides/slide1_campus.jpg", 1, "/about/"),
            ("Digital Library Gateway & NDLI Institutional Club", "24x7 online access to over 90+ million academic journals, e-Granthalaya OPAC, SWAYAM video lectures, and AICTE e-KUMBH portals.", "Digital Learning", "hero_slides/slide2_digital.jpg", 2, "/digital-library/"),
            ("Diploma Engineering Curriculum & BTEUP Question Banks", "Comprehensive technical collections for Computer Science (355), Electrical (328), and Electronics Engineering (330).", "Academic Collection", "hero_slides/slide3_academics.jpg", 3, "/catalog/"),
        ]
        for title, subtitle, badge, img_path, order, link_url in slides_data:
            HeroSlide.objects.get_or_create(
                title=title,
                defaults={
                    'subtitle': subtitle,
                    'badge_text': badge,
                    'image': img_path,
                    'order': order,
                    'link_url': link_url,
                    'link_text': 'Explore More',
                    'is_active': True,
                }
            )
        self.stdout.write(self.style.SUCCESS("✓ Seeded/verified responsive hero carousel slides."))

        self.stdout.write(self.style.SUCCESS("=" * 70))
        self.stdout.write(self.style.SUCCESS("Setup Complete: Government Polytechnic Madhogarh Central Library"))
        self.stdout.write(self.style.SUCCESS("Portal is ready for academic operations and audit verification."))
        self.stdout.write(self.style.SUCCESS("=" * 70))
