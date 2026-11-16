# Production Deployment & Maintenance Guide

**Project:** Government Polytechnic Madhogarh Central Library & Digital Resource Portal  
**Target Environment:** Ubuntu Server 22.04 / 24.04 LTS, Nginx, Gunicorn, PostgreSQL / SQLite  

---

## 1. System Requirements & Preparation

### 1.1 Install System Packages
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-venv python3-pip python3-dev postgresql postgresql-contrib libpq-dev nginx certbot python3-certbot-nginx git curl
```

### 1.2 Set up PostgreSQL Database (Recommended for Production)
```bash
sudo -u postgres psql
```
Within the PostgreSQL prompt:
```sql
CREATE DATABASE gpm_library_db;
CREATE USER gpm_library_user WITH PASSWORD 'ChangeThisToAStrongPassword123!';
ALTER ROLE gpm_library_user SET client_encoding TO 'utf8';
ALTER ROLE gpm_library_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE gpm_library_user SET timezone TO 'Asia/Kolkata';
GRANT ALL PRIVILEGES ON DATABASE gpm_library_db TO gpm_library_user;
\q
```

---

## 2. Application Setup

### 2.1 Clone Repository & Setup Virtual Environment
```bash
sudo mkdir -p /var/www/gpm_library
sudo chown -R $USER:www-data /var/www/gpm_library
cd /var/www/gpm_library

# Copy or clone files here
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install psycopg2-binary gunicorn
```

### 2.2 Configure Production Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
nano .env
```
Ensure:
```ini
SECRET_KEY=generate-a-cryptographically-secure-random-50-character-string
DEBUG=False
ALLOWED_HOSTS=gpmadhogarh.ac.in,library.gpmadhogarh.ac.in,www.gpmadhogarh.ac.in,127.0.0.1
DATABASE_URL=postgres://gpm_library_user:ChangeThisToAStrongPassword123!@localhost:5432/gpm_library_db
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
CSRF_TRUSTED_ORIGINS=https://gpmadhogarh.ac.in,https://library.gpmadhogarh.ac.in
```

### 2.3 Run Database Migrations & Seed Content
```bash
python manage.py migrate --settings=config.settings.production
python manage.py setup_madhogarh
python manage.py collectstatic --noinput --settings=config.settings.production
```

### 2.4 Verify Production Security Check
```bash
python manage.py check --deploy --settings=config.settings.production
```

---

## 3. Web Server & Service Configuration

### 3.1 Setup Systemd Service
```bash
sudo cp deployment/gpm_library.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start gpm_library.service
sudo systemctl enable gpm_library.service
sudo systemctl status gpm_library.service
```

### 3.2 Setup Nginx & SSL
```bash
sudo cp deployment/nginx_gpm_library.conf /etc/nginx/sites-available/gpm_library
sudo ln -s /etc/nginx/sites-available/gpm_library /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx

# Issue Let's Encrypt SSL Certificate
sudo certbot --nginx -d gpmadhogarh.ac.in -d library.gpmadhogarh.ac.in
```

---

## 4. Automated Backup Setup (Cron)

Edit root crontab:
```bash
sudo crontab -e
```
Add daily backup at 02:00 AM:
```cron
0 2 * * * /var/www/gpm_library/deployment/backup.sh >> /var/log/gpm_backup.log 2>&1
```

---

## 5. Routine Application Updates
```bash
cd /var/www/gpm_library
source venv/bin/activate
git pull origin main
pip install -r requirements.txt
python manage.py migrate --settings=config.settings.production
python manage.py collectstatic --noinput --settings=config.settings.production
sudo systemctl restart gpm_library.service
```

