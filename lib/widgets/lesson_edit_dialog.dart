import 'package:flutter/material.dart';
import '../models/lesson_entry.dart';
import '../models/time_slot.dart';
import '../data/curriculum_repository.dart';

class LessonEditDialog extends StatefulWidget {
  final LessonEntry? initialLesson;
  final int defaultDay;
  final int defaultPeriod;
  final List<TimeSlot> slots;

  const LessonEditDialog({
    super.key,
    this.initialLesson,
    this.defaultDay = 1,
    this.defaultPeriod = 1,
    required this.slots,
  });

  @override
  State<LessonEditDialog> createState() => _LessonEditDialogState();
}

class _LessonEditDialogState extends State<LessonEditDialog> {
  late int _dayOfWeek;
  late int _periodIndex;
  late String _selectedSubjectId;
  late int _selectedGrade;
  late TextEditingController _classNameController;
  late TextEditingController _classroomController;
  late TextEditingController _notesController;
  late int _selectedColor;

  static const List<int> _colorOptions = [
    0xFF2563EB, // Blue
    0xFF4F46E5, // Indigo
    0xFF0D9488, // Teal
    0xFF059669, // Emerald
    0xFFD97706, // Amber
    0xFFDC2626, // Red
    0xFF7C3AED, // Violet
    0xFFDB2777, // Pink
  ];

  final List<String> _dayNames = const [
    'Pazartesi',
    'Salı',
    'Çarşamba',
    'Perşembe',
    'Cuma',
    'Cumartesi',
    'Pazar',
  ];

  @override
  void initState() {
    super.initState();
    final l = widget.initialLesson;
    _dayOfWeek = l?.dayOfWeek ?? widget.defaultDay;
    _periodIndex = l?.periodIndex ?? widget.defaultPeriod;
    _selectedSubjectId = l?.subjectId ?? 'matematik';
    _selectedGrade = l?.grade ?? 7;
    _classNameController = TextEditingController(text: l?.className ?? '7-A');
    _classroomController = TextEditingController(text: l?.classroom ?? '');
    _notesController = TextEditingController(text: l?.notes ?? '');
    _selectedColor = l?.colorValue ?? _colorOptions[1];
  }

  @override
  void dispose() {
    _classNameController.dispose();
    _classroomController.dispose();
    _notesController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;
    final subjects = CurriculumRepository.getAllSubjects();

    return Dialog(
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
      backgroundColor: isDark ? const Color(0xFF1E293B) : Colors.white,
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 420),
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(20),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      color: Color(_selectedColor).withValues(alpha: 0.15),
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: Icon(
                      Icons.edit_calendar_rounded,
                      color: Color(_selectedColor),
                      size: 22,
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Text(
                      widget.initialLesson == null ? 'Yeni Ders Ekle' : 'Dersi Düzenle',
                      style: const TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                  IconButton(
                    icon: const Icon(Icons.close_rounded, size: 20),
                    onPressed: () => Navigator.pop(context),
                  ),
                ],
              ),
              const SizedBox(height: 16),

              // Gün & Saat
              Row(
                children: [
                  Expanded(
                    flex: 3,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text('Gün', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.grey)),
                        const SizedBox(height: 4),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10),
                          decoration: BoxDecoration(
                            border: Border.all(color: Colors.grey.withValues(alpha: 0.3)),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: DropdownButtonHideUnderline(
                            child: DropdownButton<int>(
                              value: _dayOfWeek,
                              isExpanded: true,
                              items: List.generate(5, (i) {
                                return DropdownMenuItem(
                                  value: i + 1,
                                  child: Text(_dayNames[i], style: const TextStyle(fontSize: 13)),
                                );
                              }),
                              onChanged: (v) {
                                if (v != null) setState(() => _dayOfWeek = v);
                              },
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(width: 10),
                  Expanded(
                    flex: 2,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text('Ders Saati', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.grey)),
                        const SizedBox(height: 4),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10),
                          decoration: BoxDecoration(
                            border: Border.all(color: Colors.grey.withValues(alpha: 0.3)),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: DropdownButtonHideUnderline(
                            child: DropdownButton<int>(
                              value: _periodIndex,
                              isExpanded: true,
                              items: widget.slots.map((s) {
                                return DropdownMenuItem(
                                  value: s.periodIndex,
                                  child: Text(s.label, style: const TextStyle(fontSize: 13)),
                                );
                              }).toList(),
                              onChanged: (v) {
                                if (v != null) setState(() => _periodIndex = v);
                              },
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 14),

              // Ders Seçimi
              const Text('Ders', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.grey)),
              const SizedBox(height: 4),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10),
                decoration: BoxDecoration(
                  border: Border.all(color: Colors.grey.withValues(alpha: 0.3)),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: DropdownButtonHideUnderline(
                  child: DropdownButton<String>(
                    value: _selectedSubjectId,
                    isExpanded: true,
                    items: subjects.map((sub) {
                      return DropdownMenuItem(
                        value: sub.id,
                        child: Row(
                          children: [
                            Icon(sub.icon, color: sub.primaryColor, size: 18),
                            const SizedBox(width: 8),
                            Expanded(child: Text(sub.name, style: const TextStyle(fontSize: 13))),
                          ],
                        ),
                      );
                    }).toList(),
                    onChanged: (v) {
                      if (v != null) {
                        setState(() {
                          _selectedSubjectId = v;
                          final sub = CurriculumRepository.getSubject(v);
                          _selectedColor = sub.primaryColor.toARGB32();
                        });
                      }
                    },
                  ),
                ),
              ),
              const SizedBox(height: 14),

              // Sınıf Düzeyi ve Şube
              Row(
                children: [
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text('Sınıf Düzeyi', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.grey)),
                        const SizedBox(height: 4),
                        Row(
                          children: [5, 6, 7, 8].map((g) {
                            final isSel = _selectedGrade == g;
                            return Expanded(
                              child: GestureDetector(
                                onTap: () => setState(() => _selectedGrade = g),
                                child: Container(
                                  margin: const EdgeInsets.symmetric(horizontal: 2),
                                  padding: const EdgeInsets.symmetric(vertical: 8),
                                  decoration: BoxDecoration(
                                    color: isSel ? Color(_selectedColor) : Colors.transparent,
                                    borderRadius: BorderRadius.circular(8),
                                    border: Border.all(
                                      color: isSel ? Color(_selectedColor) : Colors.grey.withValues(alpha: 0.3),
                                    ),
                                  ),
                                  alignment: Alignment.center,
                                  child: Text(
                                    '$g',
                                    style: TextStyle(
                                      fontSize: 13,
                                      fontWeight: FontWeight.bold,
                                      color: isSel ? Colors.white : null,
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
                  const SizedBox(width: 10),
                  SizedBox(
                    width: 90,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text('Şube / Kod', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.grey)),
                        const SizedBox(height: 4),
                        TextField(
                          controller: _classNameController,
                          decoration: InputDecoration(
                            hintText: '7-A',
                            isDense: true,
                            contentPadding: const EdgeInsets.symmetric(horizontal: 10, vertical: 9),
                            border: OutlineInputBorder(borderRadius: BorderRadius.circular(8)),
                          ),
                          style: const TextStyle(fontSize: 13, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 14),

              // Derslik / Konum
              const Text('Derslik / Yer (Opsiyonel)', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.grey)),
              const SizedBox(height: 4),
              TextField(
                controller: _classroomController,
                decoration: InputDecoration(
                  hintText: 'örn: 204 Nolu Oda, Fen Lab',
                  isDense: true,
                  contentPadding: const EdgeInsets.symmetric(horizontal: 10, vertical: 9),
                  border: OutlineInputBorder(borderRadius: BorderRadius.circular(8)),
                ),
                style: const TextStyle(fontSize: 13),
              ),
              const SizedBox(height: 14),

              // Renk Seçici
              const Text('Kart Rengi', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.grey)),
              const SizedBox(height: 6),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: _colorOptions.map((c) {
                  final isSel = _selectedColor == c;
                  return GestureDetector(
                    onTap: () => setState(() => _selectedColor = c),
                    child: Container(
                      width: 32,
                      height: 32,
                      decoration: BoxDecoration(
                        color: Color(c),
                        shape: BoxShape.circle,
                        border: isSel ? Border.all(color: Colors.white, width: 2.5) : null,
                        boxShadow: isSel
                            ? [
                                BoxShadow(
                                  color: Color(c).withValues(alpha: 0.6),
                                  blurRadius: 6,
                                  spreadRadius: 1,
                                )
                              ]
                            : null,
                      ),
                      child: isSel
                          ? const Icon(Icons.check_rounded, color: Colors.white, size: 16)
                          : null,
                    ),
                  );
                }).toList(),
              ),
              const SizedBox(height: 20),

              // Butonlar
              Row(
                children: [
                  if (widget.initialLesson != null)
                    TextButton.icon(
                      style: TextButton.styleFrom(foregroundColor: Colors.redAccent),
                      icon: const Icon(Icons.delete_outline_rounded, size: 18),
                      label: const Text('Sil'),
                      onPressed: () {
                        Navigator.pop(context, 'DELETE');
                      },
                    ),
                  const Spacer(),
                  TextButton(
                    onPressed: () => Navigator.pop(context),
                    child: const Text('İptal'),
                  ),
                  const SizedBox(width: 8),
                  ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Color(_selectedColor),
                      foregroundColor: Colors.white,
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                      padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 10),
                    ),
                    onPressed: () {
                      final sub = CurriculumRepository.getSubject(_selectedSubjectId);
                      final entry = LessonEntry(
                        id: widget.initialLesson?.id ?? DateTime.now().millisecondsSinceEpoch.toString(),
                        dayOfWeek: _dayOfWeek,
                        periodIndex: _periodIndex,
                        subjectId: _selectedSubjectId,
                        subject: sub.name,
                        grade: _selectedGrade,
                        className: _classNameController.text.trim().isEmpty
                            ? '$_selectedGrade. Sınıf'
                            : _classNameController.text.trim(),
                        classroom: _classroomController.text.trim(),
                        colorValue: _selectedColor,
                        notes: _notesController.text.trim(),
                      );
                      Navigator.pop(context, entry);
                    },
                    child: const Text('Kaydet', style: TextStyle(fontWeight: FontWeight.bold)),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
