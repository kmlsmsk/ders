# -*- coding: utf-8 -*-
"""
Generates 36 weeks for Grade 8 (LGS) Fen Bilimleri.
"""

def build_fen_8():
    # 8. Sınıf LGS Fen Bilimleri Müfredatı
    weeks = [
        # 1-5: Mevsimler ve İklim
        {
            'theme': 'Mevsimler ve İklim', 'subTheme': 'Mevsimlerin Oluşumu',
            'code': 'FEN.8.1.1', 'title': 'Dünya\'nın Dönme Ekseni Eğikliği ve Dolanma Hareketi',
            'description': 'Dünya\'nın 23° 27\'lik eksen eğikliği ve Güneş etrafında dolanması sonucu güneş ışınlarının geliş açısının değiştiğini; mevsimlerin oluşumunu modeller.',
            'process': ['a) 21 Haziran, 23 Eylül, 21 Aralık ve 21 Mart gün dönümü ve ekinoks tarihlerini çözümler.', 'b) Işığın dik geldiği yarım kürede yaz, eğik geldiği yarım kürede kış yaşandığını açıklar.'],
            'concepts': ['Eksen Eğikliği (23° 27\')', 'Geliş Açısı', 'Gün Dönümü (Solstis)', 'Ekinoks (Gece-Gündüz Eşitliği)', 'Birim Yüzeye Düşen Enerji'],
            'skills': ['Uzamsal Mantık Yürütme', 'LGS Yeni Nesil Çıkarım'], 'pedagogical': 'Işık dik geldiğinde dar alanı aydınlatıp yüksek ısı verirken, eğik geldiğinde geniş alana yayıldığı fenerle modellenir.',
            'context': 'LGS Soru Formatı / Coğrafi Felsefe', 'question': '21 Aralık tarihinde Güney Yarım Küre\'de en uzun gündüz yaşanırken Kuzey Yarım Küre\'de hangi durum gözlenir?',
            'solution': 'Kuzey Yarım Küre\'de en uzun gece ve en kısa gündüz yaşanır; kış mevsimi başlangıcıdır.', 'weeklyGoal': 'Mevsimlerin oluşumunu eksen eğikliği ve geliş açısıyla açıklama.',
            'evaluation': 'Mevsimler ve ışık açısı analizi testi'
        },
        {
            'theme': 'Mevsimler ve İklim', 'subTheme': 'Gölge Boyu ve Gece-Gündüz Süreleri',
            'code': 'FEN.8.1.1', 'title': 'Işığın Geliş Açısı, Gölge Boyu ve Gece-Gündüz Süresi Değişimi',
            'description': 'Öğle vakti dik açıyla gelen ışınlarda gölge boyunun en kısa; eğik açıda en uzun olduğunu; yazın gündüzlerin, kışın gecelerin uzun olduğunu grafiklerle analiz eder.',
            'process': ['a) Yıl boyunca gölge boyu değişim grafiklerini yorumlar.', 'b) Ekinoks tarihlerinde (21 Mart - 23 Eylül) Dünya\'nın her yerinde 12 saat gündüz 12 saat gece olduğunu belirtir.'],
            'concepts': ['Gölge Boyu', 'Öğle Vakti', 'Gece-Gündüz Süresi', 'Aydınlanma Çemberi'],
            'skills': ['Grafik Çözümleme', 'Veri Analizi'], 'pedagogical': 'Farklı enlemlerdeki şehirlerin (örneğin Sinop ve Hatay) yıl içi gölge boyu grafikleri karşılaştırılır.',
            'context': 'Navigasyon ve Güneş Saatleri', 'question': 'Kuzey Yarım Küre\'de yaşayan bir öğrencinin öğle vakti ölçtüğü gölge boyunun yıl içindeki en kısa olduğu tarih hangisidir?',
            'solution': 'Güneş ışınlarının en dik açıyla geldiği 21 Haziran (yaz gün dönümü) tarihidir.', 'weeklyGoal': 'Gölge boyu ve gece-gündüz süresi grafiklerini yorumlayabilme.',
            'evaluation': 'Gölge boyu grafik değerlendirme föyü'
        },
        {
            'theme': 'Mevsimler ve İklim', 'subTheme': 'İklim ve Hava Olayları',
            'code': 'FEN.8.1.2', 'title': 'Klimatoloji ve Meteoroloji Arasındaki Farklar',
            'description': 'Dar bir alanda kısa sürede değişkenlik gösteren hava olayları (meteoroloji) ile geniş bir bölgede uzun yıllar boyunca süregelen ortalama hava şartlarını (klimatoloji/iklim) ayırt eder.',
            'process': ['a) \'Yarın Ankara\'da kar bekleniyor\' ifadesinin hava olayı olduğunu belirtir.', 'b) \'Akdeniz bölgesinde yazlar sıcak ve kuraktır\' ifadesinin iklim olduğunu açıklar.'],
            'concepts': ['Hava Olayı', 'İklim', 'Meteoroloji', 'Meteorolog', 'Klimatoloji', 'Klimatolog'],
            'skills': ['Kavramsal Ayrıştırma', 'Metin Analizi'], 'pedagogical': 'Haber bülteni hava durumu ve coğrafi iklim haritası karşılaştırılarak tablo yapılır.',
            'context': 'Hava Tahmin Raporları', 'question': 'Meteorologlar ile klimatologların inceleme alanları ve çalışma süreleri arasındaki temel fark nedir?',
            'solution': 'Meteorologlar dar bir alanda günlük/haftalık değişken hava olaylarını incelerken; klimatologlar geniş bir alanda 35-40 yıllık ortalama verileri inceler.', 'weeklyGoal': 'İklim ve hava durumu cümlelerini hatasız sınıflandırma.',
            'evaluation': 'İklim-Hava Olayı eşleştirme etkinliği'
        },
        {
            'theme': 'Mevsimler ve İklim', 'subTheme': 'Hava Olayları ve Rüzgâr Oluşumu',
            'code': 'FEN.8.1.2', 'title': 'Yüksek Basınç (Alçalıcı Hava) - Alçak Basınç (Yükselici Hava) ve Rüzgâr',
            'description': 'Sıcak havanın yoğunluğunun azalarak yükselip alçak basınç alanı (bulutlu, yağışlı); soğuk havanın alçalarak yüksek basınç alanı (açık, güneşli) oluşturduğunu ve rüzgârın Yüksek Basınçtan Alçak Basınca estiğini modeller.',
            'process': ['a) Rüzgârın daima soğuktan sıcağa (YB -> AB) doğru estiğini kavrar.', 'b) Yağmur, kar, dolu (gökyüzüne yakın); sis, çiy, kırağı (yeryüzüne yakın) oluşumlarını açıklar.'],
            'concepts': ['Alçak Basınç Alanı', 'Yüksek Basınç Alanı', 'Rüzgâr', 'Yükselici Hava', 'Alçalıcı Hava', 'Kırağı', 'Çiy'],
            'skills': ['Basınç Gradyanı Analizi', 'Hava Olayı Şemalaştırma'], 'pedagogical': 'İki mum ve rüzgârgülüyle sıcak havanın yükselip rüzgâr oluşturması gösterilir.',
            'context': 'LGS Banko Soru Modeli', 'question': 'A şehri soğuk (yüksek basınç), B şehri sıcak (alçak basınç) olduğuna göre rüzgâr hangi şehirden hangisine doğru eser?',
            'solution': 'Rüzgâr daima Yüksek Basınçtan Alçak Basınca doğru (soğuktan sıcağa) estiğinden A şehrinden B şehrine doğru eser.', 'weeklyGoal': 'Rüzgâr yönünü ve basınç alanlarını eksiksiz belirleme.',
            'evaluation': 'Basınç alanları ve rüzgâr yönü föyü'
        },
        {
            'theme': 'Mevsimler ve İklim', 'subTheme': 'Küresel İklim Değişikliği',
            'code': 'FEN.8.1.3', 'title': 'Sera Etkisi, Fosil Yakıtlar, Küresel Isınma ve Önlemler',
            'description': 'Karbondioksit ve metan gibi sera gazlarının atmosferde birikerek dünyayı ısıtmasını (sera etkisi); buzulların erimesi, kuraklık ve aşırı hava olayları gibi sonuçlarını ve Paris İklim Anlaşması bilincini irdeler.',
            'process': ['a) Karbon ayak izini azaltma yollarını listeler.', 'b) Yenilenebilir enerjinin önemini savunur.'],
            'concepts': ['Sera Etkisi', 'Sera Gazları (CO2, CH4)', 'Küresel Isınma', 'Karbon Ayak İzi', 'İklim Krizi'],
            'skills': ['Çevresel Sorumluluk', 'Veriye Dayalı Raporlama'], 'pedagogical': 'Kavanoz içi termometre ile sera etkisi ısı artışı deneyi yapılır.',
            'context': 'Birleşmiş Milletler İklim Zirvesi', 'question': 'Fosil yakıt tüketiminin aşırı artması sera etkisini nasıl tetikler ve sonuçları nelerdir?',
            'solution': 'Atmosfere salınan CO2 gazı battaniye gibi Dünya\'dan yansıyan ısıyı hapseder, ortalama sıcaklıkları yükselterek buzulların erimesine ve kuraklığa yol açar.', 'weeklyGoal': 'Küresel iklim değişikliğinin neden ve sonuçlarını bilimsel verilerle savunma.',
            'evaluation': '1. Ünite LGS Deneme Testi'
        },

        # 6-12: DNA ve Genetik Kod
        {
            'theme': 'DNA ve Genetik Kod', 'subTheme': 'DNA\'nın Yapısı ve Nükleotidler',
            'code': 'FEN.8.2.1', 'title': 'Nükleotidler, Organik Bazlar (A, T, G, C) ve DNA Çift Sarmalı',
            'description': 'DNA\'nın çift zincirli sarmal yapısını; bir nükleotidin Fosfat + Deoksiriboz Şekeri + Organik Bazdan oluştuğunu; Adenin karşısına Timin, Guanin karşısına Sitozin geldiğini modeller.',
            'process': ['a) Toplam Nükleotid Sayısı = Fosfat Sayısı = Şeker Sayısı = Toplam Baz Sayısı kuralını uygular.', 'b) A ile T arasında ikili, G ile C arasında üçlü hidrojen bağı olduğunu kavrar.'],
            'concepts': ['DNA', 'Nükleotid', 'Adenin', 'Timin', 'Guanin', 'Sitozin', 'Deoksiriboz', 'Fosfat'],
            'skills': ['Moleküler Matematik', 'Sarmal Modelleme'], 'pedagogical': 'Origami veya renkli boncuklarla DNA çift sarmal modeli yaptırılır.',
            'context': 'LGS DNA Modelleme Soruları', 'question': 'Bir DNA zincirinde 400 Adenin, 600 Guanin nükleotidi varsa bu DNA molekülünde toplam kaç adet deoksiriboz şekeri bulunur?',
            'solution': 'A=T=400, G=C=600. Toplam nükleotid = 400 + 400 + 600 + 600 = 2000. Nükleotid sayısı şeker sayısına eşit olduğundan 2000 adet deoksiriboz şekeri vardır.', 'weeklyGoal': 'DNA nükleotid eşleşmelerini ve sayısal eşitliklerini hatasız çözme.',
            'evaluation': 'DNA nükleotid hesaplama çalışma yaprağı'
        },
        {
            'theme': 'DNA ve Genetik Kod', 'subTheme': 'DNA\'nın Kendini Eşlemesi (Replikasyon)',
            'code': 'FEN.8.2.1', 'title': 'DNA Replikasyon Aşamaları ve Hata Onarımı',
            'description': 'Hücre bölünmesi öncesi DNA\'nın fermuar gibi açılmasını, sitoplazmadaki serbest nükleotidlerin çekirdeğe girerek kalıp zincirleri tamamlamasını ve birbirinin tıpatıp aynısı 2 yeni DNA oluşmasını modeller.',
            'process': ['a) Yanlış eşleşmelerin (ör. A karşısına G gelmesi) enzimlerle onarılabileceğini kavrar.', 'b) Karşılıklı iki zincirin de boş kaldığı hasarların onarılamayarak mutasyona yol açtığını gösterir.'],
            'concepts': ['Replikasyon (Eşleme)', 'Kalıp Zincir', 'Fermuar Modeli', 'Hata Onarımı', 'Eşit DNA Kopyası'],
            'skills': ['Süreç Basamaklarını Sıralama', 'Hata Analizi'], 'pedagogical': 'Fermuarlı bir hırka ile iki ayrılan kol ve yeni dişlilerin takılması canlandırılır.',
            'context': 'Moleküler Biyoloji Laboratuvarı', 'question': 'DNA eşlenmesi sırasında tek bir zincirde yanlış baz gelirse onarılabilir mi? İki zincir birden karşılıklı boş kalırsa onarılabilir mi?',
            'solution': 'Tek zincirdeki hata kalıp zincire bakılarak onarılabilir; ancak karşılıklı iki zincir birden boşsa DNA neyin geleceğini bilemez ve onarılamaz (mutasyon oluşur).', 'weeklyGoal': 'DNA replikasyon aşamalarını ve onarılabilirlik durumlarını açıklama.',
            'evaluation': 'DNA eşlenmesi sıralama kartları'
        },
        {
            'theme': 'DNA ve Genetik Kod', 'subTheme': 'Kalıtım ve Mendel Genetiği',
            'code': 'FEN.8.2.2', 'title': 'Genotip, Fenotip, Baskın (Dominant) ve Çekinik (Resesif) Genler',
            'description': 'Mendel\'in bezelye deneylerini; homozigot (saf döl: AA, aa) ve heterozigot (melez döl: Aa) kavramlarını; dış görünüşün (fenotip) genlerin (genotip) etkisiyle nasıl belirlendiğini açıklar.',
            'process': ['a) Baskın genin büyük harfle (A), çekinik genin küçük harfle (a) gösterildiğini öğrenir.', 'b) Çekinik özelliğin fenotipte ortaya çıkabilmesi için mutlaka saf çekinik (aa) olması gerektiğini kavrar.'],
            'concepts': ['Genotip', 'Fenotip', 'Baskın (Dominant)', 'Çekinik (Resesif)', 'Homozigot (Saf)', 'Heterozigot (Melez)'],
            'skills': ['Genetik Terminoloji Kullanımı', 'Fenotip-Genotip Analizi'], 'pedagogical': 'Kahverengi göz (baskın) ve mavi göz (çekinik) aile soyağaçları incelenir.',
            'context': 'Mendel\'in Bezelye Bahçesi', 'question': 'Melez sarı tohumlu bezelye ile yeşil tohumlu bezelyenin genotipleri nasıl sembolize edilir? (Sarı tohum geni yeşile baskındır)',
            'solution': 'Melez sarı: Ss (heterozigot), yeşil tohumlu: ss (homozigot çekinik).', 'weeklyGoal': 'Genetik terimleri ve çaprazlama sembollerini doğru kavrama.',
            'evaluation': 'Genotip-Fenotip eşleştirme föyü'
        },
        {
            'theme': 'DNA ve Genetik Kod', 'subTheme': 'Monohibrit Çaprazlamalar',
            'code': 'FEN.8.2.2', 'title': 'Punnett Karesi ile Tek Karakter Çaprazlamaları ve Olasılık Hesapları',
            'description': 'İki melez bireyin çaprazlanması (Aa x Aa) sonucu oluşabilecek genotip (%25 AA, %50 Aa, %25 aa) ve fenotip (%75 baskın, %25 çekinik) oranlarını Punnett karesiyle hesaplar.',
            'process': ['a) Her doğumda ortaya çıkacak karakter olasılığının bağımsız bir olasılık (%50 kız, %50 erkek) olduğunu açıklar.', 'b) LGS çaprazlama ihtimal problemlerini çözer.'],
            'concepts': ['Çaprazlama', 'Punnett Karesi', 'Genotip Oranı', 'Fenotip Oranı', 'Bağımsız Olasılık'],
            'skills': ['İstatistiki Olasılık Hesabı', 'Tablo Çözümleme'], 'pedagogical': 'Madeni para atma deneyiyle her atışta yazı-tura şansının %50 olduğu gösterilir.',
            'context': 'LGS Genetik Soruları', 'question': 'Heterozigot iki kahverengi gözlü anne ve babanın (Aa x Aa) mavi gözlü (aa) bir çocuklarının olma ihtimali yüzde kaçtır?',
            'solution': 'Çaprazlama: AA, Aa, Aa, aa. 4 olasılıktan 1\'i \'aa\' dır, yani %25 (1/4) ihtimaldir.', 'weeklyGoal': 'Mendel çaprazlamalarını ve yüzde olasılıklarını hatasız hesaplama.',
            'evaluation': 'Çaprazlama problemleri test föyü'
        },
        {
            'theme': 'Ara Tatil', 'subTheme': '1. Dönem Ara Tatili',
            'code': 'FEN.8.GENEL.1', 'title': 'Mevsimler, İklim ve DNA Konuları LGS Soru Kampı',
            'description': 'LGS çıkmış sorular ve MEB örnek soruları üzerinden ilk 9 haftanın analizi yapılır.',
            'process': ['a) Yeni nesil grafik ve deney sorularını çözer.', 'b) Hata yaptığı kazanımları pekiştirir.'],
            'concepts': ['LGS Hazırlık', 'Soru Çözüm Stratejileri'], 'skills': ['Zaman Yönetimi', 'Kritik Okuma'],
            'pedagogical': 'MEB örnek soru analiz fasikülü uygulanır.', 'context': 'LGS Kampı',
            'question': 'İnsanda çocuğun cinsiyetini anneden gelen yumurta mı yoksa babadan gelen sperm mi belirler?',
            'solution': 'Babadan gelen sperm belirler (anne daima X verir, babadan X gelirse kız XX, Y gelirse erkek XY olur).',
            'weeklyGoal': 'LGS fen deneme sorularında eksiksiz net çıkarma.', 'evaluation': 'LGS 1. Ara Tatil Deneme Sınavı'
        },
        {
            'theme': 'DNA ve Genetik Kod', 'subTheme': 'Akraba Evliliği, Mutasyon ve Modifikasyon',
            'code': 'FEN.8.2.3', 'title': 'Akraba Evliliğinin Genetik Riskleri ve Mutasyon - Modifikasyon Farkı',
            'description': 'Akraba evliliğinde çekinik hastalık genlerinin bir araya gelme olasılığının yüksek olduğunu; DNA yapısının değişmesi olan mutasyon (van kedisi, orak hücre, albinoluk) ile fenotipteki geçici değişim olan modifikasyonu (Himalaya tavşanı, çuha çiçeği, arı sütü) ayırt eder.',
            'process': ['a) Modifikasyonların kalıtsal olmadığını, çevre şartları (ısı, ışık, besin) etkisiyle genlerin işleyişinin değiştiğini kavrar.', 'b) Radyasyon ve kimyasalların mutasyona sebep olduğunu açıklar.'],
            'concepts': ['Akraba Evliliği', 'Mutasyon', 'Modifikasyon', 'Genin Yapısı', 'Genin İşleyişi', 'Kalıtsal Olmayan Değişim'],
            'skills': ['Karşılaştırmalı Muhakeme', 'Tablo Çıkarımı'], 'pedagogical': 'Kas geliştiren sporcunun çocuğunun kaslı doğmaması örneğiyle modifikasyonun kalıtsal olmadığı gösterilir.',
            'context': 'Tıbbi Genetik', 'question': '16 °C\'de yetiştirilen sirke sineğinin düz kanatlı, 25 °C\'de yetiştirilenin kıvrık kanatlı olması mutasyon mudur modifikasyon mudur ve neden?',
            'solution': 'Modifikasyondur; çünkü sıcaklık etkisiyle genin yapısı değil işleyişi değişmiştir ve sıcaklık normale döndüğünde yeni nesiller normal kanatlı doğar.', 'weeklyGoal': 'Mutasyon ve modifikasyon örneklerini hatasız sınıflandırma.',
            'evaluation': 'Mutasyon-Modifikasyon Venn şeması föyü'
        },
        {
            'theme': 'DNA ve Genetik Kod', 'subTheme': 'Adaptasyon ve Biyoteknoloji',
            'code': 'FEN.8.2.4', 'title': 'Doğal Seçilim, Varyasyon, Adaptasyon ve Biyoteknolojik Uygulamalar',
            'description': 'Canlıların yaşama ve üreme şansını artıran kalıtsal uyumları (adaptasyon: kaktüs yaprakları, kutup ayısı kürk rengi); güçlü olanın hayatta kalmasını (doğal seçilim); gen aktarımı, klonlama ve gen tedavisi gibi biyoteknolojik çalışmaları inceler.',
            'process': ['a) Biyoteknolojinin tıp (insülin hormonu üretimi), tarım ve sanayideki yararlarını ve risklerini (GDO, biyoçeşitlilik kaybı) tartışır.', 'b) Dolly\'nin klonlanması aşamalarını açıklar.'],
            'concepts': ['Adaptasyon', 'Doğal Seçilim', 'Varyasyon (Çeşitlilik)', 'Klonlama', 'Gen Aktarımı', 'GDO', 'Genetik Mühendisliği'],
            'skills': ['Biyoetik Değerlendirme', 'Evrimsel Uyum Mantığı'], 'pedagogical': 'Biyoteknolojinin geleceği üzerine sınıf münazarası düzenlenir.',
            'context': 'Gen Teknolojileri ve Dolly', 'question': 'Kutup ayılarının beyaz kürk rengine, kalın yağ tabakasına ve geniş ayak tabanlarına sahip olması hangi kavrama örnektir ve kalıtsal mıdır?',
            'solution': 'Adaptasyondur; soğuk ortamda kamufle olma, sıcak kalma ve karda batmama avantajı sağlar ve dölden döle aktarılan kalıtsal bir özelliktir.', 'weeklyGoal': 'Adaptasyon özelliklerini ve biyoteknolojik gelişmeleri değerlendirme.',
            'evaluation': 'Biyoteknoloji etik paneli sunumu'
        },

        # 13-17: Basınç
        {
            'theme': 'Basınç', 'subTheme': 'Katı Basıncı ve Değişkenleri',
            'code': 'FEN.8.3.1', 'title': 'Katı Basıncının Ağırlık ve Yüzey Alanıyla İlişkisi (P = G / S)',
            'description': 'Birim yüzeye dik etki eden kuvvete basınç (Pascal - Pa) dendiğini; katı basıncının ağırlık (kuvvet) arttıkça arttığını, temas yüzey alanı arttıkça azaldığını deneylerle gösterir.',
            'process': ['a) Bıçak ağzının bilenerek yüzey alanının küçültülüp basıncın artırıldığını kavrar.', 'b) Kar ayakkabısı, traktör tekerleği ve fil ayaklarının geniş tabanlı yapılarak basıncın azaltıldığını modeller.'],
            'concepts': ['Katı Basıncı (P)', 'Ağırlık / Kuvvet (G)', 'Yüzey Alanı (S)', 'Pascal (Pa)', 'Ters Orantı'],
            'skills': ['Değişken Denetimi', 'Teknik Uygulama'], 'pedagogical': 'Sünger üzerine konulan tuğlanın dik ve yatay konumda süngere batma derinlikleri cetvelle ölçülür.',
            'context': 'Mühendislik ve Ağır Araçlar', 'question': 'Aynı ağırlıktaki iki ayakkabıdan biri sivri topuklu diğeri düz geniş tabanlıdır. Sivri topuklu ayakkabının kumda daha çok batmasının sebebi nedir?',
            'solution': 'Yüzey alanı çok küçük olduğu için zemine uyguladığı katı basıncı çok daha büyüktür (Basınç yüzey alanıyla ters orantılıdır).', 'weeklyGoal': 'Katı basıncını formül ve günlük yaşam örnekleriyle analiz etme.',
            'evaluation': 'Katı basıncı deney föyü'
        },
        {
            'theme': 'Basınç', 'subTheme': 'Sıvı Basıncı ve Değişkenleri',
            'code': 'FEN.8.3.1', 'title': 'Sıvı Basıncının Derinlik ve Yoğunlukla İlişkisi (P = h x d x g)',
            'description': 'Sıvıların temas ettikleri tüm yüzeylere basınç uyguladığını; sıvı basıncının derinlik (h) ve sıvının yoğunluğu (d) ile doğru orantılı olduğunu; kabın şekline ve sıvı miktarına bağlı OLMADIĞINI modeller.',
            'process': ['a) Su dolu şişeye farklı yüksekliklerde açılan deliklerden en alttakinin suyu en uzağa fışkırttığını deneyler.', 'b) Su ve zeytinyağında derinlik-basınç grafiğini çizer.'],
            'concepts': ['Sıvı Basıncı', 'Derinlik (h)', 'Sıvı Yoğunluğu (d)', 'Kabın Şeklinden Bağımsızlık'],
            'skills': ['Kontrollü Deney Çözümleme', 'LGS Şekil Analizi'], 'pedagogical': 'Farklı şekillerdeki birleşik kaplarda sıvı seviyelerinin eşit olduğu gösterilir.',
            'context': 'Baraj Duvarları Tasarımı', 'question': 'Hidroelektrik baraj duvarlarının taban kısmının tepe kısmına göre çok daha kalın inşa edilmesinin sıvı basıncı açısından sebebi nedir?',
            'solution': 'Suyun derinliği arttıkça tabandaki sıvı basıncı çok büyük değerlere ulaştığından, yüksek basınca dayanabilmesi için duvar altları kalın yapılır.', 'weeklyGoal': 'Sıvı basıncının derinlik ve yoğunluk bağımlılığını ispatlama.',
            'evaluation': 'Sıvı basıncı deney föyü ve grafikleri'
        },
        {
            'theme': 'Basınç', 'subTheme': 'Pascal Prensibi ve Sıvı Teknolojileri',
            'code': 'FEN.8.3.1', 'title': 'Sıvıların Sıkıştırılamazlığı ve Pascal Prensibi Uygulamaları',
            'description': 'Kapalı bir kaptaki sıvıya uygulanan basıncın sıvının temas ettiği her noktaya ve her yöne aynı büyüklükte iletildiğini (Pascal Prensibi); hidrolik fren, oto kaldırma lifti ve berber koltuğu tasarımlarıyla açıklar.',
            'process': ['a) Küçük bir kuvvetle büyük yüklerin kaldırılabilmesini modeller (kuvvetten kazanç).', 'b) İlaçlama pompası ve su cenderesini çözümler.'],
            'concepts': ['Pascal Prensibi', 'Basınç İletimi', 'Hidrolik Sistemler', 'Su Cenderesi', 'Kuvvet Kazancı'],
            'skills': ['Mekanik Sistem Modelleme', 'Kuvvet ve Alan Oranı'], 'pedagogical': 'İki farklı çapta şırınga ve serum hortumuyla hidrolik kepçe kolu yapılır.',
            'context': 'Oto Tamirhaneleri ve Kamyon Damperleri', 'question': 'Ağır bir otomobilin küçük bir fren pedalına hafifçe basılarak durdurulabilmesi sıvıların hangi fiziksel özelliği sayesinde gerçekleşir?',
            'solution': 'Sıvıların sıkıştırılamaması ve uygulanan basıncı Pascal Prensibi uyarınca tekerlek balatalarına aynen iletmesi sayesinde gerçekleşir.', 'weeklyGoal': 'Pascal Prensibinin teknolojideki uygulamalarını şematize etme.',
            'evaluation': 'Pascal prensibi tasarım şeması föyü'
        },
        {
            'theme': 'Basınç', 'subTheme': 'Gaz Basıncı ve Açık Hava Basıncı',
            'code': 'FEN.8.3.1', 'title': 'Toriçelli Deneyi, Açık Hava Basıncı (P0) ve Kapalı Kap Gaz Basıncı',
            'description': 'Atmosferin ağırlığından dolayı cisimlere basınç uyguladığını (Torricelli\'nin cıva deneyi: 76 cm-Hg); deniz seviyesinden yukarılara çıkıldıkça açık hava basıncının azaldığını; kapalı kaplarda gaz basıncının manometreyle ölçüldüğünü açıklar.',
            'process': ['a) İçi hava dolu vanuzların yapışması (Magdeburg küreleri) ve meyve suyu kutusunun büzüşmesini açık hava basıncıyla modeller.', 'b) Düdüklü tencere ve araç hava yastıklarını inceler.'],
            'concepts': ['Açık Hava Basıncı (Barometre)', 'Toriçelli Deneyi', '76 cm Cıva', 'Yükseklik Faktörü', 'Manometre'],
            'skills': ['Basınç Dengesi Kurma', 'Atmosferik Olay Analizi'], 'pedagogical': 'Ağzına kadar su dolu bardağın üzerine kâğıt kapatılıp ters çevrildiğinde suyun dökülmediği gösterilir.',
            'context': 'Dağcılık ve Uçak Kabin Basıncı', 'question': 'Toriçelli deneyinde 0 °C deniz seviyesinde cam borudaki cıva yüksekliğinin 76 cm olmasının nedeni nedir?',
            'solution': 'Çanağın yüzeyine etki eden açık hava basıncının, cam borudaki 76 cm yüksekliğindeki cıvanın yaptığı basınca eşit olup dengelemesidir.', 'weeklyGoal': 'Açık hava basıncının varlığını ve değişkenlerini kanıtlama.',
            'evaluation': 'Gaz basıncı deney föyü'
        },
        {
            'theme': 'Basınç', 'subTheme': 'Basınç Ünite Sentezi ve Dönem Sonu Sınavı',
            'code': 'FEN.8.3.2', 'title': 'Basınç Becerileri Sentezi ve 1. Dönem LGS Net Analizi',
            'description': 'Katı, sıvı ve gaz basıncı konularının bileşik grafik ve deney düzenekli yeni nesil LGS soruları çözülür; 1. dönem genel başarısı değerlendirilir.',
            'process': ['a) Çok aşamalı LGS deneme sınavı uygular.', 'b) Dönemlik portfolyo oluşturur.'],
            'concepts': ['Basınç Sentezi', 'LGS Denemesi', 'Dönem Sonu Karnesi'],
            'skills': ['Hızlı ve Doğru Karar Verme', 'Analitik Sentez'], 'pedagogical': '1. dönem fen deneme karnesi çıkarılır.',
            'context': '1. Dönem LGS Zirvesi', 'question': 'Uçan balon gökyüzüne doğru yükseldikçe balonun hacmi nasıl değişir ve neden?',
            'solution': 'Yukarı çıkıldıkça açık hava basıncı azaldığı için balonun içindeki gaz dış basıncı dengelemek adına genleşir ve balonun hacmi büyür (patlayabilir).', 'weeklyGoal': '1. dönem LGS fen ünitelerini eksiksiz tamamlama.',
            'evaluation': '1. Dönem Sonu Kapsamlı LGS Deneme Sınavı'
        },

        # 18-25: Madde ve Endüstri
        {
            'theme': 'Madde ve Endüstri', 'subTheme': 'Periyodik Sistem ve Tarihçesi',
            'code': 'FEN.8.4.1', 'title': 'Periyodik Tablonun Gelişimi, Grup ve Periyot Kavramı',
            'description': 'Moseley\'in elementleri artan atom numaralarına (proton sayısı) göre dizdiğini; yatay sıralara periyot (7 periyot), düşey sütunlara grup (18 grup: 8 tane A, 10 tane B grubu) dendiğini açıklar.',
            'process': ['a) Aynı gruptaki elementlerin benzer kimyasal özellik gösterdiğini (son katmandaki değerlik elektron sayısı) kavrar.', 'b) Katman sayısının periyot numarasını verdiğini hesaplar.'],
            'concepts': ['Periyodik Tablo', 'Periyot', 'Grup', 'Atom Numarası (Proton Sayısı)', 'Değerlik Elektronu'],
            'skills': ['Tablo Koordinat Okuma', 'Elektron Dizilimi Yapma'], 'pedagogical': 'İlk 18 elementin elektron katman dağılımı yapılarak grup ve periyodu bulma pratiği yapılır.',
            'context': 'LGS Periyodik Tablo Soruları', 'question': 'Elektron dizilimi 2 - 8 - 3 şeklinde olan nötr bir X elementi periyodik sistemin kaçıncı periyot ve kaçıncı grubunda yer alır?',
            'solution': '3 katmanı olduğu için 3. periyot; son katmanında 3 elektron olduğu için 3A grubunda yer alır.', 'weeklyGoal': 'Elementlerin periyodik sistemdeki yerini elektron dizilimiyle bulma.',
            'evaluation': 'Periyodik tablo koordinat bulma föyü'
        },
        {
            'theme': 'Madde ve Endüstri', 'subTheme': 'Elementlerin Sınıflandırılması',
            'code': 'FEN.8.4.1', 'title': 'Metaller, Ametaller, Yarı Metaller ve Soygazların Özellikleri',
            'description': 'Metallerin parlak, tel-levha haline gelebilen, elektrik-ısıyı iyi ileten olduğunu; ametallerin mat ve kırılgan olduğunu; soygazların (8A) kararlı olup bağ yapmadığını; hidrojenin 1A\'daki ametal istisnasını modeller.',
            'process': ['a) Yarı metallerin (Bor, Silisyum) fiziksel olarak metale, kimyasal olarak ametale benzediğini kavrar.', 'b) Helyumun son katmanında 2 elektron olmasına rağmen kararlı yapısıyla 8A\'da yer aldığını unutmaz.'],
            'concepts': ['Metaller', 'Ametaller', 'Soygazlar (Asal Gazlar)', 'Yarı Metaller', 'Hidrojen İstisnası', 'Helyum İstisnası'],
            'skills': ['Karakteristik Ayrıştırma', 'İstisnai Bilgileri Yönetme'], 'pedagogical': 'Periyodik tablo boyanarak metaller mavi, ametaller sarı, soygazlar kırmızı renkle kodlanır.',
            'context': 'LGS Çeldirici Soru Tuzakları', 'question': '1A grubunda en üstte yer alan 1 numaralı element metal midir? 8A grubundaki Helyumun son katmanında kaç elektron vardır?',
            'solution': '1A grubunun ilk elementi Hidrojen bir ametaldir. Helyumun ise son katmanında 2 elektron vardır (dublet kuralı).', 'weeklyGoal': 'Element sınıflarını ve kritik istisnalarını eksiksiz öğrenme.',
            'evaluation': 'Element sınıfları karşılaştırma tablosu'
        },
        {
            'theme': 'Madde ve Endüstri', 'subTheme': 'Fiziksel ve Kimyasal Değişimler',
            'code': 'FEN.8.4.2', 'title': 'Maddenin Dış Görünüşü ile İç Yapısındaki Değişimlerin Ayırt Edilmesi',
            'description': 'Maddenin kimliğinin değişmediği durumları fiziksel değişim (kesme, kırılma, yırtılma, erime, buharlaşma, çözünme); yeni madde oluştuğu durumları kimyasal değişim (yanma, paslanma, mayalanma, küflenme, fotosentez) olarak ayırt eder.',
            'process': ['a) Kimyasal değişimlerde renk değişimi, gaz çıkışı, çökelti ve ısı-ışık yayılması gibi ipuçlarını analiz eder.', 'b) Suyun donmasının fiziksel, elektrolizinin kimyasal olduğunu kavrar.'],
            'concepts': ['Fiziksel Değişim', 'Kimyasal Değişim', 'Maddenin Kimliği', 'Yanma', 'Paslanma', 'Mayalanma'],
            'skills': ['Fenomen Analizi', 'Sınıflandırma'], 'pedagogical': 'Kağıdın yırtılması (fiziksel) ile kağıdın yakılması (kimyasal) sınıfta uygulanarak kül incelenir.',
            'context': 'Mutfak ve Sanayi Kimyası', 'question': 'Demirin paslanması ve şekerin suda çözünmesi olayları sırasıyla hangi değişim türlerine örnektir?',
            'solution': 'Demirin paslanması yeni bir bileşik oluştuğu için kimyasal değişim; şekerin çözünmesi molekül yapısı değişmediği için fiziksel değişimdir.', 'weeklyGoal': 'Fiziksel ve kimyasal değişim örneklerini hatasız sınıflandırma.',
            'evaluation': 'Fiziksel-Kimyasal değişim sınıflandırma föyü'
        },
        {
            'theme': 'Madde ve Endüstri', 'subTheme': 'Kimyasal Tepkimeler ve Kütlenin Korunumu',
            'code': 'FEN.8.4.3', 'title': 'Kimyasal Tepkime Denklemleri ve Kütlenin Korunumu Kanunu',
            'description': 'Giren maddelerin bağlarının kopup yeni bağlar oluşarak ürünleri meydana getirdiğini (Kimyasal Tepkime); kapalı kapta girenlerin toplam kütlesinin ürünlerin kütlesine daima eşit olduğunu (Kütlenin Korunumu) hesaplar.',
            'process': ['a) Atom sayısının, atom cinsinin ve toplam kütlenin korunduğunu kanıtlar.', 'b) Molekül sayısının korunmayabileceğini grafikler üzerinden çözümler.'],
            'concepts': ['Kimyasal Tepkime', 'Girenler (Reaktifler)', 'Ürünler', 'Kütlenin Korunumu', 'Bağ Kırılımı ve Oluşumu'],
            'skills': ['Grafik Çözümleme', 'Kütle Korunumu Hesabı'], 'pedagogical': 'Lavoisier\'in kapalı cam fanus deneyi ve terazi dengesi anlatılır.',
            'context': 'LGS Grafik Soruları', 'question': 'Kapalı bir kapta 32 gram metan gazı ile bir miktar oksijen gazı tepkimeye girerek 44 gram karbondioksit ve 36 gram su oluşturmuştur. Tepkimeye giren oksijen gazı kaç gramdır?',
            'solution': 'Toplam Ürünler = 44 + 36 = 80 g. Kütle korunduğundan Girenler = 80 g olmalıdır. Oksijen = 80 - 32 = 48 gramdır.', 'weeklyGoal': 'Kimyasal tepkime grafiklerini ve kütle korunumunu doğru çözme.',
            'evaluation': 'Kimyasal tepkime kütle hesabı föyü'
        },
        {
            'theme': 'Madde ve Endüstri', 'subTheme': 'Asitler ve Bazlar',
            'code': 'FEN.8.4.4', 'title': 'Asit ve Bazların Özellikleri, pH Ölçeği ve Belirteçler (İndikatörler)',
            'description': 'Suda H+ iyonu verenlerin asit (pH < 7, tatları ekşi, turnusolu kırmızıya çevirir), OH- iyonu verenlerin baz (pH > 7, tatları acı, ele kayganlık verir, turnusolu maviye çevirir); fenolftalein, metil oranj ve kırmızı lahana suyu indikatörlerini modeller.',
            'process': ['a) pH 7\'nin nötr (saf su, tuz) olduğunu açıklar.', 'b) Asitlerin metallerle tepkimeye girip H2 gazı çıkardığını ve mermeri aşındırdığını kavrar.'],
            'concepts': ['Asit (pH 0-7)', 'Baz (pH 7-14)', 'Nötr (pH 7)', 'Turnusol Kağıdı', 'Belirteç (İndikatör)', 'H+ ve OH- İyonları'],
            'skills': ['İndikatör Renk Analizi', 'pH Cetveli Kullanma'], 'pedagogical': 'Kırmızı lahana suyu çıkarılıp limon suyunda pembe-kırmızı, deterjanda yeşil-mavi renk değişimi gözlenir.',
            'context': 'Kimya Laboratuvarı', 'question': 'pH değeri 3 olan bir çözeltiye mavi turnusol kâğıdı batırıldığında turnusolün rengi neye döner ve çözelti asidik midir bazik midir?',
            'solution': 'pH < 7 olduğu için asidiktir ve mavi turnusol kâğıdını kırmızıya çevirir.', 'weeklyGoal': 'Asit ve bazların özelliklerini ve indikatör renklerini belirleme.',
            'evaluation': 'Kırmızı lahana suyu indikatör deneyi'
        },
        {
            'theme': 'Madde ve Endüstri', 'subTheme': 'Asit Yağmurları ve Güvenlik Tedbirleri',
            'code': 'FEN.8.4.4', 'title': 'Asit Yağmurlarının Oluşumu, Çevreye Zararları ve Kimyasal Güvenlik',
            'description': 'Fabrika ve araçlardan çıkan SO2, NO2 ve CO2 gazlarının su buharıyla birleşip sülfürik ve nitrik aside dönüşerek tarihi eserleri, ormanları ve suları tahrip etmesini; çamaşır suyu ile tuz ruhunun karıştırılmaması gereğini analiz eder.',
            'process': ['a) Temizlik maddelerinin ambalajlarındaki tehlike piktogramlarını tanır.', 'b) Mermer tezgaha limon konulduğunda leke kalmasını asidin aşındırıcı etkisiyle açıklar.'],
            'concepts': ['Asit Yağmurları', 'SO2, NO2, CO2 Gazları', 'Tarihi Eser Aşınması', 'Tuz Ruhu ve Çamaşır Suyu Tehlikesi (Klor Gazı)'],
            'skills': ['Güvenlik ve Çevre Bilinci', 'Risk Değerlendirme'], 'pedagogical': 'Mermer parçası üzerine damlatılan limon suyu ve tuz ruhunun köpürmesi izletilir.',
            'context': 'Ev İçi Kimyasal Zehirlenmeler', 'question': 'Ev temizliğinde çamaşır suyu (bazik) ile tuz ruhunun (asit) kesinlikle birbiriyle karıştırılmamasının hayati nedeni nedir?',
            'solution': 'Kimyasal tepkimeye girerek ölümcül zehirlenmelere ve akciğer hasarına yol açan klor gazı (Cl2) açığa çıkarmasıdır.', 'weeklyGoal': 'Asit ve bazlarla çalışırken güvenlik kurallarını ve asit yağmuru önlemlerini savunma.',
            'evaluation': 'Kimyasal güvenlik kuralları araştırma raporu'
        },
        {
            'theme': 'Madde ve Endüstri', 'subTheme': 'Maddenin Isı ile Etkileşimi (Öz Isı)',
            'code': 'FEN.8.4.5', 'title': 'Öz Isı Kavramı ve Sıcaklık Değişimi İlişkisi (Q = m x c x Δt)',
            'description': '1 gram saf maddenin sıcaklığını 1 °C artırmak için gereken ısıya öz ısı (c) dendiğini; öz ısısı küçük olan maddelerin çabuk ısınıp çabuk soğuduğunu (metaller), öz ısısı büyük olanların (su) geç ısınıp geç soğuduğunu açıklar.',
            'process': ['a) Denizlerin karalara göre geç ısınıp geç soğumasını suyun yüksek öz ısısıyla açıklar.', 'b) Eşit ısı verilen eşit kütleli maddelerden öz ısısı küçük olanın sıcaklık artışının daha fazla olduğunu modeller.'],
            'concepts': ['Öz Isı (c)', 'Sıcaklık Artışı (Δt)', 'Isı Miktarı (Q)', 'Ayırt Edici Özellik', 'J/g°C'],
            'skills': ['Isı-Sıcaklık Grafiği Çözümleme', 'Değişken Karşılaştırma'], 'pedagogical': 'Eşit kütleli su ve zeytinyağı özdeş ısıtıcılarla ısıtılarak sıcaklık artışları termometreyle kaydedilir.',
            'context': 'Karasal İklim ve Deniz Esintileri', 'question': 'Yazın gündüz vakti kumsalda yürürken kumun ayağı yakacak kadar sıcak olmasına rağmen deniz suyunun serin olmasının sebebi nedir?',
            'solution': 'Suyun öz ısısı kumun öz ısısından çok daha büyüktür; bu yüzden kum hızla ısınırken deniz suyu çok daha yavaş ısınır.', 'weeklyGoal': 'Öz ısı kavramını ve sıcaklık değişimiyle ters ilişkisini kavrama.',
            'evaluation': 'Öz ısı ve sıcaklık artışı problem föyü'
        },
        {
            'theme': 'Madde ve Endüstri', 'subTheme': 'Hâl Değişim Grafikleri ve Isı Hesapları',
            'code': 'FEN.8.4.5', 'title': 'Erime Isısı, Buharlaşma Isısı ve Isınma-Soğuma Grafikleri',
            'description': 'Saf maddelerin hâl değiştirirken sıcaklıklarının sabit kaldığını; saf bir katının ısınma grafiğindeki yatay basamakların erime ve kaynama anlarını temsil ettiğini açıklar.',
            'process': ['a) Kar yağarken havanın ısınmasını, buz erirken çevreden ısı almasını analiz eder.', 'b) Türkiye kimya endüstrisinin ithalat-ihracat ve meslek dallarını değerlendirir.'],
            'concepts': ['Hâl Değişim Sıcaklığı', 'Erime Isısı (Le)', 'Buharlaşma Isısı (Lb)', 'Isınma Eğrisi', 'Kimya Endüstrisi'],
            'skills': ['Eğri Grafiği Analizi', 'Sektörel Farkındalık'], 'pedagogical': 'Kareli kağıda suyun -20 °C\'den 120 °C\'ye ısınma grafiği çizdirilir.',
            'context': 'LGS Grafik Banko Soru', 'question': 'Saf bir sıvının kaynama süresince sıcaklığının hiç artmayıp sabit kalmasının bilimsel açıklaması nedir?',
            'solution': 'Verilen ısı enerjisinin sıcaklığı artırmak için değil, tanecikler arasındaki bağları koparıp gaz hâle geçmek (hâl değişimi) için harcanmasıdır.', 'weeklyGoal': 'Hâl değişim grafiklerini hatasız okuma ve yorumlama.',
            'evaluation': 'Hâl değişim grafiği analizi föyü'
        },

        # 26-29: Basit Makineler
        {
            'theme': 'Basit Makineler', 'subTheme': 'Basit Makinelerin Genel İlkeleri ve Makaralar',
            'code': 'FEN.8.5.1', 'title': 'İş ve Enerjiden Kazanç Olmaz Kuralı, Sabit ve Hareketli Makaralar',
            'description': 'Basit makinelerin iş kolaylığı sağladığını ama İŞ VE ENERJİDEN KAZANÇ SAĞLANAMAYACAĞINI; sabit makaranın sadece kuvvetin yönünü değiştirdiğini, hareketli makaranın ise 2 kat kuvvet kazancı sağlarken yoldan 2 kat kaybettirdiğini modeller.',
            'process': ['a) Kuvvetten kazanç varsa aynı oranda yoldan kayıp olduğunu kavrar.', 'b) Palangaları (hareketli ve sabit makara kombinasyonu) çözümler.'],
            'concepts': ['Basit Makine', 'Kuvvet Kazancı', 'Yoldan Kayıp', 'Sabit Makara', 'Hareketli Makara', 'Palanga', 'İşten Kazanç Yoktur'],
            'skills': ['Mekanik Avantaj Hesabı', 'Kuvvet-Yol Dengesi'], 'pedagogical': 'Dinamometre ve makara düzeneğiyle 20 N\'luk yükün hareketli makarada 10 N ile çekilmesi gösterilir.',
            'context': 'İnşaat Vinçleri', 'question': 'Bir hareketli makara ile 60 N ağırlığındaki bir yükü yerden 4 metre yukarı çıkarmak için uygulanacak kuvvet ve çekilmesi gereken ip uzunluğu nedir?',
            'solution': 'Kuvvetten 2 kat kazanç vardır: F = 60 / 2 = 30 N. Yoldan 2 kat kayıp vardır: İp = 4 x 2 = 8 metre çekilmelidir.', 'weeklyGoal': 'Makaralarda kuvvet ve yol hesaplamalarını doğru yapma.',
            'evaluation': 'Makaralar kuvvet-yol hesap föyü'
        },
        {
            'theme': 'Basit Makineler', 'subTheme': 'Kaldıraçlar (3 Türü)',
            'code': 'FEN.8.5.1', 'title': 'Desteğin, Yükün ve Kuvvetin Ortada Olduğu Kaldıraç Çeşitleri',
            'description': 'Desteğin ortada olduğu (tahterevalli, makas, pense); yükün ortada olduğu daima kuvvet kazancı sağlayan (el arabası, ceviz kıracağı, kapı); kuvvetin ortada olduğu yoldan kazanç sağlayan (cımbız, maşa, tenis raketi, olta) kaldıraçları formülüyle (Kuvvet x Kuvvet Kolu = Yük x Yük Kolu) hesaplar.',
            'process': ['a) Kuvvet kolu yük kolundan uzunsa kuvvetten kazanç olduğunu açıklar.', 'b) Kürek ve beyzbol sopasını kuvvetin ortada olduğu tipe örnekler.'],
            'concepts': ['Kaldıraç', 'Kuvvet Kolu', 'Yük Kolu', 'Destek Noktası', 'Moment Dengesi'],
            'skills': ['Kaldıraç Çeşitlerini Eşleştirme', 'Formül Çözümleme'], 'pedagogical': 'Cetvel ve silgiyle mini tahterevalli kurularak yük kolları dengelenir.',
            'context': 'LGS Kaldıraç Soruları', 'question': 'Ceviz kıracağı ve cımbız hangi kaldıraç türlerine örnektir ve hangisinde kuvvetten kazanç vardır?',
            'solution': 'Ceviz kıracağında yük ortadadır ve kuvvetten kazanç vardır. Cımbızda ise kuvvet ortadadır, kuvvetten kayıp (yoldan kazanç) vardır.', 'weeklyGoal': 'Kaldıraç türlerini belirleme ve kuvvet kolu dengesini çözme.',
            'evaluation': 'Kaldıraç türleri sınıflandırma testi'
        },
        {
            'theme': 'Basit Makineler', 'subTheme': 'Eğik Düzlem',
            'code': 'FEN.8.5.1', 'title': 'Eğik Düzlemde Kuvvet Kazancı ve Yükseklik İlişkisi (Kuvvet x Boy = Yük x Yükseklik)',
            'description': 'Ağır cisimleri yükseğe çıkarmak için kullanılan eğik düzlemde boyun (L) daima yükseklikten (h) büyük olması sebebiyle DAİMA KUVVET KAZANCI olduğunu; eğim azaldıkça (boy uzadıkça) kuvvet kazancının arttığını modeller.',
            'process': ['a) Vida ve rampaların birer eğik düzlem uygulaması olduğunu kavrar.', 'b) Dağ virajlarının eğik düzlem mantığıyla yolu uzatarak tırmanışı kolaylaştırdığını açıklar.'],
            'concepts': ['Eğik Düzlem', 'Rampa Boyu (L)', 'Yükseklik (h)', 'Eğim', 'Daima Kuvvet Kazancı'],
            'skills': ['Eğim-Kuvvet Bağıntısı', 'Uygulamalı Fizik'], 'pedagogical': 'Tahta rampa üzerinde dinamometreyle çekilen takozun kuvveti farklı eğimlerde ölçülür.',
            'context': 'Engelli Rampaları ve Yükleme Platformları', 'question': 'Bir kamyona koli yüklerken kullanılan rampanın boyu uzatılırsa koliyi yukarı çıkarmak için gereken kuvvet ve yapılan iş nasıl değişir?',
            'solution': 'Eğim azaldığı için uygulanması gereken kuvvet küçülür (kuvvet kazancı artar); ancak yapılan fiziksel iş kesinlikle değişmez.', 'weeklyGoal': 'Eğik düzlemde kuvvet kazancı bağıntılarını çözebilme.',
            'evaluation': 'Eğik düzlem laboratuvar föyü'
        },
        {
            'theme': 'Basit Makineler', 'subTheme': 'Çıkrık, Dişli Çarklar, Kasnaklar ve Vida',
            'code': 'FEN.8.5.1', 'title': 'Dönme Hareketi İleten Basit Makineler ve Bileşik Makineler',
            'description': 'Eksenleri çakışık silindirlerden oluşan çıkrıkta (kuyu çıkrığı, direksiyon, tornavida, kapı anahtarı) kol uzunluğu silindir yarıçapından büyük olduğu için kuvvet kazancı olduğunu; dişli ve kasnaklarda tur sayısı ve dönme yönü ilişkilerini çözer.',
            'process': ['a) Düz ve çapraz bağlı kasnaklarda dönme yönlerini takip eder.', 'b) Bisikletin makara, kaldıraç, dişli ve tekerlekten oluşan bir bileşik makine olduğunu analiz eder.'],
            'concepts': ['Çıkrık', 'Büyük Yarıçap (R)', 'Küçük Yarıçap (r)', 'Dişli Çark', 'Kasnak', 'Vida', 'Bileşik Makine'],
            'skills': ['Dönme Yönü Takibi', 'Bileşik Sistem Analizi'], 'pedagogical': 'Lego dişlilerle saat ve bisiklet vites mekanizması kurulur.',
            'context': 'Otomobil Şanzımanı ve Bisiklet', 'question': 'Yarıçapı 3r olan bir K dişlisi 2 tur döndürüldüğünde ona bağlı yarıçapı r olan L dişlisi hangi yönde ve kaç tur döner?',
            'solution': 'Birbirine temas eden dişliler zıt yönde döner. Tur sayısı yarıçapla ters orantılı olduğundan L dişlisi 2 x (3r / r) = 6 tur döner.', 'weeklyGoal': 'Çıkrık ve dişli sistemlerinin çalışma mantığını şematize etme.',
            'evaluation': 'Basit makineler bileşik sistem projesi'
        },

        # 30-33: Enerji Dönüşümleri ve Çevre Bilimi
        {
            'theme': 'Enerji Dönüşümleri ve Çevre Bilimi', 'subTheme': 'Besin Zinciri ve Enerji Piramidi',
            'code': 'FEN.8.6.1', 'title': 'Üreticiler, Tüketiciler, Ayrıştırıcılar ve Ekolojik Piramit',
            'description': 'Güneş enerjisini fotosentezle kimyasal bağ enerjisine çeviren üreticiler (bitkiler, siyanobakteriler), tüketiciler (otçul, etçil, hepcil) ve her basamakta yer alan ayrıştırıcıların (mantar, bakteri) besin zincirini oluşturduğunu; piramitte yukarı çıkıldıkça aktarılan enerjinin azaldığını (%10 kuralı), biyokütlenin azaldığını, zehirli madde birikiminin (biyolojik birikim) arttığını modeller.',
            'process': ['a) Üreticiden son tüketiciye doğru zehir miktarının en çok arttığını kavrar.', 'b) Zincirdeki bir canlının sayısının azalmasının diğer canlılara zincirleme etkisini analiz eder.'],
            'concepts': ['Üretici', 'Tüketici (Otçul/Etçil/Hepcil)', 'Ayrıştırıcı', 'Besin Zinciri', 'Enerji Piramidi (%10 Kuralı)', 'Biyolojik Birikim'],
            'skills': ['Ekolojik Denge Analizi', 'Piramit Okuma'], 'pedagogical': 'İplerle sınıf çapında besin ağı örülüp bir canlı çıkarıldığında ağın nasıl çöktüğü gösterilir.',
            'context': 'LGS Ekoloji Soruları', 'question': 'Bir enerji piramidinde üreticiden son tüketiciye (kartal veya aslan) doğru çıkıldıkça aktarılan enerji ve biyolojik zehir birikimi nasıl değişir?',
            'solution': 'Aktarılan enerji her basamakta %90 kayıpla azalarak sadece %10\'u geçer; dokularda biriken zehirli madde miktarı ise artar.', 'weeklyGoal': 'Besin zinciri ve enerji piramidi kurallarını hatasız yorumlama.',
            'evaluation': 'Besin zinciri ve enerji piramidi föyü'
        },
        {
            'theme': 'Enerji Dönüşümleri ve Çevre Bilimi', 'subTheme': 'Fotosentez ve Hızını Etkileyen Faktörler',
            'code': 'FEN.8.6.2', 'title': 'Fotosentez Denklemi (CO2 + H2O + Işık -> Glikoz + O2) ve Değişkenleri',
            'description': 'Kloroplast taşıyan hücrelerin ışık enerjisiyle karbondioksit ve suyu glikoza ve oksijene dönüştürmesini; fotosentez hızının ışık şiddeti, karbondioksit miktarı, sıcaklık (en iyi 25-35 °C) ve ışığın rengine (mor ve kırmızıda en hızlı, yeşilde en yavaş) bağlılığını deneylerle kanıtlar.',
            'process': ['a) İyot çözeltisinin nişasta (glikoz) varlığında mavi-mor renk aldığını dener.', 'b) Elodea su bitkisinin ışık altında oksijen kabarcığı çıkarmasını gözlemler.'],
            'concepts': ['Fotosentez', 'Klorofil', 'Glikoz (Besin)', 'Oksijen', 'Işığın Rengi (Mor > Yeşil)', 'Işık Şiddeti'],
            'skills': ['Deney Düzeneği Kurma', 'Grafik Analizi'], 'pedagogical': 'Yeşil ışıkta bitkinin yeşili yansıttığı için en az fotosentez yaptığı vurgulanır.',
            'context': 'Sera Tarımı ve Yapay Işıklandırma', 'question': 'Özdeş iki saksı bitkisinden biri mor ışık, diğeri yeşil ışık altına konulduğunda hangisinde fotosentez hızı ve oksijen üretimi daha yüksek olur?',
            'solution': 'Mor ışık altındaki bitkide çok daha yüksek olur; çünkü klorofil mor ışığı yüksek oranda soğurur, yeşil ışığın çoğunu ise yansıtır.', 'weeklyGoal': 'Fotosentez hızını etkileyen faktörleri kontrollü deneyle analiz etme.',
            'evaluation': 'Fotosentez deney düzenekleri föyü'
        },
        {
            'theme': 'Enerji Dönüşümleri ve Çevre Bilimi', 'subTheme': 'Hücresel Solunum (Oksijenli ve Oksijensiz)',
            'code': 'FEN.8.6.2', 'title': 'Oksijenli Solunum, Oksijensiz Solunum ve Fermantasyon (Mayalanma)',
            'description': 'Besinlerin parçalanarak ATP enerjisi üretilmesini; mitokondride gerçekleşen bol enerji veren oksijenli solunum (Besin + O2 -> CO2 + H2O + 32 ATP) ile sitoplazmada gerçekleşen fermantasyonu (etil alkol fermantasyonu: maya mantarları, laktik asit fermantasyonu: yoğurt bakterileri ve yorulan çizgili kaslar) karşılaştırır.',
            'process': ['a) Kireç suyunun karbondioksit gazıyla bulanmasını solunum kanıtı olarak kullanır.', 'b) Fotosentez ile oksijenli solunumun birbirinin tersi bir döngü olduğunu açıklar.'],
            'concepts': ['Hücresel Solunum', 'Oksijenli Solunum (Mitokondri)', 'Fermantasyon', 'Etil Alkol / Laktik Asit', 'ATP Enerjisi', 'Kireç Suyu'],
            'skills': ['Biyokimyasal Denklem Çözümleme', 'Karşılaştırmalı Tablo'], 'pedagogical': 'Şekerli ılık suya kuru maya konulup balona takılarak gaz çıkışıyla balonun şişmesi izlenir.',
            'context': 'Ekmek ve Yoğurt Üretimi', 'question': 'Ağır spor ve koşu yapan bir sporcunun kaslarında oksijen yetersizliğinde gerçekleşen ve yorgunluk hissi veren fermantasyon türü hangisidir?',
            'solution': 'Laktik asit fermantasyonudur (süt asidi); kaslarda birikerek yorgunluk ve kramp hissi oluşturur.', 'weeklyGoal': 'Oksijenli ve oksijensiz solunum arasındaki farkları açıklama.',
            'evaluation': 'Fermantasyon ve solunum karşılaştırma föyü'
        },
        {
            'theme': 'Enerji Dönüşümleri ve Çevre Bilimi', 'subTheme': 'Madde Döngüleri ve Sürdürülebilir Kalkınma',
            'code': 'FEN.8.6.3', 'title': 'Su, Karbon, Azot Döngüleri ve Ekolojik Ayak İzi',
            'description': 'Doğadaki su, karbon ve azot döngülerinin dengesini; fosil yakıtların karbon döngüsünü bozarak küresel ısınmaya yol açmasını; kaynakların gelecek nesillere aktarılmasını ifade eden sürdürülebilir kalkınma bilincini inceler.',
            'process': ['a) Baklagil köklerindeki azot bağlayıcı bakterilerin önemini kavrar.', 'b) Bireysel ekolojik ayak izini hesaplayarak tasarruf planı yapar.'],
            'concepts': ['Madde Döngüsü', 'Su Döngüsü', 'Karbon Döngüsü', 'Azot Döngüsü', 'Sürdürülebilir Kalkınma', 'Ekolojik Ayak İzi'],
            'skills': ['Gezegen Okuryazarlığı', 'Döngüsel Sistem Tasarımı'], 'pedagogical': 'Kapalı teraryum yapılarak su ve karbon döngüsünün kendi kendine yetmesi gösterilir.',
            'context': 'Geleceğin Dünyası ve Sıfır Atık', 'question': 'Havadaki serbest azot gazının bitkiler tarafından doğrudan kullanılamayıp toprağa bağlanmasında hangi canlılar hayati rol oynar?',
            'solution': 'Baklagil köklerinde yaşayan azot bağlayıcı bakteriler ile yıldırım ve şimşek hava olayları hayati rol oynar.', 'weeklyGoal': 'Madde döngülerini ve sürdürülebilir yaşam ilkelerini savunma.',
            'evaluation': 'Ekolojik ayak izi hesaplama formu'
        },

        # 34-36: Elektrik Yükleri ve Elektrik Enerjisi
        {
            'theme': 'Elektrik Yükleri ve Elektrik Enerjisi', 'subTheme': 'Elektriklenme Çeşitleri ve Elektroskop',
            'code': 'FEN.8.7.1', 'title': 'Sürtünme, Dokunma ve Etkiyle Elektriklenme ve Elektroskop Yapısı',
            'description': 'Pozitif (+) ve negatif (-) elektrik yüklerini; sürtünmeyle (ebonit çubuk yün kumaşa sürülünce -, cam çubuk ipek kumaşa sürülünce +); dokunmayla yük paylaşımını; etkiyle kutuplanmayı ve bir cismin yüklü olup olmadığını anlamaya yarayan elektroskobun yaprak hareketlerini modeller.',
            'process': ['a) Aynı yüklerin birbirini ittiğini, zıt yüklerin çektiğini ve nötr cisimlerin yüklü cisimler tarafından çekildiğini doğrular.', 'b) Nötr elektroskoba yüklü cisim yaklaştırıldığında yaprakların açıldığını kavrar.'],
            'concepts': ['Pozitif Yük', 'Negatif Yük', 'Nötr Cisim', 'Elektroskop', 'Sürtünme / Dokunma / Etkiyle Elektriklenme'],
            'skills': ['Elektrostatik Deney', 'Yük Dağılım Şeması'], 'pedagogical': 'Plastik tarak saça sürtülüp küçük kâğıt parçalarının çekilmesi elektrostatik ile gösterilir.',
            'context': 'LGS Elektrik Yük Soruları', 'question': 'Yün kumaşa sürtülen ebonit (plastik) çubuk ile ipek kumaşa sürtülen cam çubuğun kazandığı elektrik yüklerinin işaretleri sırasıyla nedir?',
            'solution': 'Ebonit çubuk negatif (-), cam çubuk ise pozitif (+) yükle yüklenir.', 'weeklyGoal': 'Elektriklenme türlerini ve elektroskop hareketlerini eksiksiz açıklama.',
            'evaluation': 'Elektriklenme türleri laboratuvar föyü'
        },
        {
            'theme': 'Elektrik Yükleri ve Elektrik Enerjisi', 'subTheme': 'Topraklama, Şimşek, Yıldırım ve Enerji Dönüşümü',
            'code': 'FEN.8.7.2', 'title': 'Topraklama Prensibi, Paratoner ve Elektrik Enerjisinin Isı/Işığa Dönüşümü',
            'description': 'Yüklü cisimlerin iletken telle toprağa bağlanarak nötr hale getirilmesine topraklama dendiğini; bulutlar arası yük boşalmasına şimşek, bulut ile yer arasına yıldırım dendiğini; binalardaki paratonerleri; elektrik enerjisinin ısı (tost makinesi, ütü) ve ışığa (ampul) dönüşümünü inceler.',
            'process': ['a) Tankerlerin arkasındaki zincirin kıvılcım çıkmasını önleyen topraklama olduğunu kavrar.', 'b) Elektrik sigortasının aşırı akımda devreyi keserek yangını önlediğini belirtir.'],
            'concepts': ['Topraklama', 'Şimşek', 'Yıldırım', 'Paratoner', 'Elektrik Sigortası', 'Elektrik Enerjisinin Isıya Dönüşümü'],
            'skills': ['Can ve Mal Güvenliği', 'Elektriksel Koruma'], 'pedagogical': 'Van de Graaff jeneratörü ile yapay kıvılcım ve saç dikelmesi gösterilir.',
            'context': 'Akaryakıt İstasyonları ve Binalar', 'question': 'Yüksek binaların tepesine takılan ve yıldırımın taşıdığı devasa elektrik yükünü zararsızca toprağa aktaran koruma sistemine ne ad verilir?',
            'solution': 'Paratoner (yıldırımsavar) adı verilir.', 'weeklyGoal': 'Topraklama ve elektriksel güvenlik tedbirlerini açıklama.',
            'evaluation': 'Topraklama ve paratoner şeması çizimi'
        },
        {
            'theme': 'Elektrik Yükleri ve Elektrik Enerjisi', 'subTheme': 'LGS Genel Fen Bilimleri Final Kampı',
            'code': 'FEN.8.7.3', 'title': 'LGS 20 Soruluk Tam Prova ve Sınav Başarı Stratejisi',
            'description': 'Mevsimler, DNA, Basınç, Madde-Endüstri, Basit Makineler, Canlılar-Enerji ve Elektrik ünitelerinden oluşan LGS formatında MEB standartlarında genel deneme sınavı ve analizi yapılır.',
            'process': ['a) Zaman yönetimi ve turlama taktiğini pekiştirir.', 'b) Son LGS taktiklerini gözden geçirir.'],
            'concepts': ['LGS Fen Tam Prova', 'Optik Kodlama', 'Sınav Başarısı'],
            'skills': ['Üst Düzey Sınav Performansı', 'Psikolojik Dayanıklılık'], 'pedagogical': 'Gerçek sınav saatinde (09.30) sessiz ortamda LGS prova denemesi uygulanır.',
            'context': 'LGS Büyük Finali', 'question': 'LGS Fen Bilimleri testinde soru köklerindeki "kesinlikle", "olabilir", "bağımsız değişken" ifadelerine nasıl yaklaşılmalıdır?',
            'solution': 'Tüm öncüller dikkatle okunmalı; sadece verilen deneydeki değiştirilen faktöre odaklanılmalı ve kişisel tahmin değil deney tablosundaki veriler esas alınmalıdır.', 'weeklyGoal': 'LGS Fen Bilimleri testinde 20/20 tam başarıya ulaşma.',
            'evaluation': 'LGS Fen Bilimleri Genel Başarı Sertifikası'
        }
    ]
    return {
        'title': '8. Sınıf',
        'subtitle': 'LGS Fen Bilimleri Programı (Sınav Odaklı)',
        'badge': 'LGS Fen Bilimleri',
        'weeks': weeks
    }

print("Fen 7 & 8 builders compiled.")
