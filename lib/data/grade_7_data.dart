import '../models/curriculum_model.dart';

class Grade7Data {
  static final GradeCurriculum curriculum = GradeCurriculum(
    grade: 7,
    title: '7. Sınıf',
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
        subTheme: 'Tam Sayılarla İşlemler',
        weeklyGoal: 'Tam sayılarla toplama ve çıkarma işlemlerini modelleme ve kavrama.',
        evaluationActivity: 'Sayma pulları ve sayı doğrusu çalışma kâğıdı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.1',
            title: 'Tam Sayılarla Toplama ve Çıkarma İşlemleri',
            description: 'Tam sayılarla toplama ve çıkarma işlemlerini yapar, ilgili problemleri modeller.',
            processComponents: [
              'a) Sayma pulları ve sayı doğrusu kullanarak toplama ve çıkarma işlemlerini modeller.',
              'b) Çıkarma işleminin toplama işlemiyle olan ilişkisini açıklar.',
              'c) Toplama işleminin değişme, birleşme ve etkisiz eleman özelliklerini fark eder.'
            ],
            keyConcepts: ['Tam Sayı', 'Pozitif ve Negatif Yön', 'Sayı Doğrusu', 'Sayma Pulu'],
            skills: ['Matematiksel Muhakeme', 'Modelleme', 'Temsil'],
            pedagogicalNote: 'İşaret karmaşasını önlemek için sıcaklık farkı ve asansör modelleri kullanılır.',
            exampleProblem: ExampleProblem(
              context: 'Sıcaklık Değişimi',
              question: 'Erzurum\'da gece -9 °C olan sıcaklık gündüz 14 °C artmıştır. Gündüz sıcaklığı kaç °C olur?',
              solution: '(-9) + (+14) = +5 °C olarak bulunur.',
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
        subTheme: 'Tam Sayılarla İşlemler',
        weeklyGoal: 'Tam sayılarla çarpma ve bölme işlemlerinin kurallarını mantıksal olarak yapılandırma.',
        evaluationActivity: 'Kavram haritası ve işaret tablosu oluşturma',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.1',
            title: 'Tam Sayılarla Çarpma ve Bölme İşlemleri',
            description: 'Tam sayılarla çarpma ve bölme işlemlerini yapar, işaret kurallarını gerekçelendirir.',
            processComponents: [
              'a) Aynı işaretli ve zıt işaretli tam sayıların çarpım ve bölüm işaretini belirler.',
              'b) Çarpmanın toplama ve çıkarma üzerine dağılma özelliğini kullanır.',
              'c) 0 ile çarpma ve 0\'a bölmenin özel durumlarını yorumlar.'
            ],
            keyConcepts: ['İşaret Kuralı', 'Çarpma', 'Bölme', 'Dağılma Özelliği'],
            skills: ['Matematiksel Muhakeme', 'İlişkilendirme'],
            pedagogicalNote: 'İki negatif sayının çarpımının neden pozitif olduğu örüntülerle keşfettirilir.',
            exampleProblem: ExampleProblem(
              context: 'Derinlik Hesaplama',
              question: 'Bir denizaltı dakikada 12 metre dalış yapmaktadır. 5 dakika sonraki konumu nedir?',
              solution: '5 × (-12) = -60 metre olarak bulunur.',
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
        subTheme: 'Tam Sayıların Kuvvetleri',
        weeklyGoal: 'Tam sayıların kuvvetlerini ve parantezli üslü ifadelerin farkını öğrenme.',
        evaluationActivity: 'Üslü ifade eşleştirme kartları',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.1',
            title: 'Tam Sayıların Kendisiyle Tekrarlı Çarpımı',
            description: 'Tam sayıların kendileri ile tekrarlı çarpımını üslü nicelik olarak ifade eder.',
            processComponents: [
              'a) Negatif bir tam sayının tek ve çift kuvvetlerinin işaretini açıklar.',
              'b) (-3)² ile -3² arasındaki farkı işlem önceliği ve parantez ilişkisiyle ayırt eder.',
              'c) Sıfırıncı kuvvetin anlamını irdeler.'
            ],
            keyConcepts: ['Taban', 'Üs (Kuvvet)', 'Tek Kuvvet', 'Çift Kuvvet', 'Parantez Önceliği'],
            skills: ['Matematiksel Temsil', 'Eleştirel Düşünme'],
            pedagogicalNote: 'Tabandaki parantez varlığı ile yokluğunun işaret üzerindeki farkı vurgulanır.',
            exampleProblem: ExampleProblem(
              context: 'İşlem Önceliği',
              question: '(-4)² - 2³ işleminin sonucunu bulunuz.',
              solution: '(-4)² = +16, 2³ = 8. 16 - 8 = 8.',
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
        subTheme: 'Tam Sayı Problemleri',
        weeklyGoal: 'Tam sayılarla işlem gerektiren günlük hayat problemlerini çözebilme.',
        evaluationActivity: 'Problem kurma ve akran değerlendirme formu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.1',
            title: 'Tam Sayılarla Problem Çözme',
            description: 'Tam sayılarla işlemler yapmayı gerektiren problemleri çözer ve kurar.',
            processComponents: [
              'a) Problemi anlar ve verilenleri tam sayılarla modeller.',
              'b) Uygun matematiksel strateji belirleyerek adımları uygular.',
              'c) Sonucun gerçek yaşam durumuna uygunluğunu kontrol eder.'
            ],
            keyConcepts: ['Problem Çözme', 'Doğrulama', 'Girdi-Çıktı'],
            skills: ['Problem Çözme', 'Muhakeme'],
            pedagogicalNote: 'Öğrencilerin kendi günlük yaşam senaryolarını kurmaları teşvik edilir.',
            exampleProblem: ExampleProblem(
              context: 'Mali Bakiye',
              question: 'Bir esnaf birinci gün 450 TL zarar, ikinci gün 800 TL kâr, üçüncü gün 200 TL zarar etmiştir. Durum nedir?',
              solution: '(-450) + (+800) + (-200) = +150 TL kâr.',
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
        subTheme: 'Rasyonel Sayılar ve Ondalık Gösterim',
        weeklyGoal: 'Rasyonel sayı kavramını anlama, sayı doğrusunda gösterme ve devirli ondalık açılımları keşfetme.',
        evaluationActivity: 'İnteraktif sayı doğrusu etkinliği ve açık uçlu soru',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.2',
            title: 'Rasyonel Sayı Kavramı ve Ondalık Gösterim',
            description: 'Rasyonel sayıları tanır, sayı doğrusunda gösterir ve ondalık gösterimlerini bölme algoritmasıyla ifade eder.',
            processComponents: [
              'a) a/b (b≠0) biçimindeki sayıları rasyonel sayı olarak tanımlar.',
              'b) Negatif ve pozitif rasyonel sayıları sayı doğrusunda ardışık tam sayılar arasına yerleştirir.',
              'c) Payı paydaya bölerek devirli ve devirsiz ondalık gösterimleri keşfeder.'
            ],
            keyConcepts: ['Rasyonel Sayı (Q)', 'Sayı Doğrusu', 'Devirli Ondalık Gösterim', 'Bölme Algoritması'],
            skills: ['Matematiksel Anlamlandırma', 'Temsil'],
            pedagogicalNote: 'Paydanın 0 olması durumunun tanımsızlık oluşturduğu kesir şeritleriyle somutlaştırılır.',
            exampleProblem: ExampleProblem(
              context: 'Ondalık Dönüşüm',
              question: '5/3 rasyonel sayısını ondalık gösterimle yazınız.',
              solution: '5 bölü 3 = 1,666... = 1,6̄ (1 tam devirli 6).',
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
        subTheme: 'Rasyonel Sayılarda Karşılaştırma ve Sıralama',
        weeklyGoal: 'Rasyonel sayıların karşılaştırma ve sıralama ilişkilerini farklı stratejilerle yapılandırma.',
        evaluationActivity: 'Sayı doğrusunda sıralama simülasyonu ve çıkış kartı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.3',
            title: 'Rasyonel Sayıları Sıralama ve Karşılaştırma',
            description: 'Rasyonel sayıların karşılaştırma ve sıralama ilişkilerini yorumlayabilme, sayı doğrusunda sıralayabilme.',
            processComponents: [
              'a) Paydaları veya payları eşitleme stratejisini kullanarak rasyonel sayıları sıralar.',
              'b) Yarıma ve bütüne (0, 1/2, 1) yakınlık referans stratejisini kullanarak karşılaştırma yapar.',
              'c) Negatif rasyonel sayıların sıralamasını pozitif sayılara göre zıt yönlü olarak muhakeme eder.',
              'd) İki rasyonel sayı arasında sonsuz sayıda rasyonel sayı olduğu (yoğunluk özelliği) çıkarımını yapar.'
            ],
            keyConcepts: [
              'Rasyonel Sıralama',
              'Payda Eşitleme',
              'Yarıma Yakınlık',
              'Bütüne Yakınlık',
              'Negatif Sıralama',
              'Yoğunluk Özelliği'
            ],
            skills: ['Karşılaştırmalı Muhakeme', 'Analitik Düşünme', 'Matematiksel Temsil'],
            pedagogicalNote: 'Negatif rasyonel sayılarda sıfırdan uzaklaştıkça değerin küçüldüğü mantığı sayı doğrusu ve borç senaryolarıyla pekiştirilir.',
            exampleProblem: ExampleProblem(
              context: 'Yarış Sıralaması',
              question: '-3/4, -5/8 ve -1/2 rasyonel sayılarını küçükten büyüğe sıralayınız.',
              solution: 'Paydalar 8\'de eşitlenirse: -6/8, -5/8, -4/8 elde edilir. Negatif sayılarda mutlak değeri büyük olan küçük olduğundan: -3/4 < -5/8 < -1/2.',
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
        subTheme: 'Rasyonel Sayılarla Toplama ve Çıkarma',
        weeklyGoal: 'Rasyonel sayılarla toplama ve çıkarma işlemlerini algoritmik ve kavramsal olarak kavrama.',
        evaluationActivity: 'İşlem basamakları tanılayıcı dallanmış ağaç testi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.4',
            title: 'Rasyonel Sayılarla Toplama ve Çıkarma İşlemleri',
            description: 'Rasyonel sayılarla toplama ve çıkarma işlemlerini yapar, işlem özelliklerini kullanır.',
            processComponents: [
              'a) Paydaları eşit rasyonel sayılarda payları toplayıp/çıkarıp ortak paydayı korur.',
              'b) Paydaları farklı rasyonel sayılarda EKOK kullanarak payda eşitler.',
              'c) Toplama işleminin değişme, birleşme, etkisiz ve ters eleman özelliklerini açıklar.'
            ],
            keyConcepts: ['Ortak Payda', 'Ters Eleman', 'Etkisiz Eleman', 'Genişletme'],
            skills: ['Algoritmik Düşünme', 'Matematiksel Muhakeme'],
            pedagogicalNote: 'Tam sayılı kesirleri bileşik kesre çevirerek işlem yapma pratikliği gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Hisse Hesabı',
              question: '2/3 + (-5/6) işleminin sonucunu bulunuz.',
              solution: '2/3 kesri 2 ile genişletilirse 4/6 olur. 4/6 + (-5/6) = -1/6.',
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
        subTheme: 'Rasyonel Sayılarla Çarpma ve Bölme',
        weeklyGoal: 'Rasyonel sayılarla çarpma ve bölme işlemlerini kurallarıyla uygulama.',
        evaluationActivity: 'Hata analizi kartları ve eşleştirme oyunu',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.4',
            title: 'Rasyonel Sayılarla Çarpma ve Bölme İşlemleri',
            description: 'Rasyonel sayılarla çarpma ve bölme işlemlerini yapar, sadeleştirme kolaylığını kullanır.',
            processComponents: [
              'a) Payların çarpımını paya, paydaların çarpımını paydaya yazar.',
              'b) Çarpma yapmadan önce çapraz ve alt-üst sadeleştirmeleri uygular.',
              'c) Bölme işleminde ikinci kesrin çarpma işlemine göre tersiyle birinciyi çarpar.'
            ],
            keyConcepts: ['Çarpmaya Göre Ters', 'Çapraz Sadeleştirme', 'İşaret Kuralı'],
            skills: ['Hesaplama Akıcılığı', 'Strateji Geliştirme'],
            pedagogicalNote: 'Bölme işleminde ters çevirip çarpmanın arkasındaki birim kesir mantığı irdelenir.',
            exampleProblem: ExampleProblem(
              context: 'Alan Hesabı',
              question: '(-4/9) × (3/8) işleminin sonucunu en sade haliyle bulunuz.',
              solution: 'Sadeleştirme yapılırsa: (-1/3) × (1/2) = -1/6.',
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
        subTheme: 'Rasyonel Sayıların Kare ve Küpleri, Çok Adımlı İşlemler',
        weeklyGoal: 'Rasyonel sayıların kuvvetlerini alma ve merdivenli çok adımlı işlemleri çözme.',
        evaluationActivity: 'Merdivenli işlem basamak testi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.4',
            title: 'Rasyonel Sayıların Kuvvetleri ve Çok Adımlı İşlemler',
            description: 'Rasyonel sayıların kare ve küplerini hesaplar; çok adımlı işlemleri işlem önceliğine göre çözer.',
            processComponents: [
              'a) Pozitif ve negatif rasyonel sayıların kare ve küplerinin işaretini belirler.',
              'b) Ana kesir çizgisi ile işlem önceliğini (parantez, üs, çarpma/bölme, toplama/çıkarma) belirler.',
              'c) Merdivenli kesirlerde en içteki işlemden başlayarak adım adım ilerler.'
            ],
            keyConcepts: ['Kare ve Küp', 'Ana Kesir Çizgisi', 'Merdivenli Kesir', 'İşlem Önceliği'],
            skills: ['Sıralı Mantık', 'Problem Çözme'],
            pedagogicalNote: 'Ana kesir çizgisinin hizasındaki eşittir ve artı/eksi işaretlerine dikkat çekilir.',
            exampleProblem: ExampleProblem(
              context: 'Kuvvet Hesabı',
              question: '(-2/3)³ işleminin sonucunu bulunuz.',
              solution: '(-2)³ / 3³ = -8/27.',
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
        subTheme: '1. Dönem Ara Tatili / Atatürk Haftası',
        weeklyGoal: 'İlk 9 haftalık kazanımların dijital etkileşimli içeriklerle pekiştirilmesi.',
        evaluationActivity: 'MEB ÖDSGM Beceri Temelli Tekrar Testi',
        isHoliday: true,
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.T1',
            title: 'Ara Tatil Beceri Temelli Tekrar ve Pekiştirme',
            description: 'Tam sayılar ve rasyonel sayılar kazanımlarının analitik muhakeme sorularıyla sentezlenmesi.',
            processComponents: [
              'a) Tam sayılar ve rasyonel sayılar arasındaki sayı kümesi hiyerarşisini özetler.',
              'b) Günlük yaşam problemlerinde çok adımlı işlemleri bağımsız olarak çözer.'
            ],
            keyConcepts: ['Genel Tekrar', 'Problem Çözme Becerisi', 'Kavram Sentezi'],
            skills: ['Öz Değerlendirme', 'Metabilişsel Düşünme'],
            pedagogicalNote: 'Öğrencilere tatil sürecinde eğlenceli matematik zekâ oyunları önerilir.',
            exampleProblem: ExampleProblem(
              context: 'Gerçek Yaşam',
              question: 'Bir termometre -12 °C iken 2/3 katı kadar sıcaklık artışı yaşanırsa son durum ne olur?',
              solution: 'Artış = |-12| × 2/3 = 8 °C. Son sıcaklık: -12 + 8 = -4 °C.',
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
        subTheme: 'Rasyonel Sayı Problemleri',
        weeklyGoal: 'Rasyonel sayılarla işlem yapmayı gerektiren günlük hayat problemlerini çözme.',
        evaluationActivity: 'Gerçek yaşam bütçe ve tarife modelleme görevi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.5',
            title: 'Rasyonel Sayılarla Problem Çözme',
            description: 'Rasyonel sayılarla işlem yapmayı gerektiren problemleri çözer ve matematiksel model kurar.',
            processComponents: [
              'a) Parça-bütün ilişkisini ve kalanın kesrini içeren aşamalı problemleri şematize eder.',
              'b) Alışveriş, bütçe, yakıt tüketimi gibi bağlamlarda rasyonel sayı işlemlerini uygular.'
            ],
            keyConcepts: ['Parça-Bütün', 'Kalanın Kesri', 'Birim Miktar', 'Matematiksel Modelleme'],
            skills: ['Problem Çözme', 'Finansal Okuryazarlık'],
            pedagogicalNote: 'Özellikle "kalan paranın 1/3\'ü" şeklindeki sorularda kutu modelleme tekniği önerilir.',
            exampleProblem: ExampleProblem(
              context: 'Maaş Harcaması',
              question: 'Maaşının 1/3\'ünü kiraya, kalanının 2/5\'ini mutfağa harcayan birinin geriye 12.000 TL\'si kalmıştır. Maaşı kaç TL\'dir?',
              solution: 'Kalan = 2/3. Mutfak = (2/3) × (2/5) = 4/15. Toplam harcanan = 5/15 + 4/15 = 9/15. Kalan = 6/15 = 2/5 = 12.000 TL -> Maaş = 30.000 TL.',
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
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Cebirsel İfadelerle Toplama ve Çıkarma',
        weeklyGoal: 'Cebirsel ifadelerle toplama ve çıkarma işlemlerini modelleyerek kavrama.',
        evaluationActivity: 'Cebir karoları ile modelleme etkinliği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.2.1',
            title: 'Cebirsel İfadelerle Toplama ve Çıkarma',
            description: 'Cebirsel ifadelerle toplama ve çıkarma işlemlerini yapar, benzer terimleri birleştirir.',
            processComponents: [
              'a) Cebir karoları kullanarak cebirsel ifadelerin toplamını ve farkını modeller.',
              'b) Değişkenleri ve kuvvetleri aynı olan terimleri "benzer terim" olarak gruplar.',
              'c) Çıkarma işleminde çıkan ifadedeki tüm terimlerin işaretinin değiştiğini fark eder.'
            ],
            keyConcepts: ['Cebirsel İfade', 'Benzer Terim', 'Katsayı', 'Cebir Karosu'],
            skills: ['Soyutlama', 'Temsil', 'Cebirsel Düşünme'],
            pedagogicalNote: 'Çıkarma işleminde parantezin önündeki eksi işaretinin içeriye dağılması kuralı vurgulanır.',
            exampleProblem: ExampleProblem(
              context: 'Çevre Hesabı',
              question: '(5x - 7) - (2x - 11) ifadesinin en sade halini yazınız.',
              solution: '5x - 7 - 2x + 11 = (5x - 2x) + (-7 + 11) = 3x + 4.',
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
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Cebirsel İfadeleri Çarpma ve Sayı Örüntüleri',
        weeklyGoal: 'Bir doğal sayı ile cebirsel ifadeyi çarpma ve örüntünün kuralını cebirsel olarak yazma.',
        evaluationActivity: 'Örüntü kuralı bulma yarışması ve akran değerlendirmesi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.2.1',
            title: 'Doğal Sayı ile Cebirsel İfadeyi Çarpma ve Örüntüler',
            description: 'Bir doğal sayı ile cebirsel ifadeyi çarpar; aritmetik örüntülerin kuralını harfle ifade eder.',
            processComponents: [
              'a) Dağılma özelliğini cebir karoları ve alan modelleriyle görselleştirir.',
              'b) Artış miktarı sabit olan örüntülerin genel terimini (n. terim) bulur.'
            ],
            keyConcepts: ['Dağılma Özelliği', 'Genel Terim (n)', 'Aritmetik Örüntü'],
            skills: ['Genelleme', 'Cebirsel Temsil'],
            pedagogicalNote: 'Örüntüdeki ortak farkın n\'nin katsayısı olduğu somut adımlarla keşfettirilir.',
            exampleProblem: ExampleProblem(
              context: 'Masa Düzeni',
              question: '4, 11, 18, 25... örüntüsünün kuralını ve 20. terimini bulunuz.',
              solution: 'Artış = 7. Kural = 7n - 3. 20. terim = 7(20) - 3 = 137.',
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
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Eşitliğin Korunumu ve Denklem Kavramı',
        weeklyGoal: 'Eşitliğin korunumunu terazi modeliyle anlamlandırma ve 1. dereceden denklem kurma.',
        evaluationActivity: 'Eşit kollu terazi simülasyon görevi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.2.2',
            title: 'Eşitliğin Korunumu ve Denklem Kurma',
            description: 'Eşitliğin her iki tarafına aynı sayının eklenmesi veya çıkarılması ilkelerini modeller.',
            processComponents: [
              'a) Denge durumundaki terazinin kefelerine aynı kütle eklenip çıkarıldığında dengenin bozulmadığını kavrar.',
              'b) Gerçek yaşam durumlarına uygun birinci dereceden bir bilinmeyenli denklem modeller.'
            ],
            keyConcepts: ['Eşitlik', 'Denklem', 'Bilinmeyen', 'Denge'],
            skills: ['Modelleme', 'Matematiksel Mantık'],
            pedagogicalNote: 'Ezbere "karşıya işaret değiştirerek geçer" demek yerine eşitliğin iki tarafına aynı işlemi yapma mantığı oturtulur.',
            exampleProblem: ExampleProblem(
              context: 'Yaş Problemi',
              question: 'Ali\'nin yaşının 3 katının 5 eksiği 28\'dir. Denklemini kurunuz.',
              solution: '3x - 5 = 28 olarak kurulur.',
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
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Birinci Dereceden Bir Bilinmeyenli Denklemleri Çözme',
        weeklyGoal: 'Parantezli ve rasyonel katsayılı denklemleri sistematik adımlarla çözme.',
        evaluationActivity: 'Denklem çözme aşama kartları kontrolü',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.2.2',
            title: 'Birinci Dereceden Bir Bilinmeyenli Denklem Çözme',
            description: 'Birinci dereceden bir bilinmeyenli denklemleri çözer ve kökün doğruluğunu test eder.',
            processComponents: [
              'a) Parantez varsa dağılma özelliğini uygular.',
              'b) Bilinenleri eşitliğin bir tarafına, bilinmeyenleri diğer tarafına toplar.',
              'c) Bulduğu kökü denklemde yerine yazarak sağlama yapar.'
            ],
            keyConcepts: ['Denklem Kökü', 'Çözüm Kümesi', 'Sağlama'],
            skills: ['Algoritmik Düşünme', 'Doğrulama'],
            pedagogicalNote: 'İşlem adımlarında işaret hatalarını önlemek için her adım alt alta yazdırılır.',
            exampleProblem: ExampleProblem(
              context: 'Denklem Çözümü',
              question: '3(2x - 4) = 4x + 6 denklemini çözünüz.',
              solution: '6x - 12 = 4x + 6 -> 2x = 18 -> x = 9.',
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
        theme: 'İşlemlerle Cebirsel Düşünme',
        subTheme: 'Denklem Kurma Problemleri',
        weeklyGoal: 'Gerçek yaşam senaryolarını denklem kurarak çözebilme.',
        evaluationActivity: 'Senaryo tabanlı problem çözme atölyesi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.2.3',
            title: 'Birinci Dereceden Denklem Problemleri',
            description: 'Birinci dereceden bir bilinmeyenli denklem kurmayı gerektiren problemleri çözer.',
            processComponents: [
              'a) Problemin ana değişkenini (x) doğru seçer.',
              'b) Diğer çoklukları x cinsinden ifade eder.',
              'c) Kurduğu denklemi çözüp cevabın mantıksal tutarlılığını sorgular.'
            ],
            keyConcepts: ['Bilinmeyen Seçimi', 'Denklem Modeli', 'Gerçek Yaşam Bağlamı'],
            skills: ['Problem Çözme', 'Eleştirel Düşünme'],
            pedagogicalNote: 'En küçük veya en temel çokluğa x deme alışkanlığı kazandırılır.',
            exampleProblem: ExampleProblem(
              context: 'Bilet Satışı',
              question: 'Bir sinemada öğrenci bileti tam biletin 15 TL eksiğidir. 3 tam ve 4 öğrenci bileti 410 TL tuttuğuna göre tam bilet kaç TL\'dir?',
              solution: 'Tam = x, Öğrenci = x - 15. 3x + 4(x - 15) = 410 -> 7x - 60 = 410 -> 7x = 470 -> x = ... (uygun veri).',
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
        subTheme: 'Oran ve Doğru Orantı',
        weeklyGoal: 'Orantı kavramını, orantı sabitini ve doğru orantıyı keşfetme.',
        evaluationActivity: 'Mutfak tarifleri orantı tablosu etkinliği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.6',
            title: 'Oran, Orantı ve Doğru Orantı',
            description: 'İki çokluğun orantılı olup olmadığını belirler, doğru orantıyı ve orantı sabitini açıklar.',
            processComponents: [
              'a) İki oranın eşitliğini orantı olarak tanımlar ve içler-dışlar çarpımını kullanır.',
              'b) Bir çokluk artarken diğeri de aynı oranda artıyorsa doğru orantılı olduğunu kavrar.',
              'c) y/x = k orantı sabitini grafik ve tablolarda yorumlar.'
            ],
            keyConcepts: ['Orantı Sabiti (k)', 'Doğru Orantı', 'İçler-Dışlar Çarpımı'],
            skills: ['Orantısal Akıl Yürütme', 'Modelleme'],
            pedagogicalNote: 'Sabit hızla giden aracın aldığı yol gibi günlük doğrusal örnekler verilir.',
            exampleProblem: ExampleProblem(
              context: 'Yakıt Tüketimi',
              question: '100 km\'de 6 litre benzin yakan bir araç 450 km yolda kaç litre benzin tüketir?',
              solution: '100 km -> 6 L ise 450 km -> x L. x = (450 × 6) / 100 = 27 Litre.',
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
        subTheme: 'Ters Orantı ve Orantı Problemleri',
        weeklyGoal: 'Ters orantıyı kavrama, x · y = k bağıntısını çıkarma ve orantı problemlerini çözme.',
        evaluationActivity: 'İşçi-süre ve hız-zaman grafik analizi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.6',
            title: 'Ters Orantı ve Orantı Problemleri',
            description: 'Ters orantılı iki çokluk arasındaki ilişkiyi açıklar; doğru ve ters orantı problemlerini çözer.',
            processComponents: [
              'a) Çokluklardan biri artarken diğeri aynı oranda azalıyorsa ters orantı olduğunu fark eder.',
              'b) Ters orantıda çarpımların sabit (x·y=k) olduğunu modeller.',
              'c) Problemde orantı türünü (doğru mu ters mi) belirleyerek uygun yöntemi uygular.'
            ],
            keyConcepts: ['Ters Orantı', 'Çarpım Sabiti', 'İşçi Problemleri', 'Dişli Çark'],
            skills: ['Orantısal Muhakeme', 'Problem Çözme'],
            pedagogicalNote: 'Dişli çarklarda diş sayısı ile devir sayısı ilişkisi gibi görsel araçlar kullanılır.',
            exampleProblem: ExampleProblem(
              context: 'Duvar Boyama',
              question: 'Bir odayı 4 işçi 6 günde boyuyorsa, aynı hızdaki 8 işçi kaç günde boyar?',
              solution: 'İşçi sayısı 2 katına çıkarsa süre yarıya iner: 4 × 6 = 8 × x -> x = 3 gün.',
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
        subTheme: '1. Dönem Sonu Genel Değerlendirme',
        weeklyGoal: '1. Dönem boyunca edinilen tam sayı, rasyonel sayı, cebir ve orantı kazanımlarını sentezleme.',
        evaluationActivity: '1. Dönem Portfolyo Sunumu ve Beceri Sınavı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.D1',
            title: '1. Dönem Kapsamlı Sentez ve Değerlendirme',
            description: '1. Dönem matematik öğrenme alanlarının bütüncül olarak değerlendirilmesi.',
            processComponents: [
              'a) Öğrenme alanları arası geçiş ve transfer kabiliyetini sergiler.',
              'b) Matematiksel dil ve sembolleri yetkin şekilde kullanır.'
            ],
            keyConcepts: ['Portfolyo', 'Kavram Haritası', 'Öz Değerlendirme'],
            skills: ['Sentez', 'İletişim'],
            pedagogicalNote: 'Öğrencilerin gelişim grafiklerini görmeleri ve güçlü yönlerini fark etmeleri sağlanır.',
            exampleProblem: ExampleProblem(
              context: 'Dönem Sonu Sorusu',
              question: 'Bir orantıda x ile y doğru orantılı, y ile z ters orantılıdır. x=4 iken y=6 ve z=9 ise x=8 iken z kaçtır?',
              solution: 'x iki katına çıkarsa y=12 olur. y iki katına çıkarsa z yarıya iner: z = 9 / 2 = 4,5.',
            ),
          ),
        ],
      ),

      // 20. HAFTA (2. DÖNEM BAŞLANGICI)
      CurriculumWeek(
        weekNumber: 20,
        term: 2,
        dateRange: '02 - 06 Şubat',
        startDate: DateTime(2027, 2, 2),
        endDate: DateTime(2027, 2, 6),
        theme: 'Sayılar ve Nicelikler',
        subTheme: 'Yüzdeler: Bir Çokluğun Yüzdesini Hesaplama',
        weeklyGoal: 'Bir çokluğun belirtilen yüzdesini ve yüzdesi verilen çokluğun tamamını hesaplama.',
        evaluationActivity: 'Market indirim kataloğu inceleme etkinliği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.7',
            title: 'Yüzde Hesaplamaları',
            description: 'Bir çokluğun belirtilen yüzdesini, belirli bir yüzdesi verilen çokluğun tamamını hesaplar.',
            processComponents: [
              'a) Bir sayının %A\'sını bulmak için sayıyı A/100 ile çarpar veya orantı kurar.',
              'b) %20\'si 50 olan sayının tamamını bulma stratejilerini modeller.'
            ],
            keyConcepts: ['Yüzde (%)', 'Orantı', 'Birim Miktar'],
            skills: ['Finansal Okuryazarlık', 'Hesaplama'],
            pedagogicalNote: '%25\'in 1/4, %50\'nin yarım, %10\'un onda bir olduğu zihinden hesaplama ipuçları verilir.',
            exampleProblem: ExampleProblem(
              context: 'İndirim Hesabı',
              question: '600 TL\'lik bir kazağa %30 indirim uygulanırsa indirim tutarı kaç TL olur?',
              solution: '600 × (30/100) = 180 TL.',
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
        subTheme: 'Bir Çokluğu Diğerinin Yüzdesi Olarak Belirleme',
        weeklyGoal: 'Bir çokluğu diğerinin yüzdesi olarak ifade etme ve yüzde artış/azalış hesaplama.',
        evaluationActivity: 'Fiyat artış tablosu oluşturma',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.7',
            title: 'Yüzde Oranı ve Yüzde Değişimi',
            description: 'Bir çokluğu diğerinin yüzdesi olarak belirler; artış ve azalış oranlarını hesaplar.',
            processComponents: [
              'a) 40 sayısının 80\'in yüzde kaçı olduğunu orantı kurarak bulur.',
              'b) Bir ürüne %20 zam yapıldığında yeni fiyatın %120 olduğunu kavrar.'
            ],
            keyConcepts: ['Yüzde Değişim', 'Zam', 'İndirim', 'Oran'],
            skills: ['Muhakeme', 'Analiz'],
            pedagogicalNote: 'Fiyatın önce %10 artıp sonra %10 düşmesinin eski fiyata eşit olmadığı yanılgısı irdelenir.',
            exampleProblem: ExampleProblem(
              context: 'Fiyat Değişimi',
              question: '200 TL\'ye satılan bir ürünün fiyatı 260 TL olursa yüzde kaç zam yapılmıştır?',
              solution: 'Artış = 60 TL. (60 / 200) = 30/100 = %30 zam.',
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
        subTheme: 'Yüzde Problemleri',
        weeklyGoal: 'Kâr, zarar, indirim, KDV ve komisyon içeren yüzde problemlerini çözme.',
        evaluationActivity: 'Ticari simülasyon ve mini girişimcilik projesi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.1.7',
            title: 'Kâr, Zarar ve Yüzde Problemleri',
            description: 'Yüzdelerle ilgili gerçek yaşam problemlerini çözer ve stratejiler geliştirir.',
            processComponents: [
              'a) Alış, maliyet, satış, kâr ve zarar terimlerinin anlamlarını açıklar.',
              'b) KDV\'li fiyat hesaplamalarını yapar.'
            ],
            keyConcepts: ['Kâr / Zarar', 'Maliyet', 'KDV', 'İskonto'],
            skills: ['Problem Çözme', 'Finansal Okuryazarlık'],
            pedagogicalNote: 'Faturalardaki KDV oranları üzerinden gerçek dünya bağlantısı kurulur.',
            exampleProblem: ExampleProblem(
              context: 'Kâr Hesabı',
              question: 'Maliyeti 400 TL olan bir mont %25 kârla satılırken etiket fiyatı üzerinden %10 indirim yapılıyor. Satış fiyatı nedir?',
              solution: 'Kârlı fiyat = 400 + 100 = 500 TL. %10 indirim = 50 TL. Satış = 450 TL.',
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
        theme: 'Geometrik Şekiller',
        subTheme: 'Doğrular ve Açılar: Paralel İki Doğrunun Bir Kesenle Yaptığı Açılar',
        weeklyGoal: 'İç ters, dış ters, yöndeş ve karşı durumlu açıları keşfetme.',
        evaluationActivity: 'Dinamik geometri yazılımı (GeoGebra) açı keşif çalışması',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.3.1',
            title: 'Paralel Doğruların Kesenle Oluşturduğu Açılar',
            description: 'Bir açının açıortayını belirler; paralel iki doğrunun bir kesenle oluşturduğu açıları kavrar.',
            processComponents: [
              'a) Pergel ve cetvel veya dinamik geometri yazılımıyla açıortayı çizer.',
              'b) Yöndeş, iç ters ve dış ters açıların ölçülerinin eşit olduğunu gerekçelendirir.',
              'c) Z, U ve M kurallarını açı bağıntılarıyla ilişkilendirir.'
            ],
            keyConcepts: ['Açıortay', 'Yöndeş Açı', 'İç Ters Açı', 'Z Kuralı', 'U Kuralı'],
            skills: ['Geometrik Muhakeme', 'Uzamsal Düşünme'],
            pedagogicalNote: 'Raylar ve yaya geçitleri gibi mimari yapılardaki paralel çizgiler gösterilir.',
            exampleProblem: ExampleProblem(
              context: 'Z Kuralı',
              question: 'd1 // d2 olmak üzere Z şeklinde iki iç ters açıdan biri 3x - 10° diğeri 2x + 15° ise x kaçtır?',
              solution: '3x - 10 = 2x + 15 -> x = 25°.',
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
        theme: 'Geometrik Şekiller',
        subTheme: 'Açılarla İlgili Problem Çözme',
        weeklyGoal: 'Paralel doğrular ve açılar içeren karmaşık geometrik durumları çözme.',
        evaluationActivity: 'Şekilli bulmaca ve açı zinciri çözümü',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.3.1',
            title: 'Açı Bağıntıları ve Problem Çözme',
            description: 'Paralel iki doğrunun bir kesenle yaptığı açılarla ilgili problemleri çözer.',
            processComponents: [
              'a) Yardımcı paralel doğru çizerek açı sorularını basitleştirir.',
              'b) Kalem ucu (roket) kuralı ve testere kuralını uygular.'
            ],
            keyConcepts: ['Yardımcı Paralel Doğru', 'Kalem Ucu Kuralı', 'M Kuralı'],
            skills: ['Stratejik Çizim', 'Problem Çözme'],
            pedagogicalNote: 'Kırılma noktalarından geçen yardımcı paralel çizme tekniği bizzat çizdirilir.',
            exampleProblem: ExampleProblem(
              context: 'Roket Kuralı',
              question: 'Paralel iki doğru arasında kalan üç iç açının ölçüleri x, 110° ve 130° ise x kaçtır?',
              solution: 'Toplam 360° olmalıdır: x + 110 + 130 = 360 -> x = 120°.',
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
        subTheme: 'Çokgenler: Düzgün Çokgenler ve Açı Özellikleri',
        weeklyGoal: 'Düzgün çokgenlerin iç ve dış açılarının ölçülerini bağıntılarla bulma.',
        evaluationActivity: 'Çokgen tablosu oluşturma ve üçgenlere ayırma etkinliği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.3.2',
            title: 'Düzgün Çokgenlerin İç ve Dış Açıları',
            description: 'Düzgün çokgenlerin kenar ve açı özelliklerini açıklar; iç açılar toplamını geneller.',
            processComponents: [
              'a) n kenarlı çokgenin bir köşesinden (n-3) köşegen çizilip (n-2) üçgen oluştuğunu bulur.',
              'b) İç açılar toplamının (n-2)·180° olduğunu keşfeder.',
              'c) Bütün dış bükey çokgenlerin dış açılar toplamının 360° olduğunu modeller.'
            ],
            keyConcepts: ['Düzgün Çokgen', 'İç Açı Toplamı', 'Dış Açı Toplamı', 'Köşegen'],
            skills: ['Genelleme', 'Geometrik İspat'],
            pedagogicalNote: 'Bal peteği (düzgün altıgen) gibi doğadaki düzgün çokgen örnekleri incelenir.',
            exampleProblem: ExampleProblem(
              context: 'Açı Hesabı',
              question: 'Düzgün bir sekizgenin bir iç açısı ile bir dış açısının ölçüsünü bulunuz.',
              solution: 'Dış açı = 360 / 8 = 45°. İç açı = 180 - 45 = 135°.',
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
        subTheme: 'Özel Dörtgenler (Dikdörtgen, Paralelkenar, Eşkenar Dörtgen, Yamuk)',
        weeklyGoal: 'Özel dörtgenlerin kenar, açı ve köşegen özelliklerini karşılaştırma.',
        evaluationActivity: 'Dörtgenler soy ağacı ve Venn şeması sınıflandırması',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.3.2',
            title: 'Özel Dörtgenlerin Özellikleri',
            description: 'Dikdörtgen, paralelkenar, yamuk ve eşkenar dörtgeni tanır; açı ve köşegen özelliklerini belirler.',
            processComponents: [
              'a) Eşkenar dörtgende köşegenlerin birbirini dik kestiğini ve açıortay olduğunu kavrar.',
              'b) Yamukta tabanların paralel olduğunu ve ardışık iç açıların toplamının 180° olduğunu fark eder.'
            ],
            keyConcepts: ['Paralelkenar', 'Eşkenar Dörtgen', 'Yamuk', 'Dik Kesişen Köşegen'],
            skills: ['Sınıflandırma', 'Mantıksal Çıkarım'],
            pedagogicalNote: 'Her karenin bir eşkenar dörtgen ve aynı zamanda bir dikdörtgen olduğu vurgulanır.',
            exampleProblem: ExampleProblem(
              context: 'Dörtgen Açıları',
              question: 'Bir paralelkenarda ardışık iki açının ölçüsü 2x ve 3x ise büyük açı kaç derecedir?',
              solution: '2x + 3x = 180 -> 5x = 180 -> x = 36°. Büyük açı = 3 × 36 = 108°.',
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
        theme: 'Geometrik Nicelikler',
        subTheme: 'Eşkenar Dörtgen ve Yamuğun Alanı',
        weeklyGoal: 'Eşit alan dönüşümleriyle eşkenar dörtgen ve yamuğun alan formüllerini çıkarma.',
        evaluationActivity: 'Kâğıt katlama ve kesme ile alan ispatı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.3.3',
            title: 'Eşkenar Dörtgen ve Yamuğun Alan Bağıntıları',
            description: 'Eşkenar dörtgen ve yamuğun alan bağıntılarını oluşturur; ilgili problemleri çözer.',
            processComponents: [
              'a) Eşkenar dörtgenin alanının köşegenler çarpımının yarısı olduğunu (e·f/2) dikdörtgene tamamlayarak gösterir.',
              'b) Yamuğun alanının ((Alt Taban + Üst Taban) · Yükseklik) / 2 olduğunu paralelkenara tamamlayarak keşfeder.'
            ],
            keyConcepts: ['Köşegen Çarpımı', 'Alt Taban', 'Üst Taban', 'Yamuk Alanı'],
            skills: ['Modelleme', 'Formül Çıkarımı'],
            pedagogicalNote: 'Formülleri ezberletmek yerine dikdörtgen veya üçgen parçalarına ayırma sezgisi verilir.',
            exampleProblem: ExampleProblem(
              context: 'Çatı Alanı',
              question: 'Alt tabanı 14 m, üst tabanı 8 m ve yüksekliği 6 m olan yamuk şeklindeki çatının alanı kaç m²\'dir?',
              solution: 'Alan = [(14 + 8) × 6] / 2 = (22 × 6) / 2 = 66 m².',
            ),
          ),
        ],
      ),

      // 28. HAFTA (2. DÖNEM ARA TATİLİ)
      CurriculumWeek(
        weekNumber: 28,
        term: 2,
        dateRange: '30 Mart - 03 Nisan',
        startDate: DateTime(2027, 3, 30),
        endDate: DateTime(2027, 4, 3),
        theme: 'Ara Tatil & Pekiştirme',
        subTheme: '2. Dönem Ara Tatili',
        weeklyGoal: 'Yüzdeler, açılar ve çokgenler konularının beceri temelli sorularla tekrarı.',
        evaluationActivity: 'EBA ve MEB ÖDSGM Dijital Fasikülü',
        isHoliday: true,
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.T2',
            title: '2. Dönem Ara Tatil Pekiştirme ve Tekrar',
            description: 'Geometri ve yüzde hesaplamaları beceri temelli soru çözümleri.',
            processComponents: [
              'a) Çokgen alanları ve açı bağıntılarını günlük hayat projelerinde harmanlar.'
            ],
            keyConcepts: ['Tekrar', 'Geometri', 'Soru Çözümü'],
            skills: ['Problem Çözme', 'Öz Düzenleme'],
            pedagogicalNote: 'Mimari planlar üzerinden alan hesaplama çalışmaları önerilir.',
            exampleProblem: ExampleProblem(
              context: 'Peyzaj Projesi',
              question: 'Köşegen uzunlukları 10 m ve 16 m olan eşkenar dörtgen şeklindeki çim alanın metrekaresi 50 TL ise toplam maliyet nedir?',
              solution: 'Alan = (10 × 16) / 2 = 80 m². Maliyet = 80 × 50 = 4.000 TL.',
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
        subTheme: 'Çemberde Merkez Açı ve Gördüğü Yay',
        weeklyGoal: 'Çemberde merkez açı kavramını ve gördüğü yayın ölçüsü ilişkisini anlama.',
        evaluationActivity: 'İletki ile çember çizimi ve merkez açı ölçümü',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.3.4',
            title: 'Çemberde Merkez Açı ve Yay Ölçüsü',
            description: 'Çemberde merkez açıları, gördüğü yayları ve açı-yay ölçüsü ilişkisini açıklar.',
            processComponents: [
              'a) Köşesi çemberin merkezinde olan açıyı "merkez açı" olarak tanımlar.',
              'b) Merkez açının ölçüsünün gördüğü yayın derece cinsinden ölçüsüne eşit olduğunu kavrar.',
              'c) Çember yayının tamamının 360° olduğunu doğrular.'
            ],
            keyConcepts: ['Merkez Açı', 'Çember Yayı', 'Yay Ölçüsü (Derece)', 'Çember'],
            skills: ['Geometrik Temsil', 'Muhakeme'],
            pedagogicalNote: 'Saat kadranı üzerinden akrep ve yelkovanın oluşturduğu merkez açılar örneklendirilir.',
            exampleProblem: ExampleProblem(
              context: 'Saat Açısı',
              question: 'Saat tam 4.00\'ü gösterdiğinde akrep ile yelkovan arasındaki küçük merkez açı ve yay kaç derecedir?',
              solution: 'Her saat aralığı 360 / 12 = 30°. Saat 4 için 4 × 30 = 120°.',
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
        theme: 'Geometrik Nicelikler',
        subTheme: 'Çemberin ve Çember Yayının Uzunluğu',
        weeklyGoal: 'Çemberin çevre formülü (2πr) ile çember parçasının yay uzunluğunu hesaplama.',
        evaluationActivity: 'Tekerlek tur sayısı ve yay uzunluğu deneyi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.3.4',
            title: 'Çember Çevresi ve Yay Uzunluğu',
            description: 'Çemberin çevre uzunluğunu hesaplar; merkez açının gördüğü yayın uzunluğunu orantıyla bulur.',
            processComponents: [
              'a) Çemberin çevresinin çapına oranının π (pi) sayısı olduğunu keşfeder.',
              'b) Çevre = 2·π·r bağıntısını kullanır.',
              'c) α derecelik yayın uzunluğunu (2·π·r) · (α/360) formülüyle veya orantıyla hesaplar.'
            ],
            keyConcepts: ['Pi Sayısı (π)', 'Yarıçap (r)', 'Yay Uzunluğu (cm/m)', 'Çember Çevresi'],
            skills: ['Orantısal Düşünme', 'Hesaplama'],
            pedagogicalNote: 'Yay ölçüsü (derece) ile yay uzunluğu (santimetre) arasındaki kavramsal fark netleştirilir.',
            exampleProblem: ExampleProblem(
              context: 'Bisiklet Tekerleği',
              question: 'Yarıçapı 30 cm olan bir çemberde 60°\'lik merkez açının gördüğü yayın uzunluğu kaç cm\'dir? (π=3 alınız)',
              solution: 'Çevre = 2 × 3 × 30 = 180 cm. 60° için: 180 × (60/360) = 180 / 6 = 30 cm.',
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
        subTheme: 'Dairenin ve Daire Diliminin Alanı',
        weeklyGoal: 'Dairenin alanını (πr²) ve merkez açıya karşılık gelen daire diliminin alanını bulma.',
        evaluationActivity: 'Pizza dilimi alan modelleme ve hesaplama',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.3.4',
            title: 'Dairenin Alanı ve Daire Diliminin Alanı',
            description: 'Dairenin alan bağıntısını oluşturur; daire diliminin alanını hesaplar.',
            processComponents: [
              'a) Daireyi eşit sektörlere bölüp yan yana dizerek paralelkenar/dikdörtgen oluşturup Alan = πr² bağıntısını çıkarır.',
              'b) α açılı daire diliminin alanını (πr²) · (α/360) ile hesaplar.'
            ],
            keyConcepts: ['Daire Alanı', 'Daire Dilimi', 'Sektör', 'Yarıçap'],
            skills: ['Modelleme', 'Geometrik Akıl Yürütme'],
            pedagogicalNote: 'Dairenin içi dolu bir yüzey, çemberin ise sadece bir çevre eğrisi olduğu ayrımı vurgulanır.',
            exampleProblem: ExampleProblem(
              context: 'Fıskiye Sulama Alanı',
              question: 'Bir bahçe fıskiyesi en fazla 6 metre uzağa su atabilmekte ve 90° dönebilmektedir. Sulanan alan kaç m²\'dir? (π=3)',
              solution: 'Alan = 3 × 6² × (90/360) = 3 × 36 × (1/4) = 27 m².',
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
        theme: 'İstatistiksel Araştırma Süreci',
        subTheme: 'Çizgi Grafiği Oluşturma ve Yorumlama',
        weeklyGoal: 'Zaman içindeki sürekli değişimleri çizgi grafiği ile gösterme ve yorumlama.',
        evaluationActivity: 'Haftalık hava sıcaklığı değişim grafiği çizimi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.4.1',
            title: 'Çizgi Grafiği Oluşturma ve Yorumlama',
            description: 'Verileri çizgi grafiği ile gösterir ve grafikler arası çıkarımlar yapar.',
            processComponents: [
              'a) Sürekli verilerin zaman içerisindeki artış ve azalış trendini çizgi grafiğiyle gösterir.',
              'b) Birden fazla veriyi aynı grafikte çift çizgi ile karşılaştırır.'
            ],
            keyConcepts: ['Çizgi Grafiği', 'Sürekli Veri', 'Zamana Bağlı Değişim', 'Eksen Ölçeği'],
            skills: ['Veri Okuryazarlığı', 'Grafik Yorumlama'],
            pedagogicalNote: 'Eksen ölçeğinin eşit aralıklı olmasının doğru algı için önemi üzerinde durulur.',
            exampleProblem: ExampleProblem(
              context: 'Hisse Değeri',
              question: 'Pazartesi 20 TL olan bir hisse Salı 25, Çarşamba 22, Perşembe 30 TL olmuştur. En büyük artış hangi gün aralığındadır?',
              solution: 'Çarşamba-Perşembe arası 8 TL artışla en büyüktür.',
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
        theme: 'İstatistiksel Araştırma Süreci',
        subTheme: 'Merkezi Eğilim Ölçüleri: Ortalama, Medyan (Ortanca) ve Mod (Tepe Değer)',
        weeklyGoal: 'Aritmetik ortalama, ortanca ve tepe değeri hesaplama; uygun temsil ölçüsünü belirleme.',
        evaluationActivity: 'Sınıf boy uzunlukları veri seti istatistik kartı',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.4.2',
            title: 'Merkezi Eğilim Ölçüleri',
            description: 'Aritmetik ortalama, ortanca ve tepe değeri bulur; verileri temsil etmede hangisinin uygun olduğuna karar verir.',
            processComponents: [
              'a) Sayıları küçükten büyüğe dizerek tam ortadaki medyanı belirler.',
              'b) En çok tekrar eden değeri tepe değer (mod) olarak bulur.',
              'c) Uç değerlerin varlığında ortanca ölçüsünün ortalamadan daha güvenilir olduğunu fark eder.'
            ],
            keyConcepts: ['Aritmetik Ortalama', 'Ortanca (Medyan)', 'Tepe Değer (Mod)', 'Uç Değer'],
            skills: ['İstatistiksel Muhakeme', 'Karar Verme'],
            pedagogicalNote: 'Öğrencilerin maaş istatistiklerinde uç zenginlerin ortalamayı nasıl saptırdığı örneği verilir.',
            exampleProblem: ExampleProblem(
              context: 'Sınav Notları',
              question: '3, 5, 5, 7, 8, 9, 20 veri grubunun ortancasını ve tepe değerini bulunuz.',
              solution: 'Sıralı 7 veri var: Ortanca = 7. Tepe değer = 5.',
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
        theme: 'İstatistiksel Araştırma Süreci',
        subTheme: 'Daire Grafiği ve Grafikler Arası Dönüşüm',
        weeklyGoal: 'Bütünün parçalarını daire grafiğinde merkez açılarla gösterme ve diğer grafiklere dönüştürme.',
        evaluationActivity: 'Sınıf başkanlığı seçim sonuçları daire grafiği',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.4.3',
            title: 'Daire Grafiği ve Grafik Dönüşümleri',
            description: 'Verileri daire grafiği ile gösterir; sütun ve çizgi grafiklerini daire grafiğine dönüştürür.',
            processComponents: [
              'a) Toplam veriyi 360° ile eşleştirerek her kategoriye düşen merkez açıyı orantıyla bulur.',
              'b) Daire grafiğindeki açıları yüzdeye veya frekansa çevirir.'
            ],
            keyConcepts: ['Daire Grafiği', 'Oran-Orantı', 'Merkez Açı Paylaşımı'],
            skills: ['Veri Dönüştürme', 'Temsil'],
            pedagogicalNote: 'Daire grafiğinin bir bütünün parçalarını göstermede en etkili görsel olduğu vurgulanır.',
            exampleProblem: ExampleProblem(
              context: 'Bütçe Dağılımı',
              question: 'Toplam 72 sayfalık bir kitabın 18 sayfasını okuyan birinin okuduğu kısım daire grafiğinde kaç derecelik açıyla gösterilir?',
              solution: '(18 / 72) = 1/4. 360°\'nin 1/4\'ü = 90°.',
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
        theme: 'Geometrik Şekiller',
        subTheme: 'Cisimlerin Farklı Yönlerden Görünümleri',
        weeklyGoal: 'Birim küplerden oluşan yapıların önden, arkadan, sağdan, soldan ve üstten görünümlerini çizme.',
        evaluationActivity: 'İzometrik kâğıt üzerine 3B yapı çizimi ve akran kontrolü',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.3.5',
            title: 'Cisimlerin Farklı Yönlerden Görünümleri',
            description: 'Üç boyutlu cisimlerin farklı yönlerden iki boyutlu görünümlerini çizer.',
            processComponents: [
              'a) Birim küplerle oluşturulmuş yapıların üstten görünümünü kat numaralarıyla şematize eder.',
              'b) Sağdan ve soldan görünümlerin birbirinin yansıması olduğunu ayırt eder.'
            ],
            keyConcepts: ['Birim Küp', 'İzometrik Çizim', 'Üstten Görünüm', 'Önden Görünüm'],
            skills: ['Uzamsal Görselleştirme', '3 Boyutlu Düşünme'],
            pedagogicalNote: 'Somut zekâ küpleri sınıfa getirilerek bizzat farklı açılardan fotoğraflanır.',
            exampleProblem: ExampleProblem(
              context: 'Mimari Görünüm',
              question: 'Önden görünümü 3 sütunlu (yükseklikler: 2, 1, 3) olan bir birim küp yapısında en az kaç küp vardır?',
              solution: 'En az 2 + 1 + 3 = 6 küp olmalıdır.',
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
        subTheme: 'Maarif Modeli Matematik Yetkinlik Analizi',
        weeklyGoal: 'Yıl boyunca edinilen tüm matematiksel süreç becerilerini harmanlama ve genel tekrar.',
        evaluationActivity: 'Yıl Sonu Matematik Bilim Şenliği ve Proje Sergisi',
        outcomes: [
          LearningOutcome(
            code: 'MAT.7.YIL',
            title: 'Yıl Sonu Süreç ve Beceri Değerlendirmesi',
            description: '7. sınıf matematik müfredatı kazanımlarının eleştirel düşünme ve problem çözme sentezi.',
            processComponents: [
              'a) 8. sınıf LGS hazırlık temellerine yönelik kavramsal geçiş köprüsünü kurar.',
              'b) Matematiksel modelleme ve problem kurma becerilerini sergiler.'
            ],
            keyConcepts: ['Genel Tekrar', 'Maarif Modeli Yetkinlikleri', 'Gelecek Yıla Hazırlık'],
            skills: ['Metabilişsel Değerlendirme', 'Yaşam Boyu Öğrenme'],
            pedagogicalNote: 'Öğrencilerin bir yıl boyunca kat ettikleri mesafe takdir edilir.',
            exampleProblem: ExampleProblem(
              context: 'Yıl Sonu Sentezi',
              question: 'Yarıçapı 10 cm olan bir dairenin içine çizilebilecek en büyük karenin alanı kaç cm² olur?',
              solution: 'Karenin köşegeni dairenin çapıdır (20 cm). Alan = (20 × 20) / 2 = 200 cm².',
            ),
          ),
        ],
      ),
    ],
  );
}
