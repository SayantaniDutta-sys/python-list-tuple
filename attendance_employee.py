# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 11:28:33 2025

@author: 91912
"""

employees = [
    (101, "Alice", "HR"),
    (102, "Bob", "IT"),
    (103, "Charlie", "Finance"),
    (104, "David", "IT"),
    (105, "Eve", "HR")
]

attendance_records = []

def mark_attendance(employee_id, date, status):
    if any(emp[0] == employee_id for emp in employees):
        attendance_records.append((employee_id, date, status))
        print(f"Attendance marked for Employee ID {employee_id} on {date} as {status}.")
    else:
        print("Invalid Employee ID.")

def search_attendance(employee_id):
    records = [record for record in attendance_records if record[0] == employee_id]
    if records:
        print(f"Attendance records for Employee ID {employee_id}:")
        for record in records:
            print(f"Date: {record[1]}, Status: {record[2]}")
    else:
        print("No attendance records found.")

mark_attendance(101, "2025-03-13", "Present")
mark_attendance(102, "2025-03-13", "Absent")
mark_attendance(103, "2025-03-13", "Present")
search_attendance(101)
search_attendance(105)