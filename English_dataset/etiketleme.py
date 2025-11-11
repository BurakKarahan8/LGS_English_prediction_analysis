import csv
import os
import json

# Eğer dosya yoksa oluştur
filename = "lgs_dataset.csv"
fieldnames = ["id", "yıl", "ders", "konu", "soru_metni", "görsel_yolu", "şıklar", "doğru_cevap"]

if not os.path.exists(filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

print("💡 LGS Veri Seti Etiketleme Aracı\n")

while True:
    soru = {}
    with open(filename, "r", encoding="utf-8") as f:
        existing = sum(1 for _ in f) - 1  # başlık hariç satır sayısı
    soru["id"] = existing + 1
    
    soru["yıl"] = input("Yıl: ")
    soru["ders"] = input("Ders: ")
    soru["konu"] = input("Konu: ")
    soru["soru_metni"] = input("Soru metnini yapıştır: ")
    soru["görsel_yolu"] = input("Görsel yolu (yoksa boş bırak): ")

    # Şıkları JSON formatında al
    print("Şıkları sırayla gir:")
    seçenekler = {}
    for secenek in ["A", "B", "C", "D"]:
        seçenekler[secenek] = input(f"{secenek}: ")
    soru["şıklar"] = json.dumps(seçenekler, ensure_ascii=False)
    
    soru["doğru_cevap"] = input("Doğru cevap (A/B/C/D): ").upper()

    # CSV’ye kaydet
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(soru)

    devam = input("\nYeni soru eklemek ister misin? (E/H): ").upper()
    if devam != "E":
        print("✅ Etiketleme tamamlandı! Veri 'lgs_dataset.csv' dosyasına kaydedildi.")
        break
