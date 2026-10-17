# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from curriculum_builder import generate_dart_file
from generate_turkce_5 import build_turkce_5
from generate_turkce_6 import build_turkce_6
from generate_turkce_7 import build_turkce_7
from generate_turkce_8 import build_turkce_8

grades_data = {
    5: build_turkce_5(),
    6: build_turkce_6(),
    7: build_turkce_7(),
    8: build_turkce_8(),
}

output_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'lib', 'data', 'subjects', 'turkce_data.dart'
)

generate_dart_file(
    subject_id='turkce',
    subject_name='Türkçe',
    short_code='TÜR',
    description='Okuma Anlama, Söz Varlığı, Dil Bilgisi, Yazma Becerileri ve Edebî Metinler',
    icon_name='menu_book_rounded',
    primary_hex='0xFFE11D48',
    accent_hex='0xFFF43F5E',
    grades_data=grades_data,
    output_path=output_path
)

print("Türkçe generated successfully!")
