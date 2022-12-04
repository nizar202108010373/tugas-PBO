class Plant :
    def __init__(self, nama, status_tumbuh, jumlah_air, jumlah_pupuk):
        self.nama = nama
        self.status_tumbuh = status_tumbuh
        self.jumlah_air = jumlah_air
        self.jumlah_pupuk = jumlah_pupuk
    
class Anggrek(Plant):
    def __init__(self, nama, status_tumbuh, jumlah_air, jumlah_pupuk):
        super().__init__(nama, status_tumbuh, jumlah_air, jumlah_pupuk)
        self.nama = nama
        self.status_tumbuh = status_tumbuh
        self.jumlah_air = jumlah_air
        self.jumlah_pupuk = jumlah_pupuk

class Mawar(Plant):
    def __init__(self, nama, status_tumbuh, jumlah_air, jumlah_pupuk):
        super().__init__(nama, status_tumbuh, jumlah_air, jumlah_pupuk)
        self.nama = nama
        self.status_tumbuh = status_tumbuh
        self.jumlah_air = jumlah_air
        self.jumlah_pupuk = jumlah_pupuk

class Melati(Plant):
    def __init__(self, nama, status_tumbuh, jumlah_air, jumlah_pupuk):
        super().__init__(nama, status_tumbuh, jumlah_air, jumlah_pupuk)
        self.nama = nama
        self.status_tumbuh = status_tumbuh
        self.jumlah_air = jumlah_air
        self.jumlah_pupuk = jumlah_pupuk

a = Anggrek('Anggrek','Benih','2','3')
m = Mawar('Mawar','Tunas','3','4')
me = Melati('Melati','Tanaman Kecil','1','3')

parts = [a,m,me]
for part in parts:
    print('{} {} {} {}'.format(part.nama,part.status_tumbuh,part.jumlah_air,part.jumlah_pupuk))
