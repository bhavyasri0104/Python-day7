print("=== Student ID Card - Tuples ===")

# Tuple creation - () brackets
student_id = ("Bhavyasri", 25, "Python Batch", 2026)
print("Student Tuple:", student_id)

# Indexing - List laage
name = student_id[0]
age = student_id[1]
course = student_id[2]

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Course: {course}")

# Tuple marchalante error vastadi
# student_id[1] = 26 # TypeError: 'tuple' object does not support item assignment

# Tuple methods - 2 matrame
print("Length:", len(student_id))
print("Count of 2026:", student_id.count(2026))

input("\nPress Enter to exit...")


print("=== Student Report - Dictionary ===")

# Dictionary creation - {} brackets with key:value
student = {
    "name": "Bhavyasri",
    "age": 25,
    "course": "Python",
    "maths": 85,
    "science": 92,
    "total": 177
}

print("Student Data:", student)

# Values access cheyadam - key tho
print(f"Name: {student['name']}")
print(f"Maths: {student['maths']}")

# Kotha key:value add chey
student["grade"] = "A"
print("After adding grade:", student)

# Value update chey
student["age"] = 26
print("After birthday:", student)

# Keys and Values veruga chudatam
print("All Keys:", student.keys())
print("All Values:", student.values())

input("\nPress Enter to exit...")

