# -*- coding: utf-8 -*-
"""
Generates 36 weeks for Grade 7 Türkçe.
"""

def build_turkce_7():
    weeks = [
        {
            'theme': 'Duygular ve Değerler', 'subTheme': 'Sözcükte Anlam', 'code': 'TÜR.7.1.1',
            'title': 'Gerçek, Mecaz ve Terim Anlam',
            'description': 'Sözcüklerin cümledeki bağlamsal anlamlarını ve mecazlaşma yollarını çözümleme.',
            'process': ['a) Çok anlamlılığı fark eder.', 'b) Mecaz anlamlı sözcükleri tespit eder.'],
            'concepts': ['Gerçek Anlam', 'Mecaz Anlam', 'Bağlam'],
            'skills': ['Metin İçi Anlam Oluşturma', 'Söz Sanatı'],
            'pedagogical': 'Metin içi anlam oluşturma çalışmaları yapılır.',
            'context': 'Söz Sanatı', 'question': '"Gözleri sevinçten parlıyordu" cümlesinde altı çizili kelimenin anlamı nedir?',
            'solution': 'Mecaz anlamdır, mutluluğunu ve heyecanını yansıtmaktadır.',
            'weeklyGoal': 'Sözcüklerin bağlamsal anlamlarını çözme.', 'evaluation': 'Anlam kartları eşleştirme'
        },
        {
            'theme': 'Duygular ve Değerler', 'subTheme': 'Deyimler ve Atasözleri', 'code': 'TÜR.7.1.1',
            'title': 'Deyim ve Atasözlerinin Metne Katkısı',
            'description': 'Kültürel zenginlik olan deyim ve atasözlerini uygun bağlamda kullanma.',
            'process': ['a) Kalıplaşmış söz öbeklerini inceler.', 'b) Öğüt bildiren atasözlerini sınıflandırır.'],
            'concepts': ['Deyim', 'Atasözü', 'Kalıplaşma'],
            'skills': ['Kültürel Aktarım', 'Öğüt'], 'pedagogical': 'Atasözlerinin öğüt boyutları tartışılır.',
            'context': 'Öğüt', 'question': '"Damlaya damlaya göl olur" atasözünün mesajı nedir?',
            'solution': 'Tasarrufun ve küçük birikimlerin zamanla büyük değerlere dönüşeceğini vurgular.',
            'weeklyGoal': 'Deyim ve atasözlerini metinlerde belirleme.', 'evaluation': 'Deyim tamamlama bulmacası'
        },
        {
            'theme': 'Duygular ve Değerler', 'subTheme': 'Cümlede Anlam', 'code': 'TÜR.7.1.2',
            'title': 'Neden-Sonuç, Amaç-Sonuç, Koşul Cümleleri',
            'description': 'Cümleler arası mantıksal anlam ilişkilerini ayırt etme.',
            'process': ['a) "İçin", "diye", "amacıyla" edatlarının işlevini irdeler.'],
            'concepts': ['Neden-Sonuç', 'Amaç-Sonuç', 'Koşul-Sonuç'],
            'skills': ['Mantıksal Bağlaç Analizi', 'İlişki Tespiti'], 'pedagogical': 'Amacıyla ve gerekçesiyle testi uygulanır.',
            'context': 'İlişki Tespiti', 'question': '"Sınavı kazanmak için çok çalıştı" cümlesinin anlam ilişkisi nedir?',
            'solution': 'Amaç-sonuç ilişkisidir; çok çalışmanın hedefi sınavı kazanmaktır.',
            'weeklyGoal': 'Cümleler arası mantıksal ilişkileri tespit etme.', 'evaluation': 'Cümle ilişkilendirme tablosu'
        },
        {
            'theme': 'Duygular ve Değerler', 'subTheme': 'Örtülü Anlam', 'code': 'TÜR.7.1.2',
            'title': 'Örtülü Anlam ve Çıkarım Yapma',
            'description': 'Cümlede açıkça söylenmeyen ancak sezdirilen örtülü anlamları bulma.',
            'process': ['a) "De" bağlacı ve "artık" sözcüğünün kattığı anlamı çözümler.'],
            'concepts': ['Örtülü Anlam', 'Sezdirim', 'Çıkarım'],
            'skills': ['Eleştirel Okuma', 'Çıkarım'], 'pedagogical': 'Satır arası anlamlar keşfedilir.',
            'context': 'Çıkarım', 'question': '"Ahmet de geziye katıldı" cümlesindeki örtülü anlam nedir?',
            'solution': 'Ahmet dışında başkalarının da geziye katıldığı anlaşılır.',
            'weeklyGoal': 'Cümledeki örtülü anlamları saptama.', 'evaluation': 'Çıkarım formu'
        },
        {
            'theme': 'Millî Kültürümüz', 'subTheme': 'Fiiller (Eylemler)', 'code': 'TÜR.7.2.1',
            'title': 'İş, Oluş ve Durum Fiilleri',
            'description': 'Fiillerin anlam özelliklerini "onu" kelimesiyle nesne alabilirlik ve irade açısından test etme.',
            'process': ['a) İş (kılış) fiillerinin nesne aldığını kavrar.', 'b) Oluş fiillerinin irade dışı gerçekleştiğini fark eder.'],
            'concepts': ['İş Fiili', 'Oluş Fiili', 'Durum Fiili', 'Maddi Değişim'],
            'skills': ['Anlamsal Sınıflandırma', 'Fiil Türü'], 'pedagogical': "'Onu' testiyle iş, kendiliğinden zamanla oluşumla oluş fiili ayırt edilir.",
            'context': 'Fiil Türü', 'question': '"Sararmak, yazmak, uyumak" fiillerinin anlam özelliği sırasıyla nedir?',
            'solution': 'Sararmak (kendiliğinden zamanla: Oluş), Yazmak (onu yazmak: İş), Uyumak (öznenin durumu: Durum).',
            'weeklyGoal': 'Fiilleri iş, oluş ve durum özelliklerine göre sınıflandırma.', 'evaluation': 'Fiil sınıflandırma tablosu'
        },
        {
            'theme': 'Millî Kültürümüz', 'subTheme': 'Çekimli Fiiller', 'code': 'TÜR.7.2.1',
            'title': 'Fiillerde Kip ve Kişi Ekleri (Çekimli Fiil)',
            'description': 'Fiillerin haber (bildirme) ve dilek (tasarlama) kipleriyle çekimlenmesini çözümleme.',
            'process': ['a) Fiil kök veya gövdelerine gelen kip ve şahıs eklerini parçalarına ayırır.', 'b) Haber kiplerinin zaman anlamı taşıdığını (-di, -miş, -yor, -ecek, -r) kavrar.', 'c) Dilek kiplerinin zaman değil tasarı bildirdiğini (-meli, -se, -e, emir) modeller.'],
            'concepts': ['Çekimli Fiil', 'Haber Kipi', 'Dilek Kipi', 'Şahıs Eki', 'Zaman Kavramı'],
            'skills': ['Fiil Çekimi', 'Biçim Bilgisi'], 'pedagogical': 'Kök + Kip + Kişi formülü şematik olarak gösterilir.',
            'context': 'Fiil Çekimi', 'question': '"Okumalısınız" fiilinin kip ve kişisini bulunuz.',
            'solution': 'Gereklilik kipi (-malı/-meli) ve 2. çoğul şahıs (-sınız).',
            'weeklyGoal': 'Fiilleri haber ve dilek kipleriyle doğru çekimleme.', 'evaluation': 'Çekimli fiil analiz kartı'
        },
        {
            'theme': 'Millî Kültürümüz', 'subTheme': 'Fiillerde Anlam Kayması', 'code': 'TÜR.7.2.1',
            'title': 'Fiillerde Anlam (Zaman) Kayması',
            'description': 'Biçimce bir kipi gösteren fiilin anlamca başka bir kipi kastetmesini fark etme.',
            'process': ['a) Zaman zarfı ile kip eki arasındaki uyumsuzluğu analiz eder.', 'b) Bunun bir anlatım bozukluğu olmadığını kavrar.'],
            'concepts': ['Anlam Kayması', 'Zaman Kayması', 'Kip Uyuşumu'],
            'skills': ['Kural ile Kullanım Farkı', 'Anlam Kayması'], 'pedagogical': 'Günlük konuşmalardaki zaman kaymaları tespit edilir.',
            'context': 'Anlam Kayması', 'question': '"Yarın sinemaya gidiyorum" cümlesinde anlam kayması var mıdır?',
            'solution': 'Evet; şimdiki zaman kipi (-yor) kullanılmasına rağmen kastedilen gelecek zamandır (-ecek).',
            'weeklyGoal': 'Fiillerde anlam kaymasını saptama.', 'evaluation': 'Zaman kayması avı oyunu'
        },
        {
            'theme': 'Millî Kültürümüz', 'subTheme': 'Metin Türleri', 'code': 'TÜR.7.3.1',
            'title': 'Söyleşi (Sohbet) ve Makale',
            'description': 'Samimi bir dille yazılan söyleşi ile kanıta dayalı bilimsel makaleyi karşılaştırma.',
            'process': ['a) Söyleşide yazarın okuyucuyla konuşuyormuş gibi yazdığını keşfeder.', 'b) Makalede nesnellik ve kanıtlama arar.'],
            'concepts': ['Söyleşi (Sohbet)', 'Makale', 'Kanıtlama', 'Samimi Üslup'],
            'skills': ['Üslup ve Anlatım Özellikleri', 'Metin Karşılaştırma'], 'pedagogical': 'Şevket Rado\'nun Eşref Saati söyleşisi incelenir.',
            'context': 'Metin Karşılaştırma', 'question': 'Yazarın kişisel görüşlerini okuyucuyla sohbet ediyormuş gibi içtenlikle paylaştığı yazı türü nedir?',
            'solution': 'Söyleşi (sohbet) türüdür.',
            'weeklyGoal': 'Söyleşi ve makale türlerini karşılaştırma.', 'evaluation': 'Tür karşılaştırma tablosu'
        },
        {
            'theme': 'Bilim ve Teknoloji', 'subTheme': 'Ek Fiil (Ek Eylem)', 'code': 'TÜR.7.2.2',
            'title': 'Ek Fiilin İsimleri Yüklem Yapma Görevi (-idi, -imiş, -ise, -dir)',
            'description': 'Ek fiilin isim soylu sözcüklere gelerek onları yüklem yapmasını anlama.',
            'process': ['a) İsimlerin fiil gibi çekimlenmesini sağlayan ek fiili tespit eder.', 'b) Ek fiilin olumsuzunun "değil" ile yapıldığını kavrar.'],
            'concepts': ['Ek Fiil', 'İsim Cümlesi', 'Yüklem', '-idi / -imiş / -ise / -dir'],
            'skills': ['İsimlerin Yüklem Olma Gücü', 'Ek Fiil'], 'pedagogical': 'İsimlerin sonundaki gizli ek fiiller bulunur.',
            'context': 'Ek Fiil', 'question': '"Hava dün çok soğuktu" cümlesinde ek fiil var mıdır?',
            'solution': 'Evet, "soğuk-i-di" şeklinde ismi yüklem yapan ek fiil vardır.',
            'weeklyGoal': 'İsimleri yüklem yapan ek fiili doğru bulma.', 'evaluation': 'Ek fiil tamamlama testi'
        },
        {
            'theme': 'Ara Tatil', 'subTheme': '1. Dönem Ara Tatili', 'code': 'TÜR.7.GENEL.1',
            'title': 'Fiiller ve Metin Türleri Tekrar Kampı',
            'description': 'Fiil kipleri, ek fiil ve okuduğunu anlama becerilerinin eğlenceli fasikülle tekrarı.',
            'process': ['a) Paragraf ve dil bilgisi soruları çözer.'],
            'concepts': ['Genel Tekrar', 'Okuma Kültürü'],
            'skills': ['Öz Denetimli Okuma'], 'pedagogical': 'EBA tatil fasikülü uygulanır.',
            'context': 'Okuma', 'question': 'Bir metnin ana fikri nasıl bulunur?',
            'solution': 'Yazarın okuyucuya iletmek istediği asıl mesaj ve hayat dersi sorgulanır.',
            'weeklyGoal': 'İlk 9 haftanın kazanımlarını pekiştirme.', 'evaluation': 'Ara Tatil Değerlendirme Testi'
        },
        {
            'theme': 'Bilim ve Teknoloji', 'subTheme': 'Ek Fiil 2', 'code': 'TÜR.7.2.2',
            'title': 'Ek Fiilin Birleşik Zamanlı Fiil Yapma Görevi (Hikâye, Rivayet, Şart)',
            'description': 'Basit zamanlı fiillere gelerek onları birleşik zamanlı fiil (hikâye: -di, rivayet: -miş, şart: -se) yapmasını kavrama.',
            'process': ['a) İki kip ekinin üst üste geldiği birleşik çekimleri modeller.', 'b) \'Geliyordu\' (Şimdiki zamanın hikâyesi) çekimini çözümler.'],
            'concepts': ['Birleşik Zamanlı Fiil', 'Hikâye (-di)', 'Rivayet (-miş)', 'Şart (-se)'],
            'skills': ['Zaman Katmanları', 'Biçim Çözümleme'], 'pedagogical': 'İki katlı zaman piramidi çizilir.',
            'context': 'Birleşik Zaman', 'question': '"Gel-i-yor-du" fiilinin birleşik zaman türü nedir?',
            'solution': 'Şimdiki zamanın hikâyesidir.',
            'weeklyGoal': 'Birleşik zamanlı fiilleri adlandırma.', 'evaluation': 'Birleşik zaman çözümleme tablosu'
        },
        {
            'theme': 'Bilim ve Teknoloji', 'subTheme': 'Paragrafta Yapı', 'code': 'TÜR.7.1.3',
            'title': 'Giriş, Gelişme ve Sonuç Cümleleri ile Akışı Bozan Cümle',
            'description': 'Paragrafın akışını bozan cümleleri bulma ve ana düşünceyi saptama.',
            'process': ['a) Düşünceyi bağlayan geçiş ifadelerini tespit eder.', 'b) Giriş cümlesinin bağımsız olması gerektiğini açıklar.'],
            'concepts': ['Paragraf Yapısı', 'Akışı Bozan Cümle', 'Ana Fikir'],
            'skills': ['Düşünce Akışı Analizi', 'Paragraf'], 'pedagogical': 'Metin mimarisi incelenir.',
            'context': 'Paragraf', 'question': 'Bir paragraf "Bu yüzden" ifadesiyle başlayabilir mi?',
            'solution': 'Hayır, bağlayıcı bir sonuç ifadesi olduğu için giriş cümlesi olamaz.',
            'weeklyGoal': 'Paragraf yapısını ve düşünce akışını analiz etme.', 'evaluation': 'Paragraf tamamlama kartları'
        },
        {
            'theme': 'Birey ve Toplum', 'subTheme': 'Zarflar (Belirteçler)', 'code': 'TÜR.7.2.3',
            'title': 'Durum, Zaman ve Miktar Zarfları',
            'description': 'Fiilleri, fiilimsileri ve sıfatları anlamca tamamlayan zarfları ayırt etme.',
            'process': ['a) "Nasıl?", "Ne zaman?", "Ne kadar?" sorularını fiile sorar.', 'b) Sıfat ile zarf farkını isim-fiil niteleme üzerinden açıklar.'],
            'concepts': ['Zarf (Belirteç)', 'Durum Zarfı', 'Zaman Zarfı', 'Miktar Zarfı'],
            'skills': ['Fiili Niteleyen Sözcükler', 'Sözcük Türü Ayrımı'], 'pedagogical': "'Hızlı araba' (sıfat) ile 'Hızlı koştu' (zarf) karşılaştırılır.",
            'context': 'Zarf', 'question': '"Çocuk hızlıca koştu" cümlesindeki zarf ve türü nedir?',
            'solution': '"Hızlıca" sözcüğü fiile sorulan "Nasıl?" sorusunun cevabı olan durum zarfıdır.',
            'weeklyGoal': 'Zarfları cümlelerde doğru saptama.', 'evaluation': 'Zarf avı çalışma kâğıdı'
        },
        {
            'theme': 'Birey ve Toplum', 'subTheme': 'Zarflar 2', 'code': 'TÜR.7.2.3',
            'title': 'Yer-Yön ve Soru Zarfları',
            'description': 'İçeri, dışarı, ileri, geri sözcüklerinin ek aldığında isimleştiğini fark etme.',
            'process': ['a) "Aşağı indi" (zarf) ile "Aşağıya indi" (isim) farkını ayırt eder.', 'b) Soru zarflarını belirler.'],
            'concepts': ['Yer-Yön Zarfı', 'Ek Almama Kuralı', 'Soru Zarfı'],
            'skills': ['Hassas Dil Bilgisi Kuralı', 'Zarf / İsim'], 'pedagogical': 'Ek almayan yer-yön kelimeleri kodlanır.',
            'context': 'Zarf / İsim', 'question': '"Yukarı çıktı" cümlesindeki "yukarı" sözcüğünün türü nedir?',
            'solution': 'Yer-yön zarfıdır (hâl eki almamıştır).',
            'weeklyGoal': 'Yer-yön zarfını ismin hâl ekinden ayırt etme.', 'evaluation': 'Zarf eşleştirme oyunu'
        },
        {
            'theme': 'Birey ve Toplum', 'subTheme': 'Düşünceyi Geliştirme Yolları', 'code': 'TÜR.7.1.4',
            'title': 'Tanımlama, Örnekleme ve Karşılaştırma',
            'description': 'Yazarın düşüncelerini inandırıcı kılmak için başvurduğu teknikleri belirleme.',
            'process': ['a) "Bu nedir?" sorusunun cevabını tanımlama olarak saptar.'],
            'concepts': ['Tanımlama', 'Örnekleme', 'Karşılaştırma', 'Tanık Gösterme'],
            'skills': ['Metin Analiz Becerisi', 'Düşünceyi Geliştirme'], 'pedagogical': 'Tanımlama ve örnekleme metinleri incelenir.',
            'context': 'Düşünceyi Geliştirme', 'question': '"Eğitim, insanı hayata hazırlama sanatıdır" cümlesinde hangi teknik vardır?',
            'solution': 'Tanımlama yapılmıştır ("Eğitim nedir?" sorusunun cevabıdır).',
            'weeklyGoal': 'Düşünceyi geliştirme yollarını metinde belirleme.', 'evaluation': 'Metin inceleme rubriği'
        },
        {
            'theme': 'Sağlık ve Spor', 'subTheme': 'Yazım Kuralları', 'code': 'TÜR.7.4.1',
            'title': 'Büyük Harfler ve Birleşik Sözcüklerin Yazımı',
            'description': 'Kurum, unvan, tarih ve birleşik sözcüklerin yazım kurallarını uygulama.',
            'process': ['a) Ses düşmesi veya türemesi olan birleşik fiillerin bitişik yazıldığını açıklar.'],
            'concepts': ['Büyük Harf', 'Bitişik Yazım', 'Ayrı Yazım'],
            'skills': ['İmla Hassasiyeti', 'Yazım Kuralı'], 'pedagogical': 'Etmek, olmak yardımcı fiiliyle kurulan birleşikler incelenir.',
            'context': 'Yazım Kuralı', 'question': '"Terketmek" mi yoksa "terk etmek" mi doğrudur?',
            'solution': 'Ayrı yazılır: "Terk etmek" (ses olayı yoktur).',
            'weeklyGoal': 'Birleşik sözcüklerin yazımını doğru uygulama.', 'evaluation': 'Hata düzeltme metni'
        },
        {
            'theme': 'Sağlık ve Spor', 'subTheme': 'Noktalama İşaretleri', 'code': 'TÜR.7.4.2',
            'title': 'Noktalı Virgül ve İki Nokta',
            'description': 'Cümle içinde virgüllerle ayrılmış türleri ayırmada noktalı virgülün kullanımını kavrama.',
            'process': ['a) Noktalı virgülün virgülsüz cümlede bulunamayacağını modeller.'],
            'concepts': ['Noktalı Virgül (;)', 'İki Nokta (:)', 'Alıntı'],
            'skills': ['Noktalama Mantığı', 'Noktalama'], 'pedagogical': 'İki nokta ve noktalı virgül kuralları karşılaştırılır.',
            'context': 'Noktalama', 'question': 'Açıklama yapılacak cümlenin sonuna hangi işaret konur?',
            'solution': 'İki nokta (:) konur.',
            'weeklyGoal': 'Noktalı virgül ve iki noktayı hatasız kullanma.', 'evaluation': 'Noktalama tamamlama görevi'
        },
        {
            'theme': 'Sağlık ve Spor', 'subTheme': 'Metin Türleri 2', 'code': 'TÜR.7.3.2',
            'title': 'Biyografi ve Otobiyografi',
            'description': 'Yaşam öyküsü ve öz yaşam öyküsü arasındaki anlatıcı farkını çözümleme.',
            'process': ['a) 1. kişi ve 3. kişi anlatım farkını ayırt eder.'],
            'concepts': ['Biyografi', 'Otobiyografi', 'Anlatıcı Türü'],
            'skills': ['Biyografik Hafıza', 'Metin Türü'], 'pedagogical': 'Kişisel portre ve yazar yaşamı karşılaştırılır.',
            'context': 'Metin Türü', 'question': 'Kişinin kendi hayatını anlattığı eser türü nedir?',
            'solution': 'Otobiyografidir (öz yaşam öyküsü).',
            'weeklyGoal': 'Biyografi ve otobiyografi farkını saptama.', 'evaluation': 'Yazar portresi hazırlama'
        },
        {
            'theme': '1. Dönem Değerlendirme', 'subTheme': 'Dönem Sonu Sentezi', 'code': 'TÜR.7.GENEL.2',
            'title': '1. Dönem Türkçe Yetkinlik Değerlendirmesi',
            'description': 'Fiiller, ek fiil, zarflar ve metin anlama çıktılarının portfolyo değerlendirmesi.',
            'process': ['a) Yazılı ve sözlü anlatım ürünlerini sergiler.'],
            'concepts': ['Portfolyo', 'Genel Sentez'],
            'skills': ['Öz Değerlendirme', 'Dönem Tekrarı'], 'pedagogical': '1. dönem karnesi öncesi deneme yapılır.',
            'context': 'Dönem Tekrarı', 'question': 'Türkçede kaç kip türü vardır?',
            'solution': 'Haber (bildirme) ve Dilek (tasarlama) olmak üzere 2 ana grup vardır.',
            'weeklyGoal': '1. dönem Türkçe konularını pekiştirme.', 'evaluation': '1. Dönem Karnesi Öncesi Sınavı'
        },
        # 2. DÖNEM (20-36)
        {
            'theme': 'Doğa ve Evren', 'subTheme': 'Anlatım Bozuklukları', 'code': 'TÜR.7.5.1',
            'title': 'Anlam Düzeyinde Anlatım Bozuklukları',
            'description': 'Gereksiz sözcük kullanımı, çelişen sözcüklerin bir arada bulunması hatalarını düzeltme.',
            'process': ['a) Eş anlamlı kelimelerin bir arada kullanımını tespit eder.'],
            'concepts': ['Gereksiz Sözcük', 'Çelişen Sözler', 'Mantık Hatası'],
            'skills': ['Dili Duru Kullanma', 'Düzeltme'], 'pedagogical': 'Cümle cerrahlığı çalışması yapılır.',
            'context': 'Düzeltme', 'question': '"Tam olarak yaklaşık on kişi geldi" cümlesindeki bozukluk nedir?',
            'solution': '"Tam" ve "yaklaşık" çelişen ifadelerdir; biri çıkarılmalıdır.',
            'weeklyGoal': 'Anlama dayalı anlatım bozukluklarını düzeltme.', 'evaluation': 'Anlatım bozukluğu düzeltme'
        },
        {
            'theme': 'Doğa ve Evren', 'subTheme': 'Anlatım Bozuklukları 2', 'code': 'TÜR.7.5.1',
            'title': 'Sözcüğün Yanlış Yerde ve Yanlış Anlamda Kullanımı',
            'description': 'Sözcüklerin cümledeki sırasından ve anlam inceliklerinden doğan hataları giderme.',
            'process': ['a) "Çok güneşte kalmak" yerine "Güneşte çok kalmak" düzeltmesini yapar.'],
            'concepts': ['Sözcük Sırası', 'Yanlış Anlamda Kullanım'],
            'skills': ['Cümle Mimarisi', 'Düzeltme'], 'pedagogical': 'Cümledeki kelimelerin yeri düzeltilir.',
            'context': 'Düzeltme', 'question': '"Yeni okula geldim ki ders bitti" cümlesindeki hata nedir?',
            'solution': '"Okula yeni geldim" şeklinde düzeltilmelidir.',
            'weeklyGoal': 'Sözcük sırası bozukluklarını giderme.', 'evaluation': 'Cümle cerrahlığı atölyesi'
        },
        {
            'theme': 'Doğa ve Evren', 'subTheme': 'Görsel Okuma', 'code': 'TÜR.7.1.5',
            'title': 'Grafik, Tablo ve İnfografik Okuma',
            'description': 'Sayısal verileri ve infografik şemaları sözel paragrafa aktarma.',
            'process': ['a) Grafikteki uç değerleri ve oranları yorumlar.'],
            'concepts': ['Görsel Okuma', 'İnfografik', 'Tablo Yorumu'],
            'skills': ['Çoklu Okuryazarlık', 'Veri Analizi'], 'pedagogical': 'Grafik okuma alıştırmaları yapılır.',
            'context': 'Veri Analizi', 'question': 'İnfografikte pasta grafiği neyi gösterir?',
            'solution': 'Bütünün parçalara dağılımını ve yüzde oranlarını gösterir.',
            'weeklyGoal': 'Grafik ve infografikleri sözel ifadeye dönüştürme.', 'evaluation': 'İnfografik hazırlama görevi'
        },
        {
            'theme': 'Sanat ve Estetik', 'subTheme': 'Metin Türleri 3', 'code': 'TÜR.7.3.3',
            'title': 'Günlük (Günce) ve Anı (Hatıra)',
            'description': 'Günü gününe yazılan günlük ile üzerinden zaman geçtikten sonra yazılan anıyı karşılaştırma.',
            'process': ['a) Tarih atma ve samimi dil özelliklerini inceler.'],
            'concepts': ['Günlük', 'Anı', 'Tarih'],
            'skills': ['Zaman ve Hafıza', 'Metin Türü'], 'pedagogical': 'Günlük ve anı sayfaları karşılaştırılır.',
            'context': 'Metin Türü', 'question': 'Yaşanan olayların günü gününe tarih atılarak yazıldığı tür nedir?',
            'solution': 'Günlüktür (günce).',
            'weeklyGoal': 'Günlük ve anı türlerini ayırt etme.', 'evaluation': 'Kişisel günlük yazma etkinliği'
        },
        {
            'theme': 'Sanat ve Estetik', 'subTheme': 'Şiir Bilgisi', 'code': 'TÜR.7.1.6',
            'title': 'Ana Duygu (Tema), Uyak ve Redif',
            'description': 'Şiirde ahenk unsurlarını, dize sonlarındaki ses benzerliklerini ve ana duyguyu keşfetme.',
            'process': ['a) Redif ile kafiye arasındaki görev farkını kavrar.'],
            'concepts': ['Ana Duygu', 'Kafiye (Uyak)', 'Redif', 'Dize'],
            'skills': ['Şiir Zevki', 'Estetik'], 'pedagogical': 'Dize sonundaki aynı görevli ekler kırmızıyla çizilir.',
            'context': 'Şiir İnceleme', 'question': 'Dize sonundaki aynı görevli ek veya kelime tekrarına ne denir?',
            'solution': 'Redif denir.',
            'weeklyGoal': 'Şiirde kafiye ve redif unsurlarını bulma.', 'evaluation': 'Şiir tahlil kâğıdı'
        },
        {
            'theme': 'Sanat ve Estetik', 'subTheme': 'Metinler Arası Karşılaştırma', 'code': 'TÜR.7.1.7',
            'title': 'Farklı Metinlerde Aynı Temanın İşlenişi',
            'description': 'İki farklı yazarın aynı konuyu hangi bakış açılarıyla ele aldığını değerlendirme.',
            'process': ['a) Karşılaştırma kriterleri belirler.'],
            'concepts': ['Bakış Açısı', 'Tema', 'Metinler Arasılık'],
            'skills': ['Derinlemesine Eleştiri', 'Karşılaştırma'], 'pedagogical': 'Metin karşılaştırma matrisi doldurulur.',
            'context': 'Karşılaştırma', 'question': 'Aynı konu farklı türlerde işlenebilir mi?',
            'solution': 'Evet; hikâye ve şiirde aynı tema farklı duyarlılıklarla işlenebilir.',
            'weeklyGoal': 'Farklı metinlerdeki ortak temaları analiz etme.', 'evaluation': 'Metin karşılaştırma matrisi'
        },
        {
            'theme': 'Hak ve Sorumluluklar', 'subTheme': 'Yazma Becerisi', 'code': 'TÜR.7.4.3',
            'title': 'Düşünce Yazısı Yazma (Deneme)',
            'description': 'Giriş, gelişme ve sonuç planına uygun olarak kendi özgün fikirlerini yazılı ifade etme.',
            'process': ['a) Başlık ile içerik uyumunu sağlar.'],
            'concepts': ['Kompozisyon', 'Paragraf Düzeni', 'Düşünce Yazısı'],
            'skills': ['Yaratıcı Yazma', 'Kompozisyon'], 'pedagogical': 'Deneme yazma atölyesi yapılır.',
            'context': 'Kompozisyon', 'question': 'Deneme türünde kanıtlama zorunluluğu var mıdır?',
            'solution': 'Hayır, yazar kendi kendisiyle samimi bir şekilde konuşur gibi yazar.',
            'weeklyGoal': 'Kurallara uygun deneme yazma.', 'evaluation': 'Deneme yazma atölyesi'
        },
        {
            'theme': 'Hak ve Sorumluluklar', 'subTheme': 'Söz Sanatları', 'code': 'TÜR.7.1.8',
            'title': 'Kişileştirme, Konuşturma ve Abartma',
            'description': 'Teşhis, intak ve mübalağa sanatlarının anlatıma kattığı zenginliği keşfetme.',
            'process': ['a) İnsan dışı varlıklara insan özelliği verilmesini açıklar.'],
            'concepts': ['Kişileştirme', 'Konuşturma', 'Abartma (Mübalağa)'],
            'skills': ['İmgesel Düşünme', 'Söz Sanatı'], 'pedagogical': 'Şiirlerdeki teşhis ve intak bulunur.',
            'context': 'Söz Sanatı', 'question': '"Güneş bize gülümsüyordu" dizesindeki sanat nedir?',
            'solution': 'Kişileştirme (teşhis) sanatıdır.',
            'weeklyGoal': 'Söz sanatlarını şiirlerde doğru belirleme.', 'evaluation': 'Şiirde söz sanatı bulma'
        },
        {
            'theme': 'Ara Tatil', 'subTheme': '2. Dönem Ara Tatili', 'code': 'TÜR.7.GENEL.3',
            'title': 'Dil Bilgisi ve Okuma Kampı',
            'description': 'Zarflar, anlatım bozuklukları ve metin türlerinin beceri temelli sorularla tekrarı.',
            'process': ['a) Yeni nesil sözel muhakeme soruları çözer.'],
            'concepts': ['Sözel Mantık', 'Tekrar'],
            'skills': ['Akıl Yürütme', 'Mantık'], 'pedagogical': 'Tatil fasikülü uygulanır.',
            'context': 'Mantık', 'question': 'Sözel mantık sorularında ilk adım nedir?',
            'solution': 'Verilen öncülleri sıralı bir tabloya dökmektir.',
            'weeklyGoal': '2. dönem ara tatilinde dil becerilerini pekiştirme.', 'evaluation': 'Ara Tatil Dijital Fasikülü'
        },
        {
            'theme': 'Zaman ve Mekân', 'subTheme': 'Metin Türleri 4', 'code': 'TÜR.7.3.4',
            'title': 'Gezi Yazısı (Seyahatname)',
            'description': 'Gezilip görülen yerlerin tarihî ve coğrafi özelliklerinin anlatıldığı gezi yazısını inceleme.',
            'process': ['a) Evliya Çelebi Seyahatnamesi örneğini inceler.'],
            'concepts': ['Gezi Yazısı', 'Gözlem', 'Tasvir'],
            'skills': ['Gözlem ve Kültür', 'Metin Türü'], 'pedagogical': 'Seyahat broşürü tasarlanır.',
            'context': 'Metin Türü', 'question': 'Gezi yazılarında yazar neye dayanarak yazar?',
            'solution': 'Bizzat gezdiği yerlerdeki gözlemlerine ve incelemelerine dayanarak yazar.',
            'weeklyGoal': 'Gezi yazısı türünün özelliklerini saptama.', 'evaluation': 'Seyahat broşürü tasarlama'
        },
        {
            'theme': 'Zaman ve Mekân', 'subTheme': 'Cümlede Anlam 2', 'code': 'TÜR.7.1.9',
            'title': 'Öznel ve Nesnel Anlatım',
            'description': 'Kanıtlanabilir yargılar ile kişisel beğeni içeren yargıları birbirinden kesin olarak ayırma.',
            'process': ['a) Kişiden kişiye değişen durumları öznel olarak etiketler.'],
            'concepts': ['Öznel Yargı', 'Nesnel Yargı', 'Kanıtlanabilirlik'],
            'skills': ['Eleştirel Düşünme', 'Yargı Türü'], 'pedagogical': 'Kanıtlanabilirlik alıştırmaları yapılır.',
            'context': 'Yargı Türü', 'question': '"Türkiye\'nin başkenti Ankara\'dır" cümlesi nasıldır?',
            'solution': 'Kanıtlanabilir olduğu için nesnel bir yargıdır.',
            'weeklyGoal': 'Öznel ve nesnel yargıları doğru ayırt etme.', 'evaluation': 'Öznel-nesnel sınıflandırma'
        },
        {
            'theme': 'Zaman ve Mekân', 'subTheme': 'Sözel Mantık', 'code': 'TÜR.7.1.10',
            'title': 'Sözel Akıl Yürütme ve Sıralama Problemleri',
            'description': 'İpuçlarından yararlanarak tablo oluşturma ve kesin yargılara ulaşma.',
            'process': ['a) Olumsuz önermeleri eler.'],
            'concepts': ['Sözel Mantık', 'Tablo Çizimi', 'Akıl Yürütme'],
            'skills': ['LGS Hazırlık Temeli', 'Mantık Sorusu'], 'pedagogical': 'Sözel mantık tablosu çizilir.',
            'context': 'Mantık Sorusu', 'question': 'A, B ve C koşucularından A sonuncu değilse ve B birinciyse C kaçıncıdır?',
            'solution': 'C sonuncu (üçüncü) olur.',
            'weeklyGoal': 'Sözel mantık sıralama problemlerini çözme.', 'evaluation': 'Sözel mantık labirent föyü'
        },
        {
            'theme': 'İletişim ve Medya', 'subTheme': 'Medya Okuryazarlığı', 'code': 'TÜR.7.1.11',
            'title': 'Haber Metni ve Güvenilir Kaynak Analizi',
            'description': 'İnternet ve yazılı basındaki haberlerin 5N1K kuralına uygunluğunu denetleme.',
            'process': ['a) Ne, nerede, ne zaman, nasıl, neden ve kim sorularını sorar.'],
            'concepts': ['5N1K', 'Medya Dili', 'Haber'],
            'skills': ['Sorgulayıcı Bilinç', 'Haber Analizi'], 'pedagogical': 'Sınıf gazetesi çıkarma atölyesi yapılır.',
            'context': 'Haber Analizi', 'question': '5N1K açılımındaki 5N nedir?',
            'solution': 'Ne, nerede, ne zaman, nasıl, neden.',
            'weeklyGoal': 'Haber metinlerinde 5N1K unsurlarını tespit etme.', 'evaluation': 'Sınıf gazetesi çıkarma projesi'
        },
        {
            'theme': 'İletişim ve Medya', 'subTheme': 'Tartışma ve Münazara', 'code': 'TÜR.7.1.12',
            'title': 'Görüş Geliştirme ve Kanıt Sunma',
            'description': 'Karşıt fikirleri dinleme, nezaket kurallarına uygun biçimde antitez geliştirme.',
            'process': ['a) İkna edici argümanlar sunar.'],
            'concepts': ['Münazara', 'Argüman', 'Etkili İletişim'],
            'skills': ['Demokratik Diyalog', 'İletişim'], 'pedagogical': 'Sınıf içi münazara düzenlenir.',
            'context': 'İletişim', 'question': 'Münazarada temel amaç nedir?',
            'solution': 'Tezi etkili kanıtlarla jüriye savunmaktır.',
            'weeklyGoal': 'Münazara kurallarına uygun kanıt sunma.', 'evaluation': 'Sınıf içi münazara etkinliği'
        },
        {
            'theme': 'Kişisel Gelişim', 'subTheme': 'Dinleme / İzleme Stratejileri', 'code': 'TÜR.7.1.13',
            'title': 'Not Alarak ve Seçici Dinleme',
            'description': 'Konuşmacının anahtar kelimelerini yakalama ve zihin haritası oluşturma.',
            'process': ['a) Önemli bilgileri özetler.'],
            'concepts': ['Seçici Dinleme', 'Zihin Haritası'],
            'skills': ['Bilişsel Dikkat', 'Dinleme'], 'pedagogical': 'Konuşma esnasında not alma pratiği yapılır.',
            'context': 'Dinleme', 'question': 'Konuşma esnasında not almanın faydası nedir?',
            'solution': 'Önemli fikirlerin kalıcı olmasını ve hatırlanmasını sağlar.',
            'weeklyGoal': 'Not alarak seçici dinleme becerisi edinme.', 'evaluation': 'Konuşma özeti formu'
        },
        {
            'theme': 'Kişisel Gelişim', 'subTheme': 'Yıl Sonu Projesi', 'code': 'TÜR.7.4.4',
            'title': 'Yaratıcı Yazarlık ve Masal / Hikâye Yazımı',
            'description': 'Öğrenilen dil zenginliklerini kullanarak özgün kurgulu bir hikâye oluşturma.',
            'process': ['a) Serim, düğüm, çözüm planını uygular.'],
            'concepts': ['Kurgu', 'Karakter', 'Çatışma'],
            'skills': ['Estetik Yaratıcılık', 'Yazarlık'], 'pedagogical': 'Hikâye yarışması sergisi açılır.',
            'context': 'Yazarlık', 'question': 'Hikâyede merak unsurunun doruğa çıktığı bölüm neresidir?',
            'solution': 'Düğüm bölümüdür.',
            'weeklyGoal': 'Kurgusal bir hikâye yazarak sergileme.', 'evaluation': 'Hikâye yarışması sergisi'
        },
        {
            'theme': 'Yıl Sonu', 'subTheme': 'Genel Değerlendirme', 'code': 'TÜR.7.6.1',
            'title': '7. Sınıf Türkçe Kazanımları Yıl Sonu Analizi ve 8. Sınıf LGS Köprüsü',
            'description': '8. sınıf LGS Türkçe ve Paragraf becerilerine hazırlık köprüsünün kurulması.',
            'process': ['a) 8. sınıfa dair hedef ve okuma planı belirler.'],
            'concepts': ['LGS Türkçe', 'Kitap Listesi'],
            'skills': ['Sürekli Gelişim', 'Gelecek Yıl'], 'pedagogical': 'Yıl sonu Türkçe şenliği düzenlenir.',
            'context': 'Gelecek Yıl', 'question': '8. sınıf Türkçe dersinin omurgasını hangi konu oluşturur?',
            'solution': 'Fiilimsiler, Cümlenin Ögeleri ve Paragrafta Anlam oluşturur.',
            'weeklyGoal': '7. sınıf Türkçe programını tamamlayıp LGS hazırlığına başlama.', 'evaluation': 'Yıl sonu Türkçe şenliği'
        }
    ]
    return {
        'title': '7. Sınıf',
        'subtitle': 'Ortaokul 3. Kademe Türkçe Programı',
        'badge': 'Ortaokul Türkçe',
        'weeks': weeks
    }

print("Turkce 7 builder compiled.")
