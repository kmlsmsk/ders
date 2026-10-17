import '../models/curriculum_model.dart';
import 'subjects/matematik_data.dart';
import 'subjects/turkce_data.dart';
import 'subjects/fen_bilimleri_data.dart';
import 'subjects/sosyal_bilgiler_data.dart';
import 'subjects/ingilizce_data.dart';
import 'subjects/din_kulturu_data.dart';
import 'subjects/bilisim_data.dart';
import 'subjects/matematik_bilim_data.dart';

class CurriculumRepository {
  static final Map<String, SubjectCurriculum> _subjects = {
    'matematik': MatematikCurriculum.subject,
    'matematik_bilim': MatematikBilimCurriculum.subject,
    'turkce': TurkceCurriculum.subject,
    'fen': FenBilimleriCurriculum.subject,
    'sosyal': SosyalBilgilerCurriculum.subject,
    'ingilizce': IngilizceCurriculum.subject,
    'din': DinKulturuCurriculum.subject,
    'bilisim': BilisimCurriculum.subject,
  };

  /// Returns all available subjects across middle school
  static List<SubjectCurriculum> getAllSubjects() {
    return _subjects.values.toList();
  }

  /// Get subject by id (defaults to Matematik if not found)
  static SubjectCurriculum getSubject(String subjectId) {
    return _subjects[subjectId] ?? _subjects['matematik']!;
  }

  /// Get grade curriculum for a given subject and grade
  static GradeCurriculum getGradeCurriculum(String subjectId, int grade) {
    final subject = getSubject(subjectId);
    return subject.getGrade(grade);
  }

  /// Compatibility with previous code
  static GradeCurriculum getGrade(int gradeNumber) {
    return getSubject('matematik').getGrade(gradeNumber);
  }

  /// Returns available grades (5, 6, 7, 8)
  static List<int> get availableGrades => [5, 6, 7, 8];

  /// Get current week for given subject and grade
  static CurriculumWeek getCurrentAcademicWeek({
    String subjectId = 'matematik',
    int grade = 7,
    DateTime? date,
  }) {
    final gradeCurriculum = getGradeCurriculum(subjectId, grade);
    return gradeCurriculum.getCurrentWeek(date);
  }
}
