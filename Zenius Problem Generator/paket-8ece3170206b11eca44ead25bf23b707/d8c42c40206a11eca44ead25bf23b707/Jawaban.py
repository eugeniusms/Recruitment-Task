"""
Program pencarian jumlah segitiga di dalam file kata.txt di mana rumus dari segitiga yang
dimaksud adalah t(n) = 1/2n(n+1), segitiga didapati jika setiap indeks huruf dalam
alphabet yang ditotalkan memiliki nilai salah satu dari t(n). Setelah didapati bentuk
segitiga maka kembalikan hasil ke dalam jawaban.txt
"""
def buka_file(nama_file):
    """
    Fungsi untuk mengambil file masukan yang sudah dibuat, kemudian dimasukan ke dalam variabel
    untuk dilakukan proses operasi data.
    """
    file = open(nama_file)
    txt = file.read()
    file.close()
    return txt

def cek_segitiga(total):
    """
    Fungsi melakukan pengecekan total dari jumlah indeks huruf melalui perumusan segitiga.
    Jika hasil perumusan belum mencapai besaran total maka lakukan perulangan dengan n+1.
    Jika menemui titik persamaan maka kembalikan nilai 1 (Segitiga). Jika hasil perumusan (t)
    sudah melebihi total maka kembalikan 0 (Bukan segitiga).
    """
    n = 1 
    while True:
        t = 1/2*n*(n+1)
        if t == total:
            return 1
        elif t > total:
            return 0
        n += 1

def cetak_jawaban(nama_file, jawaban):
    """
    Fungsi untuk mencetak hasil keluaran yang sudah didapati di dalam program ke suatu file
    bernama nama_file.
    """
    my_file = open(nama_file, mode='w')
    print(jawaban, file=my_file)
    my_file.close()

def main():
    """
    Program di awali oleh fungsi main sebagai inisiator dalam menjalankan program, beberapa
    langkah yang ditempuh dalam fungsi ini adalah:
    1. Membuka file kata.txt dengan fungsi buka_file().
    2. Melakukan operasi pengecekan berdasarkan rumus t(n) (rumus segitiga) melalui fungsi
       cek_segitiga(), jika benar maka kembalikan nilai 1, sebaliknya jika salah maka kembalikan 
       nilai 0 dan jumlahkan.
    3. Setelah mendapati semua perulangan kata yang ada maka tuliskan jumlah segitiga dalam 
       file jawaban.txt dengan fungsi cetak_jawaban().
    """
    txt = buka_file("./paket-8ece3170206b11eca44ead25bf23b707/d8c42c40206a11eca44ead25bf23b707/kata.txt")
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 0 
    segitiga = 0
    CEK_CHAR = ""
    DETAIL = ""
    for char in txt:
        if char in alfabet:
            # Menambahkan jumlah indeks huruf untuk diidentifikasi segitiga
            total += alfabet.find(char) + 1
            CEK_CHAR += char
        else:
            # Jika total != 0 maka cek segitiga tidaknya lalu jumlahkan segitiga
            if total != 0:
                segitiga += cek_segitiga(total)

                # Simpan detail dari data segitiga ke dalam variabel DETAIL
                if cek_segitiga(total) == 1:
                    DETAIL += "\n{} : Segitiga ({})".format(CEK_CHAR,total)

            # Reset total = 0
            total = 0
            CEK_CHAR = ""

    jawaban = "Banyak kata segitiga : {}{}".format(segitiga, DETAIL) 
    cetak_jawaban("./paket-8ece3170206b11eca44ead25bf23b707/d8c42c40206a11eca44ead25bf23b707/Jawaban.txt",jawaban)
    print("Selesai")

# Memulai program
main()

