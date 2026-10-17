import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../models/lesson_entry.dart';
import '../models/time_slot.dart';
import '../models/curriculum_model.dart';
import '../services/timetable_service.dart';
import '../data/curriculum_repository.dart';
import '../widgets/lesson_edit_dialog.dart';

class TimetableScreen extends StatefulWidget {
  final Function(String subjectId, int grade, int? targetWeek)? onNavigateToCurriculum;
  final bool isDarkMode;

  const TimetableScreen({
    super.key,
    this.onNavigateToCurriculum,
    required this.isDarkMode,
  });

  @override
  State<TimetableScreen> createState() => _TimetableScreenState();
}

class _TimetableScreenState extends State<TimetableScreen>
    with SingleTickerProviderStateMixin {
  late TabController _dayTabController;
  bool _isGridView = false;

  final List<String> _dayNames = const [
    'Pazartesi',
    'Salı',
    'Çarşamba',
    'Perşembe',
    'Cuma',
  ];

  final List<String> _dayShortNames = const [
    'Pzt',
    'Sal',
    'Çar',
    'Per',
    'Cum',
  ];

  @override
  void initState() {
    super.initState();
    final todayWeekday = DateTime.now().weekday; // 1 = Pazartesi, 7 = Pazar
    final initialIndex = (todayWeekday >= 1 && todayWeekday <= 5) ? (todayWeekday - 1) : 0;
    _dayTabController = TabController(length: 5, vsync: this, initialIndex: initialIndex);
  }

  @override
  void dispose() {
    _dayTabController.dispose();
    super.dispose();
  }

  void _showLessonDetails(LessonEntry lesson, TimeSlot slot) {
    HapticFeedback.lightImpact();
    final subject = CurriculumRepository.getSubject(lesson.subjectId);
    final gradeCurriculum = subject.getGrade(lesson.grade);
    final activeWeek = gradeCurriculum.getCurrentWeek();
    final activeOutcome = activeWeek.outcomes.isNotEmpty ? activeWeek.outcomes.first : null;

    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) {
        final isDark = widget.isDarkMode;
        final theme = Theme.of(context);

        return Container(
          decoration: BoxDecoration(
            color: isDark ? const Color(0xFF1E293B) : Colors.white,
            borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
          ),
          padding: EdgeInsets.only(
            top: 16,
            left: 20,
            right: 20,
            bottom: MediaQuery.of(context).viewInsets.bottom + 24,
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Sürükleme çizgisi
              Center(
                child: Container(
                  width: 40,
                  height: 4,
                  decoration: BoxDecoration(
                    color: Colors.grey.withValues(alpha: 0.3),
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
              ),
              const SizedBox(height: 16),

              // Başlık ve Ders Bilgisi
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: lesson.color.withValues(alpha: 0.15),
                      borderRadius: BorderRadius.circular(16),
                    ),
                    child: Icon(subject.icon, color: lesson.color, size: 28),
                  ),
                  const SizedBox(width: 14),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                              decoration: BoxDecoration(
                                color: lesson.color,
                                borderRadius: BorderRadius.circular(6),
                              ),
                              child: Text(
                                lesson.className.isNotEmpty ? lesson.className : '${lesson.grade}. Sınıf',
                                style: const TextStyle(
                                  color: Colors.white,
                                  fontSize: 11,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                            const SizedBox(width: 6),
                            if (lesson.classroom.isNotEmpty) ...[
                              Container(
                                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                                decoration: BoxDecoration(
                                  color: isDark ? const Color(0xFF334155) : const Color(0xFFF1F5F9),
                                  borderRadius: BorderRadius.circular(6),
                                ),
                                child: Text(
                                  lesson.classroom,
                                  style: const TextStyle(fontSize: 11, fontWeight: FontWeight.w600),
                                ),
                              ),
                            ],
                          ],
                        ),
                        const SizedBox(height: 4),
                        Text(
                          lesson.subject,
                          style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                  ),
                  IconButton(
                    icon: const Icon(Icons.edit_note_rounded),
                    tooltip: 'Dersi Düzenle',
                    onPressed: () {
                      Navigator.pop(context);
                      _editLesson(lesson);
                    },
                  ),
                ],
              ),
              const SizedBox(height: 16),

              // Saat ve Gün Kartı
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                decoration: BoxDecoration(
                  color: isDark ? const Color(0xFF0F172A) : const Color(0xFFF8FAFC),
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(
                    color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
                  ),
                ),
                child: Row(
                  children: [
                    Icon(Icons.schedule_rounded, size: 18, color: Colors.blueAccent),
                    const SizedBox(width: 8),
                    Text(
                      '${_dayNames[lesson.dayOfWeek - 1]} • ${slot.label} (${slot.startTime} - ${slot.endTime})',
                      style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 13),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 16),

              // O HAFTANIN ÖĞRENME ÇIKTISI / KAZANIMI (Tıklanınca doğrudan gitme)
              Container(
                padding: const EdgeInsets.all(14),
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [
                      lesson.color.withValues(alpha: 0.12),
                      lesson.color.withValues(alpha: 0.04),
                    ],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: lesson.color.withValues(alpha: 0.3)),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Icon(Icons.auto_awesome_rounded, size: 16, color: lesson.color),
                        const SizedBox(width: 6),
                        Text(
                          'BU HAFTANIN KAZANIMI (${activeWeek.weekNumber}. Hafta • ${activeWeek.dateRange})',
                          style: TextStyle(
                            fontSize: 11,
                            fontWeight: FontWeight.w800,
                            color: lesson.color,
                            letterSpacing: 0.5,
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 8),
                    if (activeOutcome != null) ...[
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 3),
                            decoration: BoxDecoration(
                              color: lesson.color,
                              borderRadius: BorderRadius.circular(6),
                            ),
                            child: Text(
                              activeOutcome.code,
                              style: const TextStyle(
                                color: Colors.white,
                                fontWeight: FontWeight.bold,
                                fontSize: 11,
                              ),
                            ),
                          ),
                          const SizedBox(width: 8),
                          Expanded(
                            child: Text(
                              activeOutcome.title,
                              style: const TextStyle(
                                fontSize: 14,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 6),
                      Text(
                        activeOutcome.description,
                        style: TextStyle(
                          fontSize: 12,
                          color: isDark ? const Color(0xFFCBD5E1) : const Color(0xFF475569),
                        ),
                        maxLines: 3,
                        overflow: TextOverflow.ellipsis,
                      ),
                    ] else ...[
                      const Text(
                        'Bu hafta için tatil veya serbest etkinlik planlanmıştır.',
                        style: TextStyle(fontSize: 12, color: Colors.grey),
                      ),
                    ],
                  ],
                ),
              ),
              const SizedBox(height: 18),

              // Müfredata Git Butonu
              SizedBox(
                width: double.infinity,
                child: ElevatedButton.icon(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: lesson.color,
                    foregroundColor: Colors.white,
                    padding: const EdgeInsets.symmetric(vertical: 14),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                    elevation: 2,
                  ),
                  icon: const Icon(Icons.menu_book_rounded, size: 20),
                  label: const Text(
                    '🎯 Bu Haftanın Öğrenme Çıktısına Git',
                    style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14),
                  ),
                  onPressed: () {
                    Navigator.pop(context);
                    if (widget.onNavigateToCurriculum != null) {
                      widget.onNavigateToCurriculum!(
                        lesson.subjectId,
                        lesson.grade,
                        activeWeek.weekNumber,
                      );
                    }
                  },
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  Future<void> _addNewLesson({int? day, int? period}) async {
    final slots = TimetableService.currentSlots;
    final result = await showDialog(
      context: context,
      builder: (context) => LessonEditDialog(
        defaultDay: day ?? (_dayTabController.index + 1),
        defaultPeriod: period ?? 1,
        slots: slots,
      ),
    );

    if (result is LessonEntry) {
      await TimetableService.saveLesson(result);
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('${result.className} ${result.subject} dersi eklendi!'),
            backgroundColor: const Color(0xFF059669),
            behavior: SnackBarBehavior.floating,
          ),
        );
      }
    }
  }

  Future<void> _editLesson(LessonEntry lesson) async {
    final slots = TimetableService.currentSlots;
    final result = await showDialog(
      context: context,
      builder: (context) => LessonEditDialog(
        initialLesson: lesson,
        slots: slots,
      ),
    );

    if (result == 'DELETE') {
      await TimetableService.deleteLesson(lesson.id);
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('Ders programdan kaldırıldı.'),
            backgroundColor: Colors.redAccent,
            behavior: SnackBarBehavior.floating,
          ),
        );
      }
    } else if (result is LessonEntry) {
      await TimetableService.saveLesson(result);
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('${result.className} ${result.subject} güncellendi!'),
            backgroundColor: const Color(0xFF059669),
            behavior: SnackBarBehavior.floating,
          ),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final isDark = widget.isDarkMode;

    return ValueListenableBuilder<List<LessonEntry>>(
      valueListenable: TimetableService.lessonsNotifier,
      builder: (context, lessons, _) {
        return ValueListenableBuilder<List<TimeSlot>>(
          valueListenable: TimetableService.slotsNotifier,
          builder: (context, slots, _) {
            return Scaffold(
              appBar: AppBar(
                title: const Row(
                  children: [
                    Icon(Icons.calendar_month_rounded, color: Color(0xFF4F46E5)),
                    SizedBox(width: 8),
                    Text(
                      'Haftalık Ders Programı',
                      style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
                    ),
                  ],
                ),
                actions: [
                  // Görünüm Değiştirici (Günlük / Izgara)
                  IconButton(
                    icon: Icon(
                      _isGridView ? Icons.view_day_rounded : Icons.grid_on_rounded,
                      color: const Color(0xFF4F46E5),
                    ),
                    tooltip: _isGridView ? 'Günlük Görünüm' : 'Haftalık Tablo',
                    onPressed: () {
                      setState(() {
                        _isGridView = !_isGridView;
                      });
                      HapticFeedback.selectionClick();
                    },
                  ),
                  // Yeni Ders Ekle Butonu
                  IconButton(
                    icon: const Icon(Icons.add_circle_rounded, color: Color(0xFF4F46E5), size: 28),
                    tooltip: 'Yeni Ders Ekle',
                    onPressed: () => _addNewLesson(),
                  ),
                  const SizedBox(width: 8),
                ],
                bottom: _isGridView
                    ? null
                    : TabBar(
                        controller: _dayTabController,
                        indicatorColor: const Color(0xFF4F46E5),
                        labelColor: const Color(0xFF4F46E5),
                        unselectedLabelColor: isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B),
                        labelStyle: const TextStyle(fontWeight: FontWeight.bold, fontSize: 13),
                        tabs: List.generate(5, (index) {
                          final isToday = DateTime.now().weekday == (index + 1);
                          return Tab(
                            text: isToday ? '${_dayShortNames[index]} • Bugün' : _dayShortNames[index],
                          );
                        }),
                      ),
              ),
              body: _isGridView
                  ? _buildTimetableGrid(slots, lessons)
                  : _buildDailyTabView(slots, lessons),
            );
          },
        );
      },
    );
  }

  Widget _buildDailyTabView(List<TimeSlot> slots, List<LessonEntry> lessons) {
    return TabBarView(
      controller: _dayTabController,
      children: List.generate(5, (dayIndex) {
        final dayNum = dayIndex + 1;
        final dayLessons = lessons.where((l) => l.dayOfWeek == dayNum).toList();

        if (slots.isEmpty) {
          return const Center(child: Text('Zaman çizelgesi bulunamadı.'));
        }

        return ListView.builder(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
          itemCount: slots.length,
          itemBuilder: (context, slotIndex) {
            final slot = slots[slotIndex];
            final lesson = dayLessons.where((l) => l.periodIndex == slot.periodIndex).firstOrNull;

            return _buildDailyLessonCard(slot, lesson, dayNum);
          },
        );
      }),
    );
  }

  Widget _buildDailyLessonCard(TimeSlot slot, LessonEntry? lesson, int dayNum) {
    final isDark = widget.isDarkMode;

    if (lesson == null) {
      // Boş Ders Saati
      return Container(
        margin: const EdgeInsets.only(bottom: 10),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
        decoration: BoxDecoration(
          color: isDark ? const Color(0xFF1E293B).withValues(alpha: 0.5) : const Color(0xFFF8FAFC),
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
            style: BorderStyle.solid,
          ),
        ),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
              decoration: BoxDecoration(
                color: isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9),
                borderRadius: BorderRadius.circular(8),
              ),
              child: Column(
                children: [
                  Text(
                    slot.label,
                    style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 12),
                  ),
                  Text(
                    slot.startTime,
                    style: const TextStyle(fontSize: 10, color: Colors.grey),
                  ),
                ],
              ),
            ),
            const SizedBox(width: 14),
            const Expanded(
              child: Text(
                'Boş Ders Saati',
                style: TextStyle(color: Colors.grey, fontSize: 13, fontStyle: FontStyle.italic),
              ),
            ),
            IconButton(
              icon: const Icon(Icons.add_rounded, size: 20, color: Color(0xFF4F46E5)),
              tooltip: 'Bu Saate Ders Ekle',
              onPressed: () => _addNewLesson(day: dayNum, period: slot.periodIndex),
            ),
          ],
        ),
      );
    }

    // Dolu Ders Kartı
    final subject = CurriculumRepository.getSubject(lesson.subjectId);
    final gradeCurriculum = subject.getGrade(lesson.grade);
    final activeWeek = gradeCurriculum.getCurrentWeek();
    final activeOutcome = activeWeek.outcomes.isNotEmpty ? activeWeek.outcomes.first : null;

    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF1E293B) : Colors.white,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: lesson.color.withValues(alpha: 0.35),
          width: 1.5,
        ),
        boxShadow: [
          BoxShadow(
            color: lesson.color.withValues(alpha: 0.08),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: InkWell(
        borderRadius: BorderRadius.circular(16),
        onTap: () => _showLessonDetails(lesson, slot),
        child: Padding(
          padding: const EdgeInsets.all(14),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Üst Satır: Saat + Ders ve Sınıf
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                    decoration: BoxDecoration(
                      color: lesson.color.withValues(alpha: 0.15),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Column(
                      children: [
                        Text(
                          slot.label,
                          style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontSize: 12,
                            color: lesson.color,
                          ),
                        ),
                        Text(
                          '${slot.startTime} - ${slot.endTime}',
                          style: TextStyle(
                            fontSize: 10,
                            color: lesson.color.withValues(alpha: 0.8),
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                              decoration: BoxDecoration(
                                color: lesson.color,
                                borderRadius: BorderRadius.circular(6),
                              ),
                              child: Text(
                                lesson.className.isNotEmpty ? lesson.className : '${lesson.grade}. Sınıf',
                                style: const TextStyle(
                                  color: Colors.white,
                                  fontSize: 11,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                            if (lesson.classroom.isNotEmpty) ...[
                              const SizedBox(width: 6),
                              Text(
                                '• ${lesson.classroom}',
                                style: const TextStyle(fontSize: 11, color: Colors.grey),
                              ),
                            ],
                          ],
                        ),
                        const SizedBox(height: 3),
                        Text(
                          lesson.subject,
                          style: const TextStyle(fontSize: 15, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                  ),
                  Icon(Icons.arrow_forward_ios_rounded, size: 14, color: lesson.color),
                ],
              ),

              const SizedBox(height: 10),
              const Divider(height: 1),
              const SizedBox(height: 10),

              // O Haftanın Kazanımı Önizlemesi & Hızlı Tıklama
              InkWell(
                onTap: () {
                  if (widget.onNavigateToCurriculum != null) {
                    widget.onNavigateToCurriculum!(
                      lesson.subjectId,
                      lesson.grade,
                      activeWeek.weekNumber,
                    );
                  }
                },
                borderRadius: BorderRadius.circular(10),
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                  decoration: BoxDecoration(
                    color: lesson.color.withValues(alpha: 0.08),
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: Row(
                    children: [
                      Icon(Icons.auto_awesome_rounded, size: 15, color: lesson.color),
                      const SizedBox(width: 8),
                      Expanded(
                        child: Text(
                          activeOutcome != null
                              ? '${activeOutcome.code}: ${activeOutcome.title}'
                              : 'Bu haftaki kazanım planı',
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.w600,
                            color: lesson.color,
                          ),
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                        ),
                      ),
                      const SizedBox(width: 4),
                      Text(
                        'Kazanımı Aç →',
                        style: TextStyle(
                          fontSize: 11,
                          fontWeight: FontWeight.bold,
                          color: lesson.color,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildTimetableGrid(List<TimeSlot> slots, List<LessonEntry> lessons) {
    final isDark = widget.isDarkMode;

    return SingleChildScrollView(
      scrollDirection: Axis.horizontal,
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(12),
        child: Table(
          defaultColumnWidth: const FixedColumnWidth(115),
          border: TableBorder.all(
            color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
            borderRadius: BorderRadius.circular(14),
          ),
          children: [
            // Başlık Satırı (Saat + Günler)
            TableRow(
              decoration: BoxDecoration(
                color: isDark ? const Color(0xFF1E293B) : const Color(0xFFEEF2FF),
                borderRadius: const BorderRadius.vertical(top: Radius.circular(14)),
              ),
              children: [
                Container(
                  padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 6),
                  alignment: Alignment.center,
                  child: const Text('Saat', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12)),
                ),
                ...List.generate(5, (index) {
                  final isToday = DateTime.now().weekday == (index + 1);
                  return Container(
                    padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 6),
                    alignment: Alignment.center,
                    decoration: isToday
                        ? BoxDecoration(
                            color: const Color(0xFF4F46E5).withValues(alpha: 0.15),
                          )
                        : null,
                    child: Text(
                      _dayShortNames[index],
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 13,
                        color: isToday ? const Color(0xFF4F46E5) : null,
                      ),
                    ),
                  );
                }),
              ],
            ),

            // Satırlar (Slotlar)
            ...slots.map((slot) {
              return TableRow(
                children: [
                  // Saat başlığı
                  Container(
                    padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 4),
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                      color: isDark ? const Color(0xFF0F172A) : const Color(0xFFF8FAFC),
                    ),
                    child: Column(
                      children: [
                        Text(slot.label, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 11)),
                        Text('${slot.startTime}\n${slot.endTime}',
                            textAlign: TextAlign.center,
                            style: const TextStyle(fontSize: 9, color: Colors.grey)),
                      ],
                    ),
                  ),

                  // Günler
                  ...List.generate(5, (dayIndex) {
                    final dayNum = dayIndex + 1;
                    final lesson = lessons
                        .where((l) => l.dayOfWeek == dayNum && l.periodIndex == slot.periodIndex)
                        .firstOrNull;

                    if (lesson == null) {
                      return InkWell(
                        onTap: () => _addNewLesson(day: dayNum, period: slot.periodIndex),
                        child: Container(
                          height: 70,
                          alignment: Alignment.center,
                          child: Icon(
                            Icons.add,
                            size: 16,
                            color: Colors.grey.withValues(alpha: 0.4),
                          ),
                        ),
                      );
                    }

                    return InkWell(
                      onTap: () => _showLessonDetails(lesson, slot),
                      child: Container(
                        height: 70,
                        margin: const EdgeInsets.all(2),
                        padding: const EdgeInsets.all(6),
                        decoration: BoxDecoration(
                          color: lesson.color.withValues(alpha: 0.15),
                          borderRadius: BorderRadius.circular(8),
                          border: Border.all(color: lesson.color.withValues(alpha: 0.4)),
                        ),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 1),
                              decoration: BoxDecoration(
                                color: lesson.color,
                                borderRadius: BorderRadius.circular(4),
                              ),
                              child: Text(
                                lesson.className.isNotEmpty ? lesson.className : '${lesson.grade}',
                                style: const TextStyle(
                                  color: Colors.white,
                                  fontSize: 9,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                            const SizedBox(height: 3),
                            Text(
                              lesson.subject,
                              style: TextStyle(
                                fontSize: 10,
                                fontWeight: FontWeight.bold,
                                color: lesson.color,
                              ),
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                            ),
                            if (lesson.classroom.isNotEmpty)
                              Text(
                                lesson.classroom,
                                style: const TextStyle(fontSize: 8, color: Colors.grey),
                                maxLines: 1,
                              ),
                          ],
                        ),
                      ),
                    );
                  }),
                ],
              );
            }),
          ],
        ),
      ),
    );
  }
}
