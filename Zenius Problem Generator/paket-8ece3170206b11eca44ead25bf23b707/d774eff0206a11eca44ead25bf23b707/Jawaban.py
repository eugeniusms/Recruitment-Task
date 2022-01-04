"""
Program perhitungan rentang nilai dari angka rendah ke angka tinggi di mana jika 
angka dalam rentang tersebut dapat dibagi dengan suatu bilangan (17 dan 71) dalam
kasus ini, maka jumlahkan angka tersebut menjadi suatu total dan lakukan pembagian
modulo 51681
"""

def kelipatan(angka_1, angka_2, rentang):
    """
    Fungsi untuk mencari bilangan yang merupakan kelipatan dari angka_1 atau angka_2
    kemudian dijumlahkan dan dikembalikan nilai dari jumlahnya beserta detail di mana
    detail adalah variabel berisi list (array) dari angka-angka yang merupakan kelipatan
    """
    total = 0
    DETAIL = []
    for angka in range(1, rentang + 1):
        # Saat angka dapat dibagi angka_1 dan angka_2
        if angka % angka_1 == 0 or angka % angka_2 == 0:
            total += angka
            DETAIL.append(angka)
    return total, DETAIL

def cetak_jawaban(nama_file, jawaban):
    """
    Fungsi untuk mencetak jawaban dari hasil yang sudah dioperasikan dalam fungsi utama
    melalui fungsi-fungsi lain. Jawaban dicetak ke dalam file bernama Jawaban.txt
    """
    my_file = open(nama_file, mode='w')
    print(jawaban, file=my_file)
    my_file.close()

def main():
    """Fungsi utama untuk menjalankan program di mana di dalam fungsi ini akan dilakukan
    pengambilan data konstanta yang dibutuhkan kemudian di operasikan ke dalam setiap 
    fungsi yang tersedia,
    1. Melakukan pencarian yang berkelipatan 17 dan 71 dalam rentang dengan fungsi kelipatan()
       yang mana sekaligus melakukan penambahan nilai-nilainya.
    2. Melakukan pencetakan hasil melalui fungsi cetak_jawaban dengan hasil yang sudah di mod 51681.
    """
    # Melakukan inisialisasi data masukan
    angka_1 = 17
    angka_2 = 71
    rentang = 100000
    total, DETAIL = kelipatan(angka_1, angka_2, rentang)
    jawaban = total % 51681
    jawaban = "Jawaban : {}\nAngka dapat terbagi {} atau {}\ndalam rentang {} : {}".format(jawaban, angka_1, angka_2, rentang, DETAIL)
    cetak_jawaban("./paket-8ece3170206b11eca44ead25bf23b707/d774eff0206a11eca44ead25bf23b707/Jawaban.txt",jawaban)
    print("Selesai")

# Memulai program
main()