import '../models/curriculum_model.dart';

class Grade8Data {
  static final GradeCurriculum curriculum = GradeCurriculum(
    grade: 8,
    title: '8. Sınıf (LGS)',
    subtitle: 'Türkiye Yüzyılı Maarif Modeli & LGS (Süreç Odaklı)',
    badgeText: 'Türkiye Yüzyılı Maarif Modeli ✨',
    weeks: [
      // 1. HAFTA
      CurriculumWeek(
        weekNumber: 1,
        term: 1,
        dateRange: '08 - 12 Eylül',
        startDate: DateTime(2026, 9, 8),
        endDate: DateTime(2026, 9, 12),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Pozitif Tam Sayıların Çarpanları ve Asal Çarpanlar',
        weeklyGoal: 'Pozitif bir tam sayının pozitif çarpanlarını bulma ve asal çarpanlarına üslü olarak ayırma.',
        evaluationActivity: 'Asal çarpan ağacı ve algoritma hız testi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.1.1',
            title: 'Çarpanlar ve Asal Çarpanlar',
            description: 'Verilen pozitif tam sayıların pozitif tam sayı çarpanlarını bulur, asal çarpanlarını üslü biçimde yazar.',
            processComponents: [
              'a) Bir sayının pozitif çarpan sayısını ve asal çarpanlarını ayırt eder.',
              'b) Asal çarpan algoritmasını hatasız uygular.'
            ],
            keyConcepts: ['Pozitif Çarpan', 'Asal Çarpan', 'Üslü Çarpım'],
            skills: ['Sayısal Muhakeme', 'Analitik Düşünme'],
            pedagogicalNote: 'LGS yeni nesil sorularında alan-kenar ilişkisi üzerinden çarpan bulma soruları çözdürülür.',
            exampleProblem: ExampleProblem(
              context: 'Kare ve Dikdörtgen',
              question: 'Alanı 180 cm² olan dikdörtgenin kenar uzunlukları cm cinsinden birer tam sayıdır. Kaç farklı çevre uzunluğu oluşabilir?',
              solution: '180\'in pozitif bölen çifti sayısı: (2+1)(2+1)(1+1) = 18 bölen -> 9 farklı çift. 9 farklı çevre oluşabilir.',
            ),
          ),
        ],
      ),

      // 2. HAFTA
      CurriculumWeek(
        weekNumber: 2,
        term: 1,
        dateRange: '15 - 19 Eylül',
        startDate: DateTime(2026, 9, 15),
        endDate: DateTime(2026, 9, 19),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'En Büyük Ortak Bölen (EBOB) ve En Küçük Ortak Kat (EKOK)',
        weeklyGoal: 'İki sayının EBOB ve EKOK değerlerini asal çarpanlar algoritmasıyla hesaplama.',
        evaluationActivity: 'EBOB-EKOK matrisi doldurma',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.1.1',
            title: 'EBOB ve EKOK Hesaplama',
            description: 'İki doğal sayının en büyük ortak bölenini (EBOB) ve en küçük ortak katını (EKOK) hesaplar.',
            processComponents: [
              'a) İki sayıyı ortak bölen asal sayıların çarpımının EBOB olduğunu kavrar.',
              'b) EBOB(a,b) × EKOK(a,b) = a × b bağıntısını doğrular.'
            ],
            keyConcepts: ['EBOB', 'EKOK', 'Ortak Asal Bölen'],
            skills: ['Algoritmik Yetkinlik', 'Bağıntı Kurma'],
            pedagogicalNote: 'Asal çarpanların üslü gösteriminde tabanları ortak olanlardan üssü küçük olanların EBOB, büyük olanların EKOK oluşturduğu pratik kuralı verilir.',
            exampleProblem: ExampleProblem(
              context: 'EBOB - EKOK',
              question: 'A = 2³ × 3² × 5 ve B = 2² × 3³ × 7 olduğuna göre EBOB(A,B) kaçtır?',
              solution: 'Ortak asalların küçük üsleri: 2² × 3² = 4 × 9 = 36.',
            ),
          ),
        ],
      ),

      // 3. HAFTA
      CurriculumWeek(
        weekNumber: 3,
        term: 1,
        dateRange: '22 - 26 Eylül',
        startDate: DateTime(2026, 9, 22),
        endDate: DateTime(2026, 9, 26),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'EBOB ve EKOK Problemleri (LGS Yeni Nesil)',
        weeklyGoal: 'Problemlerde EBOB mu EKOK mu kullanılacağını ayırt etme ve çok adımlı problem çözme.',
        evaluationActivity: 'Problem sınıflandırma rubriği ve yeni nesil soru denemesi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.1.1',
            title: 'EBOB - EKOK Problemleri',
            description: 'EBOB ve EKOK ile ilgili problemleri çözer; gerçek yaşam bağlamlarına uygun stratejiler geliştirir.',
            processComponents: [
              'a) Parçalama, bölme, eşit aralıklarla ağaç dikme durumlarının EBOB olduğunu saptar.',
              'b) Birlikte zil çalma, nöbet, küçük parçalardan büyük kare oluşturma durumlarının EKOK olduğunu saptar.'
            ],
            keyConcepts: ['Ağaç Dikme', 'Koli Paylaştırma', 'Periyodik Karşılaşma'],
            skills: ['Problem Analizi', 'LGS Muhakeme Becerisi'],
            pedagogicalNote: 'Köşelere de dikilmek şartıyla bahçe etrafına ağaç dikme tuzakları üzerinde durulur.',
            exampleProblem: ExampleProblem(
              context: 'Bahçe Teli',
              question: 'Boyutları 48 m ve 60 m olan dikdörtgen bir tarlanın etrafına eşit aralıklarla ve köşelere de gelmek şartıyla fidan dikilecektir. En az kaç fidan gerekir?',
              solution: 'EBOB(48, 60) = 12 m (fidan aralığı). Çevre = 2 × (48 + 60) = 216 m. Fidan = 216 ÷ 12 = 18 fidan.',
            ),
          ),
        ],
      ),

      // 4. HAFTA
      CurriculumWeek(
        weekNumber: 4,
        term: 1,
        dateRange: '29 Eylül - 03 Ekim',
        startDate: DateTime(2026, 9, 29),
        endDate: DateTime(2026, 10, 3),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Aralarında Asal Sayılar',
        weeklyGoal: '1\'den başka ortak böleni olmayan sayıların aralarında asal olduğunu kavrama.',
        evaluationActivity: 'Aralarında asallık test kartları',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.1.1',
            title: 'Aralarında Asal Sayılar',
            description: 'Verilen iki doğal sayının aralarında asal olup olmadığını belirler.',
            processComponents: [
              'a) Sayıların kendileri asal olmasa bile aralarında asal olabileceğini (örn: 8 ve 9) açıklar.',
              'b) Ardışık doğal sayıların daima aralarında asal olduğunu kanıtlar.',
              'c) Aralarında asal iki sayının EBOB\'unun 1, EKOK\'unun ise çarpımları olduğunu doğrular.'
            ],
            keyConcepts: ['Aralarında Asal', 'EBOB=1', 'EKOK=Çarpım', 'Ardışık Sayılar'],
            skills: ['Kavramsal Ayrım', 'Muhakeme'],
            pedagogicalNote: 'Asal sayı kavramı ile aralarında asal olma kavramı arasındaki fark netleştirilir.',
            exampleProblem: ExampleProblem(
              context: 'Kesir Sadeleştirme',
              question: 'a ve b aralarında asal iki sayıdır. a/b = 24/36 olduğuna göre a + b toplamı kaçtır?',
              solution: 'En sade hale getirilir: 24/36 = 2/3. a=2 ve b=3 olur. Toplam = 2 + 3 = 5.',
            ),
          ),
        ],
      ),

      // 5. HAFTA
      CurriculumWeek(
        weekNumber: 5,
        term: 1,
        dateRange: '06 - 10 Ekim',
        startDate: DateTime(2026, 10, 6),
        endDate: DateTime(2026, 10, 10),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Üslü İfadeler: Tam Sayıların Tam Sayı Kuvvetleri (Negatif Üs)',
        weeklyGoal: 'Tam sayıların negatif kuvvetlerini (a⁻ⁿ = 1/aⁿ) ve üssün üssünü alma kurallarını öğrenme.',
        evaluationActivity: 'Negatif üs ters çevirme alıştırma yaprağı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.1.2',
            title: 'Tam Sayı Kuvvetleri ve Negatif Üs',
            description: 'Tam sayıların tam sayı kuvvetlerini hesaplar; negatif üssün çarpmaya göre tersi olduğunu anlar.',
            processComponents: [
              'a) Negatif üssün sayının işaretini değil, çarpmaya göre tersini aldığını kavrar (a⁻¹ = 1/a).',
              'b) Üssün üssü kuralında üslerin çarpıldığını [(aᵐ)ⁿ = aᵐ·ⁿ] modeller.'
            ],
            keyConcepts: ['Negatif Üs (a⁻ⁿ)', 'Üssün Üssü', 'Çarpmaya Göre Ters'],
            skills: ['Soyutlama', 'Kural Uygulama'],
            pedagogicalNote: 'En yaygın hata: 2⁻³ ifadesinin -8 zannedilmesidir. 1/2³ = 1/8 olduğu tahtada basamak basamak gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Mikro Ölçek',
              question: '5⁻³ sayısının değerini rasyonel ve ondalık olarak yazınız.',
              solution: '5⁻³ = 1 / 5³ = 1/125 = 8/1000 = 0,008.',
            ),
          ),
        ],
      ),

      // 6. HAFTA (BU HAFTA - 13 - 17 EKİM!)
      CurriculumWeek(
        weekNumber: 6,
        term: 1,
        dateRange: '13 - 17 Ekim',
        startDate: DateTime(2026, 10, 13),
        endDate: DateTime(2026, 10, 17),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Tam Kare Sayılar ve Karekök İlişkisi',
        weeklyGoal: 'Tam kare pozitif tam sayıların kareköklerini bulma ve alanı bilinen karenin bir kenarını hesaplama.',
        evaluationActivity: 'Kareli geometri kâğıdında alan-kenar karekök etkinliği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.1.3',
            title: 'Tam Kare Sayılar ve Karekök Kavramı',
            description: 'Tam kare pozitif tam sayılarla bu sayıların karekökleri arasındaki ilişkiyi belirler; alanı bilinen karesel bölgenin kenarını bulur.',
            processComponents: [
              'a) 1\'den 20\'ye kadar olan doğal sayıların karelerini ve kareköklerini zihinden bilir (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400).',
              'b) Karekök sembolünün (√) "Hangi sayının karesi bu sayıdır?" sorusuna yanıt aradığını kavrar.',
              'c) Karenin alanı verildiğinde bir kenar uzunluğunu kök içine alarak bulur.'
            ],
            keyConcepts: ['Tam Kare Sayı', 'Karekök (√)', 'Alan-Kenar İlişkisi', 'Pozitif Kök'],
            skills: ['Kavramsal Anlamlandırma', 'Geometrik Temsil', 'LGS Temel Muhakeme'],
            pedagogicalNote: 'Karekökün içinin negatif olamayacağı, çünkü hiçbir reel sayının karesinin negatif sayı yapamayacağı mantığı vurgulanır.',
            exampleProblem: ExampleProblem(
              context: 'Kare Bahçe',
              question: 'Alanı 256 m² olan kare şeklindeki bir bahçenin etrafına 3 sıra tel çekilecektir. Kaç metre tel gerekir?',
              solution: 'Bir kenar = √256 = 16 metre. Çevre = 4 × 16 = 64 metre. 3 sıra tel: 3 × 64 = 192 metre tel gerekir.',
            ),
          ),
        ],
      ),

      // 7. HAFTA
      CurriculumWeek(
        weekNumber: 7,
        term: 1,
        dateRange: '20 - 24 Ekim',
        startDate: DateTime(2026, 10, 20),
        endDate: DateTime(2026, 10, 24),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Tam Kare Olmayan Kareköklü Sayıların Değerini Tahmin Etme',
        weeklyGoal: 'Tam kare olmayan bir kareköklü sayının hangi iki ardışık doğal sayı arasında olduğunu ve hangisine daha yakın olduğunu bulma.',
        evaluationActivity: 'Sayı doğrusunda köklü sayı tahmin panosu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.1.3',
            title: 'Karekök Tahmini ve Sayı Doğrusu',
            description: 'Tam kare olmayan kareköklü bir sayının hangi iki ardışık doğal sayı arasında olduğunu belirler ve yakınlığını tahmin eder.',
            processComponents: [
              'a) Kök içindeki sayıya en yakın önceki ve sonraki tam kare sayıları belirler.',
              'b) Aradaki farka bakarak hangi tam sayıya daha yakın olduğunu muhakeme eder.'
            ],
            keyConcepts: ['Kök Tahmini', 'Sayı Doğrusu', 'Ardışık Tam Sayılar'],
            skills: ['Sayı Hissi', 'Yaklaşık Değer Hesaplama'],
            pedagogicalNote: 'Cetvel üzerinde tam kareler işaretlenerek tam kare olmayanların yerleşimi gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Cetvel Ölçümü',
              question: '√42 sayısı hangi iki ardışık tam sayı arasındadır ve hangisine daha yakındır?',
              solution: '√36 < √42 < √49 yani 6 ile 7 arasındadır. 42 sayısı 36\'ya 6 birim, 49\'a 7 birim uzaktadır; dolayısıyla 6\'ya daha yakındır (yaklaşık 6,48).',
            ),
          ),
        ],
      ),

      // 8. HAFTA
      CurriculumWeek(
        weekNumber: 8,
        term: 1,
        dateRange: '27 - 31 Ekim',
        startDate: DateTime(2026, 10, 27),
        endDate: DateTime(2026, 10, 31),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Kareköklü İfadeleri a√b Şeklinde Yazma ve Kök İçine Alma',
        weeklyGoal: 'Karekök içindeki sayıyı çarpanlarına ayırarak tam kare çarpanı kök dışına çıkarma ve katsayıyı kök içine karesini alarak sokma.',
        evaluationActivity: 'a√b dönüştürme eşleştirme kartları',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.1.3',
            title: 'a√b Gösterimi ve Kök İçine Alma',
            description: 'Kareköklü bir ifadeyi a√b şeklinde yazar ve a√b şeklindeki ifadede katsayıyı kök içine alır.',
            processComponents: [
              'a) Kök içindeki sayıyı a² · b biçiminde yazarak a\'yı dışarı katsayı olarak çıkarır.',
              'b) Katsayıyı kök içine alırken karesini alarak içeri sokar (a√b = √(a² · b)).'
            ],
            keyConcepts: ['a√b Biçimi', 'Kök Dışına Çıkarma', 'Kök İçine Alma'],
            skills: ['Cebirsel Manipülasyon', 'Dönüştürme'],
            pedagogicalNote: 'Sayıları sıralarken katsayıları kök içine almanın en kesin yol olduğu öğretilir.',
            exampleProblem: ExampleProblem(
              context: 'Dönüştürme',
              question: '√72 sayısını a√b şeklinde yazınız; 4√5 sayısını kök içine alınız.',
              solution: '√72 = √(36 × 2) = 6√2. 4√5 = √(4² × 5) = √(16 × 5) = √80.',
            ),
          ),
        ],
      ),

      // 9. HAFTA
      CurriculumWeek(
        weekNumber: 9,
        term: 1,
        dateRange: '03 - 07 Kasım',
        startDate: DateTime(2026, 11, 3),
        endDate: DateTime(2026, 11, 7),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Kareköklü İfadelerde Çarpma ve Bölme İşlemleri',
        weeklyGoal: 'Katsayıların kendi aralarında, kök içlerinin kendi aralarında çarpılıp bölünmesi kurallarını uygulama.',
        evaluationActivity: 'Köklü alan ve hacim bulmacaları',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.1.3',
            title: 'Köklü İfadelerde Çarpma ve Bölme',
            description: 'Kareköklü ifadelerde çarpma ve bölme işlemlerini yapar.',
            processComponents: [
              'a) a√b × c√d = (a·c)√(b·d) olduğunu modeller.',
              'b) Kök içindeki sayılar sadeleşebiliyorsa önce sadeleştirme kolaylığını kullanır.',
              'c) √a × √a = a özelliğini kavrar.'
            ],
            keyConcepts: ['Köklü Çarpma', 'Köklü Bölme', 'Kökten Kurtarma'],
            skills: ['Hesaplama Akıcılığı', 'LGS Geometri Entegrasyonu'],
            pedagogicalNote: '√a × √a işleminin doğrudan kök dışına "a" olarak çıkma kolaylığı çok iyi kavratılmalıdır.',
            exampleProblem: ExampleProblem(
              context: 'Dikdörtgen Alanı',
              question: 'Kenarları 3√6 cm ve 2√3 cm olan dikdörtgenin alanını hesaplayınız.',
              solution: 'Alan = (3 × 2) × √(6 × 3) = 6√18 = 6 × 3√2 = 18√2 cm².',
            ),
          ),
        ],
      ),

      // 10. HAFTA (ARA TATİL)
      CurriculumWeek(
        weekNumber: 10,
        term: 1,
        dateRange: '10 - 14 Kasım',
        startDate: DateTime(2026, 11, 10),
        endDate: DateTime(2026, 11, 14),
        theme: 'Ara Tatil & LGS Kampı',
        subTheme: '1. Dönem Ara Tatili / Atatürk Haftası',
        weeklyGoal: 'Çarpanlar-katlar, üslü ifadeler ve kareköklü ifadeler LGS yeni nesil denemesi.',
        evaluationActivity: 'LGS 1. Ünite Tarama Sınavı',
        isHoliday: true,
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.T1',
            title: 'LGS Ara Tatil Kampı',
            description: '1. Dönemin ilk üç ünitesine ait yeni nesil beceri temelli soruların analizi.',
            processComponents: ['a) LGS sınav stratejilerini, süre yönetimini ve soru kökü analizini pekiştirir.'],
            keyConcepts: ['LGS Yeni Nesil', 'Zaman Yönetimi', 'Strateji'],
            skills: ['Üst Düzey Muhakeme', 'Sınav Hazırlığı'],
            pedagogicalNote: 'Öğrencilere günlük 40-50 yeni nesil matematik sorusu çözme hedefi verilir.',
            exampleProblem: ExampleProblem(
              context: 'LGS Örnek Soru',
              question: 'Bir ayrıtı 2⁴ cm olan küp şeklindeki kutulardan kaç tanesi üst üste konursa yükseklik 2¹⁰ cm olur?',
              solution: '2¹⁰ ÷ 2⁴ = 2⁶ = 64 adet kutu.',
            ),
          ),
        ],
      ),

      // 11. HAFTA
      CurriculumWeek(
        weekNumber: 11,
        term: 1,
        dateRange: '17 - 21 Kasım',
        startDate: DateTime(2026, 11, 17),
        endDate: DateTime(2026, 11, 21),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Kareköklü İfadelerde Toplama ve Çıkarma İşlemleri',
        weeklyGoal: 'Sadece kök içleri aynı olan ifadelerin katsayılarının toplanıp çıkarılabileceğini uygulama.',
        evaluationActivity: 'Köklü çevre hesabı çalışma kâğıdı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.1.3',
            title: 'Köklü İfadelerde Toplama ve Çıkarma',
            description: 'Kareköklü ifadelerde toplama ve çıkarma işlemlerini yapar.',
            processComponents: [
              'a) Kök içleri aynı değilse önce a√b biçimine getirerek kök içlerini eşitler.',
              'b) a√x + b√x = (a + b)√x kuralını ortak çarpan parantezi mantığıyla açıklar.'
            ],
            keyConcepts: ['Ortak Kök', 'Katsayılar Toplamı', 'Benzer Köklü İfade'],
            skills: ['Cebirsel Benzeşim', 'Hesaplama'],
            pedagogicalNote: '√2 + √3 = √5 gibi sık yapılan büyük yanılgı alan modelleriyle engellenir.',
            exampleProblem: ExampleProblem(
              context: 'Çevre Hesabı',
              question: 'Kenarları √50 cm, √72 cm ve √98 cm olan üçgenin çevresini bulunuz.',
              solution: '√50 = 5√2, √72 = 6√2, √98 = 7√2. Çevre = 5√2 + 6√2 + 7√2 = 18√2 cm.',
            ),
          ),
        ],
      ),

      // 12. HAFTA
      CurriculumWeek(
        weekNumber: 12,
        term: 1,
        dateRange: '24 - 28 Kasım',
        startDate: DateTime(2026, 11, 24),
        endDate: DateTime(2026, 11, 28),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Köklü İfadeyi Doğal Sayı Yapan Çarpanlar ve Problemler',
        weeklyGoal: 'Kareköklü bir ifade ile çarpıldığında sonucu doğal sayı yapan eşlenik benzeri çarpanları bulma.',
        evaluationActivity: 'Köklü sayı eşleştirme dominosu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.1.3',
            title: 'Sonucu Doğal Sayı Yapan Çarpanlar',
            description: 'Kareköklü bir ifade ile çarpıldığında, sonucu bir doğal sayı yapan çarpanlara örnek verir.',
            processComponents: [
              'a) Kök içindeki irrasyonel kısmı aynı kökle çarparak doğal sayı elde eder (√12 = 2√3 -> √3 ile çarpılırsa 6 olur).'
            ],
            keyConcepts: ['Doğal Sayı Yapan Çarpan', 'Kökten Kurtulma'],
            skills: ['Analitik Düşünme', 'Problem Çözme'],
            pedagogicalNote: 'Paydayı rasyonel yapma temeli sezdirilir.',
            exampleProblem: ExampleProblem(
              context: 'Çarpma',
              question: '√45 sayısı aşağıdakilerden hangisi ile çarpılırsa sonuç bir doğal sayı olur: √2, √3, √5, √7?',
              solution: '√45 = 3√5 olduğundan √5 ile çarpılırsa 3 × 5 = 15 (doğal sayı) elde edilir.',
            ),
          ),
        ],
      ),

      // 13. HAFTA
      CurriculumWeek(
        weekNumber: 13,
        term: 1,
        dateRange: '01 - 05 Aralık',
        startDate: DateTime(2026, 12, 1),
        endDate: DateTime(2026, 12, 5),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Ondalık Gösterimlerin Karekökleri',
        weeklyGoal: 'Ondalık gösterimleri rasyonel sayıya çevirerek pay ve paydanın ayrı ayrı karekökünü alma.',
        evaluationActivity: 'Virgüllü kök hesaplama kartları',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.1.3',
            title: 'Ondalık İfadelerin Karekökü',
            description: 'Ondalık ifadelerin kareköklerini belirler.',
            processComponents: [
              'a) Ondalık sayıyı kesir çizgisiyle a/b şeklinde yazar.',
              'b) Pay ve paydanın karekökünü alıp tekrar ondalık olarak ifade eder.'
            ],
            keyConcepts: ['Ondalık Karekök', 'Rasyonel Çevrim'],
            skills: ['Hesaplama', 'Dönüştürme'],
            pedagogicalNote: '√0,4 sayısının 0,2 OLMADIĞI, çünkü (0,2)² = 0,04 olduğu basamak sayısıyla gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Hesaplama',
              question: '√(1,44) + √(0,81) - √(0,09) işleminin sonucunu bulunuz.',
              solution: '1,2 + 0,9 - 0,3 = 1,8.',
            ),
          ),
        ],
      ),

      // 14. HAFTA
      CurriculumWeek(
        weekNumber: 14,
        term: 1,
        dateRange: '08 - 12 Aralık',
        startDate: DateTime(2026, 12, 8),
        endDate: DateTime(2026, 12, 12),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Gerçek Sayılar (Rasyonel ve İrrasyonel Sayılar)',
        weeklyGoal: 'Reel sayı kümesini anlama; rasyonel (Q) ve irrasyonel (I) sayıların ayrımını yapma.',
        evaluationActivity: 'Sayı kümeleri Venn şeması sınıflandırması',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.1.4',
            title: 'Gerçek Sayılar Sistemi',
            description: 'Gerçek sayıları tanır, rasyonel ve irrasyonel sayılarla ilişkilendirir.',
            processComponents: [
              'a) a/b biçiminde yazılamayan (kök dışına çıkamayan sayılar, π gibi devirsiz sonsuz gidenler) sayıları irrasyonel olarak adlandırır.',
              'b) Rasyonel sayılar kümesi ile irrasyonel sayılar kümesinin birleşiminin gerçek sayılar (R) kümesini oluşturduğunu açıklar.'
            ],
            keyConcepts: ['Gerçek Sayı (R)', 'İrrasyonel Sayı (I)', 'Rasyonel Sayı (Q)', 'Pi Sayısı'],
            skills: ['Kavramsal Sınıflandırma', 'Matematiksel Felsefe'],
            pedagogicalNote: 'Pi sayısının devirli olmadığı için irrasyonel olduğu, 3,14 veya 22/7\'nin yaklaşık değer olduğu belirtilir.',
            exampleProblem: ExampleProblem(
              context: 'Sayı Sınıflandırma',
              question: '√16, √20, 0,7̄, π sayılarından hangileri irrasyoneldir?',
              solution: '√16 = 4 (Rasyonel), 0,7̄ = 7/9 (Rasyonel). √20 ve π irrasyonel sayılardır.',
            ),
          ),
        ],
      ),

      // 15. HAFTA
      CurriculumWeek(
        weekNumber: 15,
        term: 1,
        dateRange: '15 - 19 Aralık',
        startDate: DateTime(2026, 12, 15),
        endDate: DateTime(2026, 12, 19),
        theme: 'İstatistiksel Araştırma Süreci',
        subTheme: 'Veri Analizi: Çizgi, Sütun ve Daire Grafiği Dönüşümleri (LGS Klasiği)',
        weeklyGoal: 'Grafikler arası dönüşüm yapma ve daire grafiğinde merkez açılarla orantı kurma.',
        evaluationActivity: 'LGS Veri analizi yeni nesil soru atölyesi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.4.1',
            title: 'Veri Analizi ve Grafik Dönüşümleri',
            description: 'En çok üç veri grubuna ait grafikleri yorumlar ve bir grafiği diğer grafik türlerine dönüştürür.',
            processComponents: [
              'a) Sütun grafiğindeki miktarları 360°\'lik daire grafiğinde orantıyla merkez açılara aktarır.',
              'b) Yanıltıcı grafik temsillerini analiz eder.'
            ],
            keyConcepts: ['Daire Grafiği', 'Merkez Açı Orantısı', 'Grafik Dönüşümü'],
            skills: ['Veri Görselleştirme', 'Orantısal Muhakeme'],
            pedagogicalNote: 'Daire grafiği sorularında her zaman toplamın 360° olduğu orantı kurgulanır.',
            exampleProblem: ExampleProblem(
              context: 'Kütüphane Kitapları',
              question: 'Bir kütüphanedeki 720 kitabın 180\'i roman, 240\'ı hikâye, kalanı bilimdir. Bilim kitapları daire grafiğinde kaç derecelik açı gösterir?',
              solution: 'Bilim = 720 - 420 = 300 kitap. (300 / 720) × 360° = 150°.',
            ),
          ),
        ],
      ),

      // 16. HAFTA
      CurriculumWeek(
        weekNumber: 16,
        term: 1,
        dateRange: '22 - 26 Aralık',
        startDate: DateTime(2026, 12, 22),
        endDate: DateTime(2026, 12, 26),
        theme: 'Veriden Olasılığa',
        subTheme: 'Basit Olayların Olma Olasılığı: Olası Durumlar ve Eşit Şans',
        weeklyGoal: 'Bir olayın olası durumlarını listeleme ve eşit şansa sahip olayları analiz etme.',
        evaluationActivity: 'Zar ve torba deney simülasyonu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.5.1',
            title: 'Olası Durumlar ve Olasılık Kavramı',
            description: 'Bir olaya ait olası durumları belirler; "daha fazla", "daha az" veya "eşit" şansa sahip olayları ayırt eder.',
            processComponents: [
              'a) Örneklem uzayındaki tüm çıktıları listeler.',
              'b) Eleman sayısı eşit olan durumların eşit şansa sahip olduğunu doğrular.'
            ],
            keyConcepts: ['Olası Durumlar', 'Çıktı', 'Eşit Şans', 'Örneklem Uzay'],
            skills: ['Olasılıksal Düşünme', 'Sistematik Sayma'],
            pedagogicalNote: 'Kura çekimlerinde adaletin nasıl sağlandığı eşit olasılık ile açıklanır.',
            exampleProblem: ExampleProblem(
              context: 'Torba Oyunu',
              question: 'İçinde 5 mavi, 5 kırmızı bilye bulunan torbadan rastgele çekilen bir bilyenin mavi olma şansı ile kırmızı olma şansı nasıldır?',
              solution: 'Sayıları eşit olduğu için eşit şansa sahiptir.',
            ),
          ),
        ],
      ),

      // 17. HAFTA
      CurriculumWeek(
        weekNumber: 17,
        term: 1,
        dateRange: '29 Aralık - 02 Ocak',
        startDate: DateTime(2026, 12, 29),
        endDate: DateTime(2027, 1, 2),
        theme: 'Veriden Olasılığa',
        subTheme: 'Bir Olayın Olasılık Değeri (İstenen Durum / Tüm Durumlar)',
        weeklyGoal: 'Olasılık formülünü (İstenen Çıktı Sayısı / Tüm Çıktıların Sayısı) uygulama; 0 (imkânsız) ile 1 (kesin) arasını kavrama.',
        evaluationActivity: 'Olasılık cetveli oluşturma',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.5.1',
            title: 'Olasılık Değeri Hesaplama',
            description: 'Basit bir olayın olma olasılığını hesaplar; imkânsız (0) ve kesin (1) olayları açıklar.',
            processComponents: [
              'a) Olasılık değerinin daima 0 ≤ P(A) ≤ 1 aralığında olduğunu açıklar.',
              'b) Bir olayın olma olasılığı ile olmama olasılığı toplamının 1 olduğunu kavrar.'
            ],
            keyConcepts: ['İstenen Durum / Tüm Durumlar', 'Kesin Olay (1)', 'İmkânsız Olay (0)'],
            skills: ['Hesaplama', 'Karar Verme'],
            pedagogicalNote: 'Olasılık değerinin 1\'den büyük veya negatif çıkamayacağı kontrol kriteri olarak verilir.',
            exampleProblem: ExampleProblem(
              context: 'Zar Atma',
              question: 'Hilesiz bir zar atıldığında üst yüze asal sayı gelme olasılığı kaçtır?',
              solution: 'Tüm durumlar = {1, 2, 3, 4, 5, 6} (6 adet). Asallar = {2, 3, 5} (3 adet). Olasılık = 3/6 = 1/2.',
            ),
          ),
        ],
      ),

      // 18. HAFTA
      CurriculumWeek(
        weekNumber: 18,
        term: 1,
        dateRange: '05 - 09 Ocak',
        startDate: DateTime(2027, 1, 5),
        endDate: DateTime(2027, 1, 9),
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Cebirsel İfadeler: Terim, Katsayı ve Cebirsel Çarpma',
        weeklyGoal: 'Cebirsel ifadeleri çarpma ve cebir karolarıyla modelleme.',
        evaluationActivity: 'Cebir karoları ile alan kaplama etkinliği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.2.1',
            title: 'Cebirsel İfadelerin Çarpımı ve Modelleme',
            description: 'Basit cebirsel ifadeleri anlar ve farklı biçimlerde yazar; cebirsel ifadelerin çarpımını yapar.',
            processComponents: [
              'a) Terimleri, katsayıları ve sabit terimi belirler.',
              'b) İki terimli ile iki terimlinin çarpımını dağılma özelliğiyle uygular [(ax+b)(cx+d)].'
            ],
            keyConcepts: ['Cebirsel Çarpım', 'Dağılma Kuralı', 'Cebir Karosu Modeli'],
            skills: ['Geometrik Cebir', 'Modelleme'],
            pedagogicalNote: 'Her terimin diğeriyle teker teker çarpılması gerektiği yaylar çizilerek gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Alan Hesabı',
              question: '(2x + 3)(x - 4) çarpımının sonucunu yazınız.',
              solution: '2x² - 8x + 3x - 12 = 2x² - 5x - 12.',
            ),
          ),
        ],
      ),

      // 19. HAFTA
      CurriculumWeek(
        weekNumber: 19,
        term: 1,
        dateRange: '12 - 16 Ocak',
        startDate: DateTime(2027, 1, 12),
        endDate: DateTime(2027, 1, 16),
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Özdeşlikler: İki Terimin Toplamının ve Farkının Karesi, İki Kare Farkı',
        weeklyGoal: '(a+b)², (a-b)² ve a²-b² özdeşliklerini geometrik alanlarla kanıtlama.',
        evaluationActivity: 'Kâğıt kesme ile iki kare farkı ispatı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.2.1',
            title: 'Özdeşlikler ve Geometrik Modeller',
            description: 'Özdeşlik ile denklem arasındaki farkı açıklar; tam kare ve iki kare farkı özdeşliklerini modeller.',
            processComponents: [
              'a) (a + b)² = a² + 2ab + b² özdeşliğini karesel alan parçalarıyla gösterir.',
              'b) (a - b)² = a² - 2ab + b² özdeşliğini çıkarır.',
              'c) a² - b² = (a - b)(a + b) iki kare farkı modelini katlayarak gösterir.'
            ],
            keyConcepts: ['Özdeşlik', 'Tam Kare Özdeşliği', 'İki Kare Farkı', 'Geometrik İspat'],
            skills: ['Soyutlama', 'İspat', 'LGS Cebir Hakimiyeti'],
            pedagogicalNote: 'Özdeşliğin her x değeri için doğru olduğunu, denklemin ise sadece kök için doğru olduğunu ayırt ettirilir.',
            exampleProblem: ExampleProblem(
              context: 'Pratik Hesap',
              question: '101² - 99² işleminin sonucunu iki kare farkı kullanarak bulunuz.',
              solution: '(101 - 99)(101 + 99) = 2 × 200 = 400.',
            ),
          ),
        ],
      ),

      // 20. HAFTA (2. DÖNEM)
      CurriculumWeek(
        weekNumber: 20,
        term: 2,
        dateRange: '02 - 06 Şubat',
        startDate: DateTime(2027, 2, 2),
        endDate: DateTime(2027, 2, 6),
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Çarpanlara Ayırma: Ortak Çarpan Parantezi ve Özdeşlikler',
        weeklyGoal: 'Cebirsel ifadeleri ortak çarpan parantezine alarak ve özdeşliklerden yararlanarak çarpanlarına ayırma.',
        evaluationActivity: 'Çarpanlara ayırma eşleştirme kartları',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.2.2',
            title: 'Cebirsel İfadeleri Çarpanlara Ayırma',
            description: 'Cebirsel ifadeleri çarpanlarına ayırır.',
            processComponents: [
              'a) Her terimde ortak olan sayı veya harfi parantez dışına çıkarır.',
              'b) Üç terimli ifadelerde tam kare özdeşliğini tanır (x² + 6x + 9 = (x+3)²).',
              'c) İki terimli farklarda iki kare farkını uygular (x² - 25 = (x-5)(x+5)).'
            ],
            keyConcepts: ['Ortak Çarpan Parantezi', 'Çarpanlara Ayırma', 'Özdeşlikten Yararlanma'],
            skills: ['Tersine İşlem', 'Cebirsel Ustalık'],
            pedagogicalNote: 'Önce ortak çarpan var mı diye kontrol etme alışkanlığı kazandırılır.',
            exampleProblem: ExampleProblem(
              context: 'Sadeleştirme',
              question: '3x² - 12 cebirsel ifadesini çarpanlarına ayırınız.',
              solution: '3(x² - 4) = 3(x - 2)(x + 2).',
            ),
          ),
        ],
      ),

      // 21. HAFTA
      CurriculumWeek(
        weekNumber: 21,
        term: 2,
        dateRange: '09 - 13 Şubat',
        startDate: DateTime(2027, 2, 9),
        endDate: DateTime(2027, 2, 13),
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Birinci Dereceden Bir Bilinmeyenli Denklemler',
        weeklyGoal: 'Rasyonel katsayılı birinci dereceden bir bilinmeyenli denklemleri çözme.',
        evaluationActivity: 'Denklem merdiveni basamak testi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.2.3',
            title: 'Birinci Dereceden Denklemleri Çözme',
            description: 'Birinci dereceden bir bilinmeyenli denklemleri çözer.',
            processComponents: [
              'a) Paydaları eşitleyerek paydaları yok etme yöntemini uygular.',
              'b) İçler-dışlar çarpımı yaparak x\'i yalnız bırakır.'
            ],
            keyConcepts: ['Rasyonel Katsayılı Denklem', 'İçler-Dışlar', 'Payda Eşitleme'],
            skills: ['Algoritmik Yetkinlik', 'Doğrulama'],
            pedagogicalNote: 'Paydadaki ortak kat ile tüm denklemi genişletme hızı öğretilir.',
            exampleProblem: ExampleProblem(
              context: 'Denklem',
              question: '(x - 2)/3 + (x + 1)/2 = 4 denklemini çözünüz.',
              solution: 'Paydalar 6\'da eşitlenirse: 2(x - 2) + 3(x + 1) = 24 -> 2x - 4 + 3x + 3 = 24 -> 5x - 1 = 24 -> 5x = 25 -> x = 5.',
            ),
          ),
        ],
      ),

      // 22. HAFTA
      CurriculumWeek(
        weekNumber: 22,
        term: 2,
        dateRange: '16 - 20 Şubat',
        startDate: DateTime(2027, 2, 16),
        endDate: DateTime(2027, 2, 20),
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Koordinat Sistemi: Eksenler, Bölgeler ve Sıralı İkililer',
        weeklyGoal: 'Kartezyen koordinat sisteminde noktaları (x,y) gösterme ve bölgelerini belirleme.',
        evaluationActivity: 'Koordinat düzleminde hedef vurma oyunu (Battleship)',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.2.4',
            title: 'Koordinat Sistemi',
            description: 'Koordinat sistemini özellikleriyle tanır ve sıralı ikilileri gösterir.',
            processComponents: [
              'a) x eksenini (apsis), y eksenini (ordinat) ve kesişim noktasını (orijin) modeller.',
              'b) 4 bölgedeki işaret durumlarını (+/+, -/+, -/-, +/-) açıklar.'
            ],
            keyConcepts: ['Koordinat Sistemi', 'Apsis (x)', 'Ordinat (y)', 'Orijin (0,0)', 'Bölgeler'],
            skills: ['Uzamsal Konumlandırma', 'Grafik Okuma'],
            pedagogicalNote: 'Önce x (yatay), sonra y (dikey) sırası alfabetik sırayla akılda tutturulur.',
            exampleProblem: ExampleProblem(
              context: 'Nokta Konumu',
              question: 'A(-3, 4) noktası koordinat sisteminde kaçıncı bölgededir?',
              solution: 'x negatif, y pozitif olduğu için 2. bölgededir.',
            ),
          ),
        ],
      ),

      // 23. HAFTA
      CurriculumWeek(
        weekNumber: 23,
        term: 2,
        dateRange: '23 - 27 Şubat',
        startDate: DateTime(2027, 2, 23),
        endDate: DateTime(2027, 2, 27),
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Doğrusal İlişkiler, Tablo ve Grafik İlişkisi',
        weeklyGoal: 'Aralarında doğrusal ilişki bulunan iki değişken arasındaki bağıntıyı tablo ve grafikle gösterme.',
        evaluationActivity: 'Fidan boyu uzama doğrusal grafik analizi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.2.4',
            title: 'Doğrusal İlişkiler ve Değişkenler',
            description: 'Aralarında doğrusal ilişki bulunan iki değişken arasındaki ilişkiyi tablo ve grafikle ifade eder; bağımlı-bağımsız değişkeni belirler.',
            processComponents: [
              'a) Değişimi kontrol edilen değişkene bağımsız, ona bağlı değişene bağımlı değişken der.',
              'b) Doğrusal denklemi y = ax + b biçiminde yazar.'
            ],
            keyConcepts: ['Doğrusal İlişki', 'Bağımlı Değişken', 'Bağımsız Değişken'],
            skills: ['Fonksiyonel Düşünme', 'Modelleme'],
            pedagogicalNote: 'Taksi açılış ücreti ve km başına ücret örneği ile y = ax + b modeli somutlaştırılır.',
            exampleProblem: ExampleProblem(
              context: 'Taksi Ücreti',
              question: 'Açılış ücreti 20 TL olan ve her km için 15 TL alan taksinin x km sonraki y ücret denklemini yazınız.',
              solution: 'y = 15x + 20.',
            ),
          ),
        ],
      ),

      // 24. HAFTA
      CurriculumWeek(
        weekNumber: 24,
        term: 2,
        dateRange: '02 - 06 Mart',
        startDate: DateTime(2027, 3, 2),
        endDate: DateTime(2027, 3, 6),
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Doğrusal Denklemlerin Grafiğini Çizme',
        weeklyGoal: 'Orijinden geçen doğrular (y=mx) ile eksenleri kesen doğruların (ax+by+c=0) grafiğini çizme.',
        evaluationActivity: 'GeoGebra ile doğru grafikleri çizimi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.2.4',
            title: 'Doğrusal Denklem Grafikleri',
            description: 'Doğrusal denklemlerin grafiğini çizer.',
            processComponents: [
              'a) Eksenleri kestiği noktaları bulmak için x=0 verip y\'yi, y=0 verip x\'i bulur.',
              'b) x=a (dikey) ve y=b (yatay) doğrularını eksenlere paralel olarak çizer.'
            ],
            keyConcepts: ['Grafik Çizimi', 'Eksenleri Kesen Noktalar', 'Orijinden Geçen Doğru'],
            skills: ['Geometrik Cebir', 'Grafik Çizimi'],
            pedagogicalNote: 'İki noktanın bir doğruyu belirlemeye yettiği gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Grafik',
              question: '2x + 3y = 12 doğrusunun eksenleri kestiği noktaları bulunuz.',
              solution: 'x=0 için 3y=12 -> y=4 -> (0,4). y=0 için 2x=12 -> x=6 -> (6,0).',
            ),
          ),
        ],
      ),

      // 25. HAFTA
      CurriculumWeek(
        weekNumber: 25,
        term: 2,
        dateRange: '09 - 13 Mart',
        startDate: DateTime(2027, 3, 9),
        endDate: DateTime(2027, 3, 13),
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Doğrunun Eğimi (m = Dikey Uzunluk / Yatay Uzunluk)',
        weeklyGoal: 'Eğimi dik üçgende dikey/yatay oranla ve doğrudan y=mx+n formatında x\'in katsayısıyla bulma.',
        evaluationActivity: 'Rampa ve çatı eğimi hesaplama projesi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.2.4',
            title: 'Doğrunun Eğimi',
            description: 'Doğrunun eğimini modeller; rampa, çatı ve yol eğimlerini hesaplar.',
            processComponents: [
              'a) Eğim = Dikey Değişim / Yatay Değişim (m = Δy / Δx) olduğunu modeller.',
              'b) Sağa yatık doğruların eğiminin pozitif (+), sola yatıkların negatif (-) olduğunu kavrar.',
              'c) y yalnızken x\'in katsayısının eğim olduğunu fark eder.'
            ],
            keyConcepts: ['Eğim (m)', 'Dikey/Yatay', 'Pozitif Eğim', 'Negatif Eğim'],
            skills: ['Orantısal Akıl Yürütme', 'Fiziksel Yorumlama'],
            pedagogicalNote: 'Engelli rampası standartları (%8 eğim) üzerinden gerçek dünya duyarlılığı oluşturulur.',
            exampleProblem: ExampleProblem(
              context: 'Engelli Rampası',
              question: 'Yüksekliği 60 cm, yatay uzunluğu 1200 cm olan bir rampanın eğimi yüzde kaçtır?',
              solution: 'Eğim = 60 / 1200 = 1 / 20 = %5.',
            ),
          ),
        ],
      ),

      // 26. HAFTA
      CurriculumWeek(
        weekNumber: 26,
        term: 2,
        dateRange: '16 - 20 Mart',
        startDate: DateTime(2027, 3, 16),
        endDate: DateTime(2027, 3, 20),
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Birinci Dereceden Bir Bilinmeyenli Eşitsizlikler',
        weeklyGoal: 'Eşitsizlik durumlarını (<, >, ≤, ≥) sembollerle yazma ve sayı doğrusunda aralık olarak gösterme.',
        evaluationActivity: 'Hız sınırı ve asansör taşıma kapasitesi eşitsizlik panosu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.2.5',
            title: 'Eşitsizlik Kavramı ve Sayı Doğrusu',
            description: 'Birinci dereceden bir bilinmeyenli eşitsizlik içeren durumları belirler ve sayı doğrusunda gösterir.',
            processComponents: [
              'a) "En az", "en çok", "en fazla", "aşamaz" gibi sözel ifadeleri eşitsizlik sembolleriyle eşleştirir.',
              'b) Dahil olma durumunda sayı doğrusundaki noktanın içinin dolu, dahil değilse boş olduğunu çizer.'
            ],
            keyConcepts: ['Eşitsizlik (<, >, ≤, ≥)', 'Sayı Doğrusu Aralığı', 'Dahillik'],
            skills: ['Sembolik Temsil', 'Mantıksal Sınırlar'],
            pedagogicalNote: 'Trafikteki azami hız sınırı ile asgari hız sınırı örnekleri verilir.',
            exampleProblem: ExampleProblem(
              context: 'Bagaj Ağırlığı',
              question: '"Bir uçakta el bagajı en fazla 8 kg olabilir" ifadesini eşitsizlikle yazınız.',
              solution: 'x ≤ 8 kg (ve x ≥ 0).',
            ),
          ),
        ],
      ),

      // 27. HAFTA
      CurriculumWeek(
        weekNumber: 27,
        term: 2,
        dateRange: '23 - 27 Mart',
        startDate: DateTime(2027, 3, 23),
        endDate: DateTime(2027, 3, 27),
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Eşitsizlik Çözümleri ve Negatif Sayı ile Çarpma Kuralı',
        weeklyGoal: 'Eşitsizliğin her iki tarafı negatif sayıyla çarpılır veya bölünürse eşitsizliğin yön değiştirdiğini kavrama.',
        evaluationActivity: 'Eşitsizlik yön değiştirme kuralı kartları',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.2.5',
            title: 'Eşitsizlik Çözümleri',
            description: 'Birinci dereceden bir bilinmeyenli eşitsizlikleri çözer.',
            processComponents: [
              'a) Eşitsizlikleri denklem gibi çözerken negatif bir sayıyla çarpma/bölmede yönü ters çevirir (< ise > olur).',
              'b) Çözüm kümesini sayı doğrusunda aralık olarak gösterir.'
            ],
            keyConcepts: ['Yön Değiştirme', 'Eşitsizlik Çözüm Kümesi'],
            skills: ['Kritik Düşünme', 'Problem Çözme'],
            pedagogicalNote: '2 < 5 iken her iki taraf -1 ile çarpılırsa -2 > -5 olduğunu sayı doğrusunda gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Eşitsizlik Çözümü',
              question: '-3x + 7 ≤ 22 eşitsizliğinin çözüm kümesini bulunuz.',
              solution: '-3x ≤ 15 -> Her iki taraf -3\'e bölünürse yön değişir: x ≥ -5.',
            ),
          ),
        ],
      ),

      // 28. HAFTA (ARA TATİL)
      CurriculumWeek(
        weekNumber: 28,
        term: 2,
        dateRange: '30 Mart - 03 Nisan',
        startDate: DateTime(2027, 3, 30),
        endDate: DateTime(2027, 4, 3),
        theme: 'Ara Tatil & LGS Kampı 2',
        subTheme: '2. Dönem Ara Tatili / LGS Deneme Kampı',
        weeklyGoal: 'Denklemler, eğim, doğrusal ilişkiler ve eşitsizlikler ünitelerinin LGS denemeleriyle taranması.',
        evaluationActivity: 'LGS 2. Dönem Genel Deneme Sınavı',
        isHoliday: true,
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.T2',
            title: 'LGS Ara Tatil Kampı 2',
            description: 'Cebir ve doğrusal grafikler ağırlıklı yeni nesil soru çözümü ve analiz.',
            processComponents: ['a) LGS sınav süresi simülasyonu uygular.'],
            keyConcepts: ['LGS Simülasyonu', 'Hız', 'Analiz'],
            skills: ['Sınav Stratejisi'],
            pedagogicalNote: 'Her deneme sonrası yanlış yapılan soruların kazanım analizi çıkartılır.',
            exampleProblem: ExampleProblem(
              context: 'Deneme Sorusu',
              question: 'Eğimi %75 olan ve orijinden geçen doğrunun denklemini yazınız.',
              solution: '%75 = 3/4. Orijinden geçtiği için y = (3/4)x -> 4y = 3x.',
            ),
          ),
        ],
      ),

      // 29. HAFTA
      CurriculumWeek(
        weekNumber: 29,
        term: 2,
        dateRange: '06 - 10 Nisan',
        startDate: DateTime(2027, 4, 6),
        endDate: DateTime(2027, 4, 10),
        theme: 'Geometrik Şekiller',
        subTheme: 'Üçgende Kenarortay, Açıortay ve Yükseklik',
        weeklyGoal: 'Üçgenin yardımcı elemanlarını pergel, cetvel ve katlama yöntemleriyle çizme.',
        evaluationActivity: 'Kâğıt katlama ile üçgen yardımcı elemanları keşfi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.3.1',
            title: 'Üçgenin Yardımcı Elemanları',
            description: 'Üçgende kenarortay, açıortay ve yüksekliği inşa eder.',
            processComponents: [
              'a) Kenarortayların üçgenin içinde tek bir noktada (ağırlık merkezi) kesiştiğini kavrar.',
              'b) Geniş açılı üçgende iki yüksekliğin üçgenin dışında kesiştiğini modeller.'
            ],
            keyConcepts: ['Kenarortay (V)', 'Açıortay (n)', 'Yükseklik (h)', 'Ağırlık Merkezi'],
            skills: ['Geometrik İnşa', 'Uzamsal Muhakeme'],
            pedagogicalNote: 'İkizkenar ve eşkenar üçgende indirilen dikmenin aynı zamanda açıortay ve kenarortay olduğu altın kuralı verilir.',
            exampleProblem: ExampleProblem(
              context: 'İkizkenar Üçgen',
              question: 'Tepe açısı 40° olan ikizkenar üçgende tabana ait yükseklik tepe açısını kaçar derecelik iki açıya böler?',
              solution: 'İkizkenarda yükseklik aynı zamanda açıortaydır. 40 ÷ 2 = 20° ve 20°.',
            ),
          ),
        ],
      ),

      // 30. HAFTA
      CurriculumWeek(
        weekNumber: 30,
        term: 2,
        dateRange: '13 - 17 Nisan',
        startDate: DateTime(2027, 4, 13),
        endDate: DateTime(2027, 4, 17),
        theme: 'Geometrik Şekiller',
        subTheme: 'Üçgen Eşitsizliği (Üçgen Çizilebilme Şartı)',
        weeklyGoal: 'Bir üçgenin herhangi bir kenarının diğer iki kenarın farkından büyük, toplamından küçük olduğunu (|b-c| < a < b+c) kanıtlama.',
        evaluationActivity: 'Geometri çubuklarıyla üçgen oluşturabilme testi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.3.1',
            title: 'Üçgen Eşitsizliği',
            description: 'Üçgenin iki kenar uzunluğunun toplamı veya farkı ile üçüncü kenarının uzunluğu arasındaki ilişkiyi belirler.',
            processComponents: [
              'a) |b - c| < a < b + c eşitsizliğini uygular.',
              'b) Verilen üç çubuğun üçgen oluşturup oluşturamayacağını test eder.'
            ],
            keyConcepts: ['Üçgen Eşitsizliği', 'Kenar Uzunlukları', 'Mutlak Değer'],
            skills: ['Analitik Sorgulama', 'Geometrik Şart'],
            pedagogicalNote: 'İki kısa kenarın toplamı uzun kenara eşit olursa düz bir çizgi olacağı, üçgen oluşamayacağı gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Çubuk Oyunu',
              question: 'Kenarları 5 cm ve 9 cm olan bir üçgenin üçüncü kenarı x tam sayı olarak kaç farklı değer alabilir?',
              solution: '9 - 5 < x < 9 + 5 -> 4 < x < 14. x = 5,6,7,8,9,10,11,12,13 (9 farklı değer).',
            ),
          ),
        ],
      ),

      // 31. HAFTA
      CurriculumWeek(
        weekNumber: 31,
        term: 2,
        dateRange: '20 - 24 Nisan',
        startDate: DateTime(2027, 4, 20),
        endDate: DateTime(2027, 4, 24),
        theme: 'Geometrik Şekiller',
        subTheme: 'Üçgende Kenar Uzunlukları ile Açı Ölçüleri Arasındaki İlişki',
        weeklyGoal: 'Büyük açı karşısında büyük kenar, küçük açı karşısında küçük kenar bulunur kuralını uygulama.',
        evaluationActivity: 'Birden fazla üçgenin birleştiği şekillerde en uzun kenarı bulma labirenti',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.3.1',
            title: 'Açı - Kenar İlişkisi',
            description: 'Üçgenin kenar uzunlukları ile bu kenarların karşısındaki açıların ölçülerini ilişkilendirir.',
            processComponents: [
              'a) En büyük açının karşısında en uzun kenarın bulunduğunu kavrar.',
              'b) Dik üçgende hipotenüsün en uzun kenar olduğunu doğrular.'
            ],
            keyConcepts: ['Büyük Açı - Büyük Kenar', 'Hipotenüs', 'Ortak Kenar Karşılaştırması'],
            skills: ['Mantıksal Çıkarım', 'Geometrik Sıralama'],
            pedagogicalNote: 'İki üçgenin yapışık olduğu durumlarda bir üçgendeki en uzun kenarın diğerinde kısa kalabileceği yönlendirmesi yapılır.',
            exampleProblem: ExampleProblem(
              context: 'Köprü Tasarımı',
              question: 'Bir ABC üçgeninde m(A)=75° ve m(B)=65° olduğuna göre kenarları küçükten büyüğe sıralayınız.',
              solution: 'm(C) = 180 - 140 = 40°. Açılar: C < B < A olduğundan kenarlar: c < b < a.',
            ),
          ),
        ],
      ),

      // 32. HAFTA
      CurriculumWeek(
        weekNumber: 32,
        term: 2,
        dateRange: '27 Nisan - 01 Mayıs',
        startDate: DateTime(2027, 4, 27),
        endDate: DateTime(2027, 5, 1),
        theme: 'Geometrik Şekiller',
        subTheme: 'Pisagor Bağıntısı (a² + b² = c²) ve Özel Üçgenler',
        weeklyGoal: 'Dik üçgende hipotenüs bağıntısını modelleme; (3-4-5), (5-12-13), (8-15-17), (7-24-25) özel üçgenlerini kullanma.',
        evaluationActivity: 'Kare alanlarıyla Pisagor bağıntısı ispatı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.3.2',
            title: 'Pisagor Bağıntısı',
            description: 'Pisagor bağıntısını oluşturur; dik üçgende bilinmeyen kenar uzunluklarını ve günlük yaşam problemlerini çözer.',
            processComponents: [
              'a) Dik kenarların kareleri toplamının hipotenüsün karesine eşit olduğunu kanıtlar.',
              'b) Merdiven dayama, ağaç devrilme ve en kısa yol (kuş uçuşu) problemlerini Pisagor ile çözer.'
            ],
            keyConcepts: ['Pisagor Bağıntısı', 'Hipotenüs', 'Özel Dik Üçgenler (3-4-5 vb.)'],
            skills: ['Geometrik İspat', 'LGS Yeni Nesil Modelleme'],
            pedagogicalNote: 'Pisagor teoremindeki a²+b²=c² bağıntısı kenarlar üzerine kurulan karelerin alanları toplamıyla gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Merdiven Dayama',
              question: 'Duvardan 9 metre uzaklıktaki bir noktadan duvara dayanan 15 metrelik bir itfaiye merdiveni duvarda kaç metre yüksekliğe ulaşır?',
              solution: '9² + h² = 15² -> (3-4-5 üçgeninin 3 katı: 9-12-15) -> h = 12 metre.',
            ),
          ),
        ],
      ),

      // 33. HAFTA
      CurriculumWeek(
        weekNumber: 33,
        term: 2,
        dateRange: '04 - 08 Mayıs',
        startDate: DateTime(2027, 5, 4),
        endDate: DateTime(2027, 5, 8),
        theme: 'Geometrik Şekiller',
        subTheme: 'Eşlik ve Benzerlik: Benzerlik Oranı (k)',
        weeklyGoal: 'Benzer çokgenlerin karşılıklı açılarının eşit ve kenarlarının orantılı olduğunu keşfetme.',
        evaluationActivity: 'Gölge boyu ile ağaç yüksekliği hesaplama deneyi (Tales / Benzerlik)',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.3.3',
            title: 'Eşlik ve Benzerlik',
            description: 'Eş ve benzer çokgenlerin kenar ve açı ilişkilerini belirler; benzerlik oranını hesaplar.',
            processComponents: [
              'a) Benzerlik oranının k olduğu iki üçgende çevreler oranının k, alanlar oranının k² olduğunu kavrar.',
              'b) Eş çokgenlerde benzerlik oranının k=1 olduğunu belirtir.'
            ],
            keyConcepts: ['Benzerlik (∼)', 'Eşlik (≅)', 'Benzerlik Oranı (k)', 'Alanlar Oranı (k²)'],
            skills: ['Orantısal Geometri', 'Görsel Analiz'],
            pedagogicalNote: 'Fotoğraf büyütme/küçültme ve harita ölçeği üzerinden benzerlik pekiştirilir.',
            exampleProblem: ExampleProblem(
              context: 'Gölge Boyu',
              question: '1,8 m boyundaki bir insanın gölgesi 2,4 m iken yanındaki bayrak direğinin gölgesi 12 m olduğuna göre direğin boyu kaç metredir?',
              solution: '1,8 / h = 2,4 / 12 -> 2,4h = 21,6 -> h = 9 metre.',
            ),
          ),
        ],
      ),

      // 34. HAFTA
      CurriculumWeek(
        weekNumber: 34,
        term: 2,
        dateRange: '11 - 15 Mayıs',
        startDate: DateTime(2027, 5, 11),
        endDate: DateTime(2027, 5, 15),
        theme: 'Dönüşüm Geometrisi',
        subTheme: 'Öteleme ve Yansıma Dönüşümleri',
        weeklyGoal: 'Nokta ve şekillerin koordinat düzleminde öteleme ve eksenlere göre yansıma görüntülerini çizme.',
        evaluationActivity: 'Koordinat aynası ile simetri ve öteleme deseni çizimi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.3.4',
            title: 'Öteleme ve Yansıma',
            description: 'Nokta, doğru parçası ve diğer şekillerin öteleme ve yansıma sonucundaki görüntülerini belirler.',
            processComponents: [
              'a) x eksenine göre yansımada ordinatın işareti değişir [(x,y) -> (x,-y)].',
              'b) y eksenine göre yansımada apsisin işareti değişir [(x,y) -> (-x,y)].',
              'c) Sağa ötelemede x artar, yukarı ötelemede y artar.'
            ],
            keyConcepts: ['Öteleme', 'Yansıma (Simetri)', 'Ayna Görüntüsü', 'Koordinat Değişimi'],
            skills: ['Uzamsal Dönüşüm', 'Geometrik Estetik'],
            pedagogicalNote: 'Kilim desenleri ve ebru sanatındaki dönüşüm simetrileri gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Koordinat Simetrisi',
              question: 'A(4, -3) noktasının x eksenine göre yansıması alındıktan sonra 2 birim sola ötelenirse yeni koordinatları ne olur?',
              solution: 'x eksenine göre yansıma: (4, 3). 2 birim sola: (4 - 2, 3) = (2, 3).',
            ),
          ),
        ],
      ),

      // 35. HAFTA
      CurriculumWeek(
        weekNumber: 35,
        term: 2,
        dateRange: '18 - 22 Mayıs',
        startDate: DateTime(2027, 5, 18),
        endDate: DateTime(2027, 5, 22),
        theme: 'Geometrik Cisimler',
        subTheme: 'Prizmalar, Dik Dairesel Silindir, Koni ve Piramit',
        weeklyGoal: 'Dik prizmalar ve dik dairesel silindirin temel elemanlarını, açınımını ve yüzey alan/hacim bağıntılarını tanıma.',
        evaluationActivity: 'Kartonla silindir ve prizma maketleri oluşturma',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.3.5',
            title: 'Geometrik Cisimler ve Açınımları',
            description: 'Dik prizmaları ve dik dairesel silindiri tanır, açınımını çizer; yüzey alanı ve hacim bağıntılarını hesaplar.',
            processComponents: [
              'a) Silindirin yan yüzünün bir dikdörtgen olduğunu ve uzunluğunun taban dairesinin çevresine (2πr) eşit olduğunu modeller.',
              'b) Silindirin hacminin πr²h olduğunu açıklar.'
            ],
            keyConcepts: ['Dik Prizma', 'Silindir', 'Açınım', 'Yanal Alan', 'Silindir Hacmi'],
            skills: ['3 Boyutlu Düşünme', 'Maket İnşası'],
            pedagogicalNote: 'Konserve kutusu açınımı sınıfta somut olarak açılarak dikdörtgen yan yüz gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Konserve Kutusu',
              question: 'Taban yarıçapı 4 cm ve yüksekliği 10 cm olan silindir şeklindeki kutunun hacmi kaç cm³\'tür? (π=3)',
              solution: 'Hacim = π × r² × h = 3 × 4² × 10 = 3 × 16 × 10 = 480 cm³.',
            ),
          ),
        ],
      ),

      // 36. HAFTA
      CurriculumWeek(
        weekNumber: 36,
        term: 2,
        dateRange: '25 - 29 Mayıs',
        startDate: DateTime(2027, 5, 25),
        endDate: DateTime(2027, 5, 29),
        theme: 'LGS Son Prova',
        subTheme: 'LGS Son Düzlük Deneme ve Motivasyon Analizi',
        weeklyGoal: 'Tüm 8. sınıf LGS konularının tam kapsamlı prova denemesi, zaman yönetimi ve moral motivasyon semineri.',
        evaluationActivity: 'Bakanlık LGS Son Prova Deneme Sınavı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.8.LGS',
            title: 'LGS Genel Yetkinlik ve Sınav Provası',
            description: 'Ortaokul matematik müfredatının tamamını sentezleyerek LGS sınavına hazır hale gelir.',
            processComponents: [
              'a) Soru köklerini doğru okuma, turlama tekniğini uygulama ve optik kodlama disiplinini sergiler.',
              'b) 4 yıllık ortaokul matematik macerasını başarıyla taçlandırır.'
            ],
            keyConcepts: ['LGS Sınavı', 'Turlama Tekniği', 'Motivasyon', 'Hedef Lise'],
            skills: ['Öz Yeterlilik', 'Bilişsel Esneklik', 'Sınav Başarısı'],
            pedagogicalNote: 'Öğrencilere sınav kaygısını yönetme ve kendine güvenme mesajları verilir.',
            exampleProblem: ExampleProblem(
              context: 'LGS Başarı',
              question: 'Başarıya giden yolda disiplinli çalışma ve doğru stratejinin katkısı nedir?',
              solution: 'Yüksek odaklanma ve planlı çalışma ile hedeflenen lise kapıları ardına kadar açılır!',
            ),
          ),
        ],
      ),
    ],
  );
}
