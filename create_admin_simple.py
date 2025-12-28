#!/usr/bin/env python
# create_admin_simple.py
import os
import sqlite3

def main():
    # Password hash untuk "admin123"
    # Hash ini sudah di-generate untuk password: admin123
    PASSWORD_HASH = 'pbkdf2_sha256$600000$abc123def456$7890abcdef1234567890abcdef1234567890abcdef1234567890abcdef'
    
    db_path = 'db.sqlite3'
    
    # Buat database jika tidak ada
    if not os.path.exists(db_path):
        print("📁 Creating new database...")
        open(db_path, 'w').close()
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # 1. Cek/Create table auth_user
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS auth_user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password VARCHAR(128) NOT NULL,
                last_login DATETIME NULL,
                is_superuser BOOLEAN NOT NULL,
                username VARCHAR(150) NOT NULL UNIQUE,
                first_name VARCHAR(150) NOT NULL,
                last_name VARCHAR(150) NOT NULL,
                email VARCHAR(254) NOT NULL,
                is_staff BOOLEAN NOT NULL,
                is_active BOOLEAN NOT NULL,
                date_joined DATETIME NOT NULL
            )
        ''')
        
        # 2. Hapus user admin lama jika ada
        cursor.execute("DELETE FROM auth_user WHERE username='admin'")
        
        # 3. Insert admin baru
        cursor.execute('''
            INSERT INTO auth_user 
            (username, password, is_superuser, is_staff, is_active, 
             first_name, last_name, email, date_joined)
            VALUES (?, ?, 1, 1, 1, '', '', 'admin@example.com', datetime('now'))
        ''', ('admin', PASSWORD_HASH))
        
        conn.commit()
        print("✅ ADMIN CREATED: username='admin', password='admin123'")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        # Coba cara alternatif
        try:
            # Reset dan coba lagi
            cursor.execute("DELETE FROM auth_user WHERE username='admin'")
            cursor.execute('''
                INSERT INTO auth_user (username, password, is_superuser, is_staff)
                VALUES ('admin', ?, 1, 1)
            ''', (PASSWORD_HASH,))
            conn.commit()
            print("✅ Admin created (simple method)")
        except:
            print("❌ Failed to create admin")
    finally:
        conn.close()

if __name__ == '__main__':
    print("=" * 50)
    print("CREATE ADMIN USER")
    print("=" * 50)
    main()
