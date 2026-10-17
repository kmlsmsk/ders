import re
import os

def update_file(path, replacements):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
        
    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"No changes made to {path}")

def update_grade_math_files():
    # Grade 6
    p6 = r"c:\Users\Kemal ŞİMŞEK\OneDrive\Desktop\MufredatVar\lib\data\grade_6_data.dart"
    update_file(p6, [
        ("subtitle: 'Çarpanlar & Katlar, Tam Sayılar & Alan',", "subtitle: 'Türkiye Yüzyılı Maarif Modeli (7 Tema)',"),
        ("badgeText: 'Ortaokul 2. Kademe',", "badgeText: 'Türkiye Yüzyılı Maarif Modeli ✨',"),
    ])
    
    # Grade 7
    p7 = r"c:\Users\Kemal ŞİMŞEK\OneDrive\Desktop\MufredatVar\lib\data\grade_7_data.dart"
    update_file(p7, [
        ("subtitle: 'Tam Sayılar, Rasyonel Sayılar & Çember',", "subtitle: 'Türkiye Yüzyılı Maarif Modeli (7 Tema)',"),
        ("badgeText: 'LGS Hazırlık Temeli',", "badgeText: 'Türkiye Yüzyılı Maarif Modeli ✨',"),
    ])
    
    # Grade 8
    p8 = r"c:\Users\Kemal ŞİMŞEK\OneDrive\Desktop\MufredatVar\lib\data\grade_8_data.dart"
    update_file(p8, [
        ("subtitle: 'Çarpanlar & Katlar, Üslü-Köklü & Geometri',", "subtitle: 'Türkiye Yüzyılı Maarif Modeli & LGS (Süreç Odaklı)',"),
        ("badgeText: 'LGS Hedef Odaklı',", "badgeText: 'Türkiye Yüzyılı Maarif Modeli ✨',"),
    ])

def update_fen_bilimleri():
    p = r"c:\Users\Kemal ŞİMŞEK\OneDrive\Desktop\MufredatVar\lib\data\subjects\fen_bilimleri_data.dart"
    update_file(p, [
        ("subtitle: 'Ortaokul 2. Kademe Fen Programı',", "subtitle: 'Türkiye Yüzyılı Maarif Modeli (7 Ünite)',"),
        ("badgeText: 'Ortaokul Fen',", "badgeText: 'Maarif Modeli ✨',"),
        ("subtitle: 'Ortaokul 3. Kademe Fen Programı',", "subtitle: 'Türkiye Yüzyılı Maarif Modeli (7 Ünite)',"),
        ("subtitle: 'LGS Hazırlık ve Fen Okuryazarlığı',", "subtitle: 'Türkiye Yüzyılı Maarif Modeli & LGS (7 Ünite)',"),
        ("badgeText: 'LGS Fen',", "badgeText: 'Maarif Modeli ✨',"),
    ])

def update_din_kulturu():
    p = r"c:\Users\Kemal ŞİMŞEK\OneDrive\Desktop\MufredatVar\lib\data\subjects\din_kulturu_data.dart"
    update_file(p, [
        ("subtitle: 'Ortaokul Din Kültürü ve Ahlak Bilgisi',", "subtitle: 'Türkiye Yüzyılı Maarif Modeli (5 Ünite)',"),
        ("badgeText: 'Ortaokul Din',", "badgeText: 'Maarif Modeli ✨',"),
        ("subtitle: 'LGS Hazırlık ve Ahlak Eğitimi',", "subtitle: 'Türkiye Yüzyılı Maarif Modeli & LGS (5 Ünite)',"),
        ("badgeText: 'LGS Din Kültürü',", "badgeText: 'Maarif Modeli ✨',"),
    ])

def update_ingilizce():
    p = r"c:\Users\Kemal ŞİMŞEK\OneDrive\Desktop\MufredatVar\lib\data\subjects\ingilizce_data.dart"
    update_file(p, [
        ("subtitle: 'Ortaokul İngilizce Programı (10 Ünite)',", "subtitle: 'Türkiye Yüzyılı Maarif Modeli (10 Ünite)',"),
        ("badgeText: 'Ortaokul İngilizce',", "badgeText: 'Maarif Modeli ✨',"),
        ("subtitle: 'LGS Hazırlık ve İngilizce Becerileri',", "subtitle: 'Türkiye Yüzyılı Maarif Modeli & LGS (10 Ünite)',"),
        ("badgeText: 'LGS İngilizce',", "badgeText: 'Maarif Modeli ✨',"),
    ])

def update_bilisim():
    p = r"c:\Users\Kemal ŞİMŞEK\OneDrive\Desktop\MufredatVar\lib\data\subjects\bilisim_data.dart"
    update_file(p, [
        ("subtitle: 'Ortaokul Bilişim Teknolojileri ve Yazılım',", "subtitle: 'Türkiye Yüzyılı Maarif Modeli (6 Tema)',"),
        ("badgeText: 'Ortaokul Bilişim',", "badgeText: 'Maarif Modeli ✨',"),
    ])

if __name__ == "__main__":
    update_grade_math_files()
    update_fen_bilimleri()
    update_din_kulturu()
    update_ingilizce()
    update_bilisim()
    print("Batch updates completed.")
