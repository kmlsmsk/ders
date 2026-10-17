# -*- coding: utf-8 -*-
"""
Comprehensive 36-week generator for Din Kültürü ve Ahlak Bilgisi (Grades 5 Maarif, 6, 7, 8 LGS).
Generates lib/data/subjects/din_kulturu_data.dart with full details.
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
                f"a) {desc[:40]} kavrar ve açıklar.",
                f"b) {sub} ilkesini günlük hayatındaki tutum ve davranışlarına yansıtır.",
                "c) Konuyla ilgili ayet, hadis ve örnek olayları analiz eder."
            ],
            'concepts': conc,
            'skills': ['Değerler Eğitimi', 'Ahlaki Muhakeme', 'Eleştirel Düşünme', 'Kültürel Farkındalık'],
            'pedagogical': ped,
            'context': 'Din Kültürü ve Ahlak Bilgisi',
            'question': q,
            'solution': a,
            'weeklyGoal': f"{title} konusunu ve ahlaki değerini içselleştirme",
            'evaluation': 'Haftalık kazanım kavrama ve değer değerlendirme föyü'
        })
    return weeks

def get_din_5():
    # 5. Sınıf - Türkiye Yüzyılı Maarif Modeli (5 Ünite - Tam 36 Hafta)
    u = [
        # Ünite 1: Allah İnancı (1-7)
        ("Allah İnancı", "Evrendeki Mükemmel Düzen", "Evrendeki Düzen ve Yaratılış Gayesi",
         "Gök cisimleri, mevsimler ve canlılar arasındaki kusursuz nizamı inceleyerek yaratıcının varlığını kavrar.",
         ["Nizam", "Ahenk", "Yaratılış", "Tevhid"],
         "Öğrencilerin evrendeki ekolojik ve astronomik ahenge dikkatleri çekilir.",
         "Evrendeki mükemmel ahenk ve ölçü bize neyi gösterir?",
         "Her şeyin bir tesadüf eseri değil, sonsuz ilim ve kudret sahibi Allah tarafından yaratıldığını gösterir."),
        
        ("Allah İnancı", "Allah Vardır ve Birdir", "Tevhid İnancı ve Allah'ın Birliği",
         "İslam inancının temeli olan tevhid (Allah'ın tek, eşi ve benzeri olmadığı) inancını açıklar.",
         ["Tevhid", "İhlas", "Vahdaniyet", "İnanç"],
         "Şirk ve tevhid kavramları karşılaştırmalı olarak açıklanır.",
         "Tevhid inancı ne anlama gelir?",
         "Allah'ın zatında, sıfatlarında ve fiillerinde bir ve tek olması, ortağının bulunmamasıdır."),
        
        ("Allah İnancı", "Allah Yaradandır ve Yaşatandır", "Hâlık ve Rezzak İsimleri",
         "Evrendeki tüm canlıların rızkını verenin ve var edenin Allah olduğunu kavrar.",
         ["Hâlık", "Rezzak", "Şükür", "Nimet"],
         "Nimetlerin şükür bilinciyle korunması gerektiği vurgulanır.",
         "Rezzak ismi insana ne tür bir sorumluluk yükler?",
         "Verilen rızkı israf etmeden, helal yoldan kazanmayı ve ihtiyaç sahipleriyle paylaşmayı gerektirir."),
        
        ("Allah İnancı", "Allah Her Şeyi İşitir ve Görür", "Semi ve Basar Sıfatları",
         "Gizli ve açık her şeyi bilen, gören Allah'ın huzurunda olduğu bilinciyle hareket eder.",
         ["Semi", "Basar", "İlim", "Öz Denetim"],
         "İhsan kavramı (Allah'ı görüyormuş gibi yaşamak) üzerinden oto-kontrol kazandırılır.",
         "Allah'ın Basar ve Semi sıfatları insanda hangi ahlaki davranışı geliştirir?",
         "Kimsenin görmediği yerde dahi yalan söylememe, kul hakkı yememe ve dürüst davranma bilinci kazandırır."),
        
        ("Allah İnancı", "Allah'ın Güzel İsimleri", "Esma-i Hüsna: Rahman, Rahim ve Vedûd",
         "Esma-i Hüsna'dan örnek isimlerin anlamlarını ve hayata yansımalarını öğrenir.",
         ["Esma-i Hüsna", "Rahman", "Rahim", "Vedûd"],
         "Sevgi, şefkat ve merhamet değerleri örnek ayetlerle ilişkilendirilir.",
         "Vedûd isminin anlamına uygun bir insan nasıl davranmalıdır?",
         "Tüm yaratılanları Yaradan'dan ötürü sever, kin ve nefret yerine dostluk ve barışı yayar."),
        
        ("Allah İnancı", "Dua ve İbadet", "Allah ile İletişim: Dua ve İltica",
         "Duanın bir kulun Rabbiyle en samimi bağı olduğunu ve her zaman dua edilebileceğini kavrar.",
         ["Dua", "Şükür", "Tevazu", "Umut"],
         "Peygamberlerin dualarından kesitler okunur.",
         "Dua etmek insanın ruh sağlığına nasıl katkı sağlar?",
         "Yalnızlık duygusunu giderir, iç huzuru artırır ve insana sığınacak güvenli bir liman sunar."),
        
        ("Allah İnancı", "Bir Sure Öğreniyorum", "İhlas Suresi ve Anlamı",
         "İhlas suresinin okunuşunu, tecvidini ve tevhid inancını özetleyen anlamını öğrenir.",
         ["İhlas", "Samed", "Tevhid", "Sure"],
         "Sure ezberlenir ve anlamı üzerinde durulur.",
         "İhlas suresindeki 'Samed' kavramı ne demektir?",
         "Herkesin ve her şeyin O'na muhtaç olduğu, O'nun ise hiçbir şeye muhtaç olmadığı anlamına gelir."),

        # Ünite 2: Namaz (8-14)
        ("Namaz", "Allah'ın Huzurunda Olmak", "Namaz İbadetinin Anlamı ve Önemi",
         "Namazın dinin direği olduğunu, kötülüklerden alıkoyduğunu ve günde beş vakit huzur verdiğini açıklar.",
         ["Namaz", "Salat", "Huzur", "Kulluk"],
         "Namazın zamanı planlama ve disiplin kazandırma yönü ele alınır.",
         "Kur'an'da namazın insan ahlakı üzerindeki hangi etkisine dikkat çekilir?",
         "Namazın insanı her türlü hayasızlıktan, fenalıktan ve kötülükten alıkoyduğu belirtilir."),
        
        ("Namaz", "Namaza Hazırlık Şartları", "Abdest ve Namazın Dışındaki Şartlar",
         "Abdestin farzlarını, hadesten/necasetten taharet, setr-i avret, istikbal-i kıble ve vakit şartlarını uygular.",
         ["Abdest", "Taharet", "Kıble", "Vakit"],
         "Abdestin hem beden hem ruh temizliği sağladığı vurgulanır.",
         "Abdestin farzları nelerdir?",
         "Yüzü yıkamak, elleri dirseklerle beraber yıkamak, başın dörtte birini meshetmek ve ayakları topuklarla yıkamaktır."),
        
        ("Ara Tatil", "1. Dönem Ara Tatil Tekrarı", "İnanç ve İbadet Değerlendirme Kampı",
         "1. dönem ara tatilinde Allah inancı ve namaz hazırlık kazanımlarını pekiştirir.",
         ["Tekrar", "Pekiştirme", "Ölçme", "Ahlak"],
         "Boşluk doldurma ve ahlaki olay analizi çalışmaları yapılır.",
         "Namazın insana kazandırdığı en önemli alışkanlık nedir?",
         "Maddi ve manevi temizlik ile zaman yönetimi bilincidir."),
        
        ("Namaz", "Namazın Kılınış Şartları (Rükunlar)", "İftitah Tekbiri, Kıyam, Kıraat, Rükû, Secde",
         "Namazın içindeki farzları ve hareketlerin anlamlarını uygulamalı öğrenir.",
         ["Kıyam", "Rükû", "Secde", "Kade-i Ahire"],
         "Secdenin kulu Allah'a en yakın kılan an olduğu bilinci aşılanır.",
         "Namazda secde neyi sembolize eder?",
         "Kulun acziyetini kabul edip sonsuz kudret sahibi Allah karşısında en derin tevazuunu sunmasını sembolize eder."),
        
        ("Namaz", "Cemaatle Namaz ve Dayanışma", "Cuma, Bayram ve Teravih Namazları",
         "Birlikte yapılan ibadetlerin toplumsal kaynaşma, eşitlik ve dayanışmaya katkısını çözümler.",
         ["Cemaat", "Cuma", "Bayram", "Uhuvvet"],
         "Cami safında zengin-fakir ayrımının kalktığı vurgulanır.",
         "Cemaatle namaz kılmanın toplumsal yararı nedir?",
         "İnsanlar arasındaki sınıf ve statü farklarını siler, kardeşlik, tanışma ve dayanışma duygusunu perçinler."),
        
        ("Namaz", "Günde Beş Vakit Çağrı: Ezan", "Ezan ve Kametin Anlamı ve Sözleri",
         "Ezanın İslam dininin evrensel bağımsızlık ve tevhid çağrısı olduğunu kavrar.",
         ["Ezan", "Kamet", "Müezzin", "Hürriyet"],
         "İstiklal Marşımızdaki ezan vurgusu ile ilişkilendirilir.",
         "Ezanın günde beş vakit okunmasının Müslüman topluma mesajı nedir?",
         "Huzura ve kurtuluşa (felaha) çağrıdır, tevhid inancını sürekli hatırlatır."),
        
        ("Namaz", "Bir Dua Öğreniyorum", "Tahiyyat Duası ve Anlamı",
         "Namazın oturuşlarında okunan Tahiyyat duasının okunuşunu ve miraç bağlamındaki manasını öğrenir.",
         ["Tahiyyat", "Miraç", "Selam", "Dua"],
         "Peygamberimiz ile Yüce Allah arasındaki miraç diyaloğu incelenir.",
         "Tahiyyat duasında yer alan 'Esselamü aleyna ve ala ibadillahis-salihin' cümlesi ne anlama gelir?",
         "'Selam bizim üzerimize ve Allah'ın salih kullarının üzerine olsun' anlamına gelir."),

        # Ünite 3: Kur'an-ı Kerim (15-21)
        ("Kur'an-ı Kerim", "Son İlahi Kitap Kur'an", "Kur'an-ı Kerim'in İndirilişi ve Vahiy",
         "Hira Mağarası'nda Kadir Gecesi'nde başlayan vahiy sürecini ve peygambere peyderpey gelişini öğrenir.",
         ["Vahiy", "Cebrail", "Hira", "Kadir Gecesi"],
         "İlk inen ayetlerin 'Oku!' emriyle başlamasının ilme verdiği önem işlenir.",
         "Kur'an'ın bir kerede değil de 23 yılda parça parça indirilmesinin hikmeti nedir?",
         "İnsanların ayetleri anlayarak, hazmederek ve hayatlarına aşama aşama uygulayabilmeleri içindir."),
        
        ("Kur'an-ı Kerim", "Kur'an'ın İç Tertibi", "Ayet, Sure ve Cüz Kavramları",
         "Kur'an'ın 6666 ayet, 114 sure ve 30 cüzden oluşan iç nizamını kavrar.",
         ["Ayet", "Sure", "Cüz", "Mushaf"],
         "Kur'an'ın mushaf haline getirilmesi ve çoğaltılması süreci anlatılır.",
         "Kur'an-ı Kerim'in ilk ve son sureleri hangileridir?",
         "İlk suresi Fatiha, son suresi ise Nas suresidir."),
        
        ("Kur'an-ı Kerim", "Kur'an'ın Temel Konuları", "İnanç, İbadet, Ahlak ve Kıssalar",
         "Kur'an'ın insanlara yol gösteren temel muhtevasını ve ahlaki ilkelerini sınıflandırır.",
         ["Muhteva", "Ahlak", "Kıssa", "Muamelat"],
         "Kur'an'daki öğüt ve adalet prensipleri incelenir.",
         "Kur'an kıssalarının temel anlatılış gayesi nedir?",
         "Geçmiş milletlerin tecrübelerinden ibret almak, iyi davranışları örnek alıp kötülüklerden sakınmaktır."),
        
        ("Kur'an-ı Kerim", "1. Dönem Değerlendirmesi", "1. Dönem Sonu Bilgi ve Değer Ölçümü",
         "İnanç, namaz ve Kur'an ünitelerini kapsayan 1. dönem kazanımlarını pekiştirir.",
         ["Sentez", "Kazanım", "Değerlendirme", "Tekrar"],
         "Ayet mealleri üzerinden mini deneme ve proje sunumları yapılır.",
         "Kur'an-ı Kerim'i hayat rehberi edinmek ne demektir?",
         "Onu sadece okumakla kalmayıp emrettiği adalet, dürüstlük ve merhamet ilkelerini yaşam tarzı haline getirmektir."),
        
        ("Kur'an-ı Kerim", "1. Dönem Karne ve Tatil Planı", "Yarıyıl Tatili Ahlak ve Maneviyat Planı",
         "1. dönemin ahlaki ve akademik değerlendirmesini yapar, tatil için kitap okuma listesi oluşturur.",
         ["Portfolyo", "Öz Değerlendirme", "Karne", "Gelişim"],
         "Öğrencilerin manevi gelişimleri takdir edilir.",
         "İslam dininde ilim öğrenmenin yeri nedir?",
         "Kadın-erkek her Müslümana farz kılınmış, ibadet derecesinde değerli bir erdemdir."),
        
        ("Kur'an-ı Kerim", "Kur'an Okuma ve Anlama Adabı", "Kur'an'ı Anlayarak Yaşamak",
         "Kur'an okurken saygı, tertil ve tefekkür etmenin önemini açıklar.",
         ["Tertil", "Tefekkür", "Hürmet", "Meal"],
         "Ayetlerin mealleriyle birlikte okunmasının önemi vurgulanır.",
         "Tertil üzere Kur'an okumak ne anlama gelir?",
         "Ayetleri acele etmeden, dura dura, harflerin hakkını vererek ve manasını düşünerek okumaktır."),
        
        ("Kur'an-ı Kerim", "Bir Sure Öğreniyorum", "Kevser Suresi ve Anlamı",
         "Kevser suresinin nüzul sebebini, anlamını ve tükenmeyen ilahi nimetlere şükrü kavrar.",
         ["Kevser", "Şükür", "Kurban", "Teselli"],
         "Peygamberimize zor zamanında gelen ilahi teselli üzerinde durulur.",
         "Kevser suresinde peygamberimize ve inananlara verilen müjde nedir?",
         "Tükenmeyen hayır ve bereket (kevser) verildiği, soyunun ve davasının kıyamete kadar süreceğidir."),

        # Ünite 4: Peygamber Kıssaları (22-29)
        ("Peygamber Kıssaları", "Peygamberlik Kurumu", "Peygamberlerin Gönderiliş Gayesi",
         "Peygamberlerin insanlara doğru yolu göstermek için seçilmiş elçiler olduğunu kavrar.",
         ["Nübüvvet", "Risalet", "Elçi", "Hidayet"],
         "Peygamberlerin insanlardan seçilmesinin hikmeti işlenir.",
         "Peygamberler neden meleklerden değil de insanlardan seçilmiştir?",
         "İnsanlara her alanda (ibadet, aile, ahlak, sabır) yaşayarak somut bir rol model olabilmeleri içindir."),
        
        ("Peygamber Kıssaları", "Hz. İbrahim'in Arayışı", "Hz. İbrahim ve Tevhid Mücadelesi",
         "Hz. İbrahim'in aklını kullanarak gök cisimlerinden yaratıcıya ulaşma serüvenini analiz eder.",
         ["Hz. İbrahim", "Akil", "Fıtrat", "Tevhid"],
         "Batan şeylerin ilah olamayacağı akli çıkarımı incelenir.",
         "Hz. İbrahim gök cisimlerini gözlemlerken hangi sonuca ulaşmıştır?",
         "Batan, kaybolan ve değişen varlıkların yaratıcı olamayacağını; her şeyi yaratan tek bir sonsuz kudret olduğunu kavramıştır."),
        
        ("Peygamber Kıssaları", "Kâbe'nin İnşası ve Teslimiyet", "Hz. İbrahim ve Hz. İsmail",
         "Hz. İbrahim ile Hz. İsmail'in Kâbe'yi inşa edişini ve teslimiyet erdemini öğrenir.",
         ["Kâbe", "Hz. İsmail", "Teslimiyet", "Vefa"],
         "Kâbe'nin tevhidin yeryüzündeki ilk merkezi olduğu anlatılır.",
         "Hz. İbrahim ve Hz. İsmail Kâbe'yi yaparken nasıl dua etmişlerdir?",
         "Rabbimizden bu ameli kabul buyurmasını ve soylarından Müslüman bir ümmet çıkarmasını niyaz etmişlerdir."),
        
        ("Peygamber Kıssaları", "Peygamberlerin Erdemleri", "Sıdk ve Emanet Sıfatları",
         "Peygamberlerin asla yalan söylemeyen (sıdk) ve son derece güvenilir (emanet) vasıflarını modeller.",
         ["Sıdk", "Emanet", "Güven", "Doğruluk"],
         "Peygamber Efendimizin 'Muhammedü'l-Emin' lakabı hatırlatılır.",
         "Bir Müslümanın iş ve sözlerinde güvenilir olması neden farz derecesinde önemlidir?",
         "Güven duygusu toplumun temelidir; emanete hıyanet etmek İslam ahlakıyla asla bağdaşmaz."),
        
        ("Peygamber Kıssaları", "Zorluklara Karşı Metanet", "Hz. Eyyüb'ün Sabrı ve Şükrü",
         "Hz. Eyyüb'ün ağır hastalıklar ve kayıplar karşısındaki sabır ve tevekkülünü inceler.",
         ["Hz. Eyyüb", "Sabır", "Tevekkül", "Metanet"],
         "Şikayet etmeden Allah'a sığınmanın ve şifa aramanın önemi açıklanır.",
         "Hz. Eyyüb'ün sabrı bize günlük hayatımızdaki sıkıntılarda nasıl bir ufuk açar?",
         "Zorlukların geçici bir imtihan olduğunu, sabredip gayret gösterenlerin mutlaka feraha ulaşacağını öğretir."),
        
        ("Peygamber Kıssaları", "Merhamet ve Affedicilik", "Peygamberlerin Bağışlayıcı Ahlakı",
         "İntikam yerine af ve hoşgörüyü tercih eden peygamber tavrını kavrar.",
         ["Affedicilik", "Merhamet", "Sulh", "Hoşgörü"],
         "Mekke'nin fethinde sergilenen af örneği işlenir.",
         "Güçlüyken affedebilmek insan karakterine ne kazandırır?",
         "Kin ve intikam duygusunu yok eder, kalpleri birbirine ısındırır ve en büyük asalet göstergesidir."),
        
        ("Ara Tatil", "2. Dönem Ara Tatil Tekrarı", "Peygamber Kıssaları Kampı",
         "2. dönem ara tatilinde peygamberlerin ahlaki vasıfları ve dualarını pekiştirir.",
         ["Ara Tatil", "Kamp", "Ahlak", "Ölçme"],
         "Örnek soru analizleri ve değerler bulmacası çözülür.",
         "Peygamberlerin ortak mesajı nedir?",
         "Yalnızca tek bir Allah'a kulluk etmek, adaleti ayakta tutmak ve ahlaklı yaşamaktır."),
        
        ("Peygamber Kıssaları", "Bir Dua Öğreniyorum", "Rabbena Duaları ve Manası",
         "Rabbena Âtina ve Rabbenağfirli dualarının okunuşunu ve dünya-ahiret dengesini öğrenir.",
         ["Rabbena", "Mağfiret", "Dua", "Denge"],
         "Namazların son oturuşunda okunan duaların derin anlamı kavranır.",
         "Rabbena Âtina duasındaki denge bize neyi öğretir?",
         "İnsanın sadece dünyayı veya sadece ahireti değil, her iki dünyada da iyilik ve esenlik istemesi gerektiğini öğretir."),

        # Ünite 5: Mimarimizde Dinî Motifler (30-36)
        ("Mimarimizde Dinî Motifler", "Dinin Sanata Yansıması", "İslam Mimarisi ve Estetik Anlayış",
         "Tevhid inancının cami, medrese, köprü ve kervansaray gibi yapılara yansıyan estetiğini inceler.",
         ["Mimari", "Estetik", "Medeniyet", "Sanat"],
         "Sadelik ve zarafetin İslam sanatındaki yeri görsel materyallerle gösterilir.",
         "İslam mimarisinin merkezinde yer alan ana yapı nedir?",
         "Şehrin kalbini oluşturan, cemaati bir araya toplayan cami ve külliyelerdir."),
        
        ("Mimarimizde Dinî Motifler", "Camiyi Tanıyalım (Dış Unsurlar)", "Kubbe, Minare, Şerefe ve Şadırvan",
         "Cami mimarisinin dış bölümlerini ve fonksiyonlarını tanır.",
         ["Kubbe", "Minare", "Şadırvan", "Alem"],
         "Şadırvanın temizlik, minarenin tevhid sancağı simgesi olduğu aktarılır.",
         "Cami minareleri ve kubbeleri mimari olarak neyi simgeler?",
         "Kubbe gök kubbeyi ve birliği; göğe yükselen minareler ise tevhid inancını ve ilahi huzuru simgeler."),
        
        ("Mimarimizde Dinî Motifler", "Camiyi Tanıyalım (İç Unsurlar)", "Mihrap, Minber, Kürsü ve Mahfil",
         "Caminin iç kısımlarındaki ibadet ve tebliğ mekanlarını yerinde/görsellerle inceler.",
         ["Mihrap", "Minber", "Kürsü", "Hüsn-i Hat"],
         "İmam ve vaizin görev yerleri uygulamalı anlatılır.",
         "Cami içindeki Mihrap ve Minber hangi amaçlarla kullanılır?",
         "Mihrap imamın namaz kıldırdığı kıble yönündeki girinti; minber ise cuma ve bayram hutbelerinin okunduğu basamaklı yerdir."),
        
        ("Mimarimizde Dinî Motifler", "Şaheser Camilerimiz", "Süleymaniye, Selimiye ve Sultanahmet",
         "Mimar Sinan'ın eserleri başta olmak üzere ecdadımızın mimari dehasını takdir eder.",
         ["Mimar Sinan", "Süleymaniye", "Selimiye", "Külliye"],
         "Mimar Sinan'ın kalfalık ve ustalık eserleri incelenir.",
         "Mimar Sinan Selimiye Camii ile dünya mimarlık tarihine nasıl damga vurmuştur?",
         "Tek bir kubbe ile devasa bir mekanı örterek iç ferahlığı ve akustiği zirveye taşımıştır."),
        
        ("Mimarimizde Dinî Motifler", "Mimaride Merhamet: Kuş Evleri", "Tarihî Yapılardaki Kuş Köşkleri ve Vakıf Medeniyeti",
         "Cami, medrese ve han duvarlarına yapılan zarif kuş evleri üzerinden merhamet medeniyetini keşfeder.",
         ["Kuş Evleri", "Merhamet", "Vakıf Medeniyeti", "Ekoloji"],
         "Hayvanlara verilen değer ve çevre bilinci işlenir.",
         "Tarihi binalara kuş evi yapılmasının ardındaki medeniyet şuuru nedir?",
         "Yaratılan her canlının yaşam hakkına saygı duymak ve dilsiz canlılara merhamet gösterme zarafetidir."),
        
        ("Mimarimizde Dinî Motifler", "Musiki ve Edebiyatta Dinî Motifler", "İlahiler, Naatlar ve Mevlid Geleneği",
         "Ezan, sala, ilahi ve edebiyatımızdaki peygamber sevgisinin kültürel tezahürlerini değerlendirir.",
         ["Musiki", "İlahi", "Mevlid", "Naat"],
         "Yunus Emre ve Süleyman Çelebi'den beyitler okunur.",
         "Kültürümüzde kandil gecelerinde okunan Mevlid-i Şerif kime olan sevginin ifadesidir?",
         "Alemlere rahmet olarak gönderilen Peygamber Efendimiz Hz. Muhammed'e (s.a.v.) olan derin sevginin ifadesidir."),
        
        ("Mimarimizde Dinî Motifler", "Maarif Modeli Yıl Sonu Sentezi", "5. Sınıf Din Kültürü Portfolyo Sergisi",
         "Yıl boyunca edinilen inanç, ibadet, ahlak ve medeniyet değerlerini bütünleştirerek sunar.",
         ["Portfolyo", "Maarif Modeli", "Değerler", "Mezuniyet"],
         "Bütünsel değerlendirme ve proje sergisi gerçekleştirilir.",
         "Din Kültürü ve Ahlak Bilgisi dersinin temel amacı nedir?",
         "Aklını kullanan, vicdanlı, erdemli, milli ve manevi değerlerine bağlı güzel ahlaklı fertler yetiştirmektir.")
    ]
    assert len(u) == 36, f"Din 5 count: {len(u)}"
    return {
        'title': '5. Sınıf',
        'subtitle': 'Türkiye Yüzyılı Maarif Modeli (5 Ünite)',
        'badge': 'Maarif Modeli ✨',
        'weeks': _make_weeks(u, 'DİN.5')
    }

def get_din_6():
    # 6. Sınıf MEB Müfredatı (5 Ünite - Tam 36 Hafta)
    u = [
        # Ünite 1: Peygamber ve İlahi Kitap İnancı (1-8)
        ("Peygamber ve İlahi Kitap İnancı", "Peygamberlere İman", "Allah'ın Elçileri ve Tebliğ",
         "Peygamberlik kurumunun anlamını ve vahyin insanlık tarihindeki rehberliğini açıklar.",
         ["Peygamber", "Vahiy", "Nübüvvet", "İman"],
         "Peygamberlere inanmanın imanın şartlarından biri olduğu vurgulanır.",
         "Peygamberlerin insanlara tebliğ ettiği en temel ortak esas nedir?",
         "Yalnızca Allah'a ibadet etmek ve kötülüklerden sakınmaktır."),
        
        ("Peygamber ve İlahi Kitap İnancı", "Peygamberlerin Nitelikleri", "Sıdk, Emanet, Fetanet, İsmet, Tebliğ",
         "Peygamberlerin taşıdığı üstün ahlaki ve zihni sıfatları analiz eder.",
         ["Sıfatlar", "Fetanet", "İsmet", "Doğruluk"],
         "Peygamberlerin zeki, güvenilir ve günahtan korunmuş şahsiyetleri ele alınır.",
         "Peygamberlerin 'fetanet' sıfatı ne anlama gelir?",
         "Üstün akıl, kavrayış ve basiret sahibi olmaları anlamına gelir."),
        
        ("Peygamber ve İlahi Kitap İnancı", "Peygamberler İnsanlara Müjdecidir", "Tebşir ve İnzar Görevi",
         "Peygamberlerin iyileri müjdeleyen (tebşir), kötü sonuçlara karşı uyaran (inzar) vasfını kavrar.",
         ["Tebşir", "İnzar", "Rehber", "Adalet"],
         "İlahi adaletin bir gereği olarak peygamber gönderildiği anlatılır.",
         "Peygamberlerin uyarıcı olması insanlar için neden bir rahmettir?",
         "Yanlış yoldan dönüp doğru yolu bulmalarına fırsat tanıdığı için rahmettir."),
        
        ("Peygamber ve İlahi Kitap İnancı", "İlahi Kitaplar ve Sahifeler", "Dört Büyük Kitap ve Sahifeler",
         "Tevrat, Zebur, İncil, Kur'an ve sahife verilen peygamberleri öğrenir.",
         ["Tevrat", "Zebur", "İncil", "Kur'an"],
         "İlahi kitapların asıllarının tevhid esasına dayandığı vurgulanır.",
         "Dört büyük ilahi kitap hangi peygamberlere indirilmiştir?",
         "Tevrat Hz. Musa'ya, Zebur Hz. Davud'a, İncil Hz. İsa'ya, Kur'an ise Hz. Muhammed'e indirilmiştir."),
        
        ("Peygamber ve İlahi Kitap İnancı", "Son İlahi Kitap: Kur'an-ı Kerim", "Kur'an'ın Özellikleri ve Korunmuşluğu",
         "Kur'an'ın tahrif edilmeden kıyamete kadar korunacağı ilahi vaadini kavrar.",
         ["Hıfz", "Evrensellik", "Mushaf", "Mucize"],
         "Hafızlık geleneği ve yazılı metin güvencesi incelenir.",
         "Kur'an'ı diğer ilahi kitaplardan ayıran en önemli özellik nedir?",
         "Evrensel olması, kıyamete kadar geçerli kalması ve tek bir harfi dahi değişmeden günümüze ulaşmasıdır."),
        
        ("Peygamber ve İlahi Kitap İnancı", "İlk İnsan ve İlk Peygamber", "Hz. Adem Kıssası",
         "Hz. Adem'in yaratılışı, cennet imtihanı, tevbesi ve yeryüzündeki halifeliğini inceler.",
         ["Hz. Adem", "Tevbe", "Hilafet", "İmtihan"],
         "Hata karşısında pişmanlık ve tevbe erdemi işlenir.",
         "Hz. Adem kıssasından çıkarılacak en mühim ahlaki ders nedir?",
         "İnsanın hata yapabileceğini ancak kibre kapılmadan samimiyetle tevbe etmesi gerektiğini öğretir."),
        
        ("Peygamber ve İlahi Kitap İnancı", "Bir Sure Öğreniyorum", "Asr Suresi ve Anlamı",
         "Asr suresinin anlamını ve zamanı hayırla değerlendirmenin, sabır ve hakkı tavsiye etmenin önemini modeller.",
         ["Asr", "Zaman", "Sabır", "Hakk"],
         "İmam Şafii'nin Asr suresi hakkındaki sözü incelenir.",
         "Asr suresine göre hüsrandan (ziyandan) kurtulanların dört özelliği nedir?",
         "İman edenler, salih amel işleyenler, birbirine hakkı ve sabrı tavsiye edenlerdir."),
        
        ("Namaz İbadeti", "Namazın Önemi ve Anlamı", "Namaz Kılmanın Bireysel Faydaları",
         "Namazın insan ruhuna verdiği sükunet, iç disiplin ve temizlik bilincini açıklar.",
         ["Namaz", "İç Huzur", "Disiplin", "Şükür"],
         "Günün beş vaktinde Allah'ı hatırlamanın psikolojik etkileri anlatılır.",
         "Namaz ibadetinin kul ile Rabbi arasındaki bağı nasıl güçlendirir?",
         "Günün koşuşturması içinde kula yaratıcısını hatırlatır, günahlardan arındırır."),

        # Ünite 2: Namaz İbadeti (9-15)
        ("Ara Tatil", "1. Dönem Ara Tatil Tekrarı", "İnanç ve İbadet Pekiştirme",
         "Peygamberler tarihi ve namaz hazırlık konularında soru çözümü yapar.",
         ["Tatil", "Pekiştirme", "Ölçme", "Kazanım"],
         "Kazanım kavrama testleri çözülür.",
         "Namaz kılmak neden dinin direği olarak nitelendirilir?",
         "Müslümanın inancını her gün amele döken en temel ve sürekli ibadet olduğu içindir."),
        
        ("Namaz İbadeti", "Namaz Çeşitleri", "Farz, Vacip ve Nafile Namazlar",
         "Beş vakit, cuma, bayram, cenaze, vitir ve teravih namazlarını hükümlerine göre sınıflandırır.",
         ["Farz", "Vacip", "Nafile", "Vitir"],
         "Hüküm farkları ve kılınış zamanları şematize edilir.",
         "Vitir namazı ve bayram namazlarının dini hükmü nedir?",
         "Hanefi mezhebine göre vaciptir."),
        
        ("Namaz İbadeti", "Cemaatle Namaz", "Cemaatin Önemi ve Saf Düzeni",
         "Cemaatle kılınan namazın 27 derece daha faziletli olduğunu ve birlik duygusunu kavrar.",
         ["Cemaat", "İmam", "Cemaat Fazileti", "Eşitlik"],
         "Camideki saf düzeninin toplum intizamına katkısı anlatılır.",
         "Cemaatle namazda safların düzgün ve sık olmasının hikmeti nedir?",
         "Müminler arasındaki sevgiyi, birliği pekiştirmek ve şeytanın vesvesesine engel olmaktır."),
        
        ("Namaz İbadeti", "Cuma ve Cenaze Namazı", "Haftalık Buluşma ve Son Görev",
         "Cuma namazının cemaatle kılınmasının farz olduğunu; cenaze namazının ise dua niteliğini öğrenir.",
         ["Cuma", "Hutbe", "Cenaze", "Farz-ı Kifaye"],
         "Cenaze namazında rükû ve secde bulunmadığı açıklanır.",
         "Cenaze namazının hükmü nedir?",
         "Farz-ı kifayedir; bir kısım Müslüman kıldığında diğerlerinin üzerinden sorumluluk kalkar."),
        
        ("Namaz İbadeti", "Yolculukta ve Hastalıkta Namaz", "Dinde Kolaylık İlkeleri",
         "Seferilikte namazların kısaltılması, cem edilmesi ve hasta namazı kolaylıklarını değerlendirir.",
         ["Seferi", "Cem", "Kolaylık", "Ruhsat"],
         "İslam dininin zorlaştırmayıp kolaylaştırdığı prensibi incelenir.",
         "Dört rekatlık farz namazlar seferilik durumunda kaç rekat kılınır?",
         "İkişer rekat olarak kısaltılarak (kasr) kılınır."),
        
        ("Namaz İbadeti", "Bir Peygamber Tanıyorum", "Hz. Zekeriya Kıssası",
         "Hz. Zekeriya'nın samimi duası, sabrı ve Hz. Meryem'e hamilik edişini öğrenir.",
         ["Hz. Zekeriya", "Dua", "Mihrap", "Sabır"],
         "İhtiyarlık çağında dahi Allah'tan umut kesmeyip dua etmesi örneklendirilir.",
         "Hz. Zekeriya'nın duasından ne öğreniyoruz?",
         "Şartlar ne kadar zor olursa olsun Allah'ın kudretinden asla ümit kesilmemesi gerektiğini öğreniyoruz."),
        
        ("Namaz İbadeti", "Bir Sure Öğreniyorum", "Fil Suresi ve Anlamı",
         "Fil vakasını, Kâbe'yi koruyan ilahi kudreti ve Fil suresinin mesajını öğrenir.",
         ["Fil Vakası", "Ebabil", "Ebrehe", "Kâbe"],
         "Zulüm ve kibrin ilahi güç karşısında mağlup olduğu işlenir.",
         "Fil suresinin ana teması nedir?",
         "Allah'ın mukaddes evi Kâbe'yi koruduğu ve kibirli zalimleri helak ettiği gerçeğidir."),

        # Ünite 3: Zararlı Alışkanlıklar (16-22)
        ("Zararlı Alışkanlıklar", "Zararlı Alışkanlıkların Sebepleri", "Arkadaş Çevresi ve Özenti",
         "Alkol, sigara, uyuşturucu ve kumar gibi kötülüklere başlamada yanlış arkadaşlığın etkisini analiz eder.",
         ["Akran Baskısı", "Özenti", "İrade", "Seçim"],
         "Hayır diyebilme becerisi drama yoluyla canlandırılır.",
         "Zararlı alışkanlıklardan korunmada en kritik beceri nedir?",
         "Yanlış arkadaş tekliflerine ve akran baskısına karşı kararlılıkla 'Hayır!' diyebilmektir."),
        
        ("Zararlı Alışkanlıklar", "Beden ve Akıl Sağlığının Korunması", "İslam'da Aklın ve Canın Emniyeti",
         "İslam dininin haram kıldığı şeylerin tamamında insanın fiziki ve ruhi faydası olduğunu kavrar.",
         ["Haram", "Akıl Emniyeti", "Beden Sağlığı", "Fıtrat"],
         "Alkol ve uyuşturucunun beyin hücrelerine verdiği telafisiz zararlar aktarılır.",
         "İslamiyet'te alkollü içkilerin ve uyuşturucuların haram kılınmasının temel gerekçesi nedir?",
         "İnsanın aklını, iradesini ve muhakeme yeteneğini elinden alarak can ve mal emniyetini tehlikeye düşürmesidir."),
        
        ("Zararlı Alışkanlıklar", "1. Dönem Sonu Sentezi", "1. Dönem Din Kültürü Değerlendirmesi",
         "Peygamberler, namaz ve zararlı alışkanlıklardan korunma ünitelerini kapsayan değerlendirme yapar.",
         ["Sentez", "Kazanım", "Tekrar", "Ölçme"],
         "Kapsamlı soru çözümü ve ahlaki değer muhasebesi yapılır.",
         "İslam dininde emanet bilinci bedeni nasıl kapsar?",
         "Bedenimiz bize Allah'ın bir emanetidir; ona zarar verecek zararlı maddelerden korumak dini bir görevdir."),
        
        ("Zararlı Alışkanlıklar", "1. Dönem Sonu Karnesi", "Akademik ve Ahlaki Gelişim Raporu",
         "Dönem boyunca sergilenen sorumluluk, ödev ve tutumları değerlendirir.",
         ["Gelişim", "Öz Değerlendirme", "Karne", "Takdir"],
         "Manevi gelişim hedefleri belirlenir.",
         "Bir Müslümanın vaktini boşa harcamaktan kaçınması hangi değerle açıklanır?",
         "Zaman israfından kaçınma ve ömrü hayırlı amellerle değerlendirme şuuruyla açıklanır."),
        
        ("Zararlı Alışkanlıklar", "Kumar ve Şans Oyunları", "Haksız Kazanç ve Toplumsal Yıkım",
         "Alın teri dökmeden kazanılan kumardan kaynaklanan aile facialarını ve haram kazancı açıklar.",
         ["Kumar", "Haksız Kazanç", "Alın Teri", "Kul Hakkı"],
         "Şans oyunlarının bağımlılık döngüsü ve yuva yıkıcı tesirleri incelenir.",
         "Kumar oynamanın toplum üzerindeki en yıkıcı sonucu nedir?",
         "Aile düzenini çökertmesi, haksız kazanç oluşturması ve tembelliğe sevk etmesidir."),
        
        ("Zararlı Alışkanlıklar", "Teknoloji ve Dijital Bağımlılık", "Zaman İsrafı ve Sanal Tuzaklar",
         "Ekran bağımlılığı, şiddet içerikli oyunlar ve sanal kumar tehlikelerine karşı bilinçlenir.",
         ["Dijital Bağımlılık", "Siber Zorbalık", "Zaman İsrafı", "Bilinç"],
         "Ekran süresini sınırlama ve verimli ders çalışma dengesi anlatılır.",
         "Teknolojiyi ahlaklı ve dengeli kullanmak ne anlama gelir?",
         "Gerektiği kadar, ilim ve fayda odaklı kullanmak; bağımlı hale gelip gerçek hayattan kopmamaktır."),
        
        ("Zararlı Alışkanlıklar", "Bir Peygamber Tanıyorum", "Hz. Yahya Kıssası",
         "Hz. Yahya'nın genç yaşta ilim ve hikmetle donanmasını, iffet ve doğruluğunu öğrenir.",
         ["Hz. Yahya", "İffet", "Hikmet", "Şehadet"],
         "Haksızlığa karşı dimdik duran dürüst peygamber şahsiyeti işlenir.",
         "Hz. Yahya'nın gençlere rol model olan vasfı nedir?",
         "Çocukluğundan itibaren edep, iffet, ilim ve hakikati savunma konusundaki sarsılmaz cesaretidir."),

        # Ünite 4: Hz. Muhammed'in Hayatı (23-29)
        ("Hz. Muhammed'in Hayatı", "İslam Öncesi Hicaz ve Mekke", "Cahiliye Dönemi ve Erdemliler Topluluğu",
         "Cahiliye toplumundaki haksızlıkları ve Peygamberimizin Hilfü'l-Fudûl cemiyetine katılımını inceler.",
         ["Cahiliye", "Hilfü'l-Fudûl", "Adalet", "Mekke"],
         "Zayıfların hakkını korumak için genç yaşta sivil toplum faaliyetine öncülük etmesi anlatılır.",
         "Hilfü'l-Fudûl (Erdemliler Topluluğu) hangi amaçla kurulmuştur?",
         "Mekke'de yerli veya yabancı kim olursa olsun haksızlığa ve zulme uğrayan mazlumların hakkını aramak için kurulmuştur."),
        
        ("Hz. Muhammed'in Hayatı", "İlk Vahiy ve Davet", "Hira'dan Daru'l-Erkam'a Tebliğ",
         "610 yılında Hira'da gelen ilk vahiy sürecini ve gizli davet dönemini öğrenir.",
         ["İlk Vahiy", "Alak Suresi", "Daru'l-Erkam", "Davet"],
         "Hz. Hatice'nin Peygamberimize olan sarsılmaz desteği incelenir.",
         "İlk vahiy geldiğinde Hz. Hatice Peygamberimizi nasıl teselli etmiştir?",
         "'Allah seni asla utandırmaz. Çünkü sen akrabayı gözetirsin, doğru söylersin, yoksulu doyurursun' demiştir."),
        
        ("Hz. Muhammed'in Hayatı", "Tebliğe Karşı Baskılar ve Hicret", "Müşriklerin Zulmü ve Medine'ye Göç",
         "Mekke müşriklerinin boykotunu, Taif yolculuğunu ve 622 Medine'ye hicretini inceler.",
         ["Boykot", "Taif", "Hicret", "Sevr"],
         "Hicretin sadece bir mekân değişikliği değil, adalete doğru bir inkılap olduğu vurgulanır.",
         "İslam tarihinde hicretin önemi nedir?",
         "Baskı altındaki Müslümanların hürriyete kavuşması ve Medine'de İslam devletinin kurulması dönüm noktasıdır."),
        
        ("Ara Tatil", "2. Dönem Ara Tatil Tekrarı", "Siyer ve Zararlı Alışkanlıklar Kampı",
         "Hicret olayına kadar olan siyer konularında deneme soruları çözer.",
         ["Ara Tatil", "Siyer", "Kamp", "Tekrar"],
         "Tarihsel kronoloji eşleştirme etkinlikleri yapılır.",
         "Peygamber Efendimizin Medine'ye hicret ederken Sevr Mağarası'ndaki tevekkülü bize neyi öğretir?",
         "Tüm tedbirleri aldıktan sonra Allah'a tam teslimiyet göstermek gerektiğini öğretir."),
        
        ("Hz. Muhammed'in Hayatı", "Medine İslam Toplumunun İnşası", "Mescid-i Nebevi ve Muahat (Kardeşlik)",
         "Muhacir ile Ensar arasındaki kardeşlik anlaşmasını ve Medine Sözleşmesi'ni değerlendirir.",
         ["Muahat", "Ensar", "Muhacir", "Medine Sözleşmesi"],
         "Farklı din mensuplarıyla bir arada barış içinde yaşama tecrübesi işlenir.",
         "Medine Sözleşmesi'nin evrensel hukuk açısından değeri nedir?",
         "Farklı inanç ve ırktan toplulukların kendi inançlarını özgürce yaşamasını garanti altına alan ilk yazılı anayasadır."),
        
        ("Hz. Muhammed'in Hayatı", "Barış ve Fetih", "Hudeybiye Antlaşması ve Mekke'nin Fethi",
         "Hudeybiye Barışı'nın getirdiği stratejik zaferi ve Mekke'nin kansız fethini açıklar.",
         ["Hudeybiye", "Mekke'nin Fethi", "Genel Af", "Sulh"],
         "Düşmanlarına dahi merhamet eden fatih portresi üzerinde durulur.",
         "Peygamberimiz Mekke'yi fethettiğinde kendisine yıllarca zulmeden Kureyşlilere nasıl davranmıştır?",
         "Hepsini affettiğini ilan etmiş, intikam ve yağmaya asla izin vermemiştir."),
        
        ("Hz. Muhammed'in Hayatı", "İnsan Hakları Evrensel Beyannamesi: Veda Hutbesi", "Veda Haccı ve Hutbesi",
         "Veda Hutbesi'ndeki can, mal, kadın hakları ve ırkçılık karşıtı evrensel ilkeleri inceler.",
         ["Veda Hutbesi", "İnsan Hakları", "Eşitlik", "Kadın Hakları"],
         "Arap'ın Acem'e üstünlüğü olmadığı vurgulanır.",
         "Veda Hutbesi'nde ırkçılığı reddeden meşhur ifade nedir?",
         "'Ey insanlar! Rabbiniz birdir, babanız birdir. Hepiniz Adem'densiniz, Adem de topraktandır. Arap'ın Arap olmayana üstünlüğü yoktur; üstünlük ancak takvadadır.'"),

        # Ünite 5: Temel Değerlerimiz (30-36)
        ("Temel Değerlerimiz", "Bir Sure Öğreniyorum", "Nasr Suresi ve Anlamı",
         "Nasr suresinin anlamını ve Allah'ın yardımı gelip insanlar dine fevc fevc girdiğinde hamd ve istiğfar etmeyi öğrenir.",
         ["Nasr", "Zafer", "İstiğfar", "Hamd"],
         "Zafer kazanan bir müminin şımarmayıp tevazu göstermesi gerektiği işlenir.",
         "Nasr suresinde Müslümanlara zafer anında hangi emir verilmiştir?",
         "Rabbi hamd ile tesbih etmek ve O'ndan bağışlanma (istiğfar) dilemek emredilmiştir."),
        
        ("Temel Değerlerimiz", "Toplumu Birleştiren Değerler", "Milletimizi Kaynaştıran Unsurlar",
         "Din, dil, tarih ve vatan birliğinin milli dayanışmadaki hayati rolünü değerlendirir.",
         ["Milli Birlik", "Manevi Değer", "Dayanışma", "Kardeşlik"],
         "Millet olma şuurunun temelleri irdelenir.",
         "Bir milleti ayakta tutan en kuvvetli bağlar nelerdir?",
         "Ortak inanç, vatan sevgisi, bağımsızlık şuuru ve ortak tarihi mirastır."),
        
        ("Temel Değerlerimiz", "Vatan ve Bayrak Sevgisi", "Vatan Müdafaası ve Bayrağın Anlamı",
         "Vatanı korumanın dini ve ahlaki bir vecibe olduğunu kavrar.",
         ["Vatan Sevgisi", "Al Bayrak", "Müdafaa", "Hürriyet"],
         "İstiklal Marşımızın vatan ve şehadet vurguları incelenir.",
         "'Vatan sevgisi imandandır' sözü bir gence ne tür görevler yükler?",
         "Vatanı için çok çalışmayı, ilimde ilerlemeyi ve gerektiğinde canını feda edecek şuurda olmayı yükler."),
        
        ("Temel Değerlerimiz", "Şehitlik ve Gazilik", "En Yüce Mertebeler",
         "Vatan, bayrak ve mukaddesat uğruna can veren şehitlerin Allah katındaki makamını açıklar.",
         ["Şehitlik", "Gazilik", "Fedakarlık", "Makam"],
         "Kur'an'da 'Onlara ölüler demeyiniz' ayeti irdelenir.",
         "Şehitlik ve gazilik kavramları arasındaki fark nedir?",
         "Kutsal değerler uğruna canını feda edene şehit; bu uğurda savaşıp sağ dönene gazi denir."),
        
        ("Temel Değerlerimiz", "İstiklal Marşımız ve Mehmet Akif", "İstiklal Marşı'ndaki Dini Motifler",
         "Mehmet Akif Ersoy'un şiirinde geçen ezan, mabed, şehadet ve mabet mısralarını tahlil eder.",
         ["Mehmet Akif", "İstiklal Marşı", "Mabed", "Ezan"],
         "'Bu ezanlar ki şehadetleri dinin temeli' mısrası tahlil edilir.",
         "İstiklal Marşı'nda geçen 'Değmesin mabedimin göğsüne namahrem eli' mısrası neyi ifade eder?",
         "Mabetlerimizin ve vatan topraklarımızın yabancı ve düşman çizmeleriyle kirletilmesine asla izin verilmeyeceğini ifade eder."),
        
        ("Temel Değerlerimiz", "Milli ve Dini Bayramlarımız", "Kaynaşma ve Sevinç Günleri",
         "Ramazan ve Kurban bayramları ile 23 Nisan, 19 Mayıs, 29 Ekim ve 15 Temmuz'un ruhunu kavrar.",
         ["Bayram", "Milli Gün", "Ziyaret", "Birlik"],
         "Büyükleri ziyaret, küskünlerin barışması ve yetimlerin sevindirilmesi anlatılır.",
         "Bayramların toplum hayatındaki birleştirici rolü nedir?",
         "Akrabalık bağlarını canlandırır, kırgınlıkları bitirir, yoksulları sevindirerek toplumsal huzuru tesis eder."),
        
        ("Temel Değerlerimiz", "6. Sınıf Din Kültürü Yıl Sonu Sentezi", "Yıl Sonu Değerlendirme ve Veda",
         "Peygamberler, ibadet, ahlak, siyer ve temel değerler kazanımlarını bütünleştirir.",
         ["Sentez", "Mezuniyet", "Kazanım", "Portfolyo"],
         "Genel kazanım testi çözülür ve yaz tatili ahlak rehberi paylaşılır.",
         "6. Sınıf Din Kültürü dersinden edinilen en mühim ilke nedir?",
         "Sözünde duran, ibadetlerini aksatmayan, zararlı alışkanlıklardan uzak duran ve vatanını seven erdemli bir birey olmaktır.")
    ]
    assert len(u) == 36, f"Din 6 count: {len(u)}"
    return {
        'title': '6. Sınıf',
        'subtitle': 'Ortaokul Din Kültürü ve Ahlak Bilgisi',
        'badge': 'Ortaokul Din',
        'weeks': _make_weeks(u, 'DİN.6')
    }

def get_din_7():
    # 7. Sınıf MEB Müfredatı (5 Ünite - Tam 36 Hafta)
    u = [
        # Ünite 1: Melek ve Ahiret İnancı (1-8)
        ("Melek ve Ahiret İnancı", "Görülen ve Görülemeyen Varlıklar", "Madde Ötesi Âlem ve Varlıklar",
         "Duyularla algılanamayan ancak varlığı vahiy yoluyla bilinen gayb âlemini kavrar.",
         ["Gayb", "Görünmeyen Âlem", "Vahiy", "İman"],
         "Varlığın sadece gözle görülen maddeden ibaret olmadığı aktarılır.",
         "Gözümüzle göremediğimiz bir şeyin yok olduğunu iddia etmek neden bilimsel değildir?",
         "Aklımız, duygularımız, yerçekimi ve radyo dalgaları da gözle görülmez ama varlıkları inkâr edilemez."),
        
        ("Melek ve Ahiret İnancı", "Melekler ve Özellikleri", "Nurdan Yaratılan İtaatkar Varlıklar",
         "Meleklerin cinsiyetsiz, yemez içmez ve daima Allah'a ibadet eden varlıklar olduğunu öğrenir.",
         ["Melek", "Nur", "İbadet", "İtaat"],
         "Meleklerin insanlara daima iyiliği fısıldadığı vurgulanır.",
         "Meleklerin insanlardan temel farkı nedir?",
         "Nefisleri ve iradeleri yoktur; günah işlemezler ve sadece Allah'ın emirlerini harfiyen yerine getirirler."),
        
        ("Melek ve Ahiret İnancı", "Dört Büyük Melek ve Diğerleri", "Cebrail, Mikail, İsrafil ve Azrail",
         "Dört büyük melek ile Kiramen Katibin, Münker-Nekir ve Hafaza meleklerini tanır.",
         ["Cebrail", "Mikail", "İsrafil", "Azrail", "Kiramen Katibin"],
         "Kiramen Katibin'in iyi ve kötü amelleri kaydetme şuuru işlenir.",
         "Kiramen Katibin meleklerinin varlığını bilen bir insanda hangi duygu gelişir?",
         "Yalnız kaldığında bile günah işlememe, amellerinin kaydedildiği bilinciyle sorumluluk duygusu gelişir."),
        
        ("Melek ve Ahiret İnancı", "Cin ve Şeytan", "Ateşten Yaratılan İmtihan Varlıkları",
         "Cinlerin de insanlar gibi mükellef olduğunu, şeytanın ise kibirlenerek sapan varlık olduğunu kavrar.",
         ["Cin", "Şeytan", "Kibir", "Vesvese"],
         "Büyü, fal gibi batıl inançların İslam dışı olduğu anlatılır.",
         "Şeytanın insana kurduğu en tehlikeli tuzak nedir?",
         "Kötülükleri ve günahları süslü göstererek insanı Allah'ın rahmetinden ve emrinden uzaklaştırmaktır."),
        
        ("Melek ve Ahiret İnancı", "Ahiret Hayatının Aşamaları", "Ölüm, Kıyamet, Ba's ve Haşr",
         "Ölümün bir son değil, sonsuz ahiret yurduna geçiş kapısı olduğunu öğrenir.",
         ["Kıyamet", "Ba's", "Haşr", "Mahşer"],
         "Sura üflenmesi ve yeniden diriliş aşamaları Kur'an ayetleriyle açıklanır.",
         "Ahirette 'Ba's' ve 'Haşr' ne anlama gelir?",
         "Ba's insanların yeniden diriltilmesi; Haşr ise hesap vermek üzere mahşer meydanında toplanmasıdır."),
        
        ("Melek ve Ahiret İnancı", "Hesap, Mizan ve Cennet/Cehennem", "İlahi Adaletin Tecellisi",
         "Amel defterlerinin dağıtılması, mizan terazisi ve amellerin karşılığını inceler.",
         ["Hesap", "Mizan", "Amel Defteri", "Adalet"],
         "Zerre kadar hayrın ve zerre kadar şerrin karşılıksız kalmayacağı vurgulanır.",
         "Ahiret inancı insana bu dünyada nasıl bir adalet duygusu kazandırır?",
         "Haksızlığa uğrayan mazlumların hakkının mutlaka alınacağını, zalimlerin cezasız kalmayacağını bilerek güven verir."),
        
        ("Melek ve Ahiret İnancı", "Bir Peygamber Tanıyorum", "Hz. İsa Kıssası",
         "Hz. İsa'nın babasız doğumu, beşikte konuşması, mucizeleri ve tevhid mesajını öğrenir.",
         ["Hz. İsa", "Hz. Meryem", "İncil", "Mucize"],
         "Hristiyanlıktaki teslis (üçleme) inancına karşı Kur'an'ın tevhid cevabı işlenir.",
         "Hz. İsa'nın peygamberliği konusundaki İslam inancı nedir?",
         "O Allah'ın oğlu veya ilah değil; Allah'ın kulu, elçisi ve 'Kelimetullah' olarak yarattığı ulu'l-azm peygamberdir."),
        
        ("Melek ve Ahiret İnancı", "Bir Sure Öğreniyorum", "Nas Suresi ve Anlamı",
         "Nas suresinin anlamını ve sinsi vesvesecilerin şerrinden insanların Rabbine sığınmayı öğrenir.",
         ["Nas Suresi", "Vesvese", "İltica", "Korunma"],
         "Felak ve Nas surelerinin (Muavvizeteyn) koruyucu manası incelenir.",
         "Nas suresinde hangi tehlikeye karşı Allah'a sığınılmaktadır?",
         "İnsanların kalbine vesvese ve şüphe tohumları eken sinsi cin ve insan şeytanlarının şerrine karşı."),

        # Ünite 2: Hac ve Kurban (9-15)
        ("Ara Tatil", "1. Dönem Ara Tatil Tekrarı", "Melek ve Ahiret İnancı Kampı",
         "Ahiretin aşamaları ve melekler konularında LGS tarzı beceri temelli sorular çözer.",
         ["Tatil", "Kamp", "Soru Çözümü", "Tekrar"],
         "Kavram haritaları tamamlanır.",
         "Ölüm korkusunu ve kaygısını gideren en sağlam inanç nedir?",
         "Ölümün bir yok oluş değil, sonsuz güzellikteki ahiret yurduna ve Rabbe kavuşma olduğunu bilmektir."),
        
        ("Hac ve Kurban", "Hac İbadeti ve Önemi", "Kâbe'ye Yolculuk ve Farziyeti",
         "Haccın gücü yeten Müslümanlara ömürde bir kez farz olduğunu ve evrensel kardeşliği kavrar.",
         ["Hac", "Kâbe", "Mekke", "Farz"],
         "Haccın zenginlik ve sağlık şartları açıklanır.",
         "Hac ibadetinin en belirgin evrensel yönü nedir?",
         "Dünyanın dört bir yanından farklı renk, dil ve ırktan milyonlarca Müslümanı aynı safta ve eşitlikte buluşturmasıdır."),
        
        ("Hac ve Kurban", "Haccın Farzları ve Mekânları", "İhram, Tavaf ve Arafat Vakfesi",
         "İhrama girme, Kâbe etrafında 7 şavt dönerek tavaf etme ve Arafat vakfesini öğrenir.",
         ["İhram", "Tavaf", "Arafat", "Vakfe"],
         "İhram kıyafetinin kefeni ve mahşer gününü sembolize ettiği anlatılır.",
         "Haccın olmazsa olmaz iki temel farzı (rükunları) nelerdir?",
         "Arafat'ta vakfe yapmak ve Kâbe'yi ziyaret tavafı yapmaktır."),
        
        ("Hac ve Kurban", "Haccın Vacip ve Sünnetleri", "Sa'y, Şeytan Taşlama ve Müzdelife",
         "Safa ile Merve arasında sa'y etmeyi, Mina'da şeytan taşlamayı ve Müzdelife gecesini inceler.",
         ["Sa'y", "Hz. Hacer", "Mina", "Müzdelife"],
         "Hz. Hacer'in zemzem arayışı ve teslimiyeti anlatılır.",
         "Sa'y ibadeti kime olan hürmet ve hatıranın yâd edilmesidir?",
         "Oğlu Hz. İsmail için su ararken Safa ile Merve arasında koşan Hz. Hacer'in azim ve tevekkülüdür."),
        
        ("Hac ve Kurban", "Umre İbadeti", "Küçük Hac ve Ziyaret",
         "Umrenin hacdan farklarını (vakfe ve kurban olmaması, yılın her vakti yapılabilmesi) açıklar.",
         ["Umre", "Nafile", "Ziyaret", "Tavaf"],
         "Hac ile umre arasındaki farklar tablo halinde karşılaştırılır.",
         "Hac ile umre arasındaki en temel farklar nelerdir?",
         "Hac belirli zamanda yapılır, farzdır; vakfe ve kurban vardır. Umre ise sünnettir, her zaman yapılabilir; vakfe ve kurban yoktur."),
        
        ("Hac ve Kurban", "Kurban İbadeti ve Paylaşma", "Allah'a Yakınlaşma ve Cömertlik",
         "Kurbanın et ve kan değil, takva ve paylaşma ibadeti olduğunu; etlerin üçe bölünmesini öğrenir.",
         ["Kurban", "Takva", "Kurban Eti", "İnfak"],
         "Kurban etinin üçe bölünerek (yoksullara, komşulara ve aileye) dağıtılması işlenir.",
         "Kur'an'da kurban ibadetiyle ilgili 'Allah'a ulaşan nedir?' ayetinin anlamı nedir?",
         "Kurbanların ne etleri ne de kanları Allah'a ulaşır; O'na ulaşacak olan yalnızca kalplerimizdeki ihlas ve takvadır."),
        
        ("Hac ve Kurban", "Bir Peygamber Tanıyorum", "Hz. İsmail Kıssası",
         "Hz. İsmail'in babasına itaati, sabrı ve kurban hadisesindeki teslimiyetini inceler.",
         ["Hz. İsmail", "Teslimiyet", "Zemzem", "Kurban"],
         "Kurban emrinin fedakarlık ve güven sınavı olduğu vurgulanır.",
         "Hz. İsmail'in kurban hadisesindeki tavrı bir gence ne mesaj verir?",
         "Ebeveynine saygı, verilen ilahi emirlere karşı sarsılmaz güven ve teslimiyet mesajı verir."),

        # Ünite 3: Ahlaki Davranışlar (16-22)
        ("Ahlaki Davranışlar", "Güzel Ahlakın Temeli: Adalet ve Dürüstlük", "Doğruluktan Ayrılmamak",
         "Her durumda adil olmayı, akraba aleyhine olsa bile adaleti ayakta tutmayı kavrar.",
         ["Adalet", "Sıdk", "Dürüstlük", "Hakikat"],
         "Adalet mülkün temelidir ilkesi tahlil edilir.",
         "Kur'an'da adaletin uygulanmasıyla ilgili verilen en çarpıcı emir nedir?",
         "'Bir topluluğa olan öfkeniz sizi adaletsizlik yapmaya sevk etmesin. Adil olun; takvaya en yakın olan budur.'"),
        
        ("Ahlaki Davranışlar", "Dostluk ve Kardeşlik", "Güvenilir Dost Seçimi ve Vefa",
         "Dostlukta samimiyet, sır saklama, iyi ve kötü günde yan yana olma erdemini kavrar.",
         ["Dostluk", "Vefa", "Sırdaşlık", "Kardeşlik"],
         "Kötü arkadaşın demirci körüğü, iyi arkadaşın misk kokusu satan kimse misali incelenir.",
         "İslam ahlakına göre gerçek bir dost nasıl olmalıdır?",
         "Arkadaşını kötülükten alıkoyan, hayra teşvik eden ve arkasından gıybetini yapmayan kimsedir."),
        
        ("Ahlaki Davranışlar", "1. Dönem Sonu Sentezi", "1. Dönem Din Kültürü Değerlendirmesi",
         "Melekler, hac, kurban ve güzel ahlak kazanımlarını kapsayan geniş deneme sınavı yapar.",
         ["Sentez", "Deneme", "Tekrar", "Ölçme"],
         "LGS soru kalıplarıyla deneme yapılır.",
         "Hac ibadetinde giyilen ihram kumaşı insana neyi hatırlatır?",
         "Makam, zenginlik ve elbiselerin geçici olduğunu; Allah huzuruna ancak amellerimizle gideceğimizi hatırlatır."),
        
        ("Ahlaki Davranışlar", "1. Dönem Sonu Karnesi", "Yarıyıl Tatili Ahlak ve Maneviyat Planı",
         "1. dönemin değerlendirmesini yapar, tatilde akraba ve komşu ziyaretleri planlar.",
         ["Karne", "Sıla-i Rahim", "Ziyaret", "Öz Değerlendirme"],
         "Tatil ödevleri ve kitap okuma hedefleri belirlenir.",
         "Sıla-i rahim ne demektir ve neden önemlidir?",
         "Akraba ve yakınları ziyaret edip gözetmektir; ömrü bereketlendiren ve kardeşliği pekiştiren büyük bir sünnettir."),
        
        ("Ahlaki Davranışlar", "Öz Denetim ve Sabır", "Nefse Hakim Olma ve Öfke Kontrolü",
         "Peygamberimizin 'Gerçek pehlivan öfkelendiğinde nefsine hakim olan kimsedir' hadisini çözümler.",
         ["Öz Denetim", "Sabır", "Öfke Kontrolü", "Hilim"],
         "Zorluklar karşısında metanet gösterme stratejileri işlenir.",
         "Peygamberimiz öfkelenen birine ne yapmasını tavsiye etmiştir?",
         "Ayaktaysa oturmasını, oturuyorsa uzanmasını veya abdest alarak sakinleşmesini tavsiye etmiştir."),
        
        ("Ahlaki Davranışlar", "Saygı, Sevgi ve Yardımseverlik", "Büyüklere Hürmet, Küçüklere Şefkat",
         "Yetimleri koruma, komşuya ikram ve doğaya saygılı olma erdemlerini açıklar.",
         ["Saygı", "Sevgi", "Merhamet", "Yardımseverlik"],
         "'Komşusu açken tok yatan bizden değildir' ölçüsü işlenir.",
         "İslam dininin yardımseverlik anlayışı kimleri kapsar?",
         "Sadece kendi akrabalarını değil; yetimleri, yoksulları, kimsesizleri ve yardıma muhtaç tüm canlıları kapsar."),
        
        ("Ahlaki Davranışlar", "Kul Hakkı ve Helallik", "En Büyük Ahlaki Sorumluluk",
         "Kul hakkının Allah'ın affetmediği, hak sahibiyle helalleşmeyi gerektiren hassasiyet olduğunu kavrar.",
         ["Kul Hakkı", "Helallik", "Gıybet", "Kul Emniyeti"],
         "Gıybet, iftira, hırsızlık ve kamu malını gasp etmenin vebali anlatılır.",
         "Kul hakkı ihlali yapan bir insan nasıl bağışlanabilir?",
         "Tevbe etmenin yanında mutlaka hakkını yediği kimseden helallik almalı ve zararını telafi etmelidir."),

        # Ünite 4: Allah'ın Kulu ve Elçisi Hz. Muhammed (23-29)
        ("Allah'ın Kulu ve Elçisi Hz. Muhammed", "Hz. Muhammed'in İnsani Yönü", "Beşer Olarak Peygamber",
         "Peygamberimizin de bir insan olarak doğduğunu, acıktığını, üzüldüğünü ve vefat ettiğini kavrar.",
         ["Beşer", "İnsani Yön", "Tevazu", "Örnek"],
         "Hristiyanların Hz. İsa'yı ilahlaştırması hatasına düşülmemesi vurgulanır.",
         "Hz. Muhammed'in (s.a.v.) insani yönünün vurgulanması neden çok mühimdir?",
         "Onun insanüstü ulaşılamaz bir varlık olmadığını, bizim gibi bir insan olarak hayatının her alanında örnek alınabileceğini gösterir."),
        
        ("Allah'ın Kulu ve Elçisi Hz. Muhammed", "Hz. Muhammed'in Peygamberlik Yönü", "Son Peygamber: Hatemü'l-Enbiya",
         "Peygamberimizin nübüvvet zincirinin son halkası olduğunu ve evrensel davetini açıklar.",
         ["Hatemü'l-Enbiya", "Nübüvvet", "Evrensellik", "Vahiy"],
         "Peygamberimizden sonra başka peygamber gelmeyeceği akidesi aktarılır.",
         "'Hatemü'l-Enbiya' ne anlama gelir?",
         "Peygamberlerin sonuncusu, nübüvvet zincirinin mührü ve tamamlayıcısı anlamına gelir."),
        
        ("Allah'ın Kulu ve Elçisi Hz. Muhammed", "Kur'an'ı Açıklayıcı Rolü (Tebyin)", "Sünnetin Dindeki Yeri",
         "Peygamberimizin Kur'an'daki hükümleri açıklama ve bizzat yaşayarak öğretme görevini analiz eder.",
         ["Tebyin", "Sünnet", "Hadis", "Rehber"],
         "Namazın rekatları, zekatın oranları gibi konuların sünnetle netleştiği işlenir.",
         "Peygamberimizin 'tebyin' görevi olmasaydı ne tür güçlükler yaşanırdı?",
         "Kur'an'daki namaz, oruç, zekat ve hac gibi genel emirlerin nasıl uygulanacağı bilinemez ve ihtilaflar çıkardı."),
        
        ("Ara Tatil", "2. Dönem Ara Tatil Tekrarı", "Sünnet ve Güzel Ahlak Kampı",
         "Peygamberimizin sünneti ve ahlak konularında pekiştirme soruları çözer.",
         ["Ara Tatil", "Sünnet", "Kamp", "Tekrar"],
         "Hadis mealleri analizi yapılır.",
         "Sünnete uymak bir Müslümana ne kazandırır?",
         "Kur'an'ı en doğru ve dengeli şekilde anlama ve hayata tatbik etme becerisi kazandırır."),
        
        ("Allah'ın Kulu ve Elçisi Hz. Muhammed", "Hz. Muhammed'in Hüküm Koyma Yetkisi (Teşri)", "Helal ve Haramlar",
         "Peygamberimizin vahye dayanarak İslam fıkhında getirdiği hüküm ve prensipleri öğrenir.",
         ["Teşri", "Fıkıh", "Helal", "Haram"],
         "Ehl-i beyt sevgisi ve ashabın örnekliği anlatılır.",
         "Peygamberimizin teşri (hüküm koyma) yetkisi neye dayanır?",
         "Yüce Allah'ın Kur'an'da peygambere itaati emretmesine ve vahiy rehberliğine dayanır."),
        
        ("Allah'ın Kulu ve Elçisi Hz. Muhammed", "Hz. Muhammed'in Örnekliği (Üsve-i Hasene)", "En Güzel Rol Model",
         "Peygamberimizin aile reisi, komutan, öğretmen ve arkadaş olarak mükemmel ahlakını modeller.",
         ["Üsve-i Hasene", "Rol Model", "Güzel Ahlak", "Şefkat"],
         "Çocuklara olan sevgisi ve eşlerine olan nezaketi işlenir.",
         "'Üsve-i Hasene' ne demektir?",
         "İnanç, ibadet, adalet ve ahlak konusunda en mükemmel, en ideal ve örnek alınacak şahsiyet demektir."),
        
        ("Allah'ın Kulu ve Elçisi Hz. Muhammed", "Bir Sure Öğreniyorum", "Kafirun Suresi ve Anlamı",
         "Kafirun suresinin anlamını ve inançta taviz verilmeyeceğini, din ve vicdan özgürlüğünü öğrenir.",
         ["Kafirun", "Tevhid", "İnanç Hürriyeti", "Kararlılık"],
         "'Sizin dininiz size, benim dinim banadır' ayetinin hoşgörü ve kararlılık boyutu anlatılır.",
         "Kafirun suresinin ana mesajı nedir?",
         "Tevhid inancından hiçbir şartta ödün verilemeyeceği ve kimsenin inanca zorlanamayacağıdır."),

        # Ünite 5: İslam Düşüncesinde Yorumlar (30-36)
        ("İslam Düşüncesinde Yorumlar", "Din ve Din Anlayışı Arasındaki Fark", "Metin ve Yorum Farkı",
         "Dinin vahye dayalı değişmez esasları ile din anlayışının beşerî ve değişken yönünü ayırt eder.",
         ["Din", "Din Anlayışı", "Yorum", "İçtihat"],
         "Zaman ve coğrafyanın fikirler üzerindeki etkisi tartışılır.",
         "Din ile din anlayışı arasındaki en temel fark nedir?",
         "Din vahye dayanır ve değişmez; din anlayışı ise insanların vahyi anlama biçimidir ve çağa/coğrafyaya göre değişebilir."),
        
        ("İslam Düşüncesinde Yorumlar", "İslam Düşüncesinde Yorum Biçimleri", "İtikadi, Fıkhi ve Tasavvufi Yorumlar",
         "Mezheplerin bir zenginlik olduğunu ve çatışma değil kolaylık vesilesi olduğunu kavrar.",
         ["Mezhep", "İtikad", "Fıkıh", "Tasavvuf"],
         "Mezheplerin ortaya çıkış sebepleri incelenir.",
         "İslam düşüncesinde mezheplerin ortaya çıkması bir ayrışma mıdır?",
         "Hayır, bir ayrışma değil; farklı sosyal, coğrafi ve kültürel ihtiyaçlara cevap veren fikri bir zenginliktir."),
        
        ("İslam Düşüncesinde Yorumlar", "İnançla İlgili (İtikadi) Yorumlar", "Maturidilik ve Eş'arilik",
         "İmam Maturidi ve İmam Eş'ari'nin akıl ve nakil dengesini nasıl kurduğunu öğrenir.",
         ["Maturidilik", "Eş'arilik", "İtikad", "Akıl ve Vahiy"],
         "Maturidi'nin Türk dünyasındaki merkezi rolü anlatılır.",
         "İmam Maturidi'nin İslam düşüncesine en büyük katkısı nedir?",
         "Akıl ile vahiy arasındaki uyumu mükemmel bir dengede savunarak itikadi konularda sağlam bir zemin kurmasıdır."),
        
        ("İslam Düşüncesinde Yorumlar", "Amelle İlgili (Fıkhi) Yorumlar", "Hanefilik, Şafilik, Malikilik, Hanbelilik",
         "Dört büyük ameli mezhebin kurucularını ve İslam coğrafyasındaki yayılışını tanır.",
         ["Hanefilik", "Şafilik", "Malikilik", "Hanbelilik", "Ebu Hanife"],
         "Ebu Hanife'nin ilmi dehası ve hür fikirleri aktarılır.",
         "Türkiye'de ve Türk dünyasında en yaygın fıkhi mezhep hangisidir?",
         "İmam Ebu Hanife'nin içtihatlarına dayanan Hanefi mezhebidir."),
        
        ("İslam Düşüncesinde Yorumlar", "Tasavvufi Yorumlar ve Gönül Sultanları", "Yesevilik, Mevlevilik ve Bektaşilik",
         "Ahmet Yesevi, Mevlana, Hacı Bektaş Veli ve Yunus Emre'nin sevgi ve hoşgörü dilini kavrar.",
         ["Tasavvuf", "Mevlana", "Hacı Bektaş", "Ahmet Yesevi"],
         "Mevlana'nın 'Gel, ne olursan ol yine gel' çağrısı incelenir.",
         "Hacı Bektaş Veli'nin 'Bir olalım, iri olalım, diri olalım' ve 'İncinsen de incitme' sözleri hangi medeniyet değerimizi özetler?",
         "Anadolu'da kurulan sevgi, kardeşlik, hoşgörü ve barış medeniyetini özetler."),
        
        ("İslam Düşüncesinde Yorumlar", "Alevilik-Bektaşilikte Temel Kavramlar", "Cem, Semah, Musahiplik ve Gülbeng",
         "Alevi-Bektaşi geleneğindeki cem erkanı, dedelik, semah ve 12 hizmeti saygıyla öğrenir.",
         ["Alevilik-Bektaşilik", "Cem Evi", "Semah", "Musahiplik", "Gülbeng"],
         "Gülbeng duaları ve Ehl-i Beyt sevgisi işlenir.",
         "Alevilik-Bektaşilik geleneğinde 'Musahiplik' ne demektir?",
         "İki kişinin dünya ve ahiret kardeşi olması, malını ve canını hak yolunda paylaşmasıdır."),
        
        ("İslam Düşüncesinde Yorumlar", "7. Sınıf Din Kültürü Yıl Sonu Sentezi", "Bütünsel Değerlendirme ve Hoşgörü",
         "Melekler, ahiret, hac, kurban, peygamberimiz ve İslam düşüncesindeki yorumları harmanlar.",
         ["Sentez", "Mezuniyet", "Hoşgörü", "Portfolyo"],
         "Geniş kazanım değerlendirmesi yapılır.",
         "Farklı düşünce ve mezheplere karşı bir Müslümanın takınması gereken tavır ne olmalıdır?",
         "Hoşgörülü, birleştirici ve farklılıkları Allah'ın rahmet ve zenginliği olarak kabul eden bir tavır olmalıdır.")
    ]
    assert len(u) == 36, f"Din 7 count: {len(u)}"
    return {
        'title': '7. Sınıf',
        'subtitle': 'Ortaokul Din Kültürü ve Ahlak Bilgisi',
        'badge': 'Ortaokul Din',
        'weeks': _make_weeks(u, 'DİN.7')
    }

def get_din_8():
    # 8. Sınıf LGS Sınav Odaklı MEB Müfredatı (5 Ünite - Tam 36 Hafta)
    u = [
        # Ünite 1: Kader İnancı (1-8)
        ("Kader İnancı", "Kader ve Kaza Kavramları", "Ölçü, Ahenk ve İlahi Plan",
         "Kaderin Allah'ın her şeyi bir ölçü ve düzene göre takdir etmesi; kazanın ise gerçekleşmesi olduğunu çözer.",
         ["Kader", "Kaza", "Ölçü", "Ahenk"],
         "Evrendeki fiziksel ve kimyasal kanunların kader ile bağı kurulur.",
         "Kader ve kaza kavramları arasındaki fark nedir?",
         "Kader Allah'ın ezeli ilmiyle her şeyi planlaması ve takdir etmesi; kaza ise zamanı gelince yaratıp var etmesidir."),
        
        ("Kader İnancı", "Evrenin Yasaları (Sünnetullah)", "Fiziksel, Biyolojik ve Toplumsal Yasalar",
         "Sünnetullah'ı fiziksel (yerçekimi, suyun kaldırması), biyolojik (fotosentez, DNA) ve toplumsal (adalet, göç) yasalara ayırır.",
         ["Sünnetullah", "Fiziksel Yasa", "Biyolojik Yasa", "Toplumsal Yasa"],
         "LGS'de sık çıkan paragraf sorularının yasa analizleri yapılır.",
         "'Toplumlar ancak adaletle ayakta kalır, adaletsizlik çöküş getirir' tespiti hangi evrensel yasaya girer?",
         "Toplumsal yasalara girer."),
        
        ("Kader İnancı", "İnsanın İradesi ve Kader", "Külli İrade ve Cüzi İrade",
         "Allah'ın sınırsız külli iradesi ile insanın sorumlu olduğu sınırlı cüzi iradesini ayırt eder.",
         ["Külli İrade", "Cüzi İrade", "Sorumluluk", "Seçim"],
         "İnsanın saç renginden değil, ahlaki seçimlerinden hesaba çekileceği anlatılır.",
         "İnsanın cüzi iradesi neyi doğurur?",
         "Ahlaki ve hukuki sorumluluğu doğurur; insan seçimlerinden dolayı sevap veya günah kazanır."),
        
        ("Kader İnancı", "Kaderle İlgili Kavramlar: Ecel ve Ömür", "Hayatın Sınırları ve Değerlendirilmesi",
         "Her canlının ecelinin belirli olduğunu, ömrün hayırlı amellerle değerlendirilmesi gerektiğini kavrar.",
         ["Ecel", "Ömür", "Fani", "Vakit"],
         "Trafik kurallarına uymayıp eceli suçlamanın yanlışlığı ele alınır.",
         "'Nasılsa ecelim değişmez' diyerek tedbirsiz davranmak İslam'ın kader anlayışına uyar mı?",
         "Hayır, uymaz. İnsan tedbir almakla yükümlüdür; tedbirsizlik intihar ve cinayet hükmündedir."),
        
        ("Kader İnancı", "Kaderle İlgili Kavramlar: Rızık ve Emek", "Helal Kazanç ve Alın Teri",
         "Rızkı verenin Allah olduğunu ancak insanın çalışıp çabalamak zorunda olduğunu çözümler.",
         ["Rızık", "Emek", "Helal Kazanç", "Tevekkül"],
         "'İnsan için ancak çalıştığının karşılığı vardır' ayeti tahlil edilir.",
         "Çalışmadan rızık beklemek doğru bir tevekkül müdür?",
         "Hayır, bu tembelliktir. Gerçek tevekkül tarlayı ekip suladıktan sonra mahsulü Allah'tan beklemektir."),
        
        ("Kader İnancı", "Kaderle İlgili Kavramlar: Tevekkül, Başarı ve Sağlık", "Doğru Tevekkül Anlayışı",
         "Gerekli tüm sebeplere sarıldıktan sonra sonrasını Allah'a havale etme şuurunu içselleştirir.",
         ["Tevekkül", "Gayret", "Başarı", "Sağlık"],
         "Sınava çalışmadan 'kısmetim neyse o olur' demenin sapkınlık olduğu vurgulanır.",
         "Hz. Peygamber devesini bağlamayan bedeviye ne buyurmuştur?",
         "'Önce deveni sağlam bir kazığa bağla, sonra Allah'a tevekkül et' buyurmuştur."),
        
        ("Kader İnancı", "Bir Peygamber Tanıyorum", "Hz. Musa'nın Mücadelesi",
         "Hz. Musa'nın Firavun karşısındaki cesaretini, Kızıldeniz mucizesini ve Tur Dağı vahyini öğrenir.",
         ["Hz. Musa", "Firavun", "Asa", "Kızıldeniz"],
         "Zulüm ne kadar güçlü görünürse görünsün hakkın galip geleceği işlenir.",
         "Hz. Musa Kızıldeniz kıyısında sıkıştığında kavmine ne demiştir?",
         "'Asla korkmayın! Muhakkak ki Rabbim benimle beraberdir, bana bir çıkış yolu gösterecektir' diyerek tam tevekkül göstermiştir."),
        
        ("Kader İnancı", "Bir Ayet Öğreniyorum", "Ayet el-Kürsi ve Anlamı",
         "Bakara suresinin 255. ayeti olan Ayet el-Kürsi'nin Allah'ın sıfatlarını nasıl özetlediğini modeller.",
         ["Ayet el-Kürsi", "Hayy", "Kayyum", "Kürsi"],
         "Allah'ın uyuklamayacağı, yerin ve göğün mülkünün O'na ait olduğu tahlil edilir.",
         "Ayet el-Kürsi'de geçen 'Hayy' ve 'Kayyum' isimleri ne manaya gelir?",
         "Hayy daima diri olan, Kayyum ise bütün varlıkları ayakta tutan ve yöneten demektir."),

        # Ünite 2: Zekat ve Sadaka (9-15)
        ("Ara Tatil", "1. Dönem Ara Tatil Tekrarı", "LGS 1. Ünite Kader Kampı",
         "Kader ve kaza, evrenin yasaları ve tevekkül konularından 50 LGS yeni nesil soru çözer.",
         ["LGS Kampı", "Kader", "Yeni Nesil", "Soru Analizi"],
         "Tuzak şıklar ve çeldiriciler üzerinde durulur.",
         "LGS sorularında 'fiziksel yasa' ile 'biyolojik yasa' nasıl ayırt edilir?",
         "Madde ve enerjinin yapısı, yerçekimi fizikseldir; canlıların yapısı, beslenmesi, üremesi biyolojiktir."),
        
        ("Zekat ve Sadaka", "İslam'da Paylaşma ve Yardımlaşma", "Mülkün Gerçek Sahibi Allah'tır",
         "İslam'ın toplumsal gelir adaletini sağlayan en güçlü müessesesi zekatın felsefesini kavrar.",
         ["Yardımlaşma", "İnfak", "Gelir Dağılımı", "Kardeşlik"],
         "Zekatın zengin ile fakir arasındaki haset ve nefreti yok ettiği işlenir.",
         "Zekat kelimesinin sözlük anlamı nedir?",
         "Temizlenme, artma, çoğalma ve bereket anlamlarına gelir."),
        
        ("Zekat ve Sadaka", "Zekat İbadetinin Şartları", "Nisap Miktarı ve Hükümleri",
         "Asli ihtiyaçlar haricinde 80.18 gram altın (nisap) değerinde mala sahip olanın yılda bir vermesini çözer.",
         ["Nisap", "Asli İhtiyaç", "Havaric-i Asliye", "Farz"],
         "Zekat verilecek mallar ve oranları tablosu incelenir.",
         "Nisap miktarı malda zekatın farz olması için aranan süre nedir?",
         "Malın üzerinden tam bir kameri yılın (havelanu'l-havl) geçmiş olması gerekir."),
        
        ("Zekat ve Sadaka", "Zekat Kimlere Verilir, Kimlere Verilmez?", "Tevbe Suresi 60. Ayet",
         "Fakirlere, yoksullara, borçlulara, yolda kalmışlara verileceğini; anne-baba ve evlada verilemeyeceğini çözer.",
         ["Zekat Verilecekler", "Tevbe 60", "Fakir", "Borçlu"],
         "Bakmakla yükümlü olunan kişilere zekat verilmeyeceği kuralı işlenir.",
         "Bir kimse öz annesine, babasına, çocuğuna veya torununa zekat verebilir mi?",
         "Hayır, veremez. Çünkü onlara zaten bakmakla yükümlüdür; zekat doğrudan ihtiyaç sahibi diğer kimselere verilir."),
        
        ("Zekat ve Sadaka", "Zekat Verilecek Mallar ve Oranları", "1/40, 1/10 (Öşür), 1/5 Oranları",
         "Altın, nakit ve ticaret mallarında 1/40 (%2.5); sulanmayan toprak ürünlerinde 1/10 (öşür) oranını hesaplar.",
         ["Oranlar", "1/40", "Öşür", "Madenler"],
         "LGS'de çıkan matematiksel zekat hesaplama problemleri çözülür.",
         "Toprak mahsullerinden alınan zekata ne ad verilir ve masrafsız tarlada oranı nedir?",
         "Öşür adı verilir; masrafsız doğal sularla sulanan ürünlerde onda bir (1/10) oranında verilir."),
        
        ("Zekat ve Sadaka", "Sadaka ve Çeşitleri", "Geniş Kapsamlı İyilik: Tebessümden Ağaç Dikmeye",
         "Maddi-manevi her iyiliğin sadaka olduğunu; bir tebessümün, yoldaki taşı kaldırmanın sadaka sayıldığını öğrenir.",
         ["Sadaka", "Tebessüm", "Sadaka-i Cariye", "Fıtır Sadakası"],
         "Fitre (fıtır sadakası) ve sadaka-i cariye (köprü, okul, çeşme) farkları incelenir.",
         "Sadaka-i Cariye ne demektir?",
         "İnsanın vefatından sonra da amel defterine sevap yazdıran cami, okul, çeşme gibi kalıcı hayır eserleridir."),
        
        ("Zekat ve Sadaka", "Bir Sure ve Peygamber Öğreniyorum", "Ma'un Suresi ve Hz. Şuayb",
         "Ma'un suresindeki gösteriş yapan ve yetimi itip kakanların eleştirisini ve Hz. Şuayb'ın ölçü-tartı uyarısını kavrar.",
         ["Ma'un Suresi", "Hz. Şuayb", "Ölçü ve Tartı", "Riya"],
         "Yetimin hakkını gözetmeyen namaz kılıcının samimiyetsizliği tahlil edilir.",
         "Ma'un suresinde namaz kıldıkları halde kınanan kimselerin özellikleri nelerdir?",
         "Namazlarını ciddiye almayan, ibadetlerinde gösteriş (riya) yapan ve ufacık bir yardıma dahi engel olanlardır."),

        # Ünite 3: Din ve Hayat (16-22)
        ("Din ve Hayat", "Dinin Temel Gayesi (Zarurat-ı Hamse)", "İslam'ın Korunmasını Emrettiği 5 Temel İlke",
         "Canın, aklın, dinin, malın ve neslin korunması (Zarurat-ı Hamse) ilkelerini güncel hukukla bağdaştırır.",
         ["Zarurat-ı Hamse", "Can Emniyeti", "Akıl Emniyeti", "Nesil Emniyeti"],
         "Her dinî yasağın bu 5 temel haktan birini koruduğu örneklerle çözülür.",
         "Trafik kurallarına uymak ve iş güvenliği tedbirleri almak hangi temel hakkın korunması kapsamındadır?",
         "Canın korunması kapsamındadır."),
        
        ("Din ve Hayat", "Malın ve Neslin Korunması", "Haksız Kazanç, İsraf ve Aile Kurumu",
         "Rüşvet, hırsızlık, faiz ve israfın haram kılınmasının malı; meşru evliliğin ise nesli koruduğunu analiz eder.",
         ["Malın Korunması", "Neslin Korunması", "Faiz", "Helal Lokma"],
         "Aile kurumunun toplumun yapı taşı olduğu işlenir.",
         "İslam dininde faiz, karaborsacılık ve hırsızlığın kesin olarak yasaklanması hangi hakkı korur?",
         "Malın korunması hakkını güvenceye alır."),
        
        ("Din ve Hayat", "1. Dönem Sonu Sentezi", "LGS 1. Dönem Din Kültürü Denemesi",
         "Kader, Zekat ve Din-Hayat ünitelerinden oluşan 20 soruluk tam LGS denemesi uygular.",
         ["LGS Deneme", "Sentez", "Tam Puan", "Kazanım"],
         "Net analizi ve eksik konu tespiti yapılır.",
         "Bir LGS Din Kültürü sorusunda 'özgürlük ve sorumluluk' varsa hangi kavram aranmalıdır?",
         "İnsanın cüzi iradesi aranmalıdır."),
        
        ("Din ve Hayat", "1. Dönem Sonu Karnesi", "LGS Yarıyıl Tatil Çalışma Stratejisi",
         "İlk dönemin netlerini değerlendirir ve 15 günlük tatil LGS soru hedefi koyar.",
         ["Karne", "LGS Hedef", "Motivasyon", "Strateji"],
         "Öğrencilere tatil çalışma planı sunulur.",
         "LGS Din Kültürü'nde 10'da 10 yapmanın en önemli kuralı nedir?",
         "Kavramları ezberlemekle kalmayıp ayet ve hadis mealleriyle olaylar arasında doğru bağ kurabilmektir."),
        
        ("Din ve Hayat", "Din, Birey ve Toplum", "Dinin Bireysel ve Toplumsal İşlevleri",
         "Dinin insana hayat gayesi sunduğunu, toplumsal barış ve adalet duygusunu nasıl inşa ettiğini kavrar.",
         ["Hayat Gayesi", "İç Huzur", "Toplumsal Birlik", "Vicdan"],
         "Ahlak kurallarının vicdan mekanizmasıyla güçlenmesi anlatılır.",
         "Dinin bireye kazandırdığı en mühim duygu nedir?",
         "Yalnız olmadığı, hayatının anlamsız olmadığı ve yaptıklarının bir hesabı olacağı bilinciyle kazandığı iç huzurdur."),
        
        ("Din ve Hayat", "Bir Peygamber Tanıyorum", "Hz. Yusuf Kıssası",
         "Ahsenü'l-Kasas (kıssaların en güzeli) Hz. Yusuf'un kuyu, zindan ve saraydaki iffet ve affediciliğini öğrenir.",
         ["Hz. Yusuf", "Ahsenü'l-Kasas", "İffet", "Sabır"],
         "Kardeşlerini affeden yüce gönüllülüğü üzerinde durulur.",
         "Hz. Yusuf zindana atılmayı saraydaki haram teklife neden tercih etmiştir?",
         "Allah korkusu, iffeti ve günaha girmektense zindandaki sıkıntıya sabretmeyi üstün tuttuğu için."),
        
        ("Din ve Hayat", "Bir Sure Öğreniyorum", "Asr Suresi ve Zaman Yönetimi",
         "Asr suresinin LGS bağlamında iman, salih amel, hak ve sabır tavsiyesini analiz eder.",
         ["Asr", "Zaman", "Kayıp", "Kazanç"],
         "Sınav hazırlığında zamanın kıymetiyle Asr suresi bağdaştırılır.",
         "Asr suresinde geçen 'hüsran' tehlikesinden kurtulmanın reçetesi nedir?",
         "İman etmek, faydalı ve güzel işler (salih amel) yapmak, hakkı ve sabrı tavsiye etmektir."),

        # Ünite 4: Hz. Muhammed'in Örnekliği (23-29)
        ("Hz. Muhammed'in Örnekliği", "Hz. Muhammed'in Doğruluğu ve Güvenilirliği", "Muhammedü'l-Emin",
         "Müşriklerin dahi Peygamberimize değerli eşyalarını emanet ettiğini ve dürüstlüğünü çözümler.",
         ["Muhammedü'l-Emin", "Doğruluk", "Emanet", "Şahsiyet"],
         "Hicret gecesi emanetleri teslim etmesi için Hz. Ali'yi yatağına bırakması işlenir.",
         "Peygamber Efendimiz düşmanlarının bile emanetlerini neden korumuştur?",
         "Çünkü güvenilirlik İslam ahlakının temelidir; düşmana karşı bile emanete hıyanet edilemez."),
        
        ("Hz. Muhammed'in Örnekliği", "Hz. Muhammed'in Merhameti ve Affediciliği", "Alemlere Rahmet Elçi",
         "Bedir esirlerine muamelesi, Taiflilere beddua etmeyip dua edişi ve çocuk sevgisini kavrar.",
         ["Merhamet", "Af", "Şefkat", "Taif"],
         "Uhud savaşında dişi kırıldığında bile müşriklere af dilemesi anlatılır.",
         "Peygamberimizin Taif'te taşlandığı halde meleklere 'Hayır, umarım onların soyundan Allah'a ibadet edenler çıkar' demesi neyi gösterir?",
         "Onun intikam peşinde olmadığını, sonsuz bir merhamet ve insan sevgisiyle dolu olduğunu gösterir."),
        
        ("Hz. Muhammed'in Örnekliği", "İstişareye Verdiği Önem", "Ortak Akıl ve Danışma",
         "Uhud ve Hendek savaşlarında ashabıyla fikir alışverişinde bulunup gençlerin kararına uymasını tahlil eder.",
         ["İstişare", "Ortak Akıl", "Selman-ı Farisi", "Demokrasi"],
         "Hendek kazma fikrini kabul etmesi ve ortak aklın bereketi vurgulanır.",
         "Peygamberimiz vahiy almasına rağmen neden ashabıyla istişare ederdi?",
         "Ümmetine örnek olmak, ortak aklı işletmek ve insanlara değer verdiğini göstermek için."),
        
        ("Ara Tatil", "2. Dönem Ara Tatil Tekrarı", "LGS Örnek Sorular Kampı",
         "Örnek MEB LGS soruları üzerinden Hz. Muhammed'in örnekliği ünitesini pekiştirir.",
         ["Ara Tatil", "LGS Kampı", "Siyer", "Soru Çözümü"],
         "Paragraftan ana fikir çıkarma teknikleri gösterilir.",
         "LGS sorularında istişare kavramı hangi durumlarla sorulur?",
         "Peygamberimizin bir konuda karar verirken arkadaşlarına, eşine danışması durumlarıyla sorulur."),
        
        ("Hz. Muhammed'in Örnekliği", "Cesaret ve Kararlılığı", "Hak Yolunda Tavizsiz Duruş",
         "'Güneşi sağ elime, ayı sol elime koysalar bu davadan dönmem' sözündeki sarsılmaz sebatı öğrenir.",
         ["Cesaret", "Kararlılık", "Sebat", "Tavizsizlik"],
         "Bedir ve Huneyn savaşlarında gösterdiği liderlik cesareti aktarılır.",
         "Peygamberimizin 'Güneşi sağ elime, ayı sol elime koysalar...' sözü hangi özelliğini yansıtır?",
         "Davasındaki tavizsiz kararlılığını ve inancına olan sarsılmaz bağlılığını yansıtır."),
        
        ("Hz. Muhammed'in Örnekliği", "Hakkı Gözetmedeki Hassasiyeti ve Kul Hakkı", "Adalet Örneği Peygamber",
         "'Hırsızlık yapan kızım Fatıma da olsa elini keserdim' uyarısıyla iltimas ve torpili reddini analiz eder.",
         ["Adalet", "Kul Hakkı", "Torpil Karşıtlığı", "Eşitlik"],
         "Mahzum kabilesinden soylu kadının affı istendiğinde gösterdiği adalet tepkisi işlenir.",
         "Peygamberimizin kızı Fatıma örneğiyle verdiği ders nedir?",
         "Adalet ve hukuk önünde herkesin eşit olduğu; soy, makam veya akrabalığın iltimas vesilesi olamayacağıdır."),
        
        ("Hz. Muhammed'in Örnekliği", "Bir Sure Öğreniyorum", "Kureyş Suresi ve Nimetin Şükrü",
         "Kureyş suresinde hatırlatılan güven ortamı ve rızık nimetlerine karşı Kâbe'nin Rabbine kulluğu öğrenir.",
         ["Kureyş Suresi", "Emniyet", "Rızık", "Şükür"],
         "Korkudan emin kılan ve açlıktan doyuran Allah'a ibadet bilinci pekişir.",
         "Kureyş suresinde Allah'ın Kureyşlilere lütfettiği iki büyük nimet nedir?",
         "Onları açlıktan doyurması ve her türlü korkudan emin kılmasıdır."),

        # Ünite 5: Kur'an-ı Kerim ve Özellikleri (30-36)
        ("Kur'an-ı Kerim ve Özellikleri", "İslam Dininin Ana Kaynakları", "Kur'an ve Sünnet Bütünlüğü",
         "Dini doğru anlamada Kur'an'ın muhkem ayetleri ile sünnetin kılavuzluğunun ayrılmazlığını çözer.",
         ["Ana Kaynak", "Kur'an", "Sünnet", "Bütünlük"],
         "Hurafeler ve bidatlerin dinden ayıklanması incelenir.",
         "İslam dininin iki temel ana kaynağı nedir?",
         "Kur'an-ı Kerim ve Peygamber Efendimizin sünnetidir."),
        
        ("Kur'an-ı Kerim ve Özellikleri", "Kur'an-ı Kerim'in Ana Konuları", "İnanç, İbadet, Ahlak, Muamelat, Kıssalar",
         "Kur'an'ın bu beş temel alandaki hükümlerini ve hayatı tanzim edişini gruplandırır.",
         ["Muhteva", "İnanç", "İbadet", "Ahlak", "Muamelat"],
         "LGS sınıflandırma soruları çözülür.",
         "Kur'an'daki 'muamelat' kavramı neyi kapsar?",
         "İnsanların birbiriyle olan hukuki, ticari, ailevi ve toplumsal ilişkilerini düzenleyen kuralları kapsar."),
        
        ("Kur'an-ı Kerim ve Özellikleri", "Kur'an'ın Temel Özellikleri", "Yol Gösterici (Hüden), Aydınlatıcı (Nur), Şifa Olması",
         "Kur'an'ın akla, tefekküre ve araştırmaya verdiği hayati önemi ayetlerle kanıtlar.",
         ["Rehber", "Tefekkür", "Akıl", "Nur", "Şifa"],
         "'Hâlâ akletmez misiniz?', 'Hiç düşünen yok mu?' ayetlerinin mesajı işlenir.",
         "Kur'an-ı Kerim'in en çok tekrar ettiği akli uyarı nedir?",
         "İnsanları aklını kullanmaya, evrendeki ayetler üzerinde düşünmeye ve körü körüne taklitten uzak durmaya çağırmasıdır."),
        
        ("Kur'an-ı Kerim ve Özellikleri", "Bir Peygamber Tanıyorum", "Hz. Nuh Kıssası ve Kararlılık",
         "Hz. Nuh'un 950 yıllık tebliğ sabrı, gemi inşası ve tufan imtihanındaki metanetini inceler.",
         ["Hz. Nuh", "Tufan", "Gemi", "Sabır"],
         "Oğluna karşı olan baba şefkati ve ilahi adaletin kan bağı dinlememesi işlenir.",
         "Hz. Nuh kıssasında gemiye binmeyen oğlu bize neyi öğretir?",
         "Kurtuluşun peygamber soyundan gelmekle değil, bizzat iman edip salih amel işlemekle mümkün olduğunu öğretir."),
        
        ("Kur'an-ı Kerim ve Özellikleri", "LGS 1. Genel Tekrar Kampı", "Kader, Zekat ve Din-Hayat Provasi",
         "Tüm dönem ünitelerini kapsayan MEB çıkmış sorular ve LGS prova denemesi çözer.",
         ["LGS Prova", "Genel Tekrar", "MEB Soruları", "Strateji"],
         "Zaman yönetimi ve optik form kodlama taktikleri verilir.",
         "LGS Din Kültürü sorularında zaman kazandıran en etkili yöntem nedir?",
         "Önce soru kökünü okumak, ardından öncüllerdeki kavram eşleştirmelerine dikkat etmektir."),
        
        ("Kur'an-ı Kerim ve Özellikleri", "LGS 2. Genel Tekrar Kampı", "Hz. Muhammed ve Kur'an Provasi",
         "Siyer ve Kur'an konularından 10/10 tam hedefli son rötuş denemesini tamamlar.",
         ["Tam İsabet", "LGS Rötuş", "Deneme", "Siyer"],
         "Tüm peygamberlerin ortak vasıfları tablosu tekrar edilir.",
         "Tüm peygamberlerin tevhid davasındaki ortak sloganı nedir?",
         "'Ey kavmim! Yalnızca Allah'a kulluk edin, sizin O'ndan başka hiçbir ilahınız yoktur.'"),
        
        ("Kur'an-ı Kerim ve Özellikleri", "LGS Final Sınavı ve Mezuniyet", "LGS Başarı Duası ve Moral Kampı",
         "Ortaokul Din Kültürü serüvenini tam puan motivasyonu ve ahlaki değerler bilinciyle tamamlar.",
         ["LGS Final", "Başarı", "Mezuniyet", "Güzel Ahlak"],
         "Sınav kaygısını azaltma ve zihin ferahlığı çalışması yapılır.",
         "LGS sınavında ve hayatta başarının değişmez formülü nedir?",
         "Azimle çalışmak, dürüstlükten ödün vermemek ve neticeyi huzurla Allah'a tevekkül etmektir.")
    ]
    assert len(u) == 36, f"Din 8 count: {len(u)}"
    return {
        'title': '8. Sınıf',
        'subtitle': 'LGS Din Kültürü ve Ahlak Bilgisi (Sınav Odaklı)',
        'badge': 'LGS Din Kültürü',
        'weeks': _make_weeks(u, 'DİN.8')
    }

print("Loading grades for Din Kültürü...")
g5 = get_din_5()
g6 = get_din_6()
g7 = get_din_7()
g8 = get_din_8()

print(f"Week counts: G5={len(g5['weeks'])}, G6={len(g6['weeks'])}, G7={len(g7['weeks'])}, G8={len(g8['weeks'])}")

grades_data = {
    5: g5,
    6: g6,
    7: g7,
    8: g8,
}

output_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'lib', 'data', 'subjects', 'din_kulturu_data.dart'
)

generate_dart_file(
    subject_id='din',
    subject_name='Din Kültürü ve Ahlak Bilgisi',
    short_code='DİN',
    description='İnanç, İbadet, Ahlak, Peygamberler Tarihi ve İslam Düşüncesi',
    icon_name='menu_book_rounded',
    primary_hex='0xFF059669', # Emerald Green
    accent_hex='0xFF10B981',
    grades_data=grades_data,
    output_path=output_path
)

print("Din Kültürü generated successfully!")
