#!/usr/bin/env bash
# ==============================================================================
# GP Madhogarh Library Portal - Production Disaster Recovery & Restore Script
# Usage: ./restore.sh <path_to_db_dump> <path_to_media_tar_gz>
# ==============================================================================

set -euo pipefail

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <path_to_db_dump> <path_to_media_tar_gz>"
    exit 1
fi

DB_DUMP="$1"
MEDIA_ARCHIVE="$2"
DB_NAME="gpm_library_db"
DB_USER="gpm_library_user"
MEDIA_DIR="/var/www/gpm_library/media"

echo "[$(date)] Restoring GP Madhogarh Library from ${DB_DUMP}..."

# 1. Stop Gunicorn service
systemctl stop gpm_library.service

# 2. Restore Database
if [[ "${DB_DUMP}" == *.sqlite3 ]]; then
    echo "Restoring SQLite database..."
    cp "${DB_DUMP}" /var/www/gpm_library/db.sqlite3
    chown www-data:www-data /var/www/gpm_library/db.sqlite3
else
    echo "Restoring PostgreSQL database..."
    dropdb -U "${DB_USER}" --if-exists "${DB_NAME}"
    createdb -U "${DB_USER}" -O "${DB_USER}" "${DB_NAME}"
    pg_restore -U "${DB_USER}" -d "${DB_NAME}" -v "${DB_DUMP}"
fi

# 3. Restore Media Files
mkdir -p "${MEDIA_DIR}"
tar -xzf "${MEDIA_ARCHIVE}" -C "${MEDIA_DIR}"
chown -R www-data:www-data "${MEDIA_DIR}"

# 4. Restart Gunicorn service
systemctl start gpm_library.service

echo "[$(date)] Disaster recovery completed successfully. Application restarted."

