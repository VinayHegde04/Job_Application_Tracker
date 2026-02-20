import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vinay@15",
        port=3307,
        database="job_tracker"
    )

    if connection.is_connected():
        print("✅ Connected to MySQL successfully!")

except Exception as e:
    print("❌ Error:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("🔒 Connection closed.")
