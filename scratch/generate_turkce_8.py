# -*- coding: utf-8 -*-
"""
Generates 36 weeks for Grade 8 (LGS) Türkçe.
"""

def build_turkce_8():
    # 8. Sınıf LGS Türkçe Müfredatı
    weeks = [
        # 1-6: Fiilimsiler (Eylemsiler)
        {
            'theme': 'LGS Dil Bilgisi', 'subTheme': 'Fiilimsilere Giriş ve İsim-Fiiller (Mastar)',
            'code': 'TÜR.8.1.1', 'title': 'Fiilimsilerin Genel Özellikleri ve İsim-Fiil Ekleri (-ma, -ış, -mak)',
            'description': 'Fiil kök veya gövdelerine gelen yapım ekleriyle türeyip fiil gibi çekimlenemeyen; -ma, -ış, -mak (MA-YIŞ-MAK) ekleriyle oluşan isim-fiilleri modeller.',
            'process': ['a) Fiilimsilerin olumsuzluk eki (-ma/-me) alabildiğini kavrar.', 'b) Fiilimsilerin kip ve kişi eki alamayacağını, çekimli fiil olmadığını ayırt eder.'],
            'concepts': ['Fiilimsi (Eylemsi)', 'İsim-Fiil (Mastar)', '-ma / -ış / -mak', 'Olumsuzluk Eki Ayrımı'],
            'skills': ['Biçim Bilgisi Çözümleme', 'LGS Soru Kalıbı'], 'pedagogical': 'MAYIŞMAK şifresiyle isim-fiil ekleri somutlaştırılır.',
            'context': 'LGS Türkçe Dil Bilgisi', 'question': "'Kitap okumayı çok seviyorum' cümlesindeki isim-fiili ve ekini bulunuz.",
            'solution': "'Okumayı' sözcüğü -ma isim-fiil ekini almıştır.", 'weeklyGoal': 'İsim-fiil eklerini ve görevlerini doğru kavrama.',
            'evaluation': 'İsim-fiil tespit çalışma yaprağı'
        },
        {
            'theme': 'LGS Dil Bilgisi', 'subTheme': 'Kalıplaşmış İsimler ve İsim-Fiil Ayrımı',
            'code': 'TÜR.8.1.1', 'title': 'İsim-Fiil Eklerini Alarak Kalıcı İsim Haline Gelen Sözcükler',
            'description': 'Fiilimsi eki almasına rağmen bir varlığın veya kavramın kalıcı adı olan sözcükleri (ekmek, dolma, sarma, dondurma, çakmak, danışma, giriş, çıkış) fiilimsiden ayırt eder.',
            'process': ['a) Olumsuzluk eki \'-ma\' getirilebiliyorsa fiilimsi, getirilemiyorsa kalıcı isim olduğunu test eder.', 'b) \'Bahçeyi kazma\' (fiil) ile \'Elindeki kazma\' (kalıcı isim) farkını inceler.'],
            'concepts': ['Kalıplaşmış İsim', 'Kalıcı Ad', 'Olumsuzluk Testi', 'LGS Çeldirici'],
            'skills': ['Hassas Anlam Ayrıştırma', 'LGS Tuzaklarını Fark Etme'], 'pedagogical': 'Lokanta menüsü üzerinden dolma, sarma, kavurma kelimeleri incelenir.',
            'context': 'LGS Banko Soru Modeli', 'question': "'Annemin yaptığı sarmayı çok beğendim' cümlesindeki 'sarma' sözcüğü fiilimsi midir, kalıcı isim midir?",
            'solution': 'Bir yemeğin kalıcı adı olduğu için fiilimsi değil, kalıcı isimdir.', 'weeklyGoal': 'Kalıcı isimler ile isim-fiilleri hatasız ayırt etme.',
            'evaluation': 'Kalıcı isim vs İsim-fiil ayırt etme föyü'
        },
        {
            'theme': 'LGS Dil Bilgisi', 'subTheme': 'Sıfat-Fiiller (Ortaç)',
            'code': 'TÜR.8.1.2', 'title': 'Sıfat-Fiil Ekleri (-an, -ası, -mez, -ar, -dik, -ecek, -miş) ve Sıfat Görevi',
            'description': 'Fiil köklerine gelerek onları sıfat yapan ekleri (ANASIMEZARDIKECEKMİŞ şifresi); önündeki ismi niteleme görevini çözümler.',
            'process': ['a) \'Güler yüzlü insan\'daki \'güler\'in sıfat-fiil olduğunu saptar.', 'b) Sıfat tamlaması kurduğunu kavrar.'],
            'concepts': ['Sıfat-Fiil (Ortaç)', 'ANASIMEZARDIKECEKMİŞ', 'Sıfat Görevi', 'Niteleme'],
            'skills': ['Sıfat-Fiil Tespiti', 'Morfolojik Analiz'], 'pedagogical': 'ANASIMEZARDIKECEKMİŞ tekerlemesiyle ekler pekiştirilir.',
            'context': 'Edebî Metinler', 'question': "'Yıkılası dünyada güvenecek insan kalmadı' cümlesindeki sıfat-fiilleri bulunuz.",
            'solution': "'Yıkıl-ası (dünya)' ve 'güven-ecek (insan)' olmak üzere 2 adet sıfat-fiil vardır.", 'weeklyGoal': 'Sıfat-fiil eklerini ve sıfat tamlaması kurma işlevini kavrama.',
            'evaluation': 'Sıfat-fiil bulma çalışma kağıdı'
        },
        {
            'theme': 'LGS Dil Bilgisi', 'subTheme': 'Adlaşmış Sıfat-Fiil ve Zaman Eki Ayrımı',
            'code': 'TÜR.8.1.2', 'title': 'Adlaşmış Sıfat-Fiiller ve Kip Eki ile Sıfat-Fiil Ayrımı',
            'description': 'Sıfat-fiilin nitelediği isim düştüğünde adlaşmasını (\'Gelen gideni aratır\'); \'-mez, -ar, -dik, -ecek, -miş\' eklerinin kip eki (yüklem) mi yoksa sıfat-fiil eki mi olduğunu ayırt eder.',
            'process': ['a) Yüklemde yer alıp zaman bildiriyorsa çekimli fiil olduğunu saptar.', 'b) İsmin önüne gelip onu niteliyorsa sıfat-fiil olduğunu kanıtlar.'],
            'concepts': ['Adlaşmış Sıfat-Fiil', 'Kip Eki vs Sıfat-Fiil', 'LGS Soru Tuzağı'],
            'skills': ['Bağlamsal Ayrıştırma', 'LGS Kritik Düşünme'], 'pedagogical': "'Gelecek hafta gelecek' cümlesindeki iki 'gelecek' arasındaki fark çözümlenir.",
            'context': 'LGS Çıkmış Soru Formatı', 'question': "'Koşar adımlarla eve gitti' ile 'Her sabah sahilde bir saat koşar' cümlelerindeki 'koşar' sözcüklerinin görevleri sırasıyla nedir?",
            'solution': "Birincisi ismi nitelediği için sıfat-fiildir; ikincisi ise geniş zaman kipiyle çekimlenmiş bir çekimli fiildir.", 'weeklyGoal': 'Adlaşmış sıfat-fiilleri ve kip ekiyle karışan durumları çözme.',
            'evaluation': 'Adlaşmış sıfat-fiil analizi föyü'
        },
        {
            'theme': 'LGS Dil Bilgisi', 'subTheme': 'Zarf-Fiiller (Bağ-Fiil / Ulaç)',
            'code': 'TÜR.8.1.3', 'title': 'Zarf-Fiil Ekleri (-ken, -alı, -asiye, -meden, -ince, -ip, -arak, -dıkça, -e...-e, -r...-mez)',
            'description': 'Fiillere gelerek onları durum (Nasıl?) veya zaman (Ne zaman?) zarfı yapan zarf-fiil eklerini ve cümleye kattığı anlam ilgilerini çözümler.',
            'process': ['a) Zarf-fiillerin virgülle peş peşe sıralanmadığı sürece kendisinden sonra virgül ALMAYACAĞI kuralını kavrar.', 'b) Durum ve zaman anlamlarını ayırt eder.'],
            'concepts': ['Zarf-Fiil (Ulaç / Bağ-Fiil)', 'Durum Zarf-Fiili', 'Zaman Zarf-Fiili', 'Virgül Kuralı'],
            'skills': ['Zarf Görevi Analizi', 'Noktalama Uyumu'], 'pedagogical': 'KENYALI ASİYE İNCE İPİ ARAKLADIKÇA şifresi kullanılır.',
            'context': 'Hikâye Çözümlemesi', 'question': "'Çocuklar gülüşe gülüşe içeri girdiler' cümlesindeki zarf-fiili ve cümleye kattığı anlamı bulunuz.",
            'solution': "'-e ... -e' (gül-üş-e gül-üş-e) zarf-fiilidir ve cümleye 'durum' (nasıl girdi?) anlamı katmıştır.", 'weeklyGoal': 'Zarf-fiil eklerini ve cümleye kattığı durum-zaman anlamlarını tespit etme.',
            'evaluation': 'Zarf-fiil çalışma föyü'
        },
        {
            'theme': 'LGS Dil Bilgisi', 'subTheme': 'Fiilimsiler Karma Uygulama ve Sentez',
            'code': 'TÜR.8.1.4', 'title': 'Metin İçinde 3 Fiilimsi Türünün Sayılması ve Cümledeki Görevi',
            'description': 'Verilen paragraftaki tüm isim-fiil, sıfat-fiil ve zarf-fiilleri eksiksiz tespit eder; fiilimsilerin yan cümlecik oluşturduğu mantığını kavrar.',
            'process': ['a) Paragraftaki fiilimsi sayısını hatasız bulur.', 'b) Fiilimsinin cümlede özne, nesne veya zarf tümleci olabileceğini modeller.'],
            'concepts': ['Fiilimsi Karma', 'Yan Cümlecik', 'Fiilimsi Sayımı'],
            'skills': ['Bütüncül Morfoloji', 'LGS Sınav Pratiği'], 'pedagogical': 'MEB örnek fiilimsi soruları üzerinde analiz yapılır.',
            'context': 'LGS Denemesi', 'question': "Bir cümlede kaç tane fiilimsi varsa o kadar ne bulunur?",
            'solution': 'O kadar \'yan cümlecik\' (yan cümle) bulunur.', 'weeklyGoal': 'Fiilimsiler konusunu LGS düzeyinde 0 hatayla tamamlama.',
            'evaluation': 'Fiilimsiler LGS Tarama Testi'
        },

        # 7-11: Cümlenin Ögeleri
        {
            'theme': 'Cümlenin Ögeleri', 'subTheme': 'Temel Ögeler (Yüklem ve Özne)',
            'code': 'TÜR.8.2.1', 'title': 'Cümlenin Temel Ögeleri: Yüklem ve Özne (Gerçek, Gizli, Sözde Özne)',
            'description': 'Cümlenin yargı bildiren ana ögesi yüklemi bulmayı; yükleme sorulan \'Kim? Ne?\' (Yapan kim?) sorusuyla özneyi (gerçek, gizli ve sözde özne) bulmayı çözümler.',
            'process': ['a) Cümlenin ögeleri bulunurken tamlamaların, deyimlerin ve birleşik fiillerin ASLA BÖLÜNEMEYECEĞİNİ açıklar.', 'b) Önce yüklem sonra özne kuralını (Y-Ö-N) uygular.'],
            'concepts': ['Yüklem', 'Özne', 'Gerçek Özne', 'Gizli Özne', 'Sözde Özne', 'Tamlamalar Bölünmez'],
            'skills': ['Söz Dizimi Analizi', 'Söz Öbeği Koruma'], 'pedagogical': 'YÖN kuralı (Yüklem -> Özne -> Nesne) sıralaması öğretilir.',
            'context': 'LGS Öge Soruları', 'question': "'Gözlerinin içi parlayan çocuk, bize doğru koştu' cümlesinin öznesi hangi söz öbeğidir?",
            'solution': "'Koşan kim?' sorusunun cevabı olan 'Gözlerinin içi parlayan çocuk' sıfat tamlamasıdır ve bölünmeden özne alınır.", 'weeklyGoal': 'Yüklem ve özneyi söz öbeklerini bölmeden doğru bulma.',
            'evaluation': 'Yüklem ve özne bulma föyü'
        },
        {
            'theme': 'Cümlenin Ögeleri', 'subTheme': 'Nesne (Belirtili ve Belirtisiz Nesne)',
            'code': 'TÜR.8.2.1', 'title': 'Öznenin Yaptığı İşten Etkilenen Nesne (Belirtili: Kimi? Neyi?, Belirtisiz: Ne?)',
            'description': 'İsmin belirtme hâl ekini (-i) alarak \'Kimi? Neyi?\' sorularına cevap veren belirtili nesne ile yalın hâlde olup özne bulunduktan sonraki \'Ne?\' sorusuna cevap veren belirtisiz nesneyi modeller.',
            'process': ['a) Özne sorusu olan \'Ne?\' ile belirtisiz nesne sorusu olan \'Ne?\'yi karıştırmamak için YÖN kuralını uygular.', 'b) Cümle çözümlemeleri yapar.'],
            'concepts': ['Nesne (Düz Tümleç)', 'Belirtili Nesne (Neyi? Kimi?)', 'Belirtisiz Nesne (Ne?)', 'YÖN Kuralı'],
            'skills': ['Hassas Soru Yöneltme', 'Öge Ayrıştırma'], 'pedagogical': 'Özne bulunduktan sonra nesneye geçiş adımları şematize edilir.',
            'context': 'Dil Bilgisi Atölyesi', 'question': "'Ali dün akşam ilginç bir kitap okudu' cümlesindeki nesne ve türü nedir?",
            'solution': "'İlginç bir kitap' belirtisiz nesnedir ('Ali ne okudu?' sorusuna cevap verir).", 'weeklyGoal': 'Belirtili ve belirtisiz nesneleri doğru tespit etme.',
            'evaluation': 'Nesne bulma çalışma kağıdı'
        },
        {
            'theme': 'Cümlenin Ögeleri', 'subTheme': 'Yer Tamlayıcısı (Dolaylı Tümleç)',
            'code': 'TÜR.8.2.1', 'title': 'İsmin -e, -de, -den Hâl Eklerini Alan Yer Tamlayıcısı',
            'description': 'Yüklemin bildirdiği yargının yöneldiği, bulunduğu veya ayrıldığı yeri bildiren; \'Kime/Kimde/Kimden, Neye/Neyde/Neyden, Nereye/Nerede/Nereden\' (9 soru) sorularına cevap veren yer tamlayıcısını çözümler.',
            'process': ['a) Yer tamlayıcısının mutlaka -e, -de, -den eklerinden birini taşıması gerektiğini kavrar.', 'b) Yer-yön zarflarıyla (-e eki almamış içeri, dışarı) farkını ayırt eder.'],
            'concepts': ['Yer Tamlayıcısı (Dolaylı Tümleç)', '-e, -de, -den Ekleri', '9 Soru Kuralı'],
            'skills': ['Mekânsal Öge Tespiti', 'Ek ve Öge Uyumu'], 'pedagogical': 'Soruların sonundaki ek ile cevabın sonundaki ekin aynı olduğu kuralı gösterilir.',
            'context': 'LGS Cümle Tahlili', 'question': "'Öğrenciler teneffüste okul bahçesine çıktılar' cümlesindeki yer tamlayıcısı hangisidir?",
            'solution': "'Nereye çıktılar?' sorusunun cevabı olan 'okul bahçesine' ifadesidir.", 'weeklyGoal': 'Yer tamlayıcısını (dolaylı tümleç) hatasız bulabilme.',
            'evaluation': 'Yer tamlayıcısı tespit föyü'
        },
        {
            'theme': 'Ara Tatil', 'subTheme': '1. Dönem Ara Tatili',
            'code': 'TÜR.8.GENEL.1', 'title': 'Fiilimsiler ve Cümlenin Ögeleri LGS Kampı',
            'description': 'LGS çıkmış sorular ve MEB örnek soruları üzerinden ilk 9 haftanın analizi yapılır.',
            'process': ['a) Beceri temelli öge sorularını çözer.', 'b) Hatalı kazanımları giderir.'],
            'concepts': ['Genel Tekrar', 'LGS Hazırlık'], 'skills': ['Hızlı Soru Çözümü'],
            'pedagogical': 'Tatil MEB fasikülü çözülür.', 'context': 'LGS Kampı',
            'question': 'Cümlede ögeler bulunurken hangi söz öbekleri kesinlikle bölünemez?',
            'solution': 'İsim ve sıfat tamlamaları, deyimler, birleşik fiiller ve ikilemeler asla bölünemez.',
            'weeklyGoal': 'LGS ilk çeyrek konularını tamamlama.', 'evaluation': 'Ara Tatil LGS Denemesi'
        },
        {
            'theme': 'Cümlenin Ögeleri', 'subTheme': 'Zarf Tamlayıcısı (Zarf Tümleci)',
            'code': 'TÜR.8.2.1', 'title': 'Zaman, Durum, Miktar, Neden ve Vasıta Bildiren Zarf Tamlayıcısı',
            'description': 'Yükleme sorulan \'Nasıl?, Ne zaman?, Ne kadar?, Neden/Niçin?, Kiminle?, Neyle?\' sorularına cevap veren zarf tamlayıcısını; ek almamış yer-yön bildiren sözcükleri (içeri girdi) çözümler.',
            'process': ['a) \'Aşağı indi\' (Zarf tamlayıcısı) ile \'Aşağıya indi\' (Yer tamlayıcısı) farkını kavrar.', 'b) Fiilimsilerin zarf tamlayıcısı kurduğunu modeller.'],
            'concepts': ['Zarf Tamlayıcısı (Zarf Tümleci)', 'Durum / Zaman / Miktar', 'Yer-Yön Zarfı Ayrımı', 'Ek Almama Kuralı'],
            'skills': ['Cümle Katmanı Analizi', 'İnce Dil Bilgisi'], 'pedagogical': "'İçeri' (zarf tamlayıcısı) ve 'İçeriye' (yer tamlayıcısı) tahtada karşılaştırılır.",
            'context': 'LGS Soru Kalıbı', 'question': "'Güneş batarken sahil kenarında sessizce yürüdük' cümlesindeki zarf tamlayıcılarını bulunuz.",
            'solution': "'Ne zaman yürüdük? -> Güneş batarken' ve 'Nasıl yürüdük? -> Sessizce' olmak üzere 2 ayrı zarf tamlayıcısı vardır.", 'weeklyGoal': 'Zarf tamlayıcılarını sorularıyla eksiksiz saptama.',
            'evaluation': 'Zarf tamlayıcısı çalışma föyü'
        },
        {
            'theme': 'Cümlenin Ögeleri', 'subTheme': 'Cümle Vurgusu ve Ara Söz',
            'code': 'TÜR.8.2.2', 'title': 'Cümlede Vurgulanan Ögeyi Bulma ve İki Virgül Arasındaki Ara Sözler',
            'description': 'Fiil cümlelerinde vurgunun yüklemden hemen önceki ögede olduğunu; isim cümlelerinde vurgunun yüklemin kendisinde olduğunu; iki virgül veya iki kısa çizgi arasındaki ara sözleri çözümler.',
            'process': ['a) \'Ahmet dün beni aradı\' (Vurgu: Nesne) cümlesinde vurgunun yerini değiştirerek test eder.', 'b) Ara sözün hangi ögenin açıklayıcısı olduğunu belirler.'],
            'concepts': ['Cümle Vurgusu', 'Fiil Cümlesinde Vurgu', 'İsim Cümlesinde Vurgu', 'Ara Söz / Ara Cümle'],
            'skills': ['Vurgu Analizi', 'Ara Söz Tespiti'], 'pedagogical': 'Cümledeki kelimelerin yeri değiştirilerek vurgulanan öge dinletilir.',
            'context': 'Hitabet ve LGS Soruları', 'question': "'İzmir'i, doğup büyüdüğü şehri, çok özlemişti' cümlesindeki ara söz hangi ögenin açıklayıcısıdır?",
            'solution': "'Neyi özlemişti? -> İzmir'i' belirtili nesne olduğuna göre ara söz 'belirtili nesnenin açıklayıcısıdır'.", 'weeklyGoal': 'Cümle vurgusunu ve ara sözleri hatasız tespit etme.',
            'evaluation': 'Cümlenin ögeleri karma LGS testi'
        },

        # 12-16: Cümle Türleri
        {
            'theme': 'Cümle Türleri', 'subTheme': 'Yüklemin Türüne ve Yerine Göre Cümleler',
            'code': 'TÜR.8.3.1', 'title': 'Fiil (Eylem) ve İsim (Ad) Cümleleri; Kurallı, Devrik ve Eksiltili Cümleler',
            'description': 'Yüklemi çekimli fiil olan fiil cümleleri ile ek fiil almış isim/isim soylu olan isim cümlelerini; yüklemi sonda olan kurallı, sonda olmayan devrik ve yüklemi bulunmayan eksiltili (...) cümleleri modeller.',
            'process': ['a) Sesteş yüklemleri (Ör: \'varmak\' eylemi vs \'var\' mevcut ismi) bağlamından çözer.', 'b) Eksiltili cümlenin sonuna üç nokta konduğunu kavrar.'],
            'concepts': ['Fiil Cümlesi', 'İsim Cümlesi', 'Kurallı Cümle', 'Devrik Cümle', 'Eksiltili Cümle (...)'],
            'skills': ['Cümle Sınıflandırma', 'Söz Dizimi Analizi'], 'pedagogical': 'Şiir dizeleri (devrik cümleler) kurallı cümleye çevrilir.',
            'context': 'Metin Çözümlemesi', 'question': "'Bugün hava çok güzeldi' cümlesi yükleminin türüne ve yerine göre nasıl bir cümledir?",
            'solution': "Yüklemi isim soylu olduğu için 'isim cümlesi', yüklemi sonda olduğu için 'kurallı cümle'dir.", 'weeklyGoal': 'Cümleleri yüklemin türü ve yerine göre doğru sınıflandırma.',
            'evaluation': 'Yüklemin türü ve yerine göre cümleler tablosu'
        },
        {
            'theme': 'Cümle Türleri', 'subTheme': 'Anlamına Göre Cümleler',
            'code': 'TÜR.8.3.2', 'title': 'Olumlu, Olumsuz, Soru ve Biçimce-Anlamca Cümleler',
            'description': 'Eylemin yapıldığını bildiren olumlu; yapılmadığını bildiren olumsuz (-me/-ma, değil, yok, -sız); biçimce olumsuz anlamca olumlu (\'Seni sevmiyor değilim\' = Seviyorum) ve biçimce olumlu anlamca olumsuz (\'Ne aradı ne sordu\' = Aramadı) cümleleri modeller.',
            'process': ['a) Mantıksal anlam ile ahlaki beğeniyi karıştırmaz (Ör: \'Hırsız yakalandı\' olumlu cümledir).', 'b) Sözde soru cümlelerini açıklar.'],
            'concepts': ['Olumlu Cümle', 'Olumsuz Cümle', 'Biçimce Olumsuz Anlamca Olumlu', 'Biçimce Olumlu Anlamca Olumsuz', 'Soru Cümlesi'],
            'skills': ['Anlamsal Derinlik', 'Mantık Dönüşümü'], 'pedagogical': "'Ne ... ne' bağlacının cümleyi anlamca olumsuz yaptığı gösterilir.",
            'context': 'LGS Çeldirici Soruları', 'question': "'Bu manzaraya hayran olmamak elde değil' cümlesi biçimce ve anlamca nasıldır?",
            'solution': "Biçimce olumsuz (değil var), anlamca ise olumludur (yani herkes hayran olur).", 'weeklyGoal': 'Biçimce ve anlamca cümle farklılıklarını hatasız çözme.',
            'evaluation': 'Anlamına göre cümleler çalışma kağıdı'
        },
        {
            'theme': 'Cümle Türleri', 'subTheme': 'Yapısına Göre Cümleler: Tek Yüklemli (Basit) Cümle',
            'code': 'TÜR.8.3.3', 'title': 'Tek Bir Yargı Bildiren ve İçinde Fiilimsi Bulunmayan Cümleler',
            'description': 'İçinde tek bir yüklem bulunan ve hiçbir yan cümlecik (fiilimsi, alıntı, şart kipi) barındırmayan tek yüklemli (basit) cümle yapısını çözümler.',
            'process': ['a) Cümlenin uzunluğunun basitliği etkilemediğini kavrar.', 'b) Birden fazla ögesi olsa da tek yargı taşıdığını gösterir.'],
            'concepts': ['Tek Yüklemli Cümle', 'Basit Cümle', 'Tek Yargı', 'Yan Cümleciksiz'],
            'skills': ['Yapı Analizi', 'Yargı Sayımı'], 'pedagogical': 'Uzun ama tek yüklemli cümle örnekleri incelenir.',
            'context': 'Cümle Mimarisi', 'question': "'Okulun bahçesindeki ulu çınarın gölgesinde saatlerce oturduk' cümlesi yapısına göre nasıldır?",
            'solution': "Tek bir yüklemi olduğu ve içinde hiç fiilimsi bulunmadığı için 'tek yüklemli (basit) cümle'dir.", 'weeklyGoal': 'Tek yüklemli cümleleri doğru tespit etme.',
            'evaluation': 'Tek yüklemli cümle analiz föyü'
        },
        {
            'theme': 'Cümle Türleri', 'subTheme': 'Yapısına Göre: Fiilimsili (Birleşik) Cümle',
            'code': 'TÜR.8.3.3', 'title': 'İçinde Fiilimsi Bulunan Cümleler (Girişik Birleşik Cümle)',
            'description': 'Bir temel yüklemin yanında en az bir adet fiilimsi (yan cümlecik) barındıran fiilimsili cümle yapısını çözümler; LGS\'de en çok çıkan cümle türü olduğunu modeller.',
            'process': ['a) Temel cümle ile yan cümlecik öge ilişkisini kurar.', 'b) İç içe birleşik (alıntı cümleli) ve şartlı birleşik cümleleri inceler.'],
            'concepts': ['Fiilimsili Cümle', 'Girişik Birleşik', 'Temel Cümle', 'Yan Cümlecik'],
            'skills': ['LGS Banko Soru Çözümü', 'Yan Cümlecik Tespiti'], 'pedagogical': 'Cümledeki fiilimsiler yuvarlak içine alınarak yan cümleler sayılır.',
            'context': 'LGS Cümle Türleri Soruları', 'question': "'Ders çalışan öğrenciler sınavda başarılı olur' cümlesi yapısına göre nasıldır ve kaç yan cümleciği vardır?",
            'solution': "'Çalışan' sıfat-fiilini içerdiği için 'fiilimsili (birleşik) cümle'dir ve 1 adet yan cümleciği vardır.", 'weeklyGoal': 'Fiilimsili cümleleri ve yan cümleciklerini hatasız bulma.',
            'evaluation': 'Fiilimsili cümle tespit föyü'
        },
        {
            'theme': 'Cümle Türleri', 'subTheme': 'Birden Çok Yüklemli (Sıralı) ve Bağlaçlı Cümleler',
            'code': 'TÜR.8.3.3', 'title': 'Virgülle Ayrılan Sıralı Cümleler ve Bağlaçla Bağlanan Bağlaçlı Cümleler',
            'description': 'En az iki yüklemin virgül veya noktalı virgülle bağlanmasına birden çok yüklemli (sıralı: \'Geldim, gördüm, yendim\'); bağlaçlarla bağlanmasına bağlaçlı cümle (\'Kitabı okudu ama beğenmedi\') dendiğini ayırt eder.',
            'process': ['a) Bağımlı sıralı (öge ortaklığı olan) ve bağımsız sıralı cümleleri çözümler.', 'b) Cümle türleri 4\'lü analiz tablosunu (Yüklemin Türü, Yeri, Anlamı, Yapısı) doldurur.'],
            'concepts': ['Birden Çok Yüklemli (Sıralı)', 'Bağlaçlı Cümle', 'Öge Ortaklığı', '4 Boyutlu Cümle Analizi'],
            'skills': ['Bütüncül Cümle Analizi', 'LGS Matris Çözümü'], 'pedagogical': 'Her öğrenciye bir cümle verilip 4 özelliği birden tespit ettirilir.',
            'context': 'LGS Cümle Türleri Sentezi', 'question': "'Yağmur dindi, güneş açtı' cümlesi yapısına göre nasıldır?",
            'solution': "İki ayrı yüklem virgülle bağlandığı için 'birden çok yüklemli (sıralı) cümle'dir.", 'weeklyGoal': 'Cümle türlerini tüm boyutlarıyla eksiksiz çözümleme.',
            'evaluation': 'Cümle türleri 4 boyutlu analiz föyü'
        },

        # 17-21: Fiilde Çatı
        {
            'theme': 'Fiilde Çatı', 'subTheme': 'Çatı Kavramı ve İsim Cümlesi Kuralı',
            'code': 'TÜR.8.4.1', 'title': 'Fiilde Çatı Nedir ve İsim Cümlelerinde Çatı Aranmaz Kuralı',
            'description': 'Fiillerin özne ve nesnelerine göre gösterdikleri özelliklere çatı dendiğini; YÜKLEMİ İSİM SOYLU OLAN CÜMLELERDE ÇATI ÖZELLİĞİ ARANMAYACAĞINI modeller.',
            'process': ['a) LGS\'de \'Hangisinde çatı aranmaz?\' sorusunun cevabının isim cümlesi olduğunu kavrar.', 'b) Fiil soylu yüklemleri tespit eder.'],
            'concepts': ['Fiilde Çatı', 'İsim Cümlesinde Çatı Aranmaz', 'LGS Tuzağı'],
            'skills': ['Ön Koşul Denetimi', 'Hata Önleme'], 'pedagogical': 'Kırmızı dur işaretiyle isim yüklemlerde çatının aranmayacağı zihne kazınır.',
            'context': 'LGS Çatı Soruları', 'question': "'Dün hava çok soğuktu' cümlesinde neden öznesine veya nesnesine göre çatı aranmaz?",
            'solution': "Çünkü cümlenin yüklemi olan 'soğuktu' sözcüğü bir fiil değil, ek fiil almış bir isimdir (isim cümlelerinde çatı aranmaz).", 'weeklyGoal': 'Çatı arama kuralını ve isim cümlesi istisnasını bilme.',
            'evaluation': 'Çatı aranır mı aranmaz mı etkinliği'
        },
        {
            'theme': 'Fiilde Çatı', 'subTheme': 'Öznesine Göre Fiiller: Etken ve Edilgen Çatı',
            'code': 'TÜR.8.4.1', 'title': 'Gerçek Özneli Etken Fiiller ile -l/-n Eki Alan Sözde Özneli Edilgen Fiiller',
            'description': 'İşi yapan gerçek/gizli bir öznesi olan fiillere etken; işi yapanın belli olmayıp yüklemin \'-l, -n\' eklerini aldığı ve sözde öznesi olan fiillere edilgen çatı dendiğini çözümler.',
            'process': ['a) \'Ali camı kırdı\' (Etken) ile \'Cam kırıldı\' (Edilgen) farkını modeller.', 'b) \'Tarafından\' veya \'-ca/-ce\' ile örtülü özne yapısını inceler.'],
            'concepts': ['Etken Fiil (İşi Yapan Belli)', 'Edilgen Fiil (-l, -n Eki)', 'Sözde Özne', 'Örtülü Özne'],
            'skills': ['Özne-Yüklem Bağıntısı', 'LGS Çatı Çözümü'], 'pedagogical': 'DedeKTİF oyunuyla işi yapan ortada mı gizli mi araştırılır.',
            'context': 'Haber Metinleri ve Hukuk Dili', 'question': "'Sokaklar belediye ekipleri tarafından sabaha kadar temizlendi' cümlesinin çatısı öznesine göre nedir?",
            'solution': "Temizle-n-di fiili -n eki aldığı ve sokaklar sözde özne olduğu için 'edilgen çatılı' bir fiildir.", 'weeklyGoal': 'Etken ve edilgen fiilleri hatasız ayırt etme.',
            'evaluation': 'Etken-Edilgen çatı sınıflandırma tablosu'
        },
        {
            'theme': 'Fiilde Çatı', 'subTheme': 'Nesnesine Göre Fiiller ve Çatı Karma Analizi',
            'code': 'TÜR.8.4.1', 'title': 'Geçişli ve Geçişsiz Fiiller ile 1. Dönem Çatı Sentezi',
            'description': 'Başına \'Onu\' sözcüğü getirildiğinde anlamlı olan geçişli fiiller ile nesne alamayan geçişsiz fiilleri modeller; etken-edilgen ve geçişli-geçişsiz ikili çatı analizini ve 1. dönem dil bilgisi sentezini tamamlar.',
            'process': ['a) Cümlede nesne yazmasa bile fiilin geçişli olabileceğini (Ör: \'Sabahtan beri bekliyor\') kanıtlar.', 'b) \'Onu\' sağlamasını pratik olarak uygular.'],
            'concepts': ['Geçişli Fiil', 'Geçişsiz Fiil', 'İkili Çatı Analizi', '1. Dönem Sentezi'],
            'skills': ['Pratik Formül Uygulama', 'Geçişlilik Testi'], 'pedagogical': "'Onu' anahtarı testiyle fiillerin kilitleri açılır.",
            'context': 'LGS Pratik Metotları', 'question': "'Yazar, yeni romanını geçen ay bitirdi' cümlesinin çatısını iki yönden de belirtiniz.",
            'solution': "Öznesine göre 'etken' (yazar yapmıştır), nesnesine göre 'geçişli'dir (onu bitirdi / romanını).", 'weeklyGoal': 'Geçişli-geçişsiz çatı analizini eksiksiz tamamlama.',
            'evaluation': 'Fiilde çatı LGS tarama testi'
        },
        {
            'theme': '1. Dönem Finali', 'subTheme': '1. Dönem LGS Türkçe Denemesi',
            'code': 'TÜR.8.GENEL.2', 'title': 'Fiilimsiler, Ögeler, Cümle Türleri ve Çatı Konuları Dönem Finali',
            'description': '1. dönemin tüm dil bilgisi üniteleri ile sözel mantık ve paragraf becerilerini kapsayan 20 soruluk LGS Türkçe tam denemesi yapılır.',
            'process': ['a) Sınav süresini (40 dk) verimli kullanır.', 'b) Yanlış analiz formu doldurur.'],
            'concepts': ['LGS Denemesi', 'Dönem Sonu Başarısı'], 'skills': ['Sınav Kondisyonu'],
            'pedagogical': 'Optik form ile gerçek sınav simülasyonu uygulanır.', 'context': 'LGS Dönem Sonu Sınavı',
            'question': 'LGS Türkçe testinde dil bilgisi soruları ortalama kaç net getirir ve önemi nedir?',
            'solution': 'Ortalama 4-5 soru doğrudan dil bilgisinden gelir; kuralları bilindiğinde en hızlı ve kesin puan getiren bölümdür.', 'weeklyGoal': '1. dönem konularından 0 hata ile LGS hedefine ilerleme.',
            'evaluation': '1. Dönem Sonu LGS Türkçe Başarı Karnesi'
        },

        # 22-25: Anlatım Bozuklukları
        {
            'theme': 'Anlatım Bozuklukları', 'subTheme': 'Anlama Dayalı Bozukluklar (Bağdaşıklık)',
            'code': 'TÜR.8.5.1', 'title': 'Gereksiz Sözcük Kullanımı ve Çelişen Sözcüklerin Bir Arada Bulunması',
            'description': 'Eş anlamlı sözcüklerin birlikte kullanılması (\'İlgi ve alaka gösterdi\') veya anlamı başka sözcükte bulunan kelimelerin gereksiz kullanımı ile çelişen ifadelerin (\'Şüphesiz sınavı kazanmış olabilir\') yarattığı bozuklukları düzeltir.',
            'process': ['a) Duru ve yalın anlatım kurallarını kavrar.', 'b) Cümleden gereksiz kelimeyi atarak anlamı berraklaştırır.'],
            'concepts': ['Gereksiz Sözcük', 'Çelişen Sözler', 'Duru Anlatım', 'Yalınlık'],
            'skills': ['Cümle Cerrahlığı', 'İfade Düzeltme'], 'pedagogical': 'Hatalı cümleler ameliyat masasına yatırılarak gereksiz kelimeler cımbızla ayıklanır.',
            'context': 'Türkçenin Doğru Kullanımı', 'question': "'Tam olarak yaklaşık yirmi kişi toplantıya katıldı' cümlesindeki anlatım bozukluğu nedir ve nasıl düzeltilir?",
            'solution': "'Tam olarak' (kesinlik) ile 'yaklaşık' (ihtimal) çelişen sözcüklerdir; biri cümleden atılmalıdır.", 'weeklyGoal': 'Anlama dayalı anlatım bozukluklarını saptayıp düzeltme.',
            'evaluation': 'Anlatım bozukluğu düzeltme föyü'
        },
        {
            'theme': 'Anlatım Bozuklukları', 'subTheme': 'Sözcüğün Yanlış Yerde ve Yanlış Anlamda Kullanımı',
            'code': 'TÜR.8.5.1', 'title': 'Sözcük Sıralaması Hataları ve Anlam İnceliklerinin Karıştırılması',
            'description': "'Çok güneşte kalma' yerine 'Güneşte çok kalma'; 'Öğretim ücreti' yerine 'Öğrenim ücreti', 'fiyat-ücret', 'ekmek-dikmek' gibi birbirine karıştırılan sözcüklerin yol açtığı bozuklukları çözer.",
            'process': ['a) \'Fidan ekilmez, dikilir; tohum ekilir\' kuralını inceler.', 'b) Yanlış sıralamanın mantık hatasına yol açtığını kavrar.'],
            'concepts': ['Sözcüğün Yanlış Yerde Kullanımı', 'Yanlış Anlamda Kullanım', 'Sözcük Sırası'],
            'skills': ['Kelime Hassasiyeti', 'Mantıksal Sıralama'], 'pedagogical': "'İlk aklıma gelen' mi 'Aklıma ilk gelen' mi tartışması yapılır.",
            'context': 'Haber Bülteni Hataları', 'question': "'Yeni okula geldim ki zil çaldı' cümlesindeki anlatım bozukluğu nasıl giderilir?",
            'solution': "'Okula yeni geldim ki zil çaldı' şeklinde 'yeni' sözcüğü fiilin önüne getirilerek düzeltilir.", 'weeklyGoal': 'Sözcük sırası ve kelime seçimi kaynaklı bozuklukları giderme.',
            'evaluation': 'Sözcük sırası hataları tarama testi'
        },
        {
            'theme': 'Anlatım Bozuklukları', 'subTheme': 'Dil Bilgisine Dayalı Bozukluklar (Bağlaşıklık)',
            'code': 'TÜR.8.5.2', 'title': 'Özne-Yüklem Uyumsuzluğu ve Ek Fiil Eksikliği',
            'description': 'Öznenin insan dışı çoğul varlık olduğunda yüklemin tekil olması kuralını (\'Kuşlar uçuyorlar\' YANLIŞ -> \'Kuşlar uçuyor\'); olumluluk-olumsuzluk uyumunu (\'Kimse gelmedi, ders dinledi\' YANLIŞ -> \'Herkes dinledi\') ve ek fiil eksikliklerini çözümler.',
            'process': ['a) \'Ali ve ben\' öznesinin yükleminin \'biz\' (1. çoğul) olması gerektiğini kavrar.', 'b) Kişi uyumunu modeller.'],
            'concepts': ['Özne-Yüklem Uyumu', 'Tekillik-Çoğulluk', 'Kişi Uyumu', 'Ek Fiil Eksikliği'],
            'skills': ['Dil Bilgisel Uyum', 'Bağlaşıklık'], 'pedagogical': 'Özne-yüklem uyum kuralları formül tablosu yapılır.',
            'context': 'LGS Dil Bilgisi Bozuklukları', 'question': "'Ağaçlar sonbaharda yapraklarını döküyorlar' cümlesindeki anlatım bozukluğu nedir?",
            'solution': 'İnsan dışı varlıklar çoğul özne olduğunda yüklem tekil olmalıdır: \'yapraklarını döküyor\' denmelidir.', 'weeklyGoal': 'Özne-yüklem uyumsuzluklarını kuralına göre tespit etme.',
            'evaluation': 'Özne-yüklem uyumu çalışma föyü'
        },
        {
            'theme': 'Anlatım Bozuklukları', 'subTheme': 'Öge Eksiklikleri ve Tamlama Hataları',
            'code': 'TÜR.8.5.2', 'title': 'Sıralı ve Bağlaçlı Cümlelerde Nesne, Dolaylı Tümleç ve Yüklem Eksikliği',
            'description': 'Sıralı cümlelerde birinci cümlenin ögesinin ikinci cümleye uymamasından doğan nesne eksikliği (\'Kardeşine yardım etti, çok seviyordu\' -> \'Onu çok seviyordu\'); dolaylı tümleç eksikliği ve tamlama yanlışlarını modeller.',
            'process': ['a) İsim ve sıfatın aynı tamlanana bağlanamayacağını (\'Siyasi ve ekonomi kriz\' YANLIŞ -> \'Siyasi kriz ve ekonomik kriz\') açıklar.', 'b) Çatı uyuşmazlığını inceler.'],
            'concepts': ['Öge Eksikliği', 'Nesne Eksikliği', 'Dolaylı Tümleç Eksikliği', 'Tamlama Hatası', 'Çatı Uyuşmazlığı'],
            'skills': ['Karmaşık Cümle Onarımı', 'Dil Bilgisel Simetri'], 'pedagogical': 'İki vagonlu tren modeliyle ortak kullanılan parçanın her iki vagona da uyması gerektiği gösterilir.',
            'context': 'LGS İleri Düzey Dil Bilgisi', 'question': "'Arkadaşına güvendi ve her sırrını anlattı' cümlesinde hangi öge eksikliği vardır?",
            'solution': "'Kime anlattı?' sorusunun cevabı olan 'ona' (yer tamlayıcısı / dolaylı tümleç) eksikliği vardır.", 'weeklyGoal': 'Öge eksikliklerini ve tamlama hatalarını hatasız onarma.',
            'evaluation': 'Anlatım bozuklukları genel LGS testi'
        },

        # 26-29: Yazım, Noktalama ve Edebî Sanatlar
        {
            'theme': 'Yazım ve Noktalama', 'subTheme': 'LGS Banko Yazım Kuralları',
            'code': 'TÜR.8.6.1', 'title': 'Birleşik Sözcüklerin Yazımı, Kısaltmalar ve Kesme İşareti',
            'description': 'Ses düşmesi/türemesiyle bitişik yazılan birleşik fiiller (hissetmek, kaybolmak); sözcüklerden birinin anlam kaymasına uğradığı birleşik isimler (kuşburnu, hanımeli); TDK kısaltmalarına gelen ekler (TDK\'nin - \'te de ka\' kuralı) ve kesme işaretini modeller.',
            'process': ['a) Türkçede \'ka\' sesinin olmadığını, \'ke\' olduğunu (TDK\'ye) uygular.', 'b) Kurum ve kuruluş adlarına gelen eklerin kesmeyle AYRILMAYACAĞINI kavrar.'],
            'concepts': ['Birleşik Sözcük Yazımı', 'Kısaltmalar (TDK\'nin)', 'Kesme İşareti Kuralı', 'Kurum Adları İstisnası'],
            'skills': ['Yazım Kılavuzu Uzmanlığı', 'LGS Puan Avcısı'], 'pedagogical': "TDK'nın değil TDK'nin kuralı sınıfta vurgulanır.",
            'context': 'LGS Yazım Soruları', 'question': "Türk Dil Kurumu'na mı yoksa Türk Dil Kurumuna mı yazılır? Neden?",
            'solution': 'Kesme işareti kullanılmadan \'Türk Dil Kurumuna\' şeklinde yazılır; kurum, kuruluş ve kurul adlarına gelen ekler kesmeyle ayrılmaz.', 'weeklyGoal': 'LGS yazım kuralları tuzaklarına düşmeden tam puan alma.',
            'evaluation': 'LGS yazım kuralları tarama föyü'
        },
        {
            'theme': 'Yazım ve Noktalama', 'subTheme': 'Noktalama İşaretleri LGS Provası',
            'code': 'TÜR.8.6.2', 'title': 'Virgül, Noktalı Virgül, İki Nokta, Tırnak ve Kısa Çizgi Ayrımı',
            'description': 'LGS\'de paragraf içindeki yay ayraçlara doğru noktalama işaretlerini yerleştirme; virgülün görevleri (sıralı cümle, eş görevli sözcük, ara söz, hitap) üzerinde yoğunlaşır.',
            'process': ['a) Şart ekinden (-se/-sa), zarf-fiil ekinden ve \'ve/veya\' bağlaçlarından sonra virgül KONMAYACAĞINI kavrar.', 'b) Metin tamamlama yapar.'],
            'concepts': ['Virgül Yasakları', 'Noktalı Virgül', 'İki Nokta', 'Tırnak İşareti', 'Yay Ayraç'],
            'skills': ['Noktalama Hiyerarşisi', 'Paragraf İçi Yerleştirme'], 'pedagogical': 'Boş parantezli MEB çıkmış soruları adım adım analiz edilir.',
            'context': 'LGS Noktalama Denemesi', 'question': 'Bir cümlede şart eki (-se/-sa) almış bir sözcükten hemen sonra virgül konur mu?',
            'solution': 'Kesinlikle konmaz; Türkçede şart ekinden ve zarf-fiil ekinden sonra virgül konulması kural dışıdır.', 'weeklyGoal': 'Noktalama işaretlerini sıfır hatayla yerleştirme.',
            'evaluation': 'LGS noktalama tamamlama testi'
        },
        {
            'theme': 'Ara Tatil', 'subTheme': '2. Dönem Ara Tatili',
            'code': 'TÜR.8.GENEL.3', 'title': 'LGS Türkçe Büyük Soru Çözüm Kampı',
            'description': 'Tüm dil bilgisi, sözel mantık ve metin türleri çıkmış LGS soruları masaya yatırılır.',
            'process': ['a) Günde 50 yeni nesil Türkçe sorusu çözer.'],
            'concepts': ['LGS Kampı', 'Maraton'], 'skills': ['Yüksek Başarı'],
            'pedagogical': 'Tatil soru kampı takip çizelgesi uygulanır.', 'context': 'Tatil Kampı',
            'question': 'LGS Türkçe testinde zaman kaybetmemek için en etkili okuma stratejisi nedir?',
            'solution': 'Gözle blok okuma yapmak, dudak kıpırdatmamak ve sorunun ne istediğini (olumsuz soru kökü, altı çizili ifade) ilk adımda netleştirmektir.',
            'weeklyGoal': 'LGS Türkçe netlerini 18+ seviyesine sabitleme.', 'evaluation': 'LGS 2. Ara Tatil Deneme Sınavı'
        },
        {
            'theme': 'Metin Türleri ve Söz Sanatları', 'subTheme': 'Edebî Türler ve 5 Söz Sanatı',
            'code': 'TÜR.8.7.1', 'title': 'Deneme, Makale, Söyleşi, Fıkra ve Benzetme, Abartma, Kişileştirme, Konuşturma, Tezat',
            'description': 'Kanıtlama amacı olan makale; yazarın kendi kendine konuştuğu deneme; okuyucuyla sohbet ettiği söyleşi; gazete köşe yazısı fıkra ile 5 büyük söz sanatını (Teşbih, Mübalağa, Teşhis, İntak, Tezat/Zıtlık) çözümler.',
            'process': ['a) \'Ağlarım hatıra geldikçe gülüştüklerimiz\' dizesindeki tezat (zıtlık) sanatını saptar.', 'b) Makale ile denemenin üslup farkını karşılaştırır.'],
            'concepts': ['Makale (Kanıtlı)', 'Deneme (Ben Dili)', 'Söyleşi (Sohbet)', 'Köşe Yazısı (Fıkra)', 'Tezat (Karşıtlık)'],
            'skills': ['Metin Türü Tespiti', 'Edebî Derinlik'], 'pedagogical': 'Farklı türlerden aynı konuyu işleyen 4 paragraf karşılaştırılır.',
            'context': 'Edebiyat ve Medya', 'question': "'Neden böyle düşman görünürsünüz / Yıllar yılı dost bildiğim aynalar' dizelerindeki söz sanatı nedir?",
            'solution': "'Düşman' ile 'dost' sözcükleri arasında 'tezat' (karşıtlık) sanatı vardır.", 'weeklyGoal': 'Metin türlerini ve 5 söz sanatını hatasız ayırt etme.',
            'evaluation': 'Edebî türler ve söz sanatları föyü'
        },

        # 30-33: Sözel Mantık, Muhakeme ve Görsel Okuma
        {
            'theme': 'Sözel Mantık ve Muhakeme', 'subTheme': 'LGS Sözel Mantık Çözüm Stratejileri',
            'code': 'TÜR.8.8.1', 'title': 'Değişken Sayısına Göre Doğru Tablo Kurma ve İhtimal Ağacı',
            'description': 'Kişiler, günler, mekanlar ve eşyalar arasındaki ilişkileri çok boyutlu matris tablosu çizerek çözme; kesin doğruları (+) kesin yanlışları (-) ile işaretleme stratejisini modeller.',
            'process': ['a) Tablonun sabit eksenine günleri veya yerleri koymayı öğrenir.', 'b) Olumsuz ihtimalleri eleyerek kesin bilgiye ulaşır.'],
            'concepts': ['Sözel Mantık Matrisi', 'İhtimal Ağacı', 'Sabit Eksen', 'Kesin Çıkarım'],
            'skills': ['Üst Düzey Analitik Akıl Yürütme', 'LGS Mantık Çözücülüğü'], 'pedagogical': 'MEB LGS sözel mantık soru kalıpları tahtada adım adım çözülür.',
            'context': 'LGS Belirleyici Soru Formatı', 'question': 'Sözel mantık sorularında gün veya kat gibi sıralı unsurlar varsa tablo kurulurken bu unsurlar nereye yerleştirilmelidir?',
            'solution': 'Tablonun sabit eksenine (başlık satırına veya sol sütuna) sıralı olarak yazılmalıdır.', 'weeklyGoal': 'Sözel mantık sorularını 2-3 dakikada hatasız çözme becerisi edinme.',
            'evaluation': 'Sözel mantık soru çözümleri föyü'
        },
        {
            'theme': 'Görsel Okuma ve İnfografik', 'subTheme': 'İnfografik, Kroki, Harita ve Görsel Yorumlama',
            'code': 'TÜR.8.8.2', 'title': 'Grafik Verilerini Sözel Metne Eşleştirme ve İnfografik Analizi',
            'description': 'MEB ve TÜİK infografiklerini, metro krokilerini, yön haritalarını okuyup çıkarılan sonuçları değerlendirir; pasta, sütun ve çizgi grafiklerinin sözel karşılığını bulur.',
            'process': ['a) \'Bu infografikten hangisine ulaşılamaz?\' sorularını çözer.', 'b) Harita üzerindeki yön ve güzergâh takibini hatasız yapar.'],
            'concepts': ['İnfografik', 'Kroki Okuma', 'Veri Grafikleri', 'Çoklu Görsel Analizi'],
            'skills': ['Görsel Okuryazarlık', 'Veri Transferi'], 'pedagogical': 'Renkli şehir krokisi üzerinden yönerge takip oyunu oynatılır.',
            'context': 'LGS Görsel Okuma Soruları', 'question': 'Bir infografik sorusunu çözerken nelere çok dikkat edilmelidir?',
            'solution': 'Dipnotlara, küçük yazılmış istisnalara, renk kodlarına ve görseldeki oran-yüzde ifadelerine harfiyen dikkat edilmelidir.', 'weeklyGoal': 'Görsel, infografik ve grafik sorularını tam isabetle çözme.',
            'evaluation': 'İnfografik analiz föyü'
        },
        {
            'theme': 'Paragrafta Anlam ve Yapı', 'subTheme': 'Paragrafta Yapı, Akış ve İkiye Bölme',
            'code': 'TÜR.8.8.3', 'title': 'Akışı Bozan Cümle, Paragrafı İkiye Bölme ve Cümle Yerleştirme',
            'description': 'Farklı bir konuya veya konunun farklı bir yönüne geçilen cümleden itibaren paragrafın ikiye bölüneceğini; düşüncenin akışını bozan ilgisiz cümleyi bulmayı çözer.',
            'process': ['a) Zamir ve bağlaçların bağlantı gücünü denetler.', 'b) Paragrafta boş bırakılan yere getirilecek en uygun cümleyi seçer.'],
            'concepts': ['Paragrafı İkiye Bölme', 'Akışı Bozan Cümle', 'Cümle Yerleştirme', 'Anlam Bütünlüğü'],
            'skills': ['Metin Mimarisini Denetleme', 'Akış Analizi'], 'pedagogical': 'Cümleler puzzle parçaları gibi eşleştirilir.',
            'context': 'LGS Paragraf Bankosu', 'question': 'Bir paragraf hangi cümleden itibaren ikiye bölünmelidir?',
            'solution': 'Yazarın konunun farklı bir yönüne, yeni bir bakış açısına veya yeni bir konuya geçtiği cümleden itibaren bölünmelidir.', 'weeklyGoal': 'Paragrafta yapı ve akış sorularında sıfır hata yapma.',
            'evaluation': 'Paragrafta yapı soru föyü'
        },
        {
            'theme': 'Paragrafta Anlam', 'subTheme': 'Yeni Nesil Çoklu Paragraf Soruları',
            'code': 'TÜR.8.8.4', 'title': 'Aynı Metne Bağlı 2\'li ve 3\'lü Paragraf Sorularını Hızlı Çözme',
            'description': 'LGS formatındaki uzun metinlere bağlı çoklu soruları metni tek seferde dikkatle çizerek okuyup soruları art arda çözme stratejisini geliştirir.',
            'process': ['a) Zaman tasarrufu sağlar.', 'b) Metinler arası karşılaştırma sorularını çözümler.'],
            'concepts': ['Çoklu Paragraf', 'Metinler Arasılık', 'Zaman Tasarrufu'],
            'skills': ['Uzun Metin Konsantrasyonu', 'Hızlı Kavrama'], 'pedagogical': 'Uzun metinli LGS denemeleri kronometreyle çözdürülür.',
            'context': 'LGS Türkçe Ana Omurgası', 'question': 'Aynı metne bağlı 2 veya 3 soru olduğunda metni her soru için baştan sona tekrar tekrar okumak doğru mudur?',
            'solution': 'Hayır, büyük zaman kaybıdır. İlk okumada anahtar kelimelerin altı çizilmeli ve zihinsel harita çıkarılarak sorular çözülmelidir.', 'weeklyGoal': 'Çoklu paragraf sorularını yüksek hız ve doğrulukla tamamlama.',
            'evaluation': 'Çoklu paragraf çözüm föyü'
        },

        # 34-36: LGS Büyük Final Kampları
        {
            'theme': 'LGS Büyük Final', 'subTheme': 'LGS Türkçe Genel Tekrar ve Taktik Kampı',
            'code': 'TÜR.8.9.1', 'title': 'Fiilimsiden Paragrafa Tüm LGS Türkçe Soru Tipleri Sentezi',
            'description': 'Fiilimsiler, cümlenin ögeleri, cümle türleri, fiilde çatı, anlatım bozuklukları, yazım, noktalama, sözel mantık ve paragrafın püf noktaları özetlenir.',
            'process': ['a) Sınavda en çok yapılan 10 çeldirici hatayı gözden geçirir.', 'b) Hızlı soru eleme taktiklerini pekiştirir.'],
            'concepts': ['LGS Sentezi', 'Püf Noktalar', 'Soru Eleme'],
            'skills': ['Üst Düzey Sınav Hazırlığı', 'Zihinsel Hazırlık'], 'pedagogical': 'LGS Türkçe hap bilgiler el kitabı dağıtılır.',
            'context': 'LGS Şampiyonlar Kampı', 'question': 'LGS Türkçe testinde bir soruda iki şık arasında kalındığında ne yapılmalıdır?',
            'solution': 'Soru kökündeki anahtar kelimeye ve metnin ana fikrine tekrar dönülmeli; metinde açıkça yazmayan kişisel yorumlar elenmelidir.', 'weeklyGoal': 'Tüm LGS konularını bütünleştirip son taktikleri özümseme.',
            'evaluation': 'LGS Türkçe Hap Bilgiler Kontrol Listesi'
        },
        {
            'theme': 'LGS Büyük Final', 'subTheme': 'LGS Türkçe 20 Soruluk Tam Prova Denemesi',
            'code': 'TÜR.8.9.2', 'title': 'MEB Standartlarında 20 Soruluk Gerçekçi LGS Türkçe Denemesi ve Optik Kodlama',
            'description': 'Gerçek sınav kitapçığı formatında, tam süre tutularak (35-40 dakika) 20 soruluk Türkçe LGS denemesi yapılır ve anında analiz edilir.',
            'process': ['a) Optik forma işaretleme disiplinini uygular.', 'b) Sınav heyecanını yönetir.'],
            'concepts': ['LGS Prova', 'Optik Kodlama', 'Sınav Disiplini'],
            'skills': ['Sınav Kondisyonu', 'Stres Yönetimi'], 'pedagogical': 'Gerçek sınav salonu atmosferinde deneme uygulanır.',
            'context': 'LGS Genel Provası', 'question': 'LGS\'de Türkçe testine ne kadar süre ayrılması önerilir?',
            'solution': 'Sözel bölümün 75 dakikalık süresinin yaklaşık 35-40 dakikası Türkçe testine ayrılmalıdır.', 'weeklyGoal': 'LGS Türkçe sınav provasını başarıyla tamamlama.',
            'evaluation': 'LGS Türkçe Tam Deneme Karnesi'
        },
        {
            'theme': 'LGS Büyük Final', 'subTheme': 'LGS Başarı Belgesi ve Mezuniyet',
            'code': 'TÜR.8.9.3', 'title': '8. Sınıf Türkçe Programı Kapanışı ve Liseye Uğurlama',
            'description': 'Yıl boyu gösterilen LGS emeği, çözülen binlerce soru ve kitap okuma portfolyosu kutlanır; liseye başarı dilekleriyle uğurlama yapılır.',
            'process': ['a) Sınav günü stratejisini belirler.', 'b) LGS Başarı Sertifikasını alır.'],
            'concepts': ['LGS Başarısı', 'Liseye Geçiş', 'Gurur Tablosu'],
            'skills': ['Özgüven', 'Gelecek Vizyonu'], 'pedagogical': 'LGS motivasyon töreni ve mezuniyet kutlaması yapılır.',
            'context': 'LGS Mezuniyeti', 'question': 'LGS\'de Türkçe dersinde başarılı olan bir öğrencinin lisede elde edeceği en büyük avantaj nedir?',
            'solution': 'Okuduğunu hızlı anlama, derin muhakeme ve analiz yeteneği sayesinde lisedeki tüm derslerde ve üniversite sınavında üstün başarı göstermesidir.', 'weeklyGoal': 'LGS Türkçe serüvenini zirvede tamamlayıp hedeflenen liseyi kazanma.',
            'evaluation': 'LGS Türkçe Üstün Başarı Belgesi'
        }
    ]
    return {
        'title': '8. Sınıf',
        'subtitle': 'LGS Türkçe Programı (Sınav Odaklı)',
        'badge': 'LGS Türkçe',
        'weeks': weeks
    }

print("Turkce 8 builder compiled.")
