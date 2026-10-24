# Input: nilai mahasiswa
# Proses: memilih nilai yang memenuhi batas kelulusan 60
# Output: nilai yang lulus dan jumlahnya

nilai = [75, 55, 80, 60, 45, 90]
lulus = []

for x in nilai:
    if x >= 60:
        lulus.append(x)

print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")