# -*- coding: utf-8 -*-
"""
Generates complete 36 weeks for:
1. Sosyal Bilgiler & T.C. İnkılap Tarihi (5 Maarif, 6, 7, 8 LGS)
2. Din Kültürü ve Ahlak Bilgisi (5 Maarif, 6, 7, 8 LGS)
3. İngilizce (5, 6, 7, 8 LGS)
4. Bilişim Teknolojileri ve Yazılım (5, 6)
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from curriculum_builder import generate_dart_file, DATES

# ==============================================================================
# 1. SOSYAL BİLGİLER
# ==============================================================================
def build_sosyal_5():
    # 5. Sınıf Türkiye Yüzyılı Maarif Modeli (6 Öğrenme Alanı)
    # 1. Alan: Birlikte Yaşamak (1-6)
    # 2. Alan: Evimiz Dünya (7-12)
    # 3. Alan: Ortak Mirasımız (13-18)
    # 4. Alan: Yaşayan Demokrasimiz (19-24)
    # 5. Alan: Hayatımızdaki Ekonomi (25-30)
    # 6. Alan: Teknoloji ve Sosyal Bilimler (31-36)
    units = [
        ("Birlikte Yaşamak", "Gruplar ve Rollerimiz", "SB.5.1.1", "Aile ve Yakın Çevredeki Gruplar ve Roller", "Aile, okul ve arkadaş gruplarındaki rollerini ve sorumluluklarını açıklar."),
        ("Birlikte Yaşamak", "Hak ve Sorumluluklar", "SB.5.1.2", "Haklarımız, Sorumluluklarımız ve Çocuk Hakları", "Çocuk Haklarına Dair Sözleşme kapsamındaki temel haklarını ve ödevlerini kavrar."),
        ("Birlikte Yaşamak", "Birlikte Yaşama Kültürü", "SB.5.1.3", "Farklılıklara Saygı ve Toplumsal Uyum", "Toplumdaki farklı kültürel ve bireysel özelliklere saygı göstererek bir arada yaşamanın önemini açıklar."),
        ("Birlikte Yaşamak", "Yardımlaşma ve Dayanışma", "SB.5.1.4", "Toplumsal Dayanışma ve Kızılay/AFAD Faaliyetleri", "Doğal afetlerde ve sosyal yaşamda yardımlaşmanın toplumsal bağları güçlendirdiğini savunur."),
        ("Birlikte Yaşamak", "Ön Yargıları Kırma", "SB.5.1.5", "Ön Yargıların Farkına Varma ve Empati", "Kalıp yargı ve ön yargıların toplumsal ilişkilere zararını örneklerle analiz eder."),
        ("Birlikte Yaşamak", "1. Tema Değerlendirme", "SB.5.1.6", "Birlikte Yaşamak Öğrenme Alanı Sentezi", "Grup, rol, hak ve yardımlaşma ilkelerini içeren durum analizleri yapar."),

        ("Evimiz Dünya", "Yaşadığımız İlin Göreceli Konumu", "SB.5.2.1", "Yaşadığımız Yerin Harita Üzerindeki Konumu", "Yaşadığı ilin fiziki ve beşerî özelliklerini harita üzerinde gösterir ve göreceli konumunu açıklar."),
        ("Evimiz Dünya", "Doğal ve Beşerî Çevre", "SB.5.2.2", "Çevremizdeki Dağlar, Ovalar, Akarsular ve Değişim", "Yaşadığı yerdeki doğal varlıkları ve insan eliyle yapılan beşerî unsurları ayırt eder."),
        ("Evimiz Dünya", "İklim ve İnsan Faaliyetleri", "SB.5.2.3", "İklimin Konut, Giyim ve Tarıma Etkisi", "Türkiye'deki Karasal, Akdeniz ve Karadeniz iklim tiplerinin günlük yaşama yansımalarını açıklar."),
        ("Ara Tatil", "1. Dönem Ara Tatili", "SB.5.GENEL.1", "Birlikte Yaşamak ve Dünya Temaları Tekrarı", "Harita okuryazarlığı ve çocuk hakları kazanımlarını pekiştirir."),
        ("Evimiz Dünya", "Afetler ve Afet Bilinci", "SB.5.2.4", "Deprem, Sel, Heyelan Afetleri ve Önlemler", "Doğal afetlerin olası etkilerini ve afet öncesi, sırası ve sonrasında yapılması gerekenleri modeller."),
        ("Evimiz Dünya", "Komşularımız ve Sınırlarımız", "SB.5.2.5", "Türkiye'nin Komşu Ülkeleri ve İlişkiler", "Türkiye'nin kara ve deniz komşularını (Yunanistan, Bulgaristan, Gürcistan, Azerbaycan, İran, Irak, Suriye) haritada gösterir."),

        ("Ortak Mirasımız", "Somut Kültürel Miras", "SB.5.3.1", "Tarihî Mekânlar, Nesneler ve Anıtlar", "Ülkemizin ve dünyanın somut kültürel miras ögelerini (Sultanahmet, Efes, Göbeklitepe) tanır ve koruma bilinci geliştirir."),
        ("Ortak Mirasımız", "Somut Olmayan Kültürel Miras", "SB.5.3.2", "Gelenekler, Bayramlar, Halk Oyunları ve Masallar", "Kültürel zenginliğimiz olan el sanatları, yemekler ve halk oyunlarının birlik duygusuna katkısını değerlendirir."),
        ("Ortak Mirasımız", "İlk Yerleşimler ve Anadolu Medeniyetleri", "SB.5.3.3", "Hattiler, Hititler, Frigler ve Urartular", "Anadolu'da kurulan ilk uygarlıkların insanlığın ortak mirasına (tarım, yazı, kanun, mimari) katkılarını modeller."),
        ("Ortak Mirasımız", "Mezopotamya Medeniyetleri", "SB.5.3.4", "Sümerler, Babiller ve Asurların Mirası", "Yazıyı bulan Sümerler ve kütüphane kuran Asurların insanlık tarihindeki çığır açan rollerini açıklar."),
        ("Ortak Mirasımız", "Kültürel Mirası Koruma Bilinci", "SB.5.3.5", "Müzeler, Ören Yerleri ve UNESCO Listesi", "Tarihî eserlerin kaçırılmasını önleme ve koruma sorumluluğunu savunur."),
        ("Ortak Mirasımız", "1. Dönem Sentezi", "SB.5.GENEL.2", "1. Dönem Sosyal Bilgiler Kazanım Değerlendirmesi", "Kültür, harita ve haklar ünitelerini içeren portfolyo değerlendirmesi yapar."),
        ("Ortak Mirasımız", "Dönem Sonu Başarı Sınavı", "SB.5.GENEL.2", "1. Dönem Sonu Sosyal Bilgiler Karnesi", "Kapsamlı beceri temelli değerlendirme testini tamamlar."),

        ("Yaşayan Demokrasimiz", "Demokrasi ve Cumhuriyet", "SB.5.4.1", "Cumhuriyetimizin Temel Nitelikleri ve Değerleri", "Egemenliğin millete ait olduğunu, cumhuriyetin getirdiği hak ve özgürlükleri kavrar."),
        ("Yaşayan Demokrasimiz", "Etkin Vatandaşlık", "SB.5.4.2", "Etkin Vatandaşın Sorumlulukları ve Vergi Bilinci", "Kanunlara uyan, vergisini veren, oy kullanan ve çevreye duyarlı etkin vatandaş profilini açıklar."),
        ("Yaşayan Demokrasimiz", "Temel Hak ve Hürriyetler", "SB.5.4.3", "Yaşama, Eğitim, Sağlık ve Düşünce Özgürlüğü", "Anayasamızda güvence altına alınan temel hak ve özgürlükleri örnek olaylarla inceler."),
        ("Yaşayan Demokrasimiz", "Resmî Kurumlar ve STK'lar", "SB.5.4.4", "Bakanlıklar, Valilikler, Belediyeler ve Sivil Toplum", "Toplumsal ihtiyaçları karşılayan devlet kurumları ile gönüllü sivil toplum kuruluşlarını (LÖSEV, TEMA) karşılaştırır."),
        ("Yaşayan Demokrasimiz", "Dilekçe Hakkı ve Hak Arama", "SB.5.4.5", "CİMER ve Tüketici Hakem Heyetleri", "Bir sorunla karşılaşıldığında yasal yollardan dilekçe ile hakkını aramayı öğrenir."),
        ("Yaşayan Demokrasimiz", "Demokrasi Kültürü Projesi", "SB.5.4.6", "Sınıf ve Okul Meclisi Seçimleri", "Seçme ve seçilme kültürünü okul meclis başkanı seçimiyle yaşayarak deneyimler."),

        ("Hayatımızdaki Ekonomi", "İstek ve İhtiyaçlarımız", "SB.5.5.1", "Zorunlu İhtiyaçlar ve İsteklerin Dengelenmesi", "Beslenme, barınma gibi temel ihtiyaçlar ile istekleri ayırt eder; tasarruf bilinci geliştirir."),
        ("Hayatımızdaki Ekonomi", "Kişisel ve Aile Bütçesi", "SB.5.5.2", "Gelir-Gider Dengesi ve Tasarruf Planı", "Kişisel harçlıklarını ve aile bütçesini planlamayı, gereksiz israftan kaçınmayı modeller."),
        ("Ara Tatil", "2. Dönem Ara Tatili", "SB.5.GENEL.3", "Demokrasi ve Ekonomi Becerileri Kampı", "Bütçe ve vatandaşlık hakları soruları çözer."),
        ("Hayatımızdaki Ekonomi", "Ekonomik Faaliyetler ve Coğrafya", "SB.5.5.3", "Tarım, Hayvancılık, Sanayi, Turizm ve Madencilik", "Bölgelerin coğrafi özelliklerinin (iklim, yer şekilleri) ekonomik faaliyetleri nasıl belirlediğini açıklar."),
        ("Hayatımızdaki Ekonomi", "Meslekler ve Ekonomi", "SB.5.5.4", "Ekonomik Faaliyetlerin Doğurduğu Meslekler", "Çevresindeki meslekleri tanır ve gelecekteki kariyer ilgi alanlarını belirler."),

        ("Teknoloji ve Sosyal Bilimler", "Teknolojinin Topluma Etkisi", "SB.5.6.1", "Teknolojik Gelişmelerin Olumlu ve Olumsuz Yansımaları", "Ulaşım, iletişim ve sağlık teknolojilerinin hayatı kolaylaştırırken yüz yüze iletişimi azaltmasını değerlendirir."),
        ("Teknoloji ve Sosyal Bilimler", "Doğru ve Güvenilir Bilgiye Ulaşma", "SB.5.6.2", "İnternet Kaynaklarını Eleştirel Süzgeçten Geçirme", "Arama motorlarında resmî ve bilimsel siteleri (.gov, .edu) tercih etme ve bilgi kirliliğini fark etme becerisi edinir."),
        ("Teknoloji ve Sosyal Bilimler", "Güvenli ve Bilinçli Medya Kullanımı", "SB.5.6.3", "Sanal Ortam Tehditleri ve Dijital Vatandaşlık", "Kişisel verilerin gizliliği, telif hakları ve siber zorbalıktan korunma kurallarını açıklar."),
        ("Teknoloji ve Sosyal Bilimler", "Bilim İnsanlarının Ortak Özellikleri", "SB.5.6.4", "Merak, Sorgulama, Kararlılık ve Çalışkanlık", "Aziz Sancar, Cahit Arf ve İbni Sina gibi bilim insanlarının hayatından ilham alır."),
        ("Teknoloji ve Sosyal Bilimler", "Buluşlar ve Patent Bilinci", "SB.5.6.5", "Yaratıcı Fikirler, Buluş Yapma ve Fikri Mülkiyet", "Kendi özgün fikrini tasarlar; patent ve telif hakkının mucidin emeğini koruduğunu kavrar."),
        ("Teknoloji ve Sosyal Bilimler", "Maarif Modeli Yıl Sonu Sentezi", "SB.5.6.6", "5. Sınıf Sosyal Bilgiler Portfolyo Sunumu", "Tüm yılın vatandaşlık, tarih, coğrafya ve ekonomi ürünlerini içeren sergi düzenler."),
    ]
    weeks_data = []
    for i, u in enumerate(units):
        weeks_data.append({
            'theme': u[0], 'subTheme': u[1], 'code': u[2], 'title': u[3], 'description': u[4],
            'process': ['a) ' + u[4][:30] + ' analiz eder.', 'b) Günlük yaşamla ilişkilendirir.'],
            'concepts': [u[1], 'Sosyal Bilgiler', 'Vatandaşlık', 'Maarif Modeli'],
            'skills': ['Eleştirel Düşünme', 'Mekânsal Algılama', 'Tarihsel Empati'],
            'pedagogical': 'Görsel haritalar, kanıtlar ve durum çalışmaları kullanılır.',
            'context': 'Sosyal Bilgiler Atölyesi',
            'question': f"{u[1]} konusunun vatandaşlık ve günlük yaşam açısından en temel önemi nedir?",
            'solution': f"{u[3]} bilinci kazanmak ve etkin, sorumluluk sahibi bir vatandaş olmaktır.",
            'weeklyGoal': u[3], 'evaluation': 'Haftalık kazanım değerlendirme rubriği'
        })
    return {
        'title': '5. Sınıf',
        'subtitle': 'Türkiye Yüzyılı Maarif Modeli (6 Öğrenme Alanı)',
        'badge': 'Maarif Modeli ✨',
        'weeks': weeks_data
    }

def build_sosyal_6():
    # 6. Sınıf Sosyal Bilgiler MEB Müfredatı
    units = [
        ("Biz ve Değerlerimiz", "Roller ve Sosyal Kimlik", "SOS.6.1.1", "Toplumsal Rollerimiz ve Kimliklerimiz", "Farklı gruplarda üstlendiğimiz rollerin hak ve sorumluluklarını açıklar."),
        ("Biz ve Değerlerimiz", "Kültür ve Birlik", "SOS.6.1.2", "Kültürel Ögelerimizin Toplumsal Birlikteliğe Katkısı", "Dil, din, tarih ve geleneklerin milleti bir arada tutan çimento olduğunu modeller."),
        ("Biz ve Değerlerimiz", "Ön Yargılar ve Ayrımcılık", "SOS.6.1.3", "Toplumsal Ön Yargıların Aşılması ve Empati", "Farklılıklara saygı göstererek kalıp yargıları sorgular."),
        ("Biz ve Değerlerimiz", "Toplumsal Dayanışma", "SOS.6.1.4", "Yardımlaşma, Sadaka Taşları ve Vakıf Kültürü", "Tarihten günümüze vakıf ve yardımlaşma kurumlarının sosyal barışa etkisini değerlendirir."),
        ("Biz ve Değerlerimiz", "Hak Arama Yolları", "SOS.6.1.5", "Sorunların Çözümünde Hak, Özgürlük ve Sorumluluk", "Tüketici hakem heyetleri ve yasal hak arama mekanizmalarını çözümler."),

        ("Tarihe Yolculuk", "İlk Türk Devletleri", "SOS.6.2.1", "Orta Asya İlk Türk Devletleri (Hunlar, Göktürkler, Uygurlar)", "Orta Asya coğrafyasının Türklerin göçebe yaşamına, ordu-millet anlayışına ve sanatına etkisini açıklar."),
        ("Tarihe Yolculuk", "Orhun Abideleri ve Yazıtlar", "SOS.6.2.1", "Bilge Kağan, Kültigin ve Tonyukuk Yazıtları", "Türk adının geçtiği ilk Türkçe yazılı belgeler olan Orhun Kitabelerinin devlet ve millet mesajını irdeler."),
        ("Tarihe Yolculuk", "İslamiyet'in Doğuşu ve Yayılışı", "SOS.6.2.2", "İslamiyet Öncesi Arap Yarımadası ve Dört Halife Dönemi", "Cahiliye döneminden sonra İslamiyet'in getirdiği adalet, eşitlik ve bilimsel gelişmeleri açıklar."),
        ("Tarihe Yolculuk", "Türklerin İslamiyet'i Kabulü", "SOS.6.2.3", "Talas Savaşı ve İlk Türk-İslam Devletleri (Karahanlılar, Gazneliler, Selçuklular)", "Türklerin İslamiyet'e geçişiyle siyasi, kültürel ve mimari alandaki büyük dönüşümü modeller."),
        ("Ara Tatil", "1. Dönem Ara Tatili", "SOS.6.GENEL.1", "Tarihe Yolculuk ve Sosyal Değerler Kampı", "İlk Türk devletleri ve İslam tarihi soruları çözer."),
        ("Tarihe Yolculuk", "Malazgirt ve Anadolu'nun Türkleşmesi", "SOS.6.2.4", "1071 Malazgirt Zaferi ve Türkiye Tarihi Başlangıcı", "Sultan Alparslan'ın zaferiyle Anadolu'nun kapılarının Türklere açılmasını ve ilk beylikleri inceler."),
        ("Tarihe Yolculuk", "Tarihî Yollar: İpek ve Baharat Yolu", "SOS.6.2.5", "Kültür Köprüsü Ticaret Yolları", "İpek ve Baharat Yollarının devletler arası ekonomik ve kültürel etkileşimdeki rolünü savunur."),

        ("Yeryüzünde Yaşam", "Dünya'nın Neresindeyiz?", "SOS.6.3.1", "Kıtalar, Okyanuslar, Paralel ve Meridyenler", "Ekvator, Başlangıç Meridyeni ve koordinat sistemiyle bir yerin mutlak ve göreceli konumunu bulur."),
        ("Yeryüzünde Yaşam", "Türkiye'nin Coğrafi Konumu", "SOS.6.3.1", "Türkiye'nin Jeopolitik ve Matematik Konumu", "Türkiye'nin 36°-42° Kuzey paralelleri, 26°-45° Doğu meridyenleri arasında yer almasının sonuçlarını açıklar."),
        ("Yeryüzünde Yaşam", "Türkiye'nin Fiziki Özellikleri", "SOS.6.3.2", "Fiziki Harita Renkleri ve Yeryüzü Şekilleri", "Kahverenginin yüksek dağları, yeşilin deniz seviyesine yakın ovaları temsil ettiğini ayırt eder."),
        ("Yeryüzünde Yaşam", "İklim ve Bitki Örtüsü", "SOS.6.3.3", "Türkiye'de Görülen Üç Büyük İklim Tipi", "Karasal iklim (bozkır), Akdeniz iklimi (maki), Karadeniz iklimi (orman) özelliklerini karşılaştırır."),
        ("Yeryüzünde Yaşam", "Nüfus ve Yerleşmeyi Etkileyen Faktörler", "SOS.6.3.4", "Doğal ve Beşerî Nüfus Dağılımı", "Sanayi, tarım ve iklimin Türkiye'deki nüfus yoğunluğuna etkisini harita üzerinde analiz eder."),
        ("Yeryüzünde Yaşam", "1. Dönem Sonu Sentezi", "SOS.6.GENEL.2", "1. Dönem Sosyal Bilgiler Başarı Değerlendirmesi", "Tarih, coğrafya ve vatandaşlık kazanımlarını değerlendirir."),
        ("Yeryüzünde Yaşam", "1. Dönem Karnesi", "SOS.6.GENEL.2", "1. Dönem Final Sınavı", "Dönem sonu değerlendirme sınavını uygular."),

        ("Bilim, Teknoloji ve Toplum", "Bilginin Serüveni", "SOS.6.4.1", "Yazının İcadından Dijital Kütüphanelere", "Kil tablet, papirüs, parşömen, kâğıt ve matbaanın bilginin yayılmasındaki katkılarını açıklar."),
        ("Bilim, Teknoloji ve Toplum", "Türk-İslam Bilginleri", "SOS.6.4.2", "Harezmi, İbni Sina, Farabi, Biruni ve Uluğ Bey", "Sıfırı bulan Harezmi ve tıbbın hükümdarı İbni Sina gibi bilginlerin medeniyete katkılarını modeller."),
        ("Bilim, Teknoloji ve Toplum", "Avrupa'da Aydınlanma", "SOS.6.4.3", "Coğrafi Keşifler, Rönesans, Reform ve Aydınlanma Çağı", "Avrupa'da skolastik düşüncenin yıkılıp akıl ve deneyin ön plana çıkışını inceler."),
        ("Bilim, Teknoloji ve Toplum", "Telif ve Patent Hakları", "SOS.6.4.4", "Fikri Emeğe Saygı ve Korsanla Mücadele", "Korsan ürün almanın ülke ekonomisine ve yazara zararını açıklayarak bandrol bilinci geliştirir."),

        ("Üretiyorum, Tüketiyorum, Yönetiyorum", "Kaynaklarımız Kazanca Dönüşüyor", "SOS.6.5.1", "Toprak, Su, Orman ve Maden Kaynaklarımız", "Türkiye'nin bor, krom, kömür gibi zengin madenlerini ve tarım potansiyelini değerlendirir."),
        ("Üretiyorum, Tüketiyorum, Yönetiyorum", "Yatırım ve Pazarlama", "SOS.6.5.2", "Bölgelerimize Göre Yatırım Projeleri", "Bir bölgenin hammadde ve pazar imkanlarına uygun ekonomik yatırım fikirleri tasarlar."),
        ("Üretiyorum, Tüketiyorum, Yönetiyorum", "Vergilerimizle Büyüyoruz", "SOS.6.5.3", "Vergi Vermenin Kutsallığı ve Kamu Hizmetleri", "Ödenen vergilerin okul, hastane, yol ve güvenlik hizmeti olarak vatandaşa geri döndüğünü açıklar."),
        ("Üretiyorum, Tüketiyorum, Yönetiyorum", "Nitelikli İnsan Gücü", "SOS.6.5.4", "Meslek Seçimi ve İş Gücü Verimliliği", "İlgi ve yeteneklerine uygun doğru meslek seçmenin ülke kalkınmasına katkısını kavrar."),
        ("Üretiyorum, Tüketiyorum, Yönetiyorum", "Bilinçli Tüketici", "SOS.6.5.5", "Bilinçli Tüketici Davranışları ve Tüketici Hakları", "Alışverişlerde fatura, fiş alma, TSE damgası arama ve ayıplı mal durumunda hakem heyetine başvurma bilincini uygular."),
        ("Ara Tatil", "2. Dönem Ara Tatili", "SOS.6.GENEL.3", "Ekonomi ve Coğrafya Becerileri Kampı", "Kaynaklar ve harita bilgisi soruları çözer."),

        ("Etkin Vatandaşlık", "Nasıl Bir Yönetim?", "SOS.6.6.1", "Yönetim Biçimleri: Monarşi, Oligarşi, Teokrasi, Cumhuriyet", "Tarihteki ve günümüzdeki yönetim sistemlerini milli egemenlik ve insan hakları açısından karşılaştırır."),
        ("Etkin Vatandaşlık", "Üç Temel Güç: Kuvvetler Ayrılığı", "SOS.6.6.2", "Yasama (TBMM), Yürütme (Cumhurbaşkanı) ve Yargı (Bağımsız Mahkemeler)", "Demokratik devletlerde yasama, yürütme ve yargının birbirini denetleyen bağımsızlığını modeller."),
        ("Etkin Vatandaşlık", "Toplumsal Yaşamda Kadın", "SOS.6.6.3", "Tarihte ve Günümüzde Türk Kadınının Rolü", "Tomris Hatun'dan Kurtuluş Savaşı kahramanı kadınlara ve cumhuriyetle kazanılan haklara kadının yerini savunur."),

        ("Küresel Bağlantılar", "Komşularımızla Ticaret", "SOS.6.7.1", "Türkiye'nin Dış Ticareti: İhracat ve İthalat", "Sattığımız ürünler (ihracat: otomotiv, tekstil, fındık) ve aldığımız ürünler (ithalat: petrol, doğalgaz, elektronik) dengesini çözümler."),
        ("Küresel Bağlantılar", "Türk Dünyası ve TİKA", "SOS.6.7.2", "Orta Asya Türk Cumhuriyetleri ve İş Birliği", "Azerbaycan, Kazakistan, Özbekistan, Türkmenistan, Kırgızistan ile kurulan kardeşlik ve ekonomik köprüleri açıklar."),
        ("Küresel Bağlantılar", "Uluslararası Yardım Kuruluşları", "SOS.6.7.3", "Kızılay, AFAD ve BM İnsani Yardım Görevleri", "Türkiye'nin dünyada milli gelirine oranla en çok insani yardım yapan ülke vasfını değerlendirir."),
        ("Küresel Bağlantılar", "Yıl Sonu Sentezi", "SOS.6.7.4", "6. Sınıf Sosyal Bilgiler Başarı Projesi", "Yıl boyunca öğrenilen tarih, coğrafya, ekonomi ve dış ilişkiler kazanımlarını sergiler."),
    ]
    weeks_data = []
    for i, u in enumerate(units):
        weeks_data.append({
            'theme': u[0], 'subTheme': u[1], 'code': u[2], 'title': u[3], 'description': u[4],
            'process': ['a) ' + u[4][:30] + ' kavrar.', 'b) Neden-sonuç bağıntısı kurar.'],
            'concepts': [u[1], 'Tarih', 'Coğrafya', 'Vatandaşlık'],
            'skills': ['Kronolojik Düşünme', 'Harita Analizi', 'Tarihsel Empati'],
            'pedagogical': 'Görsel belgeler, haritalar ve kaynak metinler incelenir.',
            'context': 'Sosyal Bilimler Laboratuvarı',
            'question': f"{u[1]} konusunun ülkemiz tarihi ve kültürü açısından temel rolü nedir?",
            'solution': f"{u[3]} kazanımıyla millî ve evrensel değerleri özümsemektir.",
            'weeklyGoal': u[3], 'evaluation': 'Haftalık kazanım değerlendirme föyü'
        })
    return {
        'title': '6. Sınıf',
        'subtitle': 'Ortaokul 2. Kademe Sosyal Bilgiler',
        'badge': 'Ortaokul Sosyal',
        'weeks': weeks_data
    }

def build_sosyal_7():
    # 7. Sınıf Sosyal Bilgiler MEB Müfredatı
    units = [
        ("İletişim ve İnsan İlişkileri", "İletişimin Gücü", "SOS.7.1.1", "Olumlu ve Olumsuz İletişim, Beden Dili, Sen Dili ve Ben Dili", "İletişimi olumlu etkileyen empati, etkin dinleme ve tebessümü; olumsuz etkileyen ön yargı ve lakap takmayı ayırt eder."),
        ("İletişim ve İnsan İlişkileri", "Medya ve İletişim Özgürlüğü", "SOS.7.1.2", "Kitle İletişim Araçları, RTÜK ve Sansür", "Medya araçlarının toplumsal etkisini ve kamuoyu oluşturma gücünü değerlendirir."),
        ("İletişim ve İnsan İlişkileri", "Özel Hayatın Gizliliği ve Tekzip", "SOS.7.1.3", "Haberleşme Hürriyeti ve Düzeltme Yazısı (Tekzip)", "Anayasal hak olan özel hayatın gizliliğini ve yalan haberlere karşı düzeltme (tekzip) hakkını açıklar."),
        ("İletişim ve İnsan İlişkileri", "Doğru Bilgi ve Sansür", "SOS.7.1.4", "Basın Ahlakı ve Sansür Yasağı", "Basın yayın organlarının doğru bilgi verme sorumluluğunu ve sansür yasağını değerlendirir."),

        ("Türk Tarihinde Yolculuk", "Osmanlı'nın Kuruluşu", "SOS.7.2.1", "Kayı Boyu, Osman Bey ve Beylikten Devlete Geçiş", "Söğüt ve Domaniç'te kurulan Osmanlı Beyliği'nin kısa sürede büyüme nedenlerini (Bizans'ın zayıflığı, İskân ve İstimalet politikaları) açıklar."),
        ("Türk Tarihinde Yolculuk", "Osmanlı'nın Fetih Siyaseti", "SOS.7.2.2", "İskân (Yerleştirme) ve İstimalet (Hoşgörü) Politikası", "Balkanlarda fethedilen yerlere Türkmenlerin yerleştirilmesini ve gayrimüslim halka gösterilen hoşgörüyü çözümler."),
        ("Türk Tarihinde Yolculuk", "Devlet Teşkilatı ve Ordu", "SOS.7.2.3", "Divan-ı Hümayun, Tımar Sistemi ve Yeniçeri Ocağı", "Osmanlı devlet yönetiminde Divan üyelerini (Sadrazam, Şeyhülislam, Defterdar, Nişancı) ve ordu yapısını modeller."),
        ("Türk Tarihinde Yolculuk", "İstanbul'un Fethi (1453)", "SOS.7.2.4", "Fatih Sultan Mehmet ve Bir Çağın Kapanışı", "İstanbul'un fethinin hazırlıklarını (Şahi topları, Rumeli Hisarı), Türk ve dünya tarihi açısından sonuçlarını açıklar."),
        ("Türk Tarihinde Yolculuk", "Osmanlı'da Yükselme ve Denizler", "SOS.7.2.5", "Yavuz Sultan Selim, Kanuni ve Preveze Deniz Zaferi", "Akdeniz'in Türk gölü haline gelmesini (Barbaros Hayrettin Paşa) ve İpek-Baharat yollarının kontrolünü inceler."),
        ("Türk Tarihinde Yolculuk", "Osmanlı Kültür, Sanat ve Mimarisi", "SOS.7.2.6", "Mimar Sinan, Minyatür, Hat ve Çini Sanatı", "Süleymaniye, Selimiye camilerini ve Osmanlı şehir kültürünü modeller."),
        ("Ara Tatil", "1. Dönem Ara Tatili", "SOS.7.GENEL.1", "İletişim ve Osmanlı Tarihi Tekrar Kampı", "Osmanlı fetihleri ve iletişim soruları çözer."),
        ("Türk Tarihinde Yolculuk", "Osmanlı'da Islahat Hareketleri", "SOS.7.2.7", "Lale Devri, Matbaanın Gelişi ve III. Selim Islahatları", "Avrupa'daki gelişmeleri yakalamak için açılan elçilikleri ve İbrahim Müteferrika matbaasını değerlendirir."),
        ("Türk Tarihinde Yolculuk", "Seyyahların Gözüyle Osmanlı", "SOS.7.2.8", "Avrupalı Gezginlerin Kaleminden Osmanlı Toplumu", "Yabancı seyyahların Osmanlı adaletini, temizliğini ve hayvansever vakıflarını anlatan notlarını tahlil eder."),
        ("Türk Tarihinde Yolculuk", "Sanayi İnkılabının Osmanlı'ya Etkisi", "SOS.7.2.9", "Balta Limanı Ticaret Sözleşmesi ve Loncaların Durumu", "Avrupa'dan gelen ucuz malların Osmanlı yerli üretimine ve esnaf teşkilatına etkilerini değerlendirir."),

        ("Ülkemizde Nüfus", "Nüfusun Dağılışı", "SOS.7.3.1", "Türkiye'de Nüfus Yoğunluğunu Etkileyen Faktörler", "İklim, su kaynakları, sanayi ve ulaşımın nüfus dağılışına etkisini haritalarla inceler."),
        ("Ülkemizde Nüfus", "Nüfus Sayımları ve Piramitler", "SOS.7.3.2", "Nüfusun Yaş, Cinsiyet ve Eğitim Özellikleri", "Grafik ve piramitlerden yararlanarak Türkiye nüfusunun dinamik yapısını analiz eder."),
        ("Ülkemizde Nüfus", "Göçün Neden ve Sonuçları", "SOS.7.3.3", "İç Göç, Dış Göç, Beyin Göçü ve Mülteciler", "Kırsaldan kente göçün şehirlerde yarattığı altyapı ve konut sorunlarını; beyin göçünün etkilerini çözümler."),
        ("Ülkemizde Nüfus", "Yerleşme ve Seyahat Özgürlüğü", "SOS.7.3.4", "Anayasal Yerleşme ve Seyahat Hürriyeti ve Kısıtlanma Halleri", "Kamu sağlığı, suç soruşturması gibi durumlarda seyahat özgürlüğünün kanunla kısıtlanabileceğini açıklar."),
        ("Ülkemizde Nüfus", "1. Dönem Sonu Değerlendirmesi", "SOS.7.GENEL.2", "1. Dönem Sosyal Bilgiler Sentezi", "Nüfus, tarih ve iletişim konularını değerlendirir."),
        ("Ülkemizde Nüfus", "1. Dönem Karnesi", "SOS.7.GENEL.2", "1. Dönem Final Sınavı", "Dönemlik başarı ölçümünü tamamlar."),

        ("Bilim, Teknoloji ve Toplum", "Zaman İçinde Bilim", "SOS.7.4.1", "Tarihte Bilimsel Düşüncenin Gelişimi ve Skolastik Düşünce", "Orta Çağ Avrupası\'ndaki dogmatik baskı ile İslam dünyasındaki altın çağ kütüphanelerini karşılaştırır."),
        ("Bilim, Teknoloji ve Toplum", "Bilimin Öncüleri", "SOS.7.4.2", "Harezmi, Katip Çelebi, Ali Kuşçu ve Piri Reis", "Piri Reis\'in Dünya haritası ve Osmanlı denizcilik bilimine katkılarını çözümler."),
        ("Bilim, Teknoloji ve Toplum", "Aydınlanma ve Sanayi İnkılabı", "SOS.7.4.3", "Buhar Makinesi, Fabrikalaşma ve Sanayi Devrimi", "Kol gücünden makine gücüne geçişin sömürgecilik ve hammadde yarışına yol açmasını değerlendirir."),
        ("Bilim, Teknoloji ve Toplum", "Düşünce Özgürlüğü ve Bilim", "SOS.7.4.4", "Özgür Düşüncenin Bilimsel Gelişmeye Etkisi", "Demokratik ve özgür ortamlarda bilimin nasıl hızla ilerlediğini örnek olaylarla savunur."),

        ("Ekonomi ve Sosyal Hayat", "Toprak Ana", "SOS.7.5.1", "Tarihten Günümüze Toprak Yönetimi (İkta, Tımar ve Çiftçilik)", "Selçuklu\'daki ikta ve Osmanlı\'daki tımar sisteminin üretimde süreklilik ve asker yetiştirmedeki gücünü açıklar."),
        ("Ekonomi ve Sosyal Hayat", "Ahilik ve Lonca Teşkilatı", "SOS.7.5.2", "Ahi Evran, Esnaf Ahlakı ve Mesleki Eğitim", "Çırak, kalfa, usta hiyerarşisini, kalite kontrolünü ve dayanışma ahlakını modeller."),
        ("Ekonomi ve Sosyal Hayat", "Vakıf Demek Medeniyet Demektir", "SOS.7.5.3", "Osmanlı Vakıf Sistemi, İmarethaneler ve Sosyal Yardımlaşma", "Kuş evlerinden şifahanelere kadar vakıfların toplum hayatındaki hayati rolünü inceler."),
        ("Ekonomi ve Sosyal Hayat", "Meslek Seçimi ve Geleceğin Meslekleri", "SOS.7.5.4", "Yapay Zeka Çağında Meslekler ve Kariyer Planı", "Yazılım, siber güvenlik, biyoteknoloji gibi geleceğin mesleklerini değerlendirir."),
        ("Ara Tatil", "2. Dönem Ara Tatili", "SOS.7.GENEL.3", "Ekonomi ve Bilim Tarihi Soru Kampı", "Tımar, lonca ve sanayi devrimi soruları çözer."),

        ("Yaşayan Demokrasi", "Demokrasinin Serüveni", "SOS.7.6.1", "İlk Çağ\'dan Günümüze Demokrasinin Tarihsel Gelişimi", "Hammurabi Kanunları, Magna Carta, Fransız İhtilali ve İnsan Hakları Evrensel Beyannamesi sürecini çözümler."),
        ("Yaşayan Demokrasi", "Atatürk ve Demokrasi", "SOS.7.6.2", "Cumhuriyetin İlanı, TBMM ve Çok Partili Hayat Denemeleri", "Mustafa Kemal\'in milli egemenlik ilkesini ve meclis hükümetinden parlamenter sisteme geçişi inceler."),
        ("Yaşayan Demokrasimiz", "Anayasamız ve Devletin Nitelikleri", "SOS.7.6.3", "Demokratik, Laik, Sosyal ve Hukuk Devleti İlkeleri", "Türkiye Cumhuriyeti Devleti\'nin anayasada belirtilen temel niteliklerini açıklar."),

        ("Küresel Konular", "Uluslararası Örgütler", "SOS.7.7.1", "Türkiye\'nin Üye Olduğu Kuruluşlar (BM, NATO, Türk Devletleri Teşkilatı)", "Türkiye\'nin bölgesel ve küresel barışa katkı sağlayan uluslararası rollerini değerlendirir."),
        ("Küresel Konular", "Küresel Sorunlar ve Çözümler", "SOS.7.7.2", "İklim Krizi, Açlık, Terör ve Göç Dalgaları", "Dünyayı tehdit eden küresel sorunlara karşı ortak sorumluluk ve yardımlaşma bilinci geliştirir."),
        ("Küresel Konular", "Kalıp Yargılar ve Barış Kültürü", "SOS.7.7.3", "Farklı Kültürlere Karşı Hoşgörü ve Dünya Vatandaşlığı", "Farklı milletlere yönelik ön yargıların kırılmasıyla barışın tesis edileceğini savunur."),
        ("Küresel Konular", "8. Sınıf LGS İnkılap Tarihi Köprüsü", "SOS.7.7.4", "7. Sınıf Sosyal Bilgiler Kapanışı ve LGS Hazırlık", "7. sınıf kazanımlarının 8. sınıf İnkılap Tarihi için kurduğu temeli özetler."),
    ]
    weeks_data = []
    for i, u in enumerate(units):
        weeks_data.append({
            'theme': u[0], 'subTheme': u[1], 'code': u[2], 'title': u[3], 'description': u[4],
            'process': ['a) ' + u[4][:30] + ' analiz eder.', 'b) Tarihsel bağıntı kurar.'],
            'concepts': [u[1], 'Osmanlı', 'Nüfus', 'Demokrasi'],
            'skills': ['Tarihsel Analiz', 'Mekânsal Algı', 'Demokratik Bilinç'],
            'pedagogical': 'Tarihsel haritalar, fermanlar ve seyahatnameler incelenir.',
            'context': 'Tarih ve Toplum Atölyesi',
            'question': f"{u[1]} konusunun Osmanlı ve Türk medeniyet tarihindeki yeri nedir?",
            'solution': f"{u[3]} ilkesini öğrenerek millî hafızayı ve vatandaşlık şuurunu pekiştirmektir.",
            'weeklyGoal': u[3], 'evaluation': 'Haftalık kazanım değerlendirme föyü'
        })
    return {
        'title': '7. Sınıf',
        'subtitle': 'Ortaokul 3. Kademe Sosyal Bilgiler',
        'badge': 'Ortaokul Sosyal',
        'weeks': weeks_data
    }

def build_sosyal_8():
    # 8. Sınıf LGS T.C. İnkılap Tarihi ve Atatürkçülük Müfredatı
    units = [
        ("Bir Kahraman Doğuyor", "Uyanan Avrupa ve Tükenen Osmanlı", "İNK.8.1.1", "Sanayi İnkılabı, Fransız İhtilali ve Osmanlı'nın Son Dönemi", "Avrupa'daki gelişmelerin Osmanlı'ya sömürgecilik ve azınlık isyanları olarak yansımasını; Tanzimat, Islahat ve Meşrutiyet çabalarını modeller."),
        ("Bir Kahraman Doğuyor", "Mustafa Kemal'in Çocukluğu ve Öğrenim Hayatı", "İNK.8.1.2", "Selanik'in Kültürel Yapısı ve Askerî Okul Yılları", "Selanik, Manastır, İstanbul ve Sofya şehirlerinin Mustafa Kemal'in fikir hayatına (vatanseverlik, milliyetçilik, liderlik) etkisini açıklar."),
        ("Bir Kahraman Doğuyor", "Mustafa Kemal'in Askerlik Hayatı", "İNK.8.1.3", "Şam, 31 Mart Vakası, Trablusgarp ve Balkan Savaşları", "Trablusgarp'ta sömürgeci İtalya'ya karşı Derne ve Tobruk'ta yerel halkı teşkilatlandırmasını inceler."),
        ("Bir Kahraman Doğuyor", "Mustafa Kemal'in Kişilik Özellikleri", "İNK.8.1.4", "Vatanseverlik, İleri Görüşlülük, Teşkilatçılık ve Birleştiricilik", "Tarihsel olaylar üzerinden Mustafa Kemal'in üstün komutanlık ve liderlik karakterini çözümler."),
        ("Bir Kahraman Doğuyor", "1. Ünite LGS Soru Kampı", "İNK.8.1.5", "Bir Kahraman Doğuyor Ünite Değerlendirmesi", "LGS çıkmış harita ve metin analizi sorularını çözer."),

        ("Millî Uyanış", "I. Dünya Savaşı'nın Sebepleri ve Bloklar", "İNK.8.2.1", "Hammadde Yarışı, Milliyetçilik ve İttifak-İtilaf Devletleri", "Savaşın genel ve özel nedenlerini; Osmanlı'nın savaşa giriş sürecini (Goben ve Breslau) inceler."),
        ("Millî Uyanış", "Osmanlı'nın Savaştığı Cepheler", "İNK.8.2.2", "Kafkas, Kanal, Çanakkale, Hicaz-Yemen ve Irak Cepheleri", "Kafkas'ta Sarıkamış faciası ve Tehcir Kanunu'nu; Çanakkale'de Anafartalar Kahramanı Mustafa Kemal'i modeller."),
        ("Millî Uyanış", "Mondros Ateşkes Antlaşması ve İşgaller", "İNK.8.2.3", "Mondros'un Ağır Şartları (7. ve 24. Maddeler) ve İşgaller", "Anadolu'nun işgali karşısında İstanbul Hükümeti'nin teslimiyetçi tutumu ile Mustafa Kemal'in bağımsızlık kararını karşılaştırır."),
        ("Millî Uyanış", "Kuvâ-yı Millîye ve Cemiyetler", "İNK.8.2.4", "Yararlı Cemiyetler, Zararlı Cemiyetler ve Millî Direniş", "Halkın kurduğu Kuvâ-yı Millîye birliklerini ve azınlık cemiyetlerine karşı kurulan Müdafaa-i Hukuk cemiyetlerini inceler."),
        ("Ara Tatil", "1. Dönem Ara Tatili", "İNK.8.GENEL.1", "I. Dünya Savaşı ve Mondros LGS Kampı", "LGS yeni nesil harita ve kronoloji soruları çözer."),
        ("Millî Uyanış", "Samsun'dan Havza ve Amasya'ya", "İNK.8.2.5", "19 Mayıs 1919 Samsun'a Çıkış, Havza ve Amasya Genelgeleri", "Amasya Genelgesi'nde Kurtuluş Savaşı'nın amacı, gerekçesi ve yönteminin ('Milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır') ilan edilişini açıklar."),
        ("Millî Uyanış", "Erzurum ve Sivas Kongreleri", "İNK.8.2.6", "Manda ve Himayenin Reddi ve Heyet-i Temsiliye", "Erzurum'un toplanış bakımından bölgesel, kararlar bakımından millî olduğunu; Sivas'ta tüm cemiyetlerin birleştirildiğini çözümler."),
        ("Millî Uyanış", "Amasya Görüşmeleri ve Misakımillî", "İNK.8.2.7", "Son Osmanlı Mebusan Meclisi ve Misakımillî Kararları", "İstanbul'un işgali, meclisin basılması ve Misakımillî'nin vatan sınırlarını çizen ilkelerini analiz eder."),
        ("Millî Uyanış", "TBMM'nin Açılışı ve İsyanlar", "İNK.8.2.8", "23 Nisan 1920 BMM'nin Açılması ve Hıyanet-i Vataniye Kanunu", "Milli iradenin temsilcisi meclisin açılışını, ayaklanmaları bastırmak için kurulan İstiklal Mahkemelerini modeller."),
        ("Millî Uyanış", "Sevr Barış Antlaşması: Bir Ölüm Fermanı", "İNK.8.2.9", "Geçersiz ve Hukuken Yok Hükmünde Bir Antlaşma", "Milletin bağımsızlık azmi karşısında uygulanamayan Sevr'in ağır maddelerini çözümler."),

        ("Ya İstiklal Ya Ölüm!", "Doğu ve Güney Cepheleri", "İNK.8.3.1", "Kazım Karabekir (Gümrü) ve Güneyde Kahraman Şehirler", "Ermenilere karşı ilk zafer olan Gümrü Antlaşması'nı; Antep, Maraş ve Urfa'da halkın destansı direnişini açıklar."),
        ("Ya İstiklal Ya Ölüm!", "Batı Cephesi: I. ve II. İnönü Zaferleri", "İNK.8.3.2", "Düzenli Ordunun Kurulması ve İnönü Zaferleri", "I. İnönü sonrası Londra Konferansı, Afganistan Dostluk Antlaşması, İstiklal Marşı'nın kabulü ve Moskova Antlaşması'nı (MİLİM şifresi) modeller."),
        ("Ya İstiklal Ya Ölüm!", "1. Dönem LGS Finali", "İNK.8.GENEL.2", "1. Dönem LGS İnkılap Tarihi Denemesi", "Tüm 1. dönem ünitelerini kapsayan 10 soruluk LGS denemesi yapar."),
        ("Ya İstiklal Ya Ölüm!", "1. Dönem Karnesi", "İNK.8.GENEL.2", "1. Dönem Başarı Belgesi", "LGS analizini tamamlar."),

        ("Ya İstiklal Ya Ölüm!", "Kütahya-Eskişehir ve Maarif Kongresi", "İNK.8.3.3", "Geri Çekiliş ve Savaşın Ortasında Eğitim Kongresi", "Ordunun Sakarya'nın doğusuna çekilmesini ve Mustafa Kemal'in eğitime verdiği önemi gösteren Maarif Kongresi'ni inceler."),
        ("Ya İstiklal Ya Ölüm!", "Tekâlif-i Millîye Emirleri", "İNK.8.3.4", "Mustafa Kemal'e Başkomutanlık Yetkisi ve Topyekûn Seferberlik", "Milletin çarık, çorap, buğday vererek ordusunu donattığı Tekâlif-i Millîye fedakârlığını analiz eder."),
        ("Ya İstiklal Ya Ölüm!", "Sakarya Meydan Muharebesi", "İNK.8.3.5", "'Hattı Müdafaa Yoktur, Sathı Müdafaa Vardır'", "22 gün 22 gece süren savaşla 1683 Viyana'dan beri süren geri çekilişin durdurulmasını ve Fransa ile Ankara Antlaşması'nı açıklar."),
        ("Ya İstiklal Ya Ölüm!", "Büyük Taarruz ve Başkomutanlık Savaşı", "İNK.8.3.6", "'Ordular! İlk Hedefiniz Akdeniz'dir, İleri!'", "26 Ağustos'ta başlayan taarruzla düşmanın 9 Eylül'de İzmir'de denize dökülüşünü ve Mudanya Ateşkesini çözümler."),
        ("Ya İstiklal Ya Ölüm!", "Lozan Barış Antlaşması: Bağımsızlık Tapusu", "İNK.8.3.7", "Kapitülasyonların Kaldırılması ve Yeni Türk Devleti'nin Tanınması", "İsmet Paşa liderliğinde Lozan'da kapitülasyonların kaldırılışı, sınırlar, boğazlar ve tazminat maddelerini irdeler."),

        ("Atatürkçülük ve Çağdaşlaşan Türkiye", "Atatürk İlkeleri", "İNK.8.4.1", "Cumhuriyetçilik, Milliyetçilik, Halkçılık, Devletçilik, Laiklik, İnkılapçılık", "6 temel Atatürk ilkesinin amaçlarını ve birbirini tamamlayan bütünlüğünü örnek inkılaplarla eşleştirir."),
        ("Atatürkçülük ve Çağdaşlaşan Türkiye", "Siyasi Alandaki İnkılaplar", "İNK.8.4.2", "Saltanatın Kaldırılması, Ankara'nın Başkent Oluşu, Cumhuriyetin İlanı, Halifeliğin Kaldırılması", "Milli egemenliği pekiştiren siyasi devrimleri kronolojik olarak çözümler."),
        ("Atatürkçülük ve Çağdaşlaşan Türkiye", "Hukuk ve Eğitim İnkılapları", "İNK.8.4.3", "Türk Medeni Kanunu ve Tevhid-i Tedrisat Kanunu", "Kadınlara miras ve boşanma hakkı veren Medeni Kanun ile eğitimi birleştiren Tevhid-i Tedrisat'ı değerlendirir."),
        ("Atatürkçülük ve Çağdaşlaşan Türkiye", "Toplumsal ve Kültürel İnkılaplar", "İNK.8.4.4", "Harf İnkılabı, Millet Mektepleri, Şapka ve Kılık Kıyafet, Soyadı Kanunu", "Latin alfabesine geçişi, okuma yazma seferberliğini ve unvanların kaldırılışını inceler."),
        ("Ara Tatil", "2. Dönem Ara Tatili", "İNK.8.GENEL.3", "LGS İnkılap Tarihi Büyük Kampı", "İlkeler ve İnkılaplar LGS soruları çözer."),
        ("Atatürkçülük ve Çağdaşlaşan Türkiye", "Ekonomi ve Sağlık Alanında İnkılaplar", "İNK.8.4.5", "İzmir İktisat Kongresi, Kabotaj Kanunu ve Sümerbank", "Milli ekonomiyi kurma adımlarını ve Türk denizlerinde bağımsızlığı sağlayan Kabotaj Bayramı'nı açıklar."),

        ("Demokratikleşme Çabaları", "Çok Partili Hayat Denemeleri", "İNK.8.5.1", "Cumhuriyet Halk Fırkası, Terakkiperver ve Serbest Cumhuriyet Fırkaları", "Demokrasinin gereği olan çok partili hayata geçiş denemelerini ve Şeyh Sait İsyanı ile Menemen Olayı nedeniyle ertelenmesini analiz eder."),
        ("Demokratikleşme Çabaları", "Mustafa Kemal'e Suikast Girişimi", "İNK.8.5.2", "İzmir Suikastı ve 'Benim Naçiz Vücudum...'", "'Benim naçiz vücudum elbet bir gün toprak olacaktır fakat Türkiye Cumhuriyeti ilelebet payidar kalacaktır' sözünün derin anlamını kavrar."),

        ("Atatürk Dönemi Türk Dış Politikası", "Dış Politikanın Temel İlkeleri ve Başarıları", "İNK.8.6.1", "'Yurtta Sulh, Cihanda Sulh', Musul Meselesi, Milletler Cemiyeti", "Milli güce dayanan, barışçı ve gerçekçi dış politika ilkelerini inceler."),
        ("Atatürk Dönemi Türk Dış Politikası", "Boğazlar ve Hatay Zaferleri", "İNK.8.6.2", "Montrö Boğazlar Sözleşmesi (1936) ve Hatay'ın Anavatana Katılması (1939)", "Boğazlarda tam egemenlik sağlayan Montrö'yü ve Atatürk'ün 'şahsi meselem' dediği Hatay davasını çözer."),

        ("Atatürk'ün Ölümü ve Sonrası", "Bir Büyük Liderin Vedası ve II. Dünya Savaşı", "İNK.8.7.1", "10 Kasım 1938, İsmet İnönü Dönemi ve Çok Partili Hayata Kesin Geçiş (1946)", "Atatürk'ün ebediyete intikalini, eserlerini ve Türkiye'nin II. Dünya Savaşı'nda izlediği tarafsızlık politikasını açıklar."),
        ("Atatürk'ün Ölümü ve Sonrası", "LGS İnkılap Tarihi 10/10 Tam Prova", "İNK.8.7.2", "LGS İnkılap Tarihi Genel Denemesi ve Şampiyonluk Sertifikası", "LGS standartlarında 10 soruluk tam prova denemesini tamamlar."),
    ]
    weeks_data = []
    for i, u in enumerate(units):
        weeks_data.append({
            'theme': u[0], 'subTheme': u[1], 'code': u[2], 'title': u[3], 'description': u[4],
            'process': ['a) ' + u[4][:30] + ' tahlil eder.', 'b) Neden-sonuç ve kronoloji kurar.'],
            'concepts': [u[1], 'LGS İnkılap', 'Atatürkçülük', 'Millî Mücadele'],
            'skills': ['Tarihsel Muhakeme', 'Harita Yorumlama', 'LGS Soru Analizi'],
            'pedagogical': 'Kronolojik zaman çizelgeleri, Nutuk alıntıları ve LGS soru kalıpları incelenir.',
            'context': 'LGS İnkılap Tarihi Karargâhı',
            'question': f"{u[1]} konusunun Kurtuluş Savaşı ve çağdaş Türkiye tarihindeki dönüm noktası nedir?",
            'solution': f"{u[3]} ilkesini kavramak ve bağımsızlık ruhunu LGS sorularında tam doğruya dönüştürmektir.",
            'weeklyGoal': u[3], 'evaluation': 'Haftalık LGS İnkılap Tarihi Deneme Föyü'
        })
    return {
        'title': '8. Sınıf',
        'subtitle': 'LGS T.C. İnkılap Tarihi ve Atatürkçülük (Sınav Odaklı)',
        'badge': 'LGS İnkılap Tarihi',
        'weeks': weeks_data
    }

print("Sosyal Bilgiler builder compiled.")
