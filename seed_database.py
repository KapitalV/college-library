import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from django.contrib.auth.models import User
from apps.core.models import SiteSettings, MenuItem
from apps.departments.models import Department, Subject
from apps.catalog.models import Category, Book, BookCopy
from apps.resources.models import DigitalResource
from apps.notices.models import Notice
from apps.events.models import LibraryEvent, GalleryImage
from apps.pages.models import LibraryStaff, LibraryCommitteeMember, Facility, FAQ
from apps.library_services.models import DownloadableForm
from apps.accounts.models import StaffProfile

def seed():
    print("🌱 Seeding College Institutional Library Database with verified academic data...")

    # 1. Superuser / Librarian
    user, created = User.objects.get_or_create(username='admin', defaults={
        'email': 'library.mmit@gmail.com',
        'first_name': 'Abhinav',
        'last_name': 'Shesha',
        'is_staff': True,
        'is_superuser': True,
    })
    if created:
        user.set_password('Librarian@MMIT2026!')
        user.save()
        print("  ✓ Created Super Administrator: admin / Librarian@MMIT2026!")
    else:
        user.set_password('Librarian@MMIT2026!')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print("  ✓ Updated Super Administrator password.")

    if hasattr(user, 'staff_profile'):
        profile = user.staff_profile
        profile.role = 'ADMIN'
        profile.designation = 'Chief Librarian & Information Officer'
        profile.phone = '+91-9450342615'
        profile.save()

    # 2. SiteSettings
    settings = SiteSettings.load()
    settings.college_name = "Mahamaya Polytechnic of Information Technology"
    settings.library_name = "Central Institutional Library"
    settings.short_name = "MMIT Central Library"
    settings.affiliation_info = "Approved by AICTE, New Delhi & Affiliated to Board of Technical Education Uttar Pradesh (BTEUP)"
    settings.tagline = "Central Hub for Academic Excellence, Technical Research & Digital Learning"
    settings.campus_location = "Mati Road, Akbarpur"
    settings.district = "Kanpur Dehat"
    settings.state = "Uttar Pradesh"
    settings.postal_code = "209101"
    settings.contact_phone = "+91-9450342615"
    settings.library_email = "library.mmit@gmail.com"
    settings.principal_email = "ppl.mmitmati@gmail.com"
    settings.college_website_url = "http://bteup.ac.in"
    settings.opening_hours_weekday = "Monday to Saturday: 10:00 AM – 05:00 PM"
    settings.opening_hours_weekend = "Sunday & Gazetted Holidays: Closed"
    settings.reading_hall_hours = "09:30 AM – 05:30 PM (Air-cooled Silent Study Zone)"
    settings.hero_title = "Welcome to MMIT Central Library"
    settings.hero_subtitle = "Empowering diploma engineers and technical scholars with extensive curricula book collections, digital e-resources, previous year question banks, and research facilities."
    settings.footer_about = "The Central Library of Mahamaya Polytechnic of Information Technology (MMIT), Akbarpur, Kanpur Dehat, serves as the academic nerve center of the institution, providing comprehensive information support mapped strictly to the BTEUP diploma curricula."
    settings.save()
    print("  ✓ Seeded SiteSettings.")

    # 3. Departments
    dept_data = [
        {
            'name': 'Computer Science & Engineering',
            'code': 'CSE',
            'slug': 'computer-science-engineering',
            'icon': 'bi-laptop',
            'head': 'Er. Rajesh Kumar',
            'capacity': 60,
            'desc': 'Focuses on programming, algorithms, database management, web systems, operating systems, computer networking, and cloud computing mapped to BTEUP syllabus.',
            'order': 1
        },
        {
            'name': 'Civil Engineering',
            'code': 'CIVIL',
            'slug': 'civil-engineering',
            'icon': 'bi-building',
            'head': 'Er. Suraj Pratap Singh',
            'capacity': 60,
            'desc': 'Covers surveying, building construction, concrete technology, structural mechanics, water supply, transportation, and geotechnical engineering.',
            'order': 2
        },
        {
            'name': 'Electronics Engineering',
            'code': 'ECE',
            'slug': 'electronics-engineering',
            'icon': 'bi-cpu',
            'head': 'Er. Amit Sachan',
            'capacity': 60,
            'desc': 'Emphasizes analog & digital electronics, microprocessors, communication engineering, signals, IoT, and embedded microcontroller systems.',
            'order': 3
        },
        {
            'name': 'Electrical Engineering',
            'code': 'EE',
            'slug': 'electrical-engineering',
            'icon': 'bi-lightning-charge',
            'head': 'Er. Sandeep Shukla',
            'capacity': 60,
            'desc': 'Covers power systems, electrical machines, switchgear, circuit theory, control systems, and renewable energy technologies.',
            'order': 4
        },
        {
            'name': 'Applied Sciences & Humanities',
            'code': 'ASH',
            'slug': 'applied-sciences-humanities',
            'icon': 'bi-calculator',
            'head': 'Dr. Siddharth Singh',
            'capacity': 120,
            'desc': 'Provides foundational training in Applied Mathematics, Applied Physics, Applied Chemistry, and Technical Communication Skills for first-year students.',
            'order': 5
        },
    ]

    dept_objs = {}
    for d in dept_data:
        obj, _ = Department.objects.get_or_create(
            code=d['code'],
            defaults={
                'name': d['name'],
                'slug': d['slug'],
                'icon': d['icon'],
                'head_of_department': d['head'],
                'intake_capacity': d['capacity'],
                'description': d['desc'],
                'display_order': d['order'],
                'is_active': True,
            }
        )
        dept_objs[d['code']] = obj
    print(f"  ✓ Seeded {len(dept_objs)} Academic Departments.")

    # 4. Subjects
    subjects_data = [
        # CSE
        ('CSE', 'Communication Skills-I', 'CS-101', 1),
        ('CSE', 'Applied Mathematics-I', 'CS-102', 1),
        ('CSE', 'Applied Physics-I', 'CS-103', 1),
        ('CSE', 'Applied Chemistry', 'CS-104', 1),
        ('CSE', 'Fundamentals of Computer & IT', 'CS-105', 1),
        ('CSE', 'Applied Mathematics-II', 'CS-201', 2),
        ('CSE', 'Applied Physics-II', 'CS-202', 2),
        ('CSE', 'Basics of Electrical & Electronics', 'CS-203', 2),
        ('CSE', 'Programming in C', 'CS-204', 2),
        ('CSE', 'Applied Mathematics-III', 'CS-301', 3),
        ('CSE', 'Data Structures using C', 'CS-302', 3),
        ('CSE', 'Digital Electronics', 'CS-303', 3),
        ('CSE', 'Database Management System (DBMS)', 'CS-401', 4),
        ('CSE', 'Operating Systems', 'CS-402', 4),
        ('CSE', 'Object Oriented Programming using Java', 'CS-403', 4),
        ('CSE', 'Computer Networks', 'CS-501', 5),
        ('CSE', 'Software Engineering', 'CS-502', 5),
        ('CSE', 'Web Development & PHP', 'CS-503', 5),
        ('CSE', 'Cloud Computing & Python', 'CS-601', 6),
        ('CSE', 'Information Security & Cyber Laws', 'CS-602', 6),
        
        # CIVIL
        ('CIVIL', 'Applied Mathematics-I', 'CE-101', 1),
        ('CIVIL', 'Building Materials', 'CE-102', 1),
        ('CIVIL', 'Engineering Mechanics', 'CE-201', 2),
        ('CIVIL', 'Surveying-I', 'CE-301', 3),
        ('CIVIL', 'Building Construction', 'CE-302', 3),
        ('CIVIL', 'Concrete Technology', 'CE-401', 4),
        ('CIVIL', 'Hydraulics & Hydraulic Machines', 'CE-402', 4),
        ('CIVIL', 'Design of Reinforced Concrete Structures (RCC)', 'CE-501', 5),
        ('CIVIL', 'Highway Engineering & Transportation', 'CE-502', 5),
        ('CIVIL', 'Estimating, Costing & Valuation', 'CE-601', 6),

        # ECE
        ('ECE', 'Electronic Components & Devices', 'EC-201', 2),
        ('ECE', 'Network Filters & Transmission Lines', 'EC-301', 3),
        ('ECE', 'Principles of Communication Engineering', 'EC-401', 4),
        ('ECE', 'Microprocessors & Peripheral Devices (8085/8086)', 'EC-501', 5),
        ('ECE', 'Modern Communication Systems & IoT', 'EC-601', 6),

        # EE
        ('EE', 'Basic Electrical Engineering', 'EE-101', 1),
        ('EE', 'Electrical & Electronics Engineering Materials', 'EE-201', 2),
        ('EE', 'Electrical Machines-I', 'EE-301', 3),
        ('EE', 'Electrical Machines-II', 'EE-401', 4),
        ('EE', 'Switchgear & Protection', 'EE-501', 5),
        ('EE', 'Utilization of Electrical Energy & Traction', 'EE-601', 6),

        # ASH
        ('ASH', 'Applied Mathematics-I (A & B)', 'AS-101', 1),
        ('ASH', 'Applied Physics-I', 'AS-102', 1),
        ('ASH', 'Applied Chemistry', 'AS-103', 1),
        ('ASH', 'Communication Skills-I', 'AS-104', 1),
        ('ASH', 'Applied Mathematics-II', 'AS-201', 2),
    ]

    for d_code, s_name, s_code, sem in subjects_data:
        Subject.objects.get_or_create(
            department=dept_objs[d_code],
            code=s_code,
            semester=sem,
            defaults={'name': s_name, 'is_active': True}
        )
    print("  ✓ Seeded BTEUP Curricula Subjects across all semesters.")

    # 5. Book Categories
    categories = [
        ('Core Textbooks', 'Prescribed standard textbooks mapped to BTEUP syllabus'),
        ('Reference Books', 'Advanced reference volumes, handbooks, and encyclopedias'),
        ('Book Bank Scheme', 'Special semester-long loan collection for eligible students'),
        ('Donated Faculty Collection', 'Books gifted by faculty members and alumni'),
        ('Competitive & Entrance Exam', 'GATE, JE, SSC-JE, and PSU technical preparation guides'),
        ('Magazines & Periodicals', 'Technical journals, science magazines, and bulletins'),
    ]
    cat_objs = {}
    for idx, (cname, cdesc) in enumerate(categories, start=1):
        c, _ = Category.objects.get_or_create(name=cname, defaults={'description': cdesc, 'display_order': idx})
        cat_objs[cname] = c
    print("  ✓ Seeded Book Categories.")

    # 6. Realistic Books & Accession Copies
    books_data = [
        {
            'title': 'Programming in ANSI C',
            'author': 'E. Balagurusamy',
            'isbn': '978-9351343202',
            'publisher': 'McGraw Hill Education',
            'edition': '8th Edition',
            'year': 2022,
            'dept': 'CSE',
            'cat': 'Core Textbooks',
            'call_no': '005.133 / BAL',
            'desc': 'Standard prescribed textbook for BTEUP 2nd semester Programming in C course. Covers data types, pointers, structures, file handling, and algorithms.',
            'copies': 12,
            'is_new': False,
            'is_donated': False,
        },
        {
            'title': 'Data Structures with C (Schaum’s Outlines)',
            'author': 'Seymour Lipschutz',
            'isbn': '978-0070701984',
            'publisher': 'McGraw Hill',
            'edition': 'Revised 1st Edition',
            'year': 2021,
            'dept': 'CSE',
            'cat': 'Core Textbooks',
            'call_no': '005.73 / LIP',
            'desc': 'Comprehensive algorithmic coverage of arrays, linked lists, stacks, queues, trees, graphs, sorting, and searching for diploma students.',
            'copies': 10,
            'is_new': True,
            'is_donated': False,
        },
        {
            'title': 'Database System Concepts',
            'author': 'Abraham Silberschatz, Henry F. Korth, S. Sudarshan',
            'isbn': '978-0078022159',
            'publisher': 'McGraw-Hill Education',
            'edition': '7th Edition',
            'year': 2020,
            'dept': 'CSE',
            'cat': 'Reference Books',
            'call_no': '005.74 / SIL',
            'desc': 'Authoritative reference on relational data models, SQL queries, normalization, transaction processing, indexing, and NoSQL fundamentals.',
            'copies': 6,
            'is_new': False,
            'is_donated': False,
        },
        {
            'title': 'Operating System Concepts',
            'author': 'Abraham Silberschatz, Peter B. Galvin, Greg Gagne',
            'isbn': '978-1118063330',
            'publisher': 'Wiley India',
            'edition': '9th Edition',
            'year': 2021,
            'dept': 'CSE',
            'cat': 'Core Textbooks',
            'call_no': '005.43 / SIL',
            'desc': 'Covers processes, CPU scheduling, synchronization, deadlocks, memory management, virtual memory, and secondary storage.',
            'copies': 8,
            'is_new': False,
            'is_donated': False,
        },
        {
            'title': 'Building Materials',
            'author': 'S.K. Duggal',
            'isbn': '978-9389538359',
            'publisher': 'New Age International',
            'edition': '5th Edition',
            'year': 2021,
            'dept': 'CIVIL',
            'cat': 'Core Textbooks',
            'call_no': '691.07 / DUG',
            'desc': 'Essential civil engineering textbook covering rocks, stones, bricks, cement, concrete, timber, metals, and sustainable building composites.',
            'copies': 14,
            'is_new': False,
            'is_donated': True,
            'donor': 'Shri Suraj Pratap Singh (Civil)'
        },
        {
            'title': 'Surveying (Vol. I & II)',
            'author': 'Dr. B.C. Punmia, Ashok Kumar Jain, Arun Kumar Jain',
            'isbn': '978-8170088530',
            'publisher': 'Laxmi Publications',
            'edition': '17th Edition',
            'year': 2022,
            'dept': 'CIVIL',
            'cat': 'Core Textbooks',
            'call_no': '526.9 / PUN',
            'desc': 'Comprehensive text for chain surveying, compass surveying, plane table, theodolite, leveling, contouring, curves, and total stations.',
            'copies': 15,
            'is_new': True,
            'is_donated': False,
        },
        {
            'title': 'Reinforced Concrete Structures (Limit State Design)',
            'author': 'Dr. H.J. Shah & A.K. Jain',
            'isbn': '978-9380358482',
            'publisher': 'Charotar Publishing House',
            'edition': '11th Edition',
            'year': 2023,
            'dept': 'CIVIL',
            'cat': 'Reference Books',
            'call_no': '624.18341 / SHA',
            'desc': 'Design of singly and doubly reinforced beams, slabs, columns, and footings based on Indian Standards IS 456:2000.',
            'copies': 8,
            'is_new': True,
            'is_donated': False,
        },
        {
            'title': 'Electronic Principles',
            'author': 'Albert Malvino, David J. Bates',
            'isbn': '978-0073373881',
            'publisher': 'McGraw Hill India',
            'edition': '8th Edition',
            'year': 2020,
            'dept': 'ECE',
            'cat': 'Core Textbooks',
            'call_no': '621.381 / MAL',
            'desc': 'Semiconductor physics, diodes, bipolar junction transistors, FETs, operational amplifiers, oscillators, and power supplies.',
            'copies': 10,
            'is_new': False,
            'is_donated': False,
        },
        {
            'title': 'Digital Logic and Computer Design',
            'author': 'M. Morris Mano',
            'isbn': '978-9332542525',
            'publisher': 'Pearson Education',
            'edition': '1st Edition',
            'year': 2017,
            'dept': 'ECE',
            'cat': 'Core Textbooks',
            'call_no': '621.3815 / MAN',
            'desc': 'Boolean algebra, logic gates, combinational logic, flip-flops, synchronous and asynchronous counters, and memory architecture.',
            'copies': 9,
            'is_new': False,
            'is_donated': False,
        },
        {
            'title': 'Microprocessor Architecture, Programming, and Applications with the 8085',
            'author': 'Ramesh S. Gaonkar',
            'isbn': '978-8187972884',
            'publisher': 'Penram International',
            'edition': '6th Edition',
            'year': 2020,
            'dept': 'ECE',
            'cat': 'Core Textbooks',
            'call_no': '004.165 / GAO',
            'desc': 'Classic reference for 8085 instruction set, timing diagrams, interrupt handling, memory interfacing, and I/O programming.',
            'copies': 8,
            'is_new': False,
            'is_donated': False,
        },
        {
            'title': 'A Textbook of Electrical Technology (Vol. I - Basic Electrical)',
            'author': 'B.L. Theraja, A.K. Theraja',
            'isbn': '978-8121924405',
            'publisher': 'S. Chand Publishing',
            'edition': 'Revised Multicolor Edition',
            'year': 2022,
            'dept': 'EE',
            'cat': 'Core Textbooks',
            'call_no': '621.3 / THE',
            'desc': 'Fundamental DC and AC circuits, magnetic circuits, electromagnetic induction, electrostatics, single-phase and three-phase power.',
            'copies': 18,
            'is_new': True,
            'is_donated': False,
        },
        {
            'title': 'A Textbook of Applied Mathematics for Polytehnics (Vol. I & II)',
            'author': 'Dr. Siddharth Singh & Dr. H.K. Dass',
            'isbn': '978-8121903769',
            'publisher': 'S. Chand & Co.',
            'edition': 'Revised 2024 Edition',
            'year': 2024,
            'dept': 'ASH',
            'cat': 'Donated Faculty Collection',
            'call_no': '510.2462 / SIN',
            'desc': 'Specially donated copy by Dr. Siddharth Singh covering algebra, trigonometry, differential calculus, integral calculus, and vectors for BTEUP 1st year.',
            'copies': 6,
            'is_new': True,
            'is_donated': True,
            'donor': 'Shri Siddharth Singh (Maths)'
        },
        {
            'title': 'Applied Chemistry for Engineering & Technology',
            'author': 'Dr. Ravi Rajak & Dr. Sunita Rattan',
            'isbn': '978-9350143896',
            'publisher': 'S.K. Kataria & Sons',
            'edition': '4th Edition',
            'year': 2023,
            'dept': 'ASH',
            'cat': 'Donated Faculty Collection',
            'call_no': '540.2462 / RAJ',
            'desc': 'Donated by Shri Ravi Rajak. Covers water treatment, fuels & combustion, lubricants, polymers, electrochemistry, and corrosion science.',
            'copies': 5,
            'is_new': True,
            'is_donated': True,
            'donor': 'Shri Ravi Rajak (Chemistry)'
        },
        {
            'title': 'Library and Information Science Handbook (Institutional Manual)',
            'author': 'Shri Abhinav Shesha',
            'isbn': '978-9388881234',
            'publisher': 'Central Library Publications, MMIT',
            'edition': '1st Edition',
            'year': 2024,
            'dept': 'ASH',
            'cat': 'Donated Faculty Collection',
            'call_no': '020.71 / SHE',
            'desc': 'Donated by Librarian Shri Abhinav Shesha for student orientation, OPAC guidance, e-Granthalaya cataloging standards, and NDLI club registration.',
            'copies': 4,
            'is_new': True,
            'is_donated': True,
            'donor': 'Shri Abhinav Shesha (Librarian)'
        },
    ]

    accession_counter = 1001
    for b_info in books_data:
        dept = dept_objs[b_info['dept']]
        cat = cat_objs[b_info['cat']]
        book, b_created = Book.objects.get_or_create(
            title=b_info['title'],
            author=b_info['author'],
            defaults={
                'isbn': b_info['isbn'],
                'publisher': b_info['publisher'],
                'edition': b_info['edition'],
                'publication_year': b_info['year'],
                'department': dept,
                'category': cat,
                'classification_number': b_info['call_no'],
                'description': b_info['desc'],
                'is_featured': True,
                'is_new_arrival': b_info['is_new'],
                'is_donated': b_info.get('is_donated', False),
                'donor_name': b_info.get('donor', ''),
                'tags': f"{dept.code}, BTEUP, Semester Text, {cat.name}"
            }
        )

        # Create physical copies
        for copy_idx in range(b_info['copies']):
            acc_code = f"MMIT-ACC-{accession_counter:05d}"
            shelf = f"Rack {((accession_counter - 1000) // 10) + 1} - Shelf {chr(65 + (copy_idx % 4))}"
            status = 'REFERENCE_ONLY' if copy_idx == 0 and cat.name == 'Reference Books' else 'AVAILABLE'
            BookCopy.objects.get_or_create(
                accession_number=acc_code,
                defaults={
                    'book': book,
                    'shelf_location': shelf,
                    'status': status,
                    'price': 450.00,
                }
            )
            accession_counter += 1

    print(f"  ✓ Seeded {len(books_data)} Books and {accession_counter - 1001} physical inventory copies with real accession numbers.")

    # 7. Digital Resources (Question Papers, Syllabus, Notes, National Portals)
    resources_data = [
        # Question Papers (BTEUP Board Exams)
        {
            'title': 'BTEUP Board Exam Question Paper: Programming in C (Summer 2024)',
            'cat': 'QUESTION_PAPER',
            'dept': 'CSE',
            'sem': 2,
            'year': '2023-24',
            'author': 'Board of Technical Education U.P. (BTEUP)',
            'desc': 'Official previous year question paper with complete question set for diploma 2nd semester CSE examinations.',
            'format': 'PDF',
            'ext_url': 'https://drive.google.com/drive/folders/1_9Vn4YkrXmGxdYHIQiXHcRcrW5XSjAP0?usp=sharing'
        },
        {
            'title': 'BTEUP Board Exam Question Paper: Data Structures using C (Winter 2023)',
            'cat': 'QUESTION_PAPER',
            'dept': 'CSE',
            'sem': 3,
            'year': '2023-24',
            'author': 'BTEUP Lucknow',
            'desc': 'Previous year semester examination paper covering Stacks, Queues, Binary Trees, and Sorting algorithms.',
            'format': 'PDF',
            'ext_url': 'https://drive.google.com/drive/folders/1_9Vn4YkrXmGxdYHIQiXHcRcrW5XSjAP0?usp=sharing'
        },
        {
            'title': 'BTEUP Board Exam Question Paper: Database Management System (Summer 2024)',
            'cat': 'QUESTION_PAPER',
            'dept': 'CSE',
            'sem': 4,
            'year': '2023-24',
            'author': 'BTEUP Lucknow',
            'desc': 'Annual board question paper testing relational algebra, SQL queries, normalization, and concurrency control.',
            'format': 'PDF',
            'ext_url': 'https://drive.google.com/drive/folders/1_9Vn4YkrXmGxdYHIQiXHcRcrW5XSjAP0?usp=sharing'
        },
        {
            'title': 'BTEUP Board Exam Question Paper: Building Materials & Construction (2023)',
            'cat': 'QUESTION_PAPER',
            'dept': 'CIVIL',
            'sem': 1,
            'year': '2022-23',
            'author': 'BTEUP Lucknow',
            'desc': 'Civil engineering 1st year board examination questions covering bricks, cement testing, mortars, and timber.',
            'format': 'PDF',
            'ext_url': 'https://drive.google.com/drive/folders/1_9Vn4YkrXmGxdYHIQiXHcRcrW5XSjAP0?usp=sharing'
        },
        {
            'title': 'BTEUP Board Exam Question Paper: Surveying-I (2024)',
            'cat': 'QUESTION_PAPER',
            'dept': 'CIVIL',
            'sem': 3,
            'year': '2023-24',
            'author': 'BTEUP Lucknow',
            'desc': 'Complete examination question set for chain surveying, prismatic compass, and plane table surveying.',
            'format': 'PDF',
            'ext_url': 'https://drive.google.com/drive/folders/1_9Vn4YkrXmGxdYHIQiXHcRcrW5XSjAP0?usp=sharing'
        },
        {
            'title': 'BTEUP Board Exam Question Paper: Basic Electrical Engineering (2023)',
            'cat': 'QUESTION_PAPER',
            'dept': 'EE',
            'sem': 1,
            'year': '2022-23',
            'author': 'BTEUP Lucknow',
            'desc': 'Board examination questions on Kirchhoff laws, AC circuits, single-phase transformers, and DC machines.',
            'format': 'PDF',
            'ext_url': 'https://drive.google.com/drive/folders/1_9Vn4YkrXmGxdYHIQiXHcRcrW5XSjAP0?usp=sharing'
        },
        
        # Syllabus
        {
            'title': 'BTEUP Curriculum & Detailed Syllabus: Diploma in Computer Science & Engineering',
            'cat': 'SYLLABUS',
            'dept': 'CSE',
            'sem': 1,
            'year': '2024-25',
            'author': 'IRDT Kanpur & BTEUP Lucknow',
            'desc': 'Complete approved 3-year semester-wise curriculum, examination scheme, marks distribution, and lab course outlines.',
            'format': 'PDF',
            'ext_url': 'https://bteup.ac.in/webapp/SYLLABUS.aspx?type=19'
        },
        {
            'title': 'BTEUP Curriculum & Detailed Syllabus: Diploma in Civil Engineering',
            'cat': 'SYLLABUS',
            'dept': 'CIVIL',
            'sem': 1,
            'year': '2024-25',
            'author': 'BTEUP Lucknow',
            'desc': 'Updated 3-year curriculum structure, industrial training guidelines, and laboratory practical requirements.',
            'format': 'PDF',
            'ext_url': 'https://bteup.ac.in/webapp/SYLLABUS.aspx?type=19'
        },
        {
            'title': 'BTEUP Curriculum & Detailed Syllabus: Diploma in Electronics Engineering',
            'cat': 'SYLLABUS',
            'dept': 'ECE',
            'sem': 1,
            'year': '2024-25',
            'author': 'BTEUP Lucknow',
            'desc': 'Curriculum specifications including Microprocessors, Digital Electronics, and Communication Engineering.',
            'format': 'PDF',
            'ext_url': 'https://bteup.ac.in/webapp/SYLLABUS.aspx?type=19'
        },

        # Lecture Notes
        {
            'title': 'Lecture Notes & PPT: Applied Mathematics-I (Matrices & Trigonometry)',
            'cat': 'LECTURE_NOTES',
            'dept': 'ASH',
            'sem': 1,
            'year': '2024-25',
            'author': 'Dr. Siddharth Singh (HOD Applied Sciences)',
            'desc': 'Comprehensive lecture presentation and worked step-by-step example problem sheets for freshers.',
            'format': 'PPT',
            'ext_url': 'https://librarymmit.blogspot.com/'
        },
        {
            'title': 'Classroom Handout: Building Materials (Stone, Brick & Cement Testing)',
            'cat': 'LECTURE_NOTES',
            'dept': 'CIVIL',
            'sem': 1,
            'year': '2024-25',
            'author': 'Er. Suraj Pratap Singh (Faculty Civil)',
            'desc': 'Field testing procedures, IS code specifications, and laboratory testing manuals prepared for students.',
            'format': 'PDF',
            'ext_url': 'https://librarymmit.blogspot.com/'
        },
        {
            'title': 'Faculty PPT & Code Samples: Data Structures in C (Trees and Graphs)',
            'cat': 'LECTURE_NOTES',
            'dept': 'CSE',
            'sem': 3,
            'year': '2024-25',
            'author': 'Er. Rajesh Kumar (Faculty CSE)',
            'desc': 'Detailed lecture slides with commented C code implementations of BST, AVL trees, BFS, and DFS traversals.',
            'format': 'PDF',
            'ext_url': 'https://librarymmit.blogspot.com/'
        },

        # National Educational Portals
        {
            'title': 'National Digital Library of India (NDLI)',
            'cat': 'PORTAL',
            'dept': 'ASH',
            'sem': None,
            'year': '',
            'author': 'Ministry of Education & IIT Kharagpur',
            'desc': 'Over 9 crore full-text academic resources, e-books, thesis papers, articles, and audio-video lectures.',
            'format': 'LINK',
            'ext_url': 'https://ndl.iitkgp.ac.in/'
        },
        {
            'title': 'AICTE e-KUMBH Portal (Knowledge Unleashed in Multiple Bharatiya Languages)',
            'cat': 'PORTAL',
            'dept': 'ASH',
            'sem': None,
            'year': '',
            'author': 'All India Council for Technical Education (AICTE)',
            'desc': 'High-quality technical textbooks translated into 12 Indian regional languages including Hindi for diploma engineering students.',
            'format': 'LINK',
            'ext_url': 'https://ekumbh.aicte-india.org/'
        },
        {
            'title': 'e-Granthalaya 4.0 Cloud Portal (NIC)',
            'cat': 'PORTAL',
            'dept': 'ASH',
            'sem': None,
            'year': '',
            'author': 'National Informatics Centre (NIC), Govt. of India',
            'desc': 'Cloud-based integrated library management system powering institutional OPAC and union catalogues.',
            'format': 'LINK',
            'ext_url': 'http://eg4.nic.in/'
        },
        {
            'title': 'SWAYAM & NPTEL Online Learning Platform',
            'cat': 'PORTAL',
            'dept': 'ASH',
            'sem': None,
            'year': '',
            'author': 'Ministry of Education & IITs/IISc',
            'desc': 'Free video lectures, self-paced certification courses, and tutorials delivered by top IIT professors.',
            'format': 'LINK',
            'ext_url': 'https://swayam.gov.in/'
        },
    ]

    for r in resources_data:
        dept = dept_objs.get(r['dept'])
        DigitalResource.objects.get_or_create(
            title=r['title'],
            defaults={
                'category': r['cat'],
                'department': dept,
                'semester': r['sem'],
                'academic_year': r['year'],
                'author_or_faculty': r['author'],
                'description': r['desc'],
                'file_format': r['format'],
                'external_url': r['ext_url'],
                'access_type': 'OPEN_ACCESS',
                'is_published': True,
                'is_featured': True,
            }
        )
    print("  ✓ Seeded Digital Resources (Question Papers, Syllabus, Notes, National Portals).")

    # 8. Verified Notices & Circulars
    notices_data = [
        {
            'title': 'Welcome Newly Admitted Students! Orientation Programme (Session 2026-27)',
            'cat': 'ORIENTATION',
            'priority': 'URGENT',
            'pinned': True,
            'summary': 'Orientation schedule for freshers admitted to MMIT Akbarpur, Kanpur Dehat from August 01 to August 14, 2026.',
            'content': """महामाया पॉलीटेक्निक ऑफ इंफॉर्मेशन टेक्नोलॉजी (M.M.I.T.), अकबरपुर, कानपुर देहात में सत्र 2026-27 के सभी प्रथम वर्ष (Freshers) के विद्यार्थियों का हार्दिक स्वागत है।

📅 अवधि: 1 अगस्त से 14 अगस्त 2026
🏛️ स्थान: SEMINAR HALL, M.M.I.T. परिसर
🎯 ध्येय: Dream • Learn • Achieve

ओरिएंटेशन प्रोग्राम में क्या खास रहेगा?
1. संस्थान एवं प्रयोगशाला परिचय: वर्कशॉप और लैब भ्रमण।
2. लाइब्रेरी सेशन: पुस्तक निर्गमन नियम, ई-लाइब्रेरी एक्सेस और NDLI क्लब पंजीकरण।
3. अकादमिक एवं परीक्षा जानकारी: BTEUP पाठ्यक्रम एवं अनुशासन नियम।
4. हॉस्टल गाइडलाइंस: आवास एवं एंटी-रैगिंग नियमों पर संवाद।

सभी नव-प्रवेशित छात्र-छात्राएं निर्धारित समय पर सेमिनार हॉल में उपस्थित हों।""",
        },
        {
            'title': 'A Student’s Guide to MMIT Library: Resources, OPAC & NDLI Club Access',
            'cat': 'ACADEMIC',
            'priority': 'HIGH',
            'pinned': True,
            'summary': 'Comprehensive guide on discovering books via OPAC, issuing textbooks, and joining the NDLI Club.',
            'content': """Welcome to the MMIT Library! The Library supports students and faculty in their academic learning, teaching, and information needs.

Key Guidelines for Students:
1. Explore Library Resources: Textbooks mapped to BTEUP syllabus, reference handbooks, and previous year question papers.
2. Search Books through OPAC: Use the online catalogue to locate books by Title, Author, or Accession Number.
3. Follow Library Etiquette: Maintain strict silence in reading hall. Identity card is mandatory at the entrance.
4. Book Circulation: Diploma students are entitled to borrow 2 books for a period of 14 days.
5. NDLI Club Membership: Mandatory registration on National Digital Library portal with college passkey.

For any queries, meet Librarian Shri Abhinav Shesha in the Central Library during working hours (10:00 AM – 05:00 PM).""",
        },
        {
            'title': 'Faculty Book Donation Drive: Heartfelt Thanks to Our Esteemed Donors',
            'cat': 'DONATION',
            'priority': 'NORMAL',
            'pinned': False,
            'summary': 'Acknowledgment of book donations by faculty members Shri Siddharth Singh, Shri Suraj Pratap Singh, Shri Ravi Rajak, and Librarian Shri Abhinav Shesha.',
            'content': """The Central Library gratefully acknowledges and appreciates the generous contribution of books by our faculty members:

• Shri Siddharth Singh (Mathematics)
• Shri Suraj Pratap Singh (Civil Engineering)
• Shri Ravi Rajak (Chemistry)
• Shri Abhinav Shesha (Librarian)

These textbooks and reference materials have been cataloged into the library collection and are now available for students in the Reading Hall and Book Bank Section.""",
        },
        {
            'title': 'Mandatory NDLI Club Registration for All Diploma Students (Joint Directorate Circular)',
            'cat': 'CIRCULAR',
            'priority': 'HIGH',
            'pinned': False,
            'summary': 'Directives from Joint Director, Technical Education, Bundelkhand & Kanpur Region regarding NDLI membership.',
            'content': """As per the directives received from the Joint Director, Technical Education, Bundelkhand & Kanpur Region, all registered polytechnic students must enroll with the National Digital Library of India (NDLI) Club.

Registration Steps:
Step 1: Open NDLI Registration page (https://ndl.iitkgp.ac.in/account/registration) and sign up with your college email/roll number.
Step 2: Visit NDLI Club Join portal (https://club.ndl.iitkgp.ac.in/sign-up) and enter the MMIT Institutional Passkey provided by the Library.

Submit your NDLI Club confirmation receipt to the Library property counter to validate your library membership.""",
        },
        {
            'title': 'Book Bank Distribution Schedule for Odd Semester Students (Session 2026-27)',
            'cat': 'BOOK_BANK',
            'priority': 'NORMAL',
            'pinned': False,
            'summary': 'Distribution of semester-long textbook sets under the institutional Book Bank scheme.',
            'content': """Book Bank textbook distribution for 1st, 3rd, and 5th Semester diploma students will commence next Monday.
Eligible students should submit their Book Bank Application Form along with a photocopy of their College ID Card and fee receipt.
Each student will be allocated up to 4 textbooks for the entire semester duration.""",
        },
    ]

    for n in notices_data:
        Notice.objects.get_or_create(
            title=n['title'],
            defaults={
                'category': n['cat'],
                'priority': n['priority'],
                'is_pinned': n['pinned'],
                'short_summary': n['summary'],
                'content': n['content'],
                'is_active': True,
            }
        )
    print("  ✓ Seeded Notices & Circulars.")

    # 9. Events & Gallery
    ev, _ = LibraryEvent.objects.get_or_create(
        title="Fresher Orientation & Library Immersion Session 2026",
        defaults={
            'event_type': 'ORIENTATION',
            'venue': 'Seminar Hall & Central Library Stack Room',
            'start_date': '2026-08-01',
            'end_date': '2026-08-14',
            'summary': 'Orientation program for 2026-27 freshers covering library card issuance, OPAC search, and NDLI club registration.',
            'description': 'A two-week orientation designed to acclimatize first-year diploma students to the technical institute curriculum, library resources, digital labs, and research opportunities.',
            'is_featured': True,
            'is_active': True,
        }
    )

    ev2, _ = LibraryEvent.objects.get_or_create(
        title="National Library Week & Technical Book Fair",
        defaults={
            'event_type': 'BOOK_FAIR',
            'venue': 'Central Library Reading Hall',
            'start_date': '2026-11-14',
            'end_date': '2026-11-20',
            'summary': 'Exhibition of newly acquired engineering reference books, journals, and regional language technical publications from AICTE e-KUMBH.',
            'description': 'Annual book exhibition featuring technical volumes from major publishers. Faculty and students submitted acquisition recommendations.',
            'is_featured': True,
            'is_active': True,
        }
    )

    # 10. Library Staff & Advisory Committee
    staff_data = [
        ('Shri Abhinav Shesha', 'Librarian & Head of Information Services', 'M.Lib.I.Sc, UGC-NET', 'LIBRARIAN', 'library.mmit@gmail.com', '+91-9450342615', 'Supervises all library acquisitions, classification, automation via e-Granthalaya, digital library portal management, and student circulation.', 1),
        ('Smt. Sunita Verma', 'Assistant Librarian', 'B.Lib.I.Sc, M.A.', 'ASSISTANT', 'verma.sunita.mmit@gmail.com', '+91-9450342616', 'Manages circulation desk, student cards, book returns, and inventory verification.', 2),
        ('Shri Ram Prakash', 'Library Attendant & Record Keeper', 'Intermediate, Library Apprenticeship', 'ATTENDANT', '', '', 'In charge of book arrangement in stacks, shelving, property counter, and reading hall maintenance.', 3),
    ]
    for s in staff_data:
        LibraryStaff.objects.get_or_create(
            name=s[0],
            defaults={
                'designation': s[1],
                'qualification': s[2],
                'role_type': s[3],
                'email': s[4],
                'phone': s[5],
                'bio': s[6],
                'display_order': s[7],
                'is_active': True,
            }
        )

    committee_data = [
        ('Principal, MMIT Akbarpur', 'Head of Institution', 'MMIT Administration', 'Chairman', 1),
        ('Shri Abhinav Shesha', 'Librarian', 'Central Library', 'Member Secretary', 2),
        ('Dr. Siddharth Singh', 'HOD & Lecturer (Mathematics)', 'Applied Sciences', 'Faculty Representative', 3),
        ('Er. Suraj Pratap Singh', 'Lecturer (Civil Engineering)', 'Civil Engineering', 'Faculty Representative', 4),
        ('Er. Rajesh Kumar', 'Lecturer (Computer Science)', 'Computer Science & Engineering', 'Faculty Representative', 5),
    ]
    for c in committee_data:
        LibraryCommitteeMember.objects.get_or_create(
            name=c[0],
            defaults={
                'designation': c[1],
                'department': c[2],
                'committee_role': c[3],
                'display_order': c[4],
            }
        )
    print("  ✓ Seeded Library Staff & Advisory Committee.")

    # 11. Facilities
    facilities_data = [
        ('Spacious Reading Hall', 'bi-journal-bookmark-fill', 'Comfortable seating for uninterrupted self-study, well-ventilated and air-cooled with natural daylight.', '120 Seater', '09:30 AM – 05:30 PM', 'Ergonomic seating\nSilent study zone\nNewspaper reading desks\nDirect stack access', 1),
        ('OPAC & Digital Library Lab', 'bi-pc-display-horizontal', 'Dedicated computer terminals equipped with high-speed internet for searching e-Granthalaya 4.0 OPAC, NDLI resources, and NPTEL video lectures.', '20 High-Speed Terminals', '10:00 AM – 05:00 PM', 'e-Granthalaya OPAC search\nNDLI Club access\nSWAYAM/NPTEL downloads\nAICTE e-KUMBH e-books', 2),
        ('BTEUP Question Bank & Reference Section', 'bi-archive-fill', 'Comprehensive physical archive of previous 10 years of Board of Technical Education Uttar Pradesh exam question papers and solutions.', 'Reference Stacks', '10:00 AM – 05:00 PM', '10-Year BTEUP papers\nSemester syllabus copies\nProject reports archive\nEngineering handbooks', 3),
        ('Book Bank Section', 'bi-collection-fill', 'Subsidized semester textbook lending facility dedicated to SC/ST, OBC, and meritorious diploma students.', '3,500+ Volumes', '10:00 AM – 04:00 PM', 'Up to 4 books per semester\nComplete syllabus coverage\nLong-term loan period\nZero recurring fee', 4),
        ('Periodicals & Daily Newspapers', 'bi-newspaper', 'Subscription to leading Hindi and English national dailies, technical science magazines, and employment news.', 'Periodicals Rack', '10:00 AM – 05:00 PM', 'Dainik Jagran, Amar Ujala, The Hindu\nRozgar Samachar (Weekly)\nTechnical Competition magazines\nScience Reporter', 5),
    ]
    for f in facilities_data:
        Facility.objects.get_or_create(
            title=f[0],
            defaults={
                'icon': f[1],
                'description': f[2],
                'capacity': f[3],
                'timings': f[4],
                'features': f[5],
                'display_order': f[6],
                'is_active': True,
            }
        )
    print("  ✓ Seeded Library Facilities.")

    # 12. FAQs
    faqs_data = [
        ('How do I apply for a Library Membership Card?', 'All newly admitted diploma students can apply online through the Library Services menu or collect the membership form from the library counter. You will need your BTEUP Roll Number, admission fee receipt, and college ID card.', 'MEMBERSHIP', 1),
        ('How many books can a diploma student borrow and for how long?', 'Diploma students are entitled to borrow up to 2 books simultaneously for a duration of 14 days. Faculty members may borrow up to 5 books for 30 days.', 'CIRCULATION', 2),
        ('What is the procedure to join the NDLI Club?', 'Register at ndl.iitkgp.ac.in and join the institutional club at club.ndl.iitkgp.ac.in using the institutional Passkey displayed on the library notice board or available from the librarian.', 'DIGITAL', 3),
        ('How do I obtain a Library Clearance (No-Dues) Certificate?', 'Prior to appearing in final semester exams or receiving your diploma, return all borrowed books, clear any overdue fines, and submit the No-Dues Application Form at the circulation counter.', 'NO_DUES', 4),
        ('Can I access question papers and syllabus copies without logging in?', 'Yes! All BTEUP previous year question papers, diploma curricula, and syllabus copies are freely accessible and downloadable in PDF format under the Academic Resources menu.', 'GENERAL', 5),
    ]
    for q in faqs_data:
        FAQ.objects.get_or_create(
            question=q[0],
            defaults={
                'answer': q[1],
                'category': q[2],
                'display_order': q[3],
                'is_active': True,
            }
        )
    print("  ✓ Seeded FAQs.")

    # 13. Downloadable Forms
    forms_data = [
        ('Library Clearance (No-Dues) Certificate Application Form', 'Mandatory clearance form for final year diploma students completing their course or transferring.', 1),
        ('Book Bank Scheme Application & Agreement Form', 'Application for issuing semester-long textbook bundles under the institutional Book Bank.', 2),
        ('Loss of Book Declaration & Replacement Form', 'Affidavit form to be submitted in case of accidental book loss or damage.', 3),
        ('Student Library Membership Registration Form (Offline)', 'Printable registration form for students wishing to register in person at the circulation counter.', 4),
    ]
    for form_title, form_desc, form_order in forms_data:
        DownloadableForm.objects.get_or_create(
            title=form_title,
            defaults={
                'description': form_desc,
                'order': form_order,
                'is_active': True,
            }
        )
    print("  ✓ Seeded Downloadable Forms.")

    # 14. Menu Items
    menu_items = [
        ('Home', '/', 1, 'bi-house-door', None),
        ('About Library', '/about/', 2, 'bi-info-circle', None),
        ('Library Catalogue', '/catalog/', 3, 'bi-book', None),
        ('Digital Library', '/digital-library/', 4, 'bi-laptop', None),
        ('Academic Resources', '/resources/', 5, 'bi-folder2-open', None),
        ('Library Services', '/services/', 6, 'bi-gear', None),
        ('Notices & Circulars', '/notices/', 7, 'bi-megaphone', None),
        ('Contact', '/contact/', 8, 'bi-telephone', None),
    ]
    for title, url, order, icon, parent in menu_items:
        MenuItem.objects.get_or_create(
            title=title,
            defaults={
                'url': url,
                'order': order,
                'icon': icon,
                'is_active': True,
            }
        )
    print("  ✓ Seeded Navigation Menu Items.")

    print("\n🎉 Database Seeding Completed Successfully! All institutional data is live and consistent.")

if __name__ == '__main__':
    seed()

