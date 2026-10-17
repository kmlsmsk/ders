import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../models/lesson_entry.dart';
import '../models/time_slot.dart';
import '../models/curriculum_model.dart';
import '../services/timetable_service.dart';
import '../data/curriculum_repository.dart';

class TodayLiveScheduleCard extends StatelessWidget {
  final VoidCallback onOpenTimetable;
  final Function(String subjectId, int grade, int? targetWeek) onSelectLessonOutcome;
  final Function(CurriculumWeek week, LearningOutcome outcome, String gradeTitle) onShowOutcomeDetail;
  final bool isDarkMode;

  const TodayLiveScheduleCard({
    super.key,
    required this.onOpenTimetable,
    required this.onSelectLessonOutcome,
    required this.onShowOutcomeDetail,
    required this.isDarkMode,
  });

  static const List<String> _dayNames = [
    'Pazartesi',
    'Salı',
    'Çarşamba',
    'Perşembe',
    'Cuma',
    'Cumartesi',
    'Pazar',
  ];

  @override
  Widget build(BuildContext context) {
    final now = DateTime.now();
    final todayWeekday = now.weekday; // 1 = Pazartesi, 7 = Pazar
    final currentMinutes = now.hour * 60 + now.minute;

    return ValueListenableBuilder<List<TimeSlot>>(
      valueListenable: TimetableService.slotsNotifier,
      builder: (context, slots, _) {
        return ValueListenableBuilder<List<LessonEntry>>(
          valueListenable: TimetableService.lessonsNotifier,
          builder: (context, allLessons, _) {
            // Filter today's lessons
            final todayLessons = allLessons
                .where((l) => l.dayOfWeek == todayWeekday)
                .toList()
              ..sort((a, b) => a.periodIndex.compareTo(b.periodIndex));

            // Find current active lesson or next upcoming lesson
            LessonEntry? activeLesson;
            TimeSlot? activeSlot;
            LessonEntry? nextLesson;
            TimeSlot? nextSlot;

            for (final slot in slots) {
              final lesson = todayLessons
                  .where((l) => l.periodIndex == slot.periodIndex)
                  .firstOrNull;

              if (currentMinutes >= slot.startMinutesSinceMidnight &&
                  currentMinutes <= slot.endMinutesSinceMidnight) {
                activeLesson = lesson;
                activeSlot = slot;
                break;
              } else if (currentMinutes < slot.startMinutesSinceMidnight) {
                if (lesson != null && nextLesson == null) {
                  nextLesson = lesson;
                  nextSlot = slot;
                }
              }
            }

            return Container(
              margin: const EdgeInsets.only(bottom: 12),
              decoration: BoxDecoration(
                color: isDarkMode ? const Color(0xFF1E293B) : Colors.white,
                borderRadius: BorderRadius.circular(20),
                border: Border.all(
                  color: activeLesson != null
                      ? const Color(0xFF059669)
                      : (isDarkMode ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
                  width: activeLesson != null ? 1.8 : 1,
                ),
                boxShadow: [
                  BoxShadow(
                    color: activeLesson != null
                        ? const Color(0xFF059669).withValues(alpha: 0.12)
                        : Colors.black.withValues(alpha: 0.04),
                    blurRadius: 12,
                    offset: const Offset(0, 4),
                  ),
                ],
              ),
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Top Bar: Day & Time + Status Tag + Timetable Button
                    Row(
                      children: [
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                          decoration: BoxDecoration(
                            color: activeLesson != null
                                ? const Color(0xFF059669).withValues(alpha: 0.15)
                                : const Color(0xFF4F46E5).withValues(alpha: 0.12),
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(
                                activeLesson != null
                                    ? Icons.play_circle_filled_rounded
                                    : Icons.schedule_rounded,
                                size: 14,
                                color: activeLesson != null
                                    ? const Color(0xFF059669)
                                    : const Color(0xFF4F46E5),
                              ),
                              const SizedBox(width: 6),
                              Text(
                                activeLesson != null
                                    ? 'ŞU ANKİ DERS'
                                    : (nextLesson != null ? 'SIRADAKİ DERS' : 'GÜNÜN AKIŞI'),
                                style: TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.w800,
                                  color: activeLesson != null
                                      ? const Color(0xFF059669)
                                      : const Color(0xFF4F46E5),
                                  letterSpacing: 0.4,
                                ),
                              ),
                            ],
                          ),
                        ),
                        const SizedBox(width: 8),
                        Text(
                          '${_dayNames[todayWeekday - 1]}',
                          style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.grey),
                        ),
                        const Spacer(),
                        InkWell(
                          onTap: onOpenTimetable,
                          borderRadius: BorderRadius.circular(8),
                          child: Padding(
                            padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 4),
                            child: Row(
                              children: [
                                Text(
                                  'Tüm Program',
                                  style: TextStyle(
                                    fontSize: 11.5,
                                    fontWeight: FontWeight.bold,
                                    color: isDarkMode ? const Color(0xFF93C5FD) : const Color(0xFF2563EB),
                                  ),
                                ),
                                const SizedBox(width: 2),
                                Icon(
                                  Icons.chevron_right_rounded,
                                  size: 16,
                                  color: isDarkMode ? const Color(0xFF93C5FD) : const Color(0xFF2563EB),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 12),

                    // Main Lesson Content
                    if (activeLesson != null && activeSlot != null)
                      _buildActiveLessonContent(context, activeLesson, activeSlot)
                    else if (nextLesson != null && nextSlot != null)
                      _buildNextLessonContent(context, nextLesson, nextSlot)
                    else
                      _buildNoActiveLessonContent(context, todayLessons),
                  ],
                ),
              ),
            );
          },
        );
      },
    );
  }

  Widget _buildActiveLessonContent(BuildContext context, LessonEntry lesson, TimeSlot slot) {
    final subject = CurriculumRepository.getSubject(lesson.subjectId);
    final gradeCurriculum = subject.getGrade(lesson.grade);
    final currentWeek = gradeCurriculum.getCurrentWeek();
    final currentOutcome = currentWeek.outcomes.isNotEmpty ? currentWeek.outcomes.first : null;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Sınıf, Ders ve Konum Bilgisi
        Row(
          children: [
            Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: lesson.color.withValues(alpha: 0.15),
                borderRadius: BorderRadius.circular(12),
              ),
              child: Icon(subject.icon, color: lesson.color, size: 22),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 2),
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
                      const SizedBox(width: 8),
                      Text(
                        '${slot.label} • ${slot.startTime} - ${slot.endTime}',
                        style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: Colors.grey),
                      ),
                      if (lesson.classroom.isNotEmpty) ...[
                        const SizedBox(width: 6),
                        Text(
                          '• ${lesson.classroom}',
                          style: const TextStyle(fontSize: 12, color: Colors.grey),
                        ),
                      ],
                    ],
                  ),
                  const SizedBox(height: 3),
                  Text(
                    lesson.subject,
                    style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                  ),
                ],
              ),
            ),
          ],
        ),
        const SizedBox(height: 12),

        // Sınıfta İşlenecek Bu Haftanın Kazanımı (Öğretmen için en kritik bilgi)
        if (currentOutcome != null) ...[
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: isDarkMode ? const Color(0xFF0F172A) : const Color(0xFFF8FAFC),
              borderRadius: BorderRadius.circular(14),
              border: Border.all(
                color: isDarkMode ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
              ),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                      decoration: BoxDecoration(
                        color: lesson.color.withValues(alpha: 0.15),
                        borderRadius: BorderRadius.circular(6),
                      ),
                      child: Text(
                        currentOutcome.code,
                        style: TextStyle(
                          color: lesson.color,
                          fontWeight: FontWeight.bold,
                          fontSize: 11,
                        ),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      child: Text(
                        currentOutcome.title,
                        style: const TextStyle(
                          fontSize: 13,
                          fontWeight: FontWeight.bold,
                        ),
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 6),
                Text(
                  currentOutcome.description,
                  style: TextStyle(
                    fontSize: 11.5,
                    color: isDarkMode ? const Color(0xFFCBD5E1) : const Color(0xFF475569),
                  ),
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                ),
              ],
            ),
          ),
          const SizedBox(height: 10),

          // Hızlı Butonlar: Deftere Kopyala & Kazanım Detayları
          Row(
            children: [
              Expanded(
                child: OutlinedButton.icon(
                  style: OutlinedButton.styleFrom(
                    padding: const EdgeInsets.symmetric(vertical: 8),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                  ),
                  icon: const Icon(Icons.copy_rounded, size: 15),
                  label: const Text('Deftere Kopyala', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
                  onPressed: () {
                    final text = '${currentWeek.dateRange} | ${lesson.className} ${lesson.subject} | ${currentOutcome.code} - ${currentOutcome.title}';
                    Clipboard.setData(ClipboardData(text: text));
                    HapticFeedback.mediumImpact();
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(
                        content: Text('Sınıf defteri metni panoya kopyalandı!'),
                        backgroundColor: Color(0xFF059669),
                        behavior: SnackBarBehavior.floating,
                        duration: Duration(seconds: 2),
                      ),
                    );
                  },
                ),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: FilledButton.icon(
                  style: FilledButton.styleFrom(
                    backgroundColor: lesson.color,
                    padding: const EdgeInsets.symmetric(vertical: 8),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                  ),
                  icon: const Icon(Icons.auto_stories_rounded, size: 15),
                  label: const Text('Kazanımı İncele', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
                  onPressed: () {
                    onSelectLessonOutcome(lesson.subjectId, lesson.grade, currentWeek.weekNumber);
                    onShowOutcomeDetail(
                      currentWeek,
                      currentOutcome,
                      '${gradeCurriculum.title} ${subject.name}',
                    );
                  },
                ),
              ),
            ],
          ),
        ],
      ],
    );
  }

  Widget _buildNextLessonContent(BuildContext context, LessonEntry lesson, TimeSlot slot) {
    final subject = CurriculumRepository.getSubject(lesson.subjectId);
    final gradeCurriculum = subject.getGrade(lesson.grade);
    final currentWeek = gradeCurriculum.getCurrentWeek();
    final currentOutcome = currentWeek.outcomes.isNotEmpty ? currentWeek.outcomes.first : null;

    return InkWell(
      onTap: () => onSelectLessonOutcome(lesson.subjectId, lesson.grade, currentWeek.weekNumber),
      borderRadius: BorderRadius.circular(12),
      child: Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: isDarkMode ? const Color(0xFF0F172A) : const Color(0xFFF8FAFC),
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: isDarkMode ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
          ),
        ),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: lesson.color.withValues(alpha: 0.15),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Icon(subject.icon, color: lesson.color, size: 20),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    '${slot.label} (${slot.startTime}) • ${lesson.className} ${lesson.subject}',
                    style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 13),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    currentOutcome != null
                        ? '${currentOutcome.code}: ${currentOutcome.title}'
                        : 'Bu haftaki konu planı',
                    style: TextStyle(
                      fontSize: 11.5,
                      color: isDarkMode ? const Color(0xFF94A3B8) : const Color(0xFF64748B),
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                ],
              ),
            ),
            Icon(Icons.arrow_forward_ios_rounded, size: 14, color: lesson.color),
          ],
        ),
      ),
    );
  }

  Widget _buildNoActiveLessonContent(BuildContext context, List<LessonEntry> todayLessons) {
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(
              color: Colors.blueAccent.withValues(alpha: 0.12),
              shape: BoxShape.circle,
            ),
            child: const Icon(Icons.wb_sunny_rounded, color: Colors.blueAccent, size: 20),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  todayLessons.isNotEmpty
                      ? 'Bugün toplam ${todayLessons.length} dersiniz planlanmıştır.'
                      : 'Bugün için ders programınız bulunmamaktadır.',
                  style: const TextStyle(fontSize: 13, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 2),
                const Text(
                  'Ders programınızı düzenlemek veya incelemek için dokunun.',
                  style: TextStyle(fontSize: 11, color: Colors.grey),
                ),
              ],
            ),
          ),
          TextButton(
            onPressed: onOpenTimetable,
            child: const Text('Programı Gör'),
          ),
        ],
      ),
    );
  }
}
