# 📚 MüfredatVar - Türkiye Yüzyılı Maarif Modeli Öğretmen & Müfredat Asistanı

![Flutter](https://img.shields.io/badge/Flutter-3.29%2B-02569B?logo=flutter&logoColor=white)
![Dart](https://img.shields.io/badge/Dart-3.9%2B-0175C2?logo=dart&logoColor=white)
![MEB Maarif Modeli](https://img.shields.io/badge/MEB-Türkiye%20Yüzyılı%20Maarif%20Modeli-E11D48)
![Platform](https://img.shields.io/badge/Platform-Android%20%7C%20iOS%20%7C%20Web-success)
![Lisans](https://img.shields.io/badge/Lisans-MIT-blue)

**MüfredatVar**, Millî Eğitim Bakanlığı (**MEB**) tarafından yürürlüğe konulan **Türkiye Yüzyılı Maarif Modeli**'ne tam uyumlu, ortaokul öğretmenleri ve eğitimciler için geliştirilmiş modern, modüler ve kapsamlı bir müfredat takip ve haftalık ders programı uygulamasıdır.

---

## 🌟 Öne Çıkan Özellikler

### 1. 🇹🇷 Türkiye Yüzyılı Maarif Modeli Tam Uyumu
- **8 Ders Müfredatı:**
  - 📐 **Matematik** (5, 6, 7, 8. Sınıf)
  - 🔬 **Matematik ve Bilim Uygulamaları (Seçmeli)** (5, 6, 7, 8. Sınıf)
  - 📖 **Türkçe** (Dilimizin Zenginlikleri, Bağımsızlık Yolu, 6 Tema)
  - 🧪 **Fen Bilimleri** (Doğa, Madde, Enerji ve Canlılar)
  - 🌍 **Sosyal Bilgiler & T.C. İnkılap Tarihi** (6 Öğrenme Alanı & 7 Maarif Ünitesi)
  - 🇬🇧 **İngilizce** (Beceri ve Tema Odaklı İletişim)
  - 🕌 **Din Kültürü ve Ahlak Bilgisi** (5 Temel Ünite)
  - 💻 **Bilişim Teknolojileri ve Yazılım** (Robotik, Kodlama, Yapay Zekâ)
- **36 Haftalık Akademik Takvim:** 2026-2027 MEB çalışma takvimine göre ara tatiller, yarıyıl ve resmi tatiller dahil gün gün planlanmıştır.
- **Süreç Bileşenleri & Ölçme Değerlendirme:** Her kazanım için süreç bileşenleri, anahtar kavramlar, beceriler, pedagojik notlar ve örnek problem/etkinlikler.

### 2. 👨‍🏫 Çoklu Ders & Sınıf Yönetimi (Öğretmen Dashboard)
- Bir öğretmen aynı anda birden fazla sınıf ve derse girebilir (Örn: Hem 6 hem 7. Sınıf Matematik, hem de Seçmeli Matematik ve Bilim Uygulamaları).
- **Kişiselleştirilmiş Karusel (Carousel):** Girdiğiniz tüm sınıflar ve dersler yatay kart kaydırıcı şeklinde ana sayfada listelenir.
- **Hızlı Özet Izgarası (Grid):** Tek tıkla tüm sınıflarınızın o haftaki kazanımlarını yan yana ızgara olarak görebilirsiniz.
- Tek dokunuşla sınıflar arasında anında geçiş yapma.

### 3. 🗓️ Entegre Haftalık Ders Programı (Timetable)
- Pazartesi - Cuma, 1. dersten 7. derse kadar okul zaman çizelgesi.
- **Günlük ve Haftalık Matris Görünümü:** İster günün derslerini ister haftanın tamamını matris ızgarasında inceleyin.
- **Kazanımlara Doğrudan Erişim:** Ders programındaki herhangi bir derse tıklandığında, doğrudan o dersin **o haftaki güncel öğrenme çıktısına** ve müfredat detayına yönlendirir.
- Hızlı ders ekleme, saat güncelleme, derslik belirleme ve renk özelleştirme.

### 4. 📋 Sınıf Defteri Doldurma Modülü
- E-okul ve sınıf defterine yazılacak haftalık kazanım metnini tek tıkla panoya kopyalama.
- MEB standartlarına tam uyumlu format.

### 5. 📱 Android Ana Ekran Widget'ı (Home Widget)
- Telefonun ana ekranına eklenen şık widget sayesinde uygulamayı açmadan bu haftanın dersini, sınıfını ve kazanım kodunu takip edebilme.

### 6. 🎨 Modern ve Erişilebilir Arayüz
- Tam Koyu (Dark) ve Açık (Light) Tema desteği.
- Akıcı animasyonlar, dokunsal geri bildirim (Haptic Feedback) ve sezgisel tasarım.

---

## 🏗️ Mimari ve Proje Yapısı

```
lib/
├── data/
│   ├── curriculum_repository.dart       # Tüm müfredat verilerini yöneten merkezi depo
│   └── subjects/                       # 8 derse ait 36 haftalık Maarif Modeli verileri
│       ├── matematik_data.dart
│       ├── matematik_bilim_data.dart    # Seçmeli Matematik ve Bilim Uygulamaları
│       ├── turkce_data.dart
│       ├── fen_bilimleri_data.dart
│       ├── sosyal_bilgiler_data.dart
│       ├── ingilizce_data.dart
│       ├── din_kulturu_data.dart
│       └── bilisim_data.dart
├── models/
│   ├── app_settings.dart               # Öğretmen profili ve uygulama ayarları
│   ├── teacher_assignment.dart         # Öğretmenin girdiği çoklu ders/sınıf modeli
│   ├── lesson_entry.dart               # Haftalık ders programı girdisi
│   ├── time_slot.dart                  # Ders saatleri ve teneffüs aralıkları
│   └── curriculum_model.dart           # Hafta, kazanım, ünite ve tema modelleri
├── screens/
│   ├── main_navigation_screen.dart     # 4 sekmeli alt gezinme çubuğu
│   ├── home_screen.dart                # Ana ekran (Karusel, Müfredat Akışı, 36 Hafta Izgarası)
│   ├── timetable_screen.dart           # Haftalık ders programı ve canlı ders takibi
│   ├── subjects_grid_screen.dart       # Tüm dersleri listeleyen keşif ekranı
│   └── settings_screen.dart            # Profil, sınıf ekleme ve tema ayarları
├── services/
│   ├── settings_service.dart           # SharedPreferences ayar kalıcılığı
│   ├── timetable_service.dart          # Ders programı kalıcılığı ve yönetimi
│   └── widget_sync_service.dart        # Android Home Widget köprüsü
└── widgets/
    ├── lesson_edit_dialog.dart         # Ders ekleme / düzenleme iletişim penceresi
    ├── outcome_detail_sheet.dart       # Kazanım detay modalı
    └── widget_preview_card.dart        # Widget önizleme bileşeni
```

---

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler
- Flutter SDK (v3.24 veya üzeri)
- Dart SDK (v3.5 veya üzeri)
- Android SDK (minSdk 21, compileSdk 34)

### Adımlar

1. **Depoyu Klonlayın:**
   ```bash
   git clone https://github.com/kmlsmsk/ders.git
   cd ders
   ```

2. **Bağımlılıkları Yükleyin:**
   ```bash
   flutter pub get
   ```

3. **Testleri Çalıştırın:**
   ```bash
   flutter test
   ```

4. **Uygulamayı Başlatın:**
   ```bash
   flutter run
   ```

5. **Release APK Derleyin:**
   ```bash
   flutter build apk --release
   ```

---

## 📦 Doğrudan APK İndirme

Hazır derlenmiş Android uygulama paketini doğrudan ana klasörden temin edebilirsiniz:
- [**MufredatVar.apk**](./MufredatVar.apk)
- [**MufredatVar-release.apk**](./MufredatVar-release.apk)

---

## 📄 Resmi Kaynaklar & Referanslar
- [MEB Türkiye Yüzyılı Maarif Modeli Resmi Portalı (tymm.meb.gov.tr)](https://tymm.meb.gov.tr)
- [Talim ve Terbiye Kurulu Başkanlığı (mufredat.meb.gov.tr)](https://mufredat.meb.gov.tr)

---

## 👨‍💻 Geliştirici & Lisans
- **Geliştirici:** Kemal Şimşek
- **Lisans:** Bu proje MIT lisansı ile lisanslanmıştır.
