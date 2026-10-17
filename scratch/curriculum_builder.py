# -*- coding: utf-8 -*-
"""
Full Middle School Curriculum Generator for MufredatVar
Covers all 36 weeks for:
- Fen Bilimleri (5. Sınıf Maarif Modeli, 6. Sınıf, 7. Sınıf, 8. Sınıf LGS)
- Türkçe (5. Sınıf Maarif Modeli, 6. Sınıf, 7. Sınıf, 8. Sınıf LGS)
- Sosyal Bilgiler & T.C. İnkılap Tarihi (5. Sınıf Maarif Modeli, 6. Sınıf, 7. Sınıf, 8. Sınıf LGS)
- Din Kültürü ve Ahlak Bilgisi (5. Sınıf Maarif Modeli, 6, 7, 8)
- İngilizce (5, 6, 7, 8)
- Bilişim Teknolojileri ve Yazılım (5, 6)
"""

import sys

DATES = [
    ('08 - 12 Eylül', 2026, 9, 8, 2026, 9, 12),
    ('15 - 19 Eylül', 2026, 9, 15, 2026, 9, 19),
    ('22 - 26 Eylül', 2026, 9, 22, 2026, 9, 26),
    ('29 Eylül - 03 Ekim', 2026, 9, 29, 2026, 10, 3),
    ('06 - 10 Ekim', 2026, 10, 6, 2026, 10, 10),
    ('13 - 17 Ekim', 2026, 10, 13, 2026, 10, 17),
    ('20 - 24 Ekim', 2026, 10, 20, 2026, 10, 24),
    ('27 - 31 Ekim', 2026, 10, 27, 2026, 10, 31),
    ('03 - 07 Kasım', 2026, 11, 3, 2026, 11, 7),
    ('10 - 14 Kasım', 2026, 11, 10, 2026, 11, 14), # 1. Ara Tatil
    ('17 - 21 Kasım', 2026, 11, 17, 2026, 11, 21),
    ('24 - 28 Kasım', 2026, 11, 24, 2026, 11, 28),
    ('01 - 05 Aralık', 2026, 12, 1, 2026, 12, 5),
    ('08 - 12 Aralık', 2026, 12, 8, 2026, 12, 12),
    ('15 - 19 Aralık', 2026, 12, 15, 2026, 12, 19),
    ('22 - 26 Aralık', 2026, 12, 22, 2026, 12, 26),
    ('29 Aralık - 02 Ocak', 2026, 12, 29, 2027, 1, 2),
    ('05 - 09 Ocak', 2027, 1, 5, 2027, 1, 9),
    ('12 - 16 Ocak', 2027, 1, 12, 2027, 1, 16), # 1. Dönem Sonu
    ('02 - 06 Şubat', 2027, 2, 2, 2027, 2, 6), # 2. Dönem Başı
    ('09 - 13 Şubat', 2027, 2, 9, 2027, 2, 13),
    ('16 - 20 Şubat', 2027, 2, 16, 2027, 2, 20),
    ('23 - 27 Şubat', 2027, 2, 23, 2027, 2, 27),
    ('02 - 06 Mart', 2027, 3, 2, 2027, 3, 6),
    ('09 - 13 Mart', 2027, 3, 9, 2027, 3, 13),
    ('16 - 20 Mart', 2027, 3, 16, 2027, 3, 20),
    ('23 - 27 Mart', 2027, 3, 23, 2027, 3, 27),
    ('30 Mart - 03 Nisan', 2027, 3, 30, 2027, 4, 3), # 2. Ara Tatil
    ('06 - 10 Nisan', 2027, 4, 6, 2027, 4, 10),
    ('13 - 17 Nisan', 2027, 4, 13, 2027, 4, 17),
    ('20 - 24 Nisan', 2027, 4, 20, 2027, 4, 24),
    ('27 Nisan - 01 Mayıs', 2027, 4, 27, 2027, 5, 1),
    ('04 - 08 Mayıs', 2027, 5, 4, 2027, 5, 8),
    ('11 - 15 Mayıs', 2027, 5, 11, 2027, 5, 15),
    ('18 - 22 Mayıs', 2027, 5, 18, 2027, 5, 22),
    ('25 - 29 Mayıs', 2027, 5, 25, 2027, 5, 29),
]

def q(s):
    if s is None:
        return 'null'
    escaped = str(s).replace('\\', '\\\\').replace("'", "\\'").replace('$', '\\$')
    return f"'{escaped}'"

def ql(lst):
    return '[' + ', '.join(q(x) for x in lst) + ']'

def generate_dart_file(subject_id, subject_name, short_code, description, icon_name, primary_hex, accent_hex, grades_data, output_path):
    lines = []
    lines.append("// GENERATED DATA - DO NOT EDIT MANUALLY")
    lines.append("import 'package:flutter/material.dart';")
    lines.append("import '../../models/curriculum_model.dart';")
    lines.append("")
    class_name = f"{subject_id.capitalize()}Curriculum"
    if subject_id == 'fen':
        class_name = 'FenBilimleriCurriculum'
    elif subject_id == 'sosyal':
        class_name = 'SosyalBilgilerCurriculum'
    elif subject_id == 'din':
        class_name = 'DinKulturuCurriculum'
    elif subject_id == 'bilisim':
        class_name = 'BilisimCurriculum'
    elif subject_id == 'ingilizce':
        class_name = 'IngilizceCurriculum'
    elif subject_id == 'turkce':
        class_name = 'TurkceCurriculum'

    lines.append(f"class {class_name} {{")
    lines.append("  static final SubjectCurriculum subject = SubjectCurriculum(")
    lines.append(f"    id: '{subject_id}',")
    lines.append(f"    name: '{subject_name}',")
    lines.append(f"    shortCode: '{short_code}',")
    lines.append(f"    description: '{description}',")
    lines.append(f"    icon: Icons.{icon_name},")
    lines.append(f"    primaryColor: const Color({primary_hex}),")
    lines.append(f"    accentColor: const Color({accent_hex}),")
    lines.append("    grades: {")

    for grade, gdata in grades_data.items():
        title = gdata['title']
        subtitle = gdata['subtitle']
        badge = gdata['badge']
        weeks = gdata['weeks']
        lines.append(f"      {grade}: GradeCurriculum(")
        lines.append(f"        grade: {grade},")
        lines.append(f"        title: {q(title)},")
        lines.append(f"        subtitle: {q(subtitle)},")
        lines.append(f"        badgeText: {q(badge)},")
        lines.append("        weeks: [")

        for i, w in enumerate(weeks):
            wnum = i + 1
            date_range, sy, sm, sd, ey, em, ed = DATES[i]
            term = 1 if wnum <= 19 else 2
            is_hol = (wnum in [10, 20, 28])
            lines.append("          CurriculumWeek(")
            lines.append(f"            weekNumber: {wnum},")
            lines.append(f"            term: {term},")
            lines.append(f"            dateRange: {q(date_range)},")
            lines.append(f"            startDate: DateTime({sy}, {sm}, {sd}),")
            lines.append(f"            endDate: DateTime({ey}, {em}, {ed}),")
            lines.append(f"            theme: {q(w['theme'])},")
            lines.append(f"            subTheme: {q(w['subTheme'])},")
            lines.append(f"            weeklyGoal: {q(w['weeklyGoal'])},")
            lines.append(f"            evaluationActivity: {q(w['evaluation'])},")
            lines.append(f"            isHoliday: {'true' if is_hol else 'false'},")
            lines.append("            outcomes: [")
            lines.append("              LearningOutcome(")
            lines.append(f"                code: {q(w['code'])},")
            lines.append(f"                title: {q(w['title'])},")
            lines.append(f"                description: {q(w['description'])},")
            lines.append(f"                processComponents: {ql(w['process'])},")
            lines.append(f"                keyConcepts: {ql(w['concepts'])},")
            lines.append(f"                skills: {ql(w.get('skills', ['Bilimsel Düşünme', 'Akıl Yürütme', 'Problem Çözme']))},")
            lines.append(f"                pedagogicalNote: {q(w['pedagogical'])},")
            lines.append("                exampleProblem: ExampleProblem(")
            lines.append(f"                  context: {q(w['context'])},")
            lines.append(f"                  question: {q(w['question'])},")
            lines.append(f"                  solution: {q(w['solution'])},")
            lines.append("                ),")
            lines.append("              ),")
            lines.append("            ],")
            lines.append("          ),")

        lines.append("        ],")
        lines.append("      ),")

    lines.append("    },")
    lines.append("  );")
    lines.append("}")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f"Generated {output_path} successfully!")

print("Generator framework ready.")
