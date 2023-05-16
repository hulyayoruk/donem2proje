def basla():
    print("-------Deprem Sonrası Yardım Sistemi-------")
    ad_soyad = input("Adınız ve soyadınızı girin: ")
    kullanici_tipi = input("Kendiniz için mi, tanıdığınız için mi veya yardım etmek için mi kullanıyorsunuz? (Kendim/Tanıdık/Yardım): ")

    if kullanici_tipi.lower() == "admin":
        admin_giris()
    elif kullanici_tipi.lower() == "kullanici":
        kullanici_giris(ad_soyad)
    else:
        print("Geçersiz kullanıcı tipi! Sistem sonlandırılıyor.")
        return

def admin_giris():
    admin_sifre = "admin123"  # Admin giriş şifresi
    giris_sifresi = input("Admin şifresini girin: ")
    if giris_sifresi == admin_sifre:
        print("Admin girişi başarılı.")
        fiyat_belirle()
    else:
        print("Hatalı admin şifresi! Sistem sonlandırılıyor.")

def fiyat_belirle():
    yeni_fiyat = float(input("Yeni yemek fiyatını girin: "))
    print("Yeni yemek fiyatı belirlendi:", yeni_fiyat)
    basla()

def kullanici_giris(ad_soyad):
    print("Hoş geldiniz, {}!".format(ad_soyad))
    kisiler = int(input("Kaç kişilik bir grup için yardım talep ediyorsunuz? "))
    kisiler_listesi = []

    for i in range(kisiler):
        kisi_adi = input("{}. kişinin adını girin: ".format(i+1))
        kisi_yas = int(input("{}. kişinin yaşını girin: ".format(i+1)))
        kisiler_listesi.append({"Ad": kisi_adi, "Yaş": kisi_yas})

    if kisiler > 10:
        indirim_orani = 0.4
    elif kisiler > 5:
        indirim_orani = 0.3
    else:
        indirim_orani = 0

    toplam_fiyat = kisiler * 10  # Her bir kişi için 10 birim ücret

    if indirim_orani > 0:
        toplam_fiyat -= toplam_fiyat * indirim_orani

    cocuk_varmi = input("Aralarında çocuk var mı? (Evet/Hayır): ")
    if cocuk_varmi.lower() == "evet":
        oyuncaklar = ["Araba", "Bebek"]
        print("Çocuklar için oyuncak alternatifleri: ")
        for oyuncak in oyuncaklar:
            print("- " + oyuncak)

    print("Toplam fiyat: ", toplam_fiyat)
   
