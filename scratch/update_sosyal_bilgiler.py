import re

def update_sosyal():
    path = r"c:\Users\Kemal ŞİMŞEK\OneDrive\Desktop\MufredatVar\lib\data\subjects\sosyal_bilgiler_data.dart"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find where grade 6, 7, 8 start
    idx_g6 = -1
    idx_g7 = -1
    idx_g8 = -1
    
    for i, line in enumerate(lines):
        if "6: GradeCurriculum(" in line:
            idx_g6 = i
        elif "7: GradeCurriculum(" in line:
            idx_g7 = i
        elif "8: GradeCurriculum(" in line:
            idx_g8 = i

    print(f"Indices: g6={idx_g6}, g7={idx_g7}, g8={idx_g8}")
    
    # In Grade 6:
    # Update subtitle and badgeText
    lines[idx_g6 + 3] = "        subtitle: 'Türkiye Yüzyılı Maarif Modeli (6 Öğrenme Alanı)',\n"
    lines[idx_g6 + 4] = "        badgeText: 'Maarif Modeli ✨',\n"
    
    # Map weeks to Maarif themes in Grade 6:
    # W1-6: Birlikte Yaşamak
    # W7-12: Evimiz Dünya
    # W13-18: Ortak Mirasımız
    # W19-24: Yaşayan Demokrasimiz
    # W25-30: Hayatımızdaki Ekonomi
    # W31-36: Teknoloji ve Sosyal Bilimler
    g6_theme_map = {
        range(1, 7): "Birlikte Yaşamak",
        range(7, 13): "Evimiz Dünya",
        range(13, 19): "Ortak Mirasımız",
        range(19, 25): "Yaşayan Demokrasimiz",
        range(25, 31): "Hayatımızdaki Ekonomi",
        range(31, 37): "Teknoloji ve Sosyal Bilimler",
    }
    
    current_w = None
    for i in range(idx_g6, idx_g7):
        line = lines[i]
        m_w = re.search(r"weekNumber:\s*(\d+)", line)
        if m_w:
            current_w = int(m_w.group(1))
        if current_w is not None and "theme:" in line:
            for r, theme_name in g6_theme_map.items():
                if current_w in r:
                    lines[i] = f"            theme: '{theme_name}',\n"
                    break

    # In Grade 7:
    # Update subtitle and badgeText
    lines[idx_g7 + 3] = "        subtitle: 'Türkiye Yüzyılı Maarif Modeli (6 Öğrenme Alanı)',\n"
    lines[idx_g7 + 4] = "        badgeText: 'Maarif Modeli ✨',\n"
    
    # Map weeks to Maarif themes in Grade 7:
    g7_theme_map = {
        range(1, 7): "Birlikte Yaşamak",
        range(7, 13): "Evimiz Dünya",
        range(13, 19): "Ortak Mirasımız",
        range(19, 25): "Yaşayan Demokrasimiz",
        range(25, 31): "Hayatımızdaki Ekonomi",
        range(31, 37): "Teknoloji ve Sosyal Bilimler",
    }
    
    current_w = None
    for i in range(idx_g7, idx_g8):
        line = lines[i]
        m_w = re.search(r"weekNumber:\s*(\d+)", line)
        if m_w:
            current_w = int(m_w.group(1))
        if current_w is not None and "theme:" in line:
            for r, theme_name in g7_theme_map.items():
                if current_w in r:
                    lines[i] = f"            theme: '{theme_name}',\n"
                    break

    # In Grade 8:
    # Update subtitle and badgeText
    lines[idx_g8 + 3] = "        subtitle: 'Türkiye Yüzyılı Maarif Modeli & LGS (7 Ünite)',\n"
    lines[idx_g8 + 4] = "        badgeText: 'Maarif Modeli ✨',\n"
    
    g8_theme_map = {
        range(1, 7): "Bir Kahraman Doğuyor",
        range(7, 13): "Millî Uyanış: Bağımsızlık Yolunda Atılan Adımlar",
        range(13, 19): "Millî Bir Destan: Ya İstiklal Ya Ölüm!",
        range(19, 25): "Atatürk ve Çağdaşlaşan Türkiye",
        range(25, 29): "Demokratikleşme Çabaları",
        range(29, 33): "Atatürk Dönemi Türk Dış Politikası",
        range(33, 37): "Atatürk'ün Ölümü ve Sonrası",
    }
    
    current_w = None
    for i in range(idx_g8, len(lines)):
        line = lines[i]
        m_w = re.search(r"weekNumber:\s*(\d+)", line)
        if m_w:
            current_w = int(m_w.group(1))
        if current_w is not None and "theme:" in line:
            for r, theme_name in g8_theme_map.items():
                if current_w in r:
                    lines[i] = f"            theme: '{theme_name}',\n"
                    break

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("Successfully updated sosyal_bilgiler_data.dart with Maarif Modeli themes and badges!")

if __name__ == "__main__":
    update_sosyal()
