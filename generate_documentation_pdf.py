import os
from playwright.sync_api import sync_playwright

output_pdf = "Government_Polytechnic_Madhogarh_Library_Project_Report_and_Deployment_Guide.pdf"

html_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Government Polytechnic Madhogarh Library - Project Report & Deployment Guide</title>
<style>
  @page {
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @bottom-right {
      content: counter(page);
    }
  }
  
  body {
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    color: #2c3e50;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    font-size: 13px;
  }
  
  .cover {
    page-break-after: always;
    text-align: center;
    padding-top: 60px;
  }
  
  .cover-badge {
    display: inline-block;
    background: #1b5e20;
    color: white;
    font-size: 13px;
    font-weight: bold;
    padding: 6px 18px;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 25px;
  }
  
  .cover h1 {
    font-size: 28px;
    color: #1b5e20;
    margin: 15px 0 10px 0;
    line-height: 1.3;
    font-weight: 800;
  }
  
  .cover h2 {
    font-size: 18px;
    color: #0d47a1;
    font-weight: 600;
    margin: 10px 0 30px 0;
  }
  
  .cover-divider {
    height: 4px;
    width: 120px;
    background: #2e7d32;
    margin: 0 auto 30px auto;
    border-radius: 2px;
  }
  
  .meta-box {
    background: #f8fbf8;
    border: 1px solid #d4ecd5;
    border-radius: 8px;
    padding: 20px 30px;
    max-width: 550px;
    margin: 0 auto 40px auto;
    text-align: left;
  }
  
  .meta-box table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .meta-box td {
    padding: 6px 8px;
    font-size: 13px;
  }
  
  .meta-label {
    font-weight: bold;
    color: #1b5e20;
    width: 40%;
  }
  
  .meta-val {
    color: #333;
  }
  
  .cover-footer {
    margin-top: 50px;
    color: #7f8c8d;
    font-size: 12px;
  }
  
  h2 {
    color: #1b5e20;
    font-size: 18px;
    border-bottom: 2px solid #e0f0e2;
    padding-bottom: 6px;
    margin-top: 30px;
    margin-bottom: 12px;
  }
  
  h3 {
    color: #0d47a1;
    font-size: 15px;
    margin-top: 18px;
    margin-bottom: 8px;
  }
  
  p, li {
    font-size: 12.5px;
    color: #34495e;
  }
  
  ul, ol {
    margin: 6px 0 12px 20px;
    padding: 0;
  }
  
  li {
    margin-bottom: 4px;
  }
  
  table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0 20px 0;
    font-size: 12px;
  }
  
  table.data-table th {
    background: #1b5e20;
    color: white;
    text-align: left;
    padding: 8px 10px;
    font-weight: 600;
  }
  
  table.data-table td {
    border-bottom: 1px solid #e1e8ed;
    padding: 7px 10px;
  }
  
  table.data-table tr:nth-child(even) td {
    background: #f9fbf9;
  }
  
  .code-block {
    background: #1e293b;
    color: #f8fafc;
    padding: 12px 16px;
    border-radius: 6px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 11.5px;
    line-height: 1.5;
    margin: 10px 0 16px 0;
    overflow-x: auto;
  }
  
  .badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 12px;
    font-size: 11px;
    font-weight: bold;
  }
  
  .badge-green {
    background: #e8f5e9;
    color: #1b5e20;
    border: 1px solid #c8e6c9;
  }
  
  .badge-blue {
    background: #e3f2fd;
    color: #0d47a1;
    border: 1px solid #bbdefb;
  }
  
  .note-box {
    background: #fff9e6;
    border-left: 4px solid #f39c12;
    padding: 10px 14px;
    border-radius: 0 6px 6px 0;
    margin: 14px 0;
    font-size: 12px;
  }
  
  .page-break {
    page-break-after: always;
  }
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover">
  <div class="cover-badge">Official Institutional Documentation</div>
  <h1>Government Polytechnic Madhogarh<br>Central Library & Digital Resource Portal</h1>
  <h2>Technical Architecture, Feature Inventory & Live Production Deployment Guide</h2>
  <div class="cover-divider"></div>
  
  <div class="meta-box">
    <table>
      <tr>
        <td class="meta-label">Institution Name:</td>
        <td class="meta-val">Government Polytechnic Madhogarh</td>
      </tr>
      <tr>
        <td class="meta-label">Location:</td>
        <td class="meta-val">Kailor, Madhogarh, District Jalaun, UP – 285126</td>
      </tr>
      <tr>
        <td class="meta-label">Affiliation:</td>
        <td class="meta-val">Board of Technical Education Uttar Pradesh (BTEUP)</td>
      </tr>
      <tr>
        <td class="meta-label">Institution Code:</td>
        <td class="meta-val">3318 (BTEUP / URISE)</td>
      </tr>
      <tr>
        <td class="meta-label">Official College URL:</td>
        <td class="meta-val">https://gpmadhogarh.ac.in/</td>
      </tr>
      <tr>
        <td class="meta-label">Contact Mobile:</td>
        <td class="meta-val">+91 9305574396</td>
      </tr>
      <tr>
        <td class="meta-label">GitHub Repository:</td>
        <td class="meta-val">https://github.com/KapitalV/college-library.git</td>
      </tr>
      <tr>
        <td class="meta-label">Primary Framework:</td>
        <td class="meta-val">Python Django 6.0 (Full-Stack Monolithic Architecture)</td>
      </tr>
      <tr>
        <td class="meta-label">Release Version:</td>
        <td class="meta-val">Version 1.0 (Production-Ready)</td>
      </tr>
    </table>
  </div>
  
  <div class="cover-footer">
    Compiled for Institutional Audit, Web Administration, and Production Cloud Deployment &bull; 2026
  </div>
</div>

<!-- PAGE 1: EXECUTIVE SUMMARY & ARCHITECTURE -->
<h2>1. Executive Summary & Architecture</h2>
<p>
  The <strong>Government Polytechnic Madhogarh Central Library Portal</strong> is a complete, enterprise-grade, institutional academic web application built using Python Django. It delivers a modern, high-fidelity reproduction of the verified academic information architecture, navigation categories, and public resources of institutional polytechnic libraries, while providing a secure management dashboard for librarians and college administrators.
</p>

<h3>Core Technology Stack</h3>
<table class="data-table">
  <thead>
    <tr>
      <th>Layer</th>
      <th>Technology</th>
      <th>Purpose & Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Backend Framework</strong></td>
      <td>Python 3.14 / Django 6.0</td>
      <td>Robust MTV (Model-Template-View) monolithic architecture, zero external Node dependencies.</td>
    </tr>
    <tr>
      <td><strong>Database</strong></td>
      <td>SQLite (Dev) / PostgreSQL 14+ (Prod)</td>
      <td>Relational schema tracking books, notices, departments, syllabus, staff, and hero slides.</td>
    </tr>
    <tr>
      <td><strong>Frontend</strong></td>
      <td>HTML5, CSS3, Vanilla JavaScript</td>
      <td>Blogger-reference green aesthetic (#1b5e20 / #2e7d32), pure CSS multi-tier dropdowns, responsive layout.</td>
    </tr>
    <tr>
      <td><strong>Production Server</strong></td>
      <td>Gunicorn WSGI + Nginx</td>
      <td>High-concurrency Unix socket proxy with automated SSL (Let's Encrypt / Certbot).</td>
    </tr>
    <tr>
      <td><strong>Security</strong></td>
      <td>Django Security Middleware</td>
      <td>CSRF protection, XSS filtering, Secure Cookies, HSTS, SSL redirect, and SQL injection prevention.</td>
    </tr>
  </tbody>
</table>

<h3>Active Engineering Departments (Board of Technical Education UP)</h3>
<ul>
  <li><strong>Computer Science & Engineering:</strong> BTEUP Branch Code <code>355</code> (Semester 1–6 Curriculum & Notes)</li>
  <li><strong>Electrical Engineering:</strong> BTEUP Branch Code <code>328</code> (Semester 1–6 Curriculum & Notes)</li>
  <li><strong>Electronics Engineering:</strong> BTEUP Branch Code <code>330</code> (Semester 1–6 Curriculum & Notes)</li>
</ul>

<div class="page-break"></div>

<!-- PAGE 2: FEATURE INVENTORY & UI COMPONENTS -->
<h2>2. Complete Feature Inventory & Component Specifications</h2>

<h3>2.1 Responsive Header & Institutional Identity</h3>
<ul>
  <li><strong>Full-Width College Banner:</strong> Seamlessly displays the Government Polytechnic Madhogarh emblem, English/Hindi typography, and campus photograph.</li>
  <li><strong>True-to-Scale Height:</strong> Automatically renders at full natural height with <code>object-fit: contain</code>, preserving crisp resolution on all viewports without height cropping.</li>
  <li><strong>Top Utility Bar:</strong> Instant links to Official Website (<code>gpmadhogarh.ac.in</code>), ERP portal (<code>erp.bizby.io</code>), BTEUP portal, URISE (Code: 3318), Librarian Login, and direct helpline (<code>9305574396</code>).</li>
</ul>

<h3>2.2 Responsive Hero Carousel / Slideshow Component</h3>
<p>
  Integrated directly between the primary navigation bar (<code>&lt;nav&gt;</code>) and the announcement ticker banner, this component delivers dynamic institutional visual highlights.
</p>
<table class="data-table">
  <thead>
    <tr>
      <th>Feature</th>
      <th>Implementation Specification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Django Model</strong></td>
      <td><code>HeroSlide</code> (title, subtitle, badge_text, image, order, is_active, link_url, link_text) in <code>apps.core</code>.</td>
    </tr>
    <tr>
      <td><strong>Admin Controls</strong></td>
      <td>Full CRUD in Django Admin with image thumbnails, list-editable ordering, and status toggles.</td>
    </tr>
    <tr>
      <td><strong>Visual Design</strong></td>
      <td>Height: 400px (Desktop), 340px (Tablet), 240px (Mobile). Forest Green badge (#1d6f42) and elongated indicators.</td>
    </tr>
    <tr>
      <td><strong>Transitions</strong></td>
      <td>Dynamic right-to-left horizontal slide animation (0.55s) with subtle Ken Burns zoom (4s).</td>
    </tr>
    <tr>
      <td><strong>Interaction Logic</strong></td>
      <td>Non-stop auto-play (4s interval) that does not stop on cursor hover, swipe support on mobile, arrow keys on desktop.</td>
    </tr>
  </tbody>
</table>

<h3>2.3 Verified Navigation Hierarchy (8 Main Categories)</h3>
<table class="data-table">
  <thead>
    <tr>
      <th>Menu Item</th>
      <th>Verified Submenus & Destination Pages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. HOME</strong></td>
      <td>Portal root, dynamic hero carousel, announcement marquee, library overview, quick services.</td>
    </tr>
    <tr>
      <td><strong>2. LIBRARY</strong></td>
      <td>About Library, Vision & Mission, Rules & Regulations, Staff Directory, Library Advisory Committee, Facilities & Infrastructure.</td>
    </tr>
    <tr>
      <td><strong>3. DIGITAL LIBRARY</strong></td>
      <td>NDLI Institutional Club (Passkey: d3a479f5-9822-4888-a86e-eb91d907c873), e-Granthalaya OPAC, SWAYAM Portal, NPTEL, AICTE e-KUMBH.</td>
    </tr>
    <tr>
      <td><strong>4. QUESTION PAPERS</strong></td>
      <td>Branch & Semester-wise repository for CS (355), Electrical (328), and Electronics (330).</td>
    </tr>
    <tr>
      <td><strong>5. SYLLABUS</strong></td>
      <td>Semester 1 to 6 BTEUP approved diploma syllabus for all 3 engineering branches.</td>
    </tr>
    <tr>
      <td><strong>6. E-LEARNING</strong></td>
      <td>Branch lecture notes, curated video lectures, digital reference manuals, virtual lab links.</td>
    </tr>
    <tr>
      <td><strong>7. PHOTO GALLERY</strong></td>
      <td>Campus events, National Library Week, student orientation, book exhibitions, workshops.</td>
    </tr>
    <tr>
      <td><strong>8. CONTACT US</strong></td>
      <td>Interactive inquiry form, Kailor campus map, mobile (+91 9305574396), email, hours.</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<!-- PAGE 3: GITHUB PUSH & LIVE PRODUCTION DEPLOYMENT -->
<h2>3. GitHub Repository & Version Control Guide</h2>
<p>
  The source code has been prepared with an empty, clean Git history and committed for publication to the official GitHub repository.
</p>

<div class="code-block">
Target Repository URL: https://github.com/KapitalV/college-library.git
Local Branch: main
Initial Commit: "Initial release: Government Polytechnic Madhogarh Library Portal"
</div>

<h3>One-Time Push Instructions (From your Computer Terminal)</h3>
<p>
  Because GitHub requires user authentication (either via browser OAuth, SSH key, or Personal Access Token), run the following command directly in your Windows PowerShell window:
</p>
<div class="code-block">
Set-Location "c:\Users\JaiBalaJi\OneDrive\Desktop\Library"
& "C:\Users\JaiBalaJi\.mingit\cmd\git.exe" push -u origin main
</div>
<div class="note-box">
  <strong>Note:</strong> When you run this command in your PowerShell window, Windows Git Credential Manager will open a small pop-up window asking you to sign in with your GitHub account (<code>KapitalV</code>). Simply click "Sign in with your browser", and your repository will immediately be uploaded.
</div>

<hr style="border: none; border-top: 1px solid #e0f0e2; margin: 25px 0;">

<h2>4. Live Server Deployment Plan (Ubuntu VPS + Gunicorn + Nginx)</h2>

<h3>4.1 Server Requirements</h3>
<ul>
  <li><strong>Operating System:</strong> Ubuntu Server 22.04 LTS or 24.04 LTS</li>
  <li><strong>Hardware:</strong> Minimum 1 vCPU, 1 GB RAM, 20 GB SSD Storage (DigitalOcean, Hostinger, AWS EC2, etc.)</li>
  <li><strong>Domain:</strong> <code>gpmadhogarh.ac.in</code> or <code>library.gpmadhogarh.ac.in</code> pointed to your Server IP.</li>
</ul>

<h3>4.2 Step-by-Step Server Setup Commands</h3>

<p><strong>Step 1: Install System Packages on Server:</strong></p>
<div class="code-block">
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-venv python3-pip python3-dev nginx certbot python3-certbot-nginx git curl unzip
</div>

<p><strong>Step 2: Clone Code & Setup Virtual Environment:</strong></p>
<div class="code-block">
sudo mkdir -p /var/www/gpm_library
sudo chown -R $USER:www-data /var/www/gpm_library
git clone https://github.com/KapitalV/college-library.git /var/www/gpm_library
cd /var/www/gpm_library

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn
</div>

<p><strong>Step 3: Setup Production Environment Variables (<code>.env</code>):</strong></p>
<div class="code-block">
cp .env.example .env
nano .env
</div>
<p>Ensure <code>DEBUG=False</code>, <code>ALLOWED_HOSTS=library.gpmadhogarh.ac.in,YOUR_SERVER_IP</code>, and <code>SECURE_SSL_REDIRECT=True</code>.</p>

<p><strong>Step 4: Collect Static Assets & Seed Data:</strong></p>
<div class="code-block">
python manage.py collectstatic --noinput --settings=config.settings.production
python manage.py migrate --settings=config.settings.production
python manage.py setup_madhogarh
</div>

<div class="page-break"></div>

<!-- PAGE 4: SERVER SERVICE & SSL CONFIGURATION -->
<h2>5. Production Service & SSL Configuration</h2>

<h3>5.1 Gunicorn Systemd Service</h3>
<p>Enable and start the background application server:</p>
<div class="code-block">
sudo cp deployment/gpm_library.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start gpm_library.service
sudo systemctl enable gpm_library.service
sudo systemctl status gpm_library.service
</div>

<h3>5.2 Nginx Web Server Reverse Proxy</h3>
<p>Enable the pre-configured Nginx reverse proxy configuration:</p>
<div class="code-block">
sudo cp deployment/nginx_gpm_library.conf /etc/nginx/sites-available/gpm_library
sudo ln -s /etc/nginx/sites-available/gpm_library /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx
</div>

<h3>5.3 Free SSL Certificate via Let's Encrypt (HTTPS)</h3>
<p>Run Certbot to automatically configure HTTPS and auto-renewal:</p>
<div class="code-block">
sudo certbot --nginx -d gpmadhogarh.ac.in -d library.gpmadhogarh.ac.in
</div>

<hr style="border: none; border-top: 1px solid #e0f0e2; margin: 25px 0;">

<h2>6. Administration Credentials & Security Maintenance</h2>

<h3>6.1 Default Administrative Credentials</h3>
<table class="data-table">
  <thead>
    <tr>
      <th>Item</th>
      <th>Production Default Value</th>
      <th>Recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Admin Portal URL</strong></td>
      <td><code>https://YOUR_DOMAIN/admin/</code></td>
      <td>Restricted to authorized library staff.</td>
    </tr>
    <tr>
      <td><strong>Librarian Username</strong></td>
      <td><code>admin</code></td>
      <td>Retain or create secondary staff users with granular staff permissions.</td>
    </tr>
    <tr>
      <td><strong>Default Password</strong></td>
      <td><code>Librarian@GPMadhogarh2026!</code></td>
      <td>Change upon first production login via the Django admin interface.</td>
    </tr>
    <tr>
      <td><strong>Helpline Phone</strong></td>
      <td><code>+91 9305574396</code></td>
      <td>Configured across header, footer, sidebar, and contact templates.</td>
    </tr>
    <tr>
      <td><strong>NDLI Passkey</strong></td>
      <td><code>d3a479f5-9822-4888-a86e-eb91d907c873</code></td>
      <td>Official institutional registration passkey for student clubs.</td>
    </tr>
  </tbody>
</table>

<h3>6.2 Automated Daily Backups</h3>
<p>Add a nightly cron job on the server to back up database and media files at 02:00 AM:</p>
<div class="code-block">
# Edit server crontab:
sudo crontab -e

# Append the following line:
0 2 * * * /var/www/gpm_library/deployment/backup.sh >> /var/log/gpm_backup.log 2>&1
</div>

<br><br>
<div style="text-align: center; color: #7f8c8d; font-size: 11.5px; border-top: 1px solid #eee; padding-top: 15px;">
  <strong>Government Polytechnic Madhogarh Central Library Portal</strong> &bull; Developed with Python Django &bull; Kailor, Jalaun, UP
</div>

</body>
</html>
"""

print("Rendering PDF with Playwright...")
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(html_content, wait_until="networkidle")
    page.pdf(
        path=output_pdf,
        format="A4",
        print_background=True,
        margin={"top": "15mm", "bottom": "15mm", "left": "15mm", "right": "15mm"},
    )
    browser.close()

print(f"PDF generated successfully: {output_pdf} ({os.path.getsize(output_pdf)} bytes)")
