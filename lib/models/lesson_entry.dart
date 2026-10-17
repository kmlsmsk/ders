import 'package:flutter/material.dart';

class LessonEntry {
  final String id;
  final int dayOfWeek; // 1 = Pazartesi, ..., 7 = Pazar
  final int periodIndex; // 1, 2, 3...
  final String subjectId; // 'matematik', 'matematik_bilim', 'turkce', vb.
  final String subject; // Ders adı
  final int grade; // 5, 6, 7, 8
  final String className; // örn: 7-A, 6-B
  final String classroom; // örn: 204 Nolu Derslik
  final int colorValue; // Renk
  final String notes; // Notlar
  final bool isExam; // Sınav mı?

  const LessonEntry({
    required this.id,
    required this.dayOfWeek,
    required this.periodIndex,
    required this.subjectId,
    required this.subject,
    required this.grade,
    this.className = '',
    this.classroom = '',
    this.colorValue = 0xFF4F46E5,
    this.notes = '',
    this.isExam = false,
  });

  Color get color => Color(colorValue);

  Map<String, dynamic> toJson() => {
        'id': id,
        'dayOfWeek': dayOfWeek,
        'periodIndex': periodIndex,
        'subjectId': subjectId,
        'subject': subject,
        'grade': grade,
        'className': className,
        'classroom': classroom,
        'colorValue': colorValue,
        'notes': notes,
        'isExam': isExam,
      };

  factory LessonEntry.fromJson(Map<String, dynamic> json) => LessonEntry(
        id: json['id'] as String,
        dayOfWeek: json['dayOfWeek'] as int,
        periodIndex: json['periodIndex'] as int,
        subjectId: json['subjectId'] as String? ?? 'matematik',
        subject: json['subject'] as String? ?? 'Matematik',
        grade: json['grade'] as int? ?? 7,
        className: json['className'] as String? ?? '',
        classroom: json['classroom'] as String? ?? '',
        colorValue: json['colorValue'] as int? ?? 0xFF4F46E5,
        notes: json['notes'] as String? ?? '',
        isExam: json['isExam'] as bool? ?? false,
      );

  LessonEntry copyWith({
    String? id,
    int? dayOfWeek,
    int? periodIndex,
    String? subjectId,
    String? subject,
    int? grade,
    String? className,
    String? classroom,
    int? colorValue,
    String? notes,
    bool? isExam,
  }) =>
      LessonEntry(
        id: id ?? this.id,
        dayOfWeek: dayOfWeek ?? this.dayOfWeek,
        periodIndex: periodIndex ?? this.periodIndex,
        subjectId: subjectId ?? this.subjectId,
        subject: subject ?? this.subject,
        grade: grade ?? this.grade,
        className: className ?? this.className,
        classroom: classroom ?? this.classroom,
        colorValue: colorValue ?? this.colorValue,
        notes: notes ?? this.notes,
        isExam: isExam ?? this.isExam,
      );
}
