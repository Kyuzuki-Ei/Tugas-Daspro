# Nama = Muhamad Ikshan Suherman
# NIM = 2402784
# Kelas = 1B

student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"}
}

nama = input("Masukkan nama siswa: ")

studentx = student_info[nama]

print(f'Umur {nama} adalah {studentx['age']} dan prodinya adalah {studentx['major']}')

