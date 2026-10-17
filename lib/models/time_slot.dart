import 'package:flutter/material.dart';

class TimeSlot {
  final int periodIndex; // 1, 2, 3...
  final String label; // "1. Ders", "2. Ders"
  final String startTime; // "09:00"
  final String endTime; // "09:40"
  final bool isBreak;

  const TimeSlot({
    required this.periodIndex,
    required this.label,
    required this.startTime,
    required this.endTime,
    this.isBreak = false,
  });

  TimeOfDay get startHourMinute {
    final parts = startTime.split(':');
    return TimeOfDay(
      hour: int.tryParse(parts[0]) ?? 8,
      minute: int.tryParse(parts[1]) ?? 30,
    );
  }

  TimeOfDay get endHourMinute {
    final parts = endTime.split(':');
    return TimeOfDay(
      hour: int.tryParse(parts[0]) ?? 9,
      minute: int.tryParse(parts[1]) ?? 10,
    );
  }

  int get startMinutesSinceMidnight =>
      startHourMinute.hour * 60 + startHourMinute.minute;

  int get endMinutesSinceMidnight =>
      endHourMinute.hour * 60 + endHourMinute.minute;

  Map<String, dynamic> toJson() => {
        'periodIndex': periodIndex,
        'label': label,
        'startTime': startTime,
        'endTime': endTime,
        'isBreak': isBreak,
      };

  factory TimeSlot.fromJson(Map<String, dynamic> json) => TimeSlot(
        periodIndex: json['periodIndex'] as int,
        label: json['label'] as String,
        startTime: json['startTime'] as String,
        endTime: json['endTime'] as String,
        isBreak: json['isBreak'] as bool? ?? false,
      );

  TimeSlot copyWith({
    int? periodIndex,
    String? label,
    String? startTime,
    String? endTime,
    bool? isBreak,
  }) =>
      TimeSlot(
        periodIndex: periodIndex ?? this.periodIndex,
        label: label ?? this.label,
        startTime: startTime ?? this.startTime,
        endTime: endTime ?? this.endTime,
        isBreak: isBreak ?? this.isBreak,
      );

  static List<TimeSlot> defaultStandardSlots() {
    return [
      const TimeSlot(periodIndex: 1, label: '1. Ders', startTime: '09:00', endTime: '09:40'),
      const TimeSlot(periodIndex: 2, label: '2. Ders', startTime: '09:50', endTime: '10:30'),
      const TimeSlot(periodIndex: 3, label: '3. Ders', startTime: '10:40', endTime: '11:20'),
      const TimeSlot(periodIndex: 4, label: '4. Ders', startTime: '11:30', endTime: '12:10'),
      const TimeSlot(periodIndex: 5, label: '5. Ders', startTime: '13:00', endTime: '13:40'),
      const TimeSlot(periodIndex: 6, label: '6. Ders', startTime: '13:50', endTime: '14:30'),
      const TimeSlot(periodIndex: 7, label: '7. Ders', startTime: '14:40', endTime: '15:20'),
    ];
  }
}
