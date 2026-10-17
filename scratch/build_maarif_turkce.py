import os

def build():
    input_file = r"c:\Users\Kemal ŞİMŞEK\OneDrive\Desktop\MufredatVar\lib\data\subjects\turkce_data.dart"
    
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    cutoff = -1
    for i, line in enumerate(lines):
        if "6: GradeCurriculum(" in line:
            cutoff = i
            break
            
    if cutoff == -1:
        print("Cutoff not found!")
        return
        
    grade5_part = "".join(lines[:cutoff])
    
    # Weeks meta: (week_num, term, date_range, start_y, start_m, start_d, end_y, end_m, end_d, is_holiday)
    weeks_meta = [
        (1, 1, '08 - 12 Eylül', 2026, 9, 8, 2026, 9, 12, False),
        (2, 1, '15 - 19 Eylül', 2026, 9, 15, 2026, 9, 19, False),
        (3, 1, '22 - 26 Eylül', 2026, 9, 22, 2026, 9, 26, False),
        (4, 1, '29 Eylül - 03 Ekim', 2026, 9, 29, 2026, 10, 3, False),
        (5, 1, '06 - 10 Ekim', 2026, 10, 6, 2026, 10, 10, False),
        (6, 1, '13 - 17 Ekim', 2026, 10, 13, 2026, 10, 17, False),
        (7, 1, '20 - 24 Ekim', 2026, 10, 20, 2026, 10, 24, False),
        (8, 1, '27 - 31 Ekim', 2026, 10, 27, 2026, 10, 31, False),
        (9, 1, '03 - 07 Kasım', 2026, 11, 3, 2026, 11, 7, False),
        (10, 1, '10 - 14 Kasım', 2026, 11, 10, 2026, 11, 14, True),
        (11, 1, '17 - 21 Kasım', 2026, 11, 17, 2026, 11, 21, False),
        (12, 1, '24 - 28 Kasım', 2026, 11, 24, 2026, 11, 28, False),
        (13, 1, '01 - 05 Aralık', 2026, 12, 1, 2026, 12, 5, False),
        (14, 1, '08 - 12 Aralık', 2026, 12, 8, 2026, 12, 12, False),
        (15, 1, '15 - 19 Aralık', 2026, 12, 15, 2026, 12, 19, False),
        (16, 1, '22 - 26 Aralık', 2026, 12, 22, 2026, 12, 26, False),
        (17, 1, '29 Aralık - 02 Ocak', 2026, 12, 29, 2027, 1, 2, False),
        (18, 1, '05 - 09 Ocak', 2027, 1, 5, 2027, 1, 9, False),
        (19, 1, '12 - 16 Ocak', 2027, 1, 12, 2027, 1, 16, False),
        (20, 2, '02 - 06 Şubat', 2027, 2, 2, 2027, 2, 6, False),
        (21, 2, '09 - 13 Şubat', 2027, 2, 9, 2027, 2, 13, False),
        (22, 2, '16 - 20 Şubat', 2027, 2, 16, 2027, 2, 20, False),
        (23, 2, '23 - 27 Şubat', 2027, 2, 23, 2027, 2, 27, False),
        (24, 2, '02 - 06 Mart', 2027, 3, 2, 2027, 3, 6, False),
        (25, 2, '09 - 13 Mart', 2027, 3, 9, 2027, 3, 13, False),
        (26, 2, '16 - 20 Mart', 2027, 3, 16, 2027, 3, 20, False),
        (27, 2, '23 - 27 Mart', 2027, 3, 23, 2027, 3, 27, False),
        (28, 2, '30 Mart - 03 Nisan', 2027, 3, 30, 2027, 4, 3, True),
        (29, 2, '06 - 10 Nisan', 2027, 4, 6, 2027, 4, 10, False),
        (30, 2, '13 - 17 Nisan', 2027, 4, 13, 2027, 4, 17, False),
        (31, 2, '20 - 24 Nisan', 2027, 4, 20, 2027, 4, 24, False),
        (32, 2, '27 Nisan - 01 Mayıs', 2027, 4, 27, 2027, 5, 1, False),
        (33, 2, '04 - 08 Mayıs', 2027, 5, 4, 2027, 5, 8, False),
        (34, 2, '11 - 15 Mayıs', 2027, 5, 11, 2027, 5, 15, False),
        (35, 2, '18 - 22 Mayıs', 2027, 5, 18, 2027, 5, 22, False),
        (36, 2, '25 - 29 Mayıs', 2027, 5, 25, 2027, 5, 29, False),
    ]

    def render_grade(grade_num, title, subtitle, badge_text, weeks_data):
        res = []
        res.append(f"      {grade_num}: GradeCurriculum(\n")
        res.append(f"        grade: {grade_num},\n")
        res.append(f"        title: '{title}',\n")
        res.append(f"        subtitle: '{subtitle}',\n")
        res.append(f"        badgeText: '{badge_text}',\n")
        res.append("        weeks: [\n")
        
        for i, meta in enumerate(weeks_meta):
            wn, term, dr, sy, sm, sd, ey, em, ed, is_hol = meta
            w = weeks_data[i]
            theme, sub_theme, weekly_goal, eval_act, code, o_title, desc, proc, concepts, skills, ped_note, ctx, q, sol = w
            
            res.append("          CurriculumWeek(\n")
            res.append(f"            weekNumber: {wn},\n")
            res.append(f"            term: {term},\n")
            res.append(f"            dateRange: '{dr}',\n")
            res.append(f"            startDate: DateTime({sy}, {sm}, {sd}),\n")
            res.append(f"            endDate: DateTime({ey}, {em}, {ed}),\n")
            res.append(f"            theme: '{theme}',\n")
            
            # escape single quotes in strings
            def esc(s):
                return s.replace("'", "\\'")
                
            res.append(f"            subTheme: '{esc(sub_theme)}',\n")
            res.append(f"            weeklyGoal: '{esc(weekly_goal)}',\n")
            res.append(f"            evaluationActivity: '{esc(eval_act)}',\n")
            res.append(f"            isHoliday: {'true' if is_hol else 'false'},\n")
            res.append("            outcomes: [\n")
            res.append("              LearningOutcome(\n")
            res.append(f"                code: '{code}',\n")
            res.append(f"                title: '{esc(o_title)}',\n")
            res.append(f"                description: '{esc(desc)}',\n")
            
            proc_str = ", ".join([f"'{esc(p)}'" for p in proc])
            res.append(f"                processComponents: [{proc_str}],\n")
            
            concepts_str = ", ".join([f"'{esc(c)}'" for c in concepts])
            res.append(f"                keyConcepts: [{concepts_str}],\n")
            
            skills_str = ", ".join([f"'{esc(s)}'" for s in skills])
            res.append(f"                skills: [{skills_str}],\n")
            
            res.append(f"                pedagogicalNote: '{esc(ped_note)}',\n")
            res.append("                exampleProblem: ExampleProblem(\n")
            res.append(f"                  context: '{esc(ctx)}',\n")
            res.append(f"                  question: '{esc(q)}',\n")
            res.append(f"                  solution: '{esc(sol)}',\n")
            res.append("                ),\n")
            res.append("              ),\n")
            res.append("            ],\n")
            res.append("          ),\n")
            
        res.append("        ],\n")
        res.append("      ),\n")
        return "".join(res)

    # Import the actual weeks definitions for grades 6, 7, 8 from separate helper file
    import generate_weeks_data as gwd
    g6 = render_grade(6, '6. Sınıf', 'Türkiye Yüzyılı Maarif Modeli (6 Tema)', 'Maarif Modeli ✨', gwd.get_grade6())
    g7 = render_grade(7, '7. Sınıf', 'Türkiye Yüzyılı Maarif Modeli (6 Tema)', 'Maarif Modeli ✨', gwd.get_grade7())
    g8 = render_grade(8, '8. Sınıf', 'Türkiye Yüzyılı Maarif Modeli & LGS (6 Tema)', 'Maarif Modeli ✨', gwd.get_grade8())

    full_output = grade5_part + g6 + g7 + g8 + "    },\n  );\n}\n"
    
    with open(input_file, "w", encoding="utf-8") as f:
        f.write(full_output)
        
    print(f"Successfully generated turkce_data.dart! Total length: {len(full_output)} chars.")

if __name__ == "__main__":
    build()
