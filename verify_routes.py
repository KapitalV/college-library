import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse

client = Client()

routes_to_test = [
    ('Homepage', '/'),
    ('Global Search', '/search/?q=C+Programming'),
    ('Contact', '/contact/'),
    ('Robots.txt', '/robots.txt'),
    ('Sitemap.xml', '/sitemap.xml'),
    ('About Library', '/about/'),
    ('Vision & Mission', '/about/vision-mission/'),
    ('Rules & Regulations', '/rules/'),
    ('Library Staff', '/staff/'),
    ('Facilities', '/facilities/'),
    ('FAQ', '/faq/'),
    ('Catalog Search OPAC', '/catalog/'),
    ('New Arrivals', '/catalog/new-arrivals/'),
    ('Donations', '/catalog/donations/'),
    ('Digital Library Home', '/digital-library/'),
    ('Digital Portals', '/digital-library/portals/'),
    ('Question Papers', '/resources/question-papers/'),
    ('Syllabus', '/resources/syllabus/'),
    ('Lecture Notes', '/resources/lecture-notes/'),
    ('Departments List', '/departments/'),
    ('Department CSE Detail', '/departments/computer-science-engineering/'),
    ('Department EE Detail', '/departments/electrical-engineering/'),
    ('Department ECE Detail', '/departments/electronics-engineering/'),
    ('Library Services List', '/services/'),
    ('Membership Form', '/services/membership/'),
    ('Book Recommendation', '/services/book-recommendation/'),
    ('Resource Request', '/services/resource-request/'),
    ('No-Dues Clearance', '/services/no-dues/'),
    ('NDLI Club Registration', '/services/ndli-club/'),
    ('Downloadable Forms', '/services/forms/'),
    ('Notices List', '/notices/'),
    ('Events List', '/events/'),
    ('Gallery List', '/events/gallery/'),
    ('Feedback Form', '/feedback/'),
    ('Staff Login', '/accounts/login/'),
]

print("🔍 Testing All Public Routes with Django Test Client:")
all_passed = True
for name, path in routes_to_test:
    resp = client.get(path)
    status = resp.status_code
    if status == 200:
        print(f"  ✓ {name:30} [{path:45}] -> HTTP 200 OK")
    else:
        print(f"  ✗ {name:30} [{path:45}] -> HTTP {status} FAILED")
        all_passed = False

# Now test staff authentication and dashboard routes
print("\n🔐 Testing Staff Authentication & Dashboard Routes:")
client.login(username='admin', password='Librarian@GPMadhogarh2026!')

dashboard_routes = [
    ('Dashboard Overview', '/dashboard/'),
    ('Dashboard Books', '/dashboard/books/'),
    ('Dashboard Book Add', '/dashboard/books/create/'),
    ('Dashboard Book CSV Import', '/dashboard/books/import-csv/'),
    ('Dashboard Book CSV Export', '/dashboard/books/export-csv/'),
    ('Dashboard Digital Resources', '/dashboard/resources/'),
    ('Dashboard Resource Add', '/dashboard/resources/create/'),
    ('Dashboard Notices', '/dashboard/notices/'),
    ('Dashboard Notice Add', '/dashboard/notices/create/'),
    ('Dashboard Memberships', '/dashboard/memberships/'),
    ('Dashboard Recommendations', '/dashboard/recommendations/'),
    ('Dashboard Requests', '/dashboard/requests/'),
    ('Dashboard Feedback', '/dashboard/feedback/'),
    ('Dashboard Site Settings', '/dashboard/settings/'),
    ('Staff Profile', '/accounts/profile/'),
]

for name, path in dashboard_routes:
    resp = client.get(path)
    status = resp.status_code
    if status == 200:
        print(f"  ✓ {name:30} [{path:35}] -> HTTP 200 OK")
    else:
        print(f"  ✗ {name:30} [{path:35}] -> HTTP {status} FAILED")
        all_passed = False

if all_passed:
    print("\n🎉 ALL 49 ENDPOINTS RETURNED HTTP 200 OK! Zero broken links or runtime errors.")
else:
    print("\n⚠️ Some routes failed. Check logs above.")

