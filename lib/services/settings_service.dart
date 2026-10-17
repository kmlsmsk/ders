import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/app_settings.dart';
import '../models/teacher_assignment.dart';

class SettingsService {
  static const String _prefsKey = 'mufredatvar_app_settings';

  static final ValueNotifier<AppSettings> settingsNotifier =
      ValueNotifier<AppSettings>(const AppSettings());

  static AppSettings get currentSettings => settingsNotifier.value;

  /// Load settings from SharedPreferences
  static Future<void> init() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final jsonString = prefs.getString(_prefsKey);
      if (jsonString != null) {
        final Map<String, dynamic> map = jsonDecode(jsonString);
        settingsNotifier.value = AppSettings.fromJson(map);
      }
    } catch (e) {
      if (kDebugMode) {
        print('Error loading settings: $e');
      }
    }
  }

  /// Update and save settings
  static Future<void> updateSettings(AppSettings newSettings) async {
    settingsNotifier.value = newSettings;
    try {
      final prefs = await SharedPreferences.getInstance();
      final jsonString = jsonEncode(newSettings.toJson());
      await prefs.setString(_prefsKey, jsonString);
    } catch (e) {
      if (kDebugMode) {
        print('Error saving settings: $e');
      }
    }
  }

  /// Convenience updates
  static Future<void> updateTeacherProfile({
    required String teacherName,
    required String schoolName,
    required String teacherTitle,
  }) async {
    final updated = currentSettings.copyWith(
      teacherName: teacherName,
      schoolName: schoolName,
      teacherTitle: teacherTitle,
    );
    await updateSettings(updated);
  }

  static Future<void> updateActiveSubjectAndGrade({
    String? subjectId,
    int? grade,
  }) async {
    final updated = currentSettings.copyWith(
      activeSubjectId: subjectId,
      activeGrade: grade,
    );
    await updateSettings(updated);
  }

  static Future<void> updateAssignedClasses(List<TeacherAssignment> classes) async {
    final updated = currentSettings.copyWith(assignedClasses: classes);
    await updateSettings(updated);
  }

  static Future<void> addClassAssignment(TeacherAssignment assignment) async {
    final list = List<TeacherAssignment>.from(currentSettings.assignedClasses);
    list.add(assignment);
    await updateAssignedClasses(list);
  }

  static Future<void> removeClassAssignment(String id) async {
    final list = currentSettings.assignedClasses.where((e) => e.id != id).toList();
    await updateAssignedClasses(list);
  }
}
