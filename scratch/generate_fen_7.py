# -*- coding: utf-8 -*-
"""
Generates 36 weeks for Grade 7 and Grade 8 (LGS) Fen Bilimleri.
"""

def build_fen_7():
    # 7. Sınıf Fen Bilimleri MEB Müfredatı
    weeks = [
        # 1-5: Güneş Sistemi ve Ötesi
        {
            'theme': 'Güneş Sistemi ve Ötesi', 'subTheme': 'Uzay Araştırmaları ve Teknolojisi',
            'code': 'FEN.7.1.1', 'title': 'Uzay İstasyonları, Roketler, Yapay Uydular ve Uzay Kirliliği',
            'description': 'Uzay araştırmalarında kullanılan roket, uzay mekiği, sonda ve yapay uyduların görevlerini; ömrünü tamamlamış uyduların yarattığı uzay kirliliğini açıklar.',
            'process': ['a) Türksat uydularının haberleşme ve gözlemdeki önemini kavrar.', 'b) Uzay kirliliğinin gelecekteki uzay görevlerine tehdidini modeller.'],
            'concepts': ['Uzay İstasyonu', 'Yapay Uydu', 'Türksat', 'Uzay Kirliliği', 'Uzay Sondası'],
            'skills': ['Teknoloji Analizi', 'Çevre Değerlendirme'], 'pedagogical': 'Uzay teknolojisi sayesinde günlük hayatta kullandığımız ürünler (teflon, cırt cırt, dijital termometre) örneklenir.',
            'context': 'TÜRKSAT ve NASA', 'question': 'İşlevini yitirmiş eski yapay uyduların ve roket parçalarının Dünya yörüngesinde hızla dönmesi hangi tehlikeyi doğurur?',
            'solution': 'Uzay kirliliğine yol açarak çalışan uzay araçlarına ve istasyonlara çarpıp ağır hasar verme tehlikesi doğurur.', 'weeklyGoal': 'Uzay teknolojilerini ve uzay kirliliğini değerlendirme.',
            'evaluation': 'Uzay kirliliği çözüm önerisi raporu'
        },
        {
            'theme': 'Güneş Sistemi ve Ötesi', 'subTheme': 'Teleskobun Yapısı ve Gökbilimciler',
            'code': 'FEN.7.1.1', 'title': 'Teleskobun İcadı, Çeşitleri ve Işık Kirliliği',
            'description': 'Aynalı ve mercekli teleskopları; Ali Kuşçu, Galileo ve Uluğ Bey gibi gökbilimcileri; rasathanelerin şehir dışına kurulma nedenini (ışık kirliliği) inceler.',
            'process': ['a) James Webb ve Hubble uzay teleskoplarını inceler.', 'b) Işık kirliliğinin gökyüzü gözlemlerine olumsuz etkisini tartışır.'],
            'concepts': ['Teleskop', 'Aynalı / Mercekli', 'Rasathane (Gözlemevi)', 'Ali Kuşçu', 'Işık Kirliliği'],
            'skills': ['Tarihsel ve Bilimsel Çıkarım', 'Gözlemsel Farkındalık'], 'pedagogical': 'Şehir ışıkları altında ve köyde gökyüzü yıldız yoğunluğu fotoğrafı karşılaştırılır.',
            'context': 'Antalya Bakırlıtepe Gözlemevi', 'question': 'Astronomik gözlemevlerinin (rasathanelerin) şehir merkezlerine değil de yüksek ve ışıksız dağ zirvelerine kurulmasının temel sebebi nedir?',
            'solution': 'Şehirdeki ışık kirliliğinden, hava kirliliğinden ve bulutluluktan uzaklaşıp uzayı net gözlemleyebilmektir.', 'weeklyGoal': 'Teleskobun uzay araştırmalarındaki rolünü kavrama.',
            'evaluation': 'Gökbilimciler biyografi posteri'
        },
        {
            'theme': 'Güneş Sistemi ve Ötesi', 'subTheme': 'Yıldızlar ve Yıldız Yaşam Döngüsü',
            'code': 'FEN.7.1.2', 'title': 'Bulutsular (Nebula), Yıldızların Doğumu, Yaşamı ve Ölümü',
            'description': 'Yıldızların bulutsu (nebula) içinde gaz ve toz bulutunun sıkışmasıyla doğduğunu; küçük kütleli yıldızların beyaz cüceye, büyük kütleli yıldızların nötron yıldızı veya kara deliğe dönüştüğünü açıklar.',
            'process': ['a) Güneşin orta büyüklükte bir yıldız olduğunu kavrar.', 'b) Süpernova patlamasını modeller.'],
            'concepts': ['Bulutsu (Nebula)', 'Yıldız', 'Beyaz Cüce', 'Süpernova', 'Nötron Yıldızı', 'Kara Delik'],
            'skills': ['Döngüsel Evre Modelleme', 'Kozmik Kavrayış'], 'pedagogical': 'Yıldız yaşam ağacı infografiği incelenir.',
            'context': 'Astrofizik', 'question': 'Büyük kütleli bir yıldızın yakıtı bittiğinde geçirdiği şiddetli patlamaya ve geride bırakabileceği en gizemli kozmik yapıya ne ad verilir?',
            'solution': 'Süpernova patlaması denir; geride ışığı bile hapseden bir kara delik bırakabilir.', 'weeklyGoal': 'Yıldızların doğum ve ölüm süreçlerini şematize etme.',
            'evaluation': 'Yıldız yaşam döngüsü şeması'
        },
        {
            'theme': 'Güneş Sistemi ve Ötesi', 'subTheme': 'Takımyıldızları ve Galaksiler',
            'code': 'FEN.7.1.3', 'title': 'Takımyıldızları, Işık Yılı ve Galaksi (Gök Ada) Türleri',
            'description': 'Gökyüzündeki takımyıldızları (Büyükayı, Küçükayı, Avcı/Orion); ışık yılının bir zaman değil mesafe birimi olduğunu; Samanyolu ve Andromeda galaksilerini inceler.',
            'process': ['a) Kutup Yıldızının (Demirkazık) Küçükayı kuyruğunda olup yön bulmada kullanıldığını öğrenir.', 'b) Sarmal, eliptik ve düzensiz galaksi şekillerini sınıflandırır.'],
            'concepts': ['Takımyıldızı', 'Kutup Yıldızı', 'Işık Yılı', 'Samanyolu Galaksisi', 'Sarmal Galaksi'],
            'skills': ['Mekânsal Konumlandırma', 'Birim Dönüştürme'], 'pedagogical': 'Gökyüzü feneriyle sınıf tavanında takımyıldızları canlandırılır.',
            'context': 'Derin Uzay Keşifleri', 'question': "'Güneş bize 8 ışık dakikası, Proxima Centauri yıldızı ise 4,2 ışık yılı uzaklıktadır' cümlesindeki 'ışık yılı' kavramı ne anlama gelir?",
            'solution': 'Işığın boşlukta 1 yılda aldığı devasa mesafeyi (yaklaşık 9,5 trilyon kilometre) ifade eden bir uzaklık birimidir.', 'weeklyGoal': 'Galaksi türlerini ve evren ölçeğini kavrama.',
            'evaluation': 'Galaksiler ve takımyıldızları eşleştirme'
        },
        {
            'theme': 'Güneş Sistemi ve Ötesi', 'subTheme': 'Evren ve Uzay Kavramları',
            'code': 'FEN.7.1.3', 'title': 'Evrenin Genişlemesi ve Büyük Patlama (Big Bang) Teorisi',
            'description': 'Uzay ile evren kavramları arasındaki farkı (Evren = Uzay + Dünya); evrenin yaklaşık 13,8 milyar yıl önce tek bir noktadan genişlemeye başladığını (Big Bang) açıklar.',
            'process': ['a) Şişirilen balon üzerindeki noktaların birbirinden uzaklaşmasıyla evrenin genişlemesini modeller.', 'b) 1. üniteyi değerlendirir.'],
            'concepts': ['Evren', 'Uzay', 'Büyük Patlama (Big Bang)', 'Genişleyen Evren'],
            'skills': ['Bilimsel Teori Yorumlama', 'Model Analojisi'], 'pedagogical': 'Balon simülasyonuyla galaksilerin birbirine göre uzaklaşması gösterilir.',
            'context': 'Kozmoloji', 'question': 'İçinde Dünya\'nın da yer aldığı, bilinen ve bilinmeyen tüm maddeyi kapsayan sonsuz bütüne ne ad verilir?',
            'solution': 'Evren adı verilir (Dünya dışındaki kısma ise uzay denir).', 'weeklyGoal': 'Evren ve uzay kavramlarını ayırt etme.',
            'evaluation': '1. Ünite Değerlendirme Testi'
        },

        # 6-11: Hücre ve Bölünmeler
        {
            'theme': 'Hücre ve Bölünmeler', 'subTheme': 'Hücre ve Organeller',
            'code': 'FEN.7.2.1', 'title': 'Hücrenin Temel Kısımları ve Bitki-Hayvan Hücresi Organelleri',
            'description': 'Mitokondri, kloroplast, ribozom, koful, golgi, lizozom ve sentrozom organellerinin görevlerini açıklar; bitki ve hayvan hücresi farklarını modeller.',
            'process': ['a) Bitki hücresinde hücre duvarı ve kloroplast olduğunu, şeklinin köşeli olduğunu kavrar.', 'b) Hayvan hücresinin yuvarlak olduğunu ve sentrozom içerdiğini doğrular.'],
            'concepts': ['Hücre Zarı', 'Sitoplazma', 'Çekirdek', 'Mitokondri', 'Kloroplast', 'Hücre Duvarı'],
            'skills': ['Mikroskobik Modelleme', 'Analojik Düşünme'], 'pedagogical': 'Soğan zarı ve ağız içi epitel hücresi mikroskop preparatı incelenir.',
            'context': 'Sitoloji Laboratuvarı', 'question': 'Hücrede oksijenli solunum yaparak besinlerden enerji (ATP) üreten organel hangisidir?',
            'solution': 'Mitokondridir; hücrenin enerji santralidir.', 'weeklyGoal': 'Organellerin hücresel görevlerini eksiksiz açıklama.',
            'evaluation': 'Hücre organelleri eşleştirme formu'
        },
        {
            'theme': 'Hücre ve Bölünmeler', 'subTheme': 'Hücreden Canlıya ve DNA',
            'code': 'FEN.7.2.1', 'title': 'Kromozom, DNA ve Gen İlişkisi',
            'description': 'Hücre çekirdeğindeki genetik yapıyı (Kromozom > DNA > Gen > Nükleotid) karmaşıktan basite doğru sıralar ve canlılarda kromozom sayısının gelişmişlikle ilgisi olmadığını açıklar.',
            'process': ['a) İnsanda 46, moli balığında 46, eğrelti otunda 500 kromozom olduğunu inceler.', 'b) Kromozom sayısının aynı tür içinde sabit olduğunu fark eder.'],
            'concepts': ['Kromozom', 'DNA', 'Gen', 'Kromozom Sayısı Sabitliği'],
            'skills': ['Hiyerarşik Sıralama', 'Kavram Yanılgısı Giderme'], 'pedagogical': 'KediGENİ (K-D-G-N) kodlamasıyla hiyerarşi ezberletilir.',
            'context': 'Genetik Bilimi', 'question': 'Eğrelti otunun 500 kromozomu varken insanın 46 kromozomu olması eğrelti otunun insandan daha gelişmiş olduğunu gösterir mi?',
            'solution': 'Kesinlikle hayır; kromozom sayısı ile canlının gelişmişlik düzeyi veya vücut büyüklüğü arasında hiçbir ilişki yoktur.', 'weeklyGoal': 'Genetik yapıların büyüklük hiyerarşisini kavrama.',
            'evaluation': 'K-D-G-N hiyerarşi kartları'
        },
        {
            'theme': 'Hücre ve Bölünmeler', 'subTheme': 'Mitoz Bölünmenin Önemi',
            'code': 'FEN.7.2.2', 'title': 'Mitoz Bölünmenin Canlılar İçin Önemi (Büyüme, Gelişme, Onarım, Üreme)',
            'description': 'Mitoz bölünmenin tek hücrelilerde çoğalma (üreme); çok hücrelilerde ise büyüme, gelişme ve yaraların onarılmasını sağladığını açıklar.',
            'process': ['a) Vücut hücrelerinde (2n) gerçekleştiğini kavrar.', 'b) Mitoz bölünme sonucu kromozom sayısının ve genetik yapının değişmediğini açıklar.'],
            'concepts': ['Mitoz Bölünme', 'Vücut Hücresi (2n)', 'Büyüme', 'Onarım', 'Genetik Kopyalama'],
            'skills': ['Biyolojik Çıkarım', 'Hücresel Süreç İzleme'], 'pedagogical': 'Kırılan kemiğin kaynaması ve kesilen parmağın iyileşmesi mitoz ile açıklanır.',
            'context': 'Tıp ve Doku Yenilenmesi', 'question': 'Kertenkelenin kopan kuyruğunun yeniden uzaması hangi hücre bölünmesi çeşidiyle gerçekleşir ve kromozom sayısı değişir mi?',
            'solution': 'Mitoz bölünmeyle (rejenerasyon / onarım) gerçekleşir ve kuyruk hücrelerinin kromozom sayısı (2n) değişmez.', 'weeklyGoal': 'Mitoz bölünmenin canlılar için hayati rollerini açıklama.',
            'evaluation': 'Mitoz bölünme kavram haritası'
        },
        {
            'theme': 'Hücre ve Bölünmeler', 'subTheme': 'Mitoz Bölünmenin Evreleri',
            'code': 'FEN.7.2.2', 'title': 'Mitozun Birbirini Takip Eden Evreleri ve Sitoplazma Bölünmesi',
            'description': 'Hazırlık evresi (DNA eşlenmesi), çekirdek bölünmesi evreleri (kromozomların ekvatora dizilmesi, kardeş kromatitlerin zıt kutuplara çekilmesi) ve sitoplazma bölünmesini (boğumlanma / ara lamel) modeller.',
            'process': ['a) Hayvan hücresinde sitoplazmanın boğumlanarak bölündüğünü açıklar.', 'b) Bitki hücresinde sert hücre duvarı nedeniyle ara lamel oluştuğunu gösterir.'],
            'concepts': ['DNA Eşlenmesi', 'Kardeş Kromatit', 'Ekvatoral Düzlem', 'Boğumlanma', 'Ara Lamel'],
            'skills': ['Görsel Evre Sıralama', 'Mikroskobik Çizim'], 'pedagogical': 'Renkli ipler ve düğmelerle kromozomların zıt kutuplara çekilmesi canlandırılır.',
            'context': 'Hücre Laboratuvarı', 'question': 'Mitoz bölünme geçiren 2n=30 kromozomlu bir deri hücresinin art arda 3 kez bölünmesi sonucu kaç yeni hücre oluşur ve kromozom sayıları ne olur?',
            'solution': 'Oluşan hücre sayısı 2^3 = 8 hücredir ve her birinin kromozom sayısı yine 30\'dur.', 'weeklyGoal': 'Mitoz evrelerini ve matematiksel hücre artışını hesaplama.',
            'evaluation': 'Mitoz evreleri mikroskop kartları sıralama'
        },
        {
            'theme': 'Ara Tatil', 'subTheme': '1. Dönem Ara Tatili',
            'code': 'FEN.7.GENEL.1', 'title': 'Gökbilim ve Hücre Konuları Pekiştirme',
            'description': 'Uzay araştırmaları, hücre organelleri ve mitoz bölünme kazanımları beceri temelli sorularla tekrar edilir.',
            'process': ['a) Soru çözme hızını artırır.'],
            'concepts': ['Genel Tekrar', 'Analitik Düşünme'], 'skills': ['Problem Çözme'],
            'pedagogical': 'Tatil soru fasikülü uygulanır.', 'context': 'Tatil Kampı',
            'question': 'Bitki hücrelerinde sitoplazma bölünmesinin boğumlanarak değil de ara lamel ile gerçekleşmesinin nedeni nedir?',
            'solution': 'Bitki hücresinin dışındaki selüloz hücre duvarının sert ve esnek olmayan yapısıdır.',
            'weeklyGoal': 'İlk 9 haftayı kalıcılaştırma.', 'evaluation': 'Ara tatil değerlendirme testi'
        },
        {
            'theme': 'Hücre ve Bölünmeler', 'subTheme': 'Mayoz Bölünme ve Önemi',
            'code': 'FEN.7.2.3', 'title': 'Mayoz Bölünme, Parça Değişimi (Krossing-Over) ve Üreme Hücreleri',
            'description': 'Üreme ana hücrelerinde (2n) gerçekleşip kromozom sayısını yarıya (n) indiren mayoz bölünmeyi; parça değişimi sayesinde tür içi çeşitliliği (varyasyon) sağladığını açıklar.',
            'process': ['a) Mayoz sonucu 4 adet n kromozomlu üreme hücresi (sperm, yumurta, polen) oluştuğunu kavrar.', 'b) Parça değişimi ile anne ve babadan farklı gen kombinasyonları oluştuğunu modeller.'],
            'concepts': ['Mayoz Bölünme', 'Üreme Ana Hücresi (2n)', 'Üreme Hücresi / Gamet (n)', 'Parça Değişimi (Krossing-Over)', 'Çeşitlilik'],
            'skills': ['Genetik Çeşitliliği Açıklama', 'Model Karşılaştırma'], 'pedagogical': 'İki farklı renk oyun hamuruyla homolog kromozomların bacak değişimi somutlaştırılır.',
            'context': 'Genetik ve Aile Soy Ağacı', 'question': 'Kardeşlerin anne ve babaları aynı olmasına rağmen birbirlerinin tıpatıp kopyası olmamasının mayozdaki temel sebebi nedir?',
            'solution': 'Mayoz I evresinde homolog kromozomlar arasında gerçekleşen parça değişimi (krossing-over) ve homolog kromozomların rastgele ayrılmasıdır.', 'weeklyGoal': 'Mayoz bölünmenin çeşitlilik ve kromozom sabitliğindeki rolünü açıklama.',
            'evaluation': 'Mitoz-Mayoz karşılaştırma tablosu'
        },

        # 12-16: Kuvvet ve Enerji
        {
            'theme': 'Kuvvet ve Enerji', 'subTheme': 'Kütle ve Ağırlık İlişkisi',
            'code': 'FEN.7.3.1', 'title': 'Kütle ile Ağırlık Arasındaki Farklar ve Yer Çekimi Kuvveti',
            'description': 'Kütlenin madde miktarı olup dinamometreyle ölçülen ağırlığın ise cisme etki eden yer çekimi kuvveti olduğunu; Dünya ve Ay\'daki ağırlık farklarını hesaplar.',
            'process': ['a) Kütlenin her yerde aynı kaldığını, ağırlığın kutuplara gidildikçe arttığını açıklar.', 'b) Ağırlık = Kütle x Yer çekimi ivmesi (G = m x g) bağıntısını kavrar.'],
            'concepts': ['Kütle (kg/g)', 'Ağırlık (N)', 'Yer Çekimi İvmesi (g)', 'Eşit Kollu Terazi', 'Dinamometre'],
            'skills': ['Fiziksel Büyüklükleri Ayırt Etme', 'Hesaplama'], 'pedagogical': 'Dünyanın geoit şekli nedeniyle kutuplarda merkeze yakın olunduğu ve ağırlığın arttığı küre üzerinde gösterilir.',
            'context': 'Uzay Fiziği', 'question': 'Ekvatordan Kuzey Kutbu\'na doğru seyahat eden bir araştırmacının taşıdığı altın külçesinin kütlesi ve dinamometredeki ağırlığı nasıl değişir?',
            'solution': 'Kütlesi değişmez (sabit kalır). Kutuplarda yer çekimi kuvveti daha fazla olduğu için ağırlığı artar.', 'weeklyGoal': 'Kütle ve ağırlığı konum ve gök cismine göre karşılaştırma.',
            'evaluation': 'Kütle vs Ağırlık problem föyü'
        },
        {
            'theme': 'Kuvvet ve Enerji', 'subTheme': 'Fiziksel Anlamda İş',
            'code': 'FEN.7.3.2', 'title': 'Fiziksel Anlamda İş Kavramı ve Şartları (İş = Kuvvet x Yol)',
            'description': 'Bir kuvvetin fiziksel anlamda iş yapabilmesi için cismin kuvvet doğrultusunda hareket etmesi gerektiğini; İş = Kuvvet x Yol (W = F x x, Joule = N x m) formülüyle hesaplar.',
            'process': ['a) Sırtında çanta taşıyarak düz yolda yürüyen öğrencinin fiziksel anlamda yer çekimine karşı iş yapmadığını kanıtlar.', 'b) Merdiven çıkan veya kutuyu yukarı kaldıran kişinin iş yaptığını açıklar.'],
            'concepts': ['Fiziksel İş (W)', 'Kuvvet Doğrultusu', 'Alınan Yol', 'Joule (J)'],
            'skills': ['Bilimsel Tanım ile Günlük Dil Farkı', 'İş Analizi'], 'pedagogical': 'Duvardan masayı iten ama kıpırdatamayan öğrencinin fiziksel iş yapmadığı gösterilir.',
            'context': 'İnşaat ve Taşıma', 'question': 'Elindeki 20 N ağırlığındaki çantayı sallamadan düz ve yatay bir yolda 10 metre taşıyan bir kişi fen anlamında neden iş yapmamış sayılır?',
            'solution': 'Uygulanan kuvvet yukarı yönlü iken, hareket doğrultusu yataydır (kuvvet ile hareket doğrultusu birbirine diktir).', 'weeklyGoal': 'Fiziksel işin şartlarını belirleme ve hesaplama.',
            'evaluation': 'İş yapılır mı yapılmaz mı etkinlik kağıdı'
        },
        {
            'theme': 'Kuvvet ve Enerji', 'subTheme': 'Kinetik Enerji',
            'code': 'FEN.7.3.3', 'title': 'Kinetik Enerji ve Bağlı Olduğu Faktörler (Kütle ve Sürat)',
            'description': 'Hareket halindeki cisimlerin sahip olduğu kinetik enerjinin kütle arttıkça arttığını; sürat arttıkça süratin karesiyle doğru orantılı olarak çok daha fazla arttığını deneylerle doğrular.',
            'process': ['a) Aynı süratte giden kamyon ile otomobilin kinetik enerjisini kütleyle karşılaştırır.', 'b) Trafikte aşırı hızın fren mesafesine etkisini açıklar.'],
            'concepts': ['Kinetik Enerji', 'Kütle', 'Sürat', 'Trafik Fren Mesafesi'],
            'skills': ['Değişken İlişkilendirme', 'Grafik Analizi'], 'pedagogical': 'Kum havuzuna farklı hızlarla yuvarlanan misketlerin bıraktığı çukurlar ölçülür.',
            'context': 'Otomobil Çarpışma Testleri', 'question': 'Bir aracın sürati 2 katına çıktığında sahip olduğu kinetik enerji kaç katına çıkar?',
            'solution': 'Kinetik enerji süratin karesiyle orantılı olduğu için sürat 2 katına çıkarsa enerji 2^2 = 4 katına çıkar.', 'weeklyGoal': 'Kinetik enerjiyi kütle ve sürat değişkenleriyle analiz etme.',
            'evaluation': 'Kinetik enerji deney raporu'
        },
        {
            'theme': 'Kuvvet ve Enerji', 'subTheme': 'Potansiyel Enerji (Çekim ve Esneklik)',
            'code': 'FEN.7.3.3', 'title': 'Çekim Potansiyel Enerjisi ve Esneklik Potansiyel Enerjisi',
            'description': 'Cismin konumundan (yükseklik ve kütle) dolayı sahip olduğu çekim potansiyel enerjisini ve sıkıştırılmış/gerilmiş yay veya okta depolanan esneklik potansiyel enerjisini inceler.',
            'process': ['a) Barajlardaki suyun yüksekte biriktirilmesinin çekim potansiyel enerjisi sağladığını kavrar.', 'b) Gerilen yayın esneklik enerjisini oka aktardığını açıklar.'],
            'concepts': ['Çekim Potansiyel Enerjisi', 'Yükseklik (h)', 'Ağırlık', 'Esneklik Potansiyel Enerjisi', 'Sıkıştırılmış Yay'],
            'skills': ['Enerji Depolama Mekanizmaları', 'Deney Tasarımı'], 'pedagogical': 'Farklı yüksekliklerden un tepsisine bırakılan eşit kütleli bilyelerin çukur derinliği kıyaslanır.',
            'context': 'Okçuluk ve Hidroelektrik Barajlar', 'question': 'Kütleleri eşit iki saksıdan biri 2. katta, diğeri 5. katta bulunmaktadır. Hangisinin çekim potansiyel enerjisi daha büyüktür ve neden?',
            'solution': '5. kattaki saksının enerjisi daha büyüktür çünkü çekim potansiyel enerjisi kütleyle ve yükseklikle doğru orantılıdır.', 'weeklyGoal': 'Potansiyel enerji türlerini ve değişkenlerini kavrama.',
            'evaluation': 'Potansiyel enerji hesaplama föyü'
        },
        {
            'theme': 'Kuvvet ve Enerji', 'subTheme': 'Enerji Dönüşümleri ve Sürtünme',
            'code': 'FEN.7.3.4', 'title': 'Mekanik Enerjinin Korunumu ve Sürtünmenin Isıya Dönüşmesi',
            'description': 'Kinetik ve potansiyel enerjinin birbirine dönüşebileceğini (roller coaster, sarkaç); sürtünme kuvveti nedeniyle mekanik enerjinin bir kısmının ısı ve ses enerjisine dönüştüğünü açıklar.',
            'process': ['a) Havada serbest düşen cisimde potansiyel enerjinin kinetiğe dönüştüğünü modeller.', 'b) Toplam enerjinin daima korunduğunu (yoktan var, vardan yok edilemeyeceğini) kavrar.'],
            'concepts': ['Enerji Korunumu', 'Mekanik Enerji', 'Potansiyel-Kinetik Dönüşümü', 'Sürtünme ve Isı'],
            'skills': ['Dönüşüm Modelleme', 'Enerji Muhasebesi'], 'pedagogical': 'Sarkaç deneyi yapılarak sarkacın bırakıldığı yüksekliği asla aşamayacağı gösterilir.',
            'context': 'Hız Treni (Roller Coaster)', 'question': 'Bir hız treni en yüksek tepeden aşağıya doğru inerken potansiyel ve kinetik enerjisi nasıl değişir?',
            'solution': 'Yüksekliği azaldığı için çekim potansiyel enerjisi azalır, hızı arttığı için kinetik enerjisi artar (potansiyel enerji kinetiğe dönüşür).', 'weeklyGoal': 'Enerji korunumu ve dönüşüm şemalarını yorumlama.',
            'evaluation': 'Hız treni enerji dönüşüm grafiği ödevi'
        },

        # 17-23: Saf Madde ve Karışımlar
        {
            'theme': 'Saf Madde ve Karışımlar', 'subTheme': 'Atomun Yapısı ve Tarihsel Gelişimi',
            'code': 'FEN.7.4.1', 'title': 'Atomun Temel Parçacıkları (Proton, Nötron, Elektron) ve Atom Modelleri',
            'description': 'Çekirdekte pozitif yüklü proton ve yüksüz nötronun; katmanlarda ise hızlı dönen negatif yüklü elektronun bulunduğunu; Dalton, Thomson, Rutherford, Bohr ve Modern Atom Teorisini modeller.',
            'process': ['a) Thomson\'ın üzümlü kek modelini inceler.', 'b) Rutherford\'un altın levha deneyiyle çekirdeği keşfettiğini kavrar.'],
            'concepts': ['Atom', 'Çekirdek', 'Proton (+)', 'Nötron (0)', 'Elektron (-)', 'Atom Modelleri'],
            'skills': ['Tarihsel Bilim Gelişimi', 'Mikro Parçacık Modelleme'], 'pedagogical': 'Dalton (içi dolu berk küre), Thomson (üzümlü kek), Rutherford (güneş sistemi) analojileriyle poster yapılır.',
            'context': 'Nükleer Fizik ve Kimya', 'question': 'Atomun kütlesinin neredeyse tamamının toplandığı pozitif yüklü merkez bölgeye ne ad verilir ve hangi parçacıkları içerir?',
            'solution': 'Çekirdek adı verilir; içinde protonlar ve nötronlar bulunur.', 'weeklyGoal': 'Atomun yapısını ve modellerini tarihsel sırasıyla açıklama.',
            'evaluation': 'Atom modelleri zaman şeridi'
        },
        {
            'theme': 'Saf Madde ve Karışımlar', 'subTheme': 'Moleküller (Element ve Bileşik)',
            'code': 'FEN.7.4.2', 'title': 'Aynı ve Farklı Cins Atomlardan Oluşan Moleküller',
            'description': 'Atomların kimyasal bağlarla birleşerek molekülleri oluşturduğunu; aynı cins atomlardan oluşan moleküllere element molekülü (O2, H2), farklı cinsten oluşanlara bileşik molekülü (H2O, CO2) dendiğini modeller.',
            'process': ['a) Plastik küre ve çubuklarla molekül maketleri yapar.', 'b) Moleküler ve moleküler olmayan katı yapıları ayırt eder.'],
            'concepts': ['Molekül', 'Element Molekülü', 'Bileşik Molekülü', 'Kimyasal Bağ'],
            'skills': ['Molekül Modelleme', 'Yapısal Sınıflandırma'], 'pedagogical': 'Renkli oyun hamurlarıyla su (H2O) ve oksijen gazı (O2) molekülleri yapılır.',
            'context': 'Moleküler Biyoloji ve Kimya', 'question': 'O3 (Ozon) ve NH3 (Amonyak) taneciklerinden hangisi element molekülü, hangisi bileşik molekülüdür?',
            'solution': 'O3 aynı cins oksijen atomlarından oluştuğu için element molekülü; NH3 ise azot ve hidrojenden oluştuğu için bileşik molekülüdür.', 'weeklyGoal': 'Molekül çeşitlerini atom türlerine göre ayırt etme.',
            'evaluation': 'Molekül modelleri çizim föyü'
        },
        {
            'theme': 'Saf Madde ve Karışımlar', 'subTheme': 'Elementler ve Sembolleri',
            'code': 'FEN.7.4.3', 'title': 'İlk 18 Element ve Yaygın Elementlerin Sembolleri ve Kullanım Alanları',
            'description': 'İlk 18 elementin (H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar) ve yaygın elementlerin (Fe, Cu, Au, Ag, Pb, Zn) sembollerini ve günlük hayattaki yerini kavrar.',
            'process': ['a) Element sembollerinin tüm dünyada ortak bir bilim dili sağladığını belirtir.', 'b) Sembollerin Latinceden geldiğini fark eder.'],
            'concepts': ['Element', 'Kimyasal Sembol', 'İlk 18 Element', 'Altın (Au)', 'Demir (Fe)', 'Bakır (Cu)'],
            'skills': ['Sembolik Dil Kullanma', 'Hafıza ve Eşleştirme'], 'pedagogical': 'Element tombalası ve periyodik sistem hafıza kartları oyunu oynatılır.',
            'context': 'Endüstriyel Hammaddeler', 'question': 'Sembolü \'Na\' olan ve sofra tuzunun yapısında yer alan elementin adı ile sembolü \'Fe\' olan inşaat ve sanayinin temel elementi hangisidir?',
            'solution': 'Na: Sodyum, Fe: Demirdir.', 'weeklyGoal': 'İlk 18 elementin ve yaygın metallerin sembollerini hatasız yazma.',
            'evaluation': 'Element sembolleri bilgi yarışması'
        },
        {
            'theme': 'Saf Madde ve Karışımlar', 'subTheme': 'Bileşikler ve Formülleri',
            'code': 'FEN.7.4.3', 'title': 'Yaygın Bileşiklerin Formülleri ve Özellikleri',
            'description': 'Su (H2O), Karbondioksit (CO2), Sofra Tuzu (NaCl), Amonyak (NH3), Tuz Ruhu (HCl), Zaç Yağı (H2SO4) gibi bileşiklerin formüllerini ve kendi kendini oluşturan elementlerin özelliklerini kaybettiğini açıklar.',
            'process': ['a) Yanıcı hidrojen ile yakıcı oksijenin birleşerek söndürücü suyu oluşturmasını kimyasal özellik kaybıyla açıklar.', 'b) Bileşiklerin belirli oranlarda birleştiğini kavrar.'],
            'concepts': ['Bileşik', 'Kimyasal Formül', 'H2O', 'NaCl', 'CO2', 'Özellik Kaybı'],
            'skills': ['Formül Çözümleme', 'Kimyasal Kimlik'], 'pedagogical': 'Demir ve kükürdün karışımı mıknatısla ayrılırken, ısıtılıp demir sülfür bileşiği yapıldığında mıknatısın çekmediği gösterilir.',
            'context': 'Kimya Sanayisi', 'question': 'Sofra tuzu (NaCl) zehirli klor gazı ile patlayıcı sodyum metalinin birleşmesiyle oluşur. Sofra tuzunu güvenle yiyebilmemizin fen açıklaması nedir?',
            'solution': 'Elementler kimyasal bağla birleşip bileşik oluştururken kendi kimyasal özelliklerini tamamen kaybederler ve yeni özellik kazanırlar.', 'weeklyGoal': 'Bileşiklerin kimyasal doğasını ve formüllerini öğrenme.',
            'evaluation': 'Bileşik formül ve adlandırma tablosu'
        },
        {
            'theme': 'Saf Madde ve Karışımlar', 'subTheme': 'Homojen ve Heterojen Karışımlar',
            'code': 'FEN.7.4.4', 'title': 'Karışımların Özellikleri: Çözeltiler (Homojen) ve Heterojen Karışımlar',
            'description': 'Maddelerin kimyasal özelliklerini kaybetmeden rastgele oranlarda birleşmesiyle oluşan karışımları; tek bir madde gibi görünen homojen (çözelti: hava, gazoz, tuzlu su, bronz) ve heterojen (salata, ayran, çorba) olarak sınıflandırır.',
            'process': ['a) Karışımların sembolü veya formülü olmadığını öğrenir.', 'b) Çözücü ve çözünen kavramlarını tanımlar.'],
            'concepts': ['Karışım', 'Homojen Karışım (Çözelti)', 'Heterojen Karışım', 'Çözücü', 'Çözünen', 'Alaşım'],
            'skills': ['Madde Sınıflandırma', 'Karşılaştırma'], 'pedagogical': 'Tuzlu su (çözelti) ile tebeşir tozu-su (heterojen) ışık geçirgenliğiyle karşılaştırılır.',
            'context': 'Gıda ve İçecek Kimyası', 'question': 'Hava bir element midir, bileşik midir yoksa karışım mıdır? Karışımsa homojen midir heterojen midir?',
            'solution': 'Hava azot, oksijen ve diğer gazlardan oluşan homojen bir karışımdır (gaz çözeltisidir).', 'weeklyGoal': 'Homojen ve heterojen karışımları doğru ayırt etme.',
            'evaluation': 'Karışım türleri sınıflandırma tablosu'
        },
        {
            'theme': 'Saf Madde ve Karışımlar', 'subTheme': 'Çözünme Hızını Etkileyen Faktörler',
            'code': 'FEN.7.4.4', 'title': 'Sıcaklık, Karıştırma ve Temas Yüzeyinin Çözünme Hızına Etkisi',
            'description': 'Bir katının sıvıda çözünme hızını artırmak için sıcaklığın artırılması, çözeltinin karıştırılması ve katının ufalanarak temas yüzeyinin artırılması (pudra şekeri > toz şeker > küp şeker) gerektiğini deneylerle keşfeder.',
            'process': ['a) Bağımlı, bağımsız ve kontrol değişkenlerini belirleyerek deney kurar.', 'b) Çözünürlük ile çözünme hızı farkını ayırt eder.'],
            'concepts': ['Çözünme Hızı', 'Sıcaklık', 'Karıştırma', 'Temas Yüzeyi', 'Kontrollü Deney'],
            'skills': ['Bilimsel Değişken Denetimi', 'Süreç Ölçümü'], 'pedagogical': 'Sıcak ve soğuk çayda küp şeker eritilip kronometreyle çözünme süreleri kaydedilir.',
            'context': 'İlaç Sanayisi (Efervesan Tabletler)', 'question': 'Küp şekerin sıcak çayda soğuk çaya göre ve toz haline getirildiğinde tane haline göre çok daha çabuk çözünmesinin gerekçesi nedir?',
            'solution': 'Yüksek sıcaklık tanecik hareketini hızlandırır; toz haline getirmek ise temas yüzeyini artırarak çözücü taneciklerinin maddeye daha hızlı çarpmasını sağlar.', 'weeklyGoal': 'Çözünme hızını etkileyen değişkenleri kontrollü deneyle test etme.',
            'evaluation': 'Çözünme hızı laboratuvar deney föyü'
        },
        {
            'theme': 'Saf Madde ve Karışımlar', 'subTheme': 'Karışımları Ayırma Yöntemleri',
            'code': 'FEN.7.4.5', 'title': 'Buharlaştırma, Damıtma, Yoğunluk Farkı ve Mıknatısla Ayırma',
            'description': 'Katı-sıvı homojen karışımları buharlaştırmayla (tuzlu su); sıvı-sıvı homojenleri kaynama noktası farkıyla (ayrımsal damıtma: alkol-su, petrol); yoğunluk farkıyla (ayırma hunisi: zeytinyağı-su, yüzdürme: saman-buğday) ayırmayı modeller.',
            'process': ['a) Rafinerilerde ham petrolün ayrımsal damıtmayla benzin, motorin, gaza ayrıldığını kavrar.', 'b) Demir tozu-kum karışımını mıknatısla ayırır.'],
            'concepts': ['Buharlaştırma', 'Ayrımsal Damıtma', 'Kaynama Noktası Farkı', 'Ayırma Hunisi', 'Mıknatısla Ayırma'],
            'skills': ['Ayırma Stratejisi Geliştirme', 'Fiziksel Özelliklerden Yararlanma'], 'pedagogical': 'Kolonyadan alkolün damıtma düzeneğiyle ayrılması sınıfta gösterilir.',
            'context': 'Petrol Rafinerileri ve Geri Dönüşüm', 'question': 'Birbiri içinde homojen karışmış olan etil alkol (kaynama noktası 78 °C) ile su (100 °C) karışımı en etkili hangi yöntemle ayrılır?',
            'solution': 'Kaynama noktası farkından yararlanan \'ayrımsal damıtma\' yöntemiyle ayrılır; önce alkol buharlaşıp yoğuşarak ayrılır.', 'weeklyGoal': 'Karışımları bileşenlerin fiziksel özelliklerine göre uygun yöntemle ayırma.',
            'evaluation': 'Karışım ayırma planı hazırlama görevi'
        },

        # 24-29: Işığın Madde ile Etkileşimi
        {
            'theme': 'Işığın Madde ile Etkileşimi', 'subTheme': 'Işığın Soğurulması ve Renkler',
            'code': 'FEN.7.5.1', 'title': 'Işığın Soğurulması, Beyaz Işığın Renklerine Ayrılması ve Cisimlerin Renkli Görünmesi',
            'description': 'Koyu renkli yüzeylerin ışığı daha çok soğurup (absorbe edip) ısındığını; beyaz ışığın prizmada kırmızı, turuncu, sarı, yeşil, mavi, mora (KUTUSAMAM) ayrıldığını ve cisimlerin yansıttığı renkte göründüğünü açıklar.',
            'process': ['a) Kışın koyu, yazın açık renkli kıyafet tercih edilmesini soğurmayla açıklar.', 'b) Kırmızı elmanın üzerine beyaz ışık düştüğünde kırmızıyı yansıtıp diğerlerini soğurduğunu kavrar.'],
            'concepts': ['Işığın Soğurulması', 'Işık Spektrumu', 'Prizma', 'Renklerin Ayrılması', 'Yansıma'],
            'skills': ['Optik Renk Analizi', 'Enerji Emilimi'], 'pedagogical': 'Newton çarkı döndürülerek tüm renklerin birleştiğinde beyaz algılandığı gösterilir.',
            'context': 'Güneş Enerjisi Panelleri', 'question': 'Yeşil bir yaprağın üzerine beyaz güneş ışığı düştüğünde yaprağın gözümüze yeşil görünmesinin optik sebebi nedir?',
            'solution': 'Yaprak beyaz ışıktaki kırmızı, mavi gibi diğer renkleri soğurur; yalnızca yeşil dalga boyunu yansıtarak gözümüze ulaştırır.', 'weeklyGoal': 'Işığın soğurulmasını ve renklerin oluşumunu kavrama.',
            'evaluation': 'Newton renk çarkı yapımı'
        },
        {
            'theme': 'Işığın Madde ile Etkileşimi', 'subTheme': 'Düzlem Aynalar',
            'code': 'FEN.7.5.2', 'title': 'Düzlem Aynada Görüntü Özellikleri ve Simetri',
            'description': 'Düzlem aynada görüntünün düz, cisimle aynı boyda, aynaya olan uzaklığının cismin uzaklığına eşit ve sanal (zahiri/simetrik: sağ-sol ters) olduğunu açıklar.',
            'process': ['a) Ambulans yazısının önden bakan araç sürücüsünün aynasında düz okunması için ters yazıldığını analiz eder.', 'b) Periskop ve tepegözde düzlem ayna kullanımını gösterir.'],
            'concepts': ['Düzlem Ayna', 'Düz Görüntü', 'Eşit Boy', 'Simetri', 'Zahiri (Sanal) Görüntü'],
            'skills': ['Simetri Çizimi', 'Ayna Geometrisi'], 'pedagogical': 'Kareli kâğıda yazılan kelimelerin ayna karşısındaki simetrisi çizdirilir.',
            'context': 'Trafik ve Ambulans Tasarımları', 'question': 'Düzlem aynaya 3 metre mesafede duran bir kişinin aynadaki görüntüsü ile arasındaki toplam mesafe kaç metredir?',
            'solution': 'Cismin aynaya uzaklığı 3 m ise görüntünün de aynaya uzaklığı 3 m\'dir; kişi ile görüntüsü arasındaki mesafe 3 + 3 = 6 metredir.', 'weeklyGoal': 'Düzlem aynada görüntü özelliklerini kuralına göre belirleme.',
            'evaluation': 'Ayna simetrisi çizim çalışması'
        },
        {
            'theme': 'Işığın Madde ile Etkileşimi', 'subTheme': 'Küresel Aynalar (Çukur ve Tümsek Ayna)',
            'code': 'FEN.7.5.2', 'title': 'Çukur ve Tümsek Aynaların Odak Noktası ve Kullanım Alanları',
            'description': 'Çukur aynanın ışığı odak noktasında topladığını (dişçi aynası, makyaj aynası, teleskop, güneş fırını; dev aynası gibi düz-büyük görüntü); tümsek aynanın ışığı dağıttığını ve geniş görüş açısı sağladığını (araç yan aynası, kavşak aynası) modeller.',
            'process': ['a) Yemek kaşığının iç yüzünün çukur ayna, dış yüzünün tümsek ayna gibi davrandığını gözlemler.', 'b) Tümsek aynada görüntünün daima düz ve küçük olduğunu kavrar.'],
            'concepts': ['Çukur Ayna', 'Tümsek Ayna', 'Odak Noktası (F)', 'Geniş Görüş Açısı', 'Işığı Toplama / Dağıtma'],
            'skills': ['Optik Araç Tasarımı', 'Fonksiyonel Eşleştirme'], 'pedagogical': 'Metal parlak kaşıkla öğrencilerin kendi ters ve düz görüntüleri incelenir.',
            'context': 'Otomotiv ve Tıp Cihazları', 'question': 'Otopark çıkışlarında ve keskin virajlarda sürücülerin kör noktaları ve geniş bir alanı görebilmesi için neden tümsek ayna tercih edilir?',
            'solution': 'Tümsek aynalar cisimlerin daima düz ve küçük görüntüsünü oluşturarak çok geniş bir görüş alanını tek aynaya sığdırır.', 'weeklyGoal': 'Çukur ve tümsek aynaların görüntü ve kullanım alanlarını karşılaştırma.',
            'evaluation': 'Küresel ayna kullanım alanları tablosu'
        },
        {
            'theme': 'Işığın Madde ile Etkileşimi', 'subTheme': 'Işığın Kırılması ve Kırılma Kanunları',
            'code': 'FEN.7.5.3', 'title': 'Işığın Saydam Ortamlardan Geçerken Doğrultu Değiştirmesi (Kırılma)',
            'description': 'Işığın bir saydam ortamdan başka bir saydam ortama geçerken süratinin değişmesi sonucu doğrultu değiştirmesine kırılma dendiğini; az yoğun ortamdan çok yoğuna geçerken normale yaklaşarak kırıldığını keşfeder.',
            'process': ['a) Su dolu bardaktaki kalemin kırılmış gibi görünmesini kırılmayla açıklar.', 'b) Çok yoğundan az yoğuna geçerken normalden uzaklaşarak kırıldığını ve süratinin arttığını kavrar.'],
            'concepts': ['Işığın Kırılması', 'Geliş Açısı', 'Kırılma Açısı', 'Yüzey Normali (N)', 'Ortam Yoğunluğu'],
            'skills': ['Işın Çizimi', 'Optik Kanun Uygulama'], 'pedagogical': 'Lazer ışığıyla su dolu akvaryumda kırılma açısı gösterilir.',
            'context': 'Denizcilik ve Balık Avı', 'question': 'Havadan suya doğru bakan bir balıkçının suyun içindeki balığı olduğundan daha yakın ve yukarıda görmesinin gerekçesi nedir?',
            'solution': 'Balıktan çıkan ışınlar sudan (çok yoğun) havaya (az yoğun) geçerken normalden uzaklaşarak kırılır; göz ışınların uzantısını daha yukarıda algılar.', 'weeklyGoal': 'Işığın kırılma davranışını yoğunluk farkıyla açıklama.',
            'evaluation': 'Kırılma ışın diyagramı çizim föyü'
        },
        {
            'theme': 'Ara Tatil', 'subTheme': '2. Dönem Ara Tatili',
            'code': 'FEN.7.GENEL.2', 'title': 'Saf Madde, Karışımlar ve Optik Soru Kampı',
            'description': 'Atom, element-bileşikler, karışımları ayırma ve ayna-kırılma optik soruları çözülür.',
            'process': ['a) Beceri temelli LGS hazırlık sorularını irdeler.'],
            'concepts': ['Genel Tekrar', 'Analiz'], 'skills': ['Problem Çözme'],
            'pedagogical': 'Tatil fasikülü uygulanır.', 'context': 'Tatil Föyü',
            'question': 'Işığın boşluktaki sürati yaklaşık 300.000 km/s olduğuna göre suda mı yoksa camda mı daha yavaş ilerler? (Camın yoğunluğu sudan büyüktür)',
            'solution': 'Yoğunluğu daha büyük olan camda daha yavaş ilerler (yoğunluk arttıkça ışığın ortamdaki yayılma sürati azalır).',
            'weeklyGoal': 'Kimya ve optik kazanımlarını pekiştirme.', 'evaluation': 'Ara tatil deneme sınavı'
        },
        {
            'theme': 'Işığın Madde ile Etkileşimi', 'subTheme': 'Mercekler ve Kullanım Alanları',
            'code': 'FEN.7.5.4', 'title': 'İnce Kenarlı (Yakınsak) ve Kalın Kenarlı (Iraksak) Mercekler',
            'description': 'Kenarları ortasına göre ince olan ince kenarlı merceğin ışığı odak noktasında topladığını (büyüteç, mikroskop, hipermetrop gözlüğü); kalın kenarlı merceğin ışığı dağıttığını (miyop gözlüğü, dürbün) modeller.',
            'process': ['a) İnce kenarlı merceğin orman yangınlarına yol açma riskini (şişe kırıkları) tartışır.', 'b) Odak uzaklığı kavramını açıklar.'],
            'concepts': ['İnce Kenarlı Mercek', 'Kalın Kenarlı Mercek', 'Büyüteç', 'Odak Noktası', 'Orman Yangını Riski'],
            'skills': ['Optik Teçhizat Modelleme', 'Çevre Korumacılığı'], 'pedagogical': 'Büyüteçle güneş ışığı toplanarak kâğıt yakma deneyiyle odak noktası gösterilir.',
            'context': 'Optisyenlik ve Doğa Koruma', 'question': 'Piknikçilerin ormanda bıraktığı kırık cam şişelerin güneşli havalarda orman yangını başlatabilmesinin merceklerle ilişkisi nedir?',
            'solution': 'Kırık cam parçaları ince kenarlı mercek gibi davranarak güneş ışınlarını tek bir odak noktasında toplar ve kuru otları tutuşturacak yüksek sıcaklık üretir.', 'weeklyGoal': 'Mercek çeşitlerini ışık davranışı ve kullanım yerleriyle ilişkilendirme.',
            'evaluation': 'Mercek modelleri ve yangın farkındalık afişi'
        },

        # 30-33: Canlılarda Üreme, Büyüme ve Gelişme
        {
            'theme': 'Canlılarda Üreme, Büyüme ve Gelişme', 'subTheme': 'İnsanda Üreme Sistemi ve Döllenme',
            'code': 'FEN.7.6.1', 'title': 'Sperm, Yumurta, Döllenme, Zigot, Embriyo ve Fetüs Aşamaları',
            'description': 'Erkek ve dişi üreme organlarını; sperm ile yumurtanın döllenme borusunda birleşmesiyle (döllenme) zigot, mitoz bölünmelerle embriyo, fetüs ve bebeğin gelişim basamaklarını şematize eder.',
            'process': ['a) Mayozla oluşan üreme hücrelerinin döllenmeyle tekrar 2n kromozomlu zigotu oluşturduğunu kavrar.', 'b) Plasentanın anne ile bebek arasındaki besin-oksijen köprüsü olduğunu açıklar.'],
            'concepts': ['Sperm', 'Yumurta', 'Döllenme', 'Zigot', 'Embriyo', 'Fetüs', 'Bebek'],
            'skills': ['Gelişim Basamakları Sıralama', 'Embriyolojik Süreç Takibi'], 'pedagogical': 'Zigottan bebeğe gelişim aşamaları zaman şeridi üzerinde gösterilir.',
            'context': 'Kadın Doğum ve Embriyoloji', 'question': 'Sperm ve yumurtanın döllenmesi anne vücudunun hangi organ/bölümünde gerçekleşir?',
            'solution': 'Yumurta kanalında (döllenme borusunda) gerçekleşir; ardından döl yatağına (rahme) yerleşir.', 'weeklyGoal': 'İnsanda üreme ve embriyonik gelişim basamaklarını öğrenme.',
            'evaluation': 'Gelişim basamakları sıralama tablosu'
        },
        {
            'theme': 'Canlılarda Üreme, Büyüme ve Gelişme', 'subTheme': 'Anne Adayının Dikkat Etmesi Gerekenler',
            'code': 'FEN.7.6.1', 'title': 'Embriyo Sağlığını Koruma ve Gebelik Dönemi Hijyeni',
            'description': 'Hamilelik süresince sigara, alkol, uyuşturucu, gereksiz ilaç kullanımı ve radyasyonun (röntgen) embriyonun organ gelişimine verdiği zararları analiz eder.',
            'process': ['a) Yetersiz ve dengesiz beslenmenin anomalilere yol açacağını kavrar.', 'b) Anne ve bebek sağlığı bilinci geliştirir.'],
            'concepts': ['Embriyo Sağlığı', 'Hamilelik', 'Zararlı Alışkanlıklar', 'Radyasyon', 'Dengeli Beslenme'],
            'skills': ['Bilinçli Davranış Geliştirme', 'Sağlık İletişimi'], 'pedagogical': 'Kamu spotları incelenerek sağlıklı nesiller için gebelik bilinci oluşturulur.',
            'context': 'Halk Sağlığı', 'question': 'Hamile kadınların röntgen (X-ray) filmi çektirmelerinin kesinlikle yasak olmasının fen açıklaması nedir?',
            'solution': 'Radyasyonun hızla bölünen embriyo hücrelerinin DNA\'sında mutasyona yol açarak kalıcı sakatlıklara sebep olma riskidir.', 'weeklyGoal': 'Embriyo gelişimini tehdit eden risk faktörlerini açıklama.',
            'evaluation': 'Hamilelikte sağlık rehberi broşürü'
        },
        {
            'theme': 'Canlılarda Üreme, Büyüme ve Gelişme', 'subTheme': 'Hayvanlarda Üreme ve Başkalaşım (Metamorfoz)',
            'code': 'FEN.7.6.2', 'title': 'Eşeyli/Eşeysiz Üreme, İç/Dış Döllenme ve Kurbağa/Kelebek Başkalaşımı',
            'description': 'Memeliler, kuşlar, sürüngenler, balıklar ve kurbağalarda yavru bakımı, döllenme şekillerini; yumurtadan çıkan larvanın gelişerek ana canlıya benzemesi sürecini (başkalaşım) modeller.',
            'process': ['a) Kuş ve memelilerde yavru bakımı varken balık ve sürüngenlerde olmadığını belirtir.', 'b) İpek böceği ve kurbağanın metamorfoz basamaklarını çizer.'],
            'concepts': ['Yavru Bakımı', 'Başkalaşım (Metamorfoz)', 'Larva', 'Pupa', 'Kelebek / Kurbağa'],
            'skills': ['Yaşam Döngüsü Çizme', 'Canlılar Arası Karşılaştırma'], 'pedagogical': 'Kurbağanın yumurta -> iribaş -> genç kurbağa -> ergin kurbağa döngüsü canlandırılır.',
            'context': 'Zooloji ve Doğa Belgeseli', 'question': 'Kelebek ve kurbağaların yumurtadan ilk çıktıklarında ana canlıya hiç benzemeyip sonradan yapısal değişim geçirmelerine ne ad verilir?',
            'solution': 'Başkalaşım (metamorfoz) adı verilir.', 'weeklyGoal': 'Hayvanların üreme ve başkalaşım süreçlerini sınıflandırma.',
            'evaluation': 'Başkalaşım yaşam döngüsü şeması'
        },
        {
            'theme': 'Canlılarda Üreme, Büyüme ve Gelişme', 'subTheme': 'Bitkilerde Üreme ve Çimlenme',
            'code': 'FEN.7.6.3', 'title': 'Çiçeğin Kısımları, Tozlaşma, Tohum, Meyve ve Çimlenme Şartları',
            'description': 'Çiçeğin kısımlarını (taç yaprak, çanak yaprak, erkek organ, dişi organ); arı ve rüzgârla tozlaşmayı; çimlenme için gereken şartları (S-O-S: Su, Oksijen, Sıcaklık) deneylerle açıklar.',
            'process': ['a) Çimlenme için ışığa ihtiyaç olmadığını, fotosentez başladığında ışık gerektiğini kavrar.', 'b) Tohumun uyku halinden çıkışını inceler.'],
            'concepts': ['Çiçek', 'Erkek/Dişi Organ', 'Tozlaşma', 'Çimlenme', 'Su-Oksijen-Sıcaklık (SOS)'],
            'skills': ['Botanik Deneyi', 'Çimlenme Gözlemi'], 'pedagogical': 'Islak pamukta fasulye çimlendirme deneyi yapılarak ışıklı ve karanlık dolap testi kurulur.',
            'context': 'Tarım ve Botanik', 'question': 'Tohumun çimlenebilmesi için temel olarak hangi üç faktör (SOS formülü) şarttır ve bu sırada ışık gerekli midir?',
            'solution': 'Su (nem), Oksijen ve uygun Sıcaklık şarttır. Çimlenme sırasında tohum fotosentez yapmadığı için ışık şart değildir.', 'weeklyGoal': 'Çiçeğin yapısını ve tohum çimlenme koşullarını belirleme.',
            'evaluation': 'Fasulye çimlendirme gözlem günlüğü'
        },

        # 34-36: Elektrik Devreleri
        {
            'theme': 'Elektrik Devreleri', 'subTheme': 'Seri ve Paralel Bağlama',
            'code': 'FEN.7.7.1', 'title': 'Ampullerin Seri ve Paralel Bağlanması ve Parlaklık Farkları',
            'description': 'Ampullerin uç uca tek bir kol üzerinde bağlanmasına seri bağlama; kollara ayrılarak bağlanmasına paralel bağlama dendiğini; seri bağlılarda ampul sayısı arttıkça parlaklığın azaldığını, paralel bağlılarda değişmediğini modeller.',
            'process': ['a) Seri bağlı ampullerden biri patlarsa veya sökülürse diğerlerinin de söndüğünü kavrar.', 'b) Paralel bağlı ampullerden biri sönerse diğerlerinin aynı parlaklıkta yanmaya devam ettiğini keşfeder.'],
            'concepts': ['Seri Bağlama', 'Paralel Bağlama', 'Ampul Parlaklığı', 'Devre Akımı', 'Eşdeğer Direnç'],
            'skills': ['Devre Mimarisi Tasarımı', 'Karşılaştırmalı Deney'], 'pedagogical': 'Evlerimizdeki tüm priz ve lambaların paralel bağlı olduğu canlandırılır.',
            'context': 'Ev Elektrik Tesisatı', 'question': 'Evlerdeki lambaların ve elektronik aletlerin seri değil de mutlaka paralel bağlanmasının iki büyük avantajı nedir?',
            'solution': '1) Bir lamba kapatıldığında diğerleri yanmaya devam eder. 2) Her alet şehir şebekesinin tam gerilimini (220 V) alarak maksimum verimle çalışır.', 'weeklyGoal': 'Seri ve paralel bağlama farklarını ve sonuçlarını modelleme.',
            'evaluation': 'Seri-Paralel devre laboratuvar föyü'
        },
        {
            'theme': 'Elektrik Devreleri', 'subTheme': 'Akım, Gerilim ve Direnç İlişkisi (Ohm Kanunu)',
            'code': 'FEN.7.7.2', 'title': 'Ampermetre, Voltmetre Kullanımı ve Ohm Kanunu (V = I x R)',
            'description': 'Devreden geçen akım şiddetini ölçen ampermetrenin seri; gerilimi (potansiyel farkı) ölçen voltmetrenin paralel bağlandığını; Gerilim / Akım oranının sabit olup iletkenin direncini verdiğini (Ohm Kanunu) hesaplar.',
            'process': ['a) Gerilim arttıkça akımın da doğru orantılı arttığını grafik üzerinde gösterir.', 'b) Birimlerini (Volt, Amper, Ohm Ω) kullanır.'],
            'concepts': ['Akım Şiddeti (I / Amper)', 'Gerilim / Potansiyel Fark (V / Volt)', 'Direnç (R / Ohm)', 'Ampermetre', 'Voltmetre', 'Ohm Kanunu'],
            'skills': ['Ölçüm Aleti Bağlama', 'Grafik Eğimi Hesaplama'], 'pedagogical': 'V = I x R (VUR) formül üçgeniyle matematiksel problemler çözülür.',
            'context': 'Elektrik Laboratuvarı', 'question': 'Bir devrede iletkenin uçları arasındaki gerilim 30 Volt iken üzerinden 5 Amper akım geçiyorsa bu iletkenin elektriksel direnci kaç Ohm\'dur?',
            'solution': 'Ohm Kanunu R = V / I = 30 V / 5 A = 6 Ohm (Ω) dur.', 'weeklyGoal': 'Ohm Kanunu ile akım, gerilim ve direnç hesaplamalarını yapabilme.',
            'evaluation': 'Ohm Kanunu problem çözme föyü'
        },
        {
            'theme': 'Elektrik Devreleri', 'subTheme': 'Yıl Sonu Sentezi ve LGS\'ye Hazırlık',
            'code': 'FEN.7.7.3', 'title': '7. Sınıf Fen Bilimleri Yıl Sonu Sentezi ve 8. Sınıf LGS Köprüsü',
            'description': 'Gökbilim, mitoz-mayoz, iş-enerji, atom-saf madde, optik aynalar, üreme ve elektrik devreleri ünitelerinin genel kazanım analizi yapılır; 8. sınıf LGS konularına köprü kurulur.',
            'process': ['a) Öğrenme eksikliklerini giderir.', 'b) 8. sınıf LGS Fen Bilimleri hazırlık çalışma planı oluşturur.'],
            'concepts': ['Genel Değerlendirme', 'Portfolyo', 'LGS Hazırlık Köprüsü'],
            'skills': ['Öz Değerlendirme', 'Bütüncül Fen Bakışı'], 'pedagogical': 'Yıl sonu fen sergisi ve bilim şenliği ödül töreni.',
            'context': '7. Sınıf Kapanış Şenliği', 'question': '7. sınıfta öğrenilen hücre bölünmeleri ve atom konuları 8. sınıfta hangi LGS ünitelerinin temel omurgasını oluşturur?',
            'solution': 'DNA ve Genetik Kod ünitesi ile Madde ve Endüstri (Periyodik Sistem ve Kimyasal Tepkimeler) ünitelerinin temelini oluşturur.', 'weeklyGoal': '7. sınıf fen bilimleri programını başarıyla tamamlama.',
            'evaluation': '7. Sınıf Yıl Sonu Fen Bilimleri Başarı Karnesi'
        }
    ]
    return {
        'title': '7. Sınıf',
        'subtitle': 'Ortaokul 3. Kademe Fen Programı',
        'badge': 'Ortaokul Fen',
        'weeks': weeks
    }

print("Fen 7 builder compiled.")
