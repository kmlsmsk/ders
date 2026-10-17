import '../models/curriculum_model.dart';

class Grade6Data {
  static final GradeCurriculum curriculum = GradeCurriculum(
    grade: 6,
    title: '6. Sınıf',
    subtitle: 'Türkiye Yüzyılı Maarif Modeli (7 Tema)',
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
        subTheme: 'Doğal Sayıların Kendisiyle Tekrarlı Çarpımı (Üslü İfadeler)',
        weeklyGoal: 'Doğal sayıların tekrarlı çarpımını an üssü n şeklinde yazma ve değerini hesaplama.',
        evaluationActivity: 'Üslü ifade kart eşleştirme oyunu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.1',
            title: 'Üslü İfadeler',
            description: 'Bir doğal sayının kendisiyle tekrarlı çarpımını üslü ifade olarak yazar ve değerini belirler.',
            processComponents: [
              'a) Taban ve üs kavramlarını açıklar.',
              'b) 10\'un kuvvetlerinin sondaki sıfır sayısını ve basamak sayısını belirler.'
            ],
            keyConcepts: ['Taban', 'Kuvvet (Üs)', 'Tekrarlı Çarpım', 'Basamak Sayısı'],
            skills: ['Matematiksel Temsil', 'Hesaplama'],
            pedagogicalNote: '2³ ile 2×3 arasındaki fark geometrik küp modeli ile gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Bakteri Çoğalması',
              question: 'Bir bakteri her saatte 2 katına çıkmaktadır. 5 saat sonraki bakteri sayısı üslü olarak nasıl yazılır?',
              solution: '2⁵ = 32 bakteri.',
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
        subTheme: 'İşlem Önceliği ve Dağılma Özelliği',
        weeklyGoal: 'İşlem önceliği sırasını uygulama ve ortak çarpan parantezine alma özelliğini kullanma.',
        evaluationActivity: 'İşlem önceliği yarışması',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.2',
            title: 'İşlem Önceliği ve Dağılma Özelliği',
            description: 'İşlem önceliğini dikkate alarak doğal sayılarla dört işlem yapar; dağılma özelliğini modeller.',
            processComponents: [
              'a) Üslü ifade, parantez, çarpma/bölme, toplama/çıkarma hiyerarşisini takip eder.',
              'b) Çarpmanın toplama ve çıkarma üzerine dağılmasını alan modeliyle gösterir.'
            ],
            keyConcepts: ['İşlem Önceliği', 'Dağılma Özelliği', 'Ortak Çarpan'],
            skills: ['Mantıksal Sıralama', 'Modelleme'],
            pedagogicalNote: 'Aynı önceliğe sahip işlemlerde (çarpma-bölme) soldan sağa işlem yapma kuralı pekiştirilir.',
            exampleProblem: ExampleProblem(
              context: 'İşlem Önceliği',
              question: '24 - 12 ÷ 3 + 2 × 5² işleminin sonucunu bulunuz.',
              solution: '24 - 4 + 2 × 25 = 24 - 4 + 50 = 70.',
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
        subTheme: 'Doğal Sayı Problemleri',
        weeklyGoal: 'Dört işlem ve işlem önceliği gerektiren günlük yaşam problemlerini çözme.',
        evaluationActivity: 'Problem yazma atölyesi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.3',
            title: 'Doğal Sayılarla Problem Çözme',
            description: 'Doğal sayılarla dört işlem yapmayı gerektiren problemleri çözer ve kurar.',
            processComponents: [
              'a) Parantezli ifadeler kullanarak problem durumunu tek bir matematik cümlesiyle yazar.'
            ],
            keyConcepts: ['Matematiksel Cümle', 'Strateji Geliştirme'],
            skills: ['Problem Çözme', 'Muhakeme'],
            pedagogicalNote: 'Öğrencilerin çözümü adım adım açıklamaları istenir.',
            exampleProblem: ExampleProblem(
              context: 'Tiyatro Geliri',
              question: 'Bir salonda 150 tam bilet 80 TL\'den, 80 öğrenci bileti 50 TL\'den satılmıştır. Toplam gelir nedir?',
              solution: '(150 × 80) + (80 × 50) = 12 000 + 4 000 = 16 000 TL.',
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
        subTheme: 'Doğal Sayıların Çarpanları ve Katları',
        weeklyGoal: 'Bir doğal sayının çarpanlarını (bölenlerini) ve katlarını bulma.',
        evaluationActivity: 'Çarpan gökkuşağı yöntemi çalışması',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.4',
            title: 'Çarpanlar ve Katlar',
            description: 'Doğal sayıların çarpanlarını ve katlarını belirler.',
            processComponents: [
              'a) Bir sayının çarpanı ile böleninin aynı anlama geldiğini açıklar.',
              'b) 1\'den başlayarak ikili çarpımlar şeklinde çarpanları sıralar.'
            ],
            keyConcepts: ['Çarpan', 'Bölen', 'Kat', 'Çarpan Gökkuşağı'],
            skills: ['Sistematik Düşünme', 'Sayı Hissi'],
            pedagogicalNote: 'Her doğal sayının en küçük çarpanının 1, en büyüğünün kendisi olduğu vurgulanır.',
            exampleProblem: ExampleProblem(
              context: 'Dikdörtgen Alanı',
              question: 'Alanı 36 cm² olan bir dikdörtgenin kenar uzunlukları kaç farklı doğal sayı çifti olabilir?',
              solution: '1×36, 2×18, 3×12, 4×9, 6×6 olmak üzere 5 farklı durum vardır.',
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
        subTheme: 'Bölünebilme Kuralları (2, 3, 4, 5, 6, 9, 10)',
        weeklyGoal: '2, 3, 4, 5, 6, 9 ve 10 ile kalansız bölünebilme kurallarını kavrama.',
        evaluationActivity: 'Bölünebilme labirenti oyunu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.4',
            title: 'Bölünebilme Kuralları',
            description: '2, 3, 4, 5, 6, 9 ve 10\'a kalansız bölünebilme kurallarını açıklar ve kullanır.',
            processComponents: [
              'a) Son basamağa bağlı olan kurallar (2, 5, 10) ile basamak toplamına bağlı kuralları (3, 9) ayırt eder.',
              'b) Hem 2\'ye hem 3\'e bölünen sayıların 6\'ya da tam bölündüğünü çıkarır.'
            ],
            keyConcepts: ['Bölünebilme', 'Rakamları Toplamı', 'Son İki Basamak'],
            skills: ['Kural Çıkarımı', 'Hızlı Akıl Yürütme'],
            pedagogicalNote: 'Neden 3 ve 9 için basamak toplamına bakıldığı çözümleme mantığıyla hissettirilir.',
            exampleProblem: ExampleProblem(
              context: 'Şifre',
              question: '4A5 sayısı 3\'e kalansız bölünebildiğine göre A\'nın alabileceği rakamlar toplamı kaçtır?',
              solution: '4 + A + 5 = 9 + A. A = 0, 3, 6, 9 olabilir. Toplam = 18.',
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
        subTheme: 'Asal Sayılar ve Asal Çarpanlara Ayırma',
        weeklyGoal: 'Asal sayıları tanıma, Eratosthenes kalburunu uygulama ve asal çarpanlar algoritmasını kullanma.',
        evaluationActivity: 'Eratosthenes kalburu boyama etkinliği ve çarpan ağacı posteri',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.4',
            title: 'Asal Sayılar ve Asal Çarpanlar',
            description: 'Asal sayıları özellikleriyle tanır; bir doğal sayının asal çarpanlarını çarpan ağacı veya bölen listesi yöntemiyle belirler.',
            processComponents: [
              'a) Yalnızca 1\'e ve kendisine bölünebilen 1\'den büyük doğal sayıları asal sayı olarak tanımlar.',
              'b) En küçük asal sayının 2 olduğunu ve 2\'den başka çift asal sayı olmadığını gerekçelendirir.',
              'c) Sayıları bölen listesi (asal çarpan algoritması) ve çarpan ağacı ile asal çarpanlarının çarpımı şeklinde üslü yazar.'
            ],
            keyConcepts: ['Asal Sayı', 'Eratosthenes Kalburu', 'Bölen Listesi', 'Çarpan Ağacı', 'Asal Çarpan'],
            skills: ['Sınıflandırma', 'Algoritmik Düşünme', 'Matematiksel Kanıtlama'],
            pedagogicalNote: '1\'in neden asal sayı kabul edilmediği, "aritmetiğin temel teoremi" olan tek biçimde asal çarpanlara ayrılma kuralı üzerinden sezdirilir.',
            exampleProblem: ExampleProblem(
              context: 'Şifreleme',
              question: '72 sayısının asal çarpanlarını bölen listesi yöntemiyle bulunuz ve üslü biçimde yazınız.',
              solution: '72 ÷ 2 = 36, 36 ÷ 2 = 18, 18 ÷ 2 = 9, 9 ÷ 3 = 3, 3 ÷ 3 = 1. Asal çarpanları 2 ve 3\'tür. 72 = 2³ × 3².',
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
        subTheme: 'Ortak Bölenler ve Ortak Katlar',
        weeklyGoal: 'İki doğal sayının ortak bölenlerini ve ortak katlarını listeleme yöntemiyle belirleme.',
        evaluationActivity: 'Ortak kat takvimi oluşturma',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.5',
            title: 'Ortak Bölen ve Ortak Kat',
            description: 'İki doğal sayının ortak bölenleri ile ortak katlarını belirler, ilgili problemleri çözer.',
            processComponents: [
              'a) İki sayının bölen listesini çıkararak kesişen ortak bölenleri belirler.',
              'b) Sayıların katlarını yazarak en küçük ortak katta buluşma durumunu modeller.'
            ],
            keyConcepts: ['Ortak Bölen', 'Ortak Kat', 'En Büyük Ortak Bölen', 'En Küçük Ortak Kat'],
            skills: ['Karşılaştırmalı Düşünme', 'Listeleme'],
            pedagogicalNote: '8. sınıftaki EBOB-EKOK konularına zemin hazırlayacak sezgisel liste yaklaşımı kullanılır.',
            exampleProblem: ExampleProblem(
              context: 'Nöbet Tutma',
              question: 'Biri 4 günde bir, diğeri 6 günde bir nöbet tutan iki doktor birlikte ilk nöbetten kaç gün sonra tekrar birlikte tutar?',
              solution: '4 ve 6\'nın en küçük ortak katı 12\'dir. 12 gün sonra birlikte nöbet tutarlar.',
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
        subTheme: 'Ortak Bölen ve Kat Problemleri',
        weeklyGoal: 'Paketleme, paylaştırma ve tekrarlı periyot içeren ortak bölen/kat problemlerini çözme.',
        evaluationActivity: 'Zeytinyağı tenekeleri paylaştırma problem görevi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.5',
            title: 'Ortak Bölen ve Kat Problemleri',
            description: 'İki doğal sayının ortak bölen ve ortak katlarını gerektiren gerçek yaşam problemlerini çözer.',
            processComponents: [
              'a) Parçalama/bölme durumunda ortak böleni kullanacağını fark eder.',
              'b) Birleştirme/tekrar durumunda ortak katı kullanacağını fark eder.'
            ],
            keyConcepts: ['Parçalama', 'Eşit Şişeleme', 'Periyodik Buluşma'],
            skills: ['Problem Çözme', 'Strateji'],
            pedagogicalNote: 'Soruda bütünden parçaya mı, parçadan bütüne mi gidildiği sorgulanır.',
            exampleProblem: ExampleProblem(
              context: 'Zeytinyağı Şişeleme',
              question: '24 litre ve 36 litrelik iki farklı zeytinyağı eşit hacimli ve hiç artmayacak şekilde şişelere doldurulacaktır. En büyük şişe kaç litre olur?',
              solution: '24 ve 36\'nın ortak bölenleri: 1, 2, 3, 4, 6, 12. En büyük şişe 12 litredir.',
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
        subTheme: 'Kümeler: Temel Kavramlar ve Gösterimler',
        weeklyGoal: 'Küme kavramını, eleman sembollerini, liste ve Venn şeması gösterimlerini öğrenme.',
        evaluationActivity: 'Sınıf içi ilgi alanları Venn şeması oluşturma',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.6',
            title: 'Kümeler ve Gösterimleri',
            description: 'Kümeler ile ilgili temel kavramları açıklar; kesişim ve birleşim işlemlerini yapar.',
            processComponents: [
              'a) İyi tanımlanmış nesneler topluluğunun küme oluşturduğunu fark eder.',
              'b) Liste yöntemi, ortak özellik ve Venn şemasıyla gösterir.',
              'c) Kesişim (∩) ve birleşim (∪) sembollerini şema üzerinde gösterir.'
            ],
            keyConcepts: ['Küme', 'Eleman (∈)', 'Boş Küme (∅)', 'Kesişim (∩)', 'Birleşim (∪)'],
            skills: ['Sınıflandırma', 'Görsel Temsil'],
            pedagogicalNote: '"Güzel çiçekler" gibi öznel ifadelerin küme belirtmediği tartışılır.',
            exampleProblem: ExampleProblem(
              context: 'Ders Seçimi',
              question: 'A = {1, 2, 3, 4} ve B = {3, 4, 5, 6} kümeleri için A ∩ B ve s(A ∪ B) değerlerini bulunuz.',
              solution: 'A ∩ B = {3, 4}. A ∪ B = {1, 2, 3, 4, 5, 6} olduğundan eleman sayısı s = 6.',
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
        weeklyGoal: 'Çarpanlar, katlar, asal sayılar ve kümeler kazanımlarının tekrar edilmesi.',
        evaluationActivity: 'Dijital soru bankası pekiştirme modülü',
        isHoliday: true,
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.T1',
            title: 'Ara Tatil Tekrarı',
            description: 'İlk 9 haftalık kazanımların beceri temelli sorularla analizi.',
            processComponents: ['a) Sayı kuramının temel kavramlarını gözden geçirir.'],
            keyConcepts: ['Genel Tekrar', 'Analiz'],
            skills: ['Öz Değerlendirme'],
            pedagogicalNote: 'Eğlenceli sayı bulmacaları çözdürülür.',
            exampleProblem: ExampleProblem(
              context: 'Bulmaca',
              question: 'İki basamaklı en küçük asal sayı kaçtır?',
              solution: '11\'dir.',
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
        subTheme: 'Tam Sayılar: Pozitif ve Negatif Sayılar',
        weeklyGoal: 'Tam sayıların günlük hayattaki yönlü anlamını kavrama (sıcaklık, zemin altı, borç/alacak).',
        evaluationActivity: 'Termometre ve asansör çizim çalışması',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.7',
            title: 'Tam Sayı Kavramı ve Yönlü Sayılar',
            description: 'Tam sayıları tanır ve yönlü sayılarla günlük yaşam durumlarını ilişkilendirir.',
            processComponents: [
              'a) Sıfırın referans noktası olduğunu, sağının/üstünün pozitif (+), solunun/altının negatif (-) olduğunu modeller.',
              'b) 0\'ın işaretsiz bir tam sayı olduğunu belirtir.'
            ],
            keyConcepts: ['Tam Sayı (Z)', 'Pozitif (+)', 'Negatif (-)', 'Referans Noktası (0)'],
            skills: ['Kavramsal Anlama', 'Gerçek Yaşam Bağlantısı'],
            pedagogicalNote: 'Deniz seviyesi (0 m), sıfırın altındaki derinlikler ve rakım ilişkisi kurulur.',
            exampleProblem: ExampleProblem(
              context: 'Denizaltı',
              question: 'Deniz seviyesinin 45 metre altındaki bir batık hangi tam sayıyla gösterilir?',
              solution: '-45 ile gösterilir.',
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
        subTheme: 'Tam Sayıları Sayı Doğrusunda Gösterme ve Sıralama',
        weeklyGoal: 'Tam sayıları sayı doğrusuna yerleştirme ve sağa gittikçe büyüme kuralını uygulama.',
        evaluationActivity: 'Sayı doğrusu üzerinde tam sayı sıralama yarışı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.7',
            title: 'Tam Sayıları Sıralama',
            description: 'Tam sayıları sayı doğrusunda gösterir ve karşılaştırır.',
            processComponents: [
              'a) Sayı doğrusunda sağdaki sayının daima soldakinden büyük olduğunu kavrar.',
              'b) Negatif sayılarda sıfırdan uzaklaştıkça değerin küçüldüğünü muhakeme eder.'
            ],
            keyConcepts: ['Sayı Doğrusu', 'Büyüklük-Küçüklük', 'Yön'],
            skills: ['Karşılaştırmalı Muhakeme', 'Sıralama'],
            pedagogicalNote: '-10\'un -2\'den neden daha soğuk/küçük olduğu termometre ile gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Hava Sıcaklığı',
              question: '-8, +3, -2, 0 tam sayılarını küçükten büyüğe sıralayınız.',
              solution: '-8 < -2 < 0 < +3.',
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
        subTheme: 'Mutlak Değer Kavramı ve Anlamı',
        weeklyGoal: 'Mutlak değerin başlangıç noktasına olan uzaklık olduğunu ve asla negatif olamayacağını anlama.',
        evaluationActivity: 'Uzaklık ölçüm cetveli etkinliği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.8',
            title: 'Mutlak Değer',
            description: 'Bir tam sayının mutlak değerini belirler ve başlangıç noktasına olan uzaklık olarak yorumlar.',
            processComponents: [
              'a) Uzaklığın negatif olamayacağını, bu nedenle mutlak değerin en az 0 olduğunu açıklar.',
              'b) |-5| = 5 ve |+5| = 5 eşitliğini sayı doğrusunda gösterir.'
            ],
            keyConcepts: ['Mutlak Değer (|x|)', 'Uzaklık', 'Başlangıç Noktası'],
            skills: ['Kavramsal Anlamlandırma', 'Geometrik Yorum'],
            pedagogicalNote: 'Adım atarken geri gitsek bile kat edilen mesafenin pozitif olduğu örneği verilir.',
            exampleProblem: ExampleProblem(
              context: 'Uzaklık',
              question: '|-15| + |+7| - |-3| işleminin sonucunu bulunuz.',
              solution: '15 + 7 - 3 = 19.',
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
        subTheme: 'Kesirleri Karşılaştırma, Sıralama ve Sayı Doğrusu',
        weeklyGoal: 'Kesirleri ortak payda veya ortak pay stratejileriyle sıralama.',
        evaluationActivity: 'Kesir karşılaştırma kartları',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.9',
            title: 'Kesirleri Sıralama',
            description: 'Kesirleri karşılaştırır, sıralar ve sayı doğrusunda gösterir.',
            processComponents: [
              'a) Paydaları eşitleme veya bütüne/yarıma yakınlık referanslarını kullanır.'
            ],
            keyConcepts: ['Payda Eşitleme', 'Referans Noktası'],
            skills: ['Muhakeme', 'Sıralama'],
            pedagogicalNote: 'Kesirlerin payları arasındaki kat ilişkileri fark ettirilir.',
            exampleProblem: ExampleProblem(
              context: 'Yarış',
              question: '5/6, 7/12 ve 2/3 kesirlerini büyükten küçüğe sıralayınız.',
              solution: 'Paydalar 12\'de eşitlenirse: 10/12, 7/12, 8/12. Sıralama: 5/6 > 2/3 > 7/12.',
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
        subTheme: 'Kesirlerle Toplama ve Çıkarma İşlemleri',
        weeklyGoal: 'Paydaları farklı kesirlerle ve tam sayılı kesirlerle toplama ve çıkarma.',
        evaluationActivity: 'Hata arama çalışma kâğıdı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.10',
            title: 'Kesirlerle Toplama ve Çıkarma',
            description: 'Kesirlerle toplama ve çıkarma işlemlerini yapar.',
            processComponents: [
              'a) EKOK kullanarak en küçük ortak paydada buluşur.',
              'b) Tam sayılı kesirleri bileşik kesre çevirerek çıkarma işlemini güvenle yürütür.'
            ],
            keyConcepts: ['Ortak Payda', 'Tam Sayılı Kesir'],
            skills: ['Hesaplama Akıcılığı', 'Algoritmik Düzen'],
            pedagogicalNote: 'Tam kısımlar çıkarılırken kesir kısmının yetmediği durumlar vurgulanır.',
            exampleProblem: ExampleProblem(
              context: 'Pasta Dilimleri',
              question: '2 tam 1/3 - 1 tam 3/4 işlemini yapınız.',
              solution: '7/3 - 7/4 = (28 - 21) / 12 = 7/12.',
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
        subTheme: 'Kesirlerle Çarpma İşlemi ve Modelleme',
        weeklyGoal: 'İki kesrin çarpımını alan modeliyle görselleştirme ve bir sayının kesir kadarını hesaplama.',
        evaluationActivity: 'Şeffaf kesir asetatlarıyla üst üste koyma deneyi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.11',
            title: 'Kesirlerle Çarpma İşlemi',
            description: 'İki kesrin çarpma işlemini yapar ve modeller; bir doğal sayı ile kesrin çarpımını açıklar.',
            processComponents: [
              'a) Bir bütünü önce dikey sonra yatay bölerek kesişen bölgenin alanını çarpmayla ilişkilendirir.',
              'b) 1\'den küçük bir kesirle çarpıldığında sayının küçüldüğünü fark eder.'
            ],
            keyConcepts: ['Alan Modeli', 'Çarpım', 'Sadeleştirme', 'Kesrin Kesri'],
            skills: ['Modelleme', 'Kavramsal Çıkarım'],
            pedagogicalNote: '"Çarpma işlemi daima sayıyı büyütür" genel yanılgısı 1/2 × 1/4 = 1/8 örneği ile çürütülür.',
            exampleProblem: ExampleProblem(
              context: 'Tarla Ekimi',
              question: 'Bir tarlanın 3/4\'ünün 2/5\'ine mısır ekilmiştir. Tüm tarlanın kaçta kaçına mısır ekilmiştir?',
              solution: '(3/4) × (2/5) = 6/20 = 3/10.',
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
        subTheme: 'Kesirlerle Bölme İşlemi',
        weeklyGoal: 'Kesirlerle bölme işleminde ikinci kesri ters çevirip çarpma kuralının mantığını keşfetme.',
        evaluationActivity: 'Birim kesir paylaşım etkinliği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.12',
            title: 'Kesirlerle Bölme İşlemi',
            description: 'Bir doğal sayıyı bir kesre ve bir kesri bir doğal sayıya böler; iki kesrin bölme işlemini yapar.',
            processComponents: [
              'a) 3 bütünde kaç tane 1/2 olduğunu sayarak bölmenin ölçme anlamını kavrar (3 ÷ 1/2 = 6).',
              'b) Bir kesre bölmenin, o kesrin tersiyle çarpmak olduğunu algoritmik olarak uygular.'
            ],
            keyConcepts: ['Ters Çevirip Çarpma', 'Ölçme Anlamı', 'Bölme'],
            skills: ['Algoritmik Mantık', 'Problem Çözme'],
            pedagogicalNote: 'Kuralı ezberletmeden önce "Kaç yarım elma var?" gibi somut sorularla başlanır.',
            exampleProblem: ExampleProblem(
              context: 'Şişeleme',
              question: '6 litre limonata 3/4 litrelik şişelere doldurulacaktır. Kaç şişe gerekir?',
              solution: '6 ÷ (3/4) = 6 × (4/3) = 24 / 3 = 8 şişe.',
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
        subTheme: 'Kesir Problemleri ve İşlem Tahmini',
        weeklyGoal: 'Kesirlerle dört işlem gerektiren çok adımlı problemleri çözme ve sonucu tahmin etme.',
        evaluationActivity: 'Tarif uyarlama problem görevi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.13',
            title: 'Kesir Problemleri ve Tahmin',
            description: 'Kesirlerle işlem yapmayı gerektiren problemleri çözer; işlem sonuçlarını tahmin eder.',
            processComponents: [
              'a) Kesirleri 0, 1/2 ve 1 bütüne yuvarlayarak tahmini sonuç üretir.'
            ],
            keyConcepts: ['Kesir Problemi', 'Kalanın Kesri', 'Tahmin'],
            skills: ['Problem Çözme', 'Tahmin'],
            pedagogicalNote: 'Kutu çizimi veya şerit şema ile problem adımları görselleştirilir.',
            exampleProblem: ExampleProblem(
              context: 'Yolculuk',
              question: '400 km yolun önce 2/5\'ini, sonra kalanın 1/3\'ünü giden bir şoförün geriye kaç km yolu kalır?',
              solution: 'İlk = 160 km. Kalan = 240 km. İkinci = 240 ÷ 3 = 80 km. Kalan = 240 - 80 = 160 km.',
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
        subTheme: '1. Dönem Genel Değerlendirmesi',
        weeklyGoal: '1. Dönem boyunca edinilen çarpanlar, kümeler, tam sayılar ve kesirler ünitelerinin sentezi.',
        evaluationActivity: 'Dönem sonu bilgi yarışması ve karne portfolyosu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.D1',
            title: '1. Dönem Sonu Sentezi',
            description: '1. Dönem matematik öğrenme alanlarının bütüncül değerlendirmesi.',
            processComponents: ['a) Sayı sistemleri ve işlemler arasındaki köprüleri açıklar.'],
            keyConcepts: ['Genel Tekrar', 'Öz Değerlendirme'],
            skills: ['Sentez', 'İletişim'],
            pedagogicalNote: 'Öğrencinin güçlü olduğu yönler öne çıkarılır.',
            exampleProblem: ExampleProblem(
              context: 'Dönem Sorusu',
              question: '|-12| / 3 + 2 × (3/2) işleminin sonucu kaçtır?',
              solution: '12 / 3 + 3 = 4 + 3 = 7.',
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
        subTheme: 'Ondalık Gösterimleri Bölme Algoritması ile Bulma',
        weeklyGoal: 'Payı paydaya bölerek ondalık açılımları ve devirli sayıları keşfetme.',
        evaluationActivity: 'Hesap makinesi ve uzun bölme karşılaştırması',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.14',
            title: 'Bölme ile Ondalık Gösterim',
            description: 'Bölme işlemi ile kesirlerin ondalık gösterimini bulur; devirli ondalık gösterimleri tanır.',
            processComponents: [
              'a) Kalanın sıfır olmadığı durumlarda bölünenin yanına virgül ve sıfırlar koyarak bölmeyi sürdürür.',
              'b) Kalanın sürekli tekrar ettiği devirli ondalık gösterimleri devir çizgisiyle belirtir.'
            ],
            keyConcepts: ['Ondalık Gösterim', 'Devirli Sayı', 'Devir Çizgisi'],
            skills: ['Algoritmik Keşif', 'Muhakeme'],
            pedagogicalNote: '1/3 = 0,333... örneği üzerinden sonsuz devir mantığı konuşulur.',
            exampleProblem: ExampleProblem(
              context: 'Bölme',
              question: '7/4 kesrinin ondalık gösterimini bölme algoritmasıyla bulunuz.',
              solution: '7 ÷ 4 = 1,75.',
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
        subTheme: 'Ondalık Gösterimleri Yuvarlama',
        weeklyGoal: 'Ondalık gösterimleri onda birler veya yüzde birler basamağına göre yuvarlama.',
        evaluationActivity: 'Yuvarlama kuralı çarkı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.15',
            title: 'Ondalık Gösterimleri Yuvarlama',
            description: 'Ondalık gösterimleri istenilen basamağa göre yuvarlar.',
            processComponents: [
              'a) Yuvarlanacak basamağın sağındaki rakam 5 veya 5\'ten büyükse 1 artırır, küçükse aynen bırakır.'
            ],
            keyConcepts: ['Yuvarlama', 'Sağdaki Rakam', 'Onda Birler', 'Yüzde Birler'],
            skills: ['Yaklaşık Değer', 'Karar Verme'],
            pedagogicalNote: 'Benzin istasyonlarındaki litre fiyatı yuvarlamaları örnek gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Fiyat',
              question: '18,476 sayısını onda birler ve yüzde birler basamağına göre yuvarlayınız.',
              solution: 'Onda birler: 18,5. Yüzde birler: 18,48.',
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
        subTheme: 'Ondalık Gösterimlerle Çarpma ve Bölme',
        weeklyGoal: 'Ondalık gösterimleri virgül yokmuş gibi çarpıp virgülden sonraki basamakları sayma kuralı.',
        evaluationActivity: 'Virgül yerleştirme alıştırmaları',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.16',
            title: 'Ondalık Çarpma ve Bölme',
            description: 'Ondalık gösterimlerle çarpma ve bölme işlemlerini yapar.',
            processComponents: [
              'a) Çarpanlardaki virgülden sonraki basamak sayısı toplamı kadar sondan sola virgül kaydırır.',
              'b) Bölmede böleni virgülden kurtarmak için genişletme yapar.'
            ],
            keyConcepts: ['Virgül Kaydırma', 'Genişletme', 'Ondalık Çarpım'],
            skills: ['Hesaplama', 'Algoritmik Beceri'],
            pedagogicalNote: 'Bölende virgül bırakılmaz; bölen tam sayı yapılmadan işlem yürütülmez kuralı pekiştirilir.',
            exampleProblem: ExampleProblem(
              context: 'Kumaş Fiyatı',
              question: 'Metresi 24,5 TL olan kumaştan 3,2 metre alan biri kaç TL öder?',
              solution: '24,5 × 3,2 = 78,40 TL.',
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
        subTheme: '10, 100 ve 1000 ile Pratik İşlem & Ondalık Problemleri',
        weeklyGoal: '10, 100, 1000 ile zihinden çarpma ve bölme; ondalık hayat problemlerini çözme.',
        evaluationActivity: 'Döviz kuru ve market faturası hesaplama',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.17',
            title: 'Kısa Yoldan İşlem ve Ondalık Problemleri',
            description: 'Ondalık gösterimleri 10, 100 ve 1000 ile kısa yoldan çarpar ve böler; ilgili problemleri çözer.',
            processComponents: [
              'a) Çarpmada virgül sağa, bölmede virgül sola sıfır sayısı kadar kaydırılır.'
            ],
            keyConcepts: ['Zihinden İşlem', 'Kısa Yol', 'Problem'],
            skills: ['Pratiklik', 'Finansal Okuryazarlık'],
            pedagogicalNote: 'Basamakların büyümesi ve küçülmesi mantığı ile yönler açıklanır.',
            exampleProblem: ExampleProblem(
              context: 'Toptan Alış',
              question: 'Tanesi 0,75 TL olan silgilerden 100 tane alan kırtasiyeci kaç TL öder?',
              solution: '0,75 × 100 = 75 TL.',
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
        subTheme: 'Oran Kavramı ve Birimli - Birimsiz Oran',
        weeklyGoal: 'İki çokluğun birbirine bölünerek karşılaştırılmasını ve birimli/birimsiz oran farkını kavrama.',
        evaluationActivity: 'Hız ve yoğunluk birimli oran kartları',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.1.18',
            title: 'Oran ve Oran Türleri',
            description: 'İki çokluğun karşılaştırılmasında oranı kullanır; birimli ve birimsiz oranları ayırt eder.',
            processComponents: [
              'a) Birimleri aynı olan çoklukların oranının birimsiz oran olduğunu fark eder.',
              'b) km/sa veya m/sn gibi farklı birimli çoklukların oranını birimli oran olarak adlandırır.'
            ],
            keyConcepts: ['Oran', 'Birimli Oran', 'Birimsiz Oran', 'Hız (km/sa)'],
            skills: ['Orantısal Akıl Yürütme', 'Fiziksel İlişkilendirme'],
            pedagogicalNote: 'Hızın aslında alınan yolun geçen süreye oranı olduğu gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Araç Hızı',
              question: '180 km yolu 3 saatte alan bir aracın hızı birimli oran olarak nasıl yazılır?',
              solution: '180 km / 3 sa = 60 km/sa (birimli oran).',
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
        subTheme: 'Cebirsel İfadelerin Anlamı ve Değişken Kavramı',
        weeklyGoal: 'Harflerin sayıları temsil ettiğini anlama ve sözel ifadeleri cebirsel olarak yazma.',
        evaluationActivity: 'Sözel durum - cebirsel ifade eşleştirme oyunu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.2.1',
            title: 'Cebirsel İfade ve Değişken',
            description: 'Cebirsel ifadelerin anlamını açıklar; sözel olarak verilen bir duruma uygun cebirsel ifade yazar.',
            processComponents: [
              'a) En az bir değişken (harf) ve işlem içeren ifadeleri cebirsel ifade olarak adlandırır.',
              'b) Terim, katsayı ve sabit terim kavramlarını ayırt eder.'
            ],
            keyConcepts: ['Cebirsel İfade', 'Değişken (Bilinmeyen)', 'Terim', 'Katsayı', 'Sabit Terim'],
            skills: ['Soyutlama', 'Cebirsel Temsil'],
            pedagogicalNote: 'Bilinmeyenin "kutu" yerine artık evrensel bir harfle (x, a, y) gösterildiği açıklanır.',
            exampleProblem: ExampleProblem(
              context: 'Yaş İfadesi',
              question: '"Bir sayının 3 katının 5 fazlası" sözel cümlesini cebirsel olarak ifade ediniz.',
              solution: '3x + 5.',
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
        subTheme: 'Cebirsel İfadenin Değerini Hesaplama',
        weeklyGoal: 'Değişkenin verilen sayısal değerine göre cebirsel ifadenin sonucunu hesaplama.',
        evaluationActivity: 'Cebirsel makine oyunu (Girdi - Kural - Çıktı)',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.2.1',
            title: 'Cebirsel İfadenin Değerini Bulma',
            description: 'Cebirsel ifadenin değerini değişkenin alacağı farklı doğal sayı değerleri için hesaplar.',
            processComponents: [
              'a) Değişkenin yerine sayıyı yazıp işlem önceliğine göre sonucu bulur.'
            ],
            keyConcepts: ['Yerine Koyma', 'Hesaplama', 'İşlem Sırası'],
            skills: ['Hesaplama', 'Algoritmik Akıcılık'],
            pedagogicalNote: '3x ifadesinin 3 ile x\'in çarpımı olduğu, 30+x olmadığı hatırlatılır.',
            exampleProblem: ExampleProblem(
              context: 'Fonksiyon Değeri',
              question: '2x + 7 cebirsel ifadesinin x = 6 için değerini bulunuz.',
              solution: '2(6) + 7 = 12 + 7 = 19.',
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
        theme: 'İstatistiksel Araştırma Süreci',
        subTheme: 'İki Veri Grubunu Karşılaştıran Araştırma Sorusu ve Veri Toplama',
        weeklyGoal: 'Kızlar-erkekler, iki farklı okul gibi iki grubu karşılaştıran araştırma soruları üretme.',
        evaluationActivity: 'Sınıf anketi hazırlama ve veri tablosu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.4.1',
            title: 'İkili Veri Toplama ve Sıklık Tablosu',
            description: 'İki veri grubunu karşılaştırmayı gerektiren araştırma soruları oluşturur; ikili sıklık tablosunda gösterir.',
            processComponents: [
              'a) İki farklı grubun verilerini aynı tabloda satır ve sütunlarla organize eder.'
            ],
            keyConcepts: ['İki Veri Grubu', 'İkili Sıklık Tablosu', 'Araştırma Sorusu'],
            skills: ['Veri Okuryazarlığı', 'İstatistik'],
            pedagogicalNote: 'Karşılaştırmalı soruların karar verme süreçlerindeki önemi anlatılır.',
            exampleProblem: ExampleProblem(
              context: 'Spor Anketi',
              question: '"Kız ve erkek öğrencilerin haftalık kitap okuma süreleri arasında fark var mıdır?" sorusu uygun bir araştırma sorusu mudur?',
              solution: 'Evet, iki grubu karşılaştıran geçerli bir araştırma sorusudur.',
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
        weeklyGoal: 'Ondalık işlemler, oran, cebir ve veri konularının pekiştirilmesi.',
        evaluationActivity: 'EBA Beceri fasikülü',
        isHoliday: true,
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.T2',
            title: 'Ara Tatil Değerlendirmesi',
            description: 'Cebirsel düşünme ve oran kavramlarının soru çözümleriyle pekiştirilmesi.',
            processComponents: ['a) Tatil sürecinde matematiksel pratikleri canlı tutar.'],
            keyConcepts: ['Tekrar', 'Pekiştirme'],
            skills: ['Öz Düzenleme'],
            pedagogicalNote: 'Problem çözme stratejileri tavsiye edilir.',
            exampleProblem: ExampleProblem(
              context: 'Tekrar',
              question: '4x - 1 ifadesinde x=5 için değer kaçtır?',
              solution: '4(5) - 1 = 19.',
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
        theme: 'İstatistiksel Araştırma Süreci',
        subTheme: 'Aritmetik Ortalama ve Açıklık (Ranj)',
        weeklyGoal: 'Bir veri grubunun aritmetik ortalamasını ve açıklığını hesaplayarak verileri yorumlama.',
        evaluationActivity: 'Not ortalaması ve açıklık hesaplama tablosu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.4.2',
            title: 'Aritmetik Ortalama ve Açıklık',
            description: 'Bir veri grubuna ait aritmetik ortalamayı ve açıklığı hesaplar; verileri yorumlar.',
            processComponents: [
              'a) Verilerin toplamını veri sayısına bölerek aritmetik ortalamayı bulur.',
              'b) En büyük değer ile en küçük değer arasındaki farkı "açıklık" olarak hesaplar.',
              'c) Açıklığın verilerdeki kararlılığı/değişkenliği gösterdiğini yorumlar.'
            ],
            keyConcepts: ['Aritmetik Ortalama', 'Açıklık (Ranj)', 'İstikrar', 'Değişkenlik'],
            skills: ['İstatistiksel Muhakeme', 'Karar Verme'],
            pedagogicalNote: 'Açıklığı az olan bir sporcunun daha istikrarlı olduğu örneği verilir.',
            exampleProblem: ExampleProblem(
              context: 'Basketbol Skoru',
              question: 'Bir oyuncunun 4 maçtaki sayıları: 12, 18, 20, 14. Ortalama ve açıklığı nedir?',
              solution: 'Toplam = 64. Ortalama = 64 ÷ 4 = 16 sayı. Açıklık = 20 - 12 = 8.',
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
        theme: 'İstatistiksel Araştırma Süreci',
        subTheme: 'İkili Sütun Grafiği ve Veri Yorumlama',
        weeklyGoal: 'İki veri grubuna ait verileri ikili sütun grafiğinde görselleştirme ve karşılaştırma.',
        evaluationActivity: 'İkili sütun grafiği çizimi ve analiz raporu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.4.3',
            title: 'İkili Sütun Grafiği',
            description: 'İki gruba ait verileri ikili sütun grafiğiyle gösterir ve yorumlar.',
            processComponents: [
              'a) İki sütunu farklı renk veya desenlerle gösteren gösterge (lejant) ekler.',
              'b) Grupların birbirine üstünlük sağladığı durumları analiz eder.'
            ],
            keyConcepts: ['İkili Sütun Grafiği', 'Lejant (Gösterge)', 'Karşılaştırma'],
            skills: ['Görsel Yorumlama', 'Veri Analizi'],
            pedagogicalNote: 'İki ilin aylık sıcaklıklarını karşılaştıran grafikler çizdirilir.',
            exampleProblem: ExampleProblem(
              context: 'Satış Karşılaştırması',
              question: 'A ve B şirketlerinin ilk 3 ay satışları grafikte verildiğinde toplamda hangi şirket öndedir?',
              solution: 'Her ayın satışları toplanarak genel lider belirlenir.',
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
        subTheme: 'Açılar: Komşu, Tümler, Bütünler ve Ters Açılar',
        weeklyGoal: 'Komşu, tümler (toplamı 90°), bütünler (toplamı 180°) ve ters açıların özelliklerini keşfetme.',
        evaluationActivity: 'Makas ve cetvelle kesişen doğrular açı ölçümü',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.3.1',
            title: 'Açı İlişkileri (Tümler, Bütünler, Ters)',
            description: 'Komşu, tümler, bütünler ve ters açıların özelliklerini keşfeder; ilgili problemleri çözer.',
            processComponents: [
              'a) Toplamı 90° olan iki açıyı tümler açı olarak tanımlar.',
              'b) Toplamı 180° olan iki açıyı bütünler açı olarak tanımlar.',
              'c) Kesişen iki doğrudan zıt yöne bakan ters açıların ölçülerinin eşit olduğunu kanıtlar.'
            ],
            keyConcepts: ['Komşu Açı', 'Tümler Açı (90°)', 'Bütünler Açı (180°)', 'Ters Açı'],
            skills: ['Geometrik Muhakeme', 'Mantıksal Çıkarım'],
            pedagogicalNote: 'Tümler ile Bütünler kelimelerinin hece sayısı veya harf kodlamasıyla hatırlanması sağlanır.',
            exampleProblem: ExampleProblem(
              context: 'Açı Problemi',
              question: 'Ölçüsü 35° olan açının tümleri ile bütünlerinin ölçüleri toplamı kaçtır?',
              solution: 'Tümleri = 90 - 35 = 55°. Bütünleri = 180 - 35 = 145°. Toplam = 55 + 145 = 200°.',
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
        subTheme: 'Paralelkenarın Alan Bağıntısı ve Yükseklik',
        weeklyGoal: 'Paralelkenarın bir kenarı ve o kenara ait yüksekliğiyle alan formülünü (Taban × Yükseklik) çıkarma.',
        evaluationActivity: 'Kâğıttan üçgen kesip dikdörtgene dönüştürme etkinliği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.3.2',
            title: 'Paralelkenarın Alanı',
            description: 'Paralelkenarın alan bağıntısını oluşturur, ilgili problemleri çözer.',
            processComponents: [
              'a) Paralelkenarın bir köşesinden dikme indirip üçgeni diğer tarafa yapıştırarak dikdörtgen elde eder.',
              'b) Alan = Taban × Yükseklik (a · h) olduğunu doğrular.'
            ],
            keyConcepts: ['Paralelkenar Alanı', 'Taban', 'Yükseklik (h)', 'Dikme'],
            skills: ['Modelleme', 'Formül Çıkarımı'],
            pedagogicalNote: 'Hangi taban alınıyorsa o tabana ait yüksekliğin çarpılması gerektiği uyarılır.',
            exampleProblem: ExampleProblem(
              context: 'Otopark Alanı',
              question: 'Taban uzunluğu 12 m ve bu tabana ait yüksekliği 5 m olan paralelkenarın alanı kaç m²\'dir?',
              solution: 'Alan = 12 × 5 = 60 m².',
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
        subTheme: 'Üçgenin Alan Bağıntısı',
        weeklyGoal: 'Üçgenin alanının paralelkenarın yarısı olduğunu (Taban × Yükseklik / 2) modelleyerek bulma.',
        evaluationActivity: 'Köşegen boyunca kesilen paralelkenardan iki eş üçgen elde etme',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.3.3',
            title: 'Üçgenin Alanı',
            description: 'Üçgenin alan bağıntısını oluşturur, ilgili problemleri çözer.',
            processComponents: [
              'a) İki eş üçgenin birleşerek paralelkenar oluşturduğunu gösterir.',
              'b) Alan = (Taban × Yükseklik) / 2 bağıntısını çıkarır.',
              'c) Geniş açılı üçgende yüksekliğin dışarıda olduğunu fark eder.'
            ],
            keyConcepts: ['Üçgen Alanı', 'Dış Yükseklik', 'Dik Üçgen Alanı'],
            skills: ['Geometrik İspat', 'Hesaplama'],
            pedagogicalNote: 'Geniş açılı üçgenin yüksekliğinin üçgenin dışından tabanın uzantısına indiği bizzat çizdirilir.',
            exampleProblem: ExampleProblem(
              context: 'Yelken Bezi',
              question: 'Tabanı 8 metre ve yüksekliği 6 metre olan üçgen şeklindeki yelkenin alanı kaç m²\'dir?',
              solution: 'Alan = (8 × 6) / 2 = 48 / 2 = 24 m².',
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
        subTheme: 'Alan Ölçme Birimleri ve Arazi Ölçüleri (Ar, Dekar, Hektar)',
        weeklyGoal: 'm², dm², cm², mm² alan birimleri ile ar, dekar (dönüm), hektar arazi birimleri arası dönüşümler.',
        evaluationActivity: 'Tarla ve arsa parselasyon planı hesaplama',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.3.4',
            title: 'Alan ve Arazi Ölçü Birimleri',
            description: 'Alan ölçme birimlerini tanır; ar, dekar ve hektar arasındaki ilişkileri açıklar.',
            processComponents: [
              'a) Alan birimlerinde her basamakta 100 ile çarpılıp 100\'e bölündüğünü kavrar.',
              'b) 1 ar = 100 m², 1 dekar (dönüm) = 1000 m², 1 hektar = 10 000 m² eşitliklerini kullanır.'
            ],
            keyConcepts: ['Metrekare (m²)', 'Ar', 'Dekar (Dönüm)', 'Hektar'],
            skills: ['Birim Dönüşümü', 'Problem Çözme'],
            pedagogicalNote: 'Tarımda yaygın kullanılan "dönüm" kelimesinin dekar ile eşdeğer olduğu belirtilir.',
            exampleProblem: ExampleProblem(
              context: 'Fındık Bahçesi',
              question: '5 dönüm fındık bahçesi kaç metrekaredir?',
              solution: '5 dekar = 5 × 1000 = 5000 m².',
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
        theme: 'Geometrik Nicelikler',
        subTheme: 'Dikdörtgenler Prizmasının Hacmi',
        weeklyGoal: 'Birim küplerle prizmanın hacmini oluşturma ve Taban Alanı × Yükseklik (a · b · c) bağıntısını çıkarma.',
        evaluationActivity: 'Birim küplerle kutu doldurma deneyi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.3.5',
            title: 'Dikdörtgenler Prizmasının Hacmi',
            description: 'Dikdörtgenler prizmasının hacim bağıntısını oluşturur; birim küplerle modeller.',
            processComponents: [
              'a) Tabandaki birim küp sayısının kat adediyle çarpımının toplam hacmi verdiğini kavrar.',
              'b) Hacim = a × b × c formülünü uygular.'
            ],
            keyConcepts: ['Hacim', 'Birim Küp', 'Prizma Hacmi', 'Metreküp (m³)'],
            skills: ['Uzamsal Düşünme', '3 Boyutlu Modelleme'],
            pedagogicalNote: 'Koli içine kaç tane sabun sığacağı gibi günlük pratik hacim soruları yöneltilir.',
            exampleProblem: ExampleProblem(
              context: 'Akvaryum',
              question: 'Boyutları 50 cm, 30 cm ve 40 cm olan dikdörtgenler prizması akvaryumun hacmi kaç cm³\'tür?',
              solution: '50 × 30 × 40 = 60 000 cm³.',
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
        subTheme: 'Sıvı Ölçme ve 6. Sınıf Genel Yetkinlik Değerlendirmesi',
        weeklyGoal: 'Litre, mililitre ile hacim birimleri ilişkisi (1 dm³ = 1 L) ve yıl sonu genel tekrarı.',
        evaluationActivity: 'Yıl sonu proje sergisi ve akran değerlendirmesi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.6.YIL',
            title: 'Yıl Sonu Beceri ve Kazanım Değerlendirmesi',
            description: '6. sınıf kazanımlarının 7. sınıf cebir ve rasyonel sayılar köprüsüne transferi.',
            processComponents: ['a) Sıvı ölçüleri ile hacim ölçüleri arasındaki dönüşümleri yapar (1 L = 1000 cm³).'],
            keyConcepts: ['Litre', 'Mililitre', 'Hacim-Sıvı Köprüsü', 'Genel Tekrar'],
            skills: ['Metabilişsel Değerlendirme', 'Bilimsel İletişim'],
            pedagogicalNote: '7. sınıfa hazırlık bağlamında öğrencilerin matematik motivasyonu pekiştirilir.',
            exampleProblem: ExampleProblem(
              context: 'Su Deposu',
              question: 'Hacmi 3000 dm³ olan bir su deposu kaç litre su alır?',
              solution: '1 dm³ = 1 Litre olduğundan 3000 Litre su alır.',
            ),
          ),
        ],
      ),
    ],
  );
}
