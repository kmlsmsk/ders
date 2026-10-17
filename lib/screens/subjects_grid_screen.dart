import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../data/curriculum_repository.dart';
import '../models/curriculum_model.dart';
import '../services/settings_service.dart';

class SubjectsGridScreen extends StatefulWidget {
  final Function(String subjectId, int grade) onSubjectSelected;
  final bool isDarkMode;

  const SubjectsGridScreen({
    super.key,
    required this.onSubjectSelected,
    required this.isDarkMode,
  });

  @override
  State<SubjectsGridScreen> createState() => _SubjectsGridScreenState();
}

class _SubjectsGridScreenState extends State<SubjectsGridScreen> {
  int _targetGrade = 7;

  @override
  void initState() {
    super.initState();
    _targetGrade = SettingsService.currentSettings.activeGrade;
  }

  @override
  Widget build(BuildContext context) {
    final isDark = widget.isDarkMode;
    final subjects = CurriculumRepository.getAllSubjects();
    final currentSubjectId = SettingsService.currentSettings.activeSubjectId;

    return Scaffold(
      backgroundColor: isDark ? const Color(0xFF0F172A) : const Color(0xFFF8FAFC),
      appBar: AppBar(
        elevation: 0,
        backgroundColor: isDark ? const Color(0xFF1E293B) : Colors.white,
        title: const Row(
          children: [
            Icon(Icons.dashboard_rounded, color: Color(0xFF4F46E5), size: 22),
            SizedBox(width: 10),
            Text(
              'Ortaokul Dersleri & Alanlar',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
      body: SafeArea(
        child: CustomScrollView(
          physics: const BouncingScrollPhysics(),
          slivers: [
            // Sınıf Düzeyi Seçici Şerit
            SliverToBoxAdapter(
              child: Padding(
                padding: const EdgeInsets.fromLTRB(16, 16, 16, 8),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Text(
                      'İNCELEMEK İSTEDİĞİNİZ SINIF DÜZEYİ',
                      style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, letterSpacing: 0.8, color: Colors.grey),
                    ),
                    const SizedBox(height: 8),
                    Row(
                      children: [5, 6, 7, 8].map((g) {
                        final isSelected = _targetGrade == g;
                        return Expanded(
                          child: GestureDetector(
                            onTap: () {
                              setState(() => _targetGrade = g);
                              HapticFeedback.selectionClick();
                            },
                            child: AnimatedContainer(
                              duration: const Duration(milliseconds: 180),
                              margin: const EdgeInsets.symmetric(horizontal: 4),
                              padding: const EdgeInsets.symmetric(vertical: 10),
                              decoration: BoxDecoration(
                                color: isSelected
                                    ? const Color(0xFF4F46E5)
                                    : (isDark ? const Color(0xFF1E293B) : Colors.white),
                                borderRadius: BorderRadius.circular(12),
                                border: Border.all(
                                  color: isSelected
                                      ? const Color(0xFF4F46E5)
                                      : (isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
                                  width: 1,
                                ),
                                boxShadow: isSelected
                                    ? [
                                        BoxShadow(
                                          color: const Color(0xFF4F46E5).withValues(alpha: 0.3),
                                          blurRadius: 8,
                                          offset: const Offset(0, 3),
                                        ),
                                      ]
                                    : null,
                              ),
                              child: Center(
                                child: Text(
                                  '$g. Sınıf ✨',
                                  style: TextStyle(
                                    fontSize: 12.5,
                                    fontWeight: FontWeight.bold,
                                    color: isSelected
                                        ? Colors.white
                                        : (isDark ? Colors.white70 : Colors.black87),
                                  ),
                                ),
                              ),
                            ),
                          ),
                        );
                      }).toList(),
                    ),
                  ],
                ),
              ),
            ),

            // 7 Dersin Izgara Kartları
            SliverPadding(
              padding: const EdgeInsets.all(16),
              sliver: SliverGrid(
                gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(
                  maxCrossAxisExtent: 420,
                  mainAxisSpacing: 16,
                  crossAxisSpacing: 16,
                  childAspectRatio: 1.18,
                ),
                delegate: SliverChildBuilderDelegate(
                  (context, index) {
                    final sub = subjects[index];
                    final isCurrentActive = currentSubjectId == sub.id;
                    final gradeCurriculum = sub.getGrade(_targetGrade);
                    final currentWeek = gradeCurriculum.getCurrentWeek();
                    final mainOutcome = currentWeek.outcomes.first;

                    return _buildSubjectCard(
                      subject: sub,
                      gradeCurriculum: gradeCurriculum,
                      currentWeek: currentWeek,
                      mainOutcome: mainOutcome,
                      isCurrentActive: isCurrentActive,
                      isDark: isDark,
                      onTap: () {
                        widget.onSubjectSelected(sub.id, _targetGrade);
                      },
                    );
                  },
                  childCount: subjects.length,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSubjectCard({
    required SubjectCurriculum subject,
    required GradeCurriculum gradeCurriculum,
    required CurriculumWeek currentWeek,
    required LearningOutcome mainOutcome,
    required bool isCurrentActive,
    required bool isDark,
    required VoidCallback onTap,
  }) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(20),
      child: Container(
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: isDark ? const Color(0xFF1E293B) : Colors.white,
          borderRadius: BorderRadius.circular(20),
          border: Border.all(
            color: isCurrentActive
                ? subject.primaryColor
                : (isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
            width: isCurrentActive ? 2 : 1,
          ),
          boxShadow: [
            BoxShadow(
              color: subject.primaryColor.withValues(alpha: isCurrentActive ? 0.15 : 0.05),
              blurRadius: 12,
              offset: const Offset(0, 4),
            ),
          ],
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Top Row: Icon, Title, and Active Tag
            Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(10),
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      colors: [subject.primaryColor, subject.accentColor],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                    borderRadius: BorderRadius.circular(14),
                    boxShadow: [
                      BoxShadow(
                        color: subject.primaryColor.withValues(alpha: 0.3),
                        blurRadius: 6,
                        offset: const Offset(0, 2),
                      ),
                    ],
                  ),
                  child: Icon(subject.icon, color: Colors.white, size: 22),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        children: [
                          Expanded(
                            child: Text(
                              subject.name,
                              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                            ),
                          ),
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                            decoration: BoxDecoration(
                              color: subject.primaryColor.withValues(alpha: 0.12),
                              borderRadius: BorderRadius.circular(6),
                            ),
                            child: Text(
                              subject.shortCode,
                              style: TextStyle(
                                fontSize: 10,
                                fontWeight: FontWeight.w800,
                                color: subject.primaryColor,
                              ),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 2),
                      Text(
                        '$_targetGrade. Sınıf • 36 Hafta Planı',
                        style: const TextStyle(fontSize: 11, color: Colors.grey, fontWeight: FontWeight.w500),
                      ),
                    ],
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),

            // Teaser for Active Week Outcome
            Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9),
                borderRadius: BorderRadius.circular(12),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Icon(Icons.bolt_rounded, size: 14, color: subject.primaryColor),
                      const SizedBox(width: 4),
                      Text(
                        '${currentWeek.weekNumber}. Hafta: ${currentWeek.dateRange}',
                        style: TextStyle(
                          fontSize: 11,
                          fontWeight: FontWeight.bold,
                          color: subject.primaryColor,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 4),
                  Text(
                    '${mainOutcome.code} • ${mainOutcome.title}',
                    style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w600),
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                  ),
                ],
              ),
            ),
            const Spacer(),

            // Action Button
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                if (isCurrentActive)
                  Row(
                    children: [
                      Icon(Icons.check_circle_rounded, size: 16, color: subject.primaryColor),
                      const SizedBox(width: 4),
                      Text(
                        'Aktif Branşınız',
                        style: TextStyle(
                          fontSize: 11,
                          fontWeight: FontWeight.bold,
                          color: subject.primaryColor,
                        ),
                      ),
                    ],
                  )
                else
                  Text(
                    'Müfredatı Seç ➔',
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                      color: subject.primaryColor,
                    ),
                  ),
                Icon(
                  Icons.arrow_forward_ios_rounded,
                  size: 14,
                  color: isCurrentActive ? subject.primaryColor : Colors.grey,
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
