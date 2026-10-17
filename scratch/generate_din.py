# -*- coding: utf-8 -*-
"""
Generates 36 weeks for Din Kültürü ve Ahlak Bilgisi (Grades 5 Maarif, 6, 7, 8 LGS)
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from curriculum_builder import generate_dart_file

def _make_weeks(units, prefix):
    weeks_data = []
    for i, u in enumerate(units):
        code = f"{prefix}.{i+1}"
        weeks_data.append({
            'theme': u[0], 'subTheme': u[1], 'code': code, 'title': u[2], 'description': u[3],
            'process': ['a) ' + u[3][:30] + ' kavrar.', 'b) Hayatına tatbik eder.'],
            'concepts': [u[1], 'Ahlak', 'İnanç', 'İbadet'],
            'skills': ['Değerler Eğitimi', 'Ahlaki Muhakeme', 'Kültürel Farkındalık'],
            'pedagogical': 'Ayet, hadis mealleri ve erdem odaklı örnek olaylar incelenir.',
            'context': 'Din Kültürü ve Ahlak Bilgisi',
            'question': f"{u[1]} konusunun birey ve toplum ahlakı açısından kazandırdığı en önemli erdem nedir?",
            'solution': f"{u[2]} bilinciyle erdemli, dürüst ve sorumluluk sahibi bir insan olmaktır.",
            'weeklyGoal': u[2], 'evaluation': 'Haftalık ahlak ve kazanım değerlendirme föyü'
        })
    return weeks_data

def build_din_5():
    # 5. Sınıf Türkiye Yüzyılı Maarif Modeli (5 Ünite)
    units = [
        # Ünite 1: Allah İnancı (1-7)
        ("Allah İnancı", "Evrendeki Mükemmel Düzen", "Evrendeki Düzen ve Yaratılış Gayesi", "Gök cisimlerinin, mevsimlerin ve canlıların yaratılışındaki kusursuz ahengi gözlemleyerek yaratıcının varlığını kavrar."),
        ("Allah İnancı", "Allah Vardır ve Birdir (Tevhid)", "Tevhid İnancı ve Allah'ın Sıfatları", "İslam inancının temeli olan tevhid (Allah'ın birliği ve eşi benzeri olmadığı) ilkesini açıklar."),
        ("Allah İnancı", "Allah Yaradandır ve Rızık Verendir", "Hâlık ve Rezzak İsimleri", "Her şeyin yaratıcısının ve yaşatanının Allah olduğunu örneklerle kavrar."),
        ("Allah İnancı", "Allah Her Şeyi İşitir ve Görür", "Semi ve Basar Sıfatları", "Gizli ve açık her şeyi bilen Allah'ın huzurunda olduğu bilinciyle dürüstlük erdemini pekiştirir."),
        ("Allah İnancı", "Allah'ın Güzel İsimleri (Esma-i Hüsna)", "Esma-i Hüsna'dan Örnekler", "Rahman, Rahim, Vedûd, Selam isimlerinin anlamına uygun merhametli ve sevgi dolu davranışlar sergiler."),
        ("Allah İnancı", "Dua İbadeti ve Önemi", "Allah ile İletişim: Dua ve Şükür", "Duanın insanın iç huzuruna katkısını ve yalnızca Allah'a sığınma bilincini açıklar."),
        ("Allah İnancı", "Bir Sure Öğreniyorum: İhlas Suresi", "İhlas Suresi ve Anlamı", "İhlas suresinin okunuşunu, anlamını ve tevhid inancını nasıl özetlediğini modeller."),

        # Ünite 2: Namaz (8-14)
        ("Namaz", "Allah'ın Huzurunda Olmak: Namaz", "Namaz İbadetinin Anlam ve Önemi", "Namazın dinin direği olduğunu, insanı kötülüklerden alıkoyduğunu ve günde beş vakit huzur verdiğini kavrar."),
        ("Namaz", "Namazın Şartları ve Hazırlık", "Abdestin Alınışı ve Namazın Dışındaki Şartlar", "Hadesten ve necasetten taharet, setr-i avret, istikbal-i kıble, vakit ve niyet şartlarını açıklar."),
        ("Ara Tatil", "1. Dönem Ara Tatili", "1. Dönem Ara Tatili Tekrarı", "Allah inancı ve namaz konuları tekrar edilir."),
        ("Namaz", "Namazın Rükunları (İçindeki Şartlar)", "İftitah Tekbiri, Kıyam, Kıraat, Rükû, Secde ve Kade-i Ahire", "Namazın kılınışındaki temel rükunları uygulamalı olarak öğrenir."),
        ("Namaz", "Cemaatle Namaz ve Cuma Namazı", "Birlik ve Beraberlik: Cemaatle Namaz", "Cuma, bayram ve cenaze namazlarının toplumsal dayanışma ve kaynaşmaya katkısını değerlendirir."),
        ("Namaz", "Ezan ve Kamet", "Günde Beş Vakit Çağrı: Ezan", "Ezanın sözlerini, anlamını ve Müslümanların hürriyet ve bağımsızlık simgesi olduğunu kavrar."),
        ("Namaz", "Bir Dua Öğreniyorum: Tahiyyat Duası", "Tahiyyat Duası ve Anlamı", "Namazın oturuşlarında okunan Tahiyyat duasının anlamını ve Miraç olayındaki önemini modeller."),

        # Ünite 3: Kur'an-ı Kerim (15-21)
        ("Kur'an-ı Kerim", "Son İlahi Kitap Kur'an", "Kur'an-ı Kerim'in İndiriliş Süreci", "Kadir Gecesi'nde Hira Mağarası'nda başlayan vahiy sürecini ve peygambere peyderpey indirilişini açıklar."),
        ("Kur'an-ı Kerim", "Kur'an'ın İç Düzeni", "Ayet, Sure ve Cüz Kavramları", "6666 ayet, 114 sure ve 30 cüzden oluşan Kur'an-ı Kerim'in sayfa ve iç tertibini inceler."),
        ("Kur'an-ı Kerim", "Kur'an'ın Temel Konuları", "İnanç, İbadet, Ahlak ve Muamelat", "Kur'an'ın insanlara yol gösteren temel konu başlıklarını örnek ayetlerle açıklar."),
        ("Kur'an-ı Kerim", "1. Dönem Sonu Sentezi", "1. Dönem Din Kültürü Değerlendirmesi", "İnanç, namaz ve Kur'an ünitelerini içeren genel tekrar yapar."),
        ("Kur'an-ı Kerim", "1. Dönem Karnesi", "1. Dönem Final Değerlendirmesi", "Kazanım ölçme testini tamamlar."),
        ("Kur'an-ı Kerim", "Kur'an Okuma ve Anlama Ahlakı", "Kur'an'ı Anlayarak Yaşamak", "Kur'an'ın sadece lafzını okumakla yetinmeyip hayat rehberi edinmenin önemini savunur."),
        ("Kur'an-ı Kerim", "Bir Sure Öğreniyorum: Kevser Suresi", "Kevser Suresi ve Anlamı", "Kevser suresinin anlamını ve Allah'ın nimetlerine karşı şükür bilincini modeller."),

        # Ünite 4: Peygamber Kıssaları (22-29)
        ("Peygamber Kıssaları", "Kur'an'da Adı Geçen Peygamberler", "Peygamberlik Kurumu ve Görevleri", "Peygamberlerin insanlara doğru yolu göstermek için gönderilen elçiler olduğunu kavrar."),
        ("Peygamber Kıssaları", "Hz. İbrahim'in Tevhid Mücadelesi", "Hz. İbrahim ve Aklıyla Yaratıcıyı Bulması", "Güneş, ay ve yıldızların batmasından hareketle batmayan tek yaratıcıya ulaşma kıssasını analiz eder."),
        ("Peygamber Kıssaları", "Hz. İsmail ve Teslimiyet", "Hz. İsmail Kıssası ve Kâbe'nin İnşası", "Hz. İbrahim ve oğlu Hz. İsmail'in Kâbe'yi inşa edişini ve teslimiyet erdemini inceler."),
        ("Peygamber Kıssaları", "Doğruluk ve Güvenilirlik Erdemi", "Peygamberlerin Sıdk ve Emanet Sıfatları", "Asla yalan söylemeyen ve güvenilir olan peygamberlerin ahlakını örnek alır."),
        ("Peygamber Kıssaları", "Sabır ve Adalet Örnekleri", "Hz. Eyyüb'ün Sabrı ve Adalet", "Zorluklar karşısında sabretmenin ve haksızlığa karşı adaleti savunmanın değerini açıklar."),
        ("Peygamber Kıssaları", "Merhamet ve Affedicilik", "Peygamberlerin Sevgi ve Barış Dili", "İntikam yerine bağışlamayı tercih eden peygamber ahlakını modeller."),
        ("Ara Tatil", "2. Dönem Ara Tatili", "Peygamber Kıssaları Kampı", "Kıssalar ve ahlak değerleri soruları çözer."),
        ("Peygamber Kıssaları", "Bir Dua Öğreniyorum: Rabbena Duaları", "Rabbena Âtina ve Rabbenağfirli Duaları", "Dünya ve ahiret iyiliği dileyen Rabbena dualarının anlamını öğrenir."),

        # Ünite 5: Mimarimizde Dinî Motifler (30-36)
        ("Mimarimizde Dinî Motifler", "Dinin Sanat ve Mimarimize Etkisi", "İslam Sanatı ve Estetik Anlayış", "Tevhid inancının cami, medrese, köprü ve kervansaray mimarisine yansımasını inceler."),
        ("Mimarimizde Dinî Motifler", "Camileri Tanıyalım", "Caminin Bölümleri: Kubbe, Minare, Mihrap, Minber, Kürsü, Şadırvan", "Cami mimarisinin iç ve dış unsurlarını görevleriyle birlikte tanır."),
        ("Mimarimizde Dinî Motifler", "Tarihî Cami Örneklerimiz", "Süleymaniye, Sultanahmet, Selimiye ve Bursa Ulu Cami", "Osmanlı ve Selçuklu döneminden kalan şaheser camilerin kültürel değerini takdir eder."),
        ("Mimarimizde Dinî Motifler", "Mimarimizde Merhamet: Kuş Evleri", "Tarihî Yapılardaki Kuş Köşkleri ve Merhamet Medeniyeti", "Ecdadımızın cami ve kütüphane duvarlarına yaptığı zarif kuş evleriyle hayvan sevgisini keşfeder."),
        ("Mimarimizde Dinî Motifler", "Musiki ve Edebiyatımızda Dinî Motifler", "İlahiler, Mevlid ve Tasavvuf Musikisi", "Kültürümüzde ezan, sala ve naatların dinî ve edebî değerini değerlendirir."),
        ("Mimarimizde Dinî Motifler", "Maarif Modeli Din Kültürü Yıl Sonu Sentezi", "5. Sınıf Din Kültürü Portfolyo Sergisi", "Yıl boyunca öğrenilen inanç, ibadet, ahlak ve sanat kazanımlarını bütünleştirir."),
    ]
    return {
        'title': '5. Sınıf',
        'subtitle': 'Türkiye Yüzyılı Maarif Modeli (5 Ünite)',
        'badge': 'Maarif Modeli ✨',
        'weeks': _make_weeks(units, 'DİN.5')
    }

def build_din_6():
    # 6. Sınıf Din Kültürü (36 Hafta)
    units = [
        ("Peygamber ve İlahi Kitap İnancı", "Peygamberlere İman", "Allah'ın Elçileri ve Tebliğ Görevi", "Peygamberlerin sıfatlarını (sıdk, emanet, fetanet, ismet, tebliğ) ve vahyin amacını açıklar.") for _ in range(7)
    ] + [
        ("Namaz İbadeti", "Namazın Önemi ve Kılınışı", "Beş Vakit Namaz, Cemaat ve Birlik", "Namazın insanın kötülüklerden uzak durmasına katkısını ve cemaat ruhunu açıklar.") for _ in range(7)
    ] + [
        ("Zararlı Alışkanlıklar", "Zararlı Alışkanlıklardan Korunma", "Alkol, Kumar, Tütün ve Bağımlılıklar", "İslam dininin akıl, can ve mal emniyetini koruma ilkesi doğrultusunda zararlı maddelerden uzak durmayı savunur.") for _ in range(7)
    ] + [
        ("Hz. Muhammed'in Hayatı", "Peygamberimizin Hayat Çizgisi", "Medine Dönemi, Hicret ve Veda Hutbesi", "Hicretin İslam tarihindeki dönüm noktasını ve Veda Hutbesi'ndeki evrensel insan hakları ilkelerini inceler.") for _ in range(8)
    ] + [
        ("Temel Değerlerimiz", "Kültürümüzü Birleştiren Değerler", "Vatan Sevgisi, Şehitlik ve Gazilik", "Milli ve manevi değerlerimizin bağımsızlığımız ve milletimizin bekası için önemini modeller.") for _ in range(7)
    ]
    return {
        'title': '6. Sınıf',
        'subtitle': 'Ortaokul 2. Kademe Din Kültürü',
        'badge': 'Ortaokul Din',
        'weeks': _make_weeks(units, 'DİN.6')
    }

def build_din_7():
    # 7. Sınıf Din Kültürü (36 Hafta)
    units = [
        ("Melek ve Ahiret İnancı", "Görülmeyen Âlem ve Melekler", "Dört Büyük Melek ve Ahiret Hayatı", "Cebrail, Mikail, İsrafil, Azrail ve ahirette hesap verme bilincinin ahlak üzerindeki etkisini açıklar.") for _ in range(8)
    ] + [
        ("Hac ve Kurban", "Hac İbadeti ve Kurban", "İhram, Tavaf, Vakfe ve Paylaşma", "Haccın farzlarını, Kâbe etrafındaki eşitlik ve kardeşlik duygusunu ve kurbanın cömertlik boyutunu modeller.") for _ in range(7)
    ] + [
        ("Ahlaki Davranışlar", "Güzel Ahlak ve Erdemler", "Adalet, Dostluk, Dürüstlük, Öz Denetim", "İslam ahlakının temel erdemlerini ve kul hakkına riayet etmenin önemini açıklar.") for _ in range(7)
    ] + [
        ("Allah'ın Kulu ve Elçisi Hz. Muhammed", "Hz. Muhammed'in Örnek Hayatı", "Peygamberimizin İnsani ve Peygamberlik Yönü", "Hz. Muhammed'in bir insan olarak hayatını ve Kur'an'ı açıklayıcı (tebyin) rolünü değerlendirir.") for _ in range(7)
    ] + [
        ("İslam Düşüncesinde Yorumlar", "Mezhepler ve Hoşgörü", "İnanç ve Fıkıh Mezhepleri, Tasavvuf", "Mevlevilik, Bektaşilik ve fıkhi mezheplerin İslam düşüncesindeki zenginlik olduğunu savunur.") for _ in range(7)
    ]
    return {
        'title': '7. Sınıf',
        'subtitle': 'Ortaokul 3. Kademe Din Kültürü',
        'badge': 'Ortaokul Din',
        'weeks': _make_weeks(units, 'DİN.7')
    }

def build_din_8():
    # 8. Sınıf LGS Din Kültürü ve Ahlak Bilgisi (36 Hafta)
    units = [
        ("Kader İnancı", "Kader ve Kaza Kavramları", "Evrenin Yasaları: Fiziksel, Biyolojik, Toplumsal", "Allah'ın her şeyi bir ölçüye göre yarattığını; fiziksel, biyolojik ve toplumsal yasaların değişmezliğini çözümler.") for _ in range(8)
    ] + [
        ("Zekat ve Sadaka", "Paylaşma ve Yardımlaşma İbadeti", "Zekat, Sadaka, Sadaka-i Cariye ve İnfak", "Nisap miktarını, kimlere zekat verileceğini, toplumsal gelir adaletini ve köprü, çeşme gibi kalıcı sadaka-i cariyeyi açıklar.") for _ in range(7)
    ] + [
        ("Din ve Hayat", "Dinin Temel Gayesi (Zarurat-ı Hamse)", "Canın, Aklın, Dinin, Malın ve Neslin Korunması", "İslam'ın beş temel emniyeti koruma prensibini kanunlar ve insan haklarıyla ilişkilendirir.") for _ in range(7)
    ] + [
        ("Hz. Muhammed'in Örnekliği", "Peygamberimizin Örnek Ahlakı", "İstişare, Merhamet, Cesaret ve Ahde Vefa", "Bedir ve Uhud savaşlarında ashabıyla istişare eden, sözünde duran lider peygamber vasfını modeller.") for _ in range(7)
    ] + [
        ("Kur'an-ı Kerim ve Özellikleri", "Kur'an'ın Ana Konuları ve LGS Final Kampı", "Kur'an'ın İnsana Rehberliği ve 10/10 LGS Provası", "Akla ve ilme verdiği değeri; Asr suresini ve LGS tam deneme soru çözümünü tamamlar.") for _ in range(7)
    ]
    return {
        'title': '8. Sınıf',
        'subtitle': 'LGS Din Kültürü ve Ahlak Bilgisi (Sınav Odaklı)',
        'badge': 'LGS Din Kültürü',
        'weeks': _make_weeks(units, 'DİN.8')
    }

print("Din Kültürü builder compiled.")
