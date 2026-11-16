import io
import csv
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.management import call_command

from apps.core.models import SiteSettings, MenuItem
from apps.departments.models import Department, Subject
from apps.catalog.models import Category, Book, BookCopy
from apps.resources.models import DigitalResource
from apps.notices.models import Notice
from apps.library_services.models import MembershipApplication, BookRecommendation, ResourceRequest
from apps.feedback.models import Feedback
from apps.pages.models import Facility, FAQ, LibraryStaff


class LibraryPortalModelTests(TestCase):
    def setUp(self):
        call_command('setup_madhogarh')
        self.settings = SiteSettings.load()
        self.dept = Department.objects.get(code="CSE")
        self.cat, _ = Category.objects.get_or_create(name="Core Textbooks")
        self.subject, _ = Subject.objects.get_or_create(
            department=self.dept,
            name="Programming in C Test",
            code="CS-TEST-101",
            semester=2
        )
        self.book = Book.objects.create(
            title="Programming in ANSI C",
            author="E. Balagurusamy",
            isbn="978-9351343202",
            department=self.dept,
            category=self.cat,
            subject=self.subject,
            publication_year=2022
        )
        self.copy1 = BookCopy.objects.create(
            book=self.book,
            accession_number="GPM-TEST-001",
            shelf_location="Rack 1 - Shelf A",
            status="AVAILABLE"
        )
        self.copy2 = BookCopy.objects.create(
            book=self.book,
            accession_number="GPM-TEST-002",
            shelf_location="Rack 1 - Shelf B",
            status="ISSUED"
        )

    def test_site_settings_singleton_and_madhogarh_facts(self):
        s2 = SiteSettings.load()
        self.assertEqual(s2.pk, self.settings.pk)
        self.assertIn("Government Polytechnic Madhogarh", s2.college_name)
        self.assertEqual(s2.district, "Jalaun")
        self.assertEqual(s2.institution_code, "3318")
        self.assertIn("erp.bizby.io", s2.erp_url)
        self.assertEqual(s2.postal_code, "285126")

    def test_verified_departments_active(self):
        active_depts = Department.objects.filter(is_active=True).order_by('code')
        self.assertEqual(active_depts.count(), 3)
        codes = [d.code for d in active_depts]
        self.assertListEqual(sorted(codes), ['CSE', 'ECE', 'EE'])

    def test_book_copies_and_availability(self):
        self.assertEqual(self.book.total_copies, 2)
        self.assertEqual(self.book.available_copies, 1)
        self.assertTrue(self.book.is_available)

    def test_department_slug_and_branch_code(self):
        cse = Department.objects.get(code='CSE')
        self.assertEqual(cse.slug, "computer-science-engineering")
        self.assertEqual(cse.branch_code, "355")
        self.assertEqual(cse.lateral_code, "389")

    def test_digital_resource_creation(self):
        res = DigitalResource.objects.create(
            title="BTEUP C Programming Question Paper 2024",
            category="QUESTION_PAPER",
            department=self.dept,
            semester=2,
            academic_year="2023-24",
            is_published=True
        )
        self.assertTrue(res.is_published)
        self.assertEqual(res.category, "QUESTION_PAPER")

    def test_notice_priority_and_slug(self):
        notice = Notice.objects.create(
            title="Important Orientation Notice for Freshers 2026",
            category="ORIENTATION",
            priority="URGENT",
            content="Detailed orientation schedule."
        )
        self.assertTrue(notice.slug.startswith("important-orientation-notice"))
        self.assertEqual(notice.priority, "URGENT")


class PublicViewTests(TestCase):
    def setUp(self):
        call_command('setup_madhogarh')
        self.client = Client()
        self.dept = Department.objects.get(code="EE")
        self.cat, _ = Category.objects.get_or_create(name="Reference Books")
        self.book = Book.objects.create(
            title="Electrical Machines Volume 1",
            author="P.S. Bimbhra",
            department=self.dept,
            category=self.cat,
            publication_year=2021
        )
        self.notice = Notice.objects.create(
            title="Book Bank Schedule Notice 2026",
            category="BOOK_BANK",
            content="Book bank distribution next week.",
            is_active=True
        )

    def test_homepage_loads_with_madhogarh_branding(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Government Polytechnic Madhogarh")
        self.assertContains(response, "Jalaun")
        self.assertContains(response, "3318")

    def test_catalog_opac_search(self):
        response = self.client.get(reverse('catalog:search'), {'q': 'Electrical Machines'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Electrical Machines Volume 1")
        self.assertContains(response, "P.S. Bimbhra")

    def test_book_detail_view(self):
        response = self.client.get(reverse('catalog:book_detail', kwargs={'slug': self.book.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Electrical Machines Volume 1")

    def test_department_views(self):
        response = self.client.get(reverse('departments:department_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Electrical Engineering")
        self.assertContains(response, "Computer Science and Engineering")
        self.assertContains(response, "Electronics Engineering")

        detail_resp = self.client.get(reverse('departments:department_detail', kwargs={'slug': self.dept.slug}))
        self.assertEqual(detail_resp.status_code, 200)
        self.assertContains(detail_resp, "Electrical Engineering")

    def test_notices_views(self):
        response = self.client.get(reverse('notices:notice_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Book Bank Schedule Notice 2026")

    def test_membership_application_submission(self):
        payload = {
            'full_name': 'Test Student',
            'applicant_type': 'STUDENT',
            'roll_number': '2101019999',
            'enrollment_number': 'E2101019999',
            'department': self.dept.id,
            'semester': 1,
            'email': 'student.test@example.com',
            'mobile_number': '9876543210',
        }
        response = self.client.post(reverse('services:membership'), data=payload, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(MembershipApplication.objects.filter(roll_number='2101019999').exists())

    def test_feedback_submission(self):
        payload = {
            'name': 'Rahul Sharma',
            'email': 'rahul@example.com',
            'user_type': 'STUDENT',
            'category': 'READING_HALL',
            'rating': 5,
            'subject': 'Excellent Reading Hall',
            'message': 'The air-cooled silent reading hall provides an optimal study space.',
        }
        response = self.client.post(reverse('feedback:feedback'), data=payload, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Feedback.objects.filter(email='rahul@example.com').exists())


class SecurityAndDashboardTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.librarian_user = User.objects.create_user(
            username='librarian_test',
            password='TestPassword123!',
            is_staff=True
        )
        self.anonymous_client = Client()

    def test_anonymous_user_blocked_from_dashboard(self):
        response = self.anonymous_client.get(reverse('dashboard:overview'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_librarian_can_access_dashboard(self):
        self.client.login(username='librarian_test', password='TestPassword123!')
        response = self.client.get(reverse('dashboard:overview'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Executive Librarian Dashboard")

    def test_csv_export(self):
        self.client.login(username='librarian_test', password='TestPassword123!')
        response = self.client.get(reverse('dashboard:export_books_csv'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')
        self.assertIn('AccessionNumber', response.content.decode('utf-8'))
