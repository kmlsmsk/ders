import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/lesson_entry.dart';
import '../models/time_slot.dart';

class TimetableService {
  static const String _lessonsKey = 'mufredatvar_lessons';
  static const String _slotsKey = 'mufredatvar_slots';

  static final ValueNotifier<List<LessonEntry>> lessonsNotifier =
      ValueNotifier<List<LessonEntry>>([]);
  static final ValueNotifier<List<TimeSlot>> slotsNotifier =
      ValueNotifier<List<TimeSlot>>([]);

  static List<LessonEntry> get currentLessons => lessonsNotifier.value;
  static List<TimeSlot> get currentSlots => slotsNotifier.value;

  static Future<void> init() async {
    try {
      final prefs = await SharedPreferences.getInstance();

      // Slots
      final slotsJson = prefs.getString(_slotsKey);
      if (slotsJson != null) {
        final List list = jsonDecode(slotsJson);
        slotsNotifier.value =
            list.map((e) => TimeSlot.fromJson(e as Map<String, dynamic>)).toList();
      } else {
        slotsNotifier.value = TimeSlot.defaultStandardSlots();
        await saveTimeSlots(slotsNotifier.value);
      }

      // Lessons
      final lessonsJson = prefs.getString(_lessonsKey);
      if (lessonsJson != null) {
        final List list = jsonDecode(lessonsJson);
        lessonsNotifier.value =
            list.map((e) => LessonEntry.fromJson(e as Map<String, dynamic>)).toList();
      } else {
        // Seed initial default timetable for teacher
        lessonsNotifier.value = _defaultSeedLessons();
        await _saveLessonsToStorage(lessonsNotifier.value);
      }
    } catch (e) {
      if (kDebugMode) {
        print('Error loading timetable data: $e');
      }
      slotsNotifier.value = TimeSlot.defaultStandardSlots();
      lessonsNotifier.value = _defaultSeedLessons();
    }
  }

  static Future<void> saveTimeSlots(List<TimeSlot> slots) async {
    slotsNotifier.value = slots;
    try {
      final prefs = await SharedPreferences.getInstance();
      final str = jsonEncode(slots.map((e) => e.toJson()).toList());
      await prefs.setString(_slotsKey, str);
    } catch (e) {
      if (kDebugMode) print('Error saving time slots: $e');
    }
  }

  static Future<void> saveLesson(LessonEntry lesson) async {
    final list = List<LessonEntry>.from(lessonsNotifier.value);
    final idx = list.indexWhere((e) => e.id == lesson.id);
    if (idx >= 0) {
      list[idx] = lesson;
    } else {
      list.add(lesson);
    }
    lessonsNotifier.value = list;
    await _saveLessonsToStorage(list);
  }

  static Future<void> deleteLesson(String id) async {
    final list = lessonsNotifier.value.where((e) => e.id != id).toList();
    lessonsNotifier.value = list;
    await _saveLessonsToStorage(list);
  }

  static Future<void> _saveLessonsToStorage(List<LessonEntry> list) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final str = jsonEncode(list.map((e) => e.toJson()).toList());
      await prefs.setString(_lessonsKey, str);
    } catch (e) {
      if (kDebugMode) print('Error saving lessons: $e');
    }
  }

  static List<LessonEntry> _defaultSeedLessons() {
    return [
      // Pazartesi (1)
      const LessonEntry(
        id: 'seed-1',
        dayOfWeek: 1,
        periodIndex: 1,
        subjectId: 'matematik',
        subject: 'Matematik',
        grade: 6,
        className: '6-A',
        classroom: '201',
        colorValue: 0xFF2563EB,
      ),
      const LessonEntry(
        id: 'seed-2',
        dayOfWeek: 1,
        periodIndex: 2,
        subjectId: 'matematik',
        subject: 'Matematik',
        grade: 6,
        className: '6-A',
        classroom: '201',
        colorValue: 0xFF2563EB,
      ),
      const LessonEntry(
        id: 'seed-3',
        dayOfWeek: 1,
        periodIndex: 4,
        subjectId: 'matematik',
        subject: 'Matematik',
        grade: 7,
        className: '7-B',
        classroom: '204',
        colorValue: 0xFF4F46E5,
      ),
      const LessonEntry(
        id: 'seed-4',
        dayOfWeek: 1,
        periodIndex: 5,
        subjectId: 'matematik_bilim',
        subject: 'Matematik ve Bilim Uygulamaları',
        grade: 7,
        className: '7-A',
        classroom: 'Fen Lab',
        colorValue: 0xFF0D9488,
      ),

      // Salı (2)
      const LessonEntry(
        id: 'seed-5',
        dayOfWeek: 2,
        periodIndex: 2,
        subjectId: 'matematik',
        subject: 'Matematik',
        grade: 7,
        className: '7-B',
        classroom: '204',
        colorValue: 0xFF4F46E5,
      ),
      const LessonEntry(
        id: 'seed-6',
        dayOfWeek: 2,
        periodIndex: 3,
        subjectId: 'matematik',
        subject: 'Matematik',
        grade: 7,
        className: '7-B',
        classroom: '204',
        colorValue: 0xFF4F46E5,
      ),
      const LessonEntry(
        id: 'seed-7',
        dayOfWeek: 2,
        periodIndex: 6,
        subjectId: 'matematik',
        subject: 'Matematik',
        grade: 6,
        className: '6-A',
        classroom: '201',
        colorValue: 0xFF2563EB,
      ),

      // Çarşamba (3)
      const LessonEntry(
        id: 'seed-8',
        dayOfWeek: 3,
        periodIndex: 1,
        subjectId: 'matematik_bilim',
        subject: 'Matematik ve Bilim Uygulamaları',
        grade: 7,
        className: '7-A',
        classroom: 'Fen Lab',
        colorValue: 0xFF0D9488,
      ),
      const LessonEntry(
        id: 'seed-9',
        dayOfWeek: 3,
        periodIndex: 3,
        subjectId: 'matematik',
        subject: 'Matematik',
        grade: 6,
        className: '6-A',
        classroom: '201',
        colorValue: 0xFF2563EB,
      ),
      const LessonEntry(
        id: 'seed-10',
        dayOfWeek: 3,
        periodIndex: 5,
        subjectId: 'matematik',
        subject: 'Matematik',
        grade: 7,
        className: '7-B',
        classroom: '204',
        colorValue: 0xFF4F46E5,
      ),

      // Perşembe (4)
      const LessonEntry(
        id: 'seed-11',
        dayOfWeek: 4,
        periodIndex: 2,
        subjectId: 'matematik',
        subject: 'Matematik',
        grade: 7,
        className: '7-B',
        classroom: '204',
        colorValue: 0xFF4F46E5,
      ),
      const LessonEntry(
        id: 'seed-12',
        dayOfWeek: 4,
        periodIndex: 4,
        subjectId: 'matematik',
        subject: 'Matematik',
        grade: 6,
        className: '6-A',
        classroom: '201',
        colorValue: 0xFF2563EB,
      ),

      // Cuma (5)
      const LessonEntry(
        id: 'seed-13',
        dayOfWeek: 5,
        periodIndex: 1,
        subjectId: 'matematik',
        subject: 'Matematik',
        grade: 6,
        className: '6-A',
        classroom: '201',
        colorValue: 0xFF2563EB,
      ),
      const LessonEntry(
        id: 'seed-14',
        dayOfWeek: 5,
        periodIndex: 3,
        subjectId: 'matematik',
        subject: 'Matematik',
        grade: 7,
        className: '7-B',
        classroom: '204',
        colorValue: 0xFF4F46E5,
      ),
    ];
  }
}
