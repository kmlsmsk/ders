import 'package:flutter/material.dart';

class TeacherAssignment {
  final String id;
  final String subjectId;
  final int grade; // 5, 6, 7, 8
  final String branch; // örn: "A", "B", "C" veya boş
  final String customTitle; // opsiyonel özel başlık

  const TeacherAssignment({
    required this.id,
    required this.subjectId,
    required this.grade,
    this.branch = '',
    this.customTitle = '',
  });

  String get displayName {
    if (customTitle.isNotEmpty) return customTitle;
    final branchText = branch.isNotEmpty ? '-$branch' : '';
    return '$grade$branchText. Sınıf';
  }

  String get fullTitle {
    final branchText = branch.isNotEmpty ? '-$branch' : '';
    return '$grade$branchText. Sınıf ${_getSubjectName(subjectId)}';
  }

  static String _getSubjectName(String id) {
    switch (id) {
      case 'matematik':
        return 'Matematik';
      case 'matematik_bilim':
        return 'Matematik ve Bilim Uygulamaları';
      case 'turkce':
        return 'Türkçe';
      case 'fen':
        return 'Fen Bilimleri';
      case 'sosyal':
        return 'Sosyal Bilgiler';
      case 'ingilizce':
        return 'İngilizce';
      case 'din':
        return 'Din Kültürü ve Ahlak Bilgisi';
      case 'bilisim':
        return 'Bilişim Teknolojileri';
      default:
        return id;
    }
  }

  Map<String, dynamic> toJson() => {
        'id': id,
        'subjectId': subjectId,
        'grade': grade,
        'branch': branch,
        'customTitle': customTitle,
      };

  factory TeacherAssignment.fromJson(Map<String, dynamic> json) =>
      TeacherAssignment(
        id: json['id'] as String? ?? UniqueKey().toString(),
        subjectId: json['subjectId'] as String? ?? 'matematik',
        grade: json['grade'] as int? ?? 7,
        branch: json['branch'] as String? ?? '',
        customTitle: json['customTitle'] as String? ?? '',
      );

  TeacherAssignment copyWith({
    String? id,
    String? subjectId,
    int? grade,
    String? branch,
    String? customTitle,
  }) =>
      TeacherAssignment(
        id: id ?? this.id,
        subjectId: subjectId ?? this.subjectId,
        grade: grade ?? this.grade,
        branch: branch ?? this.branch,
        customTitle: customTitle ?? this.customTitle,
      );
}
