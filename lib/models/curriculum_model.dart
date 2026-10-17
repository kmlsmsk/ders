import 'package:flutter/material.dart';

class LearningOutcome {
  final String code; // örn: MAT.7.1.3, TÜR.7.1.2, FEN.7.2.1
  final String title;
  final String description;
  final List<String> processComponents; // Süreç bileşenleri (a, b, c...)
  final List<String> keyConcepts; // Anahtar kavramlar
  final List<String> skills; // Alan ve kavramsal beceriler
  final String pedagogicalNote; // Öğretim ve süreç odaklı değerlendirme notu
  final ExampleProblem? exampleProblem;

  const LearningOutcome({
    required this.code,
    required this.title,
    required this.description,
    required this.processComponents,
    required this.keyConcepts,
    required this.skills,
    required this.pedagogicalNote,
    this.exampleProblem,
  });

  Map<String, dynamic> toJson() => {
    'code': code,
    'title': title,
    'description': description,
    'processComponents': processComponents,
    'keyConcepts': keyConcepts,
    'skills': skills,
    'pedagogicalNote': pedagogicalNote,
    'exampleProblem': exampleProblem?.toJson(),
  };
}

class ExampleProblem {
  final String question;
  final String solution;
  final String context; // Gerçek yaşam bağlamı

  const ExampleProblem({
    required this.question,
    required this.solution,
    required this.context,
  });

  Map<String, dynamic> toJson() => {
    'question': question,
    'solution': solution,
    'context': context,
  };
}

class CurriculumWeek {
  final int weekNumber; // 1 - 36
  final int term; // 1: 1. Dönem, 2: 2. Dönem
  final String dateRange; // örn: "13 - 17 Ekim"
  final DateTime startDate;
  final DateTime endDate;
  final String theme; // Tema adı (örn: Sayılar ve Nicelikler)
  final String subTheme; // Alt öğrenme alanı
  final List<LearningOutcome> outcomes;
  final String weeklyGoal;
  final String evaluationActivity; // Süreç değerlendirme etkinliği
  final bool isHoliday; // Ara tatil / Sömestr durumu

  const CurriculumWeek({
    required this.weekNumber,
    required this.term,
    required this.dateRange,
    required this.startDate,
    required this.endDate,
    required this.theme,
    required this.subTheme,
    required this.outcomes,
    required this.weeklyGoal,
    required this.evaluationActivity,
    this.isHoliday = false,
  });

  bool isCurrentWeek(DateTime date) {
    final start = DateTime(startDate.year, startDate.month, startDate.day);
    final end = DateTime(endDate.year, endDate.month, endDate.day, 23, 59, 59);
    return date.isAfter(start.subtract(const Duration(seconds: 1))) &&
           date.isBefore(end.add(const Duration(seconds: 1)));
  }

  /// Format ready to be written to official Class Registry (Sınıf Defteri)
  String get classRegistryText {
    final outcome = outcomes.isNotEmpty ? outcomes.first : null;
    if (outcome == null) return '$theme: $subTheme';
    return '${outcome.code} - ${outcome.title}\nKonu: $subTheme\nEtkinlik: $evaluationActivity';
  }

  /// Compact one-line text for quick clipboard copying
  String get quickCopyText {
    final outcome = outcomes.isNotEmpty ? outcomes.first : null;
    if (outcome == null) return '$theme: $weeklyGoal';
    return '${outcome.code}: ${outcome.title}';
  }
}

class GradeCurriculum {
  final int grade; // 5, 6, 7, 8
  final String title; // "5. Sınıf", "6. Sınıf", etc.
  final String subtitle;
  final String badgeText;
  final List<CurriculumWeek> weeks;

  const GradeCurriculum({
    required this.grade,
    required this.title,
    required this.subtitle,
    required this.badgeText,
    required this.weeks,
  });

  bool get isMaarifModel => true;

  List<String> get allThemes {
    final set = <String>{};
    for (final w in weeks) {
      if (w.theme.isNotEmpty) set.add(w.theme);
    }
    return set.toList();
  }

  CurriculumWeek getCurrentWeek([DateTime? date]) {
    final now = date ?? DateTime.now();
    for (final week in weeks) {
      if (week.isCurrentWeek(now)) {
        return week;
      }
    }
    // Mid-October anchor (10-20 Ekim) -> 6. Hafta
    if (now.month == 10 && now.day >= 10 && now.day <= 20) {
      final week6 = weeks.firstWhere((w) => w.weekNumber == 6, orElse: () => weeks.first);
      return week6;
    }
    // Find closest week by date
    final sorted = List<CurriculumWeek>.from(weeks);
    sorted.sort((a, b) => (a.startDate.difference(now).abs()).compareTo(b.startDate.difference(now).abs()));
    return sorted.isNotEmpty ? sorted.first : weeks.first;
  }
}

class SubjectCurriculum {
  final String id; // 'matematik', 'turkce', 'fen', 'sosyal', 'ingilizce', 'din', 'bilisim'
  final String name; // 'Matematik', 'Türkçe', vb.
  final String shortCode; // 'MAT', 'TÜR', 'FEN', 'SOS', 'İNG', 'DİN', 'BİL'
  final String description;
  final IconData icon;
  final Color primaryColor;
  final Color accentColor;
  final Map<int, GradeCurriculum> grades;

  const SubjectCurriculum({
    required this.id,
    required this.name,
    required this.shortCode,
    required this.description,
    required this.icon,
    required this.primaryColor,
    required this.accentColor,
    required this.grades,
  });

  GradeCurriculum getGrade(int gradeNumber) {
    return grades[gradeNumber] ?? grades.values.first;
  }

  List<int> get availableGrades => grades.keys.toList()..sort();
}
