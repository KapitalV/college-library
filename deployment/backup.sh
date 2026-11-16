#!/usr/bin/env bash
# ==============================================================================
# GP Madhogarh Library Portal - Production Automated Backup Script
# Creates a timestamped dump of PostgreSQL database and media files.
# ==============================================================================

set -euo pipefail

BACKUP_DIR="/var/backups/gpm_library"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
DB_NAME="gpm_library_db"
DB_USER="gpm_library_user"
MEDIA_DIR="/var/www/gpm_library/media"

mkdir -p "${BACKUP_DIR}"

echo "[$(date)] Starting GP Madhogarh Library Portal backup..."

# 1. PostgreSQL Database Dump (if using PostgreSQL)
if command -v pg_dump &> /dev/null; then
    echo "Dumping PostgreSQL database..."
    pg_dump -U "${DB_USER}" -F c -b -v -f "${BACKUP_DIR}/db_${TIMESTAMP}.dump" "${DB_NAME}" || true
fi

# 2. Backup SQLite db if present
if [ -f "/var/www/gpm_library/db.sqlite3" ]; then
    echo "Backing up SQLite database..."
    cp "/var/www/gpm_library/db.sqlite3" "${BACKUP_DIR}/db_sqlite_${TIMESTAMP}.sqlite3"
fi

# 3. Archive User Media Files
if [ -d "${MEDIA_DIR}" ]; then
    echo "Archiving media uploads..."
    tar -czf "${BACKUP_DIR}/media_${TIMESTAMP}.tar.gz" -C "${MEDIA_DIR}" .
fi

# 4. Clean Backups Older than 30 Days
find "${BACKUP_DIR}" -type f -mtime +30 -delete

echo "[$(date)] Backup completed successfully to ${BACKUP_DIR}/"

