import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../data/curriculum_repository.dart';
import '../models/teacher_assignment.dart';
import '../services/settings_service.dart';
import '../services/widget_sync_service.dart';

class SettingsScreen extends StatefulWidget {
  final VoidCallback onToggleTheme;
  final bool isDarkMode;

  const SettingsScreen({
    super.key,
    required this.onToggleTheme,
    required this.isDarkMode,
  });

  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  late TextEditingController _nameController;
  late TextEditingController _schoolController;
  late TextEditingController _titleController;
  late String _selectedSubjectId;
  late int _selectedGrade;
  late bool _autoSyncWidget;

  // Çoklu Ders ve Sınıf Listesi
  late List<TeacherAssignment> _assignedClasses;

  // Yeni sınıf ekleme kontrolcüleri
  String _newClassSubjectId = 'matematik';
  int _newClassGrade = 7;
  final TextEditingController _newClassBranchController = TextEditingController(text: 'A');

  @override
  void initState() {
    super.initState();
    final settings = SettingsService.currentSettings;
    _nameController = TextEditingController(text: settings.teacherName);
    _schoolController = TextEditingController(text: settings.schoolName);
    _titleController = TextEditingController(text: settings.teacherTitle);
    _selectedSubjectId = settings.activeSubjectId;
    _selectedGrade = settings.activeGrade;
    _autoSyncWidget = settings.autoSyncWidget;
    _assignedClasses = List<TeacherAssignment>.from(settings.assignedClasses);
  }

  @override
  void dispose() {
    _nameController.dispose();
    _schoolController.dispose();
    _titleController.dispose();
    _newClassBranchController.dispose();
    super.dispose();
  }

  void _addNewAssignment() {
    final branch = _newClassBranchController.text.trim().toUpperCase();
    final newAssignment = TeacherAssignment(
      id: DateTime.now().millisecondsSinceEpoch.toString(),
      subjectId: _newClassSubjectId,
      grade: _newClassGrade,
      branch: branch,
    );

    setState(() {
      _assignedClasses.add(newAssignment);
    });

    HapticFeedback.lightImpact();
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('${newAssignment.fullTitle} listenize eklendi!'),
        backgroundColor: const Color(0xFF059669),
        behavior: SnackBarBehavior.floating,
        duration: const Duration(seconds: 2),
      ),
    );
  }

  void _removeAssignment(String id) {
    setState(() {
      _assignedClasses.removeWhere((e) => e.id == id);
    });
    HapticFeedback.lightImpact();
  }

  Future<void> _saveSettings() async {
    final updated = SettingsService.currentSettings.copyWith(
      teacherName: _nameController.text.trim().isEmpty ? 'Öğretmen' : _nameController.text.trim(),
      schoolName: _schoolController.text.trim().isEmpty ? 'Ortaokulu' : _schoolController.text.trim(),
      teacherTitle: _titleController.text.trim(),
      activeSubjectId: _selectedSubjectId,
      activeGrade: _selectedGrade,
      autoSyncWidget: _autoSyncWidget,
      assignedClasses: _assignedClasses,
    );

    await SettingsService.updateSettings(updated);

    // Sync widget with new settings
    if (_autoSyncWidget) {
      final subject = CurriculumRepository.getSubject(_selectedSubjectId);
      final gradeCurriculum = subject.getGrade(_selectedGrade);
      final currentWeek = gradeCurriculum.getCurrentWeek();

      await WidgetSyncService.syncWeekToWidget(
        teacherName: updated.teacherName,
        gradeTitle: '${gradeCurriculum.title} ${subject.name}',
        week: currentWeek,
        selectedOutcome: currentWeek.outcomes.first,
      );
    }

    HapticFeedback.mediumImpact();

    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: const Row(
            children: [
              Icon(Icons.check_circle_rounded, color: Colors.white),
              SizedBox(width: 12),
              Expanded(
                child: Text(
                  'Ayarlar ve Öğretmen Profili başarıyla kaydedildi!',
                  style: TextStyle(fontWeight: FontWeight.w600),
                ),
              ),
            ],
          ),
          backgroundColor: const Color(0xFF059669),
          behavior: SnackBarBehavior.floating,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final isDark = widget.isDarkMode;
    final subjects = CurriculumRepository.getAllSubjects();
    final activeSubject = CurriculumRepository.getSubject(_selectedSubjectId);

    return Scaffold(
      backgroundColor: isDark ? const Color(0xFF0F172A) : const Color(0xFFF8FAFC),
      appBar: AppBar(
        elevation: 0,
        backgroundColor: isDark ? const Color(0xFF1E293B) : Colors.white,
        title: const Row(
          children: [
            Icon(Icons.tune_rounded, color: Color(0xFF4F46E5), size: 22),
            SizedBox(width: 10),
            Text(
              'Ayarlar & Öğretmen Profili',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
          ],
        ),
        actions: [
          IconButton(
            onPressed: widget.onToggleTheme,
            icon: Icon(isDark ? Icons.light_mode_rounded : Icons.dark_mode_rounded),
            tooltip: 'Tema Değiştir',
          ),
          const SizedBox(width: 8),
        ],
      ),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.all(16),
          children: [
            // 1. Öğretmen Profili Kartı
            _buildSectionCard(
              isDark: isDark,
              title: 'ÖĞRETMEN BİLGİLERİ',
              subtitle: 'Uygulama ve masaüstü widget\'ında görünecek bilgiler',
              icon: Icons.person_pin_rounded,
              iconColor: const Color(0xFF4F46E5),
              children: [
                TextField(
                  controller: _nameController,
                  textCapitalization: TextCapitalization.words,
                  decoration: InputDecoration(
                    labelText: 'Öğretmen Adı Soyadı',
                    hintText: 'Örn: Kemal Şimşek',
                    prefixIcon: const Icon(Icons.person_outline_rounded),
                    filled: true,
                    fillColor: isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9),
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: BorderSide.none),
                  ),
                ),
                const SizedBox(height: 12),
                TextField(
                  controller: _schoolController,
                  textCapitalization: TextCapitalization.words,
                  decoration: InputDecoration(
                    labelText: 'Okul Adı',
                    hintText: 'Örn: Atatürk Ortaokulu',
                    prefixIcon: const Icon(Icons.school_outlined),
                    filled: true,
                    fillColor: isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9),
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: BorderSide.none),
                  ),
                ),
                const SizedBox(height: 12),
                TextField(
                  controller: _titleController,
                  decoration: InputDecoration(
                    labelText: 'Unvan / Görev / Branş',
                    hintText: 'Örn: Matematik Öğretmeni, Zümre Başkanı',
                    prefixIcon: const Icon(Icons.badge_outlined),
                    filled: true,
                    fillColor: isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9),
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: BorderSide.none),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),

            // 2. GİRDİĞİM DERSLER VE SINIFLAR (ÇOKLU SEÇİM & SEÇMELİ DERSLER)
            _buildSectionCard(
              isDark: isDark,
              title: 'GİRDİĞİM DERSLER & SINIFLAR (ÇOKLU SEÇİM)',
              subtitle: 'Girdiğiniz tüm sınıfları ve seçmeli dersleri ekleyiniz (Ana sayfanızda özel carousel/ızgara olarak gösterilir)',
              icon: Icons.dashboard_customize_rounded,
              iconColor: const Color(0xFF0D9488),
              children: [
                // Mevcut Liste
                const Text(
                  'Aktif Sınıf ve Ders Listeniz:',
                  style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 8),

                if (_assignedClasses.isEmpty)
                  Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9),
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: const Text(
                      'Henüz sınıf eklenmemiş. Aşağıdaki formdan girdiğiniz sınıfları ve seçmeli dersleri ekleyebilirsiniz.',
                      style: TextStyle(fontSize: 12, color: Colors.grey),
                    ),
                  )
                else
                  Wrap(
                    spacing: 8,
                    runSpacing: 8,
                    children: _assignedClasses.map((ac) {
                      final sub = CurriculumRepository.getSubject(ac.subjectId);
                      return Chip(
                        avatar: Icon(sub.icon, color: Colors.white, size: 16),
                        label: Text(
                          ac.fullTitle,
                          style: const TextStyle(
                            color: Colors.white,
                            fontWeight: FontWeight.bold,
                            fontSize: 12,
                          ),
                        ),
                        backgroundColor: sub.primaryColor,
                        deleteIconColor: Colors.white70,
                        onDeleted: () => _removeAssignment(ac.id),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                      );
                    }).toList(),
                  ),

                const SizedBox(height: 16),
                const Divider(),
                const SizedBox(height: 10),

                // Yeni Sınıf Ekleme Formu
                const Text(
                  'Yeni Sınıf veya Seçmeli Ders Ekle:',
                  style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 10),

                // Ders Seçici Dropdown
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 2),
                  decoration: BoxDecoration(
                    color: isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9),
                    borderRadius: BorderRadius.circular(12),
                    border: Border.all(color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
                  ),
                  child: DropdownButtonHideUnderline(
                    child: DropdownButton<String>(
                      value: _newClassSubjectId,
                      isExpanded: true,
                      items: subjects.map((sub) {
                        return DropdownMenuItem(
                          value: sub.id,
                          child: Row(
                            children: [
                              Icon(sub.icon, color: sub.primaryColor, size: 20),
                              const SizedBox(width: 10),
                              Expanded(
                                child: Text(
                                  sub.name,
                                  style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 13),
                                ),
                              ),
                            ],
                          ),
                        );
                      }).toList(),
                      onChanged: (val) {
                        if (val != null) setState(() => _newClassSubjectId = val);
                      },
                    ),
                  ),
                ),
                const SizedBox(height: 10),

                // Sınıf Düzeyi ve Şube
                Row(
                  children: [
                    // Sınıf
                    Expanded(
                      flex: 3,
                      child: Row(
                        children: [5, 6, 7, 8].map((g) {
                          final isSel = _newClassGrade == g;
                          return Expanded(
                            child: GestureDetector(
                              onTap: () => setState(() => _newClassGrade = g),
                              child: Container(
                                margin: const EdgeInsets.symmetric(horizontal: 2),
                                padding: const EdgeInsets.symmetric(vertical: 9),
                                decoration: BoxDecoration(
                                  color: isSel ? const Color(0xFF0D9488) : (isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9)),
                                  borderRadius: BorderRadius.circular(10),
                                  border: Border.all(
                                    color: isSel ? const Color(0xFF0D9488) : Colors.transparent,
                                  ),
                                ),
                                alignment: Alignment.center,
                                child: Text(
                                  '$g. Sınıf',
                                  style: TextStyle(
                                    fontSize: 12,
                                    fontWeight: FontWeight.bold,
                                    color: isSel ? Colors.white : (isDark ? Colors.white70 : Colors.black87),
                                  ),
                                ),
                              ),
                            ),
                          );
                        }).toList(),
                      ),
                    ),
                    const SizedBox(width: 8),

                    // Şube
                    SizedBox(
                      width: 70,
                      child: TextField(
                        controller: _newClassBranchController,
                        textCapitalization: TextCapitalization.characters,
                        textAlign: TextAlign.center,
                        decoration: InputDecoration(
                          hintText: 'Şube',
                          isDense: true,
                          contentPadding: const EdgeInsets.symmetric(horizontal: 8, vertical: 10),
                          filled: true,
                          fillColor: isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9),
                          border: OutlineInputBorder(borderRadius: BorderRadius.circular(10), borderSide: BorderSide.none),
                        ),
                        style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 13),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 10),

                // Ekle Butonu
                ElevatedButton.icon(
                  onPressed: _addNewAssignment,
                  icon: const Icon(Icons.add_rounded, size: 18),
                  label: const Text('Bu Dersi / Sınıfı Listeme Ekle', style: TextStyle(fontWeight: FontWeight.bold)),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFF0D9488),
                    foregroundColor: Colors.white,
                    minimumSize: const Size.fromHeight(42),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),

            // 3. Varsayılan Ders ve Sınıf Seçimi
            _buildSectionCard(
              isDark: isDark,
              title: 'VARSAYILAN BRANŞ & SINIF',
              subtitle: 'Uygulama ilk açıldığında öncelikli odaklanacak ders ve sınıf',
              icon: Icons.auto_stories_rounded,
              iconColor: const Color(0xFF059669),
              children: [
                const Text(
                  'Varsayılan Ders Seçiniz:',
                  style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 8),

                // Grid of Subjects
                GridView.builder(
                  shrinkWrap: true,
                  physics: const NeverScrollableScrollPhysics(),
                  itemCount: subjects.length,
                  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 2,
                    mainAxisSpacing: 8,
                    crossAxisSpacing: 8,
                    childAspectRatio: 2.2,
                  ),
                  itemBuilder: (context, index) {
                    final sub = subjects[index];
                    final isSelected = _selectedSubjectId == sub.id;

                    return GestureDetector(
                      onTap: () {
                        setState(() => _selectedSubjectId = sub.id);
                        HapticFeedback.selectionClick();
                      },
                      child: AnimatedContainer(
                        duration: const Duration(milliseconds: 180),
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                        decoration: BoxDecoration(
                          color: isSelected
                              ? sub.primaryColor.withValues(alpha: 0.15)
                              : (isDark ? const Color(0xFF0F172A) : const Color(0xFFF8FAFC)),
                          borderRadius: BorderRadius.circular(12),
                          border: Border.all(
                            color: isSelected ? sub.primaryColor : (isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
                            width: isSelected ? 2 : 1,
                          ),
                        ),
                        child: Row(
                          children: [
                            Container(
                              padding: const EdgeInsets.all(6),
                              decoration: BoxDecoration(
                                color: sub.primaryColor.withValues(alpha: isSelected ? 0.9 : 0.15),
                                shape: BoxShape.circle,
                              ),
                              child: Icon(
                                sub.icon,
                                size: 16,
                                color: isSelected ? Colors.white : sub.primaryColor,
                              ),
                            ),
                            const SizedBox(width: 8),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                mainAxisAlignment: MainAxisAlignment.center,
                                children: [
                                  Text(
                                    sub.name,
                                    style: TextStyle(
                                      fontSize: 12,
                                      fontWeight: FontWeight.bold,
                                      color: isSelected ? sub.primaryColor : (isDark ? Colors.white : Colors.black87),
                                    ),
                                    maxLines: 1,
                                    overflow: TextOverflow.ellipsis,
                                  ),
                                  Text(
                                    sub.shortCode,
                                    style: const TextStyle(fontSize: 10, color: Colors.grey),
                                  ),
                                ],
                              ),
                            ),
                            if (isSelected)
                              Icon(Icons.check_circle_rounded, size: 16, color: sub.primaryColor),
                          ],
                        ),
                      ),
                    );
                  },
                ),
                const SizedBox(height: 16),

                // Sınıf Düzeyi Seçimi
                const Text(
                  'Varsayılan Sınıf Düzeyi:',
                  style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 8),
                Row(
                  children: [5, 6, 7, 8].map((g) {
                    final isSelected = _selectedGrade == g;
                    return Expanded(
                      child: GestureDetector(
                        onTap: () {
                          setState(() => _selectedGrade = g);
                          HapticFeedback.selectionClick();
                        },
                        child: Container(
                          margin: const EdgeInsets.symmetric(horizontal: 4),
                          padding: const EdgeInsets.symmetric(vertical: 10),
                          decoration: BoxDecoration(
                            color: isSelected ? activeSubject.primaryColor : (isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9)),
                            borderRadius: BorderRadius.circular(12),
                            border: Border.all(
                              color: isSelected ? activeSubject.primaryColor : Colors.transparent,
                            ),
                          ),
                          child: Center(
                            child: Text(
                              '$g. Sınıf',
                              style: TextStyle(
                                fontSize: 13,
                                fontWeight: FontWeight.bold,
                                color: isSelected ? Colors.white : (isDark ? Colors.white70 : Colors.black87),
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
            const SizedBox(height: 16),

            // 4. Widget & Sistem Tercihleri
            _buildSectionCard(
              isDark: isDark,
              title: 'WIDGET VE BİLDİRİM TERCİHLERİ',
              subtitle: 'Android ana ekran widget senkronizasyonu',
              icon: Icons.widgets_rounded,
              iconColor: const Color(0xFFEC4899),
              children: [
                SwitchListTile.adaptive(
                  contentPadding: EdgeInsets.zero,
                  value: _autoSyncWidget,
                  onChanged: (val) => setState(() => _autoSyncWidget = val),
                  title: const Text('Otomatik Widget Senkronizasyonu', style: TextStyle(fontSize: 14, fontWeight: FontWeight.bold)),
                  subtitle: const Text('Seçilen hafta ve kazanım otomatik olarak masaüstü widget\'ına aktarılsın.', style: TextStyle(fontSize: 12)),
                  activeTrackColor: const Color(0xFF4F46E5),
                ),
                const SizedBox(height: 8),
                OutlinedButton.icon(
                  onPressed: () async {
                    final pinned = await WidgetSyncService.pinWidgetToHomeScreen();
                    if (context.mounted) {
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(
                          content: Text(pinned ? 'Widget ana ekrana ekleniyor!' : 'Widget\'ı ana ekranınızda boş bir alana basılı tutarak ekleyebilirsiniz.'),
                          backgroundColor: const Color(0xFF4F46E5),
                        ),
                      );
                    }
                  },
                  icon: const Icon(Icons.add_to_home_screen_rounded),
                  label: const Text('Ana Ekrana Widget Ekle (Pin)'),
                  style: OutlinedButton.styleFrom(
                    minimumSize: const Size.fromHeight(44),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 20),

            // Kaydet Butonu
            FilledButton.icon(
              onPressed: _saveSettings,
              icon: const Icon(Icons.save_rounded),
              label: const Text('Değişiklikleri Kaydet & Uygula', style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold)),
              style: FilledButton.styleFrom(
                backgroundColor: activeSubject.primaryColor,
                minimumSize: const Size.fromHeight(50),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
              ),
            ),
            const SizedBox(height: 20),

            // Bilgi Rozeti
            Center(
              child: Column(
                children: [
                  Text(
                    'MüfredatVar • Türkiye Yüzyılı Maarif Modeli',
                    style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.grey.withValues(alpha: 0.8)),
                  ),
                  const SizedBox(height: 2),
                  const Text(
                    'Ortaokul Müfredat & Yıllık Plan Takip Sistemi',
                    style: TextStyle(fontSize: 11, color: Colors.grey),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 30),
          ],
        ),
      ),
    );
  }

  Widget _buildSectionCard({
    required bool isDark,
    required String title,
    required String subtitle,
    required IconData icon,
    required Color iconColor,
    required List<Widget> children,
  }) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF1E293B) : Colors.white,
        borderRadius: BorderRadius.circular(18),
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
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: iconColor.withValues(alpha: 0.12),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Icon(icon, color: iconColor, size: 20),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      title,
                      style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, letterSpacing: 0.6),
                    ),
                    Text(
                      subtitle,
                      style: const TextStyle(fontSize: 11, color: Colors.grey),
                    ),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 16),
          ...children,
        ],
      ),
    );
  }
}
