import json

def format_entry(entry):
    text = "<|startoftext|>\n"
    text += "[KONU]\n"
    text += entry.get("konu", "") + "\n\n"
    
    if entry.get("kontext"):
        text += "[KONTEXT]\n"
        text += entry["kontext"] + "\n\n"
        
    text += "[SORU]\n"
    text += entry["soru_metni"] + "\n\n"
    
    text += "[SEÇENEKLER]\n"
    options = entry.get("secenekler", {})
    # Seçenekleri A, B, C, D sırasıyla eklediğimizden emin olalım
    for key in sorted(options.keys()):
        text += f"{key}) {options[key]}\n"
        
    text += "\n[CEVAP]\n"
    text += entry.get("dogru_cevap", "") + "\n"
    
    text += "<|endoftext|>\n"
    return text

# 1. Adım: Tüm verilerin olduğu data.json dosyasını yükle
try:
    with open('sorular.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Hata: 'sorular.json' dosyası bulunamadı.")
    exit()

# 2. Adım: Tüm verileri tek bir metin dosyasına yaz
with open('training_data.txt', 'w', encoding='utf-8') as f:
    for entry in data:
        formatted_text = format_entry(entry)
        f.write(formatted_text)

print(f"'training_data.txt' dosyası {len(data)} soru ile oluşturuldu.")