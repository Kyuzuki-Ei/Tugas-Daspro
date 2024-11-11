# Nama = Muhamad Ikshan Suherman
# NIM = 2402784
# Kelas = 1B

from collections import Counter

# dictionary
students = {
    "Asep": "Computer Science",
    "Baloy": "Mathematics", 
    "Cihuy": "Physics",
    "Dadang": "Computer Science",
    "Eli": "Mathematics"
}

hasil = Counter(students.values())

# Hasil
for value, count in hasil.items():
    if count > 0: 
        print(f"Prodi '{value}' sebanyak {count} ")