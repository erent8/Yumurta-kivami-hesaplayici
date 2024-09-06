# Yumurta-kivami-hesaplayici

import time

# Yumurta pişirme süreleri (dakika cinsinden)
yumurta_kivamlari = {
    'Soft-Boiled (Cıvık)': 4,
    'Medium-Boiled (Kayısı)': 6,
    'Hard-Boiled (Sert)': 9,
    'Poached (Çılbır)': 3
}

def yumurta_pisirme_suresi_bul(kivam):
    return yumurta_kivamlari.get(kivam, None)

def sayaci_baslat(sure):
    print(f"Yumurta {sure} dakika boyunca pişecek.")
    for dakika in range(sure, 0, -1):
        print(f"Kalan süre: {dakika} dakika")
        time.sleep(60)  # 1 dakikalık bekleme (örnekte beklemeyi 1 saniyeye düşürebilirsin test için)
    print("Yumurtanız hazır!")

def main():
    print("İdeal yumurta kıvamı hesaplama programına hoş geldiniz!")
    print("Lütfen istediğiniz kıvamı seçin:")
    for kivam in yumurta_kivamlari:
        print(f"- {kivam}")
    
    secilen_kivam = input("Seçiminiz: ")
    
    sure = yumurta_pisirme_suresi_bul(secilen_kivam)
    if sure:
        print(f"Seçtiğiniz kıvam: {secilen_kivam}. Pişirme süresi: {sure} dakika.")
        sayaci_baslat(sure)
    else:
        print("Geçersiz seçim, lütfen listedeki bir kıvamı seçin.")

if __name__ == "__main__":
    main()
