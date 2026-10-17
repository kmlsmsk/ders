import 'package:flutter/material.dart';
import '../../models/curriculum_model.dart';
import '../grade_5_data.dart';
import '../grade_6_data.dart';
import '../grade_7_data.dart';
import '../grade_8_data.dart';

class MatematikCurriculum {
  static final SubjectCurriculum subject = SubjectCurriculum(
    id: 'matematik',
    name: 'Matematik',
    shortCode: 'MAT',
    description: 'Sayılar, Nicelikler, Cebir, Geometri, Veri Analizi ve Olasılık',
    icon: Icons.functions_rounded,
    primaryColor: const Color(0xFF4F46E5), // Indigo
    accentColor: const Color(0xFF6366F1),
    grades: {
      5: Grade5Data.curriculum,
      6: Grade6Data.curriculum,
      7: Grade7Data.curriculum,
      8: Grade8Data.curriculum,
    },
  );
}
