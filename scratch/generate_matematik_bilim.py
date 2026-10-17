import os

def create_matematik_bilim_data():
    dates = [
        ("08 - 12 Eylül", 2026, 9, 8, 2026, 9, 12, 1, 1),
        ("15 - 19 Eylül", 2026, 9, 15, 2026, 9, 19, 2, 1),
        ("22 - 26 Eylül", 2026, 9, 22, 2026, 9, 26, 3, 1),
        ("29 Eylül - 03 Ekim", 2026, 9, 29, 2026, 10, 3, 4, 1),
        ("06 - 10 Ekim", 2026, 10, 6, 2026, 10, 10, 5, 1),
        ("13 - 17 Ekim", 2026, 10, 13, 2026, 10, 17, 6, 1),
        ("20 - 24 Ekim", 2026, 10, 20, 2026, 10, 24, 7, 1),
        ("27 - 31 Ekim", 2026, 10, 27, 2026, 10, 31, 8, 1),
        ("03 - 07 Kasım", 2026, 11, 3, 2026, 11, 7, 9, 1),
        ("10 - 14 Kasım", 2026, 11, 10, 2026, 11, 14, 10, 1), # Ara Tatil
        ("17 - 21 Kasım", 2026, 11, 17, 2026, 11, 21, 11, 1),
        ("24 - 28 Kasım", 2026, 11, 24, 2026, 11, 28, 12, 1),
        ("01 - 05 Aralık", 2026, 12, 1, 2026, 12, 5, 13, 1),
        ("08 - 12 Aralık", 2026, 12, 8, 2026, 12, 12, 14, 1),
        ("15 - 19 Aralık", 2026, 12, 15, 2026, 12, 19, 15, 1),
        ("22 - 26 Aralık", 2026, 12, 22, 2026, 12, 26, 16, 1),
        ("29 Aralık - 02 Ocak", 2026, 12, 29, 2027, 1, 2, 17, 1),
        ("05 - 09 Ocak", 2027, 1, 5, 2027, 1, 9, 18, 1),
        ("12 - 16 Ocak", 2027, 1, 12, 2027, 1, 16, 19, 1),
        ("02 - 06 Şubat", 2027, 2, 2, 2027, 2, 6, 20, 2),
        ("09 - 13 Şubat", 2027, 2, 9, 2027, 2, 13, 21, 2),
        ("16 - 20 Şubat", 2027, 2, 16, 2027, 2, 20, 22, 2),
        ("23 - 27 Şubat", 2027, 2, 23, 2027, 2, 27, 23, 2),
        ("02 - 06 Mart", 2027, 3, 2, 2027, 3, 6, 24, 2),
        ("09 - 13 Mart", 2027, 3, 9, 2027, 3, 13, 25, 2),
        ("16 - 20 Mart", 2027, 3, 16, 2027, 3, 20, 26, 2),
        ("23 - 27 Mart", 2027, 3, 23, 2027, 3, 27, 27, 2),
        ("30 Mart - 03 Nisan", 2027, 3, 30, 2027, 4, 3, 28, 2),
        ("06 - 10 Nisan", 2027, 4, 6, 2027, 4, 10, 29, 2), # 2. Ara tatil
        ("13 - 17 Nisan", 2027, 4, 13, 2027, 4, 17, 30, 2),
        ("20 - 24 Nisan", 2027, 4, 20, 2027, 4, 24, 31, 2),
        ("27 Nisan - 01 Mayıs", 2027, 4, 27, 2027, 5, 1, 32, 2),
        ("04 - 08 Mayıs", 2027, 5, 4, 2027, 5, 8, 33, 2),
        ("11 - 15 Mayıs", 2027, 5, 11, 2027, 5, 15, 34, 2),
        ("18 - 22 Mayıs", 2027, 5, 18, 2027, 5, 22, 35, 2),
        ("25 - 29 Mayıs", 2027, 5, 25, 2027, 5, 29, 36, 2),
    ]

    themes = [
        # 1-8
        ("Günlük Hayatta Matematik ve Bilim", "Ölçme, Bütçe ve Doğal Olaylar"),
        ("Günlük Hayatta Matematik ve Bilim", "Tasarruf ve Enerji Verimliliği"),
        ("Günlük Hayatta Matematik ve Bilim", "Akıllı Yaşam ve Teknoloji"),
        ("Günlük Hayatta Matematik ve Bilim", "Mutfakta ve Evde Bilim"),
        ("Günlük Hayatta Matematik ve Bilim", "Çevre ve Geri Dönüşüm"),
        ("Günlük Hayatta Matematik ve Bilim", "Matematiksel Akıl Yürütme"),
        ("Günlük Hayatta Matematik ve Bilim", "Problem Çözme ve Modelleme"),
        ("Günlük Hayatta Matematik ve Bilim", "I. Tema Değerlendirme ve STEM Projesi"),
        # 9-15
        ("Sağlık ve Sporda Matematik ve Bilim", "Besin Değerleri ve Kalori Hesabı"),
        ("Sağlık ve Sporda Matematik ve Bilim", "1. Dönem Ara Tatil"),
        ("Sağlık ve Sporda Matematik ve Bilim", "Nabız, Dolaşım ve Egzersiz Grafikleri"),
        ("Sağlık ve Sporda Matematik ve Bilim", "Vücut Kitle İndeksi ve İstatistik"),
        ("Sağlık ve Sporda Matematik ve Bilim", "Spor Saha Geometrisi ve Açılar"),
        ("Sağlık ve Sporda Matematik ve Bilim", "Hız, Mesafe ve Kuvvet Analizi"),
        ("Sağlık ve Sporda Matematik ve Bilim", "II. Tema Değerlendirme ve Sağlıklı Yaşam Projesi"),
        # 16-22
        ("Sanatta Matematik ve Bilim", "Geometrik Motifler ve Türk İslam Sanatı"),
        ("Sanatta Matematik ve Bilim", "Ebru Sanatında Sıvı Yoğunluğu ve Kimya"),
        ("Sanatta Matematik ve Bilim", "Altın Oran, Mimari ve Estetik"),
        ("Sanatta Matematik ve Bilim", "Müzikteki Ritim, Frekans ve Kesirler"),
        ("Sanatta Matematik ve Bilim", "Origami ve Üç Boyutlu Cisimler"),
        ("Sanatta Matematik ve Bilim", "Perspektif ve Işık-Gölge Geometrisi"),
        ("Sanatta Matematik ve Bilim", "III. Tema Sergisi ve Tasarım Portfolyosu"),
        # 23-29
        ("Doğada Matematik ve Bilim", "Fraktallar ve Doğadaki Geometrik Şekiller"),
        ("Doğada Matematik ve Bilim", "Fibonacci Dizisi ve Bitkilerin Yapısı"),
        ("Doğada Matematik ve Bilim", "Ekosistemdeki Nüfus ve Denge Modelleri"),
        ("Doğada Matematik ve Bilim", "Su Döngüsü ve Hacimsel Hesaplamalar"),
        ("Doğada Matematik ve Bilim", "Biyoçeşitlilik İndeksi ve Veri Analizi"),
        ("Doğada Matematik ve Bilim", "Doğa Gözlem Raporu ve Saha İncelemesi"),
        ("Doğada Matematik ve Bilim", "2. Dönem Ara Tatil"),
        # 30-36
        ("Meslekler ve Matematik ve Bilim", "Mühendislik ve Mimarlıkta Modelleme"),
        ("Meslekler ve Matematik ve Bilim", "Tıp ve Sağlık Alanında Ölçme ve Teknoloji"),
        ("Meslekler ve Matematik ve Bilim", "Yazılım, Kodlama ve Matematiksel Algoritmalar"),
        ("Meslekler ve Matematik ve Bilim", "Astronomi, Uzay ve Sayısal Ölçekler"),
        ("Meslekler ve Matematik ve Bilim", "Yeşil Meslekler ve Sürdürülebilir Kalkınma"),
        ("Meslekler ve Matematik ve Bilim", "Geleceğin Teknolojileri ve Yapay Zekâ"),
        ("Meslekler ve Matematik ve Bilim", "Yıl Sonu Bilim ve Matematik Şenliği / Proje Sunumları"),
    ]

    out = []
    out.append("// GENERATED DATA - MATEMATİK VE BİLİM UYGULAMALARI (MAARİF MODELİ)")
    out.append("import 'package:flutter/material.dart';")
    out.append("import '../../models/curriculum_model.dart';\n")
    out.append("class MatematikBilimCurriculum {")
    out.append("  static final SubjectCurriculum subject = SubjectCurriculum(")
    out.append("    id: 'matematik_bilim',")
    out.append("    name: 'Matematik ve Bilim Uygulamaları',")
    out.append("    shortCode: 'MBU',")
    out.append("    description: 'Günlük Hayat, Sağlık, Sanat, Doğa ve Mesleklerde STEM ve Modelleme Becerileri',")
    out.append("    icon: Icons.biotech_rounded,")
    out.append("    primaryColor: const Color(0xFF0D9488),")
    out.append("    accentColor: const Color(0xFF14B8A6),")
    out.append("    grades: {")

    for grade in [5, 6, 7, 8]:
        out.append(f"      {grade}: GradeCurriculum(")
        out.append(f"        grade: {grade},")
        out.append(f"        title: '{grade}. Sınıf',")
        out.append(f"        subtitle: 'Türkiye Yüzyılı Maarif Modeli (5 Tema - STEM & Modelleme)',")
        out.append(f"        badgeText: 'Maarif Modeli ✨',")
        out.append("        weeks: [")

        for idx, (d_range, sy, sm, sd, ey, em, ed, w_num, term) in enumerate(dates):
            theme, subtheme = themes[idx]
            is_holiday = "Tatil" in subtheme
            code = f"MBU.{grade}.{((idx % 7) + 1)}"
            title = f"{subtheme} Uygulamaları"
            desc = f"{theme} teması çerçevesinde {subtheme.lower()} konusunu matematiksel ve bilimsel modelleme araçlarıyla inceler."

            out.append("          CurriculumWeek(")
            out.append(f"            weekNumber: {w_num},")
            out.append(f"            term: {term},")
            out.append(f"            dateRange: '{d_range}',")
            out.append(f"            startDate: DateTime({sy}, {sm}, {sd}),")
            out.append(f"            endDate: DateTime({ey}, {em}, {ed}),")
            out.append(f"            theme: '{theme}',")
            out.append(f"            subTheme: '{subtheme}',")
            out.append(f"            weeklyGoal: '{subtheme} kapsamında araştırma, modelleme ve deney yapma',")
            out.append("            evaluationActivity: 'Etkinlik föyü, grup çalışması değerlendirme ölçeği ve gözlem formu',")
            out.append(f"            isHoliday: {'true' if is_holiday else 'false'},")
            out.append("            outcomes: [")
            out.append("              LearningOutcome(")
            out.append(f"                code: '{code}',")
            out.append(f"                title: '{title}',")
            out.append(f"                description: '{desc}',")
            out.append(f"                processComponents: [")
            out.append(f"                  'a) {subtheme} ile ilgili günlük yaşam verilerini toplar ve düzenler.',")
            out.append(f"                  'b) Matematiksel ve bilimsel modeller kurarak problem durumunu çözer.',")
            out.append(f"                  'c) Elde ettiği bulguları raporlar, sunar ve arkadaşlarıyla tartışır.',")
            out.append("                ],")
            out.append("                keyConcepts: ['Modelleme', 'Veri Analizi', 'STEM', 'Bilimsel Süreç'],")
            out.append("                skills: ['Problem Çözme', 'Eleştirel Düşünme', 'Matematiksel Muhakeme', 'Bilimsel Araştırma'],")
            out.append("                pedagogicalNote: 'Öğrencilerin yaparak-yaşayarak öğrenmeleri için somut materyaller ve teknolojik araçlar kullanılır.',")
            out.append("                exampleProblem: ExampleProblem(")
            out.append("                  context: 'Matematik ve Bilim Uygulamaları Atölyesi',")
            out.append(f"                  question: '{subtheme} konusunda karşılaşılan problemin matematiksel modeli nasıl kurulur?',")
            out.append("                  solution: 'Veriler tabloya dökülür, değişkenler belirlenir ve orantı/formül ile sonuca ulaşılır.',")
            out.append("                ),")
            out.append("              ),")
            out.append("            ],")
            out.append("          ),")

        out.append("        ],")
        out.append("      ),")

    out.append("    },")
    out.append("  );")
    out.append("}")

    content = "\n".join(out)
    with open("lib/data/subjects/matematik_bilim_data.dart", "w", encoding="utf-8") as f:
        f.write(content)
    print("matematik_bilim_data.dart generated successfully!")

create_matematik_bilim_data()
