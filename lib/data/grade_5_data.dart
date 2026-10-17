import '../models/curriculum_model.dart';

class Grade5Data {
  static final GradeCurriculum curriculum = GradeCurriculum(
    grade: 5,
    title: '5. Sınıf',
    subtitle: 'Doğal Sayılar, Kesirler & Temel Geometri',
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
        subTheme: 'Milyonlar: Doğal Sayıların Okunuşu ve Yazılışı',
        weeklyGoal: 'En çok dokuz basamaklı doğal sayıları okuma ve yazma.',
        evaluationActivity: 'Basamak tablosu kartları ve sayı okuma oyunu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.1',
            title: 'Milyonlar Bölüğü ve Doğal Sayılar',
            description: 'En çok dokuz basamaklı doğal sayıları okur, yazar ve basamak isimlerini belirtir.',
            processComponents: [
              'a) Birler, binler ve milyonlar bölüklerini tanır.',
              'b) Sayıların okunuşunda bölük isimlerinin sırasını söyler.'
            ],
            keyConcepts: ['Milyonlar Bölüğü', 'Basamak Değeri', 'Doğal Sayı'],
            skills: ['Matematiksel Temsil', 'İletişim'],
            pedagogicalNote: 'Türkiye nüfusu veya gök cisimlerinin uzaklıkları gibi büyük sayılar kullanılır.',
            exampleProblem: ExampleProblem(
              context: 'Nüfus Sayımı',
              question: '85 412 006 sayısının okunuşunu yazınız.',
              solution: 'Seksen beş milyon dört yüz on iki bin altı.',
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
        subTheme: 'Basamak Değerleri ve Sayı Örüntüleri',
        weeklyGoal: 'Basamak değerlerini çözümleme ve kuralı verilen sayı örüntülerini sürdürme.',
        evaluationActivity: 'Örüntü tamamlama çalışma kâğıdı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.1',
            title: 'Sayı Çözümleme ve Sayı Örüntüleri',
            description: 'Doğal sayıları basamak değerlerine göre çözümler; kuralı verilen örüntülerin eksik terimlerini bulur.',
            processComponents: [
              'a) Sayıdaki rakamın basamak değerini basamak çarpanıyla bulur.',
              'b) Adımlar arasındaki sabit artış veya azalışı belirler.'
            ],
            keyConcepts: ['Çözümleme', 'Sayı Örüntüsü', 'Artış Miktarı'],
            skills: ['Örüntü Tanıma', 'Genelleme'],
            pedagogicalNote: 'Rakamın sayı değeri ile basamak değeri arasındaki fark abaküsle gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Adım Sayısı',
              question: '7, 13, 19, 25, A, 37... örüntüsünde A kaçtır?',
              solution: 'Artış 6\'şar 6\'şar ilerlemektedir. A = 25 + 6 = 31.',
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
        subTheme: 'Doğal Sayılarla Toplama ve Çıkarma',
        weeklyGoal: 'En çok beş basamaklı doğal sayılarla eldeli toplama ve onluk bozarak çıkarma.',
        evaluationActivity: 'Eksik rakamları bulma bulmacası',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.2',
            title: 'Toplama ve Çıkarma İşlemleri',
            description: 'En çok beş basamaklı doğal sayılarla toplama ve çıkarma işlemlerini yapar.',
            processComponents: [
              'a) Aynı basamaktaki rakamları alt alta yazarak işlemi yürütür.',
              'b) Elde ve onluk bozma adımlarını doğru basamağa aktarır.'
            ],
            keyConcepts: ['Elde', 'Onluk Bozma', 'Toplam', 'Fark'],
            skills: ['Hesaplama Akıcılığı', 'Dikkat'],
            pedagogicalNote: 'İşlemlerde verilmeyen toplananı çıkarma yaparak bulma mantığı gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Kütüphane Kitap Sayısı',
              question: 'Bir kütüphanede 24 560 roman, 18 375 hikâye kitabı vardır. Toplam kaç kitap vardır?',
              solution: '24 560 + 18 375 = 42 935 kitap.',
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
        subTheme: 'Zihinden İşlemler ve Sonucu Tahmin Etme',
        weeklyGoal: 'Toplama ve çıkarma işlemlerini zihinden yapma ve yuvarlama ile tahmin etme.',
        evaluationActivity: 'Zihinden işlem hız kartları',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.3',
            title: 'Zihinden Toplama-Çıkarma ve Tahmin',
            description: 'Doğal sayılarla zihinden toplama ve çıkarma yapar; işlem sonuçlarını yuvarlayarak tahmin eder.',
            processComponents: [
              'a) Sayıları en yakın onluğa veya yüzlüğe yuvarlayarak tahmini sonuç bulur.',
              'b) Sayıları parçalama ve üzerine sayma stratejilerini uygular.'
            ],
            keyConcepts: ['Yuvarlama', 'Tahmin', 'Zihinden İşlem'],
            skills: ['Tahmin Becerisi', 'Esnek Düşünme'],
            pedagogicalNote: 'Alışverişte kasa kuyruğunda pratik toplam tahmin senaryosu canlandırılır.',
            exampleProblem: ExampleProblem(
              context: 'Market Alışverişi',
              question: '394 TL ve 512 TL olan iki ürünün yaklaşık toplam fiyatı en yakın yüzlüğe yuvarlanarak kaç TL bulunur?',
              solution: '394 -> 400, 512 -> 500. Yaklaşık 400 + 500 = 900 TL.',
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
        subTheme: 'Doğal Sayılarla Çarpma İşlemi',
        weeklyGoal: 'En çok üç basamaklı iki doğal sayının çarpımını basamak kaydırma kuralıyla yapma.',
        evaluationActivity: 'Çarpma işlem kâğıdı ve akran kontrolü',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.4',
            title: 'Doğal Sayılarla Çarpma İşlemi',
            description: 'En çok üç basamaklı iki doğal sayının çarpma işlemini yapar, basamak kaydırmanın nedenini açıklar.',
            processComponents: [
              'a) İkinci çarpanın onlar basamağıyla çarparken sonucun neden bir basamak sola yazıldığını irdeler.',
              'b) 10, 100 ve 1000 ile zihinden çarpmada sıfır ekleme kuralını uygular.'
            ],
            keyConcepts: ['Çarpan', 'Çarpım', 'Basamak Kaydırma', 'Kat'],
            skills: ['Algoritmik Düşünme', 'Akıl Yürütme'],
            pedagogicalNote: 'Basamak kaydırmanın aslında onlar basamağındaki sayının onlar katı ile çarpılmasından kaynaklandığı anlatılır.',
            exampleProblem: ExampleProblem(
              context: 'Koli Hesabı',
              question: 'Bir fabrikada her kolide 125 şişe su vardır. 48 koli hazırlandığında kaç şişe su paketlenmiş olur?',
              solution: '125 × 48 = 6000 şişe su.',
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
        subTheme: 'Doğal Sayılarla Bölme İşlemi ve Kalanı Yorumlama',
        weeklyGoal: 'Bölme algoritmasını eksiksiz yürütme ve kalanlı bölmede kalanı duruma göre yorumlayabilme.',
        evaluationActivity: 'Kalanı yorumlama problem atölyesi ve grup çalışması',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.4',
            title: 'Doğal Sayılarla Bölme ve Kalanı Yorumlama',
            description: 'En çok dört basamaklı bir doğal sayıyı, en çok iki basamaklı bir sayıya böler ve kalanı gerçek yaşam durumuna göre yorumlar.',
            processComponents: [
              'a) Bölünen, bölen, bölüm ve kalan arasındaki (Bölünen = Bölen × Bölüm + Kalan) ilişkisini doğrular.',
              'b) Kalanın bölenden daima küçük olması gerektiğini kontrol eder.',
              'c) Gerçek yaşam bağlamında kalanın bir sonraki tam sayıya yuvarlanması veya kesir olarak ifade edilmesi gerekip gerekmediğini tartışır.'
            ],
            keyConcepts: ['Bölünen', 'Bölen', 'Bölüm', 'Kalan', 'Kalanı Yorumlama'],
            skills: ['Mantıksal Çıkarım', 'Problem Çözme', 'Muhakeme'],
            pedagogicalNote: 'Otobüs kapasitesi örneği: 125 kişi 30 kişilik otobüslere binecekse 4 otobüs yetmez, kalan 5 kişi için 5. otobüs gerekir mantığı tartışılır.',
            exampleProblem: ExampleProblem(
              context: 'Gezi Otobüsü',
              question: 'Bir okul gezisine 145 öğrenci katılacaktır. Her minibüs 18 öğrenci alabildiğine göre en az kaç minibüs kiralanmalıdır?',
              solution: '145 ÷ 18 = 8 minibüs (kalan 1 öğrenci). Kalan öğrenci dışarıda kalamayacağı için en az 8 + 1 = 9 minibüs gereklidir.',
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
        subTheme: 'Çarpma ve Bölme Tahmini, Zihinden İşlemler',
        weeklyGoal: 'Çarpma ve bölme işlemlerinin sonucunu yuvarlama ve basamak değerleriyle tahmin etme.',
        evaluationActivity: 'Hızlı tahmin yarışması',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.5',
            title: 'Çarpma ve Bölme Sonucunu Tahmin Etme',
            description: 'Doğal sayılarla çarpma ve bölme işlemlerinin sonucunu tahmin eder, stratejilerini açıklar.',
            processComponents: [
              'a) Çarpanları uygun onluk veya yüzlüklere yuvarlayarak tahminde bulunur.',
              'b) Bölme işleminde bölen ile bölünenin ilk basamakları arasındaki ilişkiyi inceler.'
            ],
            keyConcepts: ['İşlem Tahmini', 'Yuvarlama', 'Zihinden Bölme'],
            skills: ['Sayı Hissi', 'Tahmin'],
            pedagogicalNote: 'Gerçek sonuç ile tahmin edilen sonucun farkı hesaplanarak sapma miktarı değerlendirilir.',
            exampleProblem: ExampleProblem(
              context: 'Bilet Geliri',
              question: 'Konsere 487 kişi gelmiş ve her bilet 98 TL satılmıştır. Yaklaşık hasılat nedir?',
              solution: '487 -> 500, 98 -> 100. Yaklaşık 500 × 100 = 50.000 TL.',
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
        subTheme: 'Doğal Sayılarla Dört İşlem Problemleri',
        weeklyGoal: 'Dört işlem yapmayı gerektiren çok adımlı günlük yaşam problemlerini çözme.',
        evaluationActivity: 'Problem kurma etkinliği ve çözüm rubriği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.6',
            title: 'Dört İşlem Problemleri Çözme ve Kurma',
            description: 'Doğal sayılarla dört işlem yapmayı gerektiren problemleri çözer ve problem kurar.',
            processComponents: [
              'a) Problemin aşamalarını belirler.',
              'b) Toplama, çıkarma, çarpma ve bölme işlemlerini uygun sırayla uygular.'
            ],
            keyConcepts: ['Çok Adımlı Problem', 'Plan Yapma', 'Kontrol'],
            skills: ['Problem Çözme', 'Eleştirel Düşünme'],
            pedagogicalNote: 'Öğrencilere sadece hazır soru çözdürülmemeli, verilen işlem adımlarına uygun hikâye yazdırılmalıdır.',
            exampleProblem: ExampleProblem(
              context: 'Manav Hesabı',
              question: 'Kilogramı 15 TL olan elmadan 4 kg, kilogramı 25 TL olan muzdan 3 kg alan kişi 200 TL verirse kaç TL para üstü alır?',
              solution: 'Elma = 60 TL, Muz = 75 TL. Toplam = 135 TL. Para üstü: 200 - 135 = 65 TL.',
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
        subTheme: 'Bir Doğal Sayının Karesi ve Küpü',
        weeklyGoal: 'Bir doğal sayının karesini (a²) ve küpünü (a³) üslü nicelik olarak anlama.',
        evaluationActivity: 'Birim küpler ve kare modellerle alan/hacim gösterimi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.7',
            title: 'Doğal Sayıların Karesi ve Küpü',
            description: 'Doğal sayıların karesini ve küpünü üslü olarak ifade eder, değerlerini hesaplar.',
            processComponents: [
              'a) Bir sayının karesinin karesel bölgenin alanıyla ilişkisini fark eder.',
              'b) Bir sayının küpünün küpün hacmiyle (birim küp sayısı) ilişkisini modeller.'
            ],
            keyConcepts: ['Kare (²)', 'Küp (³)', 'Taban', 'Üs'],
            skills: ['Görsel Temsil', 'Uzamsal Düşünme'],
            pedagogicalNote: '5² ile 5×2 arasındaki kavram yanılgısı kare karolar kullanılarak düzeltilir.',
            exampleProblem: ExampleProblem(
              context: 'Karesel Bahçe',
              question: 'Kenar uzunluğu 7 m olan kare şeklindeki odanın alanı kaç m² olur?',
              solution: '7² = 7 × 7 = 49 m².',
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
        theme: 'Ara Tatil & Pekiştirme',
        subTheme: '1. Dönem Ara Tatili',
        weeklyGoal: 'İlk 9 haftalık doğal sayılar ve dört işlem kazanımlarının pekiştirilmesi.',
        evaluationActivity: 'Eğlenceli matematik bulmaca fasikülü',
        isHoliday: true,
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.T1',
            title: 'Ara Tatil Beceri Pekiştirmesi',
            description: 'Doğal sayılarla işlemler ve problem çözme becerilerinin tekrarı.',
            processComponents: ['a) Dört işlem hızını koruyucu eğlenceli aktiviteler yapar.'],
            keyConcepts: ['Tekrar', 'Zihinden İşlem', 'Hız'],
            skills: ['Öz Değerlendirme'],
            pedagogicalNote: 'Matematik oyunları tavsiye edilir.',
            exampleProblem: ExampleProblem(
              context: 'Bulmaca',
              question: 'Hangi sayının küpü 64\'tür?',
              solution: '4³ = 4 × 4 × 4 = 64.',
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
        subTheme: 'Parantezli İşlemler ve İşlem Önceliği',
        weeklyGoal: 'Parantez içeren işlemlerde parantez içine öncelik verilmesi kuralını uygulama.',
        evaluationActivity: 'İşlem önceliği eşleştirme kartları',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.8',
            title: 'Parantezli İşlemler',
            description: 'Parantez içeren işlemlerde parantezin önceliğini belirleyerek sonucu bulur.',
            processComponents: [
              'a) Parantezin işlemin yönünü değiştirdiğini örneklerle açıklar.',
              'b) (12 + 8) × 3 ile 12 + (8 × 3) arasındaki farkı hesaplar.'
            ],
            keyConcepts: ['Parantez', 'İşlem Sırası', 'Öncelik'],
            skills: ['Mantıksal Sıralama', 'Hesaplama'],
            pedagogicalNote: 'Trafik kuralları benzetmesi yapılarak parantezin geçiş üstünlüğü anlatılır.',
            exampleProblem: ExampleProblem(
              context: 'Hesaplama',
              question: '25 - (3 × 4) + 6 işleminin sonucunu bulunuz.',
              solution: 'Parantez içi: 3 × 4 = 12. 25 - 12 + 6 = 13 + 6 = 19.',
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
        subTheme: 'Kesirler: Birim Kesirler ve Sayı Doğrusu',
        weeklyGoal: 'Birim kesir kavramını modelleme ve sayı doğrusunda 0 ile 1 arasında gösterme.',
        evaluationActivity: 'Kesir şeritleri ile birim kesir oluşturma',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.9',
            title: 'Birim Kesirler ve Sayı Doğrusu',
            description: 'Birim kesirleri modeller, sıralar ve sayı doğrusunda gösterir.',
            processComponents: [
              'a) Payı 1 olan kesirleri birim kesir olarak tanımlar.',
              'b) Paydası büyük olan birim kesrin daha küçük olduğunu somut olarak gösterir.'
            ],
            keyConcepts: ['Birim Kesir', 'Pay', 'Payda', 'Sayı Doğrusu'],
            skills: ['Temsil', 'Karşılaştırma'],
            pedagogicalNote: 'Bir pastayı 4 kişiye bölmekle 8 kişiye bölmek arasındaki dilim büyüklüğü farkı vurgulanır.',
            exampleProblem: ExampleProblem(
              context: 'Pasta Paylaşımı',
              question: '1/3, 1/7 ve 1/5 birim kesirlerini küçükten büyüğe sıralayınız.',
              solution: 'Payda büyüdükçe birim kesir küçülür: 1/7 < 1/5 < 1/3.',
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
        subTheme: 'Tam Sayılı ve Bileşik Kesir Dönüşümleri',
        weeklyGoal: 'Tam sayılı kesri bileşik kesre, bileşik kesri tam sayılı kesre dönüştürme.',
        evaluationActivity: 'Dönüşüm çarkı oyunu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.10',
            title: 'Tam Sayılı ve Bileşik Kesir Dönüşümleri',
            description: 'Tam sayılı kesri bileşik kesre ve bileşik kesri tam sayılı kesre dönüştürür.',
            processComponents: [
              'a) Bileşik kesri tam sayılı kesre çevirirken payı paydaya bölme algoritmasını uygular.',
              'b) Bölümün tam kısım, kalanın pay, bölenin payda olduğunu kavrar.'
            ],
            keyConcepts: ['Tam Sayılı Kesir', 'Bileşik Kesir', 'Bölme'],
            skills: ['Dönüştürme', 'Modelleme'],
            pedagogicalNote: 'Pizzalar bütün olarak ve dilimler olarak görselleştirilir.',
            exampleProblem: ExampleProblem(
              context: 'Pizza Siparişi',
              question: '17/5 kesrini tam sayılı kesir olarak ifade ediniz.',
              solution: '17 ÷ 5 = 3 (kalan 2). Yani 3 tam 2/5.',
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
        subTheme: 'Denk Kesirler, Genişletme ve Sadeleştirme',
        weeklyGoal: 'Bir kesri genişleterek veya sadeleştirerek denk kesirler elde etme.',
        evaluationActivity: 'Denk kesir hafıza kartları',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.11',
            title: 'Denk Kesirler ve Sadeleştirme',
            description: 'Sadeleştirme ve genişletmenin kesrin değerini değiştirmediğini anlar ve denk kesirler oluşturur.',
            processComponents: [
              'a) Pay ve paydayı aynı sayıyla çarparak genişletir.',
              'b) Pay ve paydayı ortak bölene bölerek sadeleştirir.'
            ],
            keyConcepts: ['Denk Kesir', 'Genişletme', 'Sadeleştirme', 'En Sade Hal'],
            skills: ['Eşdeğerlik', 'Orantısal Akıl Yürütme'],
            pedagogicalNote: 'Kesir şeritlerinde üst üste koyulduğunda aynı uzunluğu kaplayan şeritler gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Boyama Alanı',
              question: '2/5 kesrinin paydası 20 olacak şekilde genişletilmiş halini bulunuz.',
              solution: '4 ile genişletilirse: (2 × 4) / (5 × 4) = 8/20.',
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
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Kesirleri Karşılaştırma ve Sıralama',
        weeklyGoal: 'Payları veya paydaları eşit olan ya da eşitlenebilen kesirleri sıralama.',
        evaluationActivity: 'Sayı doğrusunda kesir sıralama simülasyonu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.12',
            title: 'Kesirleri Karşılaştırma ve Sıralama',
            description: 'Payları veya paydaları eşit olan kesirleri sıralar; paydaları eşit olmayanları genişleterek sıralar.',
            processComponents: [
              'a) Paydaları eşitse payı büyük olanın büyük olduğunu belirtir.',
              'b) Payları eşitse paydası küçük olanın büyük olduğunu modeller.'
            ],
            keyConcepts: ['Kesir Sıralama', 'Payda Eşitleme', 'Yarıma Yakınlık'],
            skills: ['Karşılaştırma', 'Muhakeme'],
            pedagogicalNote: 'Yarımdan küçük, yarıma eşit ve yarımdan büyük sınıflandırma stratejisi kazandırılır.',
            exampleProblem: ExampleProblem(
              context: 'Yarış Parkuru',
              question: '3/4, 5/8 ve 1/2 kesirlerini küçükten büyüğe sıralayınız.',
              solution: 'Paydalar 8\'de eşitlenirse: 6/8, 5/8, 4/8. Sıralama: 1/2 < 5/8 < 3/4.',
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
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Bir Çokluğun Kesir Kadarını Bulma',
        weeklyGoal: 'Bir çokluğun belirtilen basit kesir kadarını ve kesir kadarı verilen çokluğun tamamını bulma.',
        evaluationActivity: 'Birim model çizimi ile hesaplama',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.13',
            title: 'Bir Çokluğun Kesir Değerini Hesaplama',
            description: 'Bir çokluğun belirtilen basit kesir kadarını hesaplar.',
            processComponents: [
              'a) Çokluğu paydaya bölüp pay ile çarparak birim parçayı bulur.',
              'b) Kutu çizerek modeli görselleştirir.'
            ],
            keyConcepts: ['Birim Parça', 'Bütün', 'Kesir Değeri'],
            skills: ['Modelleme', 'Hesaplama'],
            pedagogicalNote: 'Kuralı ezberletmek yerine önce 1 kutunun değerini buldurma alışkanlığı edindirilir.',
            exampleProblem: ExampleProblem(
              context: 'Harçlık Hesabı',
              question: '120 TL\'si olan Burak harçlığının 3/5\'ini harcamıştır. Kaç TL harcamıştır?',
              solution: '120 ÷ 5 = 24 TL (1 parça). 24 × 3 = 72 TL harcamıştır.',
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
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Kesirlerle Toplama ve Çıkarma İşlemleri',
        weeklyGoal: 'Paydaları eşit veya birinin paydası diğerinin katı olan kesirlerle toplama ve çıkarma.',
        evaluationActivity: 'Kesir karoları ile toplama-çıkarma atölyesi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.14',
            title: 'Kesirlerle Toplama ve Çıkarma',
            description: 'Paydaları eşit veya birinin paydası diğerinin katı olan iki kesrin toplama ve çıkarma işlemini yapar.',
            processComponents: [
              'a) Gerektiğinde genişletme yaparak paydaları eşitler.',
              'b) Ortak paydayı aynen korur, payları toplar veya çıkarır.'
            ],
            keyConcepts: ['Ortak Payda', 'Pay Toplamı', 'Kesir Çıkarma'],
            skills: ['Hesaplama', 'Algoritmik Düşünme'],
            pedagogicalNote: 'Öğrencilerin paydaları da birbiriyle toplama yanılgısı üzerinde durulur.',
            exampleProblem: ExampleProblem(
              context: 'Meyve Suyu',
              question: 'Bir sürahideki portakal suyunun 2/3\'ü ile 1/6\'sı içilmiştir. Toplam ne kadarı içilmiştir?',
              solution: '2/3 kesri 2 ile genişletilirse 4/6 olur. 4/6 + 1/6 = 5/6.',
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
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Kesir Problemleri',
        weeklyGoal: 'Kesirlerle toplama ve çıkarma gerektiren günlük hayat problemlerini çözme.',
        evaluationActivity: 'Senaryo tabanlı problem çözümü',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.15',
            title: 'Kesir Problemleri Çözme',
            description: 'Kesirlerle işlem yapmayı gerektiren problemleri çözer.',
            processComponents: [
              'a) Parça-bütün ilişkisini şematize eder.',
              'b) Bütünü 1 tam kabul ederek kalanı hesaplar.'
            ],
            keyConcepts: ['Bütün (1 Tam)', 'Kalan Parça', 'Kesir Problemi'],
            skills: ['Problem Çözme', 'Muhakeme'],
            pedagogicalNote: 'Şerit modellerle kalanın adım adım gösterilmesi sağlanır.',
            exampleProblem: ExampleProblem(
              context: 'Kitap Okuma',
              question: 'Bir kitabın 1. gün 2/7\'sini, 2. gün 3/7\'sini okuyan Elif\'in geriye kitabın kaçta kaçı kalmıştır?',
              solution: 'Okunan = 2/7 + 3/7 = 5/7. Kalan = 7/7 - 5/7 = 2/7.',
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
        theme: 'Değerlendirme',
        subTheme: '1. Dönem Sonu Genel Tekrarı',
        weeklyGoal: '1. Dönem boyunca işlenen doğal sayılar ve kesirler ünitelerinin sentezlenmesi.',
        evaluationActivity: '1. Dönem Karne Öncesi Beceri Şenliği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.D1',
            title: '1. Dönem Genel Değerlendirmesi',
            description: '1. Dönem matematik öğrenme çıktılarının kavram haritasıyla özetlenmesi.',
            processComponents: ['a) Sayı ve işlem becerilerini problem senaryolarında sergiler.'],
            keyConcepts: ['Genel Tekrar', 'Kavram Haritası'],
            skills: ['Sentez', 'Öz Düzenleme'],
            pedagogicalNote: 'Eksik öğrenmeler için telafi adımları belirlenir.',
            exampleProblem: ExampleProblem(
              context: 'Dönem Sonu',
              question: '3 tam 1/4 kesri kaç tane çeyrekten oluşur?',
              solution: '3 tam = 12 çeyrek. 1 çeyrek daha eklenirse 13 çeyrek olur.',
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
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Ondalık Gösterim: Ondalık Kesirleri Tanıma',
        weeklyGoal: 'Paydası 10, 100 veya 1000 olan kesirleri virgül kullanarak ondalık gösterme.',
        evaluationActivity: 'Virgüllü sayı kartları eşleştirme',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.16',
            title: 'Ondalık Gösterim Kavramı',
            description: 'Paydası 10, 100 veya 1000 olan bir kesri ondalık gösterimle yazar ve okur.',
            processComponents: [
              'a) Virgülün tam kısım ile kesir kısmını ayırdığını kavrar.',
              'b) 7/10 = 0,7 ve 3 tam 25/100 = 3,25 dönüşümlerini modeller.'
            ],
            keyConcepts: ['Ondalık Gösterim', 'Virgül', 'Tam Kısım', 'Kesir Kısmı'],
            skills: ['Temsil', 'Dönüştürme'],
            pedagogicalNote: 'Para birimleri (Lira ve Kuruş) üzerinden virgülün işlevi somutlaştırılır.',
            exampleProblem: ExampleProblem(
              context: 'Fiyat Etiketi',
              question: '2 tam 8/100 kesrinin ondalık gösterimini yazınız.',
              solution: '2,08 (yüzde sekiz olarak okunur).',
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
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Ondalık Gösterimde Basamak Adları ve Değerleri',
        weeklyGoal: 'Onda birler, yüzde birler ve binde birler basamaklarını belirleme.',
        evaluationActivity: 'Ondalık basamak tablosu doldurma',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.16',
            title: 'Ondalık Basamak Değerleri',
            description: 'Ondalık gösterimdeki basamak isimlerini ve basamak değerlerini belirler.',
            processComponents: [
              'a) Virgülden sonraki basamakları sağa doğru onda birler, yüzde birler, binde birler olarak adlandırır.'
            ],
            keyConcepts: ['Onda Birler', 'Yüzde Birler', 'Binde Birler'],
            skills: ['Basamak Değeri', 'Analiz'],
            pedagogicalNote: 'Virgülden sonra eklenen sıfırların sayının değerini değiştirmediği gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Hassas Tartı',
              question: '14,375 ondalık gösteriminde 7 rakamının basamak değeri nedir?',
              solution: '7 yüzde birler basamağındadır, değeri 0,07\'dir.',
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
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Ondalık Gösterimleri Karşılaştırma ve Sıralama',
        weeklyGoal: 'Ondalık gösterimleri basamak basamak inceleyerek sıralama.',
        evaluationActivity: 'Koşu derecelerini sıralama etkinliği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.17',
            title: 'Ondalık Gösterimleri Karşılaştırma',
            description: 'Ondalık gösterimleri karşılaştırır ve sayı doğrusunda sıralar.',
            processComponents: [
              'a) Önce tam kısımları karşılaştırır.',
              'b) Tam kısımlar eşitse sırasıyla onda birler ve yüzde birler basamağına bakar.'
            ],
            keyConcepts: ['Karşılaştırma', 'Basamak Eşitleme'],
            skills: ['Sıralama', 'Muhakeme'],
            pedagogicalNote: '0,4 ile 0,38 karşılaştırılırken basamak sayısını eşitlemek için 0,40 yapılması kuralı öğretilir.',
            exampleProblem: ExampleProblem(
              context: 'Yüzme Yarışı',
              question: '24,6 saniye ile 24,58 saniye sürelerinden hangisi daha hızlı bir derecedir?',
              solution: '24,58 < 24,60 olduğundan 24,58 saniye daha hızlıdır.',
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
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Ondalık Gösterimlerle Toplama ve Çıkarma',
        weeklyGoal: 'Virgüller alt alta gelecek şekilde ondalık sayılarla toplama ve çıkarma.',
        evaluationActivity: 'Kasa fişi hesaplama görevi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.18',
            title: 'Ondalık Gösterimlerle Toplama ve Çıkarma',
            description: 'Ondalık gösterimlerle toplama ve çıkarma işlemlerini yapar.',
            processComponents: [
              'a) Aynı basamakları ve virgülleri aynı hizaya getirir.',
              'b) Eksik basamaklara sıfır yazarak işlemi yürütür.'
            ],
            keyConcepts: ['Virgül Hizalaması', 'Ondalık Toplama', 'Ondalık Çıkarma'],
            skills: ['Algoritmik Düzen', 'Hesaplama'],
            pedagogicalNote: 'En sık yapılan hata olan virgülleri hizalamadan sağa yaslayarak toplama uyarılır.',
            exampleProblem: ExampleProblem(
              context: 'Alışveriş',
              question: '12,5 TL ve 8,75 TL tutarındaki iki ürünün toplamı kaç TL eder?',
              solution: '12,50 + 8,75 = 21,25 TL.',
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
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Yüzdeler: Yüzde Sembolü (%) ile İfade Etme',
        weeklyGoal: 'Paydası 100 olan kesirleri yüzde sembolüyle gösterme ve kesir-yüzde-ondalık dönüşümü.',
        evaluationActivity: 'Yüzlük kare boyama etkinliği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.1.19',
            title: 'Yüzde Kavramı ve Sembolü',
            description: 'Paydası 100 olan veya 100 yapılabilen kesirleri yüzde sembolü (%) ile gösterir.',
            processComponents: [
              'a) Yüzlük kartta boyanan kare sayısını yüzde olarak adlandırır.',
              'b) Kesir, ondalık ve yüzde gösterimlerini birbirine dönüştürür.'
            ],
            keyConcepts: ['Yüzde Sembolü (%)', 'Yüzlük Kart', 'Eşdeğer Gösterim'],
            skills: ['Temsil', 'Dönüştürme'],
            pedagogicalNote: 'Telefon şarj göstergeleri gibi günlük hayattaki yüzdeler kullanılır.',
            exampleProblem: ExampleProblem(
              context: 'Batarya Doluluğu',
              question: 'Bataryanın 3/5\'i dolu olduğuna göre yüzde kaçı doludur?',
              solution: '3/5 kesri 20 ile genişletilirse 60/100 = %60.',
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
        theme: 'Geometrik Şekiller',
        subTheme: 'Temel Geometrik Kavramlar: Doğru, Doğru Parçası, Işın',
        weeklyGoal: 'Doğru, doğru parçası ve ışını sembolle gösterme ve çizme.',
        evaluationActivity: 'Geometri tahtasında modelleme',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.2.1',
            title: 'Doğru, Doğru Parçası ve Işın',
            description: 'Doğru, doğru parçası ve ışını açıklar ve sembolle gösterir.',
            processComponents: [
              'a) İki ucu sınırsız olanı doğru [AB veya d], bir ucu sınırlı olanı ışın [AB), iki ucu sınırlı olanı doğru parçası [AB] olarak tanımlar.'
            ],
            keyConcepts: ['Doğru', 'Doğru Parçası', 'Işın', 'Uç Noktası'],
            skills: ['Geometrik Temsil', 'Çizim'],
            pedagogicalNote: 'Lazer ışığı (ışın), gergin ip (doğru parçası) somutlaştırmaları yapılır.',
            exampleProblem: ExampleProblem(
              context: 'Güneş Işığı',
              question: 'Güneş ve yaydığı ışık hüzmeleri geometrik olarak neye model oluşturur?',
              solution: 'Başlangıç noktası belli bir yönde uzayan ışına model oluşturur.',
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
        theme: 'Geometrik Şekiller',
        subTheme: 'İki Noktanın Konumu ve Eş Doğru Parçaları',
        weeklyGoal: 'Kareli kâğıtta bir noktanın diğerine göre yön ve birim konumunu belirleme.',
        evaluationActivity: 'Labirent ve hazine haritası konumlama oyunu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.2.2',
            title: 'Noktaların Konumu ve Eşit Uzunluk',
            description: 'Bir noktanın diğer bir noktaya göre konumunu yön ve birim kullanarak ifade eder; eşit uzunlukta doğru parçaları çizer.',
            processComponents: [
              'a) Sağa, sola, yukarı, aşağı adımlarını sayarak konumu belirler.',
              'b) Eğik doğru parçalarının uzunluklarını yatay ve dikey adımlarla karşılaştırır.'
            ],
            keyConcepts: ['Konum', 'Birim', 'Yön', 'Eş Doğru Parçası'],
            skills: ['Uzamsal Yönelim', 'Analiz'],
            pedagogicalNote: 'Navigasyon sistemlerindeki adım tarifi ile ilişkilendirilir.',
            exampleProblem: ExampleProblem(
              context: 'Şehir Haritası',
              question: 'A noktası B noktasının 3 birim solunda ve 4 birim yukarısındadır. B noktası A\'nın neresindedir?',
              solution: '3 birim sağında ve 4 birim aşağısındadır.',
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
        theme: 'Geometrik Şekiller',
        subTheme: 'Açılar: Dar, Dik, Geniş ve Doğru Açı',
        weeklyGoal: 'Açıları 90 derecelik dik açıya göre dar, geniş ve doğru açı olarak sınıflandırma.',
        evaluationActivity: 'Açı ölçer (iletki) ve gönye ile açı ölçümü',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.2.3',
            title: 'Açı Çeşitleri ve Ölçümü',
            description: 'Dar, dik, geniş ve doğru açıları belirler ve çizer.',
            processComponents: [
              'a) 90°\'lik açıyı dik açı olarak referans alır.',
              'b) 90°\'den küçük açıları dar açı, büyükleri geniş açı, 180°\'yi doğru açı olarak sınıflandırır.'
            ],
            keyConcepts: ['Dar Açı', 'Dik Açı (90°)', 'Geniş Açı', 'Doğru Açı (180°)'],
            skills: ['Sınıflandırma', 'Açı Hissi'],
            pedagogicalNote: 'Kapının açılma derecesi veya saat kollarının hareketi ile açılar gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Açı Çeşidi',
              question: 'Ölçüsü 115° olan bir açı hangi açı türüne girer?',
              solution: '90° ile 180° arasında olduğu için geniş açıdır.',
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
        theme: 'Ara Tatil & Pekiştirme',
        subTheme: '2. Dönem Ara Tatili',
        weeklyGoal: 'Ondalık gösterimler, yüzdeler ve temel geometri konularının pekiştirilmesi.',
        evaluationActivity: 'Beceri temelli dijital soru çözümleri',
        isHoliday: true,
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.T2',
            title: 'Ara Tatil Tekrarı',
            description: 'Geometri ve sayılar alanlarındaki pratiklerin tekrarı.',
            processComponents: ['a) Günlük hayatta açı ve yüzde örneklerini fotoğraflar.'],
            keyConcepts: ['Tekrar', 'Pekiştirme'],
            skills: ['Gözlem', 'Öz Değerlendirme'],
            pedagogicalNote: 'Doğadaki açılar fotoğraf projesi önerilir.',
            exampleProblem: ExampleProblem(
              context: 'Fotoğraf',
              question: 'Makasın açık kolları 45° ise bu açı nedir?',
              solution: 'Dar açıdır.',
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
        subTheme: 'Üçgen Çeşitleri (Açılarına ve Kenarlarına Göre)',
        weeklyGoal: 'Üçgenleri kenarlarına (eşkenar, ikizkenar, çeşitkenar) ve açılarına göre sınıflandırma.',
        evaluationActivity: 'Geometri çubuklarıyla üçgen inşası',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.2.4',
            title: 'Üçgenleri Sınıflandırma',
            description: 'Üçgenleri kenar uzunluklarına ve açı ölçülerine göre sınıflandırır.',
            processComponents: [
              'a) Eşkenar üçgenin tüm iç açılarının 60° olduğunu kavrar.',
              'b) Bir üçgende birden fazla geniş açı veya dik açı olamayacağını sorgular.'
            ],
            keyConcepts: ['Eşkenar Üçgen', 'İkizkenar Üçgen', 'Çeşitkenar Üçgen', 'Dik Üçgen'],
            skills: ['Sınıflandırma', 'Geometrik Muhakeme'],
            pedagogicalNote: 'Üçgen eşitsizliği sezdirilerek her üç çubukla üçgen oluşturulamayacağı keşfettirilir.',
            exampleProblem: ExampleProblem(
              context: 'Trafik Levhası',
              question: 'Tüm kenarları 60 cm olan tehlike uyarı levhası kenarlarına göre hangi üçgendir?',
              solution: 'Eşkenar üçgendir.',
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
        subTheme: 'Üçgen ve Dörtgenlerin İç Açıları Toplamı',
        weeklyGoal: 'Üçgenin iç açıları toplamının 180°, dörtgenin 360° olduğunu keşfetme.',
        evaluationActivity: 'Üçgen köşelerini yırtıp birleştirme deneyi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.2.5',
            title: 'İç Açılar Toplamı',
            description: 'Üçgenin iç açılarının toplamının 180°, dörtgenin iç açılarının toplamının 360° olduğunu modeller ve bilinmeyen açıyı bulur.',
            processComponents: [
              'a) Üçgenin köşelerini koparıp yan yana dizerek bir doğru açı (180°) oluşturduğunu gösterir.',
              'b) Dörtgeni bir köşegenle iki üçgene ayırarak 180° + 180° = 360° olduğunu bulur.'
            ],
            keyConcepts: ['İç Açı Toplamı (180° / 360°)', 'Köşegen'],
            skills: ['Keşfederek Öğrenme', 'Hesaplama'],
            pedagogicalNote: 'Kâğıt katlama ve kesme etkinliği ile somutlaştırılır.',
            exampleProblem: ExampleProblem(
              context: 'Bilinmeyen Açı',
              question: 'Bir üçgenin iki iç açısı 70° ve 55° ise üçüncü iç açısı kaç derecedir?',
              solution: '70 + 55 = 125°. 180 - 125 = 55° (ikizkenar üçgen).',
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
        theme: 'Geometrik Nicelikler',
        subTheme: 'Uzunluk Ölçme Birimleri ve Dönüşümleri',
        weeklyGoal: 'Metre, kilometre, desimetre, santimetre ve milimetre arasındaki dönüşümleri yapma.',
        evaluationActivity: 'Sınıf içi mezura ile nesne ölçüm tablosu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.3.1',
            title: 'Uzunluk Ölçü Birimleri',
            description: 'Uzunluk ölçme birimlerini tanır, birbirine dönüştürür ve problemleri çözer.',
            processComponents: [
              'a) Her basamak inişte 10 ile çarpma, her basamak çıkışta 10\'a bölme kuralını anlar.'
            ],
            keyConcepts: ['Metre (m)', 'Kilometre (km)', 'Santimetre (cm)', 'Milimetre (mm)'],
            skills: ['Ölçme Becerisi', 'Birim Dönüşümü'],
            pedagogicalNote: 'Merdiven basamağı çizelgesi kullanılarak görsel destek verilir.',
            exampleProblem: ExampleProblem(
              context: 'Yol Mesafesi',
              question: '3 km 450 m kaç metreye eşittir?',
              solution: '3 km = 3000 m. 3000 + 450 = 3450 m.',
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
        theme: 'Geometrik Nicelikler',
        subTheme: 'Zaman Ölçme Birimleri ve Problemleri',
        weeklyGoal: 'Saat, dakika, saniye, gün, hafta, ay ve yıl arasındaki ilişkileri kavrama.',
        evaluationActivity: 'Günlük plan zaman tablosu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.3.2',
            title: 'Zaman Ölçüleri ve Problemleri',
            description: 'Zaman ölçme birimlerini birbirine dönüştürür; zamanla ilgili problemleri çözer.',
            processComponents: [
              'a) 1 saat = 60 dakika, 1 dakika = 60 saniye dönüşümlerini yapar.',
              'b) Başlama saati ve süre verilip bitiş saatini bulur.'
            ],
            keyConcepts: ['Saat', 'Dakika', 'Saniye', 'Süre Hesaplama'],
            skills: ['Zaman Yönetimi', 'Problem Çözme'],
            pedagogicalNote: 'Zaman çıkarma işlemlerinde 60\'lık sistemin onluk sistemden farkı vurgulanır.',
            exampleProblem: ExampleProblem(
              context: 'Film Süresi',
              question: '14.45\'te başlayan bir tiyatro oyunu 1 saat 35 dakika sürerse saat kaçta biter?',
              solution: '14.45 + 1 saat = 15.45. 15.45 + 35 dk = 16.20.',
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
        theme: 'Geometrik Nicelikler',
        subTheme: 'Dikdörtgen ve Karenin Çevre Uzunluğu',
        weeklyGoal: 'Çevre bağıntılarını çıkarma ve aynı çevreye sahip farklı geometrik şekiller oluşturma.',
        evaluationActivity: 'İp ile geometrik şekil çevre tasarımı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.3.3',
            title: 'Çevre Uzunluğu Hesaplama',
            description: 'Çokgenlerin çevre uzunluklarını hesaplar; aynı çevre uzunluğuna sahip farklı dikdörtgenler oluşturur.',
            processComponents: [
              'a) Dikdörtgenin çevresinin 2 × (Kısa Kenar + Uzun Kenar) olduğunu doğrular.'
            ],
            keyConcepts: ['Çevre', 'Kısa Kenar', 'Uzun Kenar'],
            skills: ['Uzamsal Modelleme', 'Geometrik Hesap'],
            pedagogicalNote: 'Çevre uzunluğunun bir ip uzunluğu gibi tüm dış kenarların toplamı olduğu anlatılır.',
            exampleProblem: ExampleProblem(
              context: 'Bahçe Teli',
              question: 'Uzun kenarı 18 m, kısa kenarı 12 m olan dikdörtgen bahçenin çevresi kaç metredir?',
              solution: 'Çevre = 2 × (18 + 12) = 2 × 30 = 60 metre.',
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
        theme: 'Geometrik Nicelikler',
        subTheme: 'Dikdörtgenin Alanı ve Alan Problemleri',
        weeklyGoal: 'Birim karelerle alan kavramını kavrama ve Kısa Kenar × Uzun Kenar bağıntısını uygulama.',
        evaluationActivity: 'Kareli kâğıtta oda planı alan hesabı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.3.4',
            title: 'Dikdörtgenin Alanı',
            description: 'Dikdörtgenin alanını hesaplar, santimetrekare ve metrekare birimlerini kullanır.',
            processComponents: [
              'a) Bir yüzeyi kaplayan birim kare sayısının alan olduğunu kavrar.',
              'b) Çevre ile alan arasındaki kavramsal farkı açıklar.'
            ],
            keyConcepts: ['Alan', 'Birim Kare', 'Metrekare (m²)', 'Santimetrekare (cm²)'],
            skills: ['Formül Çıkarımı', 'Problem Çözme'],
            pedagogicalNote: 'Çevre ile alanın birbirine karıştırılması en yaygın yanılgıdır; somut örneklerle ayrıştırılır.',
            exampleProblem: ExampleProblem(
              context: 'Halı Alanı',
              question: 'Boyu 4 metre, eni 3 metre olan bir salon halısının alanı kaç m²\'dir?',
              solution: 'Alan = 4 × 3 = 12 m².',
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
        theme: 'Veri İşleme',
        subTheme: 'Araştırma Sorusu, Sıklık Tablosu ve Sütun Grafiği',
        weeklyGoal: 'Araştırma sorusu üretme, veri toplama, sıklık tablosu ve sütun grafiği oluşturma.',
        evaluationActivity: 'Sınıf içi anket çalışması ve grafik sergisi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.4.1',
            title: 'Veri Toplama ve Sütun Grafiği',
            description: 'Veri toplamayı gerektiren araştırma soruları oluşturur, verileri sıklık tablosu ve sütun grafiğinde gösterir.',
            processComponents: [
              'a) Grafiğe uygun başlık ve eksen isimleri verir.',
              'b) Sütun yüksekliklerini karşılaştırarak yorum yapar.'
            ],
            keyConcepts: ['Araştırma Sorusu', 'Çetele / Sıklık Tablosu', 'Sütun Grafiği', 'Eksen'],
            skills: ['Veri Okuryazarlığı', 'İletişim'],
            pedagogicalNote: 'Tek bir kişiye sorulan soru değil ("Senin en sevdiğin renk ne?"), gruba yönelik sorular araştırma sorusudur.',
            exampleProblem: ExampleProblem(
              context: 'En Sevilen Spor',
              question: 'Sınıfta 12 kişi futbol, 8 kişi basketbol, 6 kişi voleybol seçtiyse toplam kaç öğrenci oy kullanmıştır?',
              solution: '12 + 8 + 6 = 26 öğrenci.',
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
        theme: 'Yıl Sonu Değerlendirme',
        subTheme: 'Matematik Bilim Şenliği ve Yıl Sonu Analizi',
        weeklyGoal: '5. sınıf boyunca edinilen tüm matematiksel kazanımların oyunlar ve projelerle kutlanması.',
        evaluationActivity: 'Matematik İstasyonları Şenliği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.5.YIL',
            title: 'Yıl Sonu Süreç Değerlendirmesi',
            description: '5. sınıf kazanımlarının 6. sınıfa hazırlık bağlamında sentezlenmesi.',
            processComponents: ['a) Ortaokulun ilk yılını başarıyla tamamlayarak 6. sınıf hazırlığını tamamlar.'],
            keyConcepts: ['Genel Tekrar', 'Maarif Yetkinlikleri'],
            skills: ['Öz Değerlendirme', 'Matematik Sevgisi'],
            pedagogicalNote: 'Öğrencilerin matematiğe yönelik pozitif tutumları desteklenir.',
            exampleProblem: ExampleProblem(
              context: 'Yıl Sonu Sorusu',
              question: 'Bir kenarı 5 cm olan karenin alanı ile çevresinin toplamı sayısal olarak kaçtır?',
              solution: 'Alan = 25 cm², Çevre = 20 cm. Toplam = 25 + 20 = 45.',
            ),
          ),
        ],
      ),
    ],
  );
}
