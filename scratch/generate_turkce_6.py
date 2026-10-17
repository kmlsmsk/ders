# -*- coding: utf-8 -*-
"""
Generates 36 weeks for Grade 6 and Grade 8 (LGS) in Türkçe.
"""

def build_turkce_6():
    # 6. Sınıf Türkçe MEB Müfredatı (Sözcükte Anlam, Kök-Ek, İsim-Sıfat-Zamir, Edat-Bağlaç, Tamlamalar, Metin Türleri, Yazım-Noktalama)
    weeks = [
        # 1-6: Sözcükte Anlam ve Kökler
        {
            'theme': 'Sözcükte Anlam', 'subTheme': 'Gerçek, Mecaz ve Terim Anlam',
            'code': 'TÜR.6.1.1', 'title': 'Sözcüklerin Bağlamsal Anlamları ve Çok Anlamlılık',
            'description': 'Sözcüklerin cümledeki bağlamsal kullanımına göre temel (gerçek), mecaz ve terim anlamlarını ayırt eder; çok anlamlılığı çözümler.',
            'process': ['a) \'Açmak\' sözcüğünün farklı cümlelerdeki 5 farklı anlamını eşleştirir.', 'b) Mecazlaşma yollarını modeller.'],
            'concepts': ['Gerçek Anlam', 'Mecaz Anlam', 'Terim Anlam', 'Çok Anlamlılık'],
            'skills': ['Söz Varlığı', 'Metin Çözümleme'], 'pedagogical': 'Kelime avı ve cümle içi anlam eşleştirme yapılır.',
            'context': 'Edebî Metinler', 'question': '\'Ağır\' sözcüğü \'Bu ağır çantayı taşımakta zorlandı\' cümlesinde hangi anlamdadır?',
            'solution': 'Gerçek anlamdadır; tartıda çok çeken, kütlesi fazla olan demektir.', 'weeklyGoal': 'Sözcüklerin gerçek ve mecaz anlamlarını doğru ayırt etme.',
            'evaluation': 'Çok anlamlılık çalışma kâğıdı'
        },
        {
            'theme': 'Sözcükte Anlam', 'subTheme': 'Deyimler ve Atasözleri',
            'code': 'TÜR.6.1.1', 'title': 'Deyim ve Atasözlerinin Cümleye Kattığı Anlam',
            'description': 'Kültürel zenginliğimiz olan deyim ve atasözlerini metinlerde bularak anlatıma kattığı derinliği açıklar.',
            'process': ['a) Kalıplaşmış söz öbeklerinin değiştirilemeyeceğini savunur.', 'b) Öğüt veren atasözlerini temalarına göre gruplar.'],
            'concepts': ['Deyim', 'Atasözü', 'Öğüt', 'Kalıplaşmış Anlatım'],
            'skills': ['Kültürel Aktarım', 'Mecazi Algı'], 'pedagogical': 'Deyim tamamlama bulmacaları çözülür.',
            'context': 'Dede Korkut ve Nasreddin Hoca', 'question': "'Ayağını yorganına göre uzat' atasözünün verdiği temel öğüt nedir?",
            'solution': 'Giderlerin ve harcamaların gelire (bütçeye) göre dengeli planlanması gerektiği öğüdünü verir.', 'weeklyGoal': 'Deyim ve atasözlerini doğru bağlamda kullanma.',
            'evaluation': 'Deyimler ve atasözleri eşleştirme testi'
        },
        {
            'theme': 'Sözcükte Anlam', 'subTheme': 'Söz Sanatları (Kişileştirme ve Konuşturma)',
            'code': 'TÜR.6.1.2', 'title': 'Teşhis (Kişileştirme) ve İntak (Konuşturma) Sanatları',
            'description': 'İnsan dışındaki varlıklara insan özelliği verilmesini (kişileştirme) ve bu varlıkların konuşturulmasını (intak/konuşturma: Fabl) çözümler.',
            'process': ['a) Her intak sanatında mutlaka kişileştirme de olduğunu kavrar.', 'b) Fabl türündeki konuşturma örneklerini inceler.'],
            'concepts': ['Kişileştirme (Teşhis)', 'Konuşturma (İntak)', 'Fabl'],
            'skills': ['Edebî Sanat Tespiti', 'İmgesel Düşünme'], 'pedagogical': 'La Fontaine fablları okunup intak sanatları bulunur.',
            'context': 'Fabl ve Şiir Sanatı', 'question': "'Rüzgâr neşeyle ıslık çalıyor, ağaçlar bize el sallıyordu' cümlesinde hangi söz sanatı vardır?",
            'solution': 'Kişileştirme (teşhis) sanatı vardır; rüzgâra ve ağaçlara insana ait özellikler yüklenmiştir.', 'weeklyGoal': 'Kişileştirme ve konuşturma sanatlarını ayırt etme.',
            'evaluation': 'Söz sanatları analiz föyü'
        },
        {
            'theme': 'Biçim Bilgisi', 'subTheme': 'Kökler (İsim Kökü ve Fiil Kökü)',
            'code': 'TÜR.6.2.1', 'title': 'Sözcüğün Kökünü Bulma ve İsim-Fiil Kökü Ayırımı (-mek/-mak Mastar Eki)',
            'description': 'Sözcüğün anlamlı en küçük parçasını (kök) bulur; sonuna \'-mek/-mak\' mastar eki alabilenlere fiil kökü, alamayanlara isim kökü dendiğini modeller.',
            'process': ['a) Kök ile sözcüğün türemiş hâli arasındaki anlam bağını denetler (örneğin \'balık\'ın kökü \'bal\' değildir).', 'b) Sesteş (eş sesli) kökleri ayırt eder.'],
            'concepts': ['Kök', 'İsim Kökü', 'Fiil Kökü', 'Mastar Eki (-mek/-mak)', 'Anlam Bağı'],
            'skills': ['Kelime Anatomisi', 'Morfolojik Analiz'], 'pedagogical': 'Kök bulma dedektifi oyunu oynatılır.',
            'context': 'Dil Bilgisi Atölyesi', 'question': "'Gözlükçülük, koşucular, sulamak' sözcüklerinin köklerinin türü sırasıyla nedir?",
            'solution': 'Göz (İsim kökü), Koş- (Fiil kökü), Su (İsim kökü).', 'weeklyGoal': 'Kelimelerin köklerini ve türlerini hatasız tespit etme.',
            'evaluation': 'Kök bulma ve tür belirleme tablosu'
        },
        {
            'theme': 'Biçim Bilgisi', 'subTheme': 'Yapım Ekleri ve Türemiş Sözcükler',
            'code': 'TÜR.6.2.2', 'title': 'İsimden İsim, İsimden Fiil, Fiilden İsim ve Fiilden Fiil Yapım Ekleri',
            'description': 'Sözcüğün anlamını veya türünü değiştiren yapım eklerini; gövde kavramını ve türemiş sözcük oluşturma mekanizmasını çözümler.',
            'process': ['a) \'Göz\' -> \'Gözlük\' -> \'Gözlükçü\' gövde basamaklarını modeller.', 'b) Basit sözcük ile türemiş sözcük farkını açıklar.'],
            'concepts': ['Yapım Eki', 'Gövde', 'Türemiş Sözcük', 'Basit Sözcük'],
            'skills': ['Sözcük Türetme', 'Dil Mimarisi'], 'pedagogical': 'Lego parçaları gibi kök ve ekler birleştirilerek anlam değişimleri izlenir.',
            'context': 'Türkçenin Ek Zenginliği', 'question': "'Yazarlık, sevgi, sulamak' sözcükleri yapısına göre basit midir türemiş midir?",
            'solution': 'Yapım eki (-lık, -gi, -la) alarak yeni anlam kazandıkları için türemiş sözcüklerdir.', 'weeklyGoal': 'Yapım eklerinin işlevlerini ve türemiş sözcükleri kavrama.',
            'evaluation': 'Yapım eki çözümleme çalışma kağıdı'
        },
        {
            'theme': 'Biçim Bilgisi', 'subTheme': 'Çekim Ekleri (İsim Çekim Ekleri)',
            'code': 'TÜR.6.2.3', 'title': 'Çoğul Eki, Hâl Ekleri, İyelik (Aitlik) Ekleri ve İlgi (Tamlayan) Eki',
            'description': 'İsimlere gelerek onların anlamını değiştirmeyip cümledeki görevini belirleyen çoğul (-lar), hâl (-i, -e, -de, -den), iyelik (-im, -in, -i...) ve ilgi (-in) eklerini inceler.',
            'process': ['a) \'Kitabım\' (1. tekil iyelik eki) aitlik anlamını çözümler.', 'b) 3. tekil iyelik eki (-i) ile belirtme hâl ekini (-i) \'onun\' zamiriyle ayırt eder.'],
            'concepts': ['Çekim Eki', 'İyelik Eki (Aitlik)', 'Hâl Eki', 'İlgi Eki', 'Aitlik'],
            'skills': ['Hassas Ek Analizi', 'Fonksiyonel Dil Bilgisi'], 'pedagogical': "'(Onun) evi çok güzel' (iyelik) ile 'Evi dün temizledik' (belirtme hâli) karşılaştırılır.",
            'context': 'Dil Bilgisi Zirvesi', 'question': "'Kalemini kaybetmiş' cümlesindeki ilk ve ikinci '-i' eklerinin görevleri sırasıyla nedir?",
            'solution': 'Birinci -i iyelik (aitlik) eki, ikinci -i ise ismin belirtme hâl ekidir (Kalem-i-n-i).', 'weeklyGoal': 'İsim çekim eklerini görevlerine göre doğru sınıflandırma.',
            'evaluation': 'İsim çekim ekleri matrisi'
        },

        # 7-12: İsimler ve Tamlamalar
        {
            'theme': 'Sözcük Türleri', 'subTheme': 'İsimler (Adlar)',
            'code': 'TÜR.6.3.1', 'title': 'Varlıklara Verilişine, Maddelerine ve Sayılarına Göre İsimler',
            'description': 'Özel isim - cins isim; somut isim - soyut isim; tekil isim - çoğul isim - topluluk ismini (orman, ordu, sürü, demet) sınıflandırır.',
            'process': ['a) Beş duyu organıyla algılanabilen somut isimler ile algılanamayan soyut isimleri (rüya, sevgi) ayırt eder.', 'b) Topluluk isimlerinin çoğul eki almadan çokluk bildirdiğini kavrar.'],
            'concepts': ['İsim (Ad)', 'Özel İsim', 'Cins İsim', 'Somut', 'Soyut', 'Topluluk İsmi'],
            'skills': ['Kavramsal Sınıflandırma', 'Varlık Kategorizasyonu'], 'pedagogical': 'Sınıf panosunda isim ağacı kategorileri doldurulur.',
            'context': 'Varlıklar Dünyası', 'question': "'Orman, ordu, deste, meclis' sözcükleri sayılarına göre hangi isim grubuna girer?",
            'solution': 'Biçimce tekil olmalarına rağmen anlamca çokluk bildirdikleri için \'topluluk ismi\' grubuna girer.', 'weeklyGoal': 'İsimleri özelliklerine göre eksiksiz sınıflandırma.',
            'evaluation': 'İsim türleri sınıflandırma tablosu'
        },
        {
            'theme': 'Sözcük Türleri', 'subTheme': 'İsim Tamlamaları (Belirtili ve Belirtisiz)',
            'code': 'TÜR.6.3.2', 'title': 'Tamlayan Eki (-ın/-in) ve Tamlanan Eki (-ı/-i) ile Belirtili-Belirtisiz Tamlamalar',
            'description': 'En az iki ismin birbirini tamamlamasıyla oluşan isim tamlamalarını; her iki ögesi ek alan belirtili tamlama (Kapı-n-ın kol-u) ile sadece tamlananı ek alan belirtisiz tamlamayı (Kapı kol-u) çözümler.',
            'process': ['a) Belirtili tamlamada tamlayan ile tamlanan arasına başka sözcükler girebileceğini görür.', 'b) Tamlayan ile tamlananın yer değiştirebildiğini inceler.'],
            'concepts': ['İsim Tamlaması', 'Tamlayan', 'Tamlanan', 'Belirtili İsim Tamlaması', 'Belirtisiz İsim Tamlaması'],
            'skills': ['Öbek Yapısı Çözümleme', 'Söz Dizimi'], 'pedagogical': 'İki öğrenci tamlayan ve tamlanan olup zincir oluşturur.',
            'context': 'Türkçenin Söz Dizimi', 'question': "'Okulun bahçesi' ile 'Okul bahçesi' tamlamalarının türleri sırasıyla nedir?",
            'solution': "'Okulun bahçesi' belirtili isim tamlaması; 'Okul bahçesi' belirtisiz isim tamlamasıdır.", 'weeklyGoal': 'Belirtili ve belirtisiz isim tamlamalarını ayırt etme.',
            'evaluation': 'İsim tamlamaları tespit föyü'
        },
        {
            'theme': 'Sözcük Türleri', 'subTheme': 'Zincirleme İsim Tamlaması',
            'code': 'TÜR.6.3.2', 'title': 'En Az Üç İsmin Birbirine Bağlandığı Zincirleme İsim Tamlamaları',
            'description': 'İç içe geçmiş isim tamlamalarını (Türkçe öğretmeninin kitabı, okul müdürünün odası) çözümler; araya giren sıfatların tamlamayı zincirleme yapmadığını ayırt eder.',
            'process': ['a) Üç ismin de isim soylu olduğunu denetler.', 'b) \'Güzel Türkçe kitabı\' ifadesindeki \'güzel\'in sıfat olduğunu fark eder.'],
            'concepts': ['Zincirleme İsim Tamlaması', 'Üçlü İsim Öbeği', 'Sıfat Ayrımı'],
            'skills': ['Karmaşık Cümle Analizi', 'Sözcük Öbeği Ayrıştırma'], 'pedagogical': 'Üç halkalı zincir modeliyle tamlama şemalandırılır.',
            'context': 'Metin Çözümlemesi', 'question': "'Köy muhtarının oğlu' tamlamasının türü nedir ve kaç isimden oluşmuştur?",
            'solution': 'Köy, muhtar ve oğul olmak üzere 3 isimden oluşan bir \'zincirleme isim tamlaması\'dır.', 'weeklyGoal': 'Zincirleme isim tamlamalarını doğru saptama.',
            'evaluation': 'Tamlamalar karma testi'
        },
        {
            'theme': 'Ara Tatil', 'subTheme': '1. Dönem Ara Tatili',
            'code': 'TÜR.6.GENEL.1', 'title': 'Sözcükte Anlam, Kök-Ek ve İsimler Tekrar Kampı',
            'description': 'Kazanımların beceri temelli paragraf ve dil bilgisi sorularıyla pekiştirilmesi.',
            'process': ['a) Ara tatil deneme sınavını tamamlar.'],
            'concepts': ['Genel Tekrar', 'LGS Temeli'], 'skills': ['Analitik Okuma'],
            'pedagogical': 'Tatil fasikülü kontrolü yapılır.', 'context': 'Tatil Kampı',
            'question': 'İsim tamlamalarında tamlayan hangi eki alır?',
            'solution': "İlgi ekini (-ın / -in / -un / -ün veya zamirlerde -im: benim) alır.",
            'weeklyGoal': 'İlk 9 haftayı kalıcılaştırma.', 'evaluation': 'Ara tatil değerlendirme testi'
        },
        {
            'theme': 'Sözcük Türleri', 'subTheme': 'Sıfatlar (Ön Adlar)',
            'code': 'TÜR.6.3.3', 'title': 'Niteleme Sıfatları ve Belirtme Sıfatları (İşaret, Sayı, Belgisiz, Soru)',
            'description': 'İsimlerin önüne gelerek onları renk, şekil, durum yönünden niteleyen (Nasıl? sorusu) veya işaret, sayı, belgisizlik ve soruyla belirten sıfatları modeller.',
            'process': ['a) Sıfat tamlamasının formülünü (Sıfat + İsim) kavrar.', 'b) \'Birkaç kişi\' (belgisiz sıfat), \'Şu masa\' (işaret sıfatı) örneklerini inceler.'],
            'concepts': ['Sıfat (Ön Ad)', 'Niteleme Sıfatı', 'İşaret Sıfatı', 'Sayı Sıfatı', 'Belgisiz Sıfat', 'Soru Sıfatı'],
            'skills': ['Ön Ad Tespiti', 'Tamlamalar Arası Karşılaştırma'], 'pedagogical': 'Sınıftaki nesneler niteleme ve belirtme sıfatlarıyla betimlenir.',
            'context': 'Betimleyici Anlatım', 'question': "'Kırmızı elma, üç elma, şu elma, bazı elmalar' ifadelerindeki sıfat türlerini sırasıyla belirtiniz.",
            'solution': 'Kırmızı (Niteleme), Üç (Sayı), Şu (İşaret), Bazı (Belgisiz) sıfatıdır.', 'weeklyGoal': 'Sıfatları ve çeşitlerini metinlerde doğru ayırt etme.',
            'evaluation': 'Sıfatlar avı çalışma föyü'
        },
        {
            'theme': 'Sözcük Türleri', 'subTheme': 'Adlaşmış Sıfatlar',
            'code': 'TÜR.6.3.3', 'title': 'Niteleme Sıfatlarının Önündeki İsim Düştüğünde Adlaşması',
            'description': 'Niteleme sıfatının nitelediği isim düştüğünde sıfatın ismin eklerini alarak isimleşmesini (\'Yaşlı insanlar\' yerine \'Yaşlılar\', \'Tembel öğrenciler\' yerine \'Tembeller\') çözümler.',
            'process': ['a) Adlaşmış sıfattan sonra virgülün anlam karışıklığını önlemedeki rolünü açıklar (Ör: İhtiyar, doktora baktı).', 'b) LGS tipi soruları çözer.'],
            'concepts': ['Adlaşmış Sıfat', 'İsim Düşmesi', 'Virgülün Görevi'],
            'skills': ['Hassas Anlam Çıkarımı', 'Noktalama Hassasiyeti'], 'pedagogical': 'Düşen isim kutudan çekilip sıfata ek ekleme animasyonu yapılır.',
            'context': 'LGS Soru Kalıpları', 'question': "'Gençler geleceğe umutla bakmalıdır' cümlesindeki 'gençler' sözcüğünün türü nedir?",
            'solution': "'Genç insanlar' tamlamasındaki isim düştüğü için bir 'adlaşmış sıfattır'.", 'weeklyGoal': 'Adlaşmış sıfatları ve virgül kullanımını analiz edebilme.',
            'evaluation': 'Adlaşmış sıfatlar analiz föyü'
        },

        # 13-17: Zamirler ve Metin Türleri
        {
            'theme': 'Sözcük Türleri', 'subTheme': 'Zamirler (Adıllar)',
            'code': 'TÜR.6.3.4', 'title': 'İsmin Yerini Tutan Sözcük Durumundaki Zamirler (Kişi, İşaret, Belgisiz, Soru)',
            'description': 'İsimlerin yerine kullanılan kişi zamirlerini (ben, sen, o, biz, siz, onlar ve kendi/dönüşlülük); işaret zamirlerini (bu, şu, o, bunlar); belgisiz zamirleri (biri, herkes, hepsi) ve soru zamirlerini inceler.',
            'process': ['a) \'O\' sözcüğünün insan için kullanılırsa kişi, nesne için işaret zamiri olduğunu ayırt eder.', 'b) Zamirlerin isim çekim eklerini alabildiğini kavrar.'],
            'concepts': ['Zamir (Adıl)', 'Kişi Zamiri', 'Dönüşlülük Zamiri (Kendi)', 'İşaret Zamiri', 'Belgisiz Zamir', 'Soru Zamiri'],
            'skills': ['Referans Çözümleme', 'Metin İçi Zamir Takibi'], 'pedagogical': 'Metindeki tüm kişi ve işaret zamirlerinin hangi isimlerin yerini tuttuğu oklarla gösterilir.',
            'context': 'Roman ve Hikâye Okumaları', 'question': "'Bunu ona ben verdim' cümlesindeki zamirleri ve türlerini belirtiniz.",
            'solution': "'Bunu' işaret zamiri, 'ona' kişi zamiri, 'ben' kişi zamiridir.", 'weeklyGoal': 'Zamirleri ve tuttukları isimleri metinde doğru saptama.',
            'evaluation': 'Zamirler avı çalışma föyü'
        },
        {
            'theme': 'Sözcük Türleri', 'subTheme': 'Ek Durumundaki Zamirler',
            'code': 'TÜR.6.3.4', 'title': 'İlgi Zamiri (-ki) ve İyelik Zamirleri',
            'description': 'İsmin yerini tutan bitişik yazılan ilgi zamiri \'-ki\'yi (Benim arabam bozuldu, seninki nerede?) ve iyelik eklerinin aynı zamanda iyelik zamiri sayıldığını kavrar.',
            'process': ['a) İlgi zamiri olan -ki\'nin daima bitişik yazıldığını modeller.', 'b) Bağlaç olan \'ki\' ve sıfat yapan \'-ki\' ile ilgi zamirini karşılaştırır.'],
            'concepts': ['İlgi Zamiri (-ki)', 'İyelik Zamiri', 'Bitişik Yazım'],
            'skills': ['Ek Ayrıştırma', 'Yazım Kuralları'], 'pedagogical': '3 farklı \'ki\' (bağlaç, sıfat, zamir) kartları karşılaştırılır.',
            'context': 'İmla ve Dil Bilgisi', 'question': "'Bizim ev buraya çok yakın, sizinki nerede?' cümlesindeki '-ki' ekinin görevi ve türü nedir?",
            'solution': "'Sizin eviniz' tamlamasındaki 'ev' isminin yerini tutan 'ilgi zamiri'dir.", 'weeklyGoal': 'İlgi zamiri olan -ki\'yi hatasız tanıma ve yazma.',
            'evaluation': '3 Ki kuralı karşılaştırma föyü'
        },
        {
            'theme': 'Metin Türleri', 'subTheme': 'Olay Yazıları (Masal, Fabl, Hikâye, Roman)',
            'code': 'TÜR.6.4.1', 'title': 'Masal ve Fablın Karşılaştırılması ve Hikâye Unsurları',
            'description': 'Tekerlemeyle başlayan, zaman ve mekânı belirsiz, olağanüstü olayları anlatan masal ile kahramanları genellikle hayvan/bitki olan ve ders veren fabl türlerini karşılaştırır.',
            'process': ['a) Masallarda iyilerin hep kazandığını, eğiticilik yönünü inceler.', 'b) Keloğlan ve Binbir Gece Masalları örneklerini değerlendirir.'],
            'concepts': ['Masal', 'Fabl', 'Tekerleme', 'Olağanüstülük', 'Ahlaki Ders'],
            'skills': ['Edebî Tür Mukayesesi', 'Tür Analizi'], 'pedagogical': 'Keloğlan masalı sınıfta canlandırılır.',
            'context': 'Halk Masalları ve Dünya Klasikleri', 'question': 'Masalların başında yer alan \'Bir varmış bir yokmuş, evvel zaman içinde...\' gibi kalıplaşmış sözlere ne ad verilir?',
            'solution': "'Tekerleme' (döşeme) adı verilir; dinleyicinin dikkatini masalın hayal dünyasına çekmek için söylenir.", 'weeklyGoal': 'Masal ve fabl türlerinin özelliklerini ayırt etme.',
            'evaluation': 'Masal ve Fabl karşılaştırma tablosu'
        },
        {
            'theme': 'Metin Türleri', 'subTheme': 'Düşünce Yazıları (Mektup ve Hatıra / Anı)',
            'code': 'TÜR.6.4.2', 'title': 'Yaşanmış Olayların Anlatıldığı Anı (Hatıra) ve Mektup Türü',
            'description': 'Kişinin üzerinden zaman geçtikten sonra geçmişte yaşadığı ya da tanık olduğu olayları kaleme aldığı anı (hatıra) ile duygu ve düşünceleri uzaktakine ileten mektup türünü inceler.',
            'process': ['a) Anının tarihsel belgelere ışık tutan yönünü keşfeder.', 'b) Atatürk\'ün anılarını inceler.'],
            'concepts': ['Anı (Hatıra)', 'Mektup', 'Geçmiş Zaman', 'Tanıklık'],
            'skills': ['Hafıza Yazarlığı', 'Tarihî Empati'], 'pedagogical': 'Öğrenciler kendi çocukluklarına ait unutamadıkları bir anıyı yazarlar.',
            'context': 'Edebî Hatıratlar', 'question': 'Anı (hatıra) türünün günlük (günce) türünden en belirleyici farkı nedir?',
            'solution': 'Günlük günü gününe tarih atılarak sıcağı sıcağına yazılırken; anı olayların üzerinden uzun bir zaman geçtikten sonra hafızaya dayanılarak yazılır.', 'weeklyGoal': 'Anı türünün özelliklerini ve üslubunu kavrama.',
            'evaluation': 'Anı yazma atölyesi değerlendirme rubriği'
        },
        {
            'theme': '1. Dönem Değerlendirme', 'subTheme': '1. Dönem Türkçe Sentezi',
            'code': 'TÜR.6.4.3', 'title': 'Sözcükte Anlam, Kök-Ek, İsim, Sıfat, Zamir ve Metin Türleri 1. Dönem Finali',
            'description': '1. dönemin tüm dil bilgisi ve okuma anlama kazanımlarını kapsayan geniş kapsamlı değerlendirme sınavı ve analiz çalışması yapılır.',
            'process': ['a) Soru çözüm stratejilerini uygular.', 'b) 2. döneme yönelik eksiklerini planlar.'],
            'concepts': ['Dönem Sonu Karnesi', 'Dil Yetkinliği'], 'skills': ['Öz Değerlendirme'],
            'pedagogical': '1. dönem başarı karnesi düzenlenir.', 'context': '1. Dönem Kapanış Denemesi',
            'question': 'İsimlerin yerini tutan sözcüklere ne denir, isimleri niteleyen sözcüklere ne denir?',
            'solution': 'İsmin yerini tutanlara zamir (adıl), isimleri niteleyen veya belirtenlere sıfat (ön ad) denir.', 'weeklyGoal': '1. dönem Türkçe programını eksiksiz tamamlama.',
            'evaluation': '1. Dönem Türkçe Başarı Sınavı'
        },

        # 18-23: Edat, Bağlaç, Ünlem ve Cümlede Anlam
        {
            'theme': 'Sözcük Türleri', 'subTheme': 'Edatlar (İlgeçler)',
            'code': 'TÜR.6.3.5', 'title': 'Tek Başına Anlamı Olmayan, Cümleye Anlam Katan Edatlar',
            'description': 'Tek başlarına anlamı olmayıp cümledeki diğer sözcüklerle anlam ilgisi kuran edatları (gibi, kadar, için, ile, göre, doğru, karşı, rağmen, yalnız) modeller.',
            'process': ['a) \'Cennet gibi vatan\' (benzetme), \'Akşama doğru\' (zaman) edat öbeklerini inceler.', 'b) Edatın cümleden çıkarıldığında anlamın bozulduğunu fark eder.'],
            'concepts': ['Edat (İlgeç)', 'Anlam İlgisi', 'Gibi', 'Kadar', 'İçin', 'Göre'],
            'skills': ['Bağlamsal İlişkilendirme', 'Edat Öbeği Analizi'], 'pedagogical': 'Edatların cümleye kattığı anlamlar (amaç, benzerlik, zaman, araç) tablosu yapılır.',
            'context': 'Cümle Bilgisi', 'question': "'Okula otobüs ile gittik' cümlesindeki 'ile' edatının cümleye kattığı anlam nedir?",
            'solution': "'Araç / vasıta' anlamı katmıştır.", 'weeklyGoal': 'Edatları ve cümleye kattıkları anlam ilgilerini saptama.',
            'evaluation': 'Edatlar çalışma föyü'
        },
        {
            'theme': 'Sözcük Türleri', 'subTheme': 'Bağlaçlar',
            'code': 'TÜR.6.3.5', 'title': 'Eş Görevli Sözcükleri veya Cümleleri Birbirine Bağlayan Bağlaçlar',
            'description': 'Tek başlarına anlamı olmayıp sözcükleri veya cümleleri bağlayan bağlaçları (ve, veya, ile, ama, fakat, ancak, çünkü, de, ki, hem...hem...) çözümler.',
            'process': ['a) \'İle\' sözcüğünün yerine \'ve\' geliyorsa bağlaç, gelmiyorsa edat olduğunu test eder.', 'b) Bağlaçların cümleden çıkarıldığında cümlenin yapısının tamamen bozulmadığını kavrar.'],
            'concepts': ['Bağlaç', 'Ve / Veya', 'Ama / Fakat', 'İle (Edat mı Bağlaç mı?)'],
            'skills': ['Söz Dizimi Analizi', 'Edat-Bağlaç Ayırımı'], 'pedagogical': "'Ali ile Veli geldi' (Ali ve Veli: bağlaç) ile 'Ali arabayla geldi' (araç: edat) testi yapılır.",
            'context': 'Metin Bağlaçları', 'question': "'Elma ile armut aldık' cümlesindeki 'ile' edat mıdır yoksa bağlaç mıdır?",
            'solution': "'İle' yerine 've' konabildiği için ('Elma ve armut aldık') bir bağlaçtır.", 'weeklyGoal': 'Bağlaçları edatlardan ayırt edebilme.',
            'evaluation': 'Edat-Bağlaç ayrım testi'
        },
        {
            'theme': 'Sözcük Türleri', 'subTheme': 'Ünlemler',
            'code': 'TÜR.6.3.5', 'title': 'Duyguları, Çağrıları ve Seslenmeleri Bildiren Ünlemler ve Noktalaması',
            'description': 'Korku, sevinç, şaşkınlık, acıma gibi ani duyguları bildiren (Eyvah, Ah, Vah, Yaşasın) veya seslenme bildiren (Hey, Ey) ünlemleri ve ünlem işaretinin yerini çözümler.',
            'process': ['a) Ünlem işaretinin hemen ünlemden sonra veya cümlenin en sonunda kullanılabileceğini açıklar.', 'b) Ünlemden sonra büyük harfle başlama kuralını kavrar.'],
            'concepts': ['Ünlem', 'Duygu Patlaması', 'Seslenme / Hitap', 'Ünlem İşareti (!)'],
            'skills': ['Vurgu ve Tonlama', 'Duygusal İfade'], 'pedagogical': 'Farklı ünlem kartları çekilerek ses tonu ve mimiklerle canlandırma yapılır.',
            'context': 'Tiyatro ve Seslendirme', 'question': "'Eyvah, yemek yandı!' cümlesinde ünlemin cümleye kattığı duygu nedir?",
            'solution': 'Panik, telaş ve endişe duygusu katmıştır.', 'weeklyGoal': 'Ünlemleri doğru tonlamayla seslendirme ve noktalama kuralını uygulama.',
            'evaluation': 'Ünlemler çalışma kağıdı'
        },
        {
            'theme': 'Yazım Kuralları', 'subTheme': "'de' ve 'ki'nin Yazımı",
            'code': 'TÜR.6.5.1', 'title': 'Bağlaç Olan \'de\' / \'da\' ile Hâl Eki Olan \'-de\' / \'-da\' Ayrımı',
            'description': 'Cümleden çıkarıldığında anlam bozulmuyorsa bağlaç olan ayrı yazılan \'de\'; cümleden çıkarıldığında anlam tamamen bozuluyorsa ismin bulunma hâli olan bitişik yazılan \'-de\' kuralını uygular.',
            'process': ['a) Bağlaç olan \'de\'nin asla \'te/ta\' şeklinde yazılamayacağını öğrenir.', 'b) \'Sende bir şey unuttum\' (hâl eki) ile \'Sen de bizimle gel\' (bağlaç) farkını modeller.'],
            'concepts': ['Bağlaç Olan de', 'Hâl Eki Olan -de', 'Ayrı Yazım', 'Bitişik Yazım', 'Te/Ta Kuralı'],
            'skills': ['İmla Hassasiyeti', 'LGS Soru Kalıbı'], 'pedagogical': "'de'yi parmağımızla kapatıp cümleyi okuma testi sınıfta uygulanır.",
            'context': 'LGS Yazım Kuralları', 'question': "'Evde oturup televizyonda izledik' cümlesindeki yazım yanlışı nedir ve nasıl düzeltilir?",
            'solution': "'Televizyon da' şeklinde ayrı yazılmalıdır; çünkü 'dahi / bile' anlamı katan bağlaçtır.", 'weeklyGoal': "'de' ve 'ki'nin yazımını hatasız denetleme.",
            'evaluation': 'De ve ki yazımı avı testi'
        },
        {
            'theme': 'Yazım Kuralları', 'subTheme': "Soru Eki 'mi' ve Sayıların Yazımı",
            'code': 'TÜR.6.5.1', 'title': "Soru Eki 'mı/mi/mu/mü'nün Yazılışı ve Sayıların Metin İçinde Yazımı",
            'description': "Soru ekinin daima kendinden önceki sözcükten ayrı yazıldığını ve gelen eklerin ona bitiştiğini (Gelecek misin?); sayılara gelen eklerin kesmeyle ayrıldığını ve saatlerin arasında tek nokta olduğunu modeller.",
            'process': ['a) Saat yazımında iki nokta (14:30) DEĞİL, Türkçede tek nokta (14.30) kullanıldığını düzeltir.', 'b) Sayıların metin içinde harflerle ayrı yazıldığını (on beş) kavrar.'],
            'concepts': ['Soru Eki (mi)', 'Ayrı Yazım', 'Sayıların Yazımı', 'Saat Yazımı (Tek Nokta)'],
            'skills': ['Yazım Kılavuzu Denetimi', 'Doğru Noktalama'], 'pedagogical': 'Dijital saat ekranı (iki nokta) ile Türkçe TDK kuralı (tek nokta) arasındaki fark gösterilir.',
            'context': 'Resmî Yazışmalar ve Sınavlar', 'question': 'Saat 14 ile 30 arasına Türk Dil Kurumu kurallarına göre hangi noktalama işareti konmalıdır?',
            'solution': 'Tek nokta (.) konmalıdır (14.30). İki nokta üst üste konması yazım yanlışıdır.', 'weeklyGoal': "Soru eki 'mi'yi ve sayıları imla kılavuzuna uygun yazma.",
            'evaluation': 'Yazım kuralları tarama föyü'
        },
        {
            'theme': 'Cümlede Anlam', 'subTheme': 'Örtülü Anlam ve Cümle Yorumu',
            'code': 'TÜR.6.1.3', 'title': 'Cümlede Açıkça Söylenmeyen Gizli (Örtülü) Anlamları Çıkarma',
            'description': "'De' bağlacı, 'artık, bile, yine, en' sözcükleriyle cümlede doğrudan söylenmeyen ancak sezdirilen ikinci ve derin anlamları tespit eder.",
            'process': ['a) \'Ahmet de yarışmaya katıldı\' cümlesinden başkalarının da katıldığı örtülü anlamını çıkarır.', 'b) \'Artık yalan söylemiyor\' cümlesinden eskiden yalan söylediği anlamını yakalar.'],
            'concepts': ['Örtülü Anlam', 'Sezdirim', 'Çıkarım Yapma', 'Cümle Analizi'],
            'skills': ['Satır Arası Okuma', 'Eleştirel Düşünme'], 'pedagogical': 'Örtülü anlam dedektifliği oyunuyla gizli mesajlar bulunur.',
            'context': 'LGS Sözel Muhakeme', 'question': "'Bu yılki tiyatro festivaline geçen yıla göre daha çok katılım oldu' cümlesindeki örtülü anlam nedir?",
            'solution': 'Geçen yıl da tiyatro festivali düzenlendiği ancak katılımın bu yıla göre daha az olduğu anlaşılır.', 'weeklyGoal': 'Cümledeki örtülü anlamları hatasız çözümleme.',
            'evaluation': 'Örtülü anlam tespit kâğıdı'
        },

        # 24-28: Paragrafta Anlam ve Yapı
        {
            'theme': 'Paragrafta Anlam', 'subTheme': 'Paragrafın Konusu ve Başlığı',
            'code': 'TÜR.6.1.4', 'title': 'Paragrafta \'Ne Anlatılıyor?\' Sorusuyla Konu ve Başlık Belirleme',
            'description': 'Yazarın metinde üzerinde durduğu olay, durum veya kavramı (konu) tespit eder; konuyu en iyi özetleyen ilgi çekici başlık belirler.',
            'process': ['a) Konunun metnin tamamını kapsayıcı olması gerektiğini kavrar.', 'b) Başlığın anahtar kelimelerden seçilmesini sağlar.'],
            'concepts': ['Paragrafın Konusu', 'Başlık Belirleme', 'Kapsayıcılık'],
            'skills': ['Metin Özeti', 'Kavramsal Başlıklandırma'], 'pedagogical': 'Metinlerin başlıkları silinerek öğrencilerden 3 farklı başlık alternatifi istenir.',
            'context': 'Gazete Köşe Yazıları', 'question': 'Bir metnin \'konusu\' ile \'ana düşüncesi\' arasındaki temel fark nedir?',
            'solution': 'Konu metinde \'ne anlatıldığıdır\' (örneğin sevgi, çevre); ana düşünce ise yazarın o konuyla ilgili okuyucuya ilettiği \'mesaj veya öğüttür\'.', 'weeklyGoal': 'Paragrafın konusunu ve başlığını doğru saptama.',
            'evaluation': 'Konu ve başlık eşleştirme föyü'
        },
        {
            'theme': 'Paragrafta Anlam', 'subTheme': 'Düşünceyi Geliştirme Yolları',
            'code': 'TÜR.6.1.4', 'title': 'Tanımlama, Örnekleme, Karşılaştırma ve Tanık Gösterme',
            'description': 'Yazarın düşüncelerini ispatlamak için başvurduğu tanımlama, örnekleme, karşılaştırma ve alanında uzman bir kişinin sözünü tırnak içinde aktarma (tanık gösterme) yollarını modeller.',
            'process': ['a) Tırnak içinde ünlü bir düşünürün sözü varsa tanık gösterme olduğunu kavrar.', 'b) Sayısal verilerden yararlanma tekniğini inceler.'],
            'concepts': ['Düşünceyi Geliştirme', 'Tanık Gösterme', 'Örnekleme', 'Karşılaştırma', 'Sayısal Veriler'],
            'skills': ['Metin İnceleme', 'İkna Stratejilerini Belirleme'], 'pedagogical': 'Makalelerdeki tanık gösterme alıntıları incelenir.',
            'context': 'LGS Paragraf Teknikleri', 'question': 'Yazarın savunduğu tezi inandırıcı kılmak için Atatürk\'ün veya Yunus Emre\'nin bir sözünü tırnak içinde aynen aktarması hangi düşünceyi geliştirme yoludur?',
            'solution': "'Tanık gösterme' (alıntı yapma) yoludur.", 'weeklyGoal': 'Düşünceyi geliştirme yollarını metinlerde ayırt etme.',
            'evaluation': 'Düşünceyi geliştirme yolları tahlil föyü'
        },
        {
            'theme': 'Paragrafta Anlam', 'subTheme': 'Anlatım Biçimleri (Öyküleme, Betimleme, Açıklama, Tartışma)',
            'code': 'TÜR.6.1.4', 'title': '4 Temel Anlatım Biçiminin Özellikleri ve Ayırt Edilmesi',
            'description': 'Olay, kişi, yer ve zaman içeren öykülemeyi (video gibi hareketli); sözcüklerle resim çizen betimlemeyi (fotoğraf gibi durağan); bilgi veren açıklamayı ve karşıt fikri çürütmeye çalışan tartışmayı çözümler.',
            'process': ['a) Masal ve hikâyelerde öyküleme ve betimlemenin ağırlıklı olduğunu görür.', 'b) Ders kitapları ve makalelerde açıklayıcı anlatımın kullanıldığını fark eder.'],
            'concepts': ['Öyküleyici Anlatım', 'Betimleyici Anlatım', 'Açıklayıcı Anlatım', 'Tartışmacı Anlatım'],
            'skills': ['Üslup Tespiti', 'Metin Sınıflandırma'], 'pedagogical': 'Video analojisi (öyküleme) ve fotoğraf karesi analojisi (betimleme) ile ayrım somutlaştırılır.',
            'context': 'Roman ve Makale Analizi', 'question': "'Masanın üzerinde tozlu, yıpranmış deri kapaklı bir defter vardı; odanın perdeleri soluk sarıydı' cümlesinde hangi anlatım biçimi ağır basmaktadır?",
            'solution': 'Gözle görülen varlıkları zihinde canlandırmaya yönelik sözcüklerle resim çizildiği için \'betimleyici anlatım\' (tasvir) ağır basmaktadır.', 'weeklyGoal': '4 anlatım biçimini metinlerde hatasız ayırt etme.',
            'evaluation': 'Anlatım biçimleri tespit tablosu'
        },
        {
            'theme': 'Ara Tatil', 'subTheme': '2. Dönem Ara Tatili',
            'code': 'TÜR.6.GENEL.2', 'title': 'Zamirler, Edat-Bağlaç ve Paragraf Becerileri Kampı',
            'description': 'Yeni nesil paragraf, sözel mantık ve dil bilgisi soru tipleri analiz edilir.',
            'process': ['a) Zaman tutarak 20 soruluk deneme çözer.'],
            'concepts': ['Genel Tekrar', 'Zaman Yönetimi'], 'skills': ['Sınav Stratejisi'],
            'pedagogical': 'Tatil soru kampı föyü uygulanır.', 'context': 'Tatil Kampı',
            'question': 'Öyküleme ile betimleme arasındaki en temel fark nedir?',
            'solution': 'Öykülemede zaman akışı ve olaylar zinciri (hareket) varken; betimlemede zaman durur, varlıkların nitelikleri ve görünüşleri tasvir edilir.',
            'weeklyGoal': '2. dönem Türkçe kazanımlarını pekiştirme.', 'evaluation': 'Ara tatil deneme sınavı'
        },
        {
            'theme': 'Noktalama İşaretleri', 'subTheme': 'Noktalı Virgül ve İki Nokta',
            'code': 'TÜR.6.5.2', 'title': 'Noktalı Virgül (;) ile İki Noktanın (:) Karıştırılmaması',
            'description': 'Virgülle ayrılmış tür veya takımları ayırmada (Erkeklere Ali, Can; kızlara Ayşe, Elif) ve ögeleri arasında virgül olan sıralı cümlelerde noktalı virgülün; açıklama veya örnek verilmeden önce iki noktanın kullanımını modeller.',
            'process': ['a) İki noktadan sonra cümle gelirse büyük, örnekler sıralanırsa küçük harfle başlandığını açıklar.', 'b) Noktalı virgülün virgülsüz cümlede bulunamayacağını kavrar.'],
            'concepts': ['Noktalı Virgül (;)', 'İki Nokta (:)', 'Örnek Sıralama', 'Tür ve Takım'],
            'skills': ['Noktalama Mantığı', 'İmla Disiplini'], 'pedagogical': 'Noktalı virgülün bir terazi gibi iki takımı dengelediği şematize edilir.',
            'context': 'LGS Noktalama Soruları', 'question': 'Kendisinden sonra açıklama yapılacak veya örnek verilecek cümlenin sonuna hangi noktalama işareti konur?',
            'solution': 'İki nokta (:) konur.', 'weeklyGoal': 'Noktalı virgül ve iki noktayı doğru yerlerde kullanma.',
            'evaluation': 'Noktalama işaretleri karma föyü'
        },

        # 29-33: Sözel Mantık ve Görsel Yorumlama
        {
            'theme': 'Sözel Mantık', 'subTheme': 'Sıralama ve Yerleşim Problemleri',
            'code': 'TÜR.6.1.5', 'title': 'Öncüllerden Yararlanarak Tablo Çizme ve Kesin Bilgiye Ulaşma',
            'description': 'Apartman katları, yarışma dereceleri, sinema koltukları gibi sıralama problemlerinde öncülleri tabloya yerleştirip kesin olan ve olası durumları ayırt eder.',
            'process': ['a) Olumsuz ifadeleri (Ahmet 3. katta oturmamaktadır) eler.', 'b) Tablo kurarak soru çözer.'],
            'concepts': ['Sözel Mantık', 'Öncül', 'Kesin Bilgi', 'Olasılık Tablosu'],
            'skills': ['Muhakeme', 'Sistematik Düşünme'], 'pedagogical': 'Adım adım ipucu yerleştirme stratejisi tahtada çözülür.',
            'context': 'LGS Mantık Soruları', 'question': 'A, B ve C koşucularının katıldığı yarışta A birinci değilse ve B sonuncu değilse yarışı kim kazanmış olabilir?',
            'solution': 'A birinci değilse ve B sonuncu değilse; yarışı B veya C kazanmış olabilir (ipuçlarına göre netleştirilir).', 'weeklyGoal': 'Sözel mantık sorularında tablo kurarak kesin sonuca ulaşma.',
            'evaluation': 'Sözel mantık labirent föyü'
        },
        {
            'theme': 'Görsel Okuma', 'subTheme': 'Karikatür ve Grafik Yorumlama',
            'code': 'TÜR.6.1.5', 'title': 'Karikatürdeki İletiyi Yakalama ve Grafik Verilerini Sözel Metne Aktarma',
            'description': 'Mizahi çizimlerdeki (karikatür) derin eleştirel mesajı yakalar; çizgi grafikler ve pasta grafiklerdeki değişimleri sözel paragrafa dönüştürür.',
            'process': ['a) Karikatürde verilen ironiyi ve mesajı açıklar.', 'b) Grafikteki en yüksek ve en düşük verileri kıyaslar.'],
            'concepts': ['Karikatür', 'İleti / Mesaj', 'Grafik Yorumlama', 'Görsel Okuma'],
            'skills': ['İronik Algı', 'Görsel Okuryazarlık'], 'pedagogical': 'Ödüllü karikatürler sınıfta incelenerek verilmek istenen sosyal mesaj tartışılır.',
            'context': 'Medya ve Sanat', 'question': 'Bir pasta grafiğinde dilimlerin büyüklüğü neyi gösterir?',
            'solution': 'İncelenen bütünün içinde o dilime ait parçanın oranını (yüzde payını) gösterir.', 'weeklyGoal': 'Görsel ve grafiklerden doğru çıkarımlar yapabilme.',
            'evaluation': 'Karikatür ve grafik yorumlama föyü'
        },
        {
            'theme': 'Metin Türleri', 'subTheme': 'Tiyatro ve Sahne Sanatları',
            'code': 'TÜR.6.4.3', 'title': 'Tiyatro Metinlerinin Unsurları: Perde, Sahne, Jest, Mimik ve Diyalog',
            'description': 'Sahnede canlandırılmak üzere yazılan tiyatro metinlerindeki diyalogları, yay ayraç içindeki oyuncu hareketlerini (jest ve mimik) ve dekor betimlemelerini çözümler.',
            'process': ['a) Yay ayraç içinde verilen sahne yönergelerini inceler.', 'b) Karakterlerin konuşmalarını rollerine uygun seslendirir.'],
            'concepts': ['Tiyatro', 'Diyalog', 'Jest (El-Kol Hareketi)', 'Mimik (Yüz İfadesi)', 'Perde', 'Dekor'],
            'skills': ['Sahne Sanatı Çözümleme', 'Rol Oynama'], 'pedagogical': 'Kısa bir tiyatro sahnesi öğrenciler tarafından sınıfta canlandırılır.',
            'context': 'Okul Tiyatrosu', 'question': 'Tiyatro metinlerinde oyuncunun nasıl davranacağı, ses tonu ve yüz ifadesi hangi işaret içinde yazılır?',
            'solution': 'Yay ayraç (parantez) içinde yazılır.', 'weeklyGoal': 'Tiyatro metninin unsurlarını ve sahneleme özelliklerini kavrama.',
            'evaluation': 'Tiyatro canlandırma ve okuma rubriği'
        },
        {
            'theme': 'Yazma Becerisi', 'subTheme': 'Hikâye (Öykü) Yazma Atölyesi',
            'code': 'TÜR.6.4.4', 'title': 'Serim, Düğüm ve Çözüm Planına Uygun Özgün Hikâye Oluşturma',
            'description': 'Karakterlerin tanıtıldığı serim, merak unsurunun doruğa çıktığı çatışmalı düğüm ve olayın sonuca bağlandığı çözüm bölümlerinden oluşan bir hikâye yazar.',
            'process': ['a) Hikâyede başlık ile olay örgüsünün uyumunu denetler.', 'b) Yazım ve noktalama kurallarına hassasiyet gösterir.'],
            'concepts': ['Serim', 'Düğüm (Merak/Çatışma)', 'Çözüm', 'Olay Örgüsü', 'Yaratıcı Yazarlık'],
            'skills': ['Kurgusal Yazarlık', 'Metin Kompozisyonu'], 'pedagogical': 'Yazılan hikâyeler resimlendirilerek sınıf öykü kitabı oluşturulur.',
            'context': 'Genç Yazarlar Kulübü', 'question': 'Bir hikâyede merak unsurunun en yüksek olduğu ve heyecanın doruğa çıktığı bölüm hangisidir?',
            'solution': "'Düğüm' bölümüdür; çatışma bu bölümde gelişir ve çözüme giden yol merak edilir.", 'weeklyGoal': 'Planlı ve sürükleyici bir kurgusal hikâye yazma.',
            'evaluation': 'Hikâye yazma değerlendirme rubriği'
        },
        {
            'theme': 'Yazma Becerisi', 'subTheme': 'Metin Düzeltme ve Akran Değerlendirmesi',
            'code': 'TÜR.6.4.5', 'title': 'Yazılı Taslakları İnceleme, Hataları Düzeltme ve Redaksiyon',
            'description': 'Kendi yazdığı veya akranının yazdığı metni akıcılık, mantık hataları, sözcük tekrarları, yazım ve noktalama yönünden denetler ve yeniden düzenler.',
            'process': ['a) Anlatım bozukluğu içeren cümleleri düzeltir.', 'b) Akranına yapıcı eleştiri sunar.'],
            'concepts': ['Redaksiyon', 'Düzeltme', 'Akran Değerlendirmesi', 'Akıcılık'],
            'skills': ['Editörlük Becerisi', 'Eleştirel Gözden Geçirme'], 'pedagogical': 'Öğrenciler yazdıkları hikâyeleri birbirleriyle değiş tokuş edip editörlük yaparlar.',
            'context': 'Yayınevi Editörlüğü', 'question': 'Bir metinde aynı anlama gelen sözcüklerin arka arkaya kullanılması hangi anlatım kusuruna yol açar?',
            'solution': "'Gereksiz sözcük kullanımı' kusuruna yol açar ve metnin akıcılığını bozar.", 'weeklyGoal': 'Metinleri eleştirel gözle inceleyip düzenleyebilme.',
            'evaluation': 'Akran değerlendirme editörlük formu'
        },

        # 34-36: Yıl Sonu Değerlendirmesi
        {
            'theme': 'Yıl Sonu Sentezi', 'subTheme': '6. Sınıf Dil Bilgisi Genel Tekrarı',
            'code': 'TÜR.6.6.1', 'title': 'Kök-Ek, Tamlamalar, İsim, Sıfat, Zamir, Edat-Bağlaç Bütüncül Tekrarı',
            'description': '6. sınıfın tüm morfolojik ve sözcük türü kazanımlarını kapsayan dil bilgisi genel sentezi yapar.',
            'process': ['a) Karma dil bilgisi sorularını çözer.', 'b) 7. sınıfın fiil konularına hazır bulunuşluğunu artırır.'],
            'concepts': ['Genel Sentez', 'Dil Bilgisi'], 'skills': ['Bütüncül Dil Bilgisi'],
            'pedagogical': 'Büyük dil bilgisi yarışması düzenlenir.', 'context': 'Yıl Sonu Zirvesi',
            'question': '6. sınıfta öğrenilen isim, sıfat ve zamir türleri 7. sınıfta hangi konunun temelini oluşturur?',
            'solution': 'Ek fiilin isim soylu sözcüklere gelerek yüklem yapması konusunun temelini oluşturur.', 'weeklyGoal': '6. sınıf dil bilgisi konularını eksiksiz pekiştirme.',
            'evaluation': 'Dil bilgisi yıl sonu başarı testi'
        },
        {
            'theme': 'Yıl Sonu Sentezi', 'subTheme': 'Okuma Kültürü ve Paragraf Hızı',
            'code': 'TÜR.6.6.2', 'title': 'Hızlı ve Anlayarak Okuma Teknikleri ile LGS Paragraf Köprüsü',
            'description': 'Dakikada okunan kelime sayısını artırma, göz sıçramalarıyla blok okuma teknikleri ve paragraf çözme taktiklerini geliştirir.',
            'process': ['a) Okuma hızını ölçer ve grafiklendirir.', 'b) Paragrafta anahtar kelime taktiğini uygular.'],
            'concepts': ['Hızlı Okuma', 'Blok Okuma', 'Paragraf Taktiği', 'LGS Köprüsü'],
            'skills': ['Okuma Hızı ve Verimi', 'Konsantrasyon'], 'pedagogical': 'Kronometreyle metin okuma ve anlama oranı ölçümü yapılır.',
            'context': 'LGS Hazırlık Temeli', 'question': 'Paragraf sorularını çözerken önce metin mi okunmalıdır yoksa soru kökü mü okunmalıdır?',
            'solution': 'Önce soru kökü ve varsa altı çizili ifade okunmalı, ardından metin ne arandığı bilinerek amaca yönelik okunmalıdır.', 'weeklyGoal': 'Okuma hızını ve kavrama oranını artırma.',
            'evaluation': 'Hızlı okuma ve anlama testi'
        },
        {
            'theme': 'Yıl Sonu Sentezi', 'subTheme': 'Yıl Sonu Başarı Değerlendirmesi',
            'code': 'TÜR.6.6.3', 'title': '6. Sınıf Türkçe Programı Kapanışı ve 7. Sınıfa Geçiş',
            'description': 'Yıl boyunca yapılan çalışmaların, okunan kitapların ve yazılan metinlerin portfolyo sergisi yapılır; başarı belgeleri takdim edilir.',
            'process': ['a) Portfolyo sunumunu gerçekleştirir.', 'b) 7. sınıf hedeflerini belirler.'],
            'concepts': ['Portfolyo', 'Yıl Sonu Değerlendirmesi', 'Kitap Listesi'],
            'skills': ['Sunum', 'Öz Değerlendirme'], 'pedagogical': 'Yıl sonu Türkçe başarı şenliği düzenlenir.',
            'context': '6. Sınıf Kapanış Şenliği', 'question': '7. sınıf Türkçe dersinin en önemli ve kapsamlı dil bilgisi konusunu ne oluşturacaktır?',
            'solution': 'Fiiller (eylemler), fiil kipleri, ek fiil ve zarflar konusunu oluşturacaktır.', 'weeklyGoal': '6. sınıf Türkçe eğitimini üstün başarıyla tamamlama.',
            'evaluation': '6. Sınıf Türkçe Başarı Karnesi'
        }
    ]
    return {
        'title': '6. Sınıf',
        'subtitle': 'Ortaokul 2. Kademe Türkçe Programı',
        'badge': 'Ortaokul Türkçe',
        'weeks': weeks
    }

print("Turkce 6 builder compiled.")
