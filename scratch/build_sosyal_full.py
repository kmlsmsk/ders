# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from curriculum_builder import generate_dart_file
from generate_sosyal import build_sosyal_5, build_sosyal_6, build_sosyal_7, build_sosyal_8

g5 = build_sosyal_5()
g6 = build_sosyal_6()
g7 = build_sosyal_7()
g8 = build_sosyal_8()

print("Sosyal week counts:", len(g5['weeks']), len(g6['weeks']), len(g7['weeks']), len(g8['weeks']))
assert len(g5['weeks']) == 36, f"G5: {len(g5['weeks'])}"
assert len(g6['weeks']) == 36, f"G6: {len(g6['weeks'])}"
assert len(g7['weeks']) == 36, f"G7: {len(g7['weeks'])}"
assert len(g8['weeks']) == 36, f"G8: {len(g8['weeks'])}"

grades_data = {
    5: g5,
    6: g6,
    7: g7,
    8: g8,
}

output_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'lib', 'data', 'subjects', 'sosyal_bilgiler_data.dart'
)

generate_dart_file(
    subject_id='sosyal',
    subject_name='Sosyal Bilgiler',
    short_code='SOS',
    description='Birey ve Toplum, Kültür ve Miras, İnsanlar, Yerler ve Çevreler, T.C. İnkılap Tarihi',
    icon_name='public_rounded',
    primary_hex='0xFFD97706',
    accent_hex='0xFFF59E0B',
    grades_data=grades_data,
    output_path=output_path
)

print("Sosyal Bilgiler generated successfully!")
