# -*- coding: utf-8 -*-
"""
Comprehensive 36-week generator for Bilişim Teknolojileri ve Yazılım (Grades 5 Maarif, 6, 7, 8).
Generates lib/data/subjects/bilisim_data.dart with full details.
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from curriculum_builder import generate_dart_file

def _make_weeks(raw_units, prefix):
    weeks = []
    for i, u in enumerate(raw_units):
        code = f"{prefix}.{i+1}"
        theme, sub, title, desc, conc, ped, q, a = u
        weeks.append({
            'theme': theme,
            'subTheme': sub,
            'code': code,
            'title': title,
            'description': desc,
            'process': [
                f"a) {desc[:40]} açıklar ve uygular.",
                f"b) {sub} laboratuvar uygulamasını ve algoritmasını tamamlar.",
                "c) Bilişim etiği, güvenliği ve iş birliği ilkelerine riayet eder."
            ],
            'concepts': conc,
            'skills': ['Hesaplamalı Düşünme', 'Algoritmik Tasarım', 'Dijital Okuryazarlık', 'Problem Çözme'],
            'pedagogical': ped,
            'context': 'Bilişim Teknolojileri ve Yazılım',
            'question': q,
            'solution': a,
            'weeklyGoal': f"{title} becerisini bilgisayar laboratuvarında uygulama",
            'evaluation': 'Haftalık uygulama değerlendirme rubriği ve kontrol listesi'
        })
    return weeks

def get_bil_5():
    # 5. Sınıf - Türkiye Yüzyılı Maarif Modeli / Bilişim (Tam 36 Hafta)
    u = [
        # Ünite 1: Bilişim Teknolojileri ve Donanım (1-6)
        ("Bilişim Teknolojileri", "Donanım ve Yazılım Kavramı", "Bilgisayarın Temel Bileşenleri",
         "Donanım (fiziksel parçalar) ve yazılım (programlar) kavramlarını ayırt eder; sistemin çalışma mantığını kavrar.",
         ["Donanım", "Yazılım", "Kasa", "Sistem"],
         "Kasa içi donanım parçaları maket üzerinden incelenir.",
         "Bilgisayarın elle tutulup gözle görülebilen fiziksel parçalarına ne ad verilir?",
         "Donanım (Hardware) adı verilir."),
        
        ("Bilişim Teknolojileri", "İç ve Dış Donanım Birimleri", "Anakart, İşlemci (CPU), RAM ve Sabit Disk",
         "İç donanım parçalarının (CPU, RAM, Hard Disk, Anakart) görevlerini ve bilgisayar hızına etkisini açıklar.",
         ["CPU (İşlemci)", "RAM Bellek", "Sabit Disk (HDD/SSD)", "Anakart"],
         "Bilgisayarın beyni (CPU) ve geçici hafızası (RAM) analojileri kurulur.",
         "Bilgisayarda elektrik kesildiğinde içerisindeki bilgilerin silindiği geçici bellek hangisidir?",
         "RAM Bellek (Geçici Hafıza)."),
        
        ("Bilişim Teknolojileri", "Giriş ve Çıkış Birimleri", "Klavye, Fare, Ekran, Yazıcı ve Hoparlör",
         "Bilgisayara veri giren (klavye, fare, mikrofon) ve bilgi çıkaran (ekran, yazıcı, hoparlör) birimleri sınıflandırır.",
         ["Giriş Birimleri", "Çıkış Birimleri", "Tarayıcı", "Yazıcı"],
         "Donanım kartları kutulama oyunu oynatılır.",
         "Mikrofon ve hoparlör sırasıyla hangi birim türüne girer?",
         "Mikrofon giriş birimi, hoparlör ise ses veren çıkış birimidir."),
        
        ("Bilişim Teknolojileri", "Depolama Araçları ve Kapasite Birimleri", "Bayt, Kilobayt, Megabayt, Gigabayt, Terabayt",
         "Veri depolama kapasitelerini küçükten büyüğe (B, KB, MB, GB, TB) sıralar; USB, SSD ve bulut depolamayı tanır.",
         ["Bayt", "Megabayt", "Gigabayt", "SSD", "Flash Bellek"],
         "1024 kat kuralı ve depolama alanı hesaplama alıştırması yapılır.",
         "1 Gigabayt (GB) kaç Megabayttır (MB)?",
         "1024 Megabayttır (MB)."),
        
        ("Bilişim Teknolojileri", "Ergonomi ve Bilişim Sağlığı", "Doğru Oturuş, Ekran Mesafesi ve Göz Sağlığı",
         "Bilgisayar başında doğru oturma pozisyonunu (90 derece kuralı, 50-70 cm ekran mesafesi) uygular.",
         ["Ergonomi", "Postür", "Göz Sağlığı", "20-20-20 Kuralı"],
         "Sınıfta ergonomik duruş kontrolü ve mola egzersizleri yapılır.",
         "Bilgisayar başında göz yorgunluğunu önleyen '20-20-20 kuralı' nedir?",
         "Her 20 dakikada bir, 20 saniye boyunca, 20 fit (yaklaşık 6 metre) uzağa bakmaktır."),
        
        ("Bilişim Teknolojileri", "Teknolojinin Olumlu ve Olumsuz Etkileri", "Teknoloji Bağımlılığı ve Dijital Denge",
         "Teknolojinin eğitime faydalarını ve kontrolsüz kullanımın yol açtığı asosyallik ve uyku bozukluklarını analiz eder.",
         ["Dijital Denge", "Ekran Süresi", "Faydalar", "Zararlar"],
         "Haftalık ekran süresi takip günlüğü tutturulur.",
         "Kontrolsüz teknoloji kullanımının fiziksel sağlığa en büyük zararı nedir?",
         "Hareketsizlik, duruş bozukluğu (omurga eğriliği) ve uyku kalitesinin düşmesidir."),

        # Ünite 2: Dijital Okuryazarlık ve İletişim (7-10)
        ("Dijital Okuryazarlık", "Bilgisayar Ağları ve İnternet", "Ağ Türleri: LAN ve WAN",
         "İki veya daha fazla bilgisayarın bağlanmasıyla oluşan yerel alan ağı (LAN) ve geniş alan ağını (WAN) kavrar.",
         ["Ağ (Network)", "LAN (Yerel Ağ)", "WAN (Geniş Ağ)", "Modem"],
         "Okul bilişim sınıfı yerel ağı şematik olarak çizdirilir.",
         "Bilişim sınıfındaki bilgisayarların birbirine bağlı olduğu ağ türü hangisidir?",
         "Yerel Alan Ağı (LAN - Local Area Network)."),
        
        ("Dijital Okuryazarlık", "İnternet Adresleri ve Uzantılar", "URL, Domain, .gov, .edu, .org, .k12.tr",
         "Web adreslerinin yapısını ve resmi kurum (.gov), eğitim (.edu, .k12) uzantılarının güvenilirliğini inceler.",
         ["URL", "Domain", ".gov.tr", ".k12.tr", ".edu.tr"],
         "Sahte ve güvenilir web siteleri adres çubuğundan analiz edilir.",
         "Türkiye'deki resmi devlet kurumlarına ait siteler hangi uzantıyla biter?",
         ".gov.tr uzantısıyla biter."),
        
        ("Ara Tatil", "1. Dönem Ara Tatil Tekrarı", "Bilişim ve Donanım Kampı",
         "Donanım, ağlar ve ergonomi konularını içeren interaktif bulmaca ve test çözer.",
         ["Ara Tatil", "Kamp", "Tekrar", "Pekiştirme"],
         "Kahoot / interaktif bilgi yarışması düzenlenir.",
         "İşlemcinin üzerindeki soğutucu fanın görevi nedir?",
         "İşlemcinin aşırı ısınıp yanmasını veya yavaşlamasını önlemektir."),
        
        ("Dijital Okuryazarlık", "Arama Motorları ve Bilgiye Ulaşma", "Doğru Arama Teknikleri ve Tırnak İşareti Kullanımı",
         "Arama motorlarında anahtar kelimeleri doğru seçmeyi, tırnak (\" \") ve eksi (-) işaretleriyle aramayı daraltmayı öğrenir.",
         ["Arama Motoru", "Anahtar Kelime", "Filtreleme", "Google/Yandex"],
         "Laboratuvarda hedef bilgiyi en hızlı bulma dedektiflik oyunu oynanır.",
         "Arama motorunda bir ifadeyi kelimesi kelimesine tam aratmak için ne yapılır?",
         "İfade çift tırnak içerisine alınır (örneğin: \"Türkiye Yüzyılı Maarif Modeli\")."),

        # Ünite 3: Bilişim Etiği ve Siber Güvenlik (11-15)
        ("Bilişim Etiği ve Güvenlik", "Bilişim Etiği ve Telif Hakları", "Telif Hakkı, Korsan Yazılım ve Lisans Türleri",
         "Fikir ve Sanat Eserleri Kanunu kapsamında telif hakkının önemini, intihal yapmamanın ahlaki değerini kavrar.",
         ["Telif Hakkı", "İntihal", "Korsan Yazılım", "Creative Commons"],
         "Korsan yazılımın virüs bulaştırma riskleri incelenir.",
         "İnternetten bulunan bir resmi veya yazıyı ödevde kullanırken ne yapılmalıdır?",
         "Eser sahibinden izin alınmalı veya kaynağı açıkça (kaynakça) belirtilmelidir."),
        
        ("Bilişim Etiği ve Güvenlik", "Dijital Yurttaşlık ve Ayak İzi", "Dijital Ayak İzi, E-Devlet ve Dijital Miras",
         "İnternette paylaşılan hiçbir şeyin tamamen silinmediğini; gelecekte karşımıza çıkabileceğini kavrar.",
         ["Dijital Ayak İzi", "E-Devlet", "Sanal İtibar", "Gizlilik"],
         "Sosyal medya gizlilik ayarları uygulamalı kontrol edilir.",
         "Dijital ayak izi ne anlama gelir?",
         "İnternette gezinirken, paylaşım yaparken veya giriş yaparken arkamızda bıraktığımız tüm kalıcı veri izleridir."),
        
        ("Bilişim Etiği ve Güvenlik", "Siber Zorbalık ve Başa Çıkma", "Zorbalığa Sessiz Kalma: Engelle, Kaydet, Bildir",
         "Siber zorbalığın tanımını, zorbalıkla karşılaşıldığında aileye söyleme ve Bilgi İhbar hattını (İhbarWeb) öğrenir.",
         ["Siber Zorbalık", "Ekran Görüntüsü", "İhbarWeb", "Engelleme"],
         "Örnek senaryo üzerinden kriz yönetimi ve zorbalığa tepki canlandırılır.",
         "İnternette biri sizi tehdit ettiğinde veya hakaret ettiğinde yapmanız gereken ilk üç adım nedir?",
         "1. Cevap vermemek, 2. Kanıt için ekran görüntüsü almak, 3. Güvenilir bir yetişkine (ebeveyn/öğretmen) haber vermek."),
        
        ("Bilişim Etiği ve Güvenlik", "Güçlü Parola Oluşturma", "Şifre Güvenliği ve İki Adımlı Doğrulama",
         "Büyük/küçük harf, rakam ve sembol içeren en az 8-12 karakterli kırılması imkansız parola üretir.",
         ["Güçlü Parola", "Büyük Harf", "Sembol", "2FA Doğrulama"],
         "Sınıfta parola güvenlik testi simülatörü çalıştırılır.",
         "Hangisi daha güçlü bir paroladır: '12345678' mi, yoksa 'M?fr3dat!2026' mı?",
         "'M?fr3dat!2026' parolası harf, rakam ve özel sembol içerdiği için çok güçlüdür."),
        
        ("Bilişim Etiği ve Güvenlik", "Zararlı Yazılımlar ve Antivirüs", "Virüs, Truva Atı (Trojan), Solucan ve Fidye Yazılımı",
         "Zararlı yazılım türlerini tanır; antivirüs programı kullanmanın ve şüpheli linklere tıklamamanın önemini açıklar.",
         ["Virüs", "Truva Atı", "Solucan", "Fidye Yazılımı (Ransomware)", "Antivirüs"],
         "Oltalama (phishing) e-postalarını tanıma çalışması yapılır.",
         "Kullanıcıya faydalı bir oyun veya program gibi görünüp arka planda sisteme sızan virüse ne ad verilir?",
         "Truva Atı (Trojan Horse)."),

        # Ünite 4: İletişim ve Üretim Araçları (16-19)
        ("İletişim ve Üretim", "Bulut Depolama ve E-Posta", "Google Drive, OneDrive, E-Posta Etiketi",
         "Bulut depolama servislerinde dosya yedeklemeyi, paylaşmayı ve resmi e-posta yazma kurallarını uygular.",
         ["Bulut Depolama", "Drive", "E-Posta", "Konu Başlığı", "Nezaket"],
         "Öğretmene ödev teslim eden örnek saygılı e-posta yazılır.",
         "Resmi bir e-postada 'Konu' bölümü neden boş bırakılmamalıdır?",
         "Alıcının iletinin içeriğini ve aciliyetini hızlıca anlayabilmesi ve spam olarak algılanmaması içindir."),
        
        ("İletişim ve Üretim", "Kelime İşlemci Temelleri", "Yazı Biçimlendirme, Hizalama ve Yazı Tipi",
         "Kelime işlemci (Word/Writer) programında metin yazar, kalın/italik yapar, renk ve boyut değiştirir.",
         ["Kelime İşlemci", "Yazı Tipi", "Hizalama", "Satır Aralığı"],
         "Öğrenciler İstiklal Marşı'mızı biçimlendirerek belge hazırlar.",
         "Bir metni sayfanın tam ortasına yerleştirmek için hangi hizalama düğmesi kullanılır?",
         "'Ortala' (Ctrl + R veya hizalama simgesi) düğmesi kullanılır."),
        
        ("İletişim ve Üretim", "1. Dönem Sonu Sentezi", "1. Dönem Bilişim Yetkinlik Değerlendirmesi",
         "Donanım, ağlar, güvenlik ve kelime işlemci konularını kapsayan uygulama sınavı yapar.",
         ["Sentez", "Laboratuvar Sınavı", "Uygulama", "Ölçme"],
         "Bilgisayar başında 5 soruluk pratik görev tamamlatılır.",
         "Kaydedilmemiş bir belgenin elektrik kesintisinde kaybolmaması için hangi klavye kısayolu sık sık kullanılır?",
         "Ctrl + S (Kaydet) kısayolu kullanılır."),
        
        ("İletişim ve Üretim", "1. Dönem Sonu Karnesi", "Yarıyıl Tatili Dijital Üretkenlik Planı",
         "Tatil boyunca tüketici olmak yerine kodlama ve dijital tasarımla üretici olma hedefleri belirler.",
         ["Karne", "Dijital Üretim", "Kodlama Hedefi", "Gelişim"],
         "Blok kodlama siteleri (Code.org) tatil ödevleri verilir.",
         "Teknoloji tüketicisi olmak ile üreticisi olmak arasındaki fark nedir?",
         "Sadece oyun oynamak tüketimdir; kendi oyununu veya web sitesini tasarlamak ise üretimdir."),

        # Ünite 5: Kelime İşlemci ve Görsel Tasarım (20-22)
        ("Görsel Tasarım", "Belgeye Resim ve Tablo Ekleme", "Görsel Düzenleme, Tablo Tasarımı ve Kenarlıklar",
         "Kelime işlemciye fotoğraf ve tablo ekler; sütun ve satırları biçimlendirir.",
         ["Tablo", "Satır", "Sütun", "Resim Ekleme"],
         "Haftalık ders programı tablosu tasarlanır ve renklendirilir.",
         "Bir tabloda yatay çizgiler arasında kalan bölüme ne ad verilir?",
         "Satır adı verilir (dikey olanlara ise sütun denir)."),
        
        ("Görsel Tasarım", "Afiş ve Broşür Tasarımı", "Canva / Bilişim Araçlarıyla Dijital Afiş",
         "Belirlenen bir sosyal sorumluluk konusu için (sıfır atık, siber güvenlik) afiş tasarlar.",
         ["Afiş Tasarımı", "Tipografi", "Renk Uyumu", "Görsel Hiyerarşi"],
         "Okul panosu için 'Siber Güvenlik Afişleri' yarışması düzenlenir.",
         "Etkili bir afişte yazıların okunabilirliği için neye dikkat edilmelidir?",
         "Arka plan ile yazı rengi arasında yüksek kontrast (zıtlık) bulunmalıdır."),
        
        ("Görsel Tasarım", "Sayfa Düzeni ve Yazdırma Ayarları", "Kenar Boşlukları, Yönlendirme (Yatay/Dikey) ve PDF Kaydetme",
         "Sayfa yapısını dikey veya yatay yapar, kenar boşluklarını ayarlar ve belgeyi PDF olarak dışa aktarır.",
         ["Sayfa Yapısı", "Yatay/Dikey", "PDF", "Baskı Önizleme"],
         "Yazıcıdan çıktı almadan önce baskı önizleme kontrolü yapılır.",
         "Belgenin farklı cihazlarda bozulmadan açılması için hangi formatta kaydedilmesi önerilir?",
         "PDF formatında kaydedilmesi önerilir."),

        # Ünite 6: Problem Çözme ve Algoritma (23-27)
        ("Problem Çözme ve Algoritma", "Problem Nedir? Problem Çözme Adımları", "Problemi Anlama, Plan Yapma, Çözme ve Değerlendirme",
         "Günlük hayattaki problemleri analiz eder; George Polya'nın 4 adımlı problem çözme stratejisini öğrenir.",
         ["Problem Çözme", "Analiz", "Plan", "Çözüm Adımları"],
         "Labirent bulmacaları ve mantık soruları çözülür.",
         "Problem çözme sürecinin ilk ve en kritik adımı nedir?",
         "Problemi doğru ve eksiksiz olarak anlamaktır."),
        
        ("Problem Çözme ve Algoritma", "Algoritma Kavramı ve Özellikleri", "Adım Adım Yol Haritası ve Açıklık",
         "Bir algoritmanın başlangıcı, sonu ve sırası belli net adımlardan oluştuğunu kavrar.",
         ["Algoritma", "Başla - Bitir", "Sıralama", "Netlik"],
         "Ayran yapma ve çay demleme algoritmaları tahtaya yazdırılır.",
         "Bir algoritmanın adımları neden belirsiz veya yoruma açık olmamalıdır?",
         "Çünkü bilgisayarlar kesin emirlerle çalışır; belirsizlik durumunda hata (bug) verir."),
        
        ("Problem Çözme ve Algoritma", "Akış Şemaları (Flowcharts)", "Elips, Dikdörtgen, Eşkenar Dörtgen, Paralelkenar",
         "Akış şeması sembollerini (Elips: Başla/Bitir, Dikdörtgen: İşlem, Eşkenar Dörtgen: Karar) görevleriyle tanır.",
         ["Akış Şeması", "Karar (Eşkenar Dörtgen)", "İşlem", "Girdi/Çıktı"],
         "Hava yağmurlu mu? Karar mekanizması akış şeması çizilir.",
         "Akış şemasında 'Hava yağmurlu mu? (Evet/Hayır)' gibi bir koşul hangi geometrik şekille gösterilir?",
         "Eşkenar Dörtgen (Baklava Dilimi) ile gösterilir."),
        
        ("Ara Tatil", "2. Dönem Ara Tatil Tekrarı", "Algoritma ve Mantık Kampı",
         "Akış şeması ve mantıksal karar yapıları üzerine 20 soru çözer.",
         ["Ara Tatil", "Mantık", "Akış Şeması", "Kamp"],
         "Kağıt üzerinde kod çalıştırma (kuru çalışma) yapılır.",
         "Akış şemasında 'Başla' ve 'Bitir' komutları hangi şekille çizilir?",
         "Elips (Oval) şekliyle çizilir."),
        
        ("Problem Çözme ve Algoritma", "Hata Ayıklama (Debugging)", "Hatalı Adımları Bulma ve Düzeltme",
         "Bir algoritmada istenen sonucu vermeyen hatalı mantık veya sıralama adımlarını tespit edip düzeltir.",
         ["Hata Ayıklama (Debug)", "Bug", "Mantık Hatası", "Düzeltme"],
         "Hatalı sıralanmış algoritma kartlarını doğru sıraya dizme etkinliği.",
         "Yazılım dünyasında kodlardaki hataları bulup temizleme işlemine ne ad verilir?",
         "Debugging (Hata Ayıklama)."),

        # Ünite 7: Blok Tabanlı Kodlama Temelleri (28-36)
        ("Blok Tabanlı Kodlama", "Blok Kodlama Ortamı (Code.org / Scratch)", "Sahne, Kukla ve Kod Blokları Arayüzü",
         "Blok tabanlı kodlama arayüzünü tanır; sahneye kukla ve dekor ekler.",
         ["Scratch", "Kukla (Sprite)", "Sahne (Backdrop)", "Bloklar"],
         "Scratch arayüzünde kedi kuklasını farklı kostümlere büründürür.",
         "Scratch programında ekranda hareket eden veya komut alan karakterlere ne ad verilir?",
         "Kukla (Sprite) adı verilir."),
        
        ("Blok Tabanlı Kodlama", "Olaylar ve Hareket Blokları", "Yeşil Bayrağa Tıklandığında ve X/Y Koordinatları",
         "Yeşil bayrak bloğu ile programı başlatır; kuklayı sağa, sola ve belirli koordinatlara hareket ettirir.",
         ["Olaylar", "Yeşil Bayrak", "X Koordinatı", "Y Koordinatı", "Hareket"],
         "Klavye yön tuşlarıyla hareket eden labirent oyunu kuklası kodlanır.",
         "Scratch sahnesinde yatay eksene hangi harf verilir?",
         "X ekseni (dikey olan ise Y eksenidir)."),
        
        ("Blok Tabanlı Kodlama", "Görünüm ve Ses Blokları", "Konuşma Balonları, Kostüm Değiştirme ve Müzik",
         "Kuklanın konuşmasını sağlar; sonraki kostüm bloğuyla yürüme animasyonu oluşturur.",
         ["Görünüm", "Konuşma Balonu", "Kostüm Değiştir", "Ses Efekti"],
         "Kuklaların birbirine selam verip tanıştığı animasyon diyaloğu kodlanır.",
         "Bir kuklanın yürüyormuş gibi görünmesi için hangi blok sürekli tekrarlanmalıdır?",
         "'Sonraki kostüme geç' bloğu araya bekleme süresi konularak tekrarlanmalıdır."),
        
        ("Blok Tabanlı Kodlama", "Döngü Blokları (Kontrol)", "10 Defa Tekrarla ve Sürekli Tekrarla",
         "Kodların tekrar tekrar çalışması için döngü bloklarını amacına uygun kullanır.",
         ["Döngü (Loop)", "Sürekli Tekrarla", "10 Defa Tekrarla", "Kontrol"],
         "Sürekli dönen pervane ve zıplayan top simülasyonu kodlanır.",
         "Oyun boyunca arka planda müziğin hiç durmadan çalması için hangi döngü bloğu kullanılır?",
         "'Sürekli Tekrarla' (Forever) bloğu kullanılır."),
        
        ("Blok Tabanlı Kodlama", "Şart / Karar Blokları (Eğer - İse)", "Koşula Bağlı Davranışlar",
         "Eğer ... ise (If - Then) bloğu ile kuklanın belirli bir duruma göre tepki vermesini sağlar.",
         ["Eğer - İse (If-Else)", "Koşul", "Karar Mekanizması", "Algılama"],
         "Kukla kırmızı renge değerse oyunu bitiren engel kodu yazılır.",
         "'Eğer kenara geldiyse sektir' komutu ne işe yarar?",
         "Kukla sahne sınırlarına ulaştığında dışarı çıkmayıp geri dönmesini sağlar."),
        
        ("Blok Tabanlı Kodlama", "Algılama Blokları ve Etkileşim", "Fareye Dokunuyor mu? Tuşa Basıldı mı?",
         "Kuklanın fare imlecini takip etmesini veya belirli bir nesneye değip değmediğini algılatır.",
         ["Algılama", "Fare İmleci", "Renge Dokunma", "Etkileşim"],
         "Yıldızları toplayan balık oyunu kodlaması yapılır.",
         "Bir kuklanın klavyeden 'Boşluk' tuşuna basıldığında zıplaması için hangi bloklar birleştirilir?",
         "'Boşluk tuşuna basıldı mı?' algılama bloğu 'Eğer' kontrol bloğunun içine yerleştirilir."),
        
        ("Blok Tabanlı Kodlama", "Değişkenler ve Puan Mekanizması", "Skor Tutma ve Can Azaltma",
         "Değişken tanımlar (Skor, Can, Süre); elma topladıkça skoru 1 artıran kod yazar.",
         ["Değişken (Variable)", "Skor", "Can Puanı", "Veri Saklama"],
         "Zamana karşı yarışan meyve yakalama oyunu kodlanır.",
         "Oyunda oyuncunun topladığı puanı saklayıp artıran bilişim kavramı nedir?",
         "Değişken (Variable)."),
        
        ("Blok Tabanlı Kodlama", "Oyun Tasarımı ve Proje Geliştirme", "Labirent veya Kaçış Oyunu Kodlama",
         "Öğrenilen tüm blokları (olay, hareket, döngü, eğer, değişken) birleştirerek tam teşekküllü oyun üretir.",
         ["Proje Tasarımı", "Oyun Geliştirme", "Seviye", "Bitiş Ekranı"],
         "Öğrenciler kendi hayal ettikleri eğitici oyunu kodlayıp arkadaşlarına oynatır.",
         "Bir oyun projesinde 'Tebrikler Kazandınız!' ekranı ne zaman tetiklenmelidir?",
         "Skor değişkeni hedeflenen puana (örneğin 10 puana) ulaştığında tetiklenmelidir."),
        
        ("Blok Tabanlı Kodlama", "Maarif Modeli Bilişim Yıl Sonu Şenliği", "5. Sınıf Kodlama ve Tasarım Sergisi",
         "Öğrenciler yıl boyu geliştirdikleri Scratch projelerini ve dijital afişlerini okulla paylaşır.",
         ["Portfolyo Sergisi", "Maarif Modeli", "Dijital Sergi", "Girişimcilik"],
         "Okul çapında 'Genç Yazılımcılar Kodlama Sergisi' düzenlenir.",
         "Bilişim Teknolojileri ve Yazılım dersinin öğrencilere kazandırdığı en büyük güç nedir?",
         "Sadece teknolojiyi kullanan değil, hayal gücünü algoritmalarla koda dönüştürüp üreten yenilikçi zihinler olmaktır.")
    ]
    assert len(u) == 36, f"Bil 5 count: {len(u)}"
    return {
        'title': '5. Sınıf',
        'subtitle': 'Türkiye Yüzyılı Maarif Modeli (Donanım, Güvenlik & Kodlama)',
        'badge': 'Maarif Modeli ✨',
        'weeks': _make_weeks(u, 'BİL.5')
    }

def get_bil_6():
    # 6. Sınıf MEB Bilişim (İşletim Sistemleri, Tablolama & Blok Kodlama - 36 Hafta)
    u = [
        # Ünite 1: İşletim Sistemleri ve Açık Kaynak (1-5)
        ("İşletim Sistemleri", "İşletim Sistemi Nedir?", "Donanım ile Yazılım Arasındaki Köprü",
         "İşletim sisteminin donanım kaynaklarını yöneten ana yazılım olduğunu kavrar.",
         ["İşletim Sistemi (OS)", "Sistem Yazılımı", "Arayüz", "Kaynak Yönetimi"],
         "İşletim sistemi olmadan bilgisayarın çalışamayacağı analojisi kurulur.",
         "Bilgisayar açılırken belleğe yüklenen ve tüm donanımı yöneten temel sistem yazılımı nedir?",
         "İşletim Sistemi (Operating System)."),
        
        ("İşletim Sistemleri", "İşletim Sistemi Çeşitleri", "Windows, MacOS, Linux, Pardus, Android, iOS",
         "Masaüstü ve mobil işletim sistemlerini ayırt eder.",
         ["Masaüstü OS", "Mobil OS", "Android", "Pardus", "Linux"],
         "Akıllı telefon ve bilgisayar işletim sistemleri karşılaştırılır.",
         "Akıllı telefon ve tabletlerde en yaygın kullanılan mobil işletim sistemleri hangileridir?",
         "Android ve iOS."),
        
        ("İşletim Sistemleri", "Açık Kaynak Kod ve Millî Gururumuz: PARDUS", "Özgür Yazılım, PARDUS ve Güvenlik",
         "Açık kaynak kodlu yazılımların bağımsızlık, milli güvenlik ve maliyet avantajlarını inceler.",
         ["Pardus", "TÜBİTAK", "Açık Kaynak", "Özgür Yazılım", "Linux"],
         "Pardus masaüstü ortamı ve TÜBİTAK'ın geliştirdiği milli yazılımlar tanıtılır.",
         "TÜBİTAK tarafından kamu kurumları ve okullar için geliştirilen millî işletim sistemimiz nedir?",
         "PARDUS."),
        
        ("İşletim Sistemleri", "Dosya ve Klasör Yönetimi", "Dosya Adı, Nokta ve Dosya Uzantısı",
         "Dosyaların isim ve uzantı kısımlarını (.txt, .docx, .xlsx, .pptx, .jpg, .mp3, .mp4, .pdf) tanır.",
         ["Dosya Uzantısı", "Hiyerarşi", "Klasör Ağacı", ".pdf", ".docx"],
         "Dosya uzantıları eşleştirme kartları etkinliği.",
         "Bir belgenin 'resim', 'ses' veya 'yazı' olduğunu dosya adındaki hangi kısımdan anlarız?",
         "Noktadan sonraki 3-4 harfli dosya uzantısından (örneğin .jpg, .mp3, .docx) anlarız."),
        
        ("İşletim Sistemleri", "Dosya Sıkıştırma ve Arşivleme", "ZIP ve RAR Dosyaları, Boyut Küçültme",
         "Büyük dosyaları arşivleyip boyutlarını küçülterek e-posta ile göndermeyi uygular.",
         ["Sıkıştırma", "ZIP", "RAR", "Arşiv", "Boyut Tasarrufu"],
         "Çok sayıda fotoğraf sıkıştırılarak tek bir zip klasöründe toplanır.",
         "Büyük boyutlu birden fazla dosyayı tek bir paket haline getirip boyutunu küçültmeye ne denir?",
         "Dosya sıkıştırma (ZIP/RAR)."),

        # Ünite 2: Bilişim Ağı ve Siber Dünya (6-9)
        ("Bilişim Ağı", "Ağ Cihazları ve İletişim", "Modem, Dağıtıcı (Switch), Yönlendirici (Router)",
         "Ağ bileşenlerini tanır; modemin sinyalleri dönüştürme ve router'ın yönlendirme görevini kavrar.",
         ["Modem", "Switch (Dağıtıcı)", "Router (Yönlendirici)", "Ethernet"],
         "Sınıftaki modem ve ağ kabloları yerinde incelenir.",
         "İnternet servis sağlayıcıdan gelen sinyalleri bilgisayarların anlayacağı dijital verilere çeviren cihaz nedir?",
         "Modem."),
        
        ("Bilişim Ağı", "IP Adresi ve DNS", "İnternetin Kimlik Kartı: IP ve Alan Adı Sistemi",
         "İnternete bağlı her cihazın benzersiz bir IP adresi olduğunu; DNS'in IP'yi alan adına çevirdiğini öğrenir.",
         ["IP Adresi", "DNS", "Benzersiz Kimlik", "Ağ Protokolü"],
         "Komut satırından (CMD) 'ping' ve 'ipconfig' komutları incelenir.",
         "İnternete bağlı her bilgisayarın dünyada tek olan dijital kimlik numarasına ne ad verilir?",
         "IP Adresi (Internet Protocol Address)."),
        
        ("Bilişim Ağı", "Güvenli Web ve HTTPS Protokolü", "SSL Sertifikası, Kilit Simgesi ve Veri Şifreleme",
         "Web sitelerinde HTTP ile HTTPS arasındaki farkı; şifreli veri iletiminin bankacılıktaki yerini kavrar.",
         ["HTTPS", "SSL Sertifikası", "Kilit Simgesi", "Şifreleme"],
         "Alışveriş sitelerindeki güvenli kilit simgesi kontrol edilir.",
         "Bir web sitesinin adresinde https:// ve yeşil kilit simgesi olması ne anlama gelir?",
         "Kullanıcı ile site arasındaki veri alışverişinin şifrelenerek güvenceye alındığı anlamına gelir."),
        
        ("Ara Tatil", "1. Dönem Ara Tatil Tekrarı", "İşletim Sistemleri ve Ağlar Kampı",
         "Dosya uzantıları, Pardus ve ağ cihazları üzerine pekiştirme soruları çözer.",
         ["Ara Tatil", "Pekiştirme", "Ağlar", "Test"],
         "Uygulama testleri ve kavram haritaları çözülür.",
         "Bir müzik dosyasının uzantısı genellikle ne olur?",
         ".mp3 veya .wav olur."),

        # Ünite 3: Tablolama Yazılımları (Excel / Calc) (10-15)
        ("Tablolama Yazılımları", "Tablolama Mantığı ve Hücre Kavramı", "Satır (Sayılar), Sütun (Harfler) ve Hücre Adresi (A1, B3)",
         "Elektronik tablolama yazılımının (Excel/Calc) arayüzünü ve hücre adresi mantığını öğrenir.",
         ["Tablolama", "Excel/Calc", "Hücre (Cell)", "Satır ve Sütun"],
         "Bilişim sınıfında satranç tahtası gibi hücre bulmaca oyunu oynanır.",
         "B sütunu ile 5. satırın kesiştiği hücrenin adresi nedir?",
         "B5 hücresidir."),
        
        ("Tablolama Yazılımları", "Veri Girişi ve Otomatik Doldurma", "Metin, Sayı ve Tarih Girişi, Doldurma Tutamacı",
         "Hücrelere veri girer; gün, ay ve sayı serilerini otomatik doldurma tutamacıyla hızlıca çoğaltır.",
         ["Veri Girişi", "Doldurma Tutamacı", "Seri Çoğaltma", "Hücre Biçimlendirme"],
         "1'den 100'e kadar sayılar ve haftanın günleri tek hareketle yazdırılır.",
         "Hücrenin sağ alt köşesindeki minik kare noktaya ne ad verilir?",
         "Doldurma tutamacı (Fill handle)."),
        
        ("Tablolama Yazılımları", "Temel Matematiksel Formüller", "Eşittir (=) İşareti, Toplama, Çıkarma, Çarpma, Bölme",
         "Tüm formüllerin eşittir (=) ile başladığını öğrenir; iki hücreyi birbiriyle toplar ve çarpar.",
         ["Formül", "Eşittir (=)", "Toplama (+)", "Çarpma (*)", "Bölme (/)"],
         "Bakkal alışveriş listesi ve tutar hesaplama tablosu kodlanır.",
         "Excel'de formül yazmaya başlarken mutlaka hangi işaret konulmalıdır?",
         "Eşittir (=) işareti konulmalıdır."),
        
        ("Tablolama Yazılımları", "Hazır Fonksiyonlar: TOPLA ve ORTALAMA", "=TOPLA(A1:A10) ve =ORTALAMA(B1:B5)",
         "Aralık belirten iki nokta (:) kullanarak yüzlerce sayıyı tek satırda toplayıp ortalamasını alır.",
         ["TOPLA", "ORTALAMA", "Aralık (:)", "Fonksiyon"],
         "Sınıfın yazılı notlarının ortalamasını hesaplayan karne çizelgesi yapılır.",
         "A1'den A10'a kadar olan tüm hücreleri toplamak için hangi fonksiyon yazılır?",
         "`=TOPLA(A1:A10)` formülü yazılır."),
        
        ("Tablolama Yazılımları", "Koşullu Fonksiyon: EĞER Fonksiyonu", "=EĞER(Not>=50; \"Geçti\"; \"Kaldı\")",
         "Mantıksal şartlara göre sonuç üreten EĞER formülünü not çizelgesine uygular.",
         ["EĞER (IF)", "Koşul", "Geçti/Kaldı", "Mantıksal Sınama"],
         "Öğrenci not ortalamasına göre 'Geçti' veya 'Kaldı' yazdıran otomasyon kurulur.",
         "`=EĞER(C2>=50; \"Başarılı\"; \"Başarısız\")` formülünde C2 hücresi 65 ise ekranda ne yazar?",
         "'Başarılı' yazar."),
        
        ("Tablolama Yazılımları", "Verileri Görselleştirme: Grafikler", "Sütun, Çizgi ve Pasta Grafiği Oluşturma",
         "Tablodaki sayısal verileri renkli sütun ve pasta grafiklerine dönüştürerek raporlar.",
         ["Grafik", "Sütun Grafiği", "Pasta Grafiği", "Veri Analizi"],
         "Türkiye'nin bölgelere göre yağış miktarı pasta grafiği çizdirilir.",
         "Bütçe paylarını veya bir bütünün yüzdelik parçalarını göstermek için en uygun grafik türü hangisidir?",
         "Pasta (Daire) Grafiğidir."),

        # Ünite 4: Dijital Sunu ve Multimedya (16-19)
        ("Dijital Sunu", "Etkili Sunum Teknikleri", "PowerPoint / Impress ile Slayt Tasarımı",
         "Slaytlarda az yazı, bol görsel, zıt renkler ve 6x6 kuralını uygulayarak profesyonel sunu hazırlar.",
         ["Sunum", "Slayt", "Görsel Tasarım", "6x6 Kuralı"],
         "Öğrenciler kendi memleketlerini anlatan 5 slaytlık mini sunu hazırlar.",
         "Sunum tasarımında '6x6 kuralı' ne anlama gelir?",
         "Bir slaytta en fazla 6 satır ve her satırda en fazla 6 kelime bulunması tavsiyesidir."),
        
        ("Dijital Sunu", "Geçişler ve Animasyonlar", "Slayt Geçiş Efektleri ve Nesne Animasyonları",
         "Slayt geçişi ile nesne animasyonunu ayırt eder; dikkat dağıtmayacak sade efektler seçer.",
         ["Animasyon", "Geçiş Efekti", "Zamanlama", "Multimedya"],
         "Gezegenlerin güneş etrafında sırayla belirdiği animasyonlu slayt yapılır.",
         "Tüm slayt sayfası değişirken oynayan efekte ne ad verilir?",
         "Slayt Geçişi (Transition) adı verilir."),
        
        ("Dijital Sunu", "1. Dönem Sonu Sentezi", "1. Dönem Bilişim ve Tablolama Projesi",
         "İşletim sistemleri, ağlar, Excel formülleri ve sunum konularından proje değerlendirmesi yapar.",
         ["Sentez", "Excel Projesi", "Not Çizelgesi", "Ölçme"],
         "Öğrenciler kendi mini bütçe hesap tablosunu hazırlar.",
         "Excel'de en yüksek ve en düşük değeri bulan hazır fonksiyonlar nelerdir?",
         "`=MAK()` (Maksimum) ve `=MİN()` (Minimum) fonksiyonlarıdır."),
        
        ("Dijital Sunu", "1. Dönem Sonu Karnesi", "Yarıyıl Tatili Scratch Oyun Fikirleri",
         "2. dönem başlayacak ileri düzey oyun kodlama için hikaye ve karakter senaryosu yazar.",
         ["Karne", "Senaryo", "Oyun Tasarımı", "Yarıyıl Tatili"],
         "Öğrenciler kendi oyun senaryo taslağını oluşturur.",
         "Bir oyun kodlamaya başlamadan önce yapılan karakter, kurallar ve hikaye planına ne denir?",
         "Oyun Tasarım Belgesi (Game Design Document)."),

        # Ünite 5: İleri Algoritmik Düşünme (20-22)
        ("Algoritmik Düşünme", "Karmaşık Problemleri Parçalara Ayırma (Dekompozisyon)", "Büyük Problemi Küçük Alt Parçalara Bölme",
         "Büyük ve zor bir problemi yönetilebilir küçük alt parçalara (fonksiyonlara) ayırmayı modeller.",
         ["Dekompozisyon", "Parçalama", "Hesaplamalı Düşünme", "Strateji"],
         "Akıllı ev sisteminin alt modüllere (ışık, ısı, güvenlik) bölünmesi incelenir.",
         "Karmaşık bir yazılım projesini parçalara ayırarak çözmenin yazılımcıya faydası nedir?",
         "Problemin anlaşılmasını ve çözülmesini kolaylaştırır; ekip üyeleri arasında iş bölümü sağlar."),
        
        ("Algoritmik Düşünme", "Kalıp Tanıma ve Soyutlama", "Benzerlikleri Bulma ve Gereksiz Ayrıntıları Eleme",
         "Farklı problemler arasındaki ortak döngüleri bulur; çözüme etkisi olmayan detayları ayıklar.",
         ["Kalıp Tanıma", "Soyutlama (Abstraction)", "Örüntü", "Sadeleştirme"],
         "Trafik ışıkları ve asansör sisteminin ortak durum makineleri analiz edilir.",
         "Problem çözümünde sadece önemli noktalara odaklanıp gereksiz detayları görmezden gelmeye ne denir?",
         "Soyutlama (Abstraction)."),
        
        ("Algoritmik Düşünme", "İç İçe Karar Yapıları ve Döngüler", "Akış Şemalarında Çift Koşullar",
         "Birden fazla şartın aynı anda sağlanması durumunu (VE / VEYA mantığı) akış şemasında modeller.",
         ["VE Mantığı", "VEYA Mantığı", "İç İçe Koşul", "Akış Şeması"],
         "Kullanıcı adı VE şifre doğru mu? doğrulama şeması çizilir.",
         "Bir sistemde girişin başarılı olması için hem kullanıcı adının hem de şifrenin doğru olması hangi mantık operatörüdür?",
         "'VE' (AND) mantık operatörüdür."),

        # Ünite 6: Scratch ile Blok Tabanlı Oyun Programlama (23-28)
        ("Scratch Oyun Programlama", "Scratch ile İleri Koordinat ve Hareket", "Fizik Kuralları, Sekme ve Yön Açısı",
         "Açı değerleri (0: Yukarı, 90: Sağ, 180: Aşağı, -90: Sol) ile kuklanın baktığı yönü kontrol eder.",
         ["Yön Açısı", "Açı (0-360)", "Sekme Açısı", "Fizik Hareketi"],
         "Pong (Masa Tenisi) oyunu top sekme kodları yazılır.",
         "Scratch programında sağa doğru bakan bir kuklanın yön açısı kaç derecedir?",
         "90 derecedir."),
        
        ("Scratch Oyun Programlama", "Haber Salma ve Karşılama Blokları", "Kuklalar Arası Mesajlaşma (Broadcast)",
         "'Haberini sal' ve 'haberi aldığımda' bloklarıyla kuklaların birbiriyle eşzamanlı iletişim kurmasını sağlar.",
         ["Haber Sal (Broadcast)", "Haber Aldığımda", "Kukla İletişimi", "Eşzamanlılık"],
         "Butona basıldığında kapının açılması ve müziğin başlaması senkronize edilir.",
         "Scratch'te bir kukladaki olayın diğer tüm kuklaları tetiklemesini sağlayan blok hangisidir?",
         "'... haberini sal' (Broadcast) bloğudur."),
        
        ("Scratch Oyun Programlama", "Kendi Bloklarını Yap (Fonksiyonlar)", "Kod Tekrarını Önleme ve Modüler Bloklar",
         "Scratch'te 'Bir Blok Oluştur' menüsünden kendi özel fonksiyonunu (Örn: Zıpla, HasarAl) yazar.",
         ["Özel Blok", "Fonksiyon", "Modüler Kod", "Yeniden Kullanılabilirlik"],
         "Zıplama mekaniği tek bir blok haline getirilip istenen yerde çağrılır.",
         "Aynı kodları tekrar tekrar yazmak yerine kendi bloğunu oluşturmanın avantajı nedir?",
         "Kodları kısaltır, okunabilir kılar ve hata yapıldığında tek bir yerden düzeltilmesini sağlar."),
        
        ("Ara Tatil", "2. Dönem Ara Tatil Tekrarı", "Scratch Oyun Maratonu Kampı",
         "Haber salma, değişkenler ve modüler bloklar üzerine oyun tamamlama çalışması yapar.",
         ["Ara Tatil", "Kamp", "Oyun Maratonu", "Debug"],
         "Hatalı çalışan Scratch projelerini onarma yarışması düzenlenir.",
         "Scratch'te bir değişkenin sadece o kuklaya mı yoksa tüm kuklalara mı ait olacağı nereden seçilir?",
         "Değişken oluşturulurken 'Tüm kuklalar için' veya 'Sadece bu kukla için' seçeneğinden belirlenir."),
        
        ("Scratch Oyun Programlama", "Yerçekimi ve Zıplama Mekaniği", "Platform Oyunu Temelleri (Y Hızı Değişkeni)",
         "'Y Hızı' değişkeni oluşturarak kuklaya gerçekçi yerçekimi ivmesi ve zıplama hareketi kazandırır.",
         ["Yerçekimi (Gravity)", "Platform Oyunu", "Y Hızı", "İvme"],
         "Mario tarzı basamaklara zıplayan platform karakteri kodlanır.",
         "Yerçekimi simülasyonunda kuklanın sürekli aşağı çekilmesi için 'Y Hızı' değişkeni her adımda ne yapılır?",
         "Her adımda 1 azaltılır (negatif değer alır)."),
        
        ("Scratch Oyun Programlama", "İkizini Yarat (Klonlama) Mekaniği", "Gökten Düşen Nesneler (Create Clone of Myself)",
         "Tek bir kukladan yüzlerce klon üreterek gökten yağan meyveler veya meteorlar oluşturur.",
         ["Klonlama (Clone)", "İkizini Yarat", "İkiz Olarak Başladığımda", "Hafıza"],
         "Gökten rastgele aralıklarla yağan elma yakalama oyunu kodlanır.",
         "Scratch'te klonlanan kuklaların görevleri bittiğinde ekranda kalabalık yapmaması için ne yapılmalıdır?",
         "'Bu ikizi sil' bloğu ile bellekten temizlenmelidir."),

        # Ünite 7: İleri Seviye Projeler ve Bilişim Kültürü (29-36)
        ("İleri Seviye Kodlama", "Çok Seviyeli Oyun Tasarımı (Level 1, Level 2)", "Dekor Değişimi ve Seviye Atlama",
         "Skor 10 olunca arka plan dekorunu ve engelleri değiştirerek bir üst levele geçiş yaptırır.",
         ["Level Atlama", "Dekor Değişimi", "Zorluk Artışı", "Oyun Döngüsü"],
         "2 seviyeli labirent oyunu projesi geliştirilir.",
         "Bir oyunda seviye atlandığında kuklanın ilk yapması gereken eylem nedir?",
         "Başlangıç koordinatlarına (x:0, y:0 gibi) geri dönmeli ve skoru yeni seviyeye ayarlamalıdır."),
        
        ("İleri Seviye Kodlama", "Kalem Eklentisi ile Geometrik Çizimler", "Döngülerle Kare, Üçgen ve Çember Çizdirme",
         "Scratch Kalem (Pen) eklentisini açarak kaplumbağa geometrisiyle açılar ve şekiller çizer.",
         ["Kalem Eklentisi", "Geometrik Çizim", "Dış Açılar", "Açı Hesabı"],
         "Ekrana 360 derecelik renkli spiral desenler çizdirilir.",
         "Scratch'te bir kare çizdirmek için '90 derece dön' ve '100 adım git' komutları kaç kez tekrarlanmalıdır?",
         "4 kez tekrarlanmalıdır."),
        
        ("İleri Seviye Kodlama", "Müzik ve Ses Eklentisi ile Çalgı Tasarımı", "Notalar, Vuruşlar ve Kendi Piyanonu Yap",
         "Müzik eklentisiyle bilgisayar klavyesini sanal bir piyanoya veya bateri kitine dönüştürür.",
         ["Müzik Eklentisi", "Notalar", "Vuruş", "Piyano"],
         "Klavyedeki 1, 2, 3, 4 tuşlarına Do, Re, Mi, Fa notaları atanır.",
         "Scratch'te bir notanın daha uzun veya kısa çalması hangi değerle ayarlanır?",
         "Vuruş (beat) süresi değeriyle ayarlanır."),
        
        ("İleri Seviye Kodlama", "Video Algılama ve Yapay Zekâ Eklentisi", "Kamera Hareketiyle Balon Patlatma",
         "Web kamerasını açarak ekrandaki hareket miktarıyla etkileşime giren hareketli oyun kodlar.",
         ["Video Algılama", "Kamera", "Yapay Zekâ", "Etkileşim"],
         "Elleri kameraya sallayarak ekranda uçuşan balonları patlatma oyunu yapılır.",
         "Video algılama teknolojisi günümüzde hangi alanlarda yoğun olarak kullanılır?",
         "Güvenlik kameralarında, otonom araçlarda ve akıllı telefon yüz tanıma sistemlerinde kullanılır."),
        
        ("Bilişim Kültürü", "Geleceğin Meslekleri ve Teknoloji Trendleri", "Yapay Zekâ Mühendisliği, Veri Bilimi, Siber Güvenlik",
         "Yazılım geliştirici, siber güvenlik uzmanı, robotik mühendisi gibi geleceğin mesleklerini tanır.",
         ["Geleceğin Meslekleri", "Yapay Zekâ", "Veri Bilimi", "Kariyer"],
         "Öğrenciler 2035 yılındaki hayal ettikleri teknoloji mesleğini tanıtır.",
         "Büyük miktardaki veriyi analiz edip anlamlı sonuçlar çıkaran meslek dalı hangisidir?",
         "Veri Bilimcisi (Data Scientist)."),
        
        ("Bilişim Kültürü", "Yeşil Bilişim ve E-Atık Yönetimi", "Elektronik Atıklar, Enerji Tasarrufu ve Geri Dönüşüm",
         "Eski tablet, telefon ve pillerin doğaya verdiği ağır metal zararlarını ve e-atık geri dönüşümünü kavrar.",
         ["E-Atık", "Yeşil Bilişim", "Geri Dönüşüm", "Ağır Metaller"],
         "Okulda 'E-Atık Toplama Kampanyası' düzenlenir.",
         "Kullanılmayan eski elektronik aletler neden normal çöpe atılmamalıdır?",
         "İçerdikleri cıva, kurşun ve lityum gibi zehirli ağır metallerin toprağa ve yeraltı sularına karışmaması içindir."),
        
        ("Bilişim Kültürü", "Yıl Sonu Scratch Oyun Şenliği", "Proje Sunumu ve Akran Değerlendirmesi",
         "Öğrenciler dönem boyunca geliştirdikleri oyunları bir arayüzde sunar, birbirlerinin kodlarını inceler.",
         ["Oyun Şenliği", "Akran Değerlendirmesi", "Kod İnceleme", "Portfolyo"],
         "Sınıfta mini bağımsız oyun festivali (Game Jam) sergisi yapılır.",
         "Bir yazılım projesini başkalarıyla paylaşmadan önce yapılması gereken en önemli test nedir?",
         "Farklı senaryolarda oynayarak hiçbir kilitlenme veya puan hatası olmadığını doğrulayan kullanıcı testidir."),
        
        ("Bilişim Kültürü", "6. Sınıf Bilişim Yıl Sonu Sentezi ve Mezuniyet", "Dijital Liderlik ve Başarı Sertifikası",
         "İşletim sistemleri, Excel otomasyonu ve oyun programlama kazanımlarını bütünleştirir.",
         ["Mezuniyet", "Sentez", "Dijital Liderlik", "Geleceğe Bakış"],
         "Öğrencilere 'Genç Kodlayıcı Başarı Belgesi' takdim edilir.",
         "Algoritmik düşünme becerisi bir insana sadece bilgisayarda değil hayatta ne kazandırır?",
         "Zorluklar karşısında paniğe kapılmadan, adım adım ve mantıklı çözümler üretebilme soğukkanlılığı kazandırır.")
    ]
    assert len(u) == 36, f"Bil 6 count: {len(u)}"
    return {
        'title': '6. Sınıf',
        'subtitle': 'Ortaokul Bilişim Teknolojileri ve Yazılım',
        'badge': 'Ortaokul Bilişim',
        'weeks': _make_weeks(u, 'BİL.6')
    }

def get_bil_7():
    # 7. Sınıf İleri Düzey Algoritmalar, mBlock & Robotik Kodlama (36 Hafta)
    u = [
        # Ünite 1: Bilgisayar Sistemleri ve Ağ Güvenliği (1-6)
        ("Ağ Güvenliği", "Ağ Topolojileri ve Veri İletimi", "Yıldız, Halka ve Veri Yolu (Bus) Topolojileri",
         "Bilgisayarların birbirine bağlanma biçimlerini (topolojileri) ve paket anahtarlamalı veri iletimini modeller.",
         ["Topoloji", "Yıldız Topoloji", "Veri Paketi", "Switch"],
         "Sınıfta kablolarla insan ağı simülasyonu yapılır.",
         "Bir bilgisayar bozulduğunda diğerlerinin çalışmaya devam ettiği en yaygın modern topoloji hangisidir?",
         "Yıldız (Star) Topolojisidir."),
        
        ("Ağ Güvenliği", "Güvenlik Duvarı (Firewall) ve Portlar", "Gelen ve Giden Ağ Trafiğini Denetleme",
         "Güvenlik duvarının yetkisiz girişleri nasıl engellediğini ve port mantığını kavrar.",
         ["Firewall", "Port", "Ağ Trafiği", "Siber Kalkan"],
         "Güvenlik duvarı kuralları uygulamalı incelenir.",
         "Bir bilgisayara internetten izinsiz erişimleri ve saldırıları filtreleyen güvenlik katmanı nedir?",
         "Güvenlik Duvarı (Firewall)."),
        
        ("Ağ Güvenliği", "Kriptoloji ve Veri Şifreleme", "Sezar Şifrelemesi ve Simetrik/Asimetrik Şifreleme",
         "Tarihteki Sezar şifreleme yöntemini çözer; modern 256-bit şifreleme algoritmalarını tanır.",
         ["Kriptoloji", "Sezar Şifresi", "Şifreleme", "Anahtar"],
         "Harfleri 3 kaydırarak gizli mesaj çözme atölyesi yapılır.",
         "Sezar şifrelemesinde 3 birim ileri kaydırmayla 'ALI' kelimesi nasıl şifrelenir?",
         "Ç - O - L ('ÇOL') şeklinde şifrelenir."),
        
        ("Ağ Güvenliği", "Kablosuz Ağ Güvenliği (Wi-Fi)", "WPA2, WPA3 ve Halka Açık Ağ Riskleri",
         "Halka açık şifresiz Wi-Fi ağlarında bankacılık işlemi yapmanın tehlikelerini açıklar.",
         ["Wi-Fi Güvenliği", "WPA3", "Halka Açık Ağ", "Man-in-the-Middle"],
         "Kafe ve havaalanı Wi-Fi tuzakları senaryoları incelenir.",
         "Halka açık ücretsiz Wi-Fi ağlarına bağlanırken hangi güvenlik önlemi alınmalıdır?",
         "VPN kullanılmalı ve asla şifre veya kredi kartı bilgisi girilmemelidir."),
        
        ("Ağ Güvenliği", "Yedekleme Stratejileri ve 3-2-1 Kuralı", "Fidye Yazılımlarına Karşı Veri Kurtarma",
         "Veri kaybına karşı 3 kopya, 2 farklı ortam ve 1 uzak bulut yedeği kuralını öğrenir.",
         ["Yedekleme (Backup)", "3-2-1 Kuralı", "Harici Disk", "Bulut"],
         "Okul laboratuvarı verilerinin harici diske yedeklenme planı yapılır.",
         "Veri yedeklemede altın standart olan '3-2-1 Kuralı' neyi ifade eder?",
         "Verinin en az 3 kopyası olmalı, 2 farklı depolama ortamında tutulmalı ve 1 tanesi uzak/bulut konumda saklanmalıdır."),
        
        ("Ağ Güvenliği", "Sosyal Mühendislik ve Phishing (Oltalama)", "İnsan Zaafiyetlerini Kullanan Dijital Saldırılar",
         "Tebrikler ödül kazandınız veya acil hesap kapatılacak tuzak mesajlarını tespit eder.",
         ["Sosyal Mühendislik", "Phishing", "Sahte Link", "Uyanıklık"],
         "Gelen sahte SMS ve e-postalar incelenir.",
         "Bankanızdan gelmiş gibi görünen 'Hesabınız askıya alındı, hemen tıklayın' mesajı ne tür bir saldırıdır?",
         "Oltalama (Phishing / Yemleme) saldırısıdır."),

        # Ünite 2: İleri Algoritmalar ve Veri Yapıları (7-12)
        ("İleri Algoritmalar", "Sıralama Algoritmaları (Sorting)", "Kabarcık Sıralama (Bubble Sort) ve Seçmeli Sıralama",
         "Sayı dizilerini küçükten büyüğe sıralayan algoritmaların çalışma mantığını kartlarla uygular.",
         ["Sıralama", "Bubble Sort", "Karşılaştırma", "Dizi"],
         "Öğrenciler ellerindeki sayı kartlarını yanındakilerle takas ederek Bubble Sort uygular.",
         "Bubble Sort (Kabarcık Sıralaması) yan yana duran iki sayıyı nasıl karşılaştırır?",
         "Soldaki sayı sağdakinden büyükse yerlerini değiştirir, bu işlemi dizi bitene kadar tekrarlar."),
        
        ("İleri Algoritmalar", "Arama Algoritmaları (Searching)", "Doğrusal Arama (Linear) ve İkili Arama (Binary Search)",
         "Sıralı bir listede ortadan bölerek hedef sayıyı çok hızlı bulan Binary Search algoritmasını çözümler.",
         ["Binary Search", "Linear Search", "Arama Algoritması", "Hız"],
         "1 ile 100 arasındaki bir sayıyı en fazla 7 tahminde bulma oyunu oynanır.",
         "1024 elemanlı sıralı bir listede İkili Arama (Binary Search) ile en fazla kaç adımda hedefe ulaşılır?",
         "En fazla 10 adımda ulaşılır (2^10 = 1024)."),
        
        ("Ara Tatil", "1. Dönem Ara Tatil Tekrarı", "Ağ Güvenliği ve Algoritma Kampı",
         "Kriptoloji, ağ topolojileri ve sıralama algoritmaları üzerine proje föyü tamamlar.",
         ["Ara Tatil", "Kamp", "Algoritma", "Tekrar"],
         "Mini algoritma yarışması düzenlenir.",
         "Bir arama algoritmasında listenin sıralı olması şartı hangi yöntem için zorunludur?",
         "İkili Arama (Binary Search) için zorunludur."),
        
        ("İleri Algoritmalar", "Diziler ve Listeler Mantığı", "İndeks Numarası (0. Eleman, 1. Eleman)",
         "Birden fazla veriyi tek bir değişken altında saklayan dizi (Array/List) yapısını kavrar.",
         ["Dizi (Array)", "İndeks", "Liste", "Veri Yapısı"],
         "Haftanın 7 gününü tek bir dizide tutup indeks numarasıyla çağırma alıştırması.",
         "Yazılım dillerinde dizilerin ilk elemanının indeks numarası genellikle kaçtır?",
         "0 (sıfır)dır."),
        
        ("İleri Algoritmalar", "Fonksiyonlar ve Parametre Gönderme", "Girdi Alan ve Değer Döndüren (Return) Fonksiyonlar",
         "Dışarıdan iki sayı alıp toplamını geri döndüren fonksiyon mantığını şematize eder.",
         ["Fonksiyon", "Parametre", "Argüman", "Geri Dönüş (Return)"],
         "KareAl(sayı) fonksiyonunun çalışma prensibi incelenir.",
         "Bir fonksiyona hesaplama yapması için dışarıdan gönderilen değerlere ne ad verilir?",
         "Parametre (veya Argüman) adı verilir."),
        
        ("İleri Algoritmalar", "Mantıksal Operatörler: DEĞİL, VE, VEYA", "Doğruluk Tabloları (Truth Tables)",
         "Boole (Boolean) cebirinin temelini oluşturan mantıksal doğruluk tablolarını hesaplar.",
         ["Mantık Kapıları", "VE (AND)", "VEYA (OR)", "DEĞİL (NOT)", "Boolean"],
         "Lamba anahtarı devreleri mantık operatörleriyle ilişkilendirilir.",
         "VE (AND) operatöründe sonucun Doğru (1) çıkması için girdiler nasıl olmalıdır?",
         "Her iki girdinin de mutlaka Doğru (1) olması gerekir."),

        # Ünite 3: Robotik Kodlama ve Sensörler (13-19)
        ("Robotik Kodlama", "Robotik Nedir? Robotun Bileşenleri", "Sensörler (Duyular), İşlemci (Beyin), Eyleyiciler (Kaslar)",
         "Bir robotun çevreyi sensörlerle algılayıp motorlarla hareket eden bir sistem olduğunu açıklar.",
         ["Robotik", "Mikrodenetleyici", "Sensör", "Eyleyici (Aktüatör)"],
         "İnsan vücudu ile robot bileşenleri benzetimi yapılır.",
         "Robot sisteminde insan kaslarına ve kollarına karşılık gelen bileşenlere ne ad verilir?",
         "Eyleyiciler / Aktüatörler (Motorlar, pistonlar)."),
        
        ("Robotik Kodlama", "Mikrodenetleyici Kartlar (Arduino / Micro:bit)", "Pinler, Dijital ve Analog Giriş/Çıkış",
         "Arduino veya Micro:bit üzerindeki dijital (HIGH/LOW) ve analog (0-1023) pinleri öğrenir.",
         ["Arduino", "Micro:bit", "Dijital Pin", "Analog Pin"],
         "Tinkercad Circuits ortamında sanal Arduino kartı incelenir.",
         "Dijital bir pinden alınabilecek sadece iki durum hangileridir?",
         "HIGH (1 / 5 Volt - Açık) ve LOW (0 / 0 Volt - Kapalı)."),
        
        ("Robotik Kodlama", "Temel Devre Elemanları: LED ve Direnç", "Artı/Eksi Kutuplar, Ohm Kanunu ve Breadboard",
         "LED diyotun bacaklarını (anot/katot) tanır; LED'in yanmaması için seri bağlanan direncin görevini kavrar.",
         ["LED", "Direnç (Resistor)", "Breadboard", "Ohm"],
         "Breadboard üzerinde ilk yanıp sönen LED devresi (Blink) kurulur.",
         "LED devrelerinde neden mutlaka bir direnç kullanılmalıdır?",
         "Aşırı akım geçip LED lambanın patlamasını / yanmasını engellemek için."),
        
        ("Robotik Kodlama", "Buton ile LED Kontrolü", "Giriş Sinyali ile Çıkışı Tetikleme",
         "Butona basıldığında yanan, bırakıldığında sönen dijital giriş devresini blok kodla programlar.",
         ["Buton", "Giriş Sinyali", "If Koşulu", "Pull-down"],
         "Sanal simülasyonda kapı zili devresi tasarlanır.",
         "Butona basıldığında okunan dijital sinyal değeri nedir?",
         "HIGH (1) değeridir."),
        
        ("Robotik Kodlama", "Mesafe Sensörü (HC-SR04) ile Park Sensörü", "Ultrasonik Ses Dalgaları ile Mesafe Ölçümü",
         "Ses dalgalarının yankılanma süresiyle mesafe hesaplayan sensörle otomobil park sensörü yapar.",
         ["Mesafe Sensörü", "Ultrasonik", "Park Sensörü", "Buzzer"],
         "Cisme yaklaştıkça daha hızlı öten buzzer devresi kodlanır.",
         "Ultrasonik mesafe sensörü mesafeyi nasıl ölçer?",
         "Tetik piniyle gönderdiği yüksek frekanslı ses dalgasının cisme çarpıp geri dönme süresini hesaplayarak."),
        
        ("Robotik Kodlama", "1. Dönem Sonu Sentezi", "Robotik Devre Tasarım Sınavı",
         "Sensör, LED ve buton bileşenlerini içeren akıllı sistem projesi sunumu yapar.",
         ["Sentez", "Laboratuvar", "Robotik Proje", "Ölçme"],
         "Tinkercad üzerinde çalışan park sensörü devresi notlandırılır.",
         "Ses çıkaran küçük piezo elektrik devre elemanına ne ad verilir?",
         "Buzzer adı verilir."),
        
        ("Robotik Kodlama", "1. Dönem Sonu Karnesi", "Yarıyıl Tatili 3B Tasarım Fikirleri",
         "2. dönemde yapılacak 3 boyutlu modelleme ve akıllı şehir projeleri için taslak çizer.",
         ["Karne", "3B Tasarım Taslağı", "Gelişim", "Yarıyıl"],
         "Öğrencilere tatil Tinkercad hesabı ve görevleri atanır.",
         "Robotik projelerde kullanılan yazılım ile donanımın birleştiği sistemlere ne ad verilir?",
         "Gömülü Sistemler (Embedded Systems)."),

        # Ünite 4: 3 Boyutlu Tasarım ve Katmanlı Üretim (20-24)
        ("3B Tasarım", "3 Boyutlu Düşünme ve X, Y, Z Eksenleri", "En, Boy ve Derinlik (Z Ekseni)",
         "İki boyutlu çizim ile 3 boyutlu modelleme arasındaki hacim ve derinlik (Z) farkını kavrar.",
         ["3B Tasarım", "Z Ekseni", "Hacim", "Tinkercad"],
         "Tinkercad çalışma düzleminde nesneleri yükseltme ve döndürme alıştırması.",
         "3 boyutlu uzayda derinliği / yüksekliği temsil eden eksen hangisidir?",
         "Z eksenidir."),
        
        ("3B Tasarım", "Temel Şekilleri Birleştirme ve Gruplama", "Küp, Silindir, Koni ve Hizalama",
         "Temel geometrik cisimleri bir araya getirerek 'Grupla' (Ctrl+G) aracıyla tek parça haline getirir.",
         ["Gruplama", "Hizalama", "Temel Şekiller", "Modelleme"],
         "Tinkercad ortamında minik bir anahtarlık ve satranç piyonu modellenir.",
         "Tinkercad'de iki farklı cismi tek bir nesne yapmak için hangi araç kullanılır?",
         "'Grupla' (Group) aracı kullanılır."),
        
        ("3B Tasarım", "Delik Oluşturma ve Kesme İşlemleri", "Cisimlerden Boşluk Çıkarma (Hole)",
         "Katı bir şekli 'Delik' formuna getirip başka bir cisimle gruplayarak pencere veya kupa deliği açar.",
         ["Delik (Hole)", "Boşluk Çıkarma", "Kupa Tasarımı", "Hacim"],
         "İçi boş kahve kupası ve kulpu tasarlanır.",
         "Bir silindirin ortasında delik açmak için ne yapılır?",
         "Daha küçük bir silindir 'Delik' yapılır, büyük silindirin içine ortalanıp ikisi gruplanır."),
        
        ("3B Tasarım", "3B Yazıcılar (3D Printers) ve Katmanlı İmalat", "Filament, Nozzle, Dilimleme (Slicer / Cura)",
         "3B yazıcının plastik filamenti eriterek katman katman (katmanlı üretim) basma mantığını kavrar.",
         ["3B Yazıcı", "Filament (PLA/ABS)", "Nozzle", "Katmanlı Üretim"],
         "3B yazıcının çalışma anı laboratuvarda canlı gözlemlenir.",
         "3B yazıcılarda en yaygın kullanılan doğada çözünebilen mısır nişastası bazlı filament türü hangisidir?",
         "PLA (Polilaktik Asit) filamenti."),
        
        ("3B Tasarım", "Dilimleme Yazılımları ve Baskı Süreci", "STL Dosyası, G-Code ve Destek Yapıları (Supports)",
         "Tasarımı .STL olarak dışa aktarır; dilimleme yazılımında katmanlara ve G-Code'a çevirir.",
         ["STL Formatı", "G-Code", "Dilimleme (Slicing)", "Destek (Support)"],
         "Tasarımın baskı süresi ve gramaj hesabı dilimleme programında incelenir.",
         "3B yazıcıların motorlarına hangi koordinatlara gideceğini söyleyen komut diline ne ad verilir?",
         "G-Code."),

        # Ünite 5: Akıllı Sistemler ve Nesnelerin İnterneti (IoT) (25-30)
        ("Akıllı Sistemler", "Nesnelerin İnterneti (IoT) Nedir?", "Cihazların Birbiriyle Konuşması",
         "Ev aletlerinin, sokak lambalarının ve arabaların internete bağlanarak veri paylaşmasını kavrar.",
         ["IoT (Nesnelerin İnterneti)", "Akıllı Cihaz", "Veri İletişimi", "Akıllı Şehir"],
         "Akıllı buzdolabı ve uzaktan kontrol edilen klima örnekleri tartışılır.",
         "Nesnelerin İnterneti (IoT) kavramı en basit tabirle ne anlama gelir?",
         "Fiziksel nesnelerin sensörler ve internet aracılığıyla birbirleriyle iletişim kurup veri paylaşmasıdır."),
        
        ("Akıllı Sistemler", "Akıllı Ev Sistemleri Tasarımı", "Otomatik Işık, Yangın ve Gaz Alarmı",
         "LDR (Işık sensörü) ve gaz sensörü kullanarak hava karardığında yanan akıllı sokak lambası tasarlar.",
         ["Akıllı Ev", "LDR Sensörü", "Gaz Sensörü", "Otomasyon"],
         "LDR üzerine parmak basıldığında (karanlık olunca) yanan sokak lambası devresi kurulur.",
         "Ortamdaki ışık şiddetini ölçen ve karanlıkta direnci artan sensör hangisidir?",
         "LDR (Işığa Bağımlı Direnç / Foto Direnç)."),
        
        ("Ara Tatil", "2. Dönem Ara Tatil Kampı", "3B Tasarım ve IoT Projeleri Kampı",
         "Akıllı sera veya akıllı ev maketi tasarımı üzerine proje taslağı tamamlar.",
         ["Ara Tatil", "IoT Kampı", "Akıllı Şehir", "Proje"],
         "Çevrimiçi proje inceleme oturumu yapılır.",
         "Akıllı tarımda toprağın su ihtiyacını otomatik belirleyen sensör nedir?",
         "Toprak Nem Sensörüdür."),
        
        ("Akıllı Sistemler", "Akıllı Tarım ve Sera Uygulaması", "Toprak Nem Sensörü ve Otomatik Sulama",
         "Toprak kuruduğunda su pompasını çalıştıran, nem doyunca durduran akıllı sulama devresi kodlar.",
         ["Akıllı Tarım", "Toprak Nem Sensörü", "Su Pompası", "Röle"],
         "Saksı bitkisi için otomatik sulama sistemi simüle edilir.",
         "Robotik sistemlerde yüksek voltajlı su motorlarını açıp kapatan anahtar elemanına ne denir?",
         "Röle (Relay) modülü."),
        
        ("Akıllı Sistemler", "Çizgi İzleyen ve Engelden Kaçan Robotlar", "Kızılötesi (IR) Sensörler ve DC Motor Sürücüsü",
         "Zemindeki siyah çizgiyi takip eden çizgi izleyen robotun algoritmasını ve motor yönlerini öğrenir.",
         ["Çizgi İzleyen", "IR Sensör", "Motor Sürücü (L298N)", "DC Motor"],
         "Çizgi izleyen robot pisti üzerinde sensör okuma mantığı incelenir.",
         "Çizgi izleyen robotta sağ sensör siyah çizgiyi gördüğünde robot ne tarafa dönmelidir?",
         "Sağa doğru dönmelidir."),
        
        ("Akıllı Sistemler", "Yapay Zekâya Giriş ve Makine Öğrenmesi", "Veri Seti, Eğitim ve Karar Verme",
         "Görüntüleri tanıyan bir yapay zekâ modelini (Teachable Machine) eğitir ve test eder.",
         ["Yapay Zekâ (AI)", "Makine Öğrenmesi", "Eğitim Verisi", "Model Testi"],
         "Kameraya gösterilen maskeli ve maskesiz yüzleri ayırt eden yapay zekâ eğitilir.",
         "Bir makine öğrenmesi modelinin doğru çalışması için en önemli gereksinim nedir?",
         "Yeterli miktarda, çeşitli ve doğru etiketlenmiş eğitim verisidir."),

        # Ünite 6: Bilişim ve İnovasyon Projeleri (31-36)
        ("İnovasyon Projeleri", "Proje Yönetimi ve Tasarım Odaklı Düşünme", "Empati, Tanımla, Fikir Üret, Prototiple, Test Et",
         "Tasarım odaklı düşünme (Design Thinking) 5 adımını bir toplumsal probleme çözüm üretirken uygular.",
         ["Design Thinking", "Empati", "Prototip", "İnovasyon"],
         "Engelli bireylerin hayatını kolaylaştıracak teknolojik fikir beyin fırtınası.",
         "Tasarım odaklı düşünmenin ilk adımı olan 'Empati' aşamasında ne yapılır?",
         "Kullanıcıların ihtiyaçları, hisleri ve yaşadıkları zorluklar yerinde dinlenir ve anlaşılır."),
        
        ("İnovasyon Projeleri", "Proje Taslağı ve Malzeme Listesi Çıkarma", "Devre Şeması, Maliyet ve Zaman Planı",
         "Geliştirilecek projenin malzeme listesini (BOM) ve bağlantı şemasını hazırlar.",
         ["Proje Taslağı", "Gantt Şeması", "Malzeme Listesi", "Maliyet"],
         "Proje bütçe tablosu oluşturulur.",
         "Bir projenin aşamalarını ve bitiş tarihlerini gösteren zaman çizelgesine ne ad verilir?",
         "Gantt Çizelgesi / Şeması."),
        
        ("İnovasyon Projeleri", "Prototip Üretimi ve Laboratuvar Uygulaması", "Devre Kurulumu ve Kodların Yüklenmesi",
         "3B yazıcıdan basılan gövde içerisine sensörleri ve Arduino devresini monte eder.",
         ["Prototipleme", "Montaj", "Kod Yükleme", "Entegrasyon"],
         "Gruplar halinde çalışan prototip ortaya çıkarılır.",
         "Bir ürünün seri üretime geçmeden önceki ilk çalışan deneme modeline ne denir?",
         "Prototip."),
        
        ("İnovasyon Projeleri", "Proje Testi ve Hata Giderme (Saha Testi)", "Sensör Kalibrasyonu ve Güvenilirlik",
         "Saha koşullarında robotu test eder, sensör hassasiyet ayarlarını kalibre eder.",
         ["Saha Testi", "Kalibrasyon", "Dayanıklılık", "İyileştirme"],
         "Farklı ışık koşullarında LDR ve çizgi sensörleri test edilir.",
         "Sensörlerin doğru değer okuması için yapılan sıfırlama ve hassasiyet ayarına ne denir?",
         "Kalibrasyon."),
        
        ("İnovasyon Projeleri", "Proje Sunumu ve Bilim Şenliği Hazırlığı", "Poster, Sunum Becerileri ve Jüri Savunması",
         "TÜBİTAK 4006 veya TEKNOFEST tarzı proje standı hazırlar ve çalışmasını açıklar.",
         ["Proje Standı", "TÜBİTAK 4006", "TEKNOFEST", "Savunma"],
         "Sınıfta jüri önünde 3 dakikalık asansör konuşması (pitching) provası yapılır.",
         "Teknoloji projelerinde projenin amacını ve sonucunu özetleyen kısa tanıtım konuşmasına ne denir?",
         "Asansör Konuşması (Elevator Pitch)."),
        
        ("İnovasyon Projeleri", "7. Sınıf Bilişim ve Robotik Yıl Sonu Sentezi", "Genç İnovatörler Festivali ve Veda",
         "Yıl boyu öğrenilen ağlar, algoritmalar, robotik ve 3B tasarım becerilerini kutlar.",
         ["Sentez", "İnovasyon Festivali", "Robotik", "Mezuniyet"],
         "Tüm okulun katılımıyla robot gösterileri gerçekleştirilir.",
         "Robotik ve kodlama eğitiminin geleceğin gençlerine kattığı en büyük vizyon nedir?",
         "Sorunlara şikayet etmek yerine, teknolojiyi bir araç olarak kullanarak kalıcı çözümler üretebilmektir.")
    ]
    assert len(u) == 36, f"Bil 7 count: {len(u)}"
    return {
        'title': '7. Sınıf',
        'subtitle': 'İleri Algoritmalar, Robotik Kodlama & 3B Tasarım',
        'badge': 'Ortaokul Bilişim',
        'weeks': _make_weeks(u, 'BİL.7')
    }

def get_bil_8():
    # 8. Sınıf Metin Tabanlı Kodlama (Python), Yapay Zekâ & Siber Güvenlik (36 Hafta)
    u = [
        # Ünite 1: Metin Tabanlı Kodlamaya Giriş (Python) (1-6)
        ("Python ile Programlama", "Blok Kodlamadan Metin Tabanlı Kodlamaya Geçiş", "Python Dili, Sözdizimi (Syntax) ve IDLE",
         "Metin tabanlı dillerin esnekliğini ve Python'un sade, okunabilir sözdizimini tanır.",
         ["Python", "Metin Tabanlı Kodlama", "Syntax", "IDLE / VS Code"],
         "Python kurulumu ve ilk print(\"Merhaba Dünya\") kodunun çalıştırılması.",
         "Python dilinde ekrana yazı yazdırmak için hangi yerleşik fonksiyon kullanılır?",
         "`print()` fonksiyonu kullanılır."),
        
        ("Python ile Programlama", "Değişkenler ve Temel Veri Tipleri", "int (Tam Sayı), float (Ondalık), str (Metin), bool (Mantıksal)",
         "Python'da değişken tanımlar; veri tiplerini type() fonksiyonuyla sorgular.",
         ["Değişken", "int", "float", "string", "bool"],
         "Farklı veri tipleri tanımlanarak bellekteki durumları incelenir.",
         "`yas = 14` ve `not_ort = 85.5` değişkenlerinin veri türleri sırasıyla nelerdir?",
         "Tam sayı (`int`) ve ondalıklı sayı (`float`)."),
        
        ("Python ile Programlama", "Kullanıcıdan Veri Alma: input() Fonksiyonu", "Konsol Girişi ve Tip Dönüşümü (Type Casting)",
         "input() ile kullanıcıdan string veri alır; int() ve float() ile sayıya dönüştürür.",
         ["input()", "Tip Dönüşümü", "int()", "Kullanıcı Girişi"],
         "Kullanıcıdan iki sayı alıp toplayan mini hesap makinesi kodlanır.",
         "`sayi = input(\"Bir sayı girin: \")` kodundan dönen değerin türü nedir?",
         "Her zaman metinsel ifadedir (`str`); matematiksel işlem için `int()` yapılmalıdır."),
        
        ("Python ile Programlama", "Aritmetik Operatörler ve Matematiksel İşlemler", "+, -, *, /, // (Tam Bölme), % (Mod Alma), ** (Üs Alma)",
         "Python'da mod alma (%) ve üs alma (**) operatörlerini matematiksel problemlere uygular.",
         ["Aritmetik Operatörler", "Mod Alma (%)", "Tam Bölme (//)", "Üs Alma (**)"],
         "Girilen sayının tek mi çift mi olduğunu mod 2 (% 2) işlemiyle belirleme.",
         "Python'da `7 % 3` ve `2 ** 3` işlemlerinin sonuçları sırasıyla nedir?",
         "1 (kalan 1'dir) ve 8 (2'nin küpüdür)."),
        
        ("Python ile Programlama", "Metin (String) İşlemleri ve İndeksleme", "Metinleri Birleştirme, len() ve Parçalama (Slicing)",
         "String ifadelerin karakterlerine indekslerle ulaşır; uzunluğunu len() ile hesaplar.",
         ["String Slicing", "len()", "İndeksleme", "Metin İşleme"],
         "Kullanıcının adını tersten yazdıran kodlama çalışması yapılır.",
         "`okul = \"ATATURK\"` değişkeninde `okul[0]` ifadesi hangi harfi verir?",
         "'A' harfini verir (ilk karakter 0. indekstir)."),
        
        ("Python ile Programlama", "Hata Türleri ve Kod Okuma", "Sözdizimi Hatası (SyntaxError), Çalışma Zamanı (NameError)",
         "Parantez ve tırnak hatalarını okur, konsoldaki hata mesajlarını (Traceback) çözümler.",
         ["SyntaxError", "NameError", "TypeError", "Debugging"],
         "Bozuk Python kodlarını düzeltme tamirhanesi etkinliği.",
         "Python'da tanımlanmamış bir değişken adı çağrıldığında hangi hata fırlatılır?",
         "`NameError: name '...' is not defined` hatası fırlatılır."),

        # Ünite 2: Karar Yapıları ve Koşullu Durumlar (7-11)
        ("Python ile Karar Yapıları", "Karşılaştırma ve Mantıksal Operatörler", "==, !=, <, >, <=, >= ve and, or, not",
         "İki değeri karşılaştırır; mantıksal operatörlerle birleşik şartlar oluşturur.",
         ["Karşılaştırma", "Eşittir (==)", "Eşit Değil (!=)", "and / or"],
         "Şifre kontrol koşulları hazırlanır.",
         "Python'da 'eşit midir?' kontrolü için tek eşittir mi (=) yoksa çift eşittir mi (==) kullanılır?",
         "Çift eşittir (==) kullanılır; tek eşittir atama işlemidir."),
        
        ("Python ile Karar Yapıları", "if ve else Blokları", "İki Yönlü Koşullar ve Girinti (Indentation) Kuralı",
         "Python'un en kritik kuralı olan 4 boşlukluk girintiyi (indentation) ve iki nokta (:) kuralını uygular.",
         ["if", "else", "Girinti (Indentation)", "İki Nokta (:)"],
         "Ehliyet alma yaşı (18) uygunluk testi kodlanır.",
         "Python'da `if` satırının sonuna konulması zorunlu olan noktalama işareti nedir?",
         "İki nokta üst üste (:) işaretidir."),
        
        ("Ara Tatil", "1. Dönem Ara Tatil Tekrarı", "Python Temelleri ve Karar Kampı",
         "Değişkenler, input ve if-else blokları üzerine 10 pratik kodlama görevi tamamlar.",
         ["Ara Tatil", "Kamp", "Python", "Pratik Kodlama"],
         "Çevrimiçi kodlama platformunda görev serisi tamamlanır.",
         "Python'da girinti (indentation) hatası yapıldığında hangi hata mesajı alınır?",
         "`IndentationError` hatası alınır."),
        
        ("Python ile Karar Yapıları", "elif ile Çok Yönlü Koşullar", "Not Harf Derecelendirmesi ve Menü Seçimi",
         "Birden fazla koşulu ardı ardına test etmek için `elif` bloğunu kullanır.",
         ["elif", "Çoklu Koşul", "Not Skalası", "Menü"],
         "Girilen puana göre 85-100: Pekiyi, 70-84: İyi yazdıran program kodlanır.",
         "`if - elif - else` yapısında tüm koşullar yanlışsa en son hangi blok çalışır?",
         "`else` bloğu çalışır."),
        
        ("Python ile Karar Yapıları", "İç İçe Koşullar (Nested If)", "Kullanıcı Girişi ve Yetkilendirme",
         "Bir `if` bloğu içerisine başka bir `if` yazarak kademeli güvenlik kontrolü yapar.",
         ["İç İçe If", "Nested If", "Yetkilendirme", "Admin Girişi"],
         "Banka ATM para çekme ve bakiye kontrolü simüle edilir.",
         "İç içe koşullarda ikinci if bloğunun girintisi kaç boşluk olmalıdır?",
         "İlk if bloğuna göre bir kademe daha içeride (genellikle 8 boşluk) olmalıdır."),

        # Ünite 3: Döngüler ve Tekrarlayan İşlemler (12-16)
        ("Python ile Döngüler", "for Döngüsü ve range() Fonksiyonu", "Belirli Sayıda Tekrarlayan İşlemler: range(başlangıç, bitiş, artış)",
         "`range(1, 11)` ile 1'den 10'a kadar olan sayıları ekrana yazdırır.",
         ["for Döngüsü", "range()", "Sayaç", "Artış Miktarı"],
         "1 ile 100 arasındaki tek sayıları yazdıran döngü kodlanır.",
         "`range(2, 10, 2)` fonksiyonu hangi sayıları üretir?",
         "2, 4, 6 ve 8 sayılarını üretir (bitiş değeri olan 10 dahil edilmez)."),
        
        ("Python ile Döngüler", "Döngü ile Toplam ve Çarpım Hesaplama", "Kümülatif Toplam Değişkeni (toplam += sayi)",
         "1'den n'e kadar olan sayıların toplamını ve faktöriyel hesabını döngüyle çözer.",
         ["Kümülatif Toplam", "+= Operatörü", "Faktöriyel", "Algoritma"],
         "Kullanıcının girdiği sayının faktöriyelini hesaplayan program yazılır.",
         "Python'da `toplam = toplam + i` ifadesinin kısa yazılışı nedir?",
         "`toplam += i` ifadesidir."),
        
        ("Python ile Döngüler", "while Döngüsü (Koşula Bağlı Döngü)", "Şart Sağlandığı Sürece Devam Eden Döngüler",
         "`while` döngüsünü kavrar; sayaç artırılmadığında oluşan sonsuz döngü (infinite loop) tehlikesini çözer.",
         ["while Döngüsü", "Sonsuz Döngü", "Sayaç", "Koşullu Tekrar"],
         "Doğru parola girilene kadar sürekli tekrar soran şifre paneli kodlanır.",
         "Bir `while` döngüsünde sayaç değeri artırılmazsa ne meydana gelir?",
         "Koşul daima doğru kalacağı için program sonsuz döngüye (kilitlenmeye) girer."),
        
        ("Python ile Döngüler", "Döngü Kontrol İfadeleri: break ve continue", "Döngüyü Kırma ve Adımı Atlama",
         "`break` ile döngüyü anında sonlandırır; `continue` ile o anki adımı atlayıp bir sonrakine geçer.",
         ["break", "continue", "Döngü Kontrolü", "Akış Değişimi"],
         "Sayı 13 olunca duran veya 5'in katlarını atlayan döngü kodlanır.",
         "Bir döngüde istenen şart sağlandığında döngünün tamamen sonlanmasını sağlayan anahtar kelime nedir?",
         "`break` komutudur."),
        
        ("Python ile Döngüler", "Sayı Tahmin Oyunu Projesi", "random Kütüphanesi ve Akıl Yürütme",
         "`import random` ile bilgisayarın 1-100 arasında tuttuğu sayıyı 'Yukarı / Aşağı' ipuçlarıyla bulan oyun kodlar.",
         ["import random", "randint()", "Sayı Tahmin", "Oyun Algoritması"],
         "Öğrenciler kendi metin tabanlı sayı tahmin oyunlarını kodlar.",
         "Python'da rastgele sayılar üretmek için hangi kütüphane içe aktarılır?",
         "`import random` kütüphanesi içe aktarılır."),

        # Ünite 4: Veri Yapıları ve Fonksiyonlar (17-21)
        ("Veri Yapıları ve Fonksiyonlar", "Listeler (Lists)", "Köşeli Parantez, append(), remove(), pop()",
         "Python listeleri tanımlar; eleman ekleme (append), silme (remove) ve sıralama (sort) yapar.",
         ["Liste (List)", "append()", "remove()", "sort()", "Köşeli Parantez []"],
         "Öğrenci isim listesi ve dinamik alışveriş sepeti kodlanır.",
         "`meyveler = [\"Elma\", \"Muz\"]` listesine 'Çilek' eklemek için hangi kod yazılır?",
         "`meyveler.append(\"Çilek\")` kodu yazılır."),
        
        ("Veri Yapıları ve Fonksiyonlar", "Listeler Üzerinde Döngüler", "for eleman in liste: Gezinme",
         "Liste içerisindeki elemanları `for` döngüsü ile tek tek ekrana yazdırır ve filtreler.",
         ["Liste Döngüsü", "Gezinme (Iterate)", "Filtreleme", "Eleman Sayısı"],
         "Not listesindeki 50'den büyük notları ayıklayıp yeni listeye atan kod yazılır.",
         "Bir listenin kaç elemandan oluştuğunu hangi fonksiyon söyler?",
         "`len(liste)` fonksiyonu söyler."),
        
        ("Veri Yapıları ve Fonksiyonlar", "1. Dönem Sonu Sentezi", "1. Dönem Python Yetkinlik Sınavı",
         "Değişkenler, koşullar, döngüler ve listeleri içeren konsol uygulaması sınavı yapar.",
         ["Sentez", "Python Sınavı", "Konsol Uygulaması", "Ölçme"],
         "Öğrenci not takip ve ortalama hesaplama programı kodlatılır.",
         "`[1, 2, 3] + [4, 5]` işleminin Python'daki sonucu nedir?",
         "`[1, 2, 3, 4, 5]` (iki listeyi birleştirir)."),
        
        ("Veri Yapıları ve Fonksiyonlar", "1. Dönem Sonu Karnesi", "Yarıyıl Tatili Python HackerRank Hedefi",
         "Tatil boyunca pratik kodlama yapması için çevrimiçi soru çözme listesi verilir.",
         ["Karne", "Kodlama Kampı", "Problem Çözme", "Yarıyıl"],
         "Tatil için 15 algoritma sorusu paylaşılır.",
         "Kod yazarken açıklama ve yorum satırı bırakmak için hangi sembol kullanılır?",
         "`#` (Diyez / Kare) sembolü kullanılır."),
        
        ("Veri Yapıları ve Fonksiyonlar", "Fonksiyon Tanımlama: def ve return", "Kendi Fonksiyonunu Yazma ve Çağırma",
         "`def` anahtar kelimesi ile parametreli fonksiyon yazar; sonucu `return` ile geri döndürür.",
         ["def", "return", "Fonksiyon", "Modülerlik"],
         "Dairenin alanını hesaplayan `daire_alani(r)` fonksiyonu kodlanır.",
         "Python'da yeni bir fonksiyon tanımlamaya hangi anahtar kelime ile başlanır?",
         "`def` anahtar kelimesiyle başlanır."),

        # Ünite 5: Yapay Zekâ ve Geleceğin Teknolojileri (22-28)
        ("Yapay Zekâ ve Gelecek", "Yapay Zekâ (AI) ve Tarihçesi", "Alan Turing, Turing Testi ve Zayıf/Güçlü Yapay Zekâ",
         "Turing testinin felsefesini, dar (dar kapsamlı) yapay zekâ ile genel yapay zekâ farkını tartışır.",
         ["Yapay Zekâ (AI)", "Alan Turing", "Turing Testi", "AGI"],
         "Yapay zekânın düşünebilme kapasitesi üzerine münazara yapılır.",
         "Bir bilgisayarın insan gibi düşünüp düşünemediğini anlamak için önerilen tarihi test nedir?",
         "Turing Testi."),
        
        ("Yapay Zekâ ve Gelecek", "Makine Öğrenmesi (Machine Learning)", "Denetimli (Supervised), Denetimsiz (Unsupervised) Öğrenme",
         "Etiketli verilerle sınıflandırma (denetimli) ve kümeleme (denetimsiz) modellerini kavrar.",
         ["Makine Öğrenmesi", "Denetimli Öğrenme", "Denetimsiz Öğrenme", "Sınıflandırma"],
         "Spam e-posta filtrelerinin nasıl öğrendiği incelenir.",
         "Bir yapay zekâ modeline kedi ve köpek fotoğraflarını 'etiketleriyle' göstererek eğitmek hangi öğrenme türüdür?",
         "Denetimli Öğrenme (Supervised Learning)."),
        
        ("Yapay Zekâ ve Gelecek", "Yapay Sinir Ağları ve Derin Öğrenme", "İnsan Beyni Nöron Modeli ve Katmanlar",
         "Biyolojik nöronlardan ilham alan yapay sinir ağlarının (ANN) katmanlı yapısını kavrar.",
         ["Yapay Sinir Ağı", "Nöron", "Derin Öğrenme (Deep Learning)", "Katman"],
         "Otonom araçların yayaları tanıma derin öğrenme katmanları görselleştirilir.",
         "Derin öğrenme modellerinin geleneksel algoritmalardan en büyük üstünlüğü nedir?",
         "Büyük miktarda veriden özellikleri (örüntüleri) insan müdahalesi olmadan kendi kendine çıkarabilmesidir."),
        
        ("Yapay Zekâ ve Gelecek", "Büyük Dil Modelleri (LLM) ve Üretken Yapay Zekâ", "ChatGPT, Gemini ve Prompt Mühendisliği",
         "Büyük dil modellerinin çalışma mantığını kavrar; doğru ve etkili prompt (komut) yazma kurallarını uygular.",
         ["Üretken Yapay Zekâ (GenAI)", "LLM", "Prompt Mühendisliği", "Halüsinasyon"],
         "Yapay zekâya rol vererek kod açıklatma ve hikaye tamamlama promptları yazılır.",
         "Yapay zekâ modellerine istenen doğru cevabı ürettirmek için verilen yönlendirici girdi metnine ne denir?",
         "Prompt."),
        
        ("Ara Tatil", "2. Dönem Ara Tatil Kampı", "Python ve Yapay Zekâ Kampı",
         "Python fonksiyonları ve yapay zekâ prompt mühendisliği üzerine pratik çalışması yapar.",
         ["Ara Tatil", "Yapay Zekâ Kampı", "Prompt", "Tekrar"],
         "Yapay zekâ destekli mini kodlama projesi tamamlanır.",
         "Yapay zekânın gerçekte olmayan uydurma bilgileri kesinmiş gibi üretmesine ne ad verilir?",
         "Halüsinasyon (Hallucination)."),
        
        ("Yapay Zekâ ve Gelecek", "Bilgisayarlı Görü ve Görüntü İşleme", "OpenCV Temelleri, Pikseller ve Yüz Algılama",
         "Görüntülerin piksel matrislerinden oluştuğunu; renk kanallarını (RGB) ve yüz tespitini öğrenir.",
         ["Bilgisayarlı Görü (Computer Vision)", "Piksel", "RGB", "OpenCV"],
         "Web kamerasından gerçek zamanlı yüz çevreleme demosu çalıştırılır.",
         "Dijital bir renkli fotoğrafta her piksel hangi üç temel renk kanalının karışımından oluşur?",
         "Kırmızı, Yeşil ve Mavi (RGB - Red, Green, Blue)."),
        
        ("Yapay Zekâ ve Gelecek", "Yapay Zekâ Etiği ve Güvenlik", "Önyargı (Bias), Telif Hakları ve Deepfake Tehlikesi",
         "Yapay zekâ modellerindeki önyargıları (bias), sahte ses ve video (deepfake) manipülasyonlarını analiz eder.",
         ["Yapay Zekâ Etiği", "Deepfake", "Önyargı (Bias)", "Doğrulama"],
         "Gerçek ve deepfake videoları ayırt etme analizi yapılır.",
         "Gerçek bir insanın yüz ve sesini yapay zekâ ile taklit ederek sahte içerik üretilmesine ne ad verilir?",
         "Deepfake."),

        # Ünite 6: Siber Güvenlik, Veri Tabanı ve Gelecek (29-36)
        ("Siber Güvenlik ve Gelecek", "Veri Tabanı Temelleri (SQL)", "Tablolar, Kayıtlar ve Temel Sorgular (SELECT, WHERE)",
         "Büyük verilerin saklandığı veritabanı mantığını ve temel SQL sorgulama komutlarını tanır.",
         ["Veri Tabanı", "SQL", "Tablo", "SELECT", "WHERE"],
         "Öğrenci bilgi sistemi veritabanında sorgu çalıştırma alıştırması.",
         "Veritabanından belirli kriterlere göre veri çekmek için hangi SQL komutu kullanılır?",
         "`SELECT ... FROM ... WHERE ...` komutu kullanılır."),
        
        ("Siber Güvenlik ve Gelecek", "Siber Saldırılar ve Tehditler", "DDoS, Ransomware, Man-in-the-Middle ve Zero-Day",
         "Dünya genelinde gerçekleşen siber savaş taktiklerini ve büyük şirketlere yapılan fidye saldırılarını inceler.",
         ["DDoS Saldırısı", "Ransomware", "Sıfır Gün (Zero-Day)", "Siber Tehdit"],
         "Canlı küresel siber saldırı haritası (Cyber Threat Map) incelenir.",
         "Yüz binlerce bilgisayarla bir web sitesine aynı anda istek gönderip sistemi kilitleyen saldırı türü nedir?",
         "DDoS (Dağıtık Hizmet Engelleme) saldırısı."),
        
        ("Siber Güvenlik ve Gelecek", "Beyaz Şapkalı Hackerlık ve Sızma Testi", "Etik Hackerlık, Güvenlik Açığı Tespiti ve Raporlama",
         "Sistemleri korumak için saldıran beyaz şapkalı etik hackerların yöntemlerini ve yasal çerçeveyi öğrenir.",
         ["Beyaz Şapkalı Hacker", "Sızma Testi (Pentest)", "Etik Güvenlik", "Açık Avcılığı"],
         "Zafiyet tarama araçlarının mantığı açıklanır.",
         "Kurumların güvenlik açıklarını bulup zarar vermeden raporlayan iyi niyetli siber güvenlik uzmanına ne denir?",
         "Beyaz Şapkalı Hacker (White Hat Hacker)."),
        
        ("Siber Güvenlik ve Gelecek", "Kişisel Verilerin Korunması Kanunu (KVKK)", "Gizlilik Hakları ve Dijital İtibar",
         "KVKK kapsamında kişisel verilerin korunmasını, veri ihlallerinde şikayet mekanizmalarını kavrar.",
         ["KVKK", "Kişisel Veri", "Aydınlatma Metni", "Açık Rıza"],
         "Uygulamaların telefonumuzda istediği aşırı izinler (rehber, konum) denetlenir.",
         "Kişisel Verilerin Korunması Kanunu (KVKK) bireylere hangi temel hakkı güvence eder?",
         "Kişisel verilerinin izinsiz toplanmasını, işlenmesini ve üçüncü şahıslara aktarılmasını engelleme hakkını güvence eder."),
        
        ("Siber Güvenlik ve Gelecek", "Web Geliştirme Temelleri: HTML ve CSS", "Etiketler (<h1>, <p>, <a>) ve Stil Düzenleme",
         "İnternet sayfalarının iskeletini oluşturan HTML etiketlerini ve CSS renk/yazı biçimlendirmelerini öğrenir.",
         ["HTML", "CSS", "Web Sitesi", "Etiket (Tag)"],
         "Kişisel portfolyo web sayfası kodlanır.",
         "Bir web sayfasına tıklanabilir köprü bağlantısı (link) eklemek için hangi HTML etiketi kullanılır?",
         "`<a href=\"url\">Link Metni</a>` etiketi kullanılır."),
        
        ("Siber Güvenlik ve Gelecek", "Geleceğin Bilişim Dünyası ve Kariyer", "Bilişimle Geleceği Şekillendirme",
         "Yazılım ve yapay zekânın tıp, uzay araştırmaları ve savunma sanayiindeki devrimci rolünü değerlendirir.",
         ["Milli Teknoloji Hamlesi", "Yazılım Vizyonu", "Kariyer", "Bilişim"],
         "Türkiye'nin teknoloji başarıları (İHA/SİHA yazılımları, Togg, TÜRKSAT) incelenir.",
         "Yazılım ve bilişim okuryazarlığının 21. yüzyıl gencine kazandırdığı en büyük ayrıcalık nedir?",
         "Geleceği pasif bir tüketici olarak izlemek yerine, algoritmalar ve kodla geleceğe yön verme yeteneğidir."),
        
        ("Siber Güvenlik ve Gelecek", "8. Sınıf Python ve Bilişim Final Projesi", "Yıl Sonu Yazılım Portfolyo Sergisi",
         "Öğrenciler dönem boyunca geliştirdikleri Python konsol programlarını veya web sayfalarını sergiler.",
         ["Yıl Sonu Sergisi", "Python Projesi", "Portfolyo", "Kod Sergisi"],
         "Sınıfta tüm projelerin canlı sunumu ve kod incelemesi yapılır.",
         "Bir yazılım geliştiricinin yazdığı kodları dünyayla paylaştığı en popüler açık kaynak platformu hangisidir?",
         "GitHub."),
        
        ("Siber Güvenlik ve Gelecek", "Ortaokul Bilişim Mezuniyeti ve LGS Başarı Dilekleri", "Geleceğin Mühendislerine Veda",
         "Ortaokul 4 yıllık bilişim serüvenini algoritma, etik, donanım, robotik ve Python yetkinliğiyle tamamlar.",
         ["Mezuniyet", "Geleceğin Mühendisleri", "LGS Başarı", "Veda"],
         "Öğrencilere 'Genç Bilişim Lideri Onur Sertifikası' takdim edilir.",
         "Ortaokul Bilişim Teknolojileri ve Yazılım dersinden mezun olan bir gencin temel felsefesi ne olmalıdır?",
         "Sürekli öğrenen, ahlaklı, üreten, ülkesine ve insanlığa faydalı teknolojiler geliştiren bir dünya vatandaşı olmaktır.")
    ]
    assert len(u) == 36, f"Bil 8 count: {len(u)}"
    return {
        'title': '8. Sınıf',
        'subtitle': 'Metin Tabanlı Kodlama (Python), Yapay Zekâ & Siber Güvenlik',
        'badge': 'Ortaokul Bilişim',
        'weeks': _make_weeks(u, 'BİL.8')
    }

print("Loading grades for Bilişim...")
g5 = get_bil_5()
g6 = get_bil_6()
g7 = get_bil_7()
g8 = get_bil_8()

print(f"Week counts: G5={len(g5['weeks'])}, G6={len(g6['weeks'])}, G7={len(g7['weeks'])}, G8={len(g8['weeks'])}")

grades_data = {
    5: g5,
    6: g6,
    7: g7,
    8: g8,
}

output_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'lib', 'data', 'subjects', 'bilisim_data.dart'
)

generate_dart_file(
    subject_id='bilisim',
    subject_name='Bilişim Teknolojileri',
    short_code='BİL',
    description='Bilişim Okuryazarlığı, Dijital Vatandaşlık, Algoritma, Robotik, Python ve Yapay Zekâ',
    icon_name='terminal_rounded',
    primary_hex='0xFF7C3AED', # Violet
    accent_hex='0xFF8B5CF6',
    grades_data=grades_data,
    output_path=output_path
)

print("Bilişim Teknolojileri generated successfully!")
