# -*- coding: utf-8 -*-
"""
Generates 36 weeks for all grades (5, 6, 7, 8) in Fen Bilimleri.
"""
import os
import sys

# Add scratch to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from curriculum_builder import generate_dart_file, DATES
from generate_fen_data import build_fen_5

def build_fen_6():
    # 6. Sınıf Fen Bilimleri MEB Müfredatı
    # Üniteler:
    # 1. Güneş Sistemi ve Tutulmalar (1-5)
    # 2. Vücudumuzdaki Sistemler (6-12)
    # 3. Kuvvet ve Hareket (13-17)
    # 4. Madde ve Isı (18-23)
    # 5. Ses ve Özellikleri (24-28)
    # 6. Vücudumuzdaki Sistemler ve Sağlığı (29-33)
    # 7. Elektriğin İletimi (34-36)
    weeks = [
        # 1-5: Güneş Sistemi ve Tutulmalar
        {
            'theme': 'Güneş Sistemi ve Tutulmalar', 'subTheme': 'Güneş Sistemi Gezegenleri',
            'code': 'FEN.6.1.1', 'title': 'Güneş Sistemindeki Gezegenlerin Sıralanışı ve Karasal-Gazsal Gezegenler',
            'description': 'Gezegenleri Güneşe yakınlıklarına göre (Merkür, Venüs, Dünya, Mars, Jüpiter, Satürn, Uranüs, Neptün) sıralar; iç ve dış gezegenleri ayırt eder.',
            'process': ['a) Merkür, Venüs, Dünya ve Marsın iç (karasal) gezegen olduğunu öğrenir.', 'b) Jüpiter, Satürn, Uranüs ve Neptünün dış (gazsal) gezegen olduğunu açıklar.'],
            'concepts': ['Güneş Sistemi', 'İç Gezegen', 'Dış Gezegen', 'Karasal', 'Gazsal'],
            'skills': ['Sınıflandırma', 'Model Analizi'], 'pedagogical': 'Gezegen sıralaması için akılda kalıcı tekerlemeler kullanılır.',
            'context': 'Astronomi Müzesi', 'question': 'Güneş sisteminin en büyük gezegeni hangisidir ve iç gezegen midir yoksa dış gezegen midir?',
            'solution': 'Jüpiterdir ve gazsal yapılı bir dış gezegendir.', 'weeklyGoal': 'Gezegenleri özelliklerine göre sınıflandırma.',
            'evaluation': 'Gezegenler bilgi kartı etkinliği'
        },
        {
            'theme': 'Güneş Sistemi ve Tutulmalar', 'subTheme': 'Asteroit, Meteor ve Gök Taşı',
            'code': 'FEN.6.1.1', 'title': 'Asteroit Kuşağı ve Meteorlar ile Gök Taşlarının Farkı',
            'description': 'Mars ve Jüpiter arasındaki asteroit kuşağını; atmosfere girip yanan meteor (yıldız kayması) ile yeryüzüne ulaşan gök taşını (meteorit) ayırt eder.',
            'process': ['a) Asteroit kuşağının konumunu gösterir.', 'b) Meteor çukuru ile krater kavramlarını karşılaştırır.'],
            'concepts': ['Asteroit Kuşağı', 'Meteor', 'Gök Taşı', 'Meteorit', 'Yıldız Kayması'],
            'skills': ['Kavram Karşılaştırma', 'Gözlemsel Çıkarım'], 'pedagogical': 'Halk arasında yıldız kayması denilen olayın gerçekte bir yıldızla ilgisi olmadığı anlatılır.',
            'context': 'Doğal Afetler ve Uzay', 'question': 'Gökyüzünde ışık çizgisi bırakarak yanan gök cisimlerine halk arasında ne ad verilir ve bilimsel adı nedir?',
            'solution': 'Halk arasında yıldız kayması denir; bilimsel adı atmosfere girip sürtünmeyle yanan meteordur.', 'weeklyGoal': 'Asteroit ve meteor arasındaki farkları açıklama.',
            'evaluation': 'Meteor vs Gök Taşı Venn şeması'
        },
        {
            'theme': 'Güneş Sistemi ve Tutulmalar', 'subTheme': 'Güneş Tutulması',
            'code': 'FEN.6.1.2', 'title': 'Güneş Tutulmasının Oluşumu ve Ayın Yeni Ay Evresi',
            'description': 'Ayın Dünya ile Güneş arasına girmesiyle oluşan Güneş tutulmasını modeller; Ayın Yeni Ay evresinde olduğunu ve gündüz vakti gerçekleştiğini açıklar.',
            'process': ['a) Tam gölge ve yarı gölge alanlarını modeller.', 'b) Güneş tutulmasının her yeni ay evresinde gerçekleşmeme nedenini yörünge eğikliğiyle açıklar.'],
            'concepts': ['Güneş Tutulması', 'Yeni Ay Evresi', 'Tam Gölge', 'Işığın Doğrusallığı'],
            'skills': ['Optik Modelleme', 'Bilimsel Argüman'], 'pedagogical': 'Karanlık odada pinpon topu ve fenerle gölge düşürülür.',
            'context': 'Gözlemevi Takvimi', 'question': 'Güneş tutulması Ay hangi evredeyken gerçekleşir ve Dünya üzerinde neden yalnızca dar bir alandan izlenebilir?',
            'solution': 'Yeni Ay evresinde gerçekleşir. Ay Dünya\'dan çok küçük olduğu için gölgesi Dünya yüzeyinde dar bir şeride düşer.', 'weeklyGoal': 'Güneş tutulması mekanizmasını şematize etme.',
            'evaluation': 'Güneş tutulması deney raporu'
        },
        {
            'theme': 'Güneş Sistemi ve Tutulmalar', 'subTheme': 'Ay Tutulması',
            'code': 'FEN.6.1.2', 'title': 'Ay Tutulmasının Oluşumu ve Ayın Dolunay Evresi',
            'description': 'Dünyanın Güneş ile Ay arasına girmesiyle Dünyanın gölgesinin Ay üzerine düşmesini modeller; Dolunay evresinde ve gece gerçekleştiğini açıklar.',
            'process': ['a) Dünyanın gölge konisini çizer.', 'b) Ay tutulmasının gece olan her yerden çıplak gözle izlenebildiğini doğrular.'],
            'concepts': ['Ay Tutulması', 'Dolunay Evresi', 'Dünyanın Gölgesi', 'Kızıl Ay'],
            'skills': ['Uzamsal Muhakeme', 'Döngüsel Olaylar'], 'pedagogical': 'Ay tutulmasında özel gözlük gerekmediği, çıplak gözle izlenebileceği vurgulanır.',
            'context': 'Gece Gökyüzü', 'question': 'Ay tutulması Ayın hangi evresinde gerçekleşir ve Güneş tutulmasından süre olarak neden daha uzun sürer?',
            'solution': 'Dolunay evresinde gerçekleşir. Dünyanın gölgesi çok geniş olduğu için Ayın bu gölgeden çıkması birkaç saat sürebilir.', 'weeklyGoal': 'Ay tutulmasını Güneş tutulmasıyla karşılaştırma.',
            'evaluation': 'Tutulmalar karşılaştırma tablosu'
        },
        {
            'theme': 'Güneş Sistemi ve Tutulmalar', 'subTheme': 'Ünite Değerlendirme ve Modelleme',
            'code': 'FEN.6.1.3', 'title': 'Güneş Sistemi ve Tutulmalar Portfolyo Değerlendirmesi',
            'description': 'Güneş sistemi maketi ve tutulma düzeneklerini içeren proje sunumları yapar; kavram yanılgılarını giderir.',
            'process': ['a) Çoktan seçmeli ve açık uçlu soruları çözer.', 'b) Model sunumunu gerçekleştirir.'],
            'concepts': ['Gökbilim', 'Ölçekli Model', 'Genel Tekrar'],
            'skills': ['İletişim', 'Öz Değerlendirme'], 'pedagogical': 'Akran değerlendirme formları kullanılır.',
            'context': 'Bilim Sergisi', 'question': 'Güneş ve Ay tutulmalarının ortak özelliği ışığın hangi temel davranışını kanıtlamalarıdır?',
            'solution': 'Işığın doğrusal yolla yayıldığını ve opak cisimlerin arkasında tam gölge oluşturduğunu kanıtlar.', 'weeklyGoal': '1. Ünite kazanımlarını sentezleme.',
            'evaluation': '1. Ünite Ölçme Sınavı'
        },

        # 6-12: Vücudumuzdaki Sistemler
        {
            'theme': 'Vücudumuzdaki Sistemler', 'subTheme': 'Destek ve Hareket Sistemi',
            'code': 'FEN.6.2.1', 'title': 'Kemik Çeşitleri, Eklemler ve Kaslar',
            'description': 'Uzun, kısa, yassı kemikleri; oynar, yarı oynar, oynamaz eklemleri ve çizgili, düz, kalp kası dokularını çalışma prensipleriyle açıklar.',
            'process': ['a) Kırmızı kemik iliğinde kan hücresi üretildiğini kavrar.', 'b) Çift çalışan zıt kasların koordinasyonunu modeller.'],
            'concepts': ['Kemik', 'Eklem', 'Kas', 'Kırmızı Kemik İliği', 'Zıt Çalışan Kaslar'],
            'skills': ['Yapı-İşlev Eşleştirme', 'Biyomekanik'], 'pedagogical': 'Kolu bükerken pazu kasının kasılıp arka kasın gevşemesi hissettirilir.',
            'context': 'Spor Hekimliği', 'question': 'Kalp kasının yapı ve çalışma prensibi bakımından diğer kas türleriyle benzerliği nedir?',
            'solution': 'Yapı olarak çizgili kasa (çizgili bantlı görünüm), çalışma prensibi olarak ise düz kasa benzer (istemsiz ve yorulmadan çalışır).', 'weeklyGoal': 'Destek ve hareket sisteminin anatomik yapısını anlama.',
            'evaluation': 'Kas-Eklem modeli etiketleme'
        },
        {
            'theme': 'Vücudumuzdaki Sistemler', 'subTheme': 'Sindirim Sistemi Organları',
            'code': 'FEN.6.2.2', 'title': 'Sindirime Yardımcı Organlar ve Sindirim Kanalı',
            'description': 'Besinlerin ağızdan anüse kadar izlediği yolu (ağız, yutak, yemek borusu, mide, ince bağırsak, kalın bağırsak) ve yardımcı organları (karaciğer, pankreas) şematize eder.',
            'process': ['a) Karaciğerin safra ürettiğini açıklar.', 'b) Pankreas öz suyunun tüm besin gruplarını sindirdiğini belirtir.'],
            'concepts': ['Sindirim Kanalı', 'Karaciğer', 'Safra', 'Pankreas Öz Suyu', 'Villus'],
            'skills': ['Süreç Akış Şeması', 'Organ Eşleştirme'], 'pedagogical': 'Sindirim kanalı uzunluğu (yaklaşık 8-9 metre) iplerle sınıfta gösterilir.',
            'context': 'Beslenme ve Sağlık', 'question': 'Yağların mekanik (fiziksel) sindirimini kolaylaştıran safra sıvısını hangi organ üretir ve nerede depolar?',
            'solution': 'Karaciğer üretir ve safra kesesinde depolar; ince bağırsağa salgılar.', 'weeklyGoal': 'Sindirim sistemi organlarını sırasıyla tanıma.',
            'evaluation': 'Sindirim kanalı organ haritası'
        },
        {
            'theme': 'Vücudumuzdaki Sistemler', 'subTheme': 'Mekanik ve Kimyasal Sindirim',
            'code': 'FEN.6.2.2', 'title': 'Besin İçeriklerinin Kimyasal Sindiriminin Başladığı ve Bittiği Yerler',
            'description': 'Karbonhidrat, protein ve yağların mekanik sindirimi ile enzimler yardımıyla kimyasal sindiriminin gerçekleştiği organları tablolandırır.',
            'process': ['a) Karbonhidratların ağızda başlayıp ince bağırsakta bittiğini modeller.', 'b) Proteinlerin midede başlayıp ince bağırsakta bittiğini; yağların ise ince bağırsakta başlayıp bittiğini kavrar.'],
            'concepts': ['Mekanik Sindirim', 'Kimyasal Sindirim', 'Enzim', 'Emilim (Absorpsiyon)'],
            'skills': ['Tablo Yorumlama', 'Kritik Düşünme'], 'pedagogical': 'Küp şeker ile toz şekerin suda çözünme hızıyla yüzey alanı analojisi yapılır.',
            'context': 'Biyokimya', 'question': 'Proteinlerin kimyasal sindirimi hangi organda başlar ve hangi enzimli sıvıyla devam eder?',
            'solution': 'Midede mide öz suyu (pepsin enzimi) ile başlar ve ince bağırsakta tamamlanır.', 'weeklyGoal': 'Kimyasal sindirim basamaklarını eksiksiz öğrenme.',
            'evaluation': 'Sindirim matrisi doldurma'
        },
        {
            'theme': 'Vücudumuzdaki Sistemler', 'subTheme': 'Dolaşım Sistemi (Kalp ve Damarlar)',
            'code': 'FEN.6.2.3', 'title': 'Kalbin Yapısı, Odacıkları ve Damar Çeşitleri (Atardamar, Toplardamar, Kılcaldamar)',
            'description': 'Kalbin dört odacığını (kulakçık ve karıncıklar); kanı kalpten götüren atardamarları, getiren toplardamarları ve madde alışverişini sağlayan kılcaldamarları açıklar.',
            'process': ['a) Kalbin sol tarafında temiz (oksijence zengin), sağ tarafında kirli kan olduğunu modeller.', 'b) Kapakçıkların tek yönlü açıldığını kavrar.'],
            'concepts': ['Kalp', 'Kulakçık', 'Karıncık', 'Atardamar', 'Toplardamar', 'Kılcaldamar'],
            'skills': ['Model Çözümleme', 'Fizyolojik Düşünme'], 'pedagogical': 'Koyun kalbi diseksiyonu veya 3D kalp modeli üzerinden odacıklar gösterilir.',
            'context': 'Kardiyoloji', 'question': 'Vücuttaki doku ve hücrelerle doğrudan madde ve gaz alışverişinin gerçekleştiği damar türü hangisidir?',
            'solution': 'Tek katlı epitel dokudan oluşan kılcal damarlardır.', 'weeklyGoal': 'Kalbin bölümlerini ve damar fonksiyonlarını kavrama.',
            'evaluation': 'Kalp anatomisi şeması çizimi'
        },
        {
            'theme': 'Ara Tatil', 'subTheme': '1. Dönem Ara Tatili',
            'code': 'FEN.6.GENEL.1', 'title': 'Güneş Sistemi ve Dolaşım Sistemi Tekrarı',
            'description': 'Tutulmalar, gezegenler ve vücut sistemleri konularında yeni nesil sorular çözülür.',
            'process': ['a) Soru çözme tekniklerini pekiştirir.'],
            'concepts': ['Genel Tekrar', 'LGS Temeli'], 'skills': ['Problem Çözme'],
            'pedagogical': 'Tatil fasikülü kontrol edilir.', 'context': 'Tatil Çalışması',
            'question': 'Küçük kan dolaşımının temel amacı nedir?',
            'solution': 'Kirli kanı akciğere götürüp oksijence zenginleştirerek (temizleyerek) kalbe geri getirmektir.',
            'weeklyGoal': 'İlk 9 haftayı pekiştirme.', 'evaluation': 'Ara tatil soru föyü'
        },
        {
            'theme': 'Vücudumuzdaki Sistemler', 'subTheme': 'Büyük ve Küçük Kan Dolaşımı',
            'code': 'FEN.6.2.3', 'title': 'Büyük Kan Dolaşımı ile Küçük Kan Dolaşımının Karşılaştırılması',
            'description': 'Küçük dolaşımın kanı akciğerde temizleme; büyük dolaşımın temiz kanı tüm vücuda dağıtıp kirli kanı toplama döngüsünü modeller.',
            'process': ['a) Küçük dolaşımın sağ karıncıkta başlayıp sol kulakçıkta bittiğini gösterir.', 'b) Büyük dolaşımın sol karıncıkta başlayıp sağ kulakçıkta bittiğini kavrar.'],
            'concepts': ['Küçük Kan Dolaşımı', 'Büyük Kan Dolaşımı', 'Aort', 'Akciğer Atardamarı', 'Temiz/Kirli Kan'],
            'skills': ['Döngü Şemalaştırma', 'Sistemik Muhakeme'], 'pedagogical': 'Mavi (kirli kan) ve kırmızı (temiz kan) iplerle dolaşım rotası sınıfta canlandırılır.',
            'context': 'Fizyoloji Laboratuvarı', 'question': 'Normalde atardamarlar temiz kan taşırken istisna olarak kirli kan taşıyan tek atardamar hangisidir?',
            'solution': 'Kalbin sağ karıncığından akciğere kirli kan götüren akciğer atardamarıdır.', 'weeklyGoal': 'Dolaşım yollarını sırasıyla takip edebilme.',
            'evaluation': 'Dolaşım döngüsü haritası tamamlama'
        },
        {
            'theme': 'Vücudumuzdaki Sistemler', 'subTheme': 'Kan Grupları ve Kan Bağışı',
            'code': 'FEN.6.2.4', 'title': 'Kan Hücreleri (Alyuvar, Akyuvar, Kan Pulcukları) ve Kan Bağışının Önemi',
            'description': 'Oksijen taşıyan alyuvarları, mikroplarla savaşan akyuvarları, kanı pıhtılaştıran pulcukları; A, B, AB, 0 kan grupları ve Kızılayın kan bağışı bilincini değerlendirir.',
            'process': ['a) Rh faktörünü açıklar.', 'b) Toplumsal dayanışma için kan bağışının hayati önemini kavrar.'],
            'concepts': ['Alyuvar', 'Akyuvar', 'Kan Pulcukları', 'Kan Grubu', 'Rh Faktörü', 'Kan Bağışı (Kızılay)'],
            'skills': ['Toplumsal Duyarlılık', 'Biyolojik Bilinç'], 'pedagogical': 'Kızılay kan bağışı tırı ziyareti veya simülasyonu yapılır.',
            'context': 'Kızılay ve Toplum Sağlığı', 'question': 'Vücuda mikrop girdiğinde sayısı hızla artarak savunma antikorları üreten kan hücresi hangisidir?',
            'solution': 'Akyuvarlardır (lökositler).', 'weeklyGoal': 'Kan bileşenlerini ve kan bağışının önemini savunma.',
            'evaluation': 'Kan bağışı bilgilendirme broşürü'
        },

        # 13-17: Kuvvet ve Hareket
        {
            'theme': 'Kuvvet ve Hareket', 'subTheme': 'Bileşke Kuvvet (Net Kuvvet)',
            'code': 'FEN.6.3.1', 'title': 'Aynı Doğrultulu Kuvvetlerin Bileşkesinin Hesaplanması',
            'description': 'Aynı yönlü kuvvetlerin toplanarak, zıt yönlü kuvvetlerin çıkarılarak bileşke kuvvetin (R veya Fnet) yön, doğrultu ve büyüklüğünü hesaplar.',
            'process': ['a) Doğrultu ile yön farkını kavrar.', 'b) Halat çekme oyununda kuvvet dengesini modeller.'],
            'concepts': ['Bileşke Kuvvet (R)', 'Aynı Yönlü Kuvvetler', 'Zıt Yönlü Kuvvetler', 'Doğrultu', 'Yön'],
            'skills': ['Vektörel Düşünme', 'Sayısal Hesaplama'], 'pedagogical': 'Öğrenciler karşılıklı masayı iterek kuvvet bileşkelerini oluştururlar.',
            'context': 'Halat Çekme Yarışması', 'question': 'Doğuya doğru 15 N ve 25 N çeken iki kuvvete zıt yönde (batıya) 10 N kuvvet uygulanırsa bileşke kuvvet ne olur?',
            'solution': 'Doğu: 15+25 = 40 N. Batı: 10 N. Bileşke = 40 - 10 = Doğu yönünde 30 Newton.', 'weeklyGoal': 'Bileşke kuvveti matematiksel ve yönsel bulma.',
            'evaluation': 'Bileşke kuvvet çalışma kağıdı'
        },
        {
            'theme': 'Kuvvet ve Hareket', 'subTheme': 'Dengelenmiş ve Dengelenmemiş Kuvvetler',
            'code': 'FEN.6.3.1', 'title': 'Dengelenmiş ve Dengelenmemiş Kuvvetlerin Cisimlerin Hareketine Etkisi',
            'description': 'Bileşke kuvvet sıfır ise cismin dengelenmiş kuvvetler etkisinde olduğunu (duruyorsa durur, hareket halindeyse sabit süratle gider); sıfırdan farklıysa hızlanan veya yavaşlayan hareket yaptığını açıklar.',
            'process': ['a) Masada duran kitabın dengelenmiş kuvvet etkisinde olduğunu belirtir.', 'b) Fren yapan arabanın dengelenmemiş kuvvet etkisinde olduğunu kavrar.'],
            'concepts': ['Dengelenmiş Kuvvetler (R=0)', 'Dengelenmemiş Kuvvetler (R≠0)', 'Sabit Sürat', 'Hızlanma / Yavaşlama'],
            'skills': ['Fiziksel Durum Analizi', 'Çıkarım Yapma'], 'pedagogical': 'Paraşütçünün limit hıza ulaştığında sabit süratle inmesi dengelenmiş kuvvetle açıklanır.',
            'context': 'Trafik Güvenliği', 'question': 'Sabit süratle 90 km/sa hızla düz yolda giden bir otomobil dengelenmiş mi yoksa dengelenmemiş kuvvetler etkisindedir?',
            'solution': 'Sürati ve yönü değişmediği için bileşke kuvvet sıfırdır, yani dengelenmiş kuvvetler etkisindedir.', 'weeklyGoal': 'Cismin hareket durumuna bakarak kuvvet dengesini saptama.',
            'evaluation': 'Hareket durumu sınıflandırma testi'
        },
        {
            'theme': 'Kuvvet ve Hareket', 'subTheme': 'Sabit Süratli Hareket',
            'code': 'FEN.6.3.2', 'title': 'Sürat Kavramı ve Yol - Zaman İlişkisi (Sürat = Yol / Zaman)',
            'description': 'Eşit zaman aralıklarında eşit yollar alan cismin sabit süratli hareket yaptığını; Sürat = Alınan Yol / Geçen Zaman formülüyle hesaplar.',
            'process': ['a) Birimlerini (m/s ve km/sa) birbirine dönüştürme mantığını kavrar.', 'b) Sürat üçgenini (Yol = Sürat x Zaman) kullanır.'],
            'concepts': ['Sürat', 'Alınan Yol', 'Zaman', 'm/s', 'km/sa'],
            'skills': ['Formül Uygulama', 'Oran-Orantı Kurma'], 'pedagogical': 'Kronometre ve mezura ile okul bahçesinde koşan öğrencilerin süratleri hesaplanır.',
            'context': 'Hızlı Tren Yolculuğu', 'question': '400 metrelik pisti 50 saniyede sabit süratle koşan bir atletin sürati kaç m/s\'dir?',
            'solution': 'Sürat = Yol / Zaman = 400 m / 50 s = 8 m/s.', 'weeklyGoal': 'Sabit sürat hesaplamalarını doğru yapabilme.',
            'evaluation': 'Sürat hesaplama problemleri'
        },
        {
            'theme': 'Kuvvet ve Hareket', 'subTheme': 'Yol - Zaman Grafikleri',
            'code': 'FEN.6.3.2', 'title': 'Yol-Zaman ve Sürat-Zaman Grafiklerinin Çizimi ve Yorumlanması',
            'description': 'Verilen tablodan yararlanarak yol-zaman grafiği çizer; grafiğin eğiminin sürati verdiğini keşfeder.',
            'process': ['a) Düzgün artan yol-zaman grafiğinin sabit sürati temsil ettiğini kavrar.', 'b) Sürat-zaman grafiğinde çizginin yatay olduğunu gösterir.'],
            'concepts': ['Yol-Zaman Grafiği', 'Sürat-Zaman Grafiği', 'Grafik Eğimi', 'Grafik Okuma'],
            'skills': ['Grafik Çizme', 'Veri Görselleştirme'], 'pedagogical': 'Kareli kâğıt üzerinde nokta birleştirilerek koordinat ekseninde grafik çizilir.',
            'context': 'Radar ve Trafik Kontrolü', 'question': 'Yol-zaman grafiğinde zaman geçtikçe yol değeri hiç değişmeyen (yatay bir çizgi olan) bir cismin hareketi için ne söylenebilir?',
            'solution': 'Cismin durduğu (hareketsiz olduğu) ve süratinin 0 m/s olduğu söylenir.', 'weeklyGoal': 'Hareket grafiklerini hatasız çizme ve yorumlama.',
            'evaluation': 'Grafik çizim ve yorumlama ödevi'
        },
        {
            'theme': 'Kuvvet ve Hareket', 'subTheme': 'Kuvvet ve Hareket Ünite Değerlendirme',
            'code': 'FEN.6.3.3', 'title': 'Kuvvet ve Hareket Becerileri Dönem Sonu Sentezi',
            'description': 'Bileşke kuvvet, dengelenmiş kuvvet ve sürat grafiklerini içeren problem durumları çözülür; 1. dönem genel değerlendirmesi yapılır.',
            'process': ['a) Kapsamlı deneme sınavını uygular.', 'b) Geri bildirimlerle eksiklerini tamamlar.'],
            'concepts': ['Dönem Tekrarı', 'Sentez', 'Öz Değerlendirme'],
            'skills': ['Analitik Sentez'], 'pedagogical': 'Dönem sonu başarı belgesi ve portfolyo sunumu.',
            'context': '1. Dönem Finali', 'question': 'Bir cismin dengelenmiş kuvvetler etkisinde olması için üzerindeki kuvvetlerin toplamı kaç N olmalıdır?',
            'solution': '0 Newton (bileşke kuvvet sıfır) olmalıdır.', 'weeklyGoal': '1. dönem fizik konularını pekiştirme.',
            'evaluation': '1. Dönem Fen Bilimleri Karnesi Öncesi Sınav'
        },

        # 18-23: Madde ve Isı
        {
            'theme': 'Madde ve Isı', 'subTheme': 'Maddenin Tanecikli Yapısı ve Hâlleri',
            'code': 'FEN.6.4.1', 'title': 'Maddenin Katı, Sıvı ve Gaz Hâllerinde Tanecik Boşlukları ve Hareketleri',
            'description': 'Maddenin tanecikli yapısının sıcaklıkla değişimini, katıda yalnız titreşim, sıvı ve gazda titreşim, öteleme ve dönme hareketlerini açıklar.',
            'process': ['a) Sıvıların sıkıştırılamaz kabul edildiğini öğrenir.', 'b) Gazların sıkıştırılabilme özelliğinden yararlanılan teknolojileri (LPG, yangın tüpü) örnekler.'],
            'concepts': ['Tanecik', 'Titreşim', 'Öteleme', 'Dönme', 'Sıkıştırılabilirlik'],
            'skills': ['Moleküler Modelleme', 'Görselleştirme'], 'pedagogical': 'Şırınga içine su ve hava çekilip piston itilerek sıkışma farkı test edilir.',
            'context': 'Basınçlı Gaz Teknolojileri', 'question': 'Şırınganın ağzı parmakla kapatıldığında hava kolayca sıkışırken suyun sıkışmamasının sebebi nedir?',
            'solution': 'Gaz tanecikleri arasında çok büyük boşluklar varken, sıvı tanecikleri arasındaki boşluğun yok denecek kadar az olmasıdır.', 'weeklyGoal': 'Maddenin tanecik özelliklerini sıkışabilirlikle ilişkilendirme.',
            'evaluation': 'Tanecik sıkışabilirlik deney formu'
        },
        {
            'theme': 'Madde ve Isı', 'subTheme': 'Yoğunluk (Özkütle) Kavramı',
            'code': 'FEN.6.4.2', 'title': 'Yoğunluğun Tanımı, Formülü ve Birimi (d = m / V)',
            'description': 'Yoğunluğun birim hacimdeki kütle olduğunu kavrar; kütleyi teraziyle, hacmi dereceli silindirle ölçerek d = m / V formülüyle yoğunluğu hesaplar.',
            'process': ['a) Yoğunluğun saf maddeler için ayırt edici özellik olduğunu öğrenir.', 'b) Biriminin g/cm³ olduğunu kullanır.'],
            'concepts': ['Yoğunluk (d)', 'Kütle (m)', 'Hacim (V)', 'Ayırt Edici Özellik', 'g/cm³'],
            'skills': ['Laboratuvar Ölçümü', 'Matematiksel Modelleme'], 'pedagogical': 'Dereceli silindire taş atılarak taşın taşırdığı su hacmi ölçülür.',
            'context': 'Kuyumculuk ve Madencilik', 'question': 'Kütlesi 120 gram olan bir taş parçası dereceli silindire atıldığında su seviyesi 50 mL\'den 90 mL\'ye çıkıyorsa taşın yoğunluğu kaç g/cm³ tür?',
            'solution': 'Hacim = 90 - 50 = 40 cm³. Yoğunluk d = m / V = 120 g / 40 cm³ = 3 g/cm³.', 'weeklyGoal': 'Yoğunluk hesaplamalarını deneysel verilerle yapma.',
            'evaluation': 'Yoğunluk bulma laboratuvar föyü'
        },
        {
            'theme': 'Madde ve Isı', 'subTheme': 'Birbiri İçinde Çözünmeyen Sıvılarda Yoğunluk',
            'code': 'FEN.6.4.2', 'title': 'Sıvıların Yoğunluk Kulesi ve Yüzme - Batma Durumları',
            'description': 'Birbirine karışmayan sıvılarda yoğunluğu büyük olanın en altta, küçük olanın en üstte kaldığını deneyle gösterir.',
            'process': ['a) Su ve zeytinyağı karışımında zeytinyağının üste çıkmasını yoğunlukla açıklar.', 'b) Sıvı kulesinde cisimlerin batma seviyelerini analiz eder.'],
            'concepts': ['Yoğunluk Sıralaması', 'Zeytinyağı-Su', 'Yüzme', 'Batma', 'Askıda Kalma'],
            'skills': ['Gözleme Dayalı Sıralama', 'Tahmin ve Test'], 'pedagogical': 'Bal, su, zeytinyağı ve bulaşık deterjanıyla renkli yoğunluk kulesi yapılır.',
            'context': 'Denizcilik ve Gemiler', 'question': 'Birbirine karışmayan X, Y ve Z sıvıları aynı kaba konduğunda en altta X, en üstte Z kalıyorsa yoğunlukları nasıl sıralanır?',
            'solution': 'Yoğunluğu en büyük olan en dipte kalır: dX > dY > dZ.', 'weeklyGoal': 'Sıvıların kaba diziliminden yoğunluklarını kıyaslama.',
            'evaluation': 'Yoğunluk kulesi deneyi'
        },
        {
            'theme': 'Madde ve Isı', 'subTheme': 'Suyun Canlılar İçin Önemi ve Yoğunluğu (+4 °C Özelliği)',
            'code': 'FEN.6.4.2', 'title': 'Buzun Yoğunluğunun Sudan Küçük Olmasının Hayati Önemi',
            'description': 'Maddeler donarken genellikle büzülüp yoğunluğu artarken suyun donarken hacminin genişleyip yoğunluğunun azaldığını (+4 °C anomalisi) ve göllerin üstten donarak su altı yaşamını koruduğunu açıklar.',
            'process': ['a) Buz dağlarının (aysberg) suda yüzmesini yoğunlukla açıklar.', 'b) Göllerin dipten değil üstten donmasının balıkların yaşamasını sağladığını keşfeder.'],
            'concepts': ['Buzun Yoğunluğu', 'Üstten Donma', 'Su Altı Ekosistemi', '+4 °C Kuralı'],
            'skills': ['Ekolojik Farkındalık', 'İstisnai Durumları Yorumlama'], 'pedagogical': 'Dondurucuya ağzına kadar doldurulup konan cam şişenin çatlaması örneği verilir.',
            'context': 'Kutup Gölleri Yaşamı', 'question': 'Kışın hava sıcaklığı -20 °C olduğunda bile donmuş bir gölün altındaki balıkların yaşayabilmesinin fen bilimlerindeki sebebi nedir?',
            'solution': 'Buzun yoğunluğu sudan küçük olduğu için suyun üstünde yüzer; göl yüzeyden donarak alt kısımdaki suyu (+4 °C) yalıtır ve dondurmaz.', 'weeklyGoal': 'Suyun yoğunluk anomalisinin canlılık için önemini kavrama.',
            'evaluation': 'Ekolojik yoğunluk makalesi incelemesi'
        },
        {
            'theme': 'Madde ve Isı', 'subTheme': 'Isı İletkenliği ve Isı Yalıtımı',
            'code': 'FEN.6.4.3', 'title': 'Isı İletkeni ve Isı Yalıtkanı Maddelerin Karşılaştırılması',
            'description': 'Isıyı iyi ileten maddelere ısı iletkeni (metaller); iyi iletmeyen maddelere ısı yalıtkanı (strafor köpük, ahşap, plastik, cam yünü) dendiğini açıklar.',
            'process': ['a) Tencere gövdesinin iletken, sapının yalıtkan malzemeden yapıldığını irdeler.', 'b) Çift camlı pencerelerde iki cam arasındaki havanın yalıtım gücünü kavrar.'],
            'concepts': ['Isı İletkeni', 'Isı Yalıtkanı', 'Strafor Köpük', 'Cam Yünü', 'Taş Yünü'],
            'skills': ['Malzeme Seçimi', 'Ergonomik Tasarım'], 'pedagogical': 'Sıcak suya konulan metal, tahta ve plastik kaşıkların uçlarına margarinle boncuk yapıştırılarak erime yarışı yapılır.',
            'context': 'Mutfak Eşyaları Tasarımı', 'question': 'Çorba karıştırırken metal kaşık yerine tahta kaşık tercih edilmesinin sebebi nedir?',
            'solution': 'Tahta ısı yalıtkanı olduğu için tenceredeki ısıyı elimize hızla iletmez ve elimizin yanmasını önler.', 'weeklyGoal': 'Isı iletkeni ve yalıtkanı malzemeleri kullanım alanlarıyla eşleştirme.',
            'evaluation': 'Isı iletkenliği yarışı deneyi'
        },
        {
            'theme': 'Madde ve Isı', 'subTheme': 'Binalarda Isı Yalıtımı ve Yakıtlar',
            'code': 'FEN.6.4.4', 'title': 'Binalarda Isı Yalıtımının Aile ve Ülke Ekonomisine Katkısı ve Yakıt Türleri',
            'description': 'Binalara yapılan mantolama, çift cam ve çatı yalıtımının enerji tüketimini ve karbon salınımını azalttığını; katı, sıvı ve gaz yakıtların çevreye etkilerini değerlendirir.',
            'process': ['a) Fosil yakıtların hava kirliliğine yol açtığını öğrenir.', 'b) Yenilenebilir temiz enerjinin önemini savunur.'],
            'concepts': ['Mantolama', 'Enerji Tasarrufu', 'Fosil Yakıtlar', 'Yenilenebilir Enerji'],
            'skills': ['Ekonomik ve Çevre Bilinci', 'Sürdürülebilirlik'], 'pedagogical': 'Termal kamera fotoğrafları incelenerek ısı kaçağı olan pencereler tespit edilir.',
            'context': 'Yeşil Binalar ve Tasarruf', 'question': 'Binalarda dış cephe ısı yalıtımı (mantolama) yaptırmanın kış ve yaz aylarındaki çift yönlü faydası nedir?',
            'solution': 'Kışın evin içindeki ısının dışarı kaçmasını önleyerek yakıt tasarrufu sağlar; yazın ise dışarıdaki sıcağın içeri girmesini önleyerek klima masrafını azaltır.', 'weeklyGoal': 'Binalarda ısı yalıtımının önemini gerekçelendirme.',
            'evaluation': 'Yalıtımlı ev maketi projesi'
        },

        # 24-28: Ses ve Özellikleri
        {
            'theme': 'Ses ve Özellikleri', 'subTheme': 'Sesin Yayılması',
            'code': 'FEN.6.5.1', 'title': 'Sesin Katı, Sıvı ve Gaz Ortamlarda Maddesel Yayılması',
            'description': 'Sesin titreşimler sonucu oluştuğunu ve maddesel ortamlarda (katı, sıvı, gaz) dalgalar halinde yayıldığını; boşlukta (uzayda) yayılamadığını açıklar.',
            'process': ['a) Kulağımızı masaya dayadığımızda tıkırtıyı çok net duymamızı sesin katılarda yayılmasıyla açıklar.', 'b) Havası boşaltılmış fanusta çalan çalar saatin sesinin duyulmadığını deneyler.'],
            'concepts': ['Ses Kaynağı', 'Maddesel Ortam', 'Titreşim', 'Uzay Boşluğu'],
            'skills': ['Hipotez Kurma', 'Deneysel Çıkarım'], 'pedagogical': 'İki karton bardak ve iple telefon yapılarak sesin ipte (katıda) iletimi gösterilir.',
            'context': 'Bilim Kurgu Filmleri Analizi', 'question': 'Uzayda gerçekleşen devasa gök taşı çarpışmalarının ve patlamaların Dünya\'dan duyulamamasının bilimsel gerekçesi nedir?',
            'solution': 'Ses dalgalarının yayılabilmesi için maddesel (tanecikli) bir ortama ihtiyaç vardır; uzay boşluk olduğu için ses yayılamaz.', 'weeklyGoal': 'Sesin yayılma ortamlarını kavrama.',
            'evaluation': 'Havasız fanus deneyi raporu'
        },
        {
            'theme': 'Ses ve Özellikleri', 'subTheme': 'Farklı Ortamlarda Sesin Farklı Duyulması',
            'code': 'FEN.6.5.2', 'title': 'Ses Kaynaklarının ve Sesin Yayıldığı Ortamın Sese Etkisi',
            'description': 'Farklı ses kaynaklarının farklı sesler ürettiğini; aynı ses kaynağının farklı ortamlarda (havada, suda) farklı duyulduğunu keşfeder.',
            'process': ['a) İki taşı havada birbirine vurmakla suyun içinde vurmak arasındaki ses farkını dener.', 'b) Müzik aletlerinin ses tonu farklarını (tını) ilişkilendirir.'],
            'concepts': ['Ses Kaynağı', 'Ortam Değişimi', 'Ses Farklılığı', 'Tını'],
            'skills': ['İşitsel Ayrıştırma', 'Karşılaştırmalı Gözlem'], 'pedagogical': 'Metal, porselen ve cam bardaklara kaşıkla vurularak ses farkları dinletilir.',
            'context': 'Müzik ve Enstrümanlar', 'question': 'Aynı flütün havada çalındığında çıkan sesi ile suyun altında çalındığında algılanan sesin farklı olmasının sebebi nedir?',
            'solution': 'Sesin yayıldığı ortamın (hava yerine su) değişmesi ses dalgalarının kulağımıza ulaşma hızını ve titreşim biçimini değiştirir.', 'weeklyGoal': 'Ortamın sesin algılanışına etkisini belirleme.',
            'evaluation': 'Ses tınısı deney formu'
        },
        {
            'theme': 'Ses ve Özellikleri', 'subTheme': 'Sesin Sürati',
            'code': 'FEN.6.5.3', 'title': 'Sesin Katı, Sıvı ve Gazlardaki Süratinin Karşılaştırılması ve Işık Sürati',
            'description': 'Sesin en hızlı katılarda, sonra sıvılarda, en yavaş gazlarda yayıldığını; ışığın süratinin (300.000 km/s) ses süratinden (havada 340 m/s) çok daha büyük olduğunu açıklar.',
            'process': ['a) Şimşek çaktıktan birkaç saniye sonra gök gürültüsünün duyulmasını ışık ve ses hızı farkıyla açıklar.', 'b) Tanecikler ne kadar yakınsa sesin o kadar hızlı aktarıldığını kavrar.'],
            'concepts': ['Ses Sürati', 'v_katı > v_sıvı > v_gaz', 'Işık Sürati', 'Şimşek ve Gök Gürültüsü'],
            'skills': ['Hız Mukayesesi', 'Doğa Olayı Çözümleme'], 'pedagogical': 'Domino taşları birbirine yakın ve uzak dizilerek sesin tanecik aktarımı canlandırılır.',
            'context': 'Fırtına Gözlemi', 'question': 'Gök gürültüsünü şimşek çaktıktan 6 saniye sonra duyan bir gözlemciye şimşeğin çaktığı bulut yaklaşık kaç metre uzaktadır? (v_ses = 340 m/s)',
            'solution': 'Yol = Sürat x Zaman = 340 m/s x 6 s = 2040 metre (yaklaşık 2 km) uzaktadır.', 'weeklyGoal': 'Sesin farklı ortamlardaki süratini doğru sıralama.',
            'evaluation': 'Ses hızı problem kağıdı'
        },
        {
            'theme': 'Ara Tatil', 'subTheme': '2. Dönem Ara Tatili',
            'code': 'FEN.6.GENEL.2', 'title': 'Madde, Isı ve Ses Konuları Beceri Kampı',
            'description': 'Yoğunluk hesaplamaları, ısı yalıtımı ve ses sürati konularında yeni nesil grafik soruları çözülür.',
            'process': ['a) Grafik ve deney düzenekli soruları çözümler.'],
            'concepts': ['Genel Tekrar', 'Analiz'], 'skills': ['Muhakeme'],
            'pedagogical': 'Tatil fasikülü incelenir.', 'context': 'Tatil Kampı',
            'question': 'Sesin katılarda gazlara göre daha hızlı yayılmasının tanecikli yapı açısından açıklaması nedir?',
            'solution': 'Katı taneciklerinin birbirine çok yakın olması titreşim enerjisinin komşu taneciğe çok daha hızlı aktarılmasını sağlar.',
            'weeklyGoal': 'Fiziksel olaylar kazanımlarını pekiştirme.', 'evaluation': 'Ara tatil değerlendirme testi'
        },
        {
            'theme': 'Ses ve Özellikleri', 'subTheme': 'Sesin Maddeyle Etkileşimi (Yansıma, Soğurulma, Yalıtım)',
            'code': 'FEN.6.5.4', 'title': 'Yankı Olayı, Ses Yalıtımı, Akustik ve Sonar Cihazı',
            'description': 'Sesin sert yüzeylerden yansımasını (yankı), gözenekli ve yumuşak yüzeylerde soğurulmasını; sinema ve camilerdeki akustik tasarımları ve sonar teknolojisini modeller.',
            'process': ['a) Yankı oluşabilmesi için kaynak ile engel arasında en az 17 metre mesafe olması gerektiğini açıklar.', 'b) Yarasa ve yunusların ses yansımasıyla yön bulmasını (biyomimikri) inceler.'],
            'concepts': ['Sesin Yansıması', 'Yankı', 'Soğurulma', 'Ses Yalıtımı', 'Akustik', 'Sonar'],
            'skills': ['Teknoloji ve Doğa İlişkisi', 'Mimari Tasarım'], 'pedagogical': 'Mimar Sinan\'ın Süleymaniye Camii\'ndeki akustik dehası ve nargile kandilleri örneği anlatılır.',
            'context': 'Denizaltı Sonarları ve Mimari', 'question': 'Sinema ve tiyatro salonlarının duvarlarının sünger, kumaş veya keçeyle kaplanmasının temel amacı nedir?',
            'solution': 'Sesin sert duvarlardan yansıyıp yankı yapmasını önlemek ve sesi soğurarak net işitilmesini (ses yalıtımı ve akustik düzenleme) sağlamaktır.', 'weeklyGoal': 'Sesin maddeyle etkileşimini teknolojide ve mimaride kullanma.',
            'evaluation': 'Ses yalıtım kutusu tasarım projesi'
        },

        # 29-33: Vücudumuzdaki Sistemler ve Sağlığı
        {
            'theme': 'Vücudumuzdaki Sistemler ve Sağlığı', 'subTheme': 'Denetleyici ve Düzenleyici Sistemler (Sinir Sistemi)',
            'code': 'FEN.6.6.1', 'title': 'Merkezî ve Çevresel Sinir Sistemi (Beyin, Beyincik, Omurilik Soğanı, Omurilik)',
            'description': 'Beynin (öğrenme, hafıza), beyinciğin (denge ve kas koordinasyonu), omurilik soğanının (yaşamsal refleksler: hapşırma, yutma), omuriliğin (refleks merkezi) görevlerini açıklar.',
            'process': ['a) İp cambazının veya bisiklet süren kişinin beyinciğini kullandığını kavrar.', 'b) İstemli hareketlerin beyin tarafından yönetildiğini öğrenir.'],
            'concepts': ['Beyin', 'Beyincik', 'Omurilik Soğanı', 'Omurilik', 'Merkezî Sinir Sistemi'],
            'skills': ['Organ-İşlev Eşleştirme', 'Bilişsel Harita'], 'pedagogical': 'Gözleri kapatıp tek ayak üzerinde durma testiyle beyincik ve denge fark edilir.',
            'context': 'Nöroloji', 'question': 'Kaza geçiren bir insanın solunum ve kalp atışının durması merkezî sinir sisteminin hangi hayati bölümünün hasar gördüğünü gösterir?',
            'solution': 'Yaşam düğümü olarak adlandırılan ve iç organları kontrol eden omurilik soğanının hasar gördüğünü gösterir.', 'weeklyGoal': 'Merkezî sinir sistemi bölümlerinin görevlerini ayırt etme.',
            'evaluation': 'Sinir sistemi organ şeması eşleştirme'
        },
        {
            'theme': 'Vücudumuzdaki Sistemler ve Sağlığı', 'subTheme': 'Refleksler (Kalıtsal ve Sonradan Kazanılan)',
            'code': 'FEN.6.6.1', 'title': 'Doğuştan Gelen (Kalıtsal) ve Sonradan Kazanılan (Şartlı) Refleksler',
            'description': 'Omurilik tarafından yönetilen ani ve istemsiz tepkileri (refleks); diz kapağı vuruşu, göz bebeğinin büyümesi ile araba sürme, örgü örme farkıyla inceler.',
            'process': ['a) Refleksin vücudu tehlikelere karşı koruyucu bir savunma mekanizması olduğunu kavrar.', 'b) Sonradan kazanılan reflekslerin önce beyinle öğrenilip sonra omuriliğe devredildiğini açıklar.'],
            'concepts': ['Refleks', 'Omurilik', 'Kalıtsal Refleks', 'Kazanılmış Refleks', 'Korunma'],
            'skills': ['Örnek Olay Analizi', 'Fizyolojik Mantık'], 'pedagogical': 'Ele iğne battığında elin hızla geri çekilmesi ve acının sonradan hissedilmesi canlandırılır.',
            'context': 'Acil Durum Reaksiyonları', 'question': 'Limon görünce ağzın sulanması, bisiklete binmek ve dans etmek hangi tür refleks grubuna girer?',
            'solution': 'Doğumda olmayıp sonradan deneyim ve öğrenmeyle kazanılan refleksler (şartlı refleks) grubuna girer.', 'weeklyGoal': 'Refleks çeşitlerini doğru sınıflandırma.',
            'evaluation': 'Refleks sınıflandırma tablosu'
        },
        {
            'theme': 'Vücudumuzdaki Sistemler ve Sağlığı', 'subTheme': 'İç Salgı Bezleri (Hormonlar)',
            'code': 'FEN.6.6.2', 'title': 'Hipofiz, Tiroid, Pankreas, Böbrek Üstü ve Eşeysel Bezler',
            'description': 'Hormon üreten iç salgı bezlerini; hipofizin büyüme hormonu, tiroidin tiroksin, böbrek üstünün adrenalin, pankreasın insülin ve glukagon hormonlarını inceler.',
            'process': ['a) Korku ve heyecan anında adrenalinin kalp atışını hızlandırdığını kavrar.', 'b) İnsülinin kan şekerini düşürdüğünü, glukagonun artırdığını modeller.'],
            'concepts': ['İç Salgı Bezi', 'Hormon', 'Hipofiz', 'Tiroksin', 'Adrenalin', 'İnsülin / Glukagon'],
            'skills': ['Hormonal Düzenleme', 'Kan Şekeri Grafiği Yorumlama'], 'pedagogical': 'İnsülin-glukagon tahterevalli modeliyle kan şekeri dengesi anlatılır.',
            'context': 'Endokrinoloji ve Diyabet', 'question': 'Yemek yedikten sonra kanda yükselen glikoz (şeker) seviyesini normale indiren hormon hangisidir ve hangi bezden salgılanır?',
            'solution': 'İnsülin hormonudur ve pankreas bezinden salgılanır.', 'weeklyGoal': 'Hormonların vücuttaki düzenleyici etkilerini kavrama.',
            'evaluation': 'Hormonlar ve görevleri kart oyunu'
        },
        {
            'theme': 'Vücudumuzdaki Sistemler ve Sağlığı', 'subTheme': 'Duyu Organları (Göz, Kulak, Burun, Dil, Deri)',
            'code': 'FEN.6.6.3', 'title': 'Duyu Organlarının Yapısı ve Duyu Almaçlarının İşleyişi',
            'description': 'Çevremizdeki uyarıları alan duyu organlarımızın yapısını; gözdeki sarı leke ve kör nokta, kulaktaki salyangoz ve yarım daire kanalları, dildeki tat tomurcuklarını inceler.',
            'process': ['a) Koku alma ile tat alma duyularının beyinde birlikte değerlendirildiğini keşfeder.', 'b) Grip olunduğunda yemeklerin tadının tam alınamamasının nedenini açıklar.'],
            'concepts': ['Duyu Almaçları', 'Sarı Leke', 'Salyangoz', 'Yarım Daire Kanalları', 'Tat Tomurcuğu'],
            'skills': ['Çoklu Duyu Entegrasyonu', 'Anatomik İnceleme'], 'pedagogical': 'Burnu kapalıyken elma ve patates dilimini ayırt etme tat alma deneyi yapılır.',
            'context': 'Nöro-Görsel Algı', 'question': 'Nezle veya grip olduğumuzda yediğimiz yemeklerin lezzetini ve tadını tam olarak alamamamızın sebebi nedir?',
            'solution': 'Tat alma ve koku alma duyuları birlikte çalışır; koku almaçları tıkandığında tat duyusu da eksik algılanır.', 'weeklyGoal': 'Duyu organlarının çalışma mekanizmalarını açıklama.',
            'evaluation': 'Duyu organları yapı çizimleri'
        },
        {
            'theme': 'Vücudumuzdaki Sistemler ve Sağlığı', 'subTheme': 'Göz Kusurları ve Sistemlerin Sağlığı',
            'code': 'FEN.6.6.4', 'title': 'Miyop, Hipermetrop, Astigmat ve Sağlıklı Yaşam',
            'description': 'Miyopun uzağı net görememe (kalın kenarlı mercekle düzeltme), hipermetropun yakını net görememe (ince kenarlı mercekle düzeltme) olduğunu ve organ bağışının önemini savunur.',
            'process': ['a) Göz kusurlarını mercek türleriyle eşleştirir.', 'b) Organ bağışının hayat kurtarma değerini açıklar.'],
            'concepts': ['Miyop', 'Hipermetrop', 'Astigmat', 'Mercek Düzeltmesi', 'Organ Bağışı'],
            'skills': ['Fiziksel Kusurları Optikle Giderme', 'Empati'], 'pedagogical': 'Göz doktoru muayene çizelgesi üzerinden kırma kusurları incelenir.',
            'context': 'Göz Sağlığı ve Oftalmoloji', 'question': 'Uzağı net göremeyen bir öğrenciye göz doktoru hangi tanıyı koyar ve hangi tip mercekli gözlük reçete eder?',
            'solution': 'Miyop tanısı koyar ve görüntüyü sarı lekeye düşürmek için kalın kenarlı (ıraksak) mercek verir.', 'weeklyGoal': 'Göz kusurlarını ve düzeltilme yollarını açıklama.',
            'evaluation': 'Göz kusurları optik eşleştirme formu'
        },

        # 34-36: Elektriğin İletimi
        {
            'theme': 'Elektriğin İletimi', 'subTheme': 'İletken ve Yalıtkan Maddeler',
            'code': 'FEN.6.7.1', 'title': 'Elektriği İleten ve İletmeyen Katı ve Sıvı Maddeler',
            'description': 'Elektrik enerjisini ileten iletken maddeleri (bakır, demir, tuzlu su, asitli su) ve iletmeyen yalıtkan maddeleri (plastik, kauçuk, saf su, şekerli su) test devresi kurarak belirler.',
            'process': ['a) Saf suyun yalıtkan iken tuz atıldığında iletken hale geldiğini deneyler.', 'b) Kontrol kaleminin yalıtkan sapının elektrikçiyi koruduğunu kavrar.'],
            'concepts': ['İletken Madde', 'Yalıtkan Madde', 'Tuzlu Su (İletken)', 'Saf Su (Yalıtkan)', 'Elektrik Çarpması'],
            'skills': ['Devre ile Test Etme', 'Madde Sınıflandırma'], 'pedagogical': 'Açık uçlu devreye farklı sıvılar daldırılarak ampulün yanıp yanmadığı kontrol edilir.',
            'context': 'Elektrik Tesisatı Güvenliği', 'question': 'Saf suya sofra tuzu (NaCl) ilave edildiğinde yalıtkan olan sıvının iletken hale gelmesinin kimyasal sebebi nedir?',
            'solution': 'Tuz suda çözündüğünde serbest hareket edebilen elektrik yüklü iyonlar (Na+ ve Cl-) oluşturarak akımı iletir.', 'weeklyGoal': 'Maddeleri elektriksel iletkenliklerine göre sınıflandırma.',
            'evaluation': 'İletken-Yalıtkan sıvı deney tablosu'
        },
        {
            'theme': 'Elektriğin İletimi', 'subTheme': 'Elektriksel Direnç ve Bağlı Olduğu Faktörler',
            'code': 'FEN.6.7.2', 'title': 'Bir İletkenin Direncini Etkileyen Faktörler (Uzunluk, Kesit Alanı, İletkenin Cinsi)',
            'description': 'Maddelerin elektrik akımına karşı gösterdiği zorluğa direnç dendiğini; iletkenin boyu (uzunluk L) arttıkça direncin arttığını, kesit alanı (kalınlık S) arttıkça direncin azaldığını kontrollü deneyle keşfeder.',
            'process': ['a) İnce ve uzun telin direncinin en büyük olduğunu modeller.', 'b) Ampulün içindeki tungstenden yapılmış filaman telin inceliği ve kıvrımlı uzunluğuyla yüksek direnç oluşturup akkor hale geldiğini kavrar.'],
            'concepts': ['Elektriksel Direnç', 'İletkenin Boyu (L)', 'Kesit Alanı (S/Kalınlık)', 'Öz Direnç (Cins)', 'Filaman'],
            'skills': ['Değişken Yönetimi', 'Direnç Modelleme'], 'pedagogical': 'Dar ve uzun koridorda öğrencilerin yürüme zorluğu analojisiyle direnç anlatılır.',
            'context': 'Akkor Lamba ve Isıtıcılar', 'question': 'Aynı maddeden yapılmış iki telden birincisi kısa ve kalın, ikincisi uzun ve incedir. Hangi telin elektrik akımına karşı direnci daha büyüktür?',
            'solution': 'Uzun ve ince olan ikinci telin direnci çok daha büyüktür (boyla doğru, kesitle ters orantılı).', 'weeklyGoal': 'İletkenin direncini geometrik boyutlarıyla ilişkilendirme.',
            'evaluation': 'Direnç değişkenleri laboratuvar föyü'
        },
        {
            'theme': 'Elektriğin İletimi', 'subTheme': 'Yıl Sonu Fen Bilimleri Sentezi',
            'code': 'FEN.6.7.3', 'title': '6. Sınıf Fen Bilimleri Yıl Sonu Başarı Değerlendirmesi',
            'description': 'Güneş sistemi, insan anatomisi, kuvvet, madde, ses ve elektrik alanındaki tüm kazanımları bütünleştiren fen bilimleri genel değerlendirme portfolyosu sunar.',
            'process': ['a) 7. sınıf fen konularına (hücre bölünmeleri ve kuvvet-enerji) hazırlık hedeflerini belirler.', 'b) Yıl boyu yapılan deney raporlarını sergiler.'],
            'concepts': ['Genel Değerlendirme', 'Bilimsel Süreç Becerileri', 'Portfolyo'],
            'skills': ['Sentez', 'Öz Değerlendirme'], 'pedagogical': 'Yıl sonu fen sergisi ve bilimsel bilgi yarışması yapılır.',
            'context': '6. Sınıf Bilim Şenliği', 'question': 'Reosta (ayarlı direnç) sürgüsünü hareket ettirdiğimizde devredeki ampulün parlaklığının değişmesinin çalışma ilkesi nedir?',
            'solution': 'Devreye bağlı telin uzunluğunu değiştirerek direnci artırıp azaltmak ve böylece akımı ayarlamaktır.', 'weeklyGoal': '6. sınıf fen bilimleri öğrenme alanlarını başarıyla tamamlama.',
            'evaluation': 'Yıl Sonu Fen Bilimleri Başarı Belgesi'
        }
    ]
    return {
        'title': '6. Sınıf',
        'subtitle': 'Ortaokul 2. Kademe Fen Programı',
        'badge': 'Ortaokul Fen',
        'weeks': weeks
    }

print("Fen 6 builder compiled.")
