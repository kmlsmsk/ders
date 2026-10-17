# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from curriculum_builder import generate_dart_file
from generate_fen_data import build_fen_5
from generate_fen_6 import build_fen_6
from generate_fen_7 import build_fen_7
from generate_fen_8 import build_fen_8

grades_data = {
    5: build_fen_5(),
    6: build_fen_6(),
    7: build_fen_7(),
    8: build_fen_8(),
}

output_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'lib', 'data', 'subjects', 'fen_bilimleri_data.dart'
)

generate_dart_file(
    subject_id='fen',
    subject_name='Fen Bilimleri',
    short_code='FEN',
    description='Dünya ve Evren, Canlılar ve Yaşam, Madde ve Doğası, Fiziksel Olaylar, Çevre',
    icon_name='science_rounded',
    primary_hex='0xFF0D9488',
    accent_hex='0xFF14B8A6',
    grades_data=grades_data,
    output_path=output_path
)

print("Fen Bilimleri generated successfully!")
