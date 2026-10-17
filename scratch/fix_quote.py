path = r"c:\Users\Kemal ŞİMŞEK\OneDrive\Desktop\MufredatVar\lib\data\subjects\sosyal_bilgiler_data.dart"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix unescaped single quote in Atatürk'ün
content = content.replace("theme: 'Atatürk'ün Ölümü ve Sonrası'", "theme: 'Atatürk\\'ün Ölümü ve Sonrası'")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed single quote escape in sosyal_bilgiler_data.dart successfully.")
