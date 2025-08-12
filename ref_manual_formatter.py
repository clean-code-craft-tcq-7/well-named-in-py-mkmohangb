from color_conversion import get_color_from_pair_number, MAJOR_COLORS, MINOR_COLORS

def md_header():
    return '| Pair Number | Major Color | Minor Color |\n| --- | --- | --- |\n'

def md_format_row(pair_number, major_color, minor_color):
    return f'| {pair_number} | {major_color} | {minor_color} |\n'

def printReferenceManual():
  print('Reference Manual:')
  print(md_header(), end='')
  for i in range(1, len(MAJOR_COLORS) * len(MINOR_COLORS) + 1):
    major_color, minor_color = get_color_from_pair_number(i)
    #print(f'{i}: {color_pair_to_string(major_color, minor_color)}')
    print(md_format_row(i, major_color, minor_color), end='')