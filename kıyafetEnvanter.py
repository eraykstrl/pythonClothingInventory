
class Kiyafet:
    
    def __init__(self,tür,renk,adet,tarz):
        self.tür=tür
        self.renk=renk
        self.adet=adet
        self.tarz=tarz
    
    
kiyafet1 = Kiyafet("sweatshirt", "beyaz", 32, "bol")
kiyafet2 = Kiyafet("sweatshirt", "kırmızı", 13, "dar")
kiyafet3 = Kiyafet("şort", "mavi", 28, "sport şort")
kiyafet4 = Kiyafet("şort", "beyaz", 1, "deniz şortu")
kiyafet5 = Kiyafet("eşoftman", "gri", 4, "dar")
kiyafet6 = Kiyafet("eşoftman", "siyah", 18, "bol")
kiyafet7 = Kiyafet("tişört", "siyah", 7, "dar")
kiyafet8 = Kiyafet("tişört", "sarı", 13, "bol")
kiyafet9 = Kiyafet("tişört", "sarı", 10, "bol")
kiyafet10 = Kiyafet("atlet", "beyaz", 34, "bol")
kiyafet11 = Kiyafet("atlet", "gri", 43, "bol")
kiyafet12 = Kiyafet("çorap", "beyaz", 76, "uzun")
kiyafet13 = Kiyafet("çorap", "gri", 89, "kısa")
kiyafet14 = Kiyafet("kot pantolon", "mavi", 18, "bol kot ")
kiyafet15 = Kiyafet("pantolon", "siyah", 21, "bol kumaş")
kiyafet16 = Kiyafet("pantolon", "gri", 35, "dar keten")
kiyafet17 = Kiyafet("şort", "siyah", 26, "kot şort")
kiyafet18 = Kiyafet("tişört", "siyah", 7, "dar")

kiyafetler = [kiyafet1, kiyafet2, kiyafet3, kiyafet4, kiyafet5, kiyafet6, kiyafet7, kiyafet8,
              kiyafet9, kiyafet10, kiyafet11, kiyafet12, kiyafet13, kiyafet14, kiyafet15,
              kiyafet16, kiyafet17, kiyafet18 ]
        


def tişörtleriGoster(kiyafetler):
    tişörtler = [kiyafet for kiyafet in kiyafetler if kiyafet.tür == "tişört"]
    print("------ Tişörtler ------")
    for kiyafet in tişörtler:
        print(f"{kiyafet.adet} adet {kiyafet.renk} renkli tişört ({kiyafet.tarz} kesim)")

def pantolonlarıGoster(kiyafetler):
    pantolonlar = [kiyafet for kiyafet in kiyafetler if kiyafet.tür == "pantolon"]
    print("------ Pantolonlar ------")
    for kiyafet in pantolonlar:
        print(f"{kiyafet.adet} adet {kiyafet.renk} renkli kot pantolon ({kiyafet.tarz} kesim)")

def sweatshirtleriGoster(kiyafetler):
    sweatshirtler = [kiyafet for kiyafet in kiyafetler if kiyafet.tür == "sweatshirt"]
    print("------ Sweatshirtler ------")
    for kiyafet in sweatshirtler:
        print(f"{kiyafet.adet} adet {kiyafet.renk} renkli sweatshirt ({kiyafet.tarz} kesim)")

def şortlarıGoster(kiyafetler):
    şortlar =[kiyafet for kiyafet in kiyafetler if kiyafet.tür=="şort"]
    print("------ Şortlar ------")
    for kiyafet in şortlar:
        print(f"{kiyafet.adet} adet {kiyafet.renk} renkli şort ({kiyafet.tarz} kesim)")

def eşoftmanlarıGoster(kiyafetler):
    eşoftmanlar = [kiyafet for kiyafet in kiyafetler if kiyafet.tür == "eşoftman"]
    print("------ Eşoftmanlar ------")
    for kiyafet in eşoftmanlar:
        print(f"{kiyafet.adet} adet {kiyafet.renk} renkli eşoftman ({kiyafet.tarz} kesim)")


def çoraplarıGoster(kiyafetler):
    çoraplar = [kiyafet for kiyafet in kiyafetler if kiyafet.tür == "çorap"]
    print("------ Çoraplar ------")
    for kiyafet in çoraplar:
        print(f"{kiyafet.adet} adet {kiyafet.renk} renkli çorap ({kiyafet.tarz} kesim)")

def atletleriGoster(kiyafetler):
    atletler = [kiyafet for kiyafet in kiyafetler if kiyafet.tür == "atlet"]
    print("------ Atletler ------")
    for kiyafet in atletler:
        print(f"{kiyafet.adet} adet {kiyafet.renk} renkli atlet ({kiyafet.tarz} kesim)")
def kiyafetEkle(kiyafetler):
    tür=input("Eklemek istediğiniz kıyafetin türü: ")
    renk=input("Eklemek istediğiniz kıyafetin renki: ")
    adet=input("Bu kıyafetten kaç tane eklemek istiyorsunuz? ")
    tarz=input("Bu kıyafetin hangi tarzından getirtmek isterisinz ")
    kiyafet=Kiyafet(tür,renk,adet,tarz)
    kiyafetler.append(kiyafet)
    print("Eklemek istediğiniz kıyafet başarıyla eklendi. ")
    
    
while True:
    print("--- Kıyafet Envanter Mağazası ---")
    print("1. Kıyafetleri Göster")
    print("2. Kıyafet Ekle")
    print("0. Çıkış")
    secim = input("Seçiminizi yapın: ")

    if secim == '0':
        print("Çıkış yapılıyor")
        break
    elif secim == '1':
        
        secim2=input("Hangi kıyafet türlerini görmek istersiniz (pantolon,tişört,şort,sweatshirt,atlet,çorap,eşotman): ")
        if secim2 == "pantolon":
            pantolonlarıGoster(kiyafetler)

        elif secim2 == "tişört":
            tişörtleriGoster(kiyafetler)

        elif secim2 == "sweatshirtler":
            sweatshirtleriGoster(kiyafetler)

        elif secim2 == "şort":
            şortlarıGoster(kiyafetler)

        elif secim2 == "çorap":
            çoraplarıGoster(kiyafetler)

        elif secim2 == "atlet":
            atletleriGoster(kiyafetler)
    
        elif secim2 == "eşoftman":
            eşoftmanlarıGoster(kiyafetler)

        else:
            print("Geçersiz seçim yaptınız lütfen başka seçenek seçiniz.")

    elif secim == '2':
        
        kiyafetEkle(kiyafetler)
    
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")



