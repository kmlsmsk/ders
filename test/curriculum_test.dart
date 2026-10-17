import 'package:flutter_test/flutter_test.dart';
import 'package:mufredat_var/data/curriculum_repository.dart';

void main() {
  test('CurriculumRepository loads all 8 subjects correctly', () {
    final subjects = CurriculumRepository.getAllSubjects();
    expect(subjects.length, 8);

    final mat = CurriculumRepository.getSubject('matematik');
    expect(mat.name, 'Matematik');

    final grade7 = mat.getGrade(7);
    expect(grade7.weeks.length, 36);

    // Week 6 is 13-17 Ekim (Rasyonel Sayılarda Karşılaştırma ve Sıralama)
    final week6 = grade7.weeks[5];
    expect(week6.weekNumber, 6);
    expect(week6.outcomes.first.code, 'MAT.7.1.3');
  });

  test('All subjects have valid grade curricula for 5, 6, 7, 8', () {
    final subjects = CurriculumRepository.getAllSubjects();
    for (final sub in subjects) {
      for (final g in [5, 6, 7, 8]) {
        final gc = sub.getGrade(g);
        expect(gc.weeks.length, 36);
      }
    }
  });
}
