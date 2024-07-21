import csv

class AttendanceAnalytics:
    def __init__(self, attendance_file):
        self.attendance_file = attendance_file

    def read_attendance_data(self):
        """Reads attendance data from a CSV file."""
        attendance_data = []
        with open(self.attendance_file, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header row
            for row in reader:
                attendance_data.append(row)
        return attendance_data

    def calculate_average_attendance(self):
        """Calculates the average attendance of students."""
        attendance_data = self.read_attendance_data()
        student_attendance = {}
        
        for record in attendance_data:
            student_id, date, status = record
            if student_id not in student_attendance:
                student_attendance[student_id] = {'present': 0, 'total': 0}
            student_attendance[student_id]['total'] += 1
            if status.lower() == 'present':
                student_attendance[student_id]['present'] += 1
        
        total_students = len(student_attendance)
        total_attendance = sum(student['present'] for student in student_attendance.values())
        total_days = sum(student['total'] for student in student_attendance.values())

        average_attendance = (total_attendance / total_days) * 100 if total_days > 0 else 0
        return average_attendance

    def generate_report(self):
        """Generates a report of average attendance."""
        average_attendance = self.calculate_average_attendance()
        print(f"Average Attendance: {average_attendance:.2f}%")

if __name__ == "__main__":
    attendance_file = 'attendance.csv'
    analytics = AttendanceAnalytics(attendance_file)
    analytics.generate_report()
