from flask import Flask, render_template, request, redirect, url_for
import oracledb

app = Flask(__name__)

def get_connection():
    return oracledb.connect(
        user="system",  # Use SYSTEM user
        password="noni123",
        dsn="localhost/XE"
    )

def init_database():
    """Check if the patients table exists - since it already exists, we'll skip creation"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if patients table exists in current schema
        cursor.execute("""
            SELECT COUNT(*) 
            FROM all_tables 
            WHERE table_name = 'PATIENTS' AND owner = 'SYSTEM'
        """)
        
        table_exists = cursor.fetchone()[0]
        
        if table_exists:
            print("✅ PATIENTS table found in SYSTEM schema")
            
            # Count patients
            cursor.execute("SELECT COUNT(*) FROM patients")
            count = cursor.fetchone()[0]
            print(f"✅ Number of patients in database: {count}")
        else:
            print("⚠️  PATIENTS table does not exist in SYSTEM schema")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Database check error: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients')
def patients():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, ailment FROM patients ORDER BY id")
        patients_data = cursor.fetchall()
        print("Fetched patients:", patients_data)
        return render_template('patients.html', patients=patients_data)
    except Exception as e:
        print("ERROR:", e)
        return f"<h1>Error: {e}</h1>", 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route('/add_patient', methods=['POST'])
def add_patient():
    conn = None
    cursor = None
    try:
        name = request.form['name']
        age = int(request.form['age'])
        condition = request.form['condition']
        
        conn = get_connection()
        cursor = conn.cursor()
        
        sql = "INSERT INTO patients (name, age, ailment) VALUES (:1, :2, :3)"
        cursor.execute(sql, (name, age, condition))
        conn.commit()
        
        return redirect(url_for('patients'))
    except Exception as e:
        print(f"Error adding patient: {e}")
        return f"<h1>Error adding patient: {e}</h1>", 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    # Initialize database on startup
    init_database()
    app.run(debug=True)