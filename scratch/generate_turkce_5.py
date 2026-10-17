# -*- coding: utf-8 -*-
"""
Generates 36 weeks for Türkçe (Grades 5, 6, 7, 8)
Grade 5: Türkiye Yüzyılı Maarif Modeli (6 Tema)
Grade 6: MEB Müfredatı
Grade 7: MEB Müfredatı
Grade 8: LGS Türkçe Müfredatı
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from curriculum_builder import generate_dart_file, DATES

def build_turkce_5():
    # 5. Sınıf Türkiye Yüzyılı Maarif Modeli (6 Tema)
    # 1. Tema: Oyun Dünyası (1-6)
    # 2. Tema: Atatürk'ü Tanımak (7-12)
    # 3. Tema: Duygularımı Tanıyorum (13-18)
    # 4. Tema: Geleneklerimiz (19-24)
    # 5. Tema: İletişim ve Sosyal İlişkiler (25-30)
    # 6. Tema: Sağlıklı Yaşıyorum (31-36)
    weeks = [
        # 1-6: 1. Tema: Oyun Dünyası
        {
            'theme': 'Oyun Dünyası', 'subTheme': 'Dinleme ve Konuşma Kuralları',
            'code': 'TÜR.5.1.1', 'title': 'Etkili Dinleme/İzleme Stratejileri ve Oyun Kurallarını İfade Etme',
            'description': 'Konuşmacıyı dinlerken göz teması kurma, söz kesmeme, oyun kurallarını sıralı ve anlaşılır bir dille arkadaşlarına anlatma becerilerini geliştirir.',
            'process': ['a) Dinleme amacını belirler.', 'b) Konuşurken beden dilini ve ses tonunu ayarlar.'],
            'concepts': ['Etkili Dinleme', 'Nezaket', 'Oyun Kuralları', 'Sözlü İletişim'],
            'skills': ['Dinleme Becerisi', 'Sözlü Anlatım'], 'pedagogical': 'Geleneksel çocuk oyunları (seksek, mendil kapmaca) kuralları sınıfta canlandırılır.',
            'context': 'Geleneksel Çocuk Oyunları', 'question': 'Bir oyunu yeni oynayacak bir arkadaşımıza kurallarını anlatırken nelere dikkat etmeliyiz?',
            'solution': 'Oyunun amacını, oyuncu sayısını, kurallarını oluş sırasına göre ve açık, net cümlelerle aktarmalıyız.', 'weeklyGoal': 'Dinleme ve sözlü anlatım kurallarını oyun bağlamında uygulama.',
            'evaluation': 'Oyun anlatımı konuşma rubriği'
        },
        {
            'theme': 'Oyun Dünyası', 'subTheme': 'Sözcükte Gerçek ve Mecaz Anlam',
            'code': 'TÜR.5.1.2', 'title': 'Sözcüklerin Gerçek (Temel) ve Mecaz Anlamlarını Ayırt Etme',
            'description': 'Sözcüklerin akla ilk gelen anlamı (gerçek) ile ilgi ve benzetme yoluyla kazandığı yeni anlamları (mecaz) metin bağlamında çözümler.',
            'process': ['a) Sözcüklerin cümledeki bağlamsal anlamını saptar.', 'b) Mecaz anlamlı sözcükleri somutlaştırır.'],
            'concepts': ['Gerçek Anlam', 'Mecaz Anlam', 'Bağlam', 'Çok Anlamlılık'],
            'skills': ['Söz Varlığını Geliştirme', 'Metin Çözümleme'], 'pedagogical': '\'Sıcak çorba\' (gerçek) ile \'sıcak karşılama\' (mecaz) kartları eşleştirilir.',
            'context': 'Hikâye Çözümlemesi', 'question': '\'Oyunda takım arkadaşına çok soğuk davrandı\' cümlesindeki \'soğuk\' sözcüğü hangi anlamda kullanılmıştır?',
            'solution': 'Mecaz anlamda kullanılmıştır; ilgisiz, mesafeli ve sevgisiz davranmayı ifade eder.', 'weeklyGoal': 'Gerçek ve mecaz anlamları metin içinde doğru tespit etme.',
            'evaluation': 'Gerçek-Mecaz anlam eşleştirme kâğıdı'
        },
        {
            'theme': 'Oyun Dünyası', 'subTheme': 'Söz Varlığı ve Terim Anlam',
            'code': 'TÜR.5.1.2', 'title': 'Oyun, Spor ve Bilim Alanına Ait Terim Anlamlı Sözcükler',
            'description': 'Bilim, sanat, meslek veya spor dallarına özgü özel kavramları (terim anlam: taç, penaltı, perde, nota) metinlerde belirler ve doğru kullanır.',
            'process': ['a) Terimlerin günlük kullanımdan farkını ayırt eder.', 'b) Oyun terimleriyle sözlük çalışması yapar.'],
            'concepts': ['Terim Anlam', 'Spor Terimleri', 'Bilimsel Terim'],
            'skills': ['Kavramsal Ayrıştırma', 'Sözlük Kullanımı'], 'pedagogical': 'Futbol, voleybol, tiyatro ve müzik terimleri sepetlerine kelime gruplama oyunu oynatılır.',
            'context': 'Oyun ve Spor Dünyası', 'question': '\'Hakem maçın son dakikasında penaltı noktasını gösterdi\' cümlesindeki terim anlamlı sözcük hangisidir?',
            'solution': '\'Penaltı\' ve \'hakem\' sözcükleri futbol sporuna ait birer terimdir.', 'weeklyGoal': 'Terim anlamlı sözcükleri alanlarına göre ayırt etme.',
            'evaluation': 'Terim avı çalışma fasikülü'
        },
        {
            'theme': 'Oyun Dünyası', 'subTheme': 'Kökler ve Ekler (Yapım Ekleri)',
            'code': 'TÜR.5.1.3', 'title': 'Sözcüğün Kökü ve Anlam Değiştiren Yapım Ekleri (-lik, -ci, -li, -siz)',
            'description': 'Sözcüğün anlamlı en küçük parçasını (kök) bulur; köke gelerek yeni anlamlı sözcük türeten yapım eklerini çözümler.',
            'process': ['a) Kök ile türemiş sözcük arasındaki anlam bağını denetler.', 'b) Oyun -> oyuncu -> oyunculuk türetme basamaklarını modeller.'],
            'concepts': ['Kök', 'Yapım Eki', 'Türemiş Sözcük', 'Gövde'],
            'skills': ['Biçim Bilgisi Analizi', 'Sözcük Türetme'], 'pedagogical': 'Kelime ağacı çizilerek kökten dallara yeni türetilen kelimeler asılır.',
            'context': 'Türkçenin Zenginliği', 'question': '\'Kitaplık, gözlükçü, evsiz\' sözcüklerinin köklerini ve kök türlerini bulunuz.',
            'solution': 'Kitap (İsim kökü), Göz (İsim kökü), Ev (İsim kökü).', 'weeklyGoal': 'Kök ve yapım eki ayrımını kavrayarak sözcük türetme.',
            'evaluation': 'Kök ve ek çözümleme tablosu'
        },
        {
            'theme': 'Oyun Dünyası', 'subTheme': 'Hikâye Unsurları ve Betimleme',
            'code': 'TÜR.5.1.4', 'title': 'Olay, Yer, Zaman, Şahıs ve Varlık Kadrosu (Hikâye Haritası)',
            'description': 'Okuduğu hikâyedeki 4 temel unsuru (olay örgüsü, mekân/yer, zaman, kahramanlar/şahıs kadrosu) tespit eder; betimleyici unsurları analiz eder.',
            'process': ['a) Hikâye haritasını şematize eder.', 'b) Karakterlerin fiziksel ve ruhsal özelliklerini karşılaştırır.'],
            'concepts': ['Hikâye Haritası', 'Olay', 'Mekân', 'Zaman', 'Karakter', 'Betimleme'],
            'skills': ['Metin İçi Yapı Analizi', 'Görselleştirme'], 'pedagogical': 'Hikâyedeki sokak veya oyun alanı resmedilerek betimleme somutlaştırılır.',
            'context': 'Çocuk Edebiyatı Hikâyeleri', 'question': 'Bir hikâyede \'Kimin başından geçti, nerede ve ne zaman gerçekleşti?\' soruları hangi unsurları buldurur?',
            'solution': 'Sırasıyla şahıs kadrosunu (karakterleri), mekânı (yeri) ve zamanı buldurur.', 'weeklyGoal': 'Hikâye unsurlarını eksiksiz çözümleme.',
            'evaluation': 'Hikâye haritası çıkarma görevi'
        },
        {
            'theme': 'Oyun Dünyası', 'subTheme': 'Yazma Becerisi: Oyun Kuralları Kılavuzu',
            'code': 'TÜR.5.1.5', 'title': 'Kurallı ve Açık Yönerge Metni Yazma',
            'description': 'Kendi tasarladığı yeni bir kutu oyununun veya sokak oyununun adını, amacını, malzemelerini ve oynanış kurallarını maddeler halinde yazar.',
            'process': ['a) Başlık, giriş, kurallar ve puanlama bölümlerini düzenler.', 'b) Noktalama ve yazım kurallarına uyar.'],
            'concepts': ['Yönerge Yazma', 'Kural Metni', 'Sıralı Anlatım', 'Yazım Kuralları'],
            'skills': ['Yazılı Anlatım', 'Yaratıcı Yazarlık'], 'pedagogical': 'Öğrenciler kendi yazdıkları oyun kılavuzunu arkadaşlarına verip oyunu oynatırlar.',
            'context': 'Oyun Tasarım Atölyesi', 'question': 'Bir oyun kılavuzunda yönergelerin anlaşılır olması için anlatımda hangi ifade biçimi tercih edilmelidir?',
            'solution': 'Maddeler halinde, kronolojik sıraya uygun ve emir/gereklilik kipiyle açık, net cümleler kurulmalıdır.', 'weeklyGoal': 'Açık ve anlaşılır bir oyun yönerge metni oluşturma.',
            'evaluation': '1. Tema Ürün Dosyası ve Yazma Rubriği'
        },

        # 7-12: 2. Tema: Atatürk'ü Tanımak
        {
            'theme': "Atatürk'ü Tanımak", 'subTheme': "Atatürk'ün Çocukluğu ve Eğitimi",
            'code': 'TÜR.5.2.1', 'title': 'Biyografik Metinlerde Kronolojik Sıralama ve Önemli Olaylar',
            'description': "Atatürk'ün Selanik'teki çocukluğu, Mahalle Mektebi, Şemsi Efendi Mektebi ve Askerî Rüştiye yıllarını anlatan metinleri kronolojik sıraya göre inceler.",
            'process': ['a) Olayların akışını zaman bağlaçlarıyla takip eder.', 'b) Metne uygun başlık önerir.'],
            'concepts': ['Biyografi', 'Kronoloji', 'Mustafa Kemal', 'Tarihî Metin'],
            'skills': ['Kronolojik Düşünme', 'Ana Düşünce Belirleme'], 'pedagogical': "Mustafa Kemal'e 'Kemal' adının matematik öğretmeni tarafından veriliş hikâyesi okunur.",
            'context': 'Millî Mücadele ve Atatürk', 'question': "Biyografi (yaşam öyküsü) türündeki bir metnin en belirleyici özelliği nedir?",
            'solution': 'Tanınmış bir kişinin hayatının, başarılarının ve eserlerinin tarafsız ve kronolojik olarak anlatılmasıdır.', 'weeklyGoal': 'Biyografik metinlerde ana düşünce ve kronolojiyi takip etme.',
            'evaluation': 'Biyografi zaman şeridi çizimi'
        },
        {
            'theme': "Atatürk'ü Tanımak", 'subTheme': 'Eş Anlamlı ve Zıt Anlamlı Sözcükler',
            'code': 'TÜR.5.2.2', 'title': 'Anlamdaş (Eş Anlamlı) ve Karşıt (Zıt Anlamlı) Sözcükler',
            'description': 'Yazılışları farklı anlamları aynı olan eş anlamlı sözcükler (vatan-yurt, lider-önder) ile birbirinin tam karşıtı olan zıt anlamlı sözcükleri cümle bağlamında ayırt eder.',
            'process': ['a) Bir sözcüğün olumsuzunun (geldi - gelmedi) onun zıt anlamlısı OLMADIĞINI kavrar.', 'b) Cümlede birbirinin yerine kullanarak söz varlığını zenginleştirir.'],
            'concepts': ['Eş Anlam (Anlamdaş)', 'Zıt Anlam (Karşıt)', 'Olumsuzluk Farkı'],
            'skills': ['Kelime Dağarcığı', 'Anlamsal Hassasiyet'], 'pedagogical': "'Gülmek' eyleminin zıttı 'gülmemek' değil 'ağlamak'tır kuralı panoya asılır.",
            'context': 'Vatan ve Bağımsızlık Metinleri', 'question': "'Cesur' sözcüğünün eş anlamlısı ile zıt anlamlısı nedir?",
            'solution': "Eş anlamlısı: 'Yiğit / Yürekli', zıt anlamlısı: 'Korkak'tır.", 'weeklyGoal': 'Eş ve zıt anlamlı sözcükleri olumsuzlukla karıştırmadan kullanma.',
            'evaluation': 'Eş-Zıt anlam kartları eşleştirme'
        },
        {
            'theme': "Atatürk'ü Tanımak", 'subTheme': 'Büyük Harflerin Kullanımı',
            'code': 'TÜR.5.2.3', 'title': 'Büyük Harflerin Yazımı Kuralları (Kişi, Yer, Kurum, Tarih Adları)',
            'description': 'Kişi ad ve unvanları, akrabalık bildiren kelimeler, yer adları (il, ilçe, kıta), belirli tarih bildiren gün ve ay adlarının büyük harfle yazılış kurallarını uygular.',
            'process': ['a) \'29 Ekim 1923 Pazartesi\' yazılışında ay ve günün büyük yazıldığını açıklar.', 'b) Akrabalık bildiren küçük harf (Ayşe teyze) kuralını inceler.'],
            'concepts': ['Büyük Harf', 'Özel İsim', 'Tarih Yazımı', 'Kurum Adları'],
            'skills': ['İmla Denetimi', 'Kural Uygulama'], 'pedagogical': 'Hatalı yazılmış afiş ve gazete kupürleri üzerindeki imla hataları düzeltilir.',
            'context': 'Cumhuriyet Bayramı Kutlama Programı', 'question': "'Okullar eylül ayında açılacak' cümlesi ile 'Okullar 15 Eylül'de açılacak' cümlesindeki yazım farkının sebebi nedir?",
            'solution': "Belirli bir kesin tarih (15 rakamı) bildirildiğinde ay adı büyük harfle yazılır ve ek kesmeyle ayrılır; genel kullanıldığında küçük yazılır.", 'weeklyGoal': 'Büyük harflerin kullanım yerlerini hatasız uygulama.',
            'evaluation': 'Yazım kuralları avı çalışma kâğıdı'
        },
        {
            'theme': 'Ara Tatil', 'subTheme': '1. Dönem Ara Tatili',
            'code': 'TÜR.5.GENEL.1', 'title': 'Oyun Dünyası ve Atatürk Temaları Okuma Kampı',
            'description': 'Kök-ek, eş-zıt anlam ve paragraf okuduğunu anlama metinleri çözümlenir.',
            'process': ['a) Kapsamlı okuma fasikülü tamamlar.'],
            'concepts': ['Genel Tekrar', 'Okuma Kültürü'], 'skills': ['Eleştirel Okuma'],
            'pedagogical': 'Tatil kitap okuma günlüğü tutulur.', 'context': 'Tatil Okuma Kulübü',
            'question': 'Bir metnin ana fikri (ana düşüncesi) ne demektir?',
            'solution': 'Yazarın metni yazarken okuyucuya iletmek istediği temel mesaj, ders veya asıl düşüncedir.',
            'weeklyGoal': 'İlk 9 haftanın dil becerilerini pekiştirme.', 'evaluation': 'Ara Tatil Okuma Değerlendirme Testi'
        },
        {
            'theme': "Atatürk'ü Tanımak", 'subTheme': "Atatürk'ün Kişilik Özellikleri ve Metin İnceleme",
            'code': 'TÜR.5.2.4', 'title': "Metindeki İpuçlarından Atatürk'ün Kişilik Özelliklerini Çıkarma",
            'description': "Okuduğu anı ve metinlerden yola çıkarak Atatürk'ün vatanseverlik, ileri görüşlülük, kararlılık, birleştiricilik ve bilime verdiği önem gibi özelliklerini çıkarır.",
            'process': ['a) Çanakkale Savaşındaki emirlerinden kararlılık özelliğini tespit eder.', 'b) \'Hayatta en hakiki mürşit ilimdir\' sözünden bilimselliğini modeller.'],
            'concepts': ['Kişilik Özellikleri', 'Vatanseverlik', 'İleri Görüşlülük', 'Metinden Çıkarım'],
            'skills': ['Çıkarım Yapma', 'Karakter Analizi'], 'pedagogical': "Atatürk'ün anıları okunup sınıf panosunda erdemler haritası oluşturulur.",
            'context': "Çanakkale Zaferi ve 10 Kasım", 'question': "'Geldikleri gibi giderler!' sözü Atatürk'ün hangi üstün kişilik özelliğini yansıtır?",
            'solution': "İleri görüşlülüğünü, millete olan inancını ve bağımsızlık konusundaki kesin kararlılığını yansıtır.", 'weeklyGoal': "Metinden hareketle lider kişilik özelliklerini gerekçelendirme.",
            'evaluation': 'Kişilik özellikleri analiz formu'
        },
        {
            'theme': "Atatürk'ü Tanımak", 'subTheme': "Noktalama İşaretleri ve Şiir Yazma",
            'code': 'TÜR.5.2.5', 'title': "Nokta, Virgül, Soru ve Ünlem İşaretleri ve Atatürk Sevgisi Şiiri",
            'description': "Cümle sonunda nokta, soru işareti, ünlem; eş görevli kelimeler arasında virgülün kullanımını pekiştirir; ana duygusu Atatürk sevgisi olan özgün bir şiir yazar.",
            'process': ['a) Noktalama işaretlerini doğru yerlere koyar.', 'b) Şiirde dize ve kıta ahengini sağlar.'],
            'concepts': ['Nokta (.)', 'Virgül (,)', 'Ünlem (!)', 'Soru İşareti (?)', 'Dize (Mısra)', 'Kıta'],
            'skills': ['Noktalama Yetkinliği', 'Şiirsel İfade'], 'pedagogical': 'Öğrencilerin yazdığı Atatürk şiirleri sınıf panosunda sergilenir.',
            'context': '10 Kasım Atatürk\'ü Anma Programı', 'question': "Hitap bildiren kelimelerden sonra (örneğin: 'Sevgili Öğrenciler,') hangi noktalama işareti konur?",
            'solution': 'Virgül (,) konur.', 'weeklyGoal': 'Temel noktalama işaretlerini doğru kullanarak duygulu bir şiir yazma.',
            'evaluation': 'Şiir dinletisi ve noktalama değerlendirme rubriği'
        },

        # 13-18: 3. Tema: Duygularımı Tanıyorum
        {
            'theme': 'Duygularımı Tanıyorum', 'subTheme': 'Deyimler ve Atasözleri',
            'code': 'TÜR.5.3.1', 'title': 'Deyim ve Atasözlerinin Metne Anlam Katkısı ve Kalıplaşmış Yapısı',
            'description': 'Deyimlerin duyguları (öfke, sevinç, şaşkınlık) etkili anlatma gücünü; atasözlerinin öğüt bildiren kültürel kalıplar olduğunu ve sözcüklerinin değiştirilemeyeceğini açıklar.',
            'process': ['a) \'Küpere binmek\' (öfkelenmek), \'etekleri zil çalmak\' (sevinmek) deyimlerini çözümler.', 'b) Kalıplaşmış söz dizimini inceler.'],
            'concepts': ['Deyim', 'Atasözü', 'Kalıplaşma', 'Öğüt', 'Duygu İfadeleri'],
            'skills': ['Kültürel Söz Varlığı', 'Mecazi Algı'], 'pedagogical': 'Deyimler resimlenerek sınıfta \'Deyim Çizmece / Tabu\' oyunu oynatılır.',
            'context': 'Deyimler ve Masallar', 'question': "'Damlaya damlaya göl olur' atasözündeki 'göl' kelimesinin yerine 'deniz' kelimesi kullanılabilir mi, neden?",
            'solution': 'Kullanılamaz; çünkü atasözleri ve deyimler kalıplaşmış söz öbekleridir, kelimeleri değiştirilemez veya eş anlamlısı konamaz.', 'weeklyGoal': 'Deyimleri duygu bağlamında doğru ve yerinde kullanma.',
            'evaluation': 'Deyimler karikatür albümü'
        },
        {
            'theme': 'Duygularımı Tanıyorum', 'subTheme': 'Öznel ve Nesnel Yargılar',
            'code': 'TÜR.5.3.2', 'title': 'Kanıtlanabilir Nesnel Cümleler ile Kişisel Beğeni Bildiren Öznel Cümleler',
            'description': 'Kişiden kişiye değişmeyen, doğruluğu veya yanlışlığı ispatlanabilen nesnel yargılar ile kişisel beğeni, duygu ve yorum içeren öznel yargıları ayırt eder.',
            'process': ['a) \'Türkiye\'nin başkenti Ankara\'dır\' cümlesinin nesnel olduğunu belirtir.', 'b) \'En güzel renk mavidir\' cümlesinin öznel olduğunu kavrar.'],
            'concepts': ['Öznel Anlatım (Kişisel)', 'Nesnel Anlatım (Kanıtlanabilir)', 'Kanıt'],
            'skills': ['Eleştirel Düşünme', 'Fikir-Olay Ayrımı'], 'pedagogical': 'Gazete haberlerindeki öznel yorumlar sarı, nesnel bilgiler mavi kalemle çizilir.',
            'context': 'Film ve Kitap Eleştirisi', 'question': "'Yazarın son kitabı sürükleyici anlatımıyla herkesi büyüleyecek harika bir eserdir' cümlesi öznel midir nesnel midir?",
            'solution': 'Öznel bir cümledir; kişisel beğeni, takdir ve övgü içermektedir.', 'weeklyGoal': 'Öznel ve nesnel cümleleri metinlerde ayırt edebilme.',
            'evaluation': 'Öznel-Nesnel sınıflandırma çalışma yaprağı'
        },
        {
            'theme': 'Duygularımı Tanıyorum', 'subTheme': 'Cümlede Anlam İlişkileri: Neden-Sonuç ve Amaç-Sonuç',
            'code': 'TÜR.5.3.3', 'title': 'Neden-Sonuç (Sebep-Sonuç) ile Amaç-Sonuç Cümlelerinin Ayırt Edilmesi',
            'description': "'İçin, diye, -dığından' eklerinin kullanıldığı cümlelerde sonucun hangi gerekçeyle gerçekleştiğini (neden) veya hangi hedef doğrultusunda yapıldığını (amaç) test eder.",
            'process': ['a) \'Amacıyla\' kelimesi konulduğunda anlamlı oluyorsa amaç-sonuç olduğunu kavrar.', 'b) Neden-sonuçta her iki eylemin de gerçekleştiğini fark eder.'],
            'concepts': ['Neden-Sonuç', 'Amaç-Sonuç', 'Gerekçe', 'Hedef'],
            'skills': ['Mantıksal Akıl Yürütme', 'Cümle İçi İlişki Kurma'], 'pedagogical': 'Formül uygulanır: Cümleye \'Hangi amaçla?\' ve \'Hangi sebeple?\' soruları sorularak ayrım yapılır.',
            'context': 'Günlük Diyaloglar', 'question': "'Hasta olduğu için okula gelemedi' ile 'İyileşmek için doktora gitti' cümlelerinin anlam ilişkileri sırasıyla nedir?",
            'solution': 'Birincisi neden-sonuç (hastalık sebep), ikincisi amaç-sonuçtur (doktora gitme amacı iyileşmektir).', 'weeklyGoal': 'Neden-sonuç ve amaç-sonuç cümlelerini hatasız çözümleme.',
            'evaluation': 'Cümle anlam ilişkileri test kâğıdı'
        },
        {
            'theme': 'Duygularımı Tanıyorum', 'subTheme': 'Koşul-Sonuç (Şart) Cümleleri',
            'code': 'TÜR.5.3.3', 'title': 'Bir Eylemin Gerçekleşmesini Bir Şarta Bağlayan Koşul Cümleleri',
            'description': "'-se/-sa, üzere, ancak' ekleriyle kurulan, bir olayın gerçekleşmesinin başka bir olaya bağlı olduğunu belirten koşul-sonuç cümlelerini çözümler.",
            'process': ['a) Şart eki -se/-sa\'nın kattığı anlamı irdeler.', 'b) Koşul gerçekleşmezse sonucun da gerçekleşmeyeceğini modeller.'],
            'concepts': ['Koşul-Sonuç (Şart)', '-se / -sa Eki', 'Ön Koşul'],
            'skills': ['Mantıksal Çıkarım', 'Şartlı Düşünme'], 'pedagogical': "'Kitabı geri vermek üzere alabilirsin' cümlesiyle kütüphane kuralı ilişkilendirilir.",
            'context': 'Sınıf Kuralları ve Sözleşmeler', 'question': "'Düzenli çalışırsan sınavda başarılı olursun' cümlesinde başarının koşulu nedir?",
            'solution': 'Düzenli çalışmaktır; çalışma koşulu yerine gelirse başarı sonucu elde edilir.', 'weeklyGoal': 'Koşul-sonuç ilişkisini cümlelerde doğru saptama.',
            'evaluation': 'Koşul cümleleri tamamlama oyunu'
        },
        {
            'theme': 'Duygularımı Tanıyorum', 'subTheme': 'Şiirde Ana Duygu ve Ses Benzerlikleri',
            'code': 'TÜR.5.3.4', 'title': 'Şiirde Tema/Ana Duygu, Dize Sonu Ses Benzerlikleri (Uyak/Kafiye)',
            'description': 'Şiirde şairin hissettirmek istediği temel duyguyu (özlem, sevinç, yalnızlık, vatan sevgisi) bulur; dize sonlarındaki ses benzerliklerinin kattığı ritmi keşfeder.',
            'process': ['a) Şiir başlığı ile tema uyumunu denetler.', 'b) Ritimli ve ahenkli okuma yapar.'],
            'concepts': ['Ana Duygu (Tema)', 'Dize Sonu Uyum', 'Şiir Ritim', 'Ahenk'],
            'skills': ['Estetik Duyarlık', 'Şiirsel Yorumlama'], 'pedagogical': 'Sınıfta fon müziği eşliğinde duygu temalı şiir okuma dinletisi yapılır.',
            'context': 'Türk Şiiri Antolojisi', 'question': 'Düz yazılarda \'ana fikir\' aranırken şiirlerde ne aranır?',
            'solution': 'Şiirde okuyucuya hissettirilmek istenen temel duygu olan \'ana duygu\' aranır.', 'weeklyGoal': 'Şiirde ana duyguyu ve ahenk unsurlarını kavrama.',
            'evaluation': 'Şiir çözümleme föyü'
        },
        {
            'theme': 'Duygularımı Tanıyorum', 'subTheme': 'Yazma Becerisi: Duygu Günlüğü',
            'code': 'TÜR.5.3.5', 'title': 'Kişisel Günlük (Günce) Yazma ve 1. Dönem Değerlendirmesi',
            'description': 'Yaşadığı önemli bir olayı, hissettiği duyguları tarih belirterek birinci tekil kişi ağzıyla (ben dili) anlatan bir günlük sayfası yazar; 1. dönem dil yetkinliğini değerlendirir.',
            'process': ['a) Günlük türünün özelliklerini (samimi dil, tarih atma) uygular.', 'b) 1. dönem Türkçe ürün dosyasını düzenler.'],
            'concepts': ['Günlük (Günce)', 'Tarih', 'İçten Anlatım', 'Öz Değerlendirme'],
            'skills': ['Duygusal Farkındalık', 'Kişisel Yazarlık'], 'pedagogical': 'Öğrenciler kendi tasarım kapaklarıyla mini günlük defteri oluştururlar.',
            'context': 'Kişisel Gelişim ve Yazarlık', 'question': 'Günlük yazarken sayfanın başına mutlaka ne yazılmalıdır ve dil nasıl olmalıdır?',
            'solution': 'O günün tarihi yazılmalı; dil içten, samimi ve birinci tekil kişiyle (kendi kendine konuşur gibi) olmalıdır.', 'weeklyGoal': 'Duygularını günlük formatında etkili yazılı ifade etme.',
            'evaluation': '1. Dönem Türkçe Karne Öncesi Yetkinlik Sınavı'
        },

        # 19-24: 4. Tema: Geleneklerimiz
        {
            'theme': 'Geleneklerimiz', 'subTheme': 'Kültürel Miras ve Bayramlarımız',
            'code': 'TÜR.5.4.1', 'title': 'Somut Olmayan Kültürel Miras, Millî ve Dinî Bayramlarımız',
            'description': 'Kültürümüzü yansıtan geleneksel bayramlar, kına gecesi, el öpme, imece kültürü ve misafirperverlik temalı bilgilendirici metinleri okuyup özetler.',
            'process': ['a) Metnin anahtar kelimelerini belirler.', 'b) Metinle ilgili 5N1K sorularını cevaplar.'],
            'concepts': ['Gelenek', 'Kültürel Değer', 'İmece', 'Misafirperverlik', 'Özet Çıkarma'],
            'skills': ['Metin Özetleme', 'Kültürel Aktarım'], 'pedagogical': 'Eski bayramlaşma hatıraları aile büyükleriyle yapılan röportajlarla sınıfa taşınır.',
            'context': 'Kültür ve Turizm Bakanlığı Miras Arşivi', 'question': 'Köy ve mahallelerde ortak bir işin (örneğin ekin biçme veya kış hazırlığı) yardımlaşarak hep birlikte yapılmasına ne ad verilir?',
            'solution': "'İmece' kültürü adı verilir; dayanışmanın ve birlikteliğin simgesidir.", 'weeklyGoal': 'Gelenek konulu metinleri 5N1K yöntemiyle anlama ve özetleme.',
            'evaluation': '5N1K metin inceleme kâğıdı'
        },
        {
            'theme': 'Geleneklerimiz', 'subTheme': 'Paragrafta Ana Düşünce ve Yardımcı Düşünceler',
            'code': 'TÜR.5.4.2', 'title': 'Paragrafın Ana Düşüncesini ve Onu Destekleyen Yardımcı Fikirleri Bulma',
            'description': 'Bir paragrafta yazarın vermek istediği temel mesajı (ana düşünce) ile bu düşünceyi destekleyen, örnekleyen yardımcı düşünceleri analiz eder.',
            'process': ['a) \'Bu metinde asıl anlatılmak istenen nedir?\' sorusuyla ana düşünceye ulaşır.', 'b) \'Metinden hangisi çıkarılamaz?\' yardımcı fikir sorularını çözer.'],
            'concepts': ['Paragraf', 'Ana Düşünce', 'Yardımcı Düşünceler', 'Metin Analizi'],
            'skills': ['Derinlemesine Anlama', 'Soru Çözüm Mantığı'], 'pedagogical': 'Paragraf bir şemsiyeye benzetilir; ana düşünce şemsiyenin sapı, yardımcı düşünceler telleri olarak gösterilir.',
            'context': 'Kültürel Miras Metinleri', 'question': 'Bir paragrafta birden fazla ana düşünce olabilir mi? Yardımcı düşünceler ne işe yarar?',
            'solution': 'Bir paragrafta yalnızca tek bir ana düşünce olur; yardımcı düşünceler ise bu ana düşünceyi açıklamak, inandırıcı kılmak ve desteklemek için kullanılır.', 'weeklyGoal': 'Paragrafta ana düşünceyi ve yardımcı düşünceleri hatasız tespit etme.',
            'evaluation': 'Paragrafta ana fikir bulma föyü'
        },
        {
            'theme': 'Geleneklerimiz', 'subTheme': 'Söz Sanatları: Benzetme (Teşbih) ve Abartma (Mübalağa)',
            'code': 'TÜR.5.4.3', 'title': 'Metinlerde Benzetme ve Abartma Sanatlarının Anlatıma Katkısı',
            'description': 'Aralarında ilgi kurulan iki şeyden zayıf olanın güçlü olana benzetilmesini (benzetme: \'Aslan gibi kuvvetli çocuk\') ve bir şeyin olduğundan çok büyük/küçük gösterilmesini (abartma: \'Dünyalar kadar ödevim var\') modeller.',
            'process': ['a) Benzetmenin 4 unsurunu (benzeyen, benzetilen, benzetme edatı, benzetme yönü) keşfeder.', 'b) Deyimlerdeki abartmaları inceler.'],
            'concepts': ['Söz Sanatı', 'Benzetme (Teşbih)', 'Abartma (Mübalağa)', 'Benzetme Edatı (Gibi)'],
            'skills': ['İmgesel Anlatım', 'Edebî Çözümleme'], 'pedagogical': 'Geleneksel masallardaki abartılı ve benzetmeli motifler incelenir.',
            'context': 'Türk Masalları ve Destanlar', 'question': "'Gözyaşlarım sel oldu aktı' cümlesinde hangi söz sanatı vardır ve anlatıma nasıl bir etki yapmıştır?",
            'solution': 'Abartma (mübalağa) sanatı vardır; üzüntünün ve dökülen gözyaşının çokluğunu çarpıcı bir şekilde vurgulamıştır.', 'weeklyGoal': 'Benzetme ve abartma sanatlarını cümlelerde belirleme.',
            'evaluation': 'Söz sanatları tespit çalışma kâğıdı'
        },
        {
            'theme': 'Geleneklerimiz', 'subTheme': 'Kökler ve Çekim Ekleri (Çoğul ve Hâl Ekleri)',
            'code': 'TÜR.5.4.4', 'title': 'İsmin Hâl Ekleri (-i, -e, -de, -den) ve Çoğul Eki (-lar/-ler)',
            'description': 'Sözcüğün anlamını değiştirmeyip cümledeki görevini belirleyen çekim eklerini; ismin yalın, belirtme (-i), yönelme (-e), bulunma (-de) ve ayrılma (-den) hâllerini modeller.',
            'process': ['a) Hâl eklerinin sözcüğe kattığı yer ve durum anlamını irdeler.', 'b) Çoğul ekinin aile (Aliler) veya abartma kattığı durumları fark eder.'],
            'concepts': ['Çekim Eki', 'İsmin Hâl Ekleri', 'Belirtme (-i)', 'Yönelme (-e)', 'Bulunma (-de)', 'Ayrılma (-den)', 'Çoğul Eki (-lar)'],
            'skills': ['Dil Bilgisi Çözümleme', 'Ek-Kök Ayrımı'], 'pedagogical': 'Ev -> Evi -> Eve -> Evde -> Evden aşamaları sınıfta adım adım canlandırılır.',
            'context': 'Kültür Gezisi Anlatımı', 'question': "'Okuldan eve doğru yürürken kitabı çantada unuttuğumu fark ettim' cümlesindeki altı çizili eklerin hâl isimleri nedir?",
            'solution': 'Okul-dan (Ayrılma hâli), ev-e (Yönelme hâli), kitab-ı (Belirtme hâli), çanta-da (Bulunma hâli).', 'weeklyGoal': 'İsmin hâl eklerini ve işlevlerini doğru ayırt etme.',
            'evaluation': 'Hâl ekleri bulmaca föyü'
        },
        {
            'theme': 'Geleneklerimiz', 'subTheme': 'Geleneksel Sanatlarımız ve Bilgilendirici Metin',
            'code': 'TÜR.5.4.5', 'title': 'Ebru, Çini ve Dokuma Sanatları Metin İncelemesi',
            'description': 'Geleneksel Türk el sanatlarını anlatan metinlerde yazarın amacını, konuyu ve başlığı belirler; açıklayıcı anlatım tekniklerini çözümler.',
            'process': ['a) Bilgilendirici metin ile öyküleyici metin arasındaki dil farkını ayırt eder.', 'b) Ebru sanatının aşamalarını sıralar.'],
            'concepts': ['Geleneksel Sanat', 'Ebru Sanatı', 'Çini', 'Bilgilendirici Metin', 'Açıklama'],
            'skills': ['Metin Türü Karşılaştırma', 'Kültürel Farkındalık'], 'pedagogical': 'Tekne ve kitreyle sınıfta ebru yapımı simüle edilir.',
            'context': 'Geleneksel El Sanatları Sergisi', 'question': 'Bilgilendirici bir metin yazarken yazarın temel amacı nedir ve anlatım nasıldır?',
            'solution': 'Okuyucuya bir konu hakkında doğru bilgi vermek, öğretmek ve aydınlatmaktır; nesnel ve açık bir anlatım kullanılır.', 'weeklyGoal': 'Geleneksel sanatlar metnini inceleyerek ana fikri belirleme.',
            'evaluation': 'El sanatları metin tahlili formu'
        },
        {
            'theme': 'Geleneklerimiz', 'subTheme': 'Yazma Becerisi: Tebrik Kartı ve Mektup',
            'code': 'TÜR.5.4.6', 'title': 'Geleneksel İletişim: Bayram Tebrik Kartı veya Mektup Yazma',
            'description': 'Bayram kutlaması veya uzaktaki bir akrabaya mektup yazma kurallarını (tarih, hitap, giriş, içerik, dilek ve imza; zarf üzerine adres yazımı) uygular.',
            'process': ['a) Mektup zarfının sol üstüne gönderen, sağ altına alıcı yazıldığını öğrenir.', 'b) Saygı ve sevgi ifadelerini yerinde kullanır.'],
            'concepts': ['Mektup', 'Tebrik Kartı', 'Hitap', 'İmza', 'Zarf Düzeni'],
            'skills': ['Geleneksel Yazışma Kültürü', 'Nezaket'], 'pedagogical': 'PTT iş birliğiyle postaya verilmek üzere gerçek bayram kartları hazırlanır.',
            'context': 'Bayramlaşma ve Mektup Geleneği', 'question': 'Bir mektup zarfının sol üst köşesine ve sağ alt köşesine sırasıyla kimlerin bilgileri yazılır?',
            'solution': 'Sol üst köşeye gönderenin adı, soyadı ve adresi; sağ alt köşeye ise alıcının adı, soyadı ve açık adresi yazılır.', 'weeklyGoal': 'Kurallarına uygun bir tebrik kartı ve mektup hazırlama.',
            'evaluation': 'Mektup ve zarf hazırlama performans görevi'
        },

        # 25-30: 5. Tema: İletişim ve Sosyal İlişkiler
        {
            'theme': 'İletişim ve Sosyal İlişkiler', 'subTheme': 'Etkili İletişim ve Nezaket Kuralları',
            'code': 'TÜR.5.5.1', 'title': 'Sözlü İletişimde Ben Dili - Sen Dili ve Empati',
            'description': 'Karşı tarafı suçlayıcı \'sen dili\' yerine duyguları ve rahatsızlığı ifade eden yapıcı \'ben dili\' kullanımını; dinleme nezaketini ve empatiyi metinler üzerinden modeller.',
            'process': ['a) \'Beni hiç dinlemiyorsun!\' (Sen dili) cümlesini \'Sözüm kesildiğinde kendimi değersiz hissediyorum\' (Ben dili) şekline dönüştürür.', 'b) Çatışmaları çözme yollarını tartışır.'],
            'concepts': ['Etkili İletişim', 'Ben Dili', 'Sen Dili', 'Empati', 'Çözüm Odaklılık'],
            'skills': ['Sosyal-Duygusal Beceriler', 'Diyalog Yönetimi'], 'pedagogical': 'Öğrenciler canlandırma yaparak sen dili ve ben dilinin insan psikolojisindeki etkisini hissederler.',
            'context': 'Sınıf ve Aile İletişimi', 'question': "'Ödevlerini hep aksatıyorsun, çok tembelsin!' diyen bir öğretmenin cümlesi hangi dildir ve ben diline nasıl çevrilir?",
            'solution': "Suçlayıcı 'sen dili'dir. Ben diliyle: 'Ödevlerin zamanında yapılmadığını gördüğümde senin adına endişeleniyorum ve üzülüyorum' şeklinde ifade edilir.", 'weeklyGoal': 'İletişimde ben dilini ve empati yaklaşımını uygulama.',
            'evaluation': 'Ben dili dönüştürme atölyesi formu'
        },
        {
            'theme': 'İletişim ve Sosyal İlişkiler', 'subTheme': 'Karşılaştırma ve Benzerlik Cümleleri',
            'code': 'TÜR.5.5.2', 'title': 'Cümleler Arası Karşılaştırma, Benzerlik ve Farklılık İlişkileri',
            'description': 'İki veya daha fazla varlığın, durumun veya kişinin benzer, farklı ya da üstün yönlerini bildiren cümleleri (\'kadar, gibi, göre, daha, en\') inceler.',
            'process': ['a) \'Sınıfın en çalışkan öğrencisidir\' cümlesindeki üstünlük karşılaştırmasını saptar.', 'b) Kitap ve film uyarlamalarını karşılaştırır.'],
            'concepts': ['Karşılaştırma Cümlesi', 'Daha / En', 'Göre / Kadar', 'Üstünlük'],
            'skills': ['Mukayese Becerisi', 'Analitik Düşünme'], 'pedagogical': 'Radyo ile televizyonun iletişimdeki güçleri karşılaştırmalı tablo yapılır.',
            'context': 'Medya ve İletişim Araçları', 'question': "'Bu yılki kış mevsimi geçen yıla göre çok daha ılık geçti' cümlesindeki anlam ilişkisi nedir?",
            'solution': 'İki farklı yılın kış mevsiminin sıcaklık yönünden \'karşılaştırması\' yapılmıştır.', 'weeklyGoal': 'Karşılaştırma cümlelerini belirleme ve kendi metinlerinde kullanma.',
            'evaluation': 'Karşılaştırma cümleleri tespit föyü'
        },
        {
            'theme': 'İletişim ve Sosyal İlişkiler', 'subTheme': 'Paragrafta Yapı (Giriş, Gelişme, Sonuç)',
            'code': 'TÜR.5.5.3', 'title': 'Paragrafın Bölümleri, Akışı Bozan Cümle ve Düşünceyi Bağlayan İfadeler',
            'description': 'Bir metnin giriş (konuyu tanıtan), gelişme (örneklerin ve detayların verildiği) ve sonuç (özetleyen ve ana fikri bağlayan) bölümlerini; düşüncenin yönünü değiştiren ifadeleri (\'ama, fakat, lakin, oysa, ne var ki, çünkü\') çözümler.',
            'process': ['a) Giriş cümlesinin kendisinden önce bir cümle varmış hissi vermeyeceğini (bağlaçla başlamayacağını) öğrenir.', 'b) Paragrafın anlam bütünlüğünü bozan cümleyi eler.'],
            'concepts': ['Giriş Cümlesi', 'Gelişme', 'Sonuç Cümlesi', 'Düşünceyi Değiştiren İfadeler', 'Akışı Bozan Cümle'],
            'skills': ['Metin Mimarisi', 'Mantıksal Tutarlılık'], 'pedagogical': 'Karışık verilmiş 4 cümle sıralanarak anlamlı bir paragraf oluşturulur.',
            'context': 'Metin Yazarlığı', 'question': "'Bu nedenle çevre kirliliğine karşı acil önlem almalıyız' cümlesi bir metnin giriş cümlesi olabilir mi, neden?",
            'solution': "Olamaz; çünkü 'Bu nedenle' ifadesi kendisinden önce başka cümleler geçtiğini ve bir sonuca bağlandığını gösteren sonuç ifadesidir.", 'weeklyGoal': 'Paragraf bölümlerini ve geçiş-bağlantı ifadelerini doğru yönetme.',
            'evaluation': 'Paragraf tamamlama ve akış düzeltme föyü'
        },
        {
            'theme': 'Ara Tatil', 'subTheme': '2. Dönem Ara Tatili',
            'code': 'TÜR.5.GENEL.2', 'title': 'Geleneklerimiz ve İletişim Becerileri Soru Kampı',
            'description': 'Hâl ekleri, söz sanatları, benzetme-abartma ve paragraf yapı soruları çözülür.',
            'process': ['a) Sözel mantık ve okuduğunu anlama hızını geliştirir.'],
            'concepts': ['Genel Tekrar', 'Muhakeme'], 'skills': ['Hızlı ve Doğru Okuma'],
            'pedagogical': 'Tatil EBA fasikülü uygulanır.', 'context': 'Tatil Kampı',
            'question': 'Düşüncenin yönünü değiştiren geçiş ifadelerine 3 örnek veriniz.',
            'solution': "'Ama', 'fakat', 'ancak' (veya 'lakin', 'ne var ki').",
            'weeklyGoal': '2. dönem Türkçe kazanımlarını pekiştirme.', 'evaluation': 'Ara tatil Türkçe denemesi'
        },
        {
            'theme': 'İletişim ve Sosyal İlişkiler', 'subTheme': 'Dijital İletişim ve Medya Okuryazarlığı',
            'code': 'TÜR.5.5.4', 'title': 'İnternet ve Sosyal Medya İletişim Kuralları (Netiket) ve Güvenilir Kaynak',
            'description': 'Dijital ortamlarda nezaket kurallarını (büyük harfle yazmanın bağırmak anlamına gelmesi, siber zorbalıktan kaçınma); internetteki her bilginin doğru olmadığını ve güvenilir resmî (.gov, .edu) sitelerin tercih edilmesini açıklar.',
            'process': ['a) Dijital ayak izinin kalıcılığını kavrar.', 'b) Kişisel şifre ve bilgilerin internette paylaşılmaması bilincini edinir.'],
            'concepts': ['Dijital Nezaket (Netiket)', 'Siber Zorbalık', 'Güvenilir Bilgi', 'Dijital Ayak İzi'],
            'skills': ['Medya Okuryazarlığı', 'Eleştirel Dijital Bilinç'], 'pedagogical': 'Sahte haber ve bilgi kirliliği örnekleri incelenerek doğrulama yolları tartışılır.',
            'context': 'Güvenli İnternet Günü', 'question': "İnternette e-posta veya mesaj yazarken BÜTÜN KELİMELERİ BÜYÜK HARFLE YAZMAK dijital nezaket kurallarına göre ne anlama gelir?",
            'solution': "Karşı tarafa 'bağırmak, öfkelenmek ve azarlamak' anlamına gelir; bu yüzden kaba kabul edilir.", 'weeklyGoal': 'Bilinçli, güvenli ve saygılı bir dijital iletişim dili benimseme.',
            'evaluation': 'Güvenli dijital iletişim rehberi hazırlama'
        },
        {
            'theme': 'İletişim ve Sosyal İlişkiler', 'subTheme': 'Tartışma ve Münazara Becerisi',
            'code': 'TÜR.5.5.5', 'title': 'Görüş Geliştirme, Kanıt Sunma ve Karşıt Görüşe Saygı',
            'description': 'Bir konu hakkında tez ve antitez oluşturur; kendi görüşlerini kanıtlarla savunurken karşı tarafın görüşlerini sabırla dinleme ve nezaket kurallarına uyma pratiği yapar.',
            'process': ['a) Argümanlarını \'çünkü\' bağlacıyla gerekçelendirir.', 'b) Ses tonunu ve jest-mimiklerini kontrollü kullanır.'],
            'concepts': ['Münazara', 'Argüman / Kanıt', 'Görüş', 'Karşı Görüşe Saygı'],
            'skills': ['İkna Kabiliyeti', 'Demokratik Konuşma'], 'pedagogical': "'Geleneksel oyunlar mı yoksa dijital oyunlar mı çocuk gelişimine daha faydalıdır?' münazarası yapılır.",
            'context': 'Sınıf Münazara Turnuvası', 'question': 'Münazarada bir konuşmacının tezini savunurken yapabileceği en büyük iletişim hatası nedir?',
            'solution': 'Kanıt sunmak yerine karşı tarafın şahsına saldırmak, sözünü kesmek ve sesini öfkeyle yükseltmektir.', 'weeklyGoal': 'Argümanlara dayalı saygılı tartışma kültürünü kazanma.',
            'evaluation': 'Münazara jüri değerlendirme formu'
        },

        # 31-36: 6. Tema: Sağlıklı Yaşıyorum
        {
            'theme': 'Sağlıklı Yaşıyorum', 'subTheme': 'Dengeli Beslenme ve Spor Metinleri',
            'code': 'TÜR.5.6.1', 'title': 'Bilgilendirici Metinlerde Konu, Ana Fikir ve Başlık İlişkisi',
            'description': 'Sağlıklı beslenme, su tüketimi, düzenli uyku ve sporun insan yaşamına katkılarını anlatan metinlerde yazarın iletisini ve başlık-içerik tutarlılığını inceler.',
            'process': ['a) Metinden çıkarılan ana fikri kendi cümleleriyle özetler.', 'b) Metne özgün ve ilgi çekici yeni bir başlık önerir.'],
            'concepts': ['Dengeli Beslenme', 'Yaşam Kalitesi', 'Başlık Uyumu', 'Özet'],
            'skills': ['Metin Yapılandırma', 'Sağlıklı Yaşam Bilinci'], 'pedagogical': 'Öğrenciler 1 haftalık sağlıklı beslenme ve uyku günlüğü tutarlar.',
            'context': 'Beslenme Dostu Okul Projesi', 'question': 'Bir metne başlık seçerken uyulması gereken en temel iki kural nedir?',
            'solution': 'Başlığın metnin konusu ve ana fikriyle doğrudan uyumlu olması ve okuyucuda merak uyandıracak kadar öz ve çarpıcı olmasıdır.', 'weeklyGoal': 'Sağlık temalı metinlerde konu ve başlık uyumunu değerlendirme.',
            'evaluation': 'Metin başlıklandırma ve tahlil föyü'
        },
        {
            'theme': 'Sağlıklı Yaşıyorum', 'subTheme': 'İnfografik, Grafik ve Tablo Okuma',
            'code': 'TÜR.5.6.2', 'title': 'Görsel Okuma: Sağlık İnfografiklerini ve Tabloları Yorumlama',
            'description': 'Görsellerle desteklenmiş veri ve istatistik şemalarını (infografik: besin piramidi, su tüketim cetveli, obezite oranları) okuyarak sözel çıkarımlarda bulunur.',
            'process': ['a) Grafikteki uç değerleri ve artış-azalış eğilimlerini yorumlar.', 'b) Görseldeki sembol ve renklerin ne anlama geldiğini açıklar.'],
            'concepts': ['İnfografik', 'Görsel Okuma', 'Besin Piramidi', 'Veri Grafiği', 'Çıkarım'],
            'skills': ['Çoklu Okuryazarlık', 'Görsel-Metin Entegrasyonu'], 'pedagogical': 'Sağlık Bakanlığı besin piramidi infografiği üzerinde soru-cevap çalışması yapılır.',
            'context': 'Sağlık İstatistikleri ve İnfografik', 'question': 'Bir besin piramidinde en altta yer alan geniş gruptan en üstteki dar gruba doğru gidildikçe tüketim miktarı nasıl olmalıdır?',
            'solution': 'En alttaki tahıllar ve su en çok tüketilmeli; en üstteki şeker ve doymuş yağlar ise en az (sınırlı) tüketilmelidir.', 'weeklyGoal': 'İnfografik ve tablolardan doğru sözel çıkarımlar yapabilme.',
            'evaluation': 'İnfografik çözümleme ve soru föyü'
        },
        {
            'theme': 'Sağlıklı Yaşıyorum', 'subTheme': 'Düşünceyi Geliştirme Yolları (Örnekleme ve Tanımlama)',
            'code': 'TÜR.5.6.3', 'title': 'Yazarın Düşüncelerini Açıklama Teknikleri: Tanımlama ve Örnekleme',
            'description': '\'Bu nedir?\' sorusunun cevabı olan tanımlama cümleleri (\'Sağlık, insanın bedenen ve ruhen tam bir iyilik hâlidir\') ile soyut fikri somutlaştıran örneklemeleri metinde belirler.',
            'process': ['a) Tanımlama cümlelerinin genellikle \'-dır/-dir\' ile bittiğini fark eder.', 'b) \'Örneğin, mesela, söz gelimi\' bağlayıcılarını inceler.'],
            'concepts': ['Düşünceyi Geliştirme', 'Tanımlama', 'Örnekleme', 'Açıklama'],
            'skills': ['Anlatım Tekniklerini Çözümleme', 'Metin Eleştirisi'], 'pedagogical': 'Tanımlama ve örnekleme içeren paragrafların formülü sınıfta çözümlenir.',
            'context': 'Tıp ve Yaşam Rehberi', 'question': "'Spor, vücudun zinde kalmasını sağlayan planlı fiziksel aktivitelerdir. Örneğin yüzme, koşu ve basketbol kasları güçlendirir.' Bu parçada hangi iki düşünceyi geliştirme yolu kullanılmıştır?",
            'solution': "Birinci cümlede 'tanımlama' (Spor nedir?), ikinci cümlede ise 'örnekleme' yapılmıştır.", 'weeklyGoal': 'Tanımlama ve örnekleme tekniklerini metinlerde doğru tespit etme.',
            'evaluation': 'Düşünceyi geliştirme yolları föyü'
        },
        {
            'theme': 'Sağlıklı Yaşıyorum', 'subTheme': 'Sözel Mantık ve Akıl Yürütme',
            'code': 'TÜR.5.6.4', 'title': 'İpuçlarından Yararlanarak Tablo Çizme ve Sözel Mantık Çözümü',
            'description': 'Verilen kurallardan ve olumsuz önermelerden hareketle sıralama veya eşleştirme tablosu oluşturarak kesin doğru bilgilere mantık yoluyla ulaşır.',
            'process': ['a) Olumsuz veya kesin olmayan ihtimalleri eler.', 'b) Tablo kurarak akıl yürütür.'],
            'concepts': ['Sözel Mantık', 'Tablo Oluşturma', 'İpucu', 'Kesin Bilgi', 'Olasılık Eleme'],
            'skills': ['Muhakeme Becerisi', 'Sistematik Düşünme'], 'pedagogical': '4 arkadaşın haftalık spor günleri tablosu adım adım ipuçlarıyla doldurulur.',
            'context': 'LGS Hazırlık Temeli', 'question': "Ali, Burak ve Can'dan Ali basketbol oynamaktadır. Can futbol oynamadığına göre ve geriye futbol ile voleybol kaldığına göre Can hangi sporu yapar?",
            'solution': 'Can futbol oynamadığına göre mecburen voleybol oynamaktadır; Burak ise futbol oynamaktadır.', 'weeklyGoal': 'Sözel mantık problemlerinde tablo kurarak kesin sonuca ulaşma.',
            'evaluation': 'Sözel mantık çalışma fasikülü'
        },
        {
            'theme': 'Sağlıklı Yaşıyorum', 'subTheme': 'Yazma Becerisi: Sağlıklı Yaşam Afişi ve Slogan',
            'code': 'TÜR.5.6.5', 'title': 'Çarpıcı Slogan Üretme ve Bilgilendirici Afiş / Broşür Tasarımı',
            'description': 'Abur cubur ve hareketsiz yaşama karşı akılda kalıcı sloganlar üreterek okul panosunda sergilenecek görsel ve metin dengeli bir sağlıklı yaşam broşürü tasarlar.',
            'process': ['a) Kısa, kafiyeli ve etkileyici sloganlar bulur.', 'b) Görsel ile metnin uyumunu sağlar.'],
            'concepts': ['Slogan', 'Afiş Tasarımı', 'Broşür', 'İkna Edici Yazarlık'],
            'skills': ['Yaratıcı Tasarım', 'Kitle İletişimi'], 'pedagogical': 'Sağlıklı yaşam sloganları yarışması yapılarak okul kantininde sergilenir.',
            'context': 'Okul Sağlığı Kampanyası', 'question': 'Etkili bir sloganın taşıması gereken en önemli 3 özellik nedir?',
            'solution': 'Kısa ve akılda kalıcı olması, ritimli/çarpıcı bir dille yazılması ve vermek istediği mesajı doğrudan iletmesidir.', 'weeklyGoal': 'Çarpıcı bir slogan eşliğinde bilgilendirici afiş tasarlama.',
            'evaluation': 'Afiş ve slogan tasarım rubriği'
        },
        {
            'theme': 'Sağlıklı Yaşıyorum', 'subTheme': 'Yıl Sonu Sentezi ve Maarif Portfolyosu',
            'code': 'TÜR.5.6.6', 'title': 'Türkiye Yüzyılı Maarif Modeli 5. Sınıf Türkçe Yıl Sonu Sentezi',
            'description': '6 temanın anlama (dinleme/okuma) ve anlatma (konuşma/yazma) kazanımlarını, kitap okuma listesini ve yazarlık ürünlerini kapsayan portfolyo sunumu yapar; 6. sınıfa hazır bulunuşluk düzeyini belirler.',
            'process': ['a) Öz değerlendirme formunu doldurur.', 'b) Yaz tatili için nitelikli kitap okuma listesi oluşturur.'],
            'concepts': ['Yıl Sonu Sentezi', 'Portfolyo', 'Yazarlık Gelişimi', 'Maarif Modeli'],
            'skills': ['Sunum Becerisi', 'Öz Yansıtma'], 'pedagogical': 'Öğrenciler yıl boyu yazdıkları hikaye, mektup, şiir ve günlüklerden oluşan kişisel kitapçıklarını sergilerler.',
            'context': 'Maarif Türkçe Şenliği', 'question': '5. sınıf Türkçe dersinin temel amacı öğrenciye hangi 4 temel dil becerisini kazandırmaktır?',
            'solution': 'Dinleme/İzleme, Okuma, Konuşma ve Yazma olmak üzere dört temel dil becerisini bütüncül olarak kazandırmaktır.', 'weeklyGoal': '5. sınıf Türkçe öğretim programını başarıyla tamamlama.',
            'evaluation': '5. Sınıf Yıl Sonu Türkçe Başarı Sertifikası'
        }
    ]
    return {
        'title': '5. Sınıf',
        'subtitle': 'Türkiye Yüzyılı Maarif Modeli (6 Tema)',
        'badge': 'Maarif Modeli ✨',
        'weeks': weeks
    }

print("Turkce 5 builder compiled.")
