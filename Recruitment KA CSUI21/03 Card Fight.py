# Membuat inisiasi input
jumlah_kartu, health = input().split()
kartu_dika = str(input()).upper()
kartu_dina = str(input()).upper()

# Memberi type data pada variabel
jumlah_kartu = int(jumlah_kartu)
health = int(health)

# Menyatukan kartu dika dan dina dalam list di mana kartu dika index genap 0 2 dst dan dina sebaliknya
lst_kartu_dika = []
lst_kartu_dina = []

for i in range(jumlah_kartu):
    lst_kartu_dika.append(kartu_dika[i])
    lst_kartu_dina.append(kartu_dina[i])

# Membuat class self object untuk pemain dan atributnya
class Profil():

    def __init__(self, health, attack, defense):
        self.health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
    
    def support_card(self):
        self.attack += 1
        self.defense += 1

    def attack_card_nodef(self, enemy):
        enemy.health -= self.attack

    def reset_atkdef(self):
        self.attack = 1
        self.defense = 1

    def attack_card_withdef(self, enemy):
        if self.attack > enemy.defense:
            enemy.health -= abs(self.attack - enemy.defense)


# Menginisiasi last_card untuk kartu terakhir dan count untuk menghitung jumlah turn
last_card = ""
count = 0

# Menginisiasi atribut pemain
dika = Profil(int(health), 1, 1)
dina = Profil(int(health), 1, 1)

# Melakukan perulangan permainan
while count != jumlah_kartu:
    
    # Jika ada salah satu nyawa kurang atau sama dengan 0 maka sudahi game
    if dika.health <= 0 or dina.health <= 0:
            break
        
    # Permulaan game diinisiasi sama dika dulu karena belum ada kartu sebelumnya
    if count == 0:
        last_card = lst_kartu_dika[count]
        if last_card == "A":
            Profil.attack_card_nodef(dika, dina)
            Profil.reset_atkdef(dika)

        elif last_card == "S":
            Profil.support_card(dika)

        if dika.health <= 0 or dina.health <= 0:
            break
        
        # Reaksi dina saat masih turn setelah dika 1 agar program setelah ini dapat berjalan lancar di loop
        if last_card == "D" and lst_kartu_dina[count] == "A":
            Profil.attack_card_withdef(dina, dika)
            Profil.reset_atkdef(dina)
            Profil.reset_atkdef(dika)

        elif last_card != "D" and lst_kartu_dina[count] == "A":
            Profil.attack_card_nodef(dina, dika)
            Profil.reset_atkdef(dina)

        # UPDATE 10 Sep - Untuk saat kartu sebelum adalah S atau D
        elif last_card == "D" and lst_kartu_dina[count] != "A":
            Profil.reset_atkdef(dika)

        if lst_kartu_dina[count] == "S":
            Profil.support_card(dina)

        if dika.health <= 0 or dina.health <= 0:
            break
        
        last_card = lst_kartu_dina[count]

    if count > 0:
        # UNTUK TURN DIKA LAKUKAN HAL INI
        if last_card == "A" and lst_kartu_dika[count] == "A":
            Profil.reset_atkdef(dina)

        if last_card == "D" and lst_kartu_dika[count] == "A":
            Profil.attack_card_withdef(dika, dina)
            Profil.reset_atkdef(dika)
            Profil.reset_atkdef(dina)

        elif last_card != "D" and lst_kartu_dika[count] == "A": 
            Profil.attack_card_nodef(dika, dina)
            Profil.reset_atkdef(dika)

        # UPDATE 10 Sep - Untuk saat kartu sebelum adalah S atau D
        elif last_card == "D" and lst_kartu_dika[count] != "A":
            Profil.reset_atkdef(dina)

        if lst_kartu_dika[count] == "S":
            Profil.support_card(dika)

        if dika.health <= 0 or dina.health <= 0:
            break

        last_card = lst_kartu_dika[count]

        # UNTUK TURN DINA LAKUKAN HAL INI
        if last_card == "D" and lst_kartu_dina[count] == "A":
            Profil.attack_card_withdef(dina, dika)
            Profil.reset_atkdef(dina)
            Profil.reset_atkdef(dika)

        elif last_card != "D" and lst_kartu_dina[count] == "A":
            Profil.attack_card_nodef(dina, dika)
            Profil.reset_atkdef(dina)

        # UPDATE 10 Sep - Untuk saat kartu sebelum adalah S atau D
        elif last_card == "D" and lst_kartu_dina[count] != "A":
            Profil.reset_atkdef(dika)

        if lst_kartu_dina[count] == "S":
            Profil.support_card(dina)

        if dika.health <= 0 or dina.health <= 0:
            break

        last_card = lst_kartu_dina[count]

    # Menambah perulangan
    count += 1

# Jika keluar dari loop maka output akan diproses seperti pada problem
if dika.health < dina.health:
    print("Dina")
elif dika.health > dina.health:
    print("Dika")
elif dika.health == dina.health:
    print("Seri")
