import oracledb

def test_connection():
    try:
        # Test connection
        conn = oracledb.connect(
            user="system",
            password="noni123",
            dsn="localhost/XE"
        )
        
        cursor = conn.cursor()
        print("✅ Connected to Oracle successfully!")
        
        # Test if we can query the database
        cursor.execute("SELECT USER FROM DUAL")
        result = cursor.fetchone()
        print(f"✅ Connected as user: {result[0]}")
        
        # Check if patients table exists
        cursor.execute("""
            SELECT COUNT(*) 
            FROM user_tables 
            WHERE table_name = 'PATIENTS'
        """)
        table_exists = cursor.fetchone()[0]
        
        if table_exists:
            print("✅ PATIENTS table exists")
            
            # Count patients
            cursor.execute("SELECT COUNT(*) FROM patients")
            count = cursor.fetchone()[0]
            print(f"✅ Number of patients in database: {count}")
        else:
            print("⚠️  PATIENTS table does not exist - will be created when you run the Flask app")
        
        cursor.close()
        conn.close()
        
    except oracledb.Error as e:
        print(f"❌ Database Error: {e}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    test_connection()