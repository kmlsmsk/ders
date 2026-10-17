import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:mufredat_var/main.dart';
import 'package:mufredat_var/services/settings_service.dart';
import 'package:mufredat_var/services/timetable_service.dart';

void main() {
  setUp(() async {
    TestWidgetsFlutterBinding.ensureInitialized();
    GoogleFonts.config.allowRuntimeFetching = false;
    SharedPreferences.setMockInitialValues({});
    await SettingsService.init();
    await TimetableService.init();
    TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
        .setMockMethodCallHandler(
      const MethodChannel('home_widget'),
      (MethodCall methodCall) async => true,
    );
  });

  testWidgets('App renders correctly and displays navigation tabs, timetable, and curriculum', (WidgetTester tester) async {
    await tester.pumpWidget(const MufredatVarApp(initialDarkMode: false));
    await tester.pumpAndSettle();

    // Verify navigation tabs (4 tabs: Müfredat, Program, Dersler, Ayarlar)
    expect(find.text('Müfredat'), findsAtLeastNWidgets(1));
    expect(find.byIcon(Icons.calendar_month_rounded), findsAtLeastNWidgets(1));
    expect(find.byIcon(Icons.grid_view_rounded), findsAtLeastNWidgets(1));
    expect(find.byIcon(Icons.tune_rounded), findsAtLeastNWidgets(1));

    // Verify Teacher Personalization Greeting
    expect(find.textContaining('İyi Dersler'), findsAtLeastNWidgets(1));

    // Verify Teacher Multi-Class Dashboard Section
    expect(find.text('GİRDİĞİM DERSLER & SINIFLAR'), findsAtLeastNWidgets(1));

    // Verify Grade pills with Maarif sparkle
    expect(find.text('7. Sınıf ✨'), findsAtLeastNWidgets(1));
  });
}
