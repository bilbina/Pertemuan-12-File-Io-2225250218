
def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    data.append((nim, nilai))
                except ValueError:
                    print(f"Data tidak valid: {baris}")

    except FileNotFoundError:
        print("File tidak ditemukan.")

    return data


def tulis_rekap(nama_file, data):
    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            for nim, nilai in data:
                file.write(f"{nim},{nilai}\n")

        print("Rekap nilai berhasil disimpan.")

    except OSError:
        print("Terjadi kesalahan saat menulis file.")


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data_nilai = baca_data(input_file)
tulis_rekap(output_file, data_nilai)

print("Data yang berhasil dibaca:", data_nilai)
