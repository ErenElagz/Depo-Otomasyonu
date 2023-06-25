# Sınıflar
class Depo():
    def __init__(self, isim):
        self.isim = isim

class Elektronik(Depo):
    def __init__(self, isim, adet, fiyat, marka, kategori, uretimYeri, garantiSuresi):
        self.isim = isim
        self.adet = adet
        self.fiyat = fiyat
        self.marka = marka
        self.uretimYeri = uretimYeri
        self.kategori = kategori
        self.garantiSuresi = garantiSuresi

    def UrunEkle(self):
        print("\n", self.isim, "Güncel Adet:", self.adet)
        print("----------------------------")
        adet = int(input("Kaç adet eklemek istiyorsunuz ? "))
        self.adet = self.adet + adet

    def UrunSilme(self):
        print("\n", self.isim, "Güncel Adet:", self.adet)
        print("----------------------------")
        adet = int(input("Kaç adet çıkarmak istiyorsunuz? "))
        self.adet = self.adet - adet

    def BilgiGuncelleme(self):
        print("\n----------------------------")
        print("Ne güncellemek istiyorsunuz? ")
        print("1: Ürün Adı        :", self.isim)
        print("2: Ürün Adeti      :", self.adet)
        print("3: Ürün Fiyat      :", self.fiyat)
        print("4: Ürün Üretim Yeri:", self.uretimYeri)
        print("5: Ürün Marka      :", self.marka)
        print("6: Ürün Kategorisi :", self.kategori)
        print("7: Ürün G. Süresi  :", self.garantiSuresi)
        secim = int(input("Değiştirmek istediginiz değeri girin: "))

        if secim == 1:
            self.isim = (input("Ürün Adını Giriniz: "))

        elif secim == 2:
            self.adet = int(input("Ürün Adetini Giriniz: "))

        elif secim == 3:
            self.fiyat = int(input("Ürün Fiyatını Giriniz: "))

        elif secim == 4:
            self.uretimYeri = (input("Ürün Üretim Yeri Giriniz: "))

        elif secim == 5:
            self.marka = (input("Ürün Marka Giriniz: "))

        elif secim == 6:
            self.kategori = int(input("Ürün Kategorisi Giriniz: "))

        elif secim == 7:
            self.garantiSuresi = int(input("Ürün G. Süresi Giriniz: "))

        else:
            print("Geçerli Bir Değer Giriniz!\n")

    def UrunBilgi(self):
        print("\n" + self.isim, "Ürünü bilgisi")
        print("-----------------------")
        print("Adeti       :", self.adet, "Adet")
        print("Fiyat       :", self.fiyat, "₺")
        print("Markası     :", self.marka)
        print("Kategorisi  :", self.kategori)
        print("Üretim Yeri :", self.uretimYeri)
        print("G. Süresi   :", self.garantiSuresi, "Yılı")

class Organik(Depo):
    def __init__(self, isim, adet, fiyat, kategori, uretimYeri, stt,):
        self.isim = isim
        self.adet = adet
        self.fiyat = fiyat
        self.uretimYeri = uretimYeri
        self.kategori = kategori
        self.stt = stt

    def UrunEkle(self):
        print("\n", self.isim, "Güncel Adet:", self.adet)
        print("----------------------------")
        adet = int(input("Kaç adet eklemek istiyorsunuz ? "))
        self.adet = self.adet + adet

    def UrunSilme(self):
        print("\n", self.isim, "güncel adet:", self.adet)
        print("----------------------------")
        adet = int(input("Kaç adet çıkarmak istiyorsunuz? "))
        self.adet = self.adet - adet

    def BilgiGuncelleme(self):
        print("\n----------------------------")
        print("Ne güncellemek istiyorsunuz? ")
        print("1: Ürün Adı        :", self.isim)
        print("2: Ürün Adeti      :", self.adet)
        print("3: Ürün Fiyat      :", self.fiyat)
        print("4: Ürün Üretim Yeri:", self.uretimYeri)
        print("5: Ürün Kategorisi :", self.kategori)
        print("6: Ürün STT        :", self.stt)
        secim = int(input("Değiştirmek istediginiz değeri girin: "))

        if secim == 1:
            self.isim = (input("Ürün Adını Giriniz: "))

        elif secim == 2:
            self.adet = int(input("Ürün Adetini Giriniz: "))

        elif secim == 3:
            self.fiyat = int(input("Ürün Fiyatını Giriniz: "))

        elif secim == 4:
            self.uretimYeri = (input("Ürün Üretim Yeri Giriniz: "))

        elif secim == 5:
            self.kategori = int(input("Ürün Kategorisi Giriniz: "))

        elif secim == 6:
            self.stt = int(input("Ürün STT Giriniz: "))

        else:
            print("Geçerli Bir Değer Giriniz!\n")

    def UrunBilgi(self):
        print("\n" + self.isim, "Ürünü bilgisi")
        print("---------------------------------")
        print("Adeti (Kg)  :", self.adet, "Kg")
        print("Fiyat       :", self.fiyat, "₺")
        print("Kategori    :", self.kategori)
        print("Üretim Yeri :", self.uretimYeri)
        print("STT (Ay)    :", self.stt, "Ay")

# Nesneler
telefon = Elektronik("Iphone 14 Pro", 120, 35000, "Iphone", "Telefon", "USA", 2027)
tablet = Elektronik("Samsung Tab 7", 400, 4000, "Samsung", "Tablet", "TAIWAN", 2025)
laptop = Elektronik("MSI G63", 320, 45000, "MSI", "Bilgisayar", "CHINA", 2025)
kulaklık = Elektronik("Abingo BT30NC", 200, 560, "Abingo", "Çevre Birimleri", "CHINA", 2024)
mouse = Elektronik("Logitech G102", 400, 220, "Logitech", "Çevre Birimleri", "SWEDEN", 2024)
klavye = Elektronik("Logitech G203", 800, 350, "Logitech", "Çevre Birimleri", "FRANCE", 2024)
elektronikListe = [telefon, tablet, laptop, kulaklık, mouse, klavye]
#
elma = Organik("Elma", 1000, 12, "Meyve", "Amasya/Turkey", 2)
armut = Organik("Armut", 600, 14, "Meyve", "Mugla/Turkey", 2)
muz = Organik("Muz", 400, 22, "Meyve", "Mumbai/India", 4)
domates = Organik("Domates", 6000, 20, "Sebze", "Rotterdam/The Netherlands", 3)
havuc = Organik("Havuç", 1000, 25, "Sebze", "Kars/Turkey", 5)
salatalık = Organik("Salatalık", 3000, 14, "Sebze", "Bursa/Turkey", 6)
organikListe = [elma, armut, muz, domates, havuc, salatalık]

#Fonksiyonlar
def UrunEkle(liste):
    alimIndex = 1
    print("\n-----------------------------------------------")
    for i in liste:
        print(alimIndex, i.isim)
        print("Güncel Adet:", i.adet)
        print("-----------------------------------------------")
        alimIndex += 1
    alimInput = int(input("Ürün Numarası Giriniz: "))
    
    if alimInput == 0:
        print("\n> Geçerli Bir Değer Giriniz!\n")
    
    else:
        try:
            liste[alimInput-1].UrunEkle()

        except:
            print("\n> Geçerli Bir Değer Giriniz!\n")

def UrunCıkart(liste):
    alimIndex = 1
    print("\n-----------------------------------------------")
    for i in liste:
        print(alimIndex, i.isim)
        print("Güncel Adet:", i.adet)
        print("-----------------------------------------------")
        alimIndex += 1
    alimInput = int(input("Ürün Numarası Giriniz: "))
    
    if alimInput == 0:
        print("\n> Geçerli Bir Değer Giriniz!\n")
    
    else:
        try:
            liste[alimInput-1].UrunSilme()

        except:
            print("\n> Geçerli Bir Değer Giriniz!\n")

def BilgiGuncelle(liste):
    alimIndex = 1
    print("\n-----------------------------------------------")
    for i in liste:
        print(alimIndex, i.isim)
        print("-----------------------------------------------")
        alimIndex += 1
    alimInput = int(input("Ürün Numarası Giriniz: "))
    
    if alimInput == 0:
        print("\n> Geçerli Bir Değer Giriniz!\n")
    
    else:
        try:
            liste[alimInput-1].BilgiGuncelleme()

        except:
            print("\n> Geçerli Bir Değer Giriniz!\n")

# Ana Döngü
while True:
    print("\n------------------------------------------------")
    print("        Depo Kontrol ve Otomasyon Sistemi         ")
    print("------------------------------------------------")
    print("> 1- Elektronik Deposu")
    print("> 2- Organik Ürün Hali")
    print("> 3- Hakkında")
    print("> 0- Çıkış\n")
    anasayfaSayfa = int(input("Sayfa Numarası Giriniz: "))

    # Çıkış
    if anasayfaSayfa == 0:
        print("\nDepodan Çıkıldı.")
        break

    # Elektronik Deposu
    elif anasayfaSayfa == 1:
        while True:
            print("\n------------------------------------------------")
            print("                 Elektronik Deposu                ")
            print("------------------------------------------------")
            print("> 1- Tüm Ürünleri Gör")
            print("> 2- Ürün Ekle")
            print("> 3- Ürün Çıkart")
            print("> 4- Ürün Bilgisi Güncelle")
            print("> 0- Çıkış\n")
            elektronikSayfa = int(input("Sayfa Numarası Giriniz: "))
            if elektronikSayfa == 0:
                print("\nAnasayfaya Dönüldü.")
                break

            # Tüm Ürünleri Gör
            elif elektronikSayfa == 1:
                for i in elektronikListe:
                    i.UrunBilgi()

            # Ürün Ekle
            elif elektronikSayfa == 2:
                UrunEkle(elektronikListe)

            # Ürün Çıkart
            elif elektronikSayfa == 3:
                UrunCıkart(elektronikListe)

            # Ürün Güncelle
            elif elektronikSayfa == 4:
                BilgiGuncelle(elektronikListe)

            # Hata
            else:
                print("\n> Geçerli Bir Değer Giriniz!\n")

    # Organik Ürün Hali
    elif anasayfaSayfa == 2:
        while True:
            print("\n------------------------------------------------")
            print("                 Organik Ürün Hali                ")
            print("------------------------------------------------")
            print("> 1- Tüm Ürünleri Gör")
            print("> 2- Ürün Ekle")
            print("> 3- Ürün Çıkart")
            print("> 4- Ürün Bilgisi Güncelle")
            print("> 0- Çıkış\n")
            organikSayfa = int(input("Sayfa Numarası Giriniz: "))
            if organikSayfa == 0:
                print("\nAnasayfaya Dönüldü.")
                break

            # Tüm Ürünleri Gör
            elif organikSayfa == 1:
                for i in organikListe:
                    i.UrunBilgi()

            # Ürün Ekle
            elif organikSayfa == 2:
                UrunEkle(organikListe)

            # Ürün Çıkart
            elif organikSayfa == 3:
                UrunCıkart(organikListe)

            # Ürün Güncelle
            elif organikSayfa == 4:
                BilgiGuncelle(organikListe)

            # Hata
            else:
                print("\n> Geçerli Bir Değer Giriniz!\n")

    # Hakkında
    elif anasayfaSayfa == 3:
        print("\n------------------------")
        print("Yapımcılar: Eren Elagöz\n")
        print("Depo Yönetim Otomasyonu, Birçok farklı ürün için entegre edebileceğiniz text-based depo yönetim sistemi")
        print("Ürünler üzerinden stok güncelleme azaltma artırma, ürün bilgilerini güncelle yapabileceğiniz ekrana sahiptir.")
        print("Aynı anda hem elektronik hemde organik deposu olan otomasyon sistemi\n")

    # Hata
    else:
        print("\n> Geçerli Bir Değer Giriniz!\n")
