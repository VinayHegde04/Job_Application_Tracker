import mysql.connector


class JobApplicationTracker:

   def __init__(self):
    try:
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_PASSWORD",
            port=3307,
            database="job_tracker"
        )
        self.cursor = self.connection.cursor()
        print("✅ Database Connected Successfully")
    except mysql.connector.Error as err:
        print("❌ Database Connection Failed:", err)
        exit()


    def add_application(self):
        print("\n--- Add Job Application ---")
        company = input("Enter Company Name: ")
        role = input("Enter Role: ")
        location = input("Enter Location: ")
        salary = input("Enter Salary: ")
        date = input("Enter Applied Date (YYYY-MM-DD): ")
        notes = input("Enter Notes: ")

        query = """
        INSERT INTO applications 
        (company_name, role, location, salary, applied_date, notes)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (company, role, location, salary, date, notes)
        self.cursor.execute(query, values)
        self.connection.commit()

        print("✅ Application Added Successfully!")

    def view_applications(self):
        print("\n--- All Job Applications ---")

        query = "SELECT * FROM applications"
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        if not records:
            print("No applications found.")
        else:
            for row in records:
                print(f"""
ID: {row[0]}
Company: {row[1]}
Role: {row[2]}
Location: {row[3]}
Salary: {row[4]}
Status: {row[5]}
Applied Date: {row[6]}
Notes: {row[7]}
----------------------------
""")

    def update_status(self):
        print("\n--- Update Application Status ---")
        app_id = input("Enter Application ID to update: ")
        new_status = input("Enter New Status (Applied/Interview/Selected/Rejected): ")

        query = "UPDATE applications SET status = %s WHERE id = %s"
        self.cursor.execute(query, (new_status, app_id))
        self.connection.commit()

        if self.cursor.rowcount > 0:
            print("✅ Status Updated Successfully!")
        else:
            print("❌ No record found with that ID.")

    def delete_application(self):
        print("\n--- Delete Application ---")
        app_id = input("Enter Application ID to delete: ")

        query = "DELETE FROM applications WHERE id = %s"
        self.cursor.execute(query, (app_id,))
        self.connection.commit()

        if self.cursor.rowcount > 0:
            print("✅ Application Deleted Successfully!")
        else:
            print("❌ No record found with that ID.")
    
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("🔒 Database Connection Closed")


    def run(self):
        while True:
            print("\n==== Job Application Tracker ====")
            print("1. Add Application")
            print("2. View Applications")
            print("3. Update Status")
            print("4. Delete Application")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_application()
            elif choice == "2":
                self.view_applications()
            elif choice == "3":
                self.update_status()
            elif choice == "4":
                self.delete_application()
            elif choice == "5":
                print("Goodbye!")
                self.close_connection()
                break



if __name__ == "__main__":
    app = JobApplicationTracker()
    app.run()
