import 'package:flutter/foundation.dart';
import 'package:home_widget/home_widget.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/curriculum_model.dart';
import 'settings_service.dart';

class WidgetSyncService {
  static const String appWidgetProviderName = 'MufredatWidgetProvider';
  static const String qualifiedAndroidName = 'com.mufredatvar.MufredatWidgetProvider';

  /// Syncs the given week, grade, subject, and teacher to the Android Home Screen App Widget
  static Future<bool> syncWeekToWidget({
    String? teacherName,
    required String gradeTitle,
    required CurriculumWeek week,
    LearningOutcome? selectedOutcome,
  }) async {
    try {
      final tName = teacherName ?? SettingsService.currentSettings.teacherName;
      final outcome = selectedOutcome ?? week.outcomes.first;
      final weekInfo = '${week.weekNumber}. Hafta • ${week.dateRange}';
      final themeName = 'Tema: ${week.theme}';
      final outcomeCode = outcome.code;
      final outcomeDesc = outcome.title;
      final subtopic = outcome.description;

      // Save data for Android Widget RemoteViews
      await HomeWidget.saveWidgetData<String>('teacher_name', tName.toUpperCase());
      await HomeWidget.saveWidgetData<String>('grade_title', gradeTitle.toUpperCase());
      await HomeWidget.saveWidgetData<String>('week_info', weekInfo);
      await HomeWidget.saveWidgetData<String>('theme_name', themeName);
      await HomeWidget.saveWidgetData<String>('outcome_code', outcomeCode);
      await HomeWidget.saveWidgetData<String>('outcome_desc', outcomeDesc);
      await HomeWidget.saveWidgetData<String>('subtopic', subtopic);

      // Trigger Widget update with qualified name
      await HomeWidget.updateWidget(
        name: appWidgetProviderName,
        androidName: appWidgetProviderName,
        qualifiedAndroidName: qualifiedAndroidName,
      );

      // Save preference
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString('last_synced_grade', gradeTitle);
      await prefs.setInt('last_synced_week', week.weekNumber);
      await prefs.setString('last_synced_time', DateTime.now().toIso8601String());

      if (kDebugMode) {
        print('Widget successfully updated: $tName | $gradeTitle | $weekInfo | $outcomeCode - $outcomeDesc');
      }
      return true;
    } catch (e) {
      if (kDebugMode) {
        print('Widget update error: $e');
      }
      return false;
    }
  }

  /// Request launcher to pin widget to home screen (Android 8.0+)
  static Future<bool> pinWidgetToHomeScreen() async {
    try {
      final isSupported = await HomeWidget.isRequestPinWidgetSupported();
      if (isSupported == true) {
        await HomeWidget.requestPinWidget(
          name: appWidgetProviderName,
          androidName: appWidgetProviderName,
          qualifiedAndroidName: qualifiedAndroidName,
        );
        return true;
      }
      return false;
    } catch (e) {
      if (kDebugMode) {
        print('Widget pin error: $e');
      }
      return false;
    }
  }

  /// Get last synced week number
  static Future<int?> getLastSyncedWeek() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      return prefs.getInt('last_synced_week');
    } catch (_) {
      return null;
    }
  }

  /// Get last synced grade name
  static Future<String?> getLastSyncedGrade() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      return prefs.getString('last_synced_grade');
    } catch (_) {
      return null;
    }
  }
}
