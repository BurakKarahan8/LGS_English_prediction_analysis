import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import os

# Dosya adı
<<<<<<< Updated upstream
FILENAME = "lgs_veri_seti_v7.json"
=======
FILENAME = "lgs_veri_seti_v6.json"
>>>>>>> Stashed changes

class LGSLabeler:
    def __init__(self, root):
        self.root = root
        self.root.title("LGS İngilizce Veri Etiketleme Asistanı")
        self.root.geometry("700x850")

        # Üniteler Listesi
        self.units = [
            "1. Friendship", "2. Teen Life", "3. In The Kitchen", 
            "4. On The Phone", "5. The Internet", "6. Adventures", 
            "7. Tourism", "8. Chores", "9. Science", "10. Natural Forces"
        ]

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # 1. Ünite Seçimi
        tk.Label(self.root, text="Ünite Seçiniz:", font=("Arial", 10, "bold")).pack(pady=5)
        self.unit_var = tk.StringVar()
        self.unit_combo = ttk.Combobox(self.root, textvariable=self.unit_var, values=self.units, state="readonly")
        self.unit_combo.pack()
        self.unit_combo.current(0)

        # 2. Context (Görsel Tasviri / Diyalog / Tablo)
        tk.Label(self.root, text="Context (Metin/Diyalog/Tablo Verisi):", font=("Arial", 10, "bold"), fg="red").pack(pady=5)
        tk.Label(self.root, text="* Tabloları ve görselleri buraya metin olarak dökün.", font=("Arial", 8)).pack()
        self.txt_context = scrolledtext.ScrolledText(self.root, height=8, width=70)
        self.txt_context.pack(pady=5)

        # 3. Soru Kökü
        tk.Label(self.root, text="Soru Metni (Kökü):", font=("Arial", 10, "bold")).pack(pady=5)
        self.txt_question = tk.Text(self.root, height=3, width=70)
        self.txt_question.pack(pady=5)

        # 4. Seçenekler
        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=10)
        
        self.entries_opts = {}
        for idx, opt in enumerate(["A", "B", "C", "D"]):
            tk.Label(options_frame, text=f"{opt})").grid(row=idx, column=0, padx=5, pady=2)
            entry = tk.Entry(options_frame, width=60)
            entry.grid(row=idx, column=1, padx=5, pady=2)
            self.entries_opts[opt] = entry

        # 5. Doğru Cevap
        tk.Label(self.root, text="Doğru Cevap:", font=("Arial", 10, "bold")).pack(pady=5)
        self.correct_var = tk.StringVar()
        self.combo_correct = ttk.Combobox(self.root, textvariable=self.correct_var, values=["A", "B", "C", "D"], state="readonly", width=10)
        self.combo_correct.pack()

        # Kaydet Butonu ve İstatistik
        btn_save = tk.Button(self.root, text="KAYDET ve TEMİZLE", bg="green", fg="white", font=("Arial", 12, "bold"), command=self.save_entry)
        btn_save.pack(pady=20)

        self.lbl_stats = tk.Label(self.root, text="Toplam Kayıtlı Soru: 0", fg="blue")
        self.lbl_stats.pack()

    def load_data(self):
        if os.path.exists(FILENAME):
            with open(FILENAME, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        else:
            self.data = []
        self.update_stats()

    def update_stats(self):
        self.lbl_stats.config(text=f"Toplam Kayıtlı Soru: {len(self.data)}")

    def save_entry(self):
        # Verileri al
        unit = self.unit_var.get()
        context = self.txt_context.get("1.0", tk.END).strip()
        question = self.txt_question.get("1.0", tk.END).strip()
        correct = self.correct_var.get()
        
        # Validasyon
        if not question or not correct:
            messagebox.showwarning("Eksik Veri", "Lütfen en az soru metni ve doğru cevabı giriniz.")
            return

        options = {k: v.get().strip() for k, v in self.entries_opts.items()}

        # JSON objesi oluştur
        new_entry = {
            "id": len(self.data) + 1,
            "konu": unit,
            "kontext": context,  # Burası boş olabilir, sorun değil
            "soru_metni": question,
            "secenekler": options,
            "dogru_cevap": correct
        }

        self.data.append(new_entry)

        # Anında Dosyaya Yaz (Veri kaybını önlemek için)
        with open(FILENAME, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

        # Alanları Temizle
        self.txt_context.delete("1.0", tk.END)
        self.txt_question.delete("1.0", tk.END)
        for entry in self.entries_opts.values():
            entry.delete(0, tk.END)
        self.combo_correct.set("")
        
        self.update_stats()
        # messagebox.showinfo("Başarılı", "Soru kaydedildi!") # Hız kesmemek için bunu kapattım

if __name__ == "__main__":
    root = tk.Tk()
    app = LGSLabeler(root)
    root.mainloop()