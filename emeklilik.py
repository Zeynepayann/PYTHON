

# Kullanıcıdan doğum yılını alıyoruz
dogum_yili = int(input("Doğum yılı: "))

# 1. Güncel yılı döndüren fonksiyon
def guncel_yil_getir():
    # Bu fonksiyon, sadece mevcut yılı döndürmekle sorumludur.
    import datetime
    return datetime.datetime.now().year

# Güncel yılı bir değişkene atıyoruz
# Fonksiyon çağrısının sonucu (int) direkt 'guncel_yil' değişkenine atanır.
guncel_yil = guncel_yil_getir()

# 2. Yaş hesaplama fonksiyonu
def yas_hesapla(guncel_yil, dogum_yili):
    # Yaşı hesaplar ve döndürür.
    return guncel_yil - dogum_yili

# Güncel yaşı hesaplayıp yazdırıyoruz
print("Güncel yaş: ", yas_hesapla(guncel_yil, dogum_yili))

# 3. Emeklilik durumu hesaplama fonksiyonu
# Bu fonksiyon, yas_hesapla'yı tekrar çağırarak güncel yaşı bulur.
def emeklilik_durumu_hesapla(isim, dogum_yili, guncel_yil):
    # Yaşı hesaplamak için diğer fonksiyonu kullanıyoruz
    yas = yas_hesapla(guncel_yil, dogum_yili)
    
    # Kalan süre (65 yaş emeklilik kabul edilmiştir)
    kalan_sure = 65 - yas
    
    # 4. Mantıksal kontrol
    if kalan_sure > 0:
        # Emekliliğe kalan süre pozitifse
        return f"{isim}, emekliliğinize {kalan_sure} yıl kaldı."
    else:
        # Emeklilik yaşı geçilmişse. 
        # abs() mutlak değeri verir (Örn: -5 -> 5)
        return f"{isim}, {abs(kalan_sure)} yıldır emeklisiniz."
    
# Emeklilik durumunu hesaplayıp yazdırıyoruz

print(emeklilik_durumu_hesapla("Ayşe", dogum_yili, guncel_yil))
