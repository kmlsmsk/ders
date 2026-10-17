import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../models/curriculum_model.dart';
import '../services/widget_sync_service.dart';

enum WidgetPreviewSize { wide4x2, compact2x1 }

class WidgetPreviewCard extends StatefulWidget {
  final String gradeTitle;
  final SubjectCurriculum? subject;
  final CurriculumWeek week;
  final LearningOutcome outcome;
  final VoidCallback? onSyncSuccess;

  const WidgetPreviewCard({
    super.key,
    this.gradeTitle = '7. Sınıf',
    this.subject,
    required this.week,
    required this.outcome,
    this.onSyncSuccess,
  });

  @override
  State<WidgetPreviewCard> createState() => _WidgetPreviewCardState();
}

class _WidgetPreviewCardState extends State<WidgetPreviewCard> {
  bool _isSyncing = false;
  bool _isPinning = false;
  WidgetPreviewSize _previewSize = WidgetPreviewSize.wide4x2;

  String get _subjectName => widget.subject?.name ?? 'Müfredat';
  Color get _primaryColor => widget.subject?.primaryColor ?? const Color(0xFF4F46E5);
  Color get _accentColor => widget.subject?.accentColor ?? const Color(0xFF6366F1);

  String get _fullGradeSubjectTitle {
    if (widget.gradeTitle.contains(_subjectName)) {
      return widget.gradeTitle;
    }
    return '${widget.gradeTitle} $_subjectName';
  }

  Future<void> _syncToWidget() async {
    setState(() => _isSyncing = true);
    final success = await WidgetSyncService.syncWeekToWidget(
      gradeTitle: _fullGradeSubjectTitle,
      week: widget.week,
      selectedOutcome: widget.outcome,
    );
    setState(() => _isSyncing = false);

    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Row(
            children: [
              Icon(
                success ? Icons.check_circle_rounded : Icons.info_outline_rounded,
                color: Colors.white,
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Text(
                  success
                      ? 'Android Widget güncellendi: $_fullGradeSubjectTitle - ${widget.outcome.code}'
                      : 'Widget verisi yerel olarak kaydedildi.',
                  style: const TextStyle(fontWeight: FontWeight.w600),
                ),
              ),
            ],
          ),
          backgroundColor: success ? const Color(0xFF059669) : _primaryColor,
          behavior: SnackBarBehavior.floating,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        ),
      );
      widget.onSyncSuccess?.call();
    }
  }

  Future<void> _pinWidgetToHome() async {
    setState(() => _isPinning = true);
    await WidgetSyncService.syncWeekToWidget(
      gradeTitle: _fullGradeSubjectTitle,
      week: widget.week,
      selectedOutcome: widget.outcome,
    );
    final pinned = await WidgetSyncService.pinWidgetToHomeScreen();
    setState(() => _isPinning = false);

    if (mounted) {
      if (pinned) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: const Row(
              children: [
                Icon(Icons.push_pin_rounded, color: Colors.white),
                SizedBox(width: 12),
                Expanded(
                  child: Text(
                    'Ana ekrana widget ekleme isteği gönderildi!',
                    style: TextStyle(fontWeight: FontWeight.w600),
                  ),
                ),
              ],
            ),
            backgroundColor: const Color(0xFF10B981),
            behavior: SnackBarBehavior.floating,
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
          ),
        );
      } else {
        _showWidgetHelpDialog();
      }
    }
  }

  void _copyClassRegistryText() {
    final textToCopy =
        '${widget.week.dateRange} | $_fullGradeSubjectTitle | ${widget.outcome.code}: ${widget.outcome.title}\nKonu: ${widget.week.subTheme}\nEtkinlik: ${widget.week.evaluationActivity}';

    Clipboard.setData(ClipboardData(text: textToCopy));
    HapticFeedback.mediumImpact();

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: const Row(
          children: [
            Icon(Icons.assignment_turned_in_rounded, color: Colors.white),
            SizedBox(width: 12),
            Expanded(
              child: Text(
                'Sınıf defteri metni panoya kopyalandı! Deftere veya e-Okul sistemine yapıştırabilirsiniz.',
                style: TextStyle(fontWeight: FontWeight.w600, fontSize: 13),
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

  void _showWidgetHelpDialog() {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        title: Row(
          children: [
            Icon(Icons.widgets_rounded, color: _primaryColor),
            const SizedBox(width: 10),
            const Text('Android Widget Rehberi', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          ],
        ),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            _buildStepRow(1, 'Telefonunuzun ana ekranında boş bir alana basılı tutun.'),
            const SizedBox(height: 12),
            _buildStepRow(2, 'Açılan menüden "Widget\'lar" (Araç Takımları) seçeneğine dokunun.'),
            const SizedBox(height: 12),
            _buildStepRow(3, 'Listeden "MüfredatVar" uygulamasını seçin.'),
            const SizedBox(height: 12),
            _buildStepRow(4, 'Widget\'ı basılı tutup ana ekranınızda dilediğiniz konuma bırakın.'),
            const SizedBox(height: 16),
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: _primaryColor.withValues(alpha: 0.1),
                borderRadius: BorderRadius.circular(12),
                border: Border(
                  left: BorderSide(color: _primaryColor, width: 4),
                ),
              ),
              child: Text(
                '💡 İpucu: Widget otomatik olarak seçilen dersin ($_subjectName) aktif haftasını Maarif Modeli kazanımlarıyla gösterir.',
                style: TextStyle(fontSize: 12.5, color: _primaryColor, height: 1.4, fontWeight: FontWeight.w500),
              ),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Anladım', style: TextStyle(fontWeight: FontWeight.bold)),
          ),
        ],
      ),
    );
  }

  static Widget _buildStepRow(int number, String text) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        CircleAvatar(
          radius: 11,
          backgroundColor: const Color(0xFF4F46E5),
          child: Text(
            '$number',
            style: const TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold),
          ),
        ),
        const SizedBox(width: 10),
        Expanded(
          child: Text(text, style: const TextStyle(fontSize: 13, height: 1.3)),
        ),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;

    return Container(
      margin: const EdgeInsets.symmetric(vertical: 8),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF1E293B) : Colors.white,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(
          color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.04),
            blurRadius: 12,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Header with Widget Size Selector Tabs
          Row(
            children: [
              Container(
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: _primaryColor.withValues(alpha: 0.12),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Icon(Icons.widgets_rounded, color: _primaryColor, size: 20),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'Android Canlı Widget Önizlemesi',
                      style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14, color: isDark ? Colors.white : Colors.black87),
                    ),
                    const Text(
                      'Ana ekranınızda masaüstünde canlı olarak çalışır',
                      style: TextStyle(fontSize: 11, color: Colors.grey),
                    ),
                  ],
                ),
              ),
              IconButton(
                onPressed: _showWidgetHelpDialog,
                icon: Icon(Icons.help_outline_rounded, size: 20, color: _primaryColor),
                tooltip: 'Widget Nasıl Eklenir?',
              ),
            ],
          ),
          const SizedBox(height: 12),

          // Size Selector Pills (4x2 Geniş / 2x1 Kompakt)
          Container(
            padding: const EdgeInsets.all(4),
            decoration: BoxDecoration(
              color: isDark ? const Color(0xFF0F172A) : const Color(0xFFF1F5F9),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Row(
              children: [
                Expanded(
                  child: GestureDetector(
                    onTap: () => setState(() => _previewSize = WidgetPreviewSize.wide4x2),
                    child: Container(
                      padding: const EdgeInsets.symmetric(vertical: 6),
                      decoration: BoxDecoration(
                        color: _previewSize == WidgetPreviewSize.wide4x2
                            ? (isDark ? const Color(0xFF334155) : Colors.white)
                            : Colors.transparent,
                        borderRadius: BorderRadius.circular(8),
                        boxShadow: _previewSize == WidgetPreviewSize.wide4x2
                            ? [
                                BoxShadow(
                                  color: Colors.black.withValues(alpha: 0.05),
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
                            Icons.view_agenda_rounded,
                            size: 14,
                            color: _previewSize == WidgetPreviewSize.wide4x2 ? _primaryColor : Colors.grey,
                          ),
                          const SizedBox(width: 6),
                          Text(
                            '4x2 Geniş Widget',
                            style: TextStyle(
                              fontSize: 11.5,
                              fontWeight: _previewSize == WidgetPreviewSize.wide4x2 ? FontWeight.bold : FontWeight.normal,
                              color: _previewSize == WidgetPreviewSize.wide4x2 ? _primaryColor : Colors.grey,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
                Expanded(
                  child: GestureDetector(
                    onTap: () => setState(() => _previewSize = WidgetPreviewSize.compact2x1),
                    child: Container(
                      padding: const EdgeInsets.symmetric(vertical: 6),
                      decoration: BoxDecoration(
                        color: _previewSize == WidgetPreviewSize.compact2x1
                            ? (isDark ? const Color(0xFF334155) : Colors.white)
                            : Colors.transparent,
                        borderRadius: BorderRadius.circular(8),
                        boxShadow: _previewSize == WidgetPreviewSize.compact2x1
                            ? [
                                BoxShadow(
                                  color: Colors.black.withValues(alpha: 0.05),
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
                            Icons.crop_16_9_rounded,
                            size: 14,
                            color: _previewSize == WidgetPreviewSize.compact2x1 ? _primaryColor : Colors.grey,
                          ),
                          const SizedBox(width: 6),
                          Text(
                            '2x1 Kompakt',
                            style: TextStyle(
                              fontSize: 11.5,
                              fontWeight: _previewSize == WidgetPreviewSize.compact2x1 ? FontWeight.bold : FontWeight.normal,
                              color: _previewSize == WidgetPreviewSize.compact2x1 ? _primaryColor : Colors.grey,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 14),

          // Live Android Widget Preview Simulation
          _previewSize == WidgetPreviewSize.wide4x2 ? _buildWideWidgetPreview() : _buildCompactWidgetPreview(),
          const SizedBox(height: 14),

          // Action Buttons: Send to Widget, Pin to Home, Copy Registry Text
          Row(
            children: [
              Expanded(
                flex: 3,
                child: FilledButton.icon(
                  onPressed: _isSyncing ? null : _syncToWidget,
                  icon: _isSyncing
                      ? const SizedBox(
                          width: 16,
                          height: 16,
                          child: CircularProgressIndicator(strokeWidth: 2, color: Colors.white),
                        )
                      : const Icon(Icons.sync_rounded, size: 18),
                  label: Text(_isSyncing ? 'Gönderiliyor...' : 'Widget\'a Gönder'),
                  style: FilledButton.styleFrom(
                    backgroundColor: _primaryColor,
                    padding: const EdgeInsets.symmetric(vertical: 12),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                ),
              ),
              const SizedBox(width: 8),
              Expanded(
                flex: 2,
                child: OutlinedButton.icon(
                  onPressed: _isPinning ? null : _pinWidgetToHome,
                  icon: const Icon(Icons.add_to_home_screen_rounded, size: 18),
                  label: const Text('Ekrana Ekle'),
                  style: OutlinedButton.styleFrom(
                    foregroundColor: _primaryColor,
                    side: BorderSide(color: _primaryColor),
                    padding: const EdgeInsets.symmetric(vertical: 12),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),

          // 1-Click Class Registry (Defter Doldur) Button
          SizedBox(
            width: double.infinity,
            child: TextButton.icon(
              onPressed: _copyClassRegistryText,
              icon: const Icon(Icons.copy_rounded, size: 16),
              label: const Text(
                'Bu Kazanımı Sınıf Defteri Formatında Kopyala',
                style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
              ),
              style: TextButton.styleFrom(
                foregroundColor: const Color(0xFF059669),
                backgroundColor: const Color(0xFF059669).withValues(alpha: 0.08),
                padding: const EdgeInsets.symmetric(vertical: 10),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildWideWidgetPreview() {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [
            const Color(0xFF0F172A),
            _primaryColor.withValues(alpha: 0.8),
            const Color(0xFF020617),
          ],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: _accentColor.withValues(alpha: 0.6), width: 1.5),
        boxShadow: [
          BoxShadow(
            color: _primaryColor.withValues(alpha: 0.25),
            blurRadius: 16,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisSize: MainAxisSize.min,
        children: [
          // Top Row: App Logo, Course & Grade Pill, Week & Date
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  ClipRRect(
                    borderRadius: BorderRadius.circular(4),
                    child: Image.asset(
                      'assets/images/app_logo.png',
                      width: 20,
                      height: 20,
                      fit: BoxFit.contain,
                    ),
                  ),
                  const SizedBox(width: 6),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                    decoration: BoxDecoration(
                      color: _primaryColor.withValues(alpha: 0.3),
                      borderRadius: BorderRadius.circular(6),
                      border: Border.all(color: _accentColor, width: 0.8),
                    ),
                    child: Text(
                      _fullGradeSubjectTitle.toUpperCase(),
                      style: const TextStyle(
                        color: Color(0xFFE0E7FF),
                        fontSize: 10.5,
                        fontWeight: FontWeight.bold,
                        letterSpacing: 0.3,
                      ),
                    ),
                  ),
                ],
              ),
              Text(
                '${widget.week.weekNumber}. Hafta • ${widget.week.dateRange}',
                style: TextStyle(
                  color: _accentColor.withValues(alpha: 0.9),
                  fontSize: 10.5,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),

          // Theme
          Text(
            'Tema: ${widget.week.theme}',
            style: const TextStyle(color: Color(0xFFCBD5E1), fontSize: 11),
          ),
          const SizedBox(height: 6),

          // Code & Title
          Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                decoration: BoxDecoration(
                  color: const Color(0xFF064E3B),
                  borderRadius: BorderRadius.circular(5),
                  border: Border.all(color: const Color(0xFF10B981), width: 0.8),
                ),
                child: Text(
                  widget.outcome.code,
                  style: const TextStyle(
                    color: Color(0xFF6EE7B7),
                    fontSize: 11,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  widget.outcome.title,
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 12.5,
                    fontWeight: FontWeight.bold,
                    height: 1.25,
                  ),
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                ),
              ),
            ],
          ),
          const SizedBox(height: 6),

          // Description
          Text(
            widget.outcome.description,
            style: const TextStyle(color: Color(0xFFCBD5E1), fontSize: 10.5, height: 1.3),
            maxLines: 2,
            overflow: TextOverflow.ellipsis,
          ),
          const SizedBox(height: 10),

          // Bottom Bar of Widget
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(Icons.star_rounded, size: 13, color: Color(0xFFFBBF24)),
                  SizedBox(width: 4),
                  Text(
                    'Türkiye Yüzyılı Maarif Modeli ✨',
                    style: TextStyle(
                      color: Color(0xFFFBBF24),
                      fontSize: 10,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ],
              ),
              Text(
                'Deftere hazır ➔',
                style: TextStyle(color: _accentColor, fontSize: 10, fontWeight: FontWeight.bold),
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildCompactWidgetPreview() {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [
            const Color(0xFF0F172A),
            _primaryColor.withValues(alpha: 0.7),
          ],
          begin: Alignment.centerLeft,
          end: Alignment.centerRight,
        ),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: _accentColor.withValues(alpha: 0.5), width: 1.2),
        boxShadow: [
          BoxShadow(
            color: _primaryColor.withValues(alpha: 0.2),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        children: [
          ClipRRect(
            borderRadius: BorderRadius.circular(6),
            child: Image.asset(
              'assets/images/app_logo.png',
              width: 32,
              height: 32,
              fit: BoxFit.contain,
            ),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                Row(
                  children: [
                    Text(
                      _fullGradeSubjectTitle,
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(width: 6),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 1),
                      decoration: BoxDecoration(
                        color: const Color(0xFF064E3B),
                        borderRadius: BorderRadius.circular(4),
                      ),
                      child: Text(
                        widget.outcome.code,
                        style: const TextStyle(color: Color(0xFF6EE7B7), fontSize: 9.5, fontWeight: FontWeight.bold),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 3),
                Text(
                  widget.outcome.title,
                  style: const TextStyle(
                    color: Color(0xFFE2E8F0),
                    fontSize: 11.5,
                    fontWeight: FontWeight.w600,
                  ),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
              ],
            ),
          ),
          const SizedBox(width: 8),
          Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              Text(
                '${widget.week.weekNumber}. Hf',
                style: TextStyle(
                  color: _accentColor,
                  fontSize: 12,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text(
                widget.week.dateRange.split(' ')[0],
                style: const TextStyle(color: Color(0xFF94A3B8), fontSize: 9.5),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
