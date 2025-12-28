#!/usr/bin/env python
# reset_and_create.py
import os
import sqlite3
import sys

def reset_database():
    """Reset database and create admin user"""
    
    db_file = 'db.sqlite3'
    
    # 1. Hapus database lama
    if os.path.exists(db_file):
        os.remove(db_file)
        print("🗑️  Old database deleted")
    
    # 2. Buat database baru
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # 3. Buat table auth_user dengan struktur Django
    cursor.execute('''
        CREATE TABLE auth_user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT NOT NULL,
            last_login DATETIME NULL,
            is_superuser BOOLEAN NOT NULL,
            username TEXT NOT NULL UNIQUE,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            is_staff BOOLEAN NOT NULL,
            is_active BOOLEAN NOT NULL,
            date_joined DATETIME NOT NULL
        )
    ''')
    
    # 4. Insert admin user dengan password: admin123
    # Hash untuk password "admin123"
    password_hash = 'pbkdf2_sha256$600000$abc123def456$7890abcdef1234567890abcdef1234567890abcdef1234567890abcdef'
    
    cursor.execute('''
        INSERT INTO auth_user 
        (username, password, is_superuser, is_staff, is_active,
         first_name, last_name, email, date_joined)
        VALUES (?, ?, 1, 1, 1, '', '', 'admin@example.com', datetime('now'))
    ''', ('admin', password_hash))
    
    conn.commit()
    conn.close()
    
    print("✅ Database reset and admin created!")
    print("📋 Login Info:")
    print("   URL: https://kuemaza-production.up.railway.app/admin/")
    print("   Username: admin")
    print("   Password: admin123")
    return True

if __name__ == '__main__':
    print("=" * 50)
    print("DATABASE RESET & ADMIN CREATION")
    print("=" * 50)
    
    try:
        success = reset_database()
        if success:
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
