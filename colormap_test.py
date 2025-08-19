from color_conversion import get_color_from_pair_number, get_pair_number_from_color 
from ref_manual_formatter import md_header, md_format_row, printReferenceManual, csv_header, csv_format_row

def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = get_color_from_pair_number(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)


def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = get_pair_number_from_color(major_color, minor_color)
  assert(pair_number == expected_pair_number)

def testPrintReferenceManual():
  assert(md_header() == '| Pair Number | Major Color | Minor Color |\n| --- | --- | --- |\n')
  assert(md_format_row(1, 'White', 'Blue') == '| 1 | White | Blue |\n')
  printReferenceManual(md_header, md_format_row)

def testPrintReferenceManualCsv():
  assert(csv_header() == 'Pair Number,Major Color,Minor Color\n')
  assert(csv_format_row(1, 'White', 'Blue') == '1,White,Blue\n')
  printReferenceManual(csv_header, csv_format_row)

if __name__ == '__main__':
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  testPrintReferenceManual()
  testPrintReferenceManualCsv()