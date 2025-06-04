import oracledb

def debug_connection():
    try:
        # Test connection as SYSTEM
        conn = oracledb.connect(
            user="system",
            password="noni123",
            dsn="localhost/XE"
        )
        
        cursor = conn.cursor()
        print("✅ Connected as SYSTEM")
        
        # Check current user
        cursor.execute("SELECT USER FROM DUAL")
        current_user = cursor.fetchone()[0]
        print(f"Current user: {current_user}")
        
        # Check all schemas/users
        print("\n📋 All users/schemas:")
        cursor.execute("SELECT username FROM all_users ORDER BY username")
        users = cursor.fetchall()
        for user in users:
            print(f"  - {user[0]}")
        
        # Check if NONIIGUPTAA user exists
        cursor.execute("SELECT COUNT(*) FROM all_users WHERE username = 'NONIIGUPTAA'")
        user_exists = cursor.fetchone()[0]
        print(f"\n🔍 NONIIGUPTAA user exists: {'Yes' if user_exists else 'No'}")
        
        # Check tables accessible to SYSTEM
        print("\n📊 Tables accessible to SYSTEM:")
        cursor.execute("""
            SELECT owner, table_name 
            FROM all_tables 
            WHERE owner IN ('SYSTEM', 'NONIIGUPTAA') 
            ORDER BY owner, table_name
        """)
        tables = cursor.fetchall()
        for table in tables:
            print(f"  - {table[0]}.{table[1]}")
        
        # Try different ways to access the patients table
        print("\n🔍 Trying to find PATIENTS table:")
        
        # Method 1: As NONIIGUPTAA.PATIENTS
        try:
            cursor.execute("SELECT COUNT(*) FROM noniiguptaa.patients")
            count = cursor.fetchone()[0]
            print(f"✅ noniiguptaa.patients - Found {count} records")
        except Exception as e:
            print(f"❌ noniiguptaa.patients - Error: {e}")
        
        # Method 2: As PATIENTS (if in current schema)
        try:
            cursor.execute("SELECT COUNT(*) FROM patients")
            count = cursor.fetchone()[0]
            print(f"✅ patients - Found {count} records")
        except Exception as e:
            print(f"❌ patients - Error: {e}")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Connection Error: {e}")

def test_noniiguptaa_direct():
    """Try connecting directly as noniiguptaa user"""
    try:
        conn = oracledb.connect(
            user="noniiguptaa",
            password="noni123",  # You might need the correct password for this user
            dsn="localhost/XE"
        )
        
        cursor = conn.cursor()
        print("✅ Connected directly as NONIIGUPTAA")
        
        cursor.execute("SELECT COUNT(*) FROM patients")
        count = cursor.fetchone()[0]
        print(f"✅ Found {count} patients in table")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Direct NONIIGUPTAA connection error: {e}")

if __name__ == "__main__":
    print("=== Debugging Oracle Connection ===")
    debug_connection()
    
    print("\n=== Testing Direct NONIIGUPTAA Connection ===")
    test_noniiguptaa_direct()