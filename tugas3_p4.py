# Nama = Muhamad Ikshan Suherman
# NIM = 2402784
# Kelas = 1B

student_info = {
    "Alice": {"age": 19, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Mathematics"},
    "Charlie": {"age": 21, "major": "Physics"}
}

nama = input("Masukkan nama siswa: ")

studentx = student_info[nama]

print(f'Umur {nama} adalah {studentx['age']} dan prodinya adalah {studentx['major']}')

