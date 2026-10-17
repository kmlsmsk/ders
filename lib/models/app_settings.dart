import 'teacher_assignment.dart';

class AppSettings {
  final String teacherName;
  final String schoolName;
  final String teacherTitle; // örn: Matematik Öğretmeni, Zümre Başkanı
  final String activeSubjectId; // 'matematik', 'matematik_bilim', 'turkce', 'fen', 'sosyal', 'ingilizce', 'din', 'bilisim'
  final int activeGrade; // 5, 6, 7, 8
  final bool autoSyncWidget;
  final List<TeacherAssignment> assignedClasses;

  const AppSettings({
    this.teacherName = 'Kemal Öğretmen',
    this.schoolName = 'Ortaokulu',
    this.teacherTitle = 'Matematik Öğretmeni',
    this.activeSubjectId = 'matematik',
    this.activeGrade = 7,
    this.autoSyncWidget = true,
    this.assignedClasses = const [
      TeacherAssignment(id: '1', subjectId: 'matematik', grade: 6, branch: 'A'),
      TeacherAssignment(id: '2', subjectId: 'matematik', grade: 7, branch: 'B'),
      TeacherAssignment(id: '3', subjectId: 'matematik_bilim', grade: 7, branch: 'A'),
    ],
  });

  List<TeacherAssignment> get effectiveAssignedClasses {
    if (assignedClasses.isNotEmpty) return assignedClasses;
    return [
      TeacherAssignment(
        id: 'default',
        subjectId: activeSubjectId,
        grade: activeGrade,
        branch: 'A',
      ),
    ];
  }

  AppSettings copyWith({
    String? teacherName,
    String? schoolName,
    String? teacherTitle,
    String? activeSubjectId,
    int? activeGrade,
    bool? autoSyncWidget,
    List<TeacherAssignment>? assignedClasses,
  }) {
    return AppSettings(
      teacherName: teacherName ?? this.teacherName,
      schoolName: schoolName ?? this.schoolName,
      teacherTitle: teacherTitle ?? this.teacherTitle,
      activeSubjectId: activeSubjectId ?? this.activeSubjectId,
      activeGrade: activeGrade ?? this.activeGrade,
      autoSyncWidget: autoSyncWidget ?? this.autoSyncWidget,
      assignedClasses: assignedClasses ?? this.assignedClasses,
    );
  }

  Map<String, dynamic> toJson() => {
        'teacherName': teacherName,
        'schoolName': schoolName,
        'teacherTitle': teacherTitle,
        'activeSubjectId': activeSubjectId,
        'activeGrade': activeGrade,
        'autoSyncWidget': autoSyncWidget,
        'assignedClasses': assignedClasses.map((e) => e.toJson()).toList(),
      };

  factory AppSettings.fromJson(Map<String, dynamic> json) {
    List<TeacherAssignment> classes = [];
    if (json['assignedClasses'] != null) {
      final list = json['assignedClasses'] as List;
      classes = list
          .map((item) => TeacherAssignment.fromJson(item as Map<String, dynamic>))
          .toList();
    } else {
      classes = const [
        TeacherAssignment(id: '1', subjectId: 'matematik', grade: 6, branch: 'A'),
        TeacherAssignment(id: '2', subjectId: 'matematik', grade: 7, branch: 'B'),
        TeacherAssignment(id: '3', subjectId: 'matematik_bilim', grade: 7, branch: 'A'),
      ];
    }

    return AppSettings(
      teacherName: json['teacherName'] as String? ?? 'Kemal Öğretmen',
      schoolName: json['schoolName'] as String? ?? 'Ortaokulu',
      teacherTitle: json['teacherTitle'] as String? ?? 'Matematik Öğretmeni',
      activeSubjectId: json['activeSubjectId'] as String? ?? 'matematik',
      activeGrade: json['activeGrade'] as int? ?? 7,
      autoSyncWidget: json['autoSyncWidget'] as bool? ?? true,
      assignedClasses: classes,
    );
  }
}
