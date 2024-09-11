import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Görseller için gerekli kütüphane
import time
import threading  # Sayaç işlemini arka planda çalıştırmak için

# Yumurta pişirme süreleri (dakika cinsinden)
yumurta_kivamlari = {
    'Soft-Boiled (Cıvık)': {'sure': 4, 'image': 'soft_boiled.jpg'},
    'Medium-Boiled (Kayısı)': {'sure': 6, 'image': 'medium_boiled.jpg'},
    'Hard-Boiled (Sert)': {'sure': 9, 'image': 'hard_boiled.jpg'},
    'Poached (Çılbır)': {'sure': 3, 'image': 'poached.jpg'}
}

def sayaci_baslat(sure):
    for dakika in range(sure, 0, -1):
        zaman_label.config(text=f"Kalan süre: {dakika} dakika")
        root.update()  # Arayüzü güncelle
        time.sleep(1)  # Test için süreyi hızlandır (normalde 60 saniye olacak)
    messagebox.showinfo("Yumurtanız Hazır", "Yumurtanız pişti!")

def kivam_sec(kivam):
    secilen_kivam = yumurta_kivamlari.get(kivam)
    if secilen_kivam:
        sure = secilen_kivam['sure']
        image_path = secilen_kivam['image']
        
        # Görseli göster
        img = Image.open(image_path)
        img = img.resize((200, 150))  # Görsel boyutunu ayarla
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img  # Referansı sakla
        
        zaman_label.config(text=f"{kivam} seçildi. Pişirme süresi: {sure} dakika.")
        
        # Sayaç başlatma işlemini ayrı bir thread ile yapıyoruz ki arayüz donmasın
        t = threading.Thread(target=sayaci_baslat, args=(sure,))
        t.start()
    else:
        messagebox.showerror("Hata", "Geçersiz seçim!")

# Ana Tkinter penceresi
root = tk.Tk()
root.title("Yumurta Kıvamı Hesaplayıcı")

# Başlık
baslik_label = tk.Label(root, text="İdeal Yumurta Kıvamı Seçimi", font=("Helvetica", 16))
baslik_label.pack(pady=10)

# Yumurta kıvamı düğmeleri
for kivam in yumurta_kivamlari:
    button = tk.Button(root, text=kivam, width=25, command=lambda k=kivam: kivam_sec(k))
    button.pack(pady=5)

# Görseli gösterecek etiket
img_label = tk.Label(root)
img_label.pack(pady=10)

# Zaman geri sayımı
zaman_label = tk.Label(root, text="")
zaman_label.pack(pady=5)

root.mainloop()
