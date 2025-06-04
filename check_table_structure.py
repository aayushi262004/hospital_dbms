import oracledb

def check_table_structure():
    try:
        conn = oracledb.connect(
            user="system",
            password="noni123",
            dsn="localhost/XE"
        )
        
        cursor = conn.cursor()
        print("✅ Connected as SYSTEM")
        
        # Get table structure
        print("\n📋 PATIENTS table structure:")
        cursor.execute("""
            SELECT column_name, data_type, data_length, nullable
            FROM user_tab_columns 
            WHERE table_name = 'PATIENTS'
            ORDER BY column_id
        """)
        
        columns = cursor.fetchall()
        for col in columns:
            nullable = "NULL" if col[3] == 'Y' else "NOT NULL"
            print(f"  - {col[0]}: {col[1]}({col[2]}) {nullable}")
        
        # Get actual data
        print(f"\n📊 Current data in PATIENTS table:")
        cursor.execute("SELECT * FROM patients")
        patients = cursor.fetchall()
        
        if patients:
            # Print header
            column_names = [desc[0] for desc in cursor.description]
            print(f"Columns: {column_names}")
            
            for i, patient in enumerate(patients, 1):
                print(f"Row {i}: {patient}")
        else:
            print("No data found")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    check_table_structure()