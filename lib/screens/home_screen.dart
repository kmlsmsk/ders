import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../data/curriculum_repository.dart';
import '../models/app_settings.dart';
import '../models/curriculum_model.dart';
import '../models/teacher_assignment.dart';
import '../services/settings_service.dart';
import '../services/widget_sync_service.dart';
import '../widgets/outcome_detail_sheet.dart';
import '../widgets/today_live_schedule_card.dart';
import '../widgets/widget_preview_card.dart';

enum HomeViewMode {
  weeklyCards, // 🗂️ Haftalık Akış (Modern Kartlar)
  weekGrid,    // ⊞ 36 Hafta Izgara Görünümü (Responsive Grid)
  defterDoldur // 📋 Sınıf Defteri Doldur (defterdoldur.com uyumlu)
}

class HomeScreen extends StatefulWidget {
  final VoidCallback onToggleTheme;
  final bool isDarkMode;
  final VoidCallback onOpenSubjectsGrid;
  final VoidCallback onOpenSettings;
  final VoidCallback onOpenTimetable;

  const HomeScreen({
    super.key,
    required this.onToggleTheme,
    required this.isDarkMode,
    required this.onOpenSubjectsGrid,
    required this.onOpenSettings,
    required this.onOpenTimetable,
  });

  @override
  State<HomeScreen> createState() => HomeScreenState();
}

class HomeScreenState extends State<HomeScreen> {
  late String _activeSubjectId;
  late int _selectedGrade;
  late SubjectCurriculum _currentSubject;
  late GradeCurriculum _currentGradeCurriculum;
  late CurriculumWeek _activeAcademicWeek; // Real-world current academic week
  late CurriculumWeek _selectedWeek; // Currently viewed week
  LearningOutcome? _selectedOutcome;
  final TextEditingController _searchController = TextEditingController();
  String _selectedThemeFilter = 'Tümü';
  int _selectedTermFilter = 0; // 0: Tümü, 1: 1. Dönem, 2: 2. Dönem
  final ScrollController _weekScrollController = ScrollController();
  HomeViewMode _viewMode = HomeViewMode.weeklyCards;
  bool _showProblemSolution = false;
  bool _isTeacherGridExpanded = false;

  @override
  void initState() {
    super.initState();
    final settings = SettingsService.currentSettings;
    _activeSubjectId = settings.activeSubjectId;
    _selectedGrade = settings.activeGrade;
    _loadCurriculum(initial: true);

    // Listen to settings changes (teacher name, default subject/grade)
    SettingsService.settingsNotifier.addListener(_onSettingsChanged);
  }

  @override
  void dispose() {
    SettingsService.settingsNotifier.removeListener(_onSettingsChanged);
    _searchController.dispose();
    _weekScrollController.dispose();
    super.dispose();
  }

  void _onSettingsChanged() {
    final settings = SettingsService.currentSettings;
    if (_activeSubjectId != settings.activeSubjectId || _selectedGrade != settings.activeGrade) {
      setState(() {
        _activeSubjectId = settings.activeSubjectId;
        _selectedGrade = settings.activeGrade;
        _loadCurriculum();
      });
    } else {
      setState(() {}); // refresh teacher name greeting
    }
  }

  void selectSubjectAndGrade(String subjectId, int grade, [int? targetWeek]) {
    setState(() {
      _activeSubjectId = subjectId;
      _selectedGrade = grade;
      _loadCurriculum();
      _searchController.clear();
      _selectedThemeFilter = 'Tümü';
      _selectedTermFilter = 0;
      if (targetWeek != null && targetWeek >= 1 && targetWeek <= _currentGradeCurriculum.weeks.length) {
        _selectedWeek = _currentGradeCurriculum.weeks[targetWeek - 1];
        if (_selectedWeek.outcomes.isNotEmpty) {
          _selectedOutcome = _selectedWeek.outcomes.first;
        }
      }
    });
    _scrollToCurrentWeek();
    HapticFeedback.lightImpact();
  }

  void _loadCurriculum({bool initial = false}) {
    _currentSubject = CurriculumRepository.getSubject(_activeSubjectId);
    _currentGradeCurriculum = _currentSubject.getGrade(_selectedGrade);
    _activeAcademicWeek = _currentGradeCurriculum.getCurrentWeek();
    _selectedWeek = _activeAcademicWeek;
    _selectedOutcome = _selectedWeek.outcomes.first;
    _showProblemSolution = false;

    // Automatically sync widget if enabled
    if (SettingsService.currentSettings.autoSyncWidget) {
      WidgetsBinding.instance.addPostFrameCallback((_) {
        WidgetSyncService.syncWeekToWidget(
          teacherName: SettingsService.currentSettings.teacherName,
          gradeTitle: '${_currentGradeCurriculum.title} ${_currentSubject.name}',
          week: _activeAcademicWeek,
          selectedOutcome: _selectedOutcome,
        );
        if (initial) {
          _scrollToCurrentWeek();
        }
      });
    }
  }

  void _onGradeChanged(int gradeNumber) {
    if (_selectedGrade == gradeNumber) return;
    setState(() {
      _selectedGrade = gradeNumber;
      _currentGradeCurriculum = _currentSubject.getGrade(gradeNumber);
      _activeAcademicWeek = _currentGradeCurriculum.getCurrentWeek();
      _selectedWeek = _activeAcademicWeek;
      _selectedOutcome = _selectedWeek.outcomes.first;
      _showProblemSolution = false;
      _searchController.clear();
      _selectedThemeFilter = 'Tümü';
      _selectedTermFilter = 0;
    });
    _scrollToCurrentWeek();
    HapticFeedback.lightImpact();
  }

  void _scrollToCurrentWeek() {
    final index = _activeAcademicWeek.weekNumber - 1;
    if (_weekScrollController.hasClients) {
      final offset = (index * 84.0) - 100.0;
      _weekScrollController.animateTo(
        offset.clamp(0.0, _weekScrollController.position.maxScrollExtent),
        duration: const Duration(milliseconds: 400),
        curve: Curves.easeOutCubic,
      );
    }
  }

  void _onWeekSelected(CurriculumWeek week) {
    setState(() {
      _selectedWeek = week;
      _selectedOutcome = week.outcomes.first;
      _showProblemSolution = false;
      _searchController.clear();
      if (_viewMode != HomeViewMode.weeklyCards) {
        _viewMode = HomeViewMode.weeklyCards; // switch to card detail view
      }
    });
    HapticFeedback.selectionClick();
  }

  void _showOutcomeDetails(LearningOutcome outcome) {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => OutcomeDetailSheet(
        gradeTitle: '${_currentGradeCurriculum.title} ${_currentSubject.name}',
        week: _selectedWeek,
        outcome: outcome,
      ),
    );
  }

  void _copyToClipboard(String text, String title) {
    Clipboard.setData(ClipboardData(text: text));
    HapticFeedback.mediumImpact();
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Row(
          children: [
            const Icon(Icons.assignment_turned_in_rounded, color: Colors.white),
            const SizedBox(width: 12),
            Expanded(
              child: Text(
                '$title panoya kopyalandı!',
                style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 13),
              ),
            ),
          ],
        ),
        backgroundColor: const Color(0xFF059669),
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        duration: const Duration(seconds: 2),
      ),
    );
  }

  void _showSubjectSwitcherModal() {
    final subjects = CurriculumRepository.getAllSubjects();
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (context) {
        final isDark = widget.isDarkMode;
        return Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            color: isDark ? const Color(0xFF1E293B) : Colors.white,
            borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Center(
                child: Container(
                  width: 40,
                  height: 4,
                  decoration: BoxDecoration(
                    color: Colors.grey.withValues(alpha: 0.4),
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
              ),
              const SizedBox(height: 14),
              const Text(
                'Ders Değiştir',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              const Text(
                'İncelemek istediğiniz ortaokul dersini seçiniz:',
                style: TextStyle(fontSize: 12, color: Colors.grey),
              ),
              const SizedBox(height: 16),
              GridView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: subjects.length,
                gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 2,
                  mainAxisSpacing: 10,
                  crossAxisSpacing: 10,
                  childAspectRatio: 2.3,
                ),
                itemBuilder: (context, index) {
                  final sub = subjects[index];
                  final isSelected = _activeSubjectId == sub.id;

                  return GestureDetector(
                    onTap: () {
                      Navigator.pop(context);
                      selectSubjectAndGrade(sub.id, _selectedGrade);
                    },
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                      decoration: BoxDecoration(
                        color: isSelected
                            ? sub.primaryColor.withValues(alpha: 0.15)
                            : (isDark ? const Color(0xFF0F172A) : const Color(0xFFF8FAFC)),
                        borderRadius: BorderRadius.circular(12),
                        border: Border.all(
                          color: isSelected
                              ? sub.primaryColor
                              : (isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
                          width: isSelected ? 2 : 1,
                        ),
                      ),
                      child: Row(
                        children: [
                          Icon(sub.icon, color: sub.primaryColor, size: 20),
                          const SizedBox(width: 8),
                          Expanded(
                            child: Text(
                              sub.name,
                              style: TextStyle(
                                fontSize: 13,
                                fontWeight: FontWeight.bold,
                                color: isSelected
                                    ? sub.primaryColor
                                    : (isDark ? Colors.white : Colors.black87),
                              ),
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                            ),
                          ),
                        ],
                      ),
                    ),
                  );
                },
              ),
              const SizedBox(height: 16),
            ],
          ),
        );
      },
    );
  }

  List<CurriculumWeek> _getFilteredWeeks() {
    final query = _searchController.text.trim().toLowerCase();
    return _currentGradeCurriculum.weeks.where((week) {
      if (_selectedTermFilter != 0 && week.term != _selectedTermFilter) {
        return false;
      }
      if (_selectedThemeFilter != 'Tümü' && !week.theme.contains(_selectedThemeFilter)) {
        return false;
      }
      if (query.isEmpty) return true;
      final inTitle = week.outcomes.any((o) => o.title.toLowerCase().contains(query));
      final inDesc = week.outcomes.any((o) => o.description.toLowerCase().contains(query));
      final inCode = week.outcomes.any((o) => o.code.toLowerCase().contains(query));
      final inConcepts = week.outcomes.any((o) => o.keyConcepts.any((c) => c.toLowerCase().contains(query)));
      final inWeekNum = '${week.weekNumber}. hafta'.contains(query) || '${week.weekNumber}'.contains(query);
      return inTitle || inDesc || inCode || inConcepts || inWeekNum;
    }).toList();
  }

  @override
  Widget build(BuildContext context) {
    final isDark = widget.isDarkMode;
    final primaryColor = _currentSubject.primaryColor;
    final settings = SettingsService.currentSettings;
    final filteredWeeks = _getFilteredWeeks();
    final gradeThemes = ['Tümü', ...{for (var w in _currentGradeCurriculum.weeks) w.theme}];

    return Scaffold(
      backgroundColor: isDark ? const Color(0xFF0F172A) : const Color(0xFFF8FAFC),
      appBar: _buildAppBar(isDark, primaryColor),
      body: SafeArea(
        child: CustomScrollView(
          physics: const BouncingScrollPhysics(),
          slivers: [
            // Top Sticky Control Panel: Teacher Greeting, Subject/Grade Menu Bar, View Mode Segmented Control
            SliverToBoxAdapter(
              child: Padding(
                padding: const EdgeInsets.fromLTRB(16, 12, 16, 8),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Teacher Personalization Greeting Card
                    _buildTeacherGreetingBar(settings, primaryColor, isDark),
                    const SizedBox(height: 12),

                    // Today's Live Schedule Card (Teacher Classroom Workflow)
                    TodayLiveScheduleCard(
                      onOpenTimetable: widget.onOpenTimetable,
                      onSelectLessonOutcome: (subjectId, grade, targetWeek) {
                        selectSubjectAndGrade(subjectId, grade, targetWeek);
                      },
                      onShowOutcomeDetail: (week, outcome, gradeTitle) {
                        showModalBottomSheet(
                          context: context,
                          isScrollControlled: true,
                          backgroundColor: Colors.transparent,
                          builder: (context) => OutcomeDetailSheet(
                            gradeTitle: gradeTitle,
                            week: week,
                            outcome: outcome,
                          ),
                        );
                      },
                      isDarkMode: isDark,
                    ),
                    const SizedBox(height: 12),

                    // Teacher Assigned Classes & Carousel / Grid Dashboard
                    _buildTeacherClassesSection(settings, isDark),
                    const SizedBox(height: 12),

                    // Active Subject & Grade Selector with Maarif Model Badge
                    _buildSubjectAndGradeBar(primaryColor, isDark),
                    const SizedBox(height: 12),

                    // View Mode Segmented Control: [ 🗂️ Akış | ⊞ 36 Hafta Izgara | 📋 Defter Doldur ]
                    _buildViewModeSegmentedBar(primaryColor, isDark),
                    const SizedBox(height: 12),

                    // Search and Theme Filters (visible in all views)
                    _buildSearchAndFilterBar(gradeThemes, primaryColor, isDark),
                    const SizedBox(height: 8),

                    // Weekly Horizontal Slider (only in Cards view)
                    if (_viewMode == HomeViewMode.weeklyCards) ...[
                      const SizedBox(height: 6),
                      _buildWeekHorizontalSlider(primaryColor, isDark),
                    ],
                  ],
                ),
              ),
            ),

            // Main Content Area depending on View Mode
            if (_viewMode == HomeViewMode.weeklyCards) ...[
              // VIEW 1: WEEKLY CARDS (Akış Görünümü)
              if (filteredWeeks.isNotEmpty) ...[
                SliverToBoxAdapter(
                  child: Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        // Active Academic Week Alert Banner (Quick Jump & Status)
                        _buildActiveWeekAlertCard(primaryColor, isDark),
                        const SizedBox(height: 12),

                        // Active Week Hero Card
                        _buildWeekHeaderBanner(primaryColor, isDark),
                        const SizedBox(height: 12),

                        // Pedagogical Grid of Colored Icon Boxes
                        _buildPedagogicalGrid(primaryColor, isDark),
                        const SizedBox(height: 16),

                        // Example Question & Solution Accordion
                        if (_selectedOutcome?.exampleProblem != null) ...[
                          _buildExampleProblemBox(primaryColor, isDark),
                          const SizedBox(height: 16),
                        ],

                        // Android Live Widget Preview Card with dynamic subject support
                        WidgetPreviewCard(
                          gradeTitle: _currentGradeCurriculum.title,
                          subject: _currentSubject,
                          week: _selectedWeek,
                          outcome: _selectedOutcome ?? _selectedWeek.outcomes.first,
                          onSyncSuccess: () => setState(() {}),
                        ),
                        const SizedBox(height: 30),
                      ],
                    ),
                  ),
                ),
              ] else ...[
                _buildEmptySearchState(),
              ],
            ] else if (_viewMode == HomeViewMode.weekGrid) ...[
              // VIEW 2: 36 WEEKS RESPONSIVE GRID (Izgara Görünümü)
              _buildFullWeekGridSliver(filteredWeeks, primaryColor, isDark),
            ] else ...[
              // VIEW 3: DEFTER DOLDUR MODULE (Sınıf Defteri Tablosu - defterdoldur.com)
              _buildDefterDoldurSliver(filteredWeeks, primaryColor, isDark),
            ],
          ],
        ),
      ),
      floatingActionButton: _buildFloatingActionButtons(primaryColor),
    );
  }

  // -------------------------------------------------------------
  // SUB-COMPONENTS & VIEW BUILDERS
  // -------------------------------------------------------------

  PreferredSizeWidget _buildAppBar(bool isDark, Color primaryColor) {
    return AppBar(
      elevation: 0,
      backgroundColor: isDark ? const Color(0xFF1E293B) : Colors.white,
      titleSpacing: 16,
      title: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(4),
            decoration: BoxDecoration(
              color: primaryColor.withValues(alpha: 0.12),
              borderRadius: BorderRadius.circular(10),
            ),
            child: ClipRRect(
              borderRadius: BorderRadius.circular(6),
              child: Image.asset(
                'assets/images/app_logo.png',
                width: 28,
                height: 28,
                fit: BoxFit.contain,
              ),
            ),
          ),
          const SizedBox(width: 10),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Text.rich(
                    TextSpan(
                      text: 'Müfredat',
                      style: TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                        color: isDark ? Colors.white : const Color(0xFF0F172A),
                      ),
                      children: [
                        TextSpan(
                          text: 'Var',
                          style: TextStyle(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                            color: primaryColor,
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(width: 6),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                    decoration: BoxDecoration(
                      color: primaryColor.withValues(alpha: 0.15),
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Text(
                      _currentSubject.shortCode,
                      style: TextStyle(fontSize: 10, fontWeight: FontWeight.w800, color: primaryColor),
                    ),
                  ),
                ],
              ),
              Row(
                children: [
                  Text(
                    _selectedGrade == 5 ? 'Türkiye Yüzyılı Maarif Modeli ✨' : 'MEB Ortaokul Müfredatı',
                    style: TextStyle(
                      fontSize: 11,
                      color: _selectedGrade == 5 ? const Color(0xFFD97706) : Colors.grey,
                      fontWeight: _selectedGrade == 5 ? FontWeight.bold : FontWeight.w500,
                    ),
                  ),
                ],
              ),
            ],
          ),
        ],
      ),
      actions: [
        IconButton(
          onPressed: widget.onToggleTheme,
          icon: Icon(
            widget.isDarkMode ? Icons.light_mode_rounded : Icons.dark_mode_rounded,
            color: primaryColor,
          ),
          tooltip: widget.isDarkMode ? 'Açık Tema' : 'Koyu Tema',
        ),
        IconButton(
          onPressed: widget.onOpenSubjectsGrid,
          icon: Icon(Icons.dashboard_rounded, color: primaryColor),
          tooltip: 'Tüm Dersler',
        ),
        IconButton(
          onPressed: widget.onOpenSettings,
          icon: const Icon(Icons.settings_rounded),
          tooltip: 'Ayarlar & Profil',
        ),
        const SizedBox(width: 4),
      ],
    );
  }

  Widget _buildTeacherGreetingBar(AppSettings settings, Color primaryColor, bool isDark) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF1E293B) : Colors.white,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
      ),
      child: Row(
        children: [
          CircleAvatar(
            radius: 18,
            backgroundColor: primaryColor.withValues(alpha: 0.15),
            child: Icon(Icons.person_rounded, color: primaryColor, size: 20),
          ),
          const SizedBox(width: 10),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'İyi Dersler, ${settings.teacherName}! 👋',
                  style: const TextStyle(fontSize: 13.5, fontWeight: FontWeight.bold),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
                Text(
                  '${settings.schoolName} • ${_currentGradeCurriculum.title} ${_currentSubject.name}',
                  style: const TextStyle(fontSize: 11, color: Colors.grey),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
              ],
            ),
          ),
          GestureDetector(
            onTap: widget.onOpenSettings,
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
              decoration: BoxDecoration(
                color: primaryColor.withValues(alpha: 0.1),
                borderRadius: BorderRadius.circular(8),
              ),
              child: Text(
                'Profili Düzenle',
                style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: primaryColor),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildTeacherClassesSection(AppSettings settings, bool isDark) {
    final classes = settings.effectiveAssignedClasses;
    if (classes.isEmpty) return const SizedBox.shrink();

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Row(
              children: [
                Icon(Icons.dashboard_customize_rounded, size: 15, color: _currentSubject.primaryColor),
                const SizedBox(width: 6),
                const Text(
                  'GİRDİĞİM DERSLER & SINIFLAR',
                  style: TextStyle(
                    fontSize: 11,
                    fontWeight: FontWeight.w800,
                    letterSpacing: 0.5,
                    color: Colors.grey,
                  ),
                ),
              ],
            ),
            GestureDetector(
              onTap: () {
                setState(() => _isTeacherGridExpanded = !_isTeacherGridExpanded);
                HapticFeedback.selectionClick();
              },
              child: Row(
                children: [
                  Icon(
                    _isTeacherGridExpanded ? Icons.view_carousel_rounded : Icons.grid_view_rounded,
                    size: 13,
                    color: _currentSubject.primaryColor,
                  ),
                  const SizedBox(width: 4),
                  Text(
                    _isTeacherGridExpanded ? 'Karusel' : 'Izgara',
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.bold,
                      color: _currentSubject.primaryColor,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
        const SizedBox(height: 8),
        if (_isTeacherGridExpanded)
          _buildTeacherClassesGrid(classes, isDark)
        else
          _buildTeacherClassesCarousel(classes, isDark),
      ],
    );
  }

  Widget _buildTeacherClassesCarousel(List<TeacherAssignment> classes, bool isDark) {
    return SizedBox(
      height: 115,
      child: ListView.separated(
        scrollDirection: Axis.horizontal,
        physics: const BouncingScrollPhysics(),
        itemCount: classes.length,
        separatorBuilder: (_, __) => const SizedBox(width: 10),
        itemBuilder: (context, index) {
          final item = classes[index];
          final sub = CurriculumRepository.getSubject(item.subjectId);
          final gc = sub.getGrade(item.grade);
          final activeW = gc.getCurrentWeek();
          final activeOut = activeW.outcomes.isNotEmpty ? activeW.outcomes.first : null;
          final isSelected = _activeSubjectId == item.subjectId && _selectedGrade == item.grade;

          return GestureDetector(
            onTap: () => selectSubjectAndGrade(item.subjectId, item.grade),
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 200),
              width: 250,
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: isDark ? const Color(0xFF1E293B) : Colors.white,
                borderRadius: BorderRadius.circular(14),
                border: Border.all(
                  color: isSelected ? sub.primaryColor : (isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
                  width: isSelected ? 2 : 1,
                ),
                boxShadow: [
                  BoxShadow(
                    color: isSelected ? sub.primaryColor.withValues(alpha: 0.15) : Colors.black.withValues(alpha: 0.03),
                    blurRadius: 6,
                    offset: const Offset(0, 2),
                  )
                ],
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.all(5),
                        decoration: BoxDecoration(
                          color: sub.primaryColor.withValues(alpha: 0.15),
                          borderRadius: BorderRadius.circular(6),
                        ),
                        child: Icon(sub.icon, color: sub.primaryColor, size: 14),
                      ),
                      const SizedBox(width: 6),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              item.fullTitle,
                              style: TextStyle(
                                fontSize: 12,
                                fontWeight: FontWeight.bold,
                                color: isSelected ? sub.primaryColor : null,
                              ),
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                            ),
                            Text(
                              '${activeW.weekNumber}. Hafta • ${activeW.dateRange}',
                              style: const TextStyle(fontSize: 9.5, color: Colors.grey),
                            ),
                          ],
                        ),
                      ),
                      if (isSelected)
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 2),
                          decoration: BoxDecoration(
                            color: sub.primaryColor,
                            borderRadius: BorderRadius.circular(4),
                          ),
                          child: const Text(
                            'Seçili',
                            style: TextStyle(color: Colors.white, fontSize: 9, fontWeight: FontWeight.bold),
                          ),
                        ),
                    ],
                  ),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 5),
                    decoration: BoxDecoration(
                      color: sub.primaryColor.withValues(alpha: 0.08),
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Row(
                      children: [
                        Icon(Icons.auto_awesome_rounded, size: 11, color: sub.primaryColor),
                        const SizedBox(width: 5),
                        Expanded(
                          child: Text(
                            activeOut != null ? '${activeOut.code}: ${activeOut.title}' : 'Bu haftaki kazanım',
                            style: TextStyle(
                              fontSize: 10.5,
                              fontWeight: FontWeight.w600,
                              color: sub.primaryColor,
                            ),
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }

  Widget _buildTeacherClassesGrid(List<TeacherAssignment> classes, bool isDark) {
    return GridView.builder(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      itemCount: classes.length,
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
        mainAxisSpacing: 8,
        crossAxisSpacing: 8,
        childAspectRatio: 1.6,
      ),
      itemBuilder: (context, index) {
        final item = classes[index];
        final sub = CurriculumRepository.getSubject(item.subjectId);
        final gc = sub.getGrade(item.grade);
        final activeW = gc.getCurrentWeek();
        final activeOut = activeW.outcomes.isNotEmpty ? activeW.outcomes.first : null;
        final isSelected = _activeSubjectId == item.subjectId && _selectedGrade == item.grade;

        return GestureDetector(
          onTap: () => selectSubjectAndGrade(item.subjectId, item.grade),
          child: Container(
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(
              color: isDark ? const Color(0xFF1E293B) : Colors.white,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(
                color: isSelected ? sub.primaryColor : (isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
                width: isSelected ? 2 : 1,
              ),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withValues(alpha: 0.03),
                  blurRadius: 4,
                  offset: const Offset(0, 1),
                )
              ],
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Row(
                  children: [
                    Icon(sub.icon, color: sub.primaryColor, size: 14),
                    const SizedBox(width: 5),
                    Expanded(
                      child: Text(
                        item.displayName,
                        style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 11),
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                      ),
                    ),
                    if (isSelected)
                      Icon(Icons.check_circle_rounded, color: sub.primaryColor, size: 13),
                  ],
                ),
                Text(
                  sub.name,
                  style: TextStyle(
                    fontSize: 10.5,
                    fontWeight: FontWeight.w600,
                    color: sub.primaryColor,
                  ),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 2),
                  decoration: BoxDecoration(
                    color: sub.primaryColor.withValues(alpha: 0.08),
                    borderRadius: BorderRadius.circular(5),
                  ),
                  child: Text(
                    activeOut != null ? activeOut.title : 'Kazanım Planı',
                    style: TextStyle(fontSize: 9.5, fontWeight: FontWeight.w600, color: sub.primaryColor),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  Widget _buildSubjectAndGradeBar(Color primaryColor, bool isDark) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Subject Selector Pill & Grade Tabs
        Row(
          children: [
            // Subject Pill (Clickable to switch subject)
            GestureDetector(
              onTap: _showSubjectSwitcherModal,
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [primaryColor, _currentSubject.accentColor],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  borderRadius: BorderRadius.circular(12),
                  boxShadow: [
                    BoxShadow(
                      color: primaryColor.withValues(alpha: 0.3),
                      blurRadius: 6,
                      offset: const Offset(0, 2),
                    ),
                  ],
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(_currentSubject.icon, color: Colors.white, size: 16),
                    const SizedBox(width: 6),
                    Text(
                      _currentSubject.name,
                      style: const TextStyle(color: Colors.white, fontSize: 13, fontWeight: FontWeight.bold),
                    ),
                    const SizedBox(width: 4),
                    const Icon(Icons.arrow_drop_down_rounded, color: Colors.white, size: 18),
                  ],
                ),
              ),
            ),
            const SizedBox(width: 8),

            // Grade Pills (5, 6, 7, 8) with Maarif Model
            Expanded(
              child: Row(
                children: [5, 6, 7, 8].map((g) {
                  final isSelected = _selectedGrade == g;
                  return Expanded(
                    child: GestureDetector(
                      onTap: () => _onGradeChanged(g),
                      child: Container(
                        margin: const EdgeInsets.symmetric(horizontal: 2),
                        padding: const EdgeInsets.symmetric(vertical: 8),
                        decoration: BoxDecoration(
                          color: isSelected ? primaryColor : (isDark ? const Color(0xFF1E293B) : Colors.white),
                          borderRadius: BorderRadius.circular(10),
                          border: Border.all(
                            color: isSelected
                                ? primaryColor
                                : (isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
                            width: 1,
                          ),
                        ),
                        child: Center(
                          child: Text(
                            '$g. Sınıf ✨',
                            style: TextStyle(
                              fontSize: 11.5,
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
            ),
          ],
        ),
      ],
    );
  }

  Widget _buildViewModeSegmentedBar(Color primaryColor, bool isDark) {
    return Container(
      padding: const EdgeInsets.all(4),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF1E293B) : const Color(0xFFF1F5F9),
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
      ),
      child: Row(
        children: [
          _buildViewModeTab(
            mode: HomeViewMode.weeklyCards,
            title: 'Haftalık Akış',
            icon: Icons.view_agenda_rounded,
            primaryColor: primaryColor,
            isDark: isDark,
          ),
          _buildViewModeTab(
            mode: HomeViewMode.weekGrid,
            title: '36 Hafta Izgarası',
            icon: Icons.grid_view_rounded,
            primaryColor: primaryColor,
            isDark: isDark,
          ),
          _buildViewModeTab(
            mode: HomeViewMode.defterDoldur,
            title: 'Defter Doldur',
            icon: Icons.assignment_rounded,
            primaryColor: primaryColor,
            isDark: isDark,
          ),
        ],
      ),
    );
  }

  Widget _buildViewModeTab({
    required HomeViewMode mode,
    required String title,
    required IconData icon,
    required Color primaryColor,
    required bool isDark,
  }) {
    final isSelected = _viewMode == mode;
    return Expanded(
      child: GestureDetector(
        onTap: () {
          setState(() => _viewMode = mode);
          HapticFeedback.lightImpact();
        },
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 200),
          padding: const EdgeInsets.symmetric(vertical: 8),
          decoration: BoxDecoration(
            color: isSelected
                ? (isDark ? const Color(0xFF334155) : Colors.white)
                : Colors.transparent,
            borderRadius: BorderRadius.circular(10),
            boxShadow: isSelected
                ? [
                    BoxShadow(
                      color: Colors.black.withValues(alpha: 0.06),
                      blurRadius: 4,
                      offset: const Offset(0, 1),
                    )
                  ]
                : null,
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(
                icon,
                size: 14,
                color: isSelected ? primaryColor : (isDark ? Colors.grey : const Color(0xFF64748B)),
              ),
              const SizedBox(width: 4),
              Flexible(
                child: Text(
                  title,
                  style: TextStyle(
                    fontSize: 11,
                    fontWeight: isSelected ? FontWeight.bold : FontWeight.w500,
                    color: isSelected ? primaryColor : (isDark ? Colors.grey : const Color(0xFF64748B)),
                  ),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildActiveWeekAlertCard(Color primaryColor, bool isDark) {
    final activeOutcome = _activeAcademicWeek.outcomes.first;
    final isViewingActiveWeek = _selectedWeek.weekNumber == _activeAcademicWeek.weekNumber;

    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: isDark
              ? [const Color(0xFF1E1B4B), const Color(0xFF1E293B)]
              : [primaryColor.withValues(alpha: 0.08), Colors.white],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: primaryColor.withValues(alpha: 0.3)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                decoration: BoxDecoration(
                  color: primaryColor,
                  borderRadius: BorderRadius.circular(6),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    const Icon(Icons.bolt_rounded, color: Colors.white, size: 13),
                    const SizedBox(width: 4),
                    Text(
                      'BU HAFTANIN KAZANIMI (${_activeAcademicWeek.dateRange.toUpperCase()})',
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 10,
                        fontWeight: FontWeight.bold,
                        letterSpacing: 0.3,
                      ),
                    ),
                  ],
                ),
              ),
              const Spacer(),
              Text(
                '${_activeAcademicWeek.weekNumber}. Hafta',
                style: TextStyle(
                  fontSize: 11.5,
                  fontWeight: FontWeight.bold,
                  color: primaryColor,
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),
          Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                decoration: BoxDecoration(
                  color: const Color(0xFF064E3B),
                  borderRadius: BorderRadius.circular(6),
                ),
                child: Text(
                  activeOutcome.code,
                  style: const TextStyle(color: Color(0xFF6EE7B7), fontSize: 11, fontWeight: FontWeight.bold),
                ),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  activeOutcome.title,
                  style: const TextStyle(
                    fontSize: 13,
                    fontWeight: FontWeight.bold,
                    height: 1.25,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 4),
          Text(
            activeOutcome.description,
            style: TextStyle(
              fontSize: 11,
              color: isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B),
              height: 1.3,
            ),
            maxLines: 2,
            overflow: TextOverflow.ellipsis,
          ),
          const SizedBox(height: 8),
          Row(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              OutlinedButton.icon(
                onPressed: () => _copyToClipboard(
                  '${_activeAcademicWeek.dateRange} | ${_currentGradeCurriculum.title} ${_currentSubject.name} | ${activeOutcome.code} - ${activeOutcome.title}',
                  'Bu haftanın kazanımı',
                ),
                icon: const Icon(Icons.copy_rounded, size: 13),
                label: const Text('Deftere Kopyala', style: TextStyle(fontSize: 11)),
                style: OutlinedButton.styleFrom(
                  visualDensity: VisualDensity.compact,
                  foregroundColor: const Color(0xFF059669),
                  side: const BorderSide(color: Color(0xFF059669)),
                ),
              ),
              if (!isViewingActiveWeek) ...[
                const SizedBox(width: 8),
                TextButton.icon(
                  onPressed: () => _onWeekSelected(_activeAcademicWeek),
                  icon: const Icon(Icons.arrow_forward_rounded, size: 14),
                  label: const Text('Görüntüle', style: TextStyle(fontSize: 11.5)),
                  style: TextButton.styleFrom(
                    visualDensity: VisualDensity.compact,
                    foregroundColor: primaryColor,
                  ),
                ),
              ],
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildSearchAndFilterBar(List<String> themes, Color primaryColor, bool isDark) {
    return Column(
      children: [
        Row(
          children: [
            Expanded(
              child: TextField(
                controller: _searchController,
                onChanged: (_) => setState(() {}),
                decoration: InputDecoration(
                  hintText: '${_currentSubject.name} ($_selectedGrade. Sınıf) veya konuda ara...',
                  hintStyle: const TextStyle(fontSize: 12),
                  prefixIcon: const Icon(Icons.search_rounded, size: 18),
                  suffixIcon: _searchController.text.isNotEmpty
                      ? IconButton(
                          icon: const Icon(Icons.clear_rounded, size: 18),
                          onPressed: () {
                            _searchController.clear();
                            setState(() {});
                          },
                        )
                      : null,
                  filled: true,
                  fillColor: isDark ? const Color(0xFF1E293B) : Colors.white,
                  contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                    borderSide: BorderSide(color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
                  ),
                  enabledBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                    borderSide: BorderSide(color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
                  ),
                ),
              ),
            ),
            const SizedBox(width: 8),
            // Term Selector Pill (Tümü / 1. Dönem / 2. Dönem)
            Container(
              decoration: BoxDecoration(
                color: isDark ? const Color(0xFF1E293B) : Colors.white,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
              ),
              child: PopupMenuButton<int>(
                initialValue: _selectedTermFilter,
                onSelected: (val) => setState(() => _selectedTermFilter = val),
                itemBuilder: (context) => [
                  const PopupMenuItem(value: 0, child: Text('Tüm Yıl (1 & 2. Dönem)')),
                  const PopupMenuItem(value: 1, child: Text('1. Dönem (1-19. Hafta)')),
                  const PopupMenuItem(value: 2, child: Text('2. Dönem (20-36. Hafta)')),
                ],
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 9),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Icon(Icons.calendar_month_rounded, size: 16, color: primaryColor),
                      const SizedBox(width: 4),
                      Text(
                        _selectedTermFilter == 0
                            ? 'Tüm Yıl'
                            : '$_selectedTermFilter. Dönem',
                        style: TextStyle(
                          fontSize: 11.5,
                          fontWeight: FontWeight.bold,
                          color: isDark ? Colors.white : Colors.black87,
                        ),
                      ),
                      const Icon(Icons.arrow_drop_down_rounded, size: 18),
                    ],
                  ),
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 8),
        // Horizontal Theme Chips
        SizedBox(
          height: 32,
          child: ListView.separated(
            scrollDirection: Axis.horizontal,
            physics: const BouncingScrollPhysics(),
            itemCount: themes.length,
            separatorBuilder: (_, __) => const SizedBox(width: 6),
            itemBuilder: (context, index) {
              final theme = themes[index];
              final isSelected = _selectedThemeFilter == theme;
              return ChoiceChip(
                label: Text(theme),
                selected: isSelected,
                labelStyle: TextStyle(
                  fontSize: 10.5,
                  fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                  color: isSelected ? Colors.white : (isDark ? Colors.white70 : Colors.black87),
                ),
                selectedColor: primaryColor,
                backgroundColor: isDark ? const Color(0xFF1E293B) : Colors.white,
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                side: BorderSide(
                  color: isSelected ? primaryColor : (isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
                ),
                onSelected: (selected) {
                  setState(() {
                    _selectedThemeFilter = selected ? theme : 'Tümü';
                  });
                },
              );
            },
          ),
        ),
      ],
    );
  }

  Widget _buildWeekHorizontalSlider(Color primaryColor, bool isDark) {
    final weeks = _currentGradeCurriculum.weeks;
    return SizedBox(
      height: 90,
      child: ListView.separated(
        controller: _weekScrollController,
        scrollDirection: Axis.horizontal,
        physics: const BouncingScrollPhysics(),
        itemCount: weeks.length,
        separatorBuilder: (_, __) => const SizedBox(width: 8),
        itemBuilder: (context, index) {
          final week = weeks[index];
          final isSelected = week.weekNumber == _selectedWeek.weekNumber;
          final isCurrent = week.weekNumber == _activeAcademicWeek.weekNumber;

          return GestureDetector(
            onTap: () => _onWeekSelected(week),
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 200),
              width: 84,
              padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 6),
              decoration: BoxDecoration(
                color: isSelected
                    ? primaryColor
                    : (isCurrent
                        ? primaryColor.withValues(alpha: 0.12)
                        : (isDark ? const Color(0xFF1E293B) : Colors.white)),
                borderRadius: BorderRadius.circular(16),
                border: Border.all(
                  color: isSelected
                      ? primaryColor
                      : (isCurrent ? primaryColor : (isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0))),
                  width: isCurrent ? 2 : 1,
                ),
                boxShadow: isSelected
                    ? [
                        BoxShadow(
                          color: primaryColor.withValues(alpha: 0.3),
                          blurRadius: 8,
                          offset: const Offset(0, 3),
                        )
                      ]
                    : null,
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  if (isCurrent && !isSelected)
                    Container(
                      margin: const EdgeInsets.only(bottom: 2),
                      width: 6,
                      height: 6,
                      decoration: BoxDecoration(
                        color: primaryColor,
                        shape: BoxShape.circle,
                      ),
                    ),
                  Text(
                    '${week.weekNumber}. Hafta',
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                      color: isSelected
                          ? Colors.white
                          : (isCurrent ? primaryColor : (isDark ? Colors.white : Colors.black87)),
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    week.dateRange,
                    textAlign: TextAlign.center,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 9.5,
                      color: isSelected
                          ? Colors.white.withValues(alpha: 0.9)
                          : (isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B)),
                    ),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }

  // -------------------------------------------------------------
  // VIEW 2: 36 WEEKS GRID (Izgara Görünümü)
  // -------------------------------------------------------------

  Widget _buildFullWeekGridSliver(List<CurriculumWeek> weeks, Color primaryColor, bool isDark) {
    if (weeks.isEmpty) {
      return SliverToBoxAdapter(child: _buildEmptySearchState());
    }

    return SliverPadding(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      sliver: SliverGrid(
        gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(
          maxCrossAxisExtent: 380,
          mainAxisSpacing: 12,
          crossAxisSpacing: 12,
          childAspectRatio: 1.35,
        ),
        delegate: SliverChildBuilderDelegate(
          (context, index) {
            final week = weeks[index];
            final outcome = week.outcomes.first;
            final isCurrent = week.weekNumber == _activeAcademicWeek.weekNumber;
            final isSelected = week.weekNumber == _selectedWeek.weekNumber;

            return Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: isDark ? const Color(0xFF1E293B) : Colors.white,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(
                  color: isCurrent
                      ? primaryColor
                      : (isSelected
                          ? primaryColor.withValues(alpha: 0.5)
                          : (isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0))),
                  width: isCurrent ? 2 : 1,
                ),
                boxShadow: [
                  BoxShadow(
                    color: isCurrent
                        ? primaryColor.withValues(alpha: 0.15)
                        : Colors.black.withValues(alpha: 0.03),
                    blurRadius: 8,
                    offset: const Offset(0, 3),
                  ),
                ],
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Header Row: Week Badge, BU HAFTA tag, Date
                  Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                        decoration: BoxDecoration(
                          color: primaryColor.withValues(alpha: 0.15),
                          borderRadius: BorderRadius.circular(6),
                        ),
                        child: Text(
                          '${week.weekNumber}. Hafta',
                          style: TextStyle(
                            fontSize: 11,
                            fontWeight: FontWeight.bold,
                            color: primaryColor,
                          ),
                        ),
                      ),
                      if (isCurrent) ...[
                        const SizedBox(width: 6),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                          decoration: BoxDecoration(
                            color: const Color(0xFF10B981),
                            borderRadius: BorderRadius.circular(6),
                          ),
                          child: const Text(
                            'BU HAFTA',
                            style: TextStyle(color: Colors.white, fontSize: 9.5, fontWeight: FontWeight.bold),
                          ),
                        ),
                      ],
                      const Spacer(),
                      Text(
                        week.dateRange,
                        style: TextStyle(
                          fontSize: 10.5,
                          color: isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B),
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),

                  // Theme Tag
                  Text(
                    week.theme,
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w600,
                      color: primaryColor,
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const SizedBox(height: 4),

                  // Outcome Code & Title
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 2),
                        decoration: BoxDecoration(
                          color: const Color(0xFF064E3B),
                          borderRadius: BorderRadius.circular(4),
                        ),
                        child: Text(
                          outcome.code,
                          style: const TextStyle(
                            color: Color(0xFF6EE7B7),
                            fontSize: 10,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                      const SizedBox(width: 6),
                      Expanded(
                        child: Text(
                          outcome.title,
                          style: const TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.bold,
                            height: 1.25,
                          ),
                          maxLines: 2,
                          overflow: TextOverflow.ellipsis,
                        ),
                      ),
                    ],
                  ),
                  const Spacer(),

                  // Bottom Action Buttons: "İncele" & "📋 Deftere Kopyala"
                  Row(
                    children: [
                      Expanded(
                        child: OutlinedButton(
                          onPressed: () => _onWeekSelected(week),
                          style: OutlinedButton.styleFrom(
                            visualDensity: VisualDensity.compact,
                            padding: EdgeInsets.zero,
                            side: BorderSide(color: primaryColor.withValues(alpha: 0.5)),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                          ),
                          child: Text(
                            'İncele',
                            style: TextStyle(fontSize: 11, color: primaryColor, fontWeight: FontWeight.bold),
                          ),
                        ),
                      ),
                      const SizedBox(width: 6),
                      IconButton(
                        onPressed: () => _copyToClipboard(
                          '${week.dateRange} | ${_currentGradeCurriculum.title} ${_currentSubject.name} | ${outcome.code} - ${outcome.title}\nKonu: ${week.subTheme}\nEtkinlik: ${week.evaluationActivity}',
                          '${week.weekNumber}. hafta defter metni',
                        ),
                        icon: const Icon(Icons.copy_rounded, size: 16),
                        tooltip: 'Deftere Kopyala',
                        color: const Color(0xFF059669),
                        style: IconButton.styleFrom(
                          backgroundColor: const Color(0xFF059669).withValues(alpha: 0.1),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            );
          },
          childCount: weeks.length,
        ),
      ),
    );
  }

  // -------------------------------------------------------------
  // VIEW 3: DEFTER DOLDUR MODULE (defterdoldur.com Uyumlu)
  // -------------------------------------------------------------

  Widget _buildDefterDoldurSliver(List<CurriculumWeek> weeks, Color primaryColor, bool isDark) {
    if (weeks.isEmpty) {
      return SliverToBoxAdapter(child: _buildEmptySearchState());
    }

    return SliverPadding(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      sliver: SliverList(
        delegate: SliverChildBuilderDelegate(
          (context, index) {
            if (index == 0) {
              // Information & Bulk Copy Banner
              return Container(
                margin: const EdgeInsets.only(bottom: 12),
                padding: const EdgeInsets.all(14),
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [
                      const Color(0xFF065F46),
                      const Color(0xFF047857),
                    ],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  borderRadius: BorderRadius.circular(16),
                  boxShadow: [
                    BoxShadow(
                      color: const Color(0xFF059669).withValues(alpha: 0.2),
                      blurRadius: 8,
                      offset: const Offset(0, 3),
                    ),
                  ],
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Row(
                      children: [
                        Icon(Icons.assignment_turned_in_rounded, color: Colors.white, size: 20),
                        SizedBox(width: 8),
                        Text(
                          'Sınıf Defteri Doldurma Modülü',
                          style: TextStyle(color: Colors.white, fontSize: 14, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    const SizedBox(height: 6),
                    const Text(
                      'Resmî MEB müfredatı ve Türkiye Yüzyılı Maarif Modeli standartlarında hazırlanmıştır. Tek tıkla kopyalayıp okul sınıf defterinize veya e-Okul sistemine yapıştırabilirsiniz.',
                      style: TextStyle(color: Color(0xFFD1FAE5), fontSize: 11.5, height: 1.35),
                    ),
                    const SizedBox(height: 10),
                    ElevatedButton.icon(
                      onPressed: () {
                        final allWeeksText = weeks.map((w) {
                          final o = w.outcomes.first;
                          return '${w.weekNumber}. Hafta (${w.dateRange}) | ${o.code}: ${o.title} | Konu: ${w.subTheme}';
                        }).join('\n\n');
                        _copyToClipboard(allWeeksText, 'Filtrelenen tüm haftaların defter metinleri');
                      },
                      icon: const Icon(Icons.copy_all_rounded, size: 16),
                      label: Text('Listelenen ${weeks.length} Haftayı Toplu Kopyala', style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.white,
                        foregroundColor: const Color(0xFF065F46),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                      ),
                    ),
                  ],
                ),
              );
            }

            final week = weeks[index - 1];
            final outcome = week.outcomes.first;
            final isCurrent = week.weekNumber == _activeAcademicWeek.weekNumber;

            return Container(
              margin: const EdgeInsets.only(bottom: 10),
              padding: const EdgeInsets.all(14),
              decoration: BoxDecoration(
                color: isDark ? const Color(0xFF1E293B) : Colors.white,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(
                  color: isCurrent
                      ? const Color(0xFF10B981)
                      : (isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
                  width: isCurrent ? 2 : 1,
                ),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Row: Hafta, Tarih, Kopyala Butonu
                  Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                        decoration: BoxDecoration(
                          color: primaryColor.withValues(alpha: 0.15),
                          borderRadius: BorderRadius.circular(6),
                        ),
                        child: Text(
                          '${week.weekNumber}. Hafta',
                          style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: primaryColor),
                        ),
                      ),
                      const SizedBox(width: 8),
                      Text(
                        week.dateRange,
                        style: TextStyle(
                          fontSize: 11.5,
                          fontWeight: FontWeight.w600,
                          color: isDark ? Colors.white70 : Colors.black87,
                        ),
                      ),
                      if (isCurrent) ...[
                        const SizedBox(width: 6),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                          decoration: BoxDecoration(
                            color: const Color(0xFF10B981),
                            borderRadius: BorderRadius.circular(4),
                          ),
                          child: const Text(
                            'BU HAFTA',
                            style: TextStyle(color: Colors.white, fontSize: 9.5, fontWeight: FontWeight.bold),
                          ),
                        ),
                      ],
                      const Spacer(),
                      // 1-Click Copy Button
                      ElevatedButton.icon(
                        onPressed: () => _copyToClipboard(
                          '${week.dateRange} | ${_currentGradeCurriculum.title} ${_currentSubject.name} | ${outcome.code} - ${outcome.title}\nKonu: ${week.subTheme}\nEtkinlik: ${week.evaluationActivity}',
                          '${week.weekNumber}. hafta defter metni',
                        ),
                        icon: const Icon(Icons.copy_rounded, size: 14),
                        label: const Text('Deftere Kopyala', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold)),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: const Color(0xFF059669),
                          foregroundColor: Colors.white,
                          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                          visualDensity: VisualDensity.compact,
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                        ),
                      ),
                    ],
                  ),
                  const Divider(height: 16),

                  // Resmî Defter Metni
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                        decoration: BoxDecoration(
                          color: const Color(0xFF064E3B),
                          borderRadius: BorderRadius.circular(4),
                        ),
                        child: Text(
                          outcome.code,
                          style: const TextStyle(color: Color(0xFF6EE7B7), fontSize: 10.5, fontWeight: FontWeight.bold),
                        ),
                      ),
                      const SizedBox(width: 8),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              outcome.title,
                              style: const TextStyle(fontSize: 13, fontWeight: FontWeight.bold, height: 1.25),
                            ),
                            const SizedBox(height: 3),
                            Text(
                              outcome.description,
                              style: TextStyle(
                                fontSize: 11,
                                color: isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B),
                                height: 1.3,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),

                  // Alt Öğrenme Alanı & Değerlendirme Etkinliği
                  Container(
                    width: double.infinity,
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      color: isDark ? const Color(0xFF0F172A) : const Color(0xFFF8FAFC),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            const Text('Ünite / Tema: ', style: TextStyle(fontSize: 10.5, fontWeight: FontWeight.bold, color: Colors.grey)),
                            Expanded(child: Text(week.theme, style: const TextStyle(fontSize: 10.5, fontWeight: FontWeight.w600))),
                          ],
                        ),
                        const SizedBox(height: 2),
                        Row(
                          children: [
                            const Text('Alt Konu: ', style: TextStyle(fontSize: 10.5, fontWeight: FontWeight.bold, color: Colors.grey)),
                            Expanded(child: Text(week.subTheme, style: const TextStyle(fontSize: 10.5, fontWeight: FontWeight.w600))),
                          ],
                        ),
                        const SizedBox(height: 2),
                        Row(
                          children: [
                            const Text('Süreç Etkinliği: ', style: TextStyle(fontSize: 10.5, fontWeight: FontWeight.bold, color: Colors.grey)),
                            Expanded(child: Text(week.evaluationActivity, style: const TextStyle(fontSize: 10.5, color: Color(0xFF059669), fontWeight: FontWeight.w600))),
                          ],
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            );
          },
          childCount: weeks.length + 1,
        ),
      ),
    );
  }

  // -------------------------------------------------------------
  // HERO & DETAIL SECTIONS FOR VIEW 1 (Cards View)
  // -------------------------------------------------------------

  Widget _buildWeekHeaderBanner(Color primaryColor, bool isDark) {
    final outcome = _selectedOutcome ?? _selectedWeek.outcomes.first;
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF1E293B) : Colors.white,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.03),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                decoration: BoxDecoration(
                  color: primaryColor.withValues(alpha: 0.1),
                  borderRadius: BorderRadius.circular(6),
                ),
                child: Text(
                  _selectedWeek.theme,
                  style: TextStyle(
                    color: primaryColor,
                    fontSize: 11,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const Spacer(),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                decoration: BoxDecoration(
                  color: const Color(0xFF064E3B),
                  borderRadius: BorderRadius.circular(6),
                  border: Border.all(color: const Color(0xFF10B981), width: 0.8),
                ),
                child: Text(
                  outcome.code,
                  style: const TextStyle(
                    color: Color(0xFF6EE7B7),
                    fontSize: 11,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 10),
          Text(
            outcome.title,
            style: const TextStyle(
              fontSize: 17,
              fontWeight: FontWeight.bold,
              height: 1.3,
            ),
          ),
          const SizedBox(height: 6),
          Text(
            outcome.description,
            style: TextStyle(
              fontSize: 13,
              color: isDark ? const Color(0xFFCBD5E1) : const Color(0xFF475569),
              height: 1.4,
            ),
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: outcome.keyConcepts.map((concept) {
              return Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(
                  color: isDark ? const Color(0xFF334155) : const Color(0xFFF1F5F9),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    const Icon(Icons.tag_rounded, size: 12, color: Colors.grey),
                    const SizedBox(width: 4),
                    Text(
                      concept,
                      style: TextStyle(
                        fontSize: 11,
                        color: isDark ? Colors.white70 : const Color(0xFF334155),
                      ),
                    ),
                  ],
                ),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }

  Widget _buildPedagogicalGrid(Color primaryColor, bool isDark) {
    final outcome = _selectedOutcome ?? _selectedWeek.outcomes.first;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Text(
          'PEDAGOJİK VE SÜREÇ BİLEŞENLERİ',
          style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, letterSpacing: 0.8, color: Colors.grey),
        ),
        const SizedBox(height: 10),

        LayoutBuilder(
          builder: (context, constraints) {
            final isTablet = constraints.maxWidth > 600;
            return GridView.count(
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              crossAxisCount: isTablet ? 4 : 2,
              crossAxisSpacing: 10,
              mainAxisSpacing: 10,
              childAspectRatio: isTablet ? 1.4 : 1.15,
              children: [
                _buildGridCard(
                  title: 'Haftalık Hedef',
                  content: _selectedWeek.weeklyGoal,
                  icon: Icons.flag_rounded,
                  iconColor: const Color(0xFF3B82F6),
                  bgColor: const Color(0xFF3B82F6).withValues(alpha: 0.08),
                  isDark: isDark,
                ),
                _buildGridCard(
                  title: 'Süreç Adımları',
                  content: outcome.processComponents.join('\n'),
                  icon: Icons.account_tree_rounded,
                  iconColor: const Color(0xFF10B981),
                  bgColor: const Color(0xFF10B981).withValues(alpha: 0.08),
                  isDark: isDark,
                  onTap: () => _showOutcomeDetails(outcome),
                ),
                _buildGridCard(
                  title: 'Maarif Notu',
                  content: outcome.pedagogicalNote,
                  icon: Icons.lightbulb_rounded,
                  iconColor: const Color(0xFFF59E0B),
                  bgColor: const Color(0xFFF59E0B).withValues(alpha: 0.08),
                  isDark: isDark,
                  onTap: () => _showOutcomeDetails(outcome),
                ),
                _buildGridCard(
                  title: 'Değerlendirme',
                  content: _selectedWeek.evaluationActivity,
                  icon: Icons.task_alt_rounded,
                  iconColor: const Color(0xFFEC4899),
                  bgColor: const Color(0xFFEC4899).withValues(alpha: 0.08),
                  isDark: isDark,
                ),
              ],
            );
          },
        ),
      ],
    );
  }

  Widget _buildGridCard({
    required String title,
    required String content,
    required IconData icon,
    required Color iconColor,
    required Color bgColor,
    required bool isDark,
    VoidCallback? onTap,
  }) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(16),
      child: Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: isDark ? const Color(0xFF1E293B) : Colors.white,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(6),
                  decoration: BoxDecoration(
                    color: bgColor,
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Icon(icon, size: 16, color: iconColor),
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    title,
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                      color: isDark ? Colors.white70 : const Color(0xFF1E293B),
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
                if (onTap != null)
                  const Icon(Icons.chevron_right_rounded, size: 16, color: Colors.grey),
              ],
            ),
            const SizedBox(height: 8),
            Expanded(
              child: Text(
                content,
                style: TextStyle(
                  fontSize: 11,
                  color: isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B),
                  height: 1.3,
                ),
                maxLines: 4,
                overflow: TextOverflow.ellipsis,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildExampleProblemBox(Color primaryColor, bool isDark) {
    final problem = _selectedOutcome?.exampleProblem;
    if (problem == null) return const SizedBox.shrink();

    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF1E293B) : Colors.white,
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: primaryColor.withValues(alpha: 0.3)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.all(6),
                decoration: BoxDecoration(
                  color: primaryColor.withValues(alpha: 0.12),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Icon(Icons.psychology_alt_rounded, size: 18, color: primaryColor),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Text(
                      'Örnek Problem & Etkinlik Çözümü',
                      style: TextStyle(fontSize: 13.5, fontWeight: FontWeight.bold),
                    ),
                    Text(
                      'Bağlam: ${problem.context}',
                      style: const TextStyle(fontSize: 11, color: Colors.grey),
                    ),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Text(
            problem.question,
            style: const TextStyle(fontSize: 13, fontWeight: FontWeight.w600, height: 1.35),
          ),
          const SizedBox(height: 12),
          AnimatedCrossFade(
            duration: const Duration(milliseconds: 250),
            crossFadeState: _showProblemSolution ? CrossFadeState.showSecond : CrossFadeState.showFirst,
            firstChild: OutlinedButton.icon(
              onPressed: () => setState(() => _showProblemSolution = true),
              icon: const Icon(Icons.visibility_rounded, size: 16),
              label: const Text('Adım Adım Çözümü Göster', style: TextStyle(fontSize: 12)),
              style: OutlinedButton.styleFrom(
                foregroundColor: primaryColor,
                side: BorderSide(color: primaryColor),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
              ),
            ),
            secondChild: Container(
              width: double.infinity,
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: primaryColor.withValues(alpha: 0.08),
                borderRadius: BorderRadius.circular(12),
                border: Border(left: BorderSide(color: primaryColor, width: 4)),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        '💡 Çözüm Adımları:',
                        style: TextStyle(
                          fontSize: 12,
                          fontWeight: FontWeight.bold,
                          color: primaryColor,
                        ),
                      ),
                      IconButton(
                        onPressed: () => setState(() => _showProblemSolution = false),
                        icon: const Icon(Icons.visibility_off_rounded, size: 16),
                        tooltip: 'Gizle',
                        visualDensity: VisualDensity.compact,
                      ),
                    ],
                  ),
                  const SizedBox(height: 4),
                  Text(
                    problem.solution,
                    style: TextStyle(
                      fontSize: 12.5,
                      color: isDark ? const Color(0xFFE2E8F0) : const Color(0xFF0F172A),
                      height: 1.35,
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildEmptySearchState() {
    return SliverToBoxAdapter(
      child: Padding(
        padding: const EdgeInsets.all(32),
        child: Center(
          child: Column(
            children: [
              Icon(Icons.search_off_rounded, size: 48, color: Colors.grey.withValues(alpha: 0.5)),
              const SizedBox(height: 12),
              const Text(
                'Aramanıza uygun hafta veya kazanım bulunamadı.',
                style: TextStyle(fontWeight: FontWeight.w600, color: Colors.grey),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildFloatingActionButtons(Color primaryColor) {
    return FloatingActionButton.extended(
      onPressed: () {
        setState(() {
          _selectedWeek = _activeAcademicWeek;
          _selectedOutcome = _selectedWeek.outcomes.first;
          _searchController.clear();
          _selectedThemeFilter = 'Tümü';
          _selectedTermFilter = 0;
          _viewMode = HomeViewMode.weeklyCards;
        });
        _scrollToCurrentWeek();
        HapticFeedback.mediumImpact();
      },
      backgroundColor: primaryColor,
      icon: const Icon(Icons.today_rounded, color: Colors.white),
      label: const Text(
        'Bu Haftaya Git',
        style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
      ),
    );
  }
}
