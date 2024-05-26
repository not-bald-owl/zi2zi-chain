import argparse
import fontforge
import os

def generate_font(svg_directory, output_font_path):

    base_name = os.path.splitext(output_font_path)[0]

    # 创建新字体对象
    font = fontforge.font()
    font.fontname = base_name
    font.familyname = base_name + " family"
    font.fullname = base_name
    font.encoding = "UnicodeFull"

    # 为所有SVG文件创建字符
    processed_chars = set()
    for svg_filename in os.listdir(svg_directory):
        if svg_filename.endswith('.svg'):
            char = svg_filename.replace('.svg', '')
            char_code = ord(char)
            processed_chars.add(char_code)
            glyph = font.createChar(char_code)
            if not glyph.importOutlines(os.path.join(svg_directory, svg_filename)):
                print(f"Failed to import outlines for {char}")
            # glyph.width = 500
            if glyph.layers[1].isEmpty():
                print(f"Glyph {char} is empty after attempting to import outlines.")


    # log：字符回退功能经实验无法使用

    # # 字符回退，包括中文字符
    # print(os.getcwd())
    # fallback_font = fontforge.open('.\\fonts\\basic\\TimesNewRoman.ttf')  # Times New Roman 路径
    # print("Times New Roman successfully imported")
    # fallback_font_chinese = fontforge.open('.\\fonts\\basic\\STSong.ttf')   # 宋体 路径
    # print("STSong successfully imported")

    # for char in processed_chars:
    #     print(char)

    # # 回退缩放因子
    # SCALE_FACTOR = 0.5

    # for i in range(32, 0x9FFF + 1):
    #     if i not in processed_chars:
    #         # fallback_font_to_use = fallback_font_chinese if 0x4E00 <= i <= 0x9FFF and i in fallback_font_chinese else fallback_font
    #         fallback_font_to_use = fallback_font
    #         if i in fallback_font_to_use:
    #             fallback_font_to_use.selection.select(('unicode',), i)
    #             glyph = fallback_font_to_use.copy()
    #             original_width = fallback_font_to_use[i].width * SCALE_FACTOR
    #             if i in font:
    #                 font.selection.select(('unicode',), i)
    #                 font.paste()
    #                 font[i].width = original_width

    for glyph in font.glyphs():
        glyph.correctDirection()

    # # 检查 ASCII 字符是否回退到了 Times New Roman
    # ascii_fallback_count = 0
    # for i in range(32, 127):
    #     if i not in processed_chars and i in fallback_font:
    #         ascii_fallback_count += 1

    # print(f"Total ASCII characters that fell back to Times New Roman: {ascii_fallback_count}")

    if sum(1 for _ in font.glyphs()) == 0:
        raise Exception("No valid glyphs in font. Cannot generate TTF.")

    font.generate(output_font_path, "ttf")

    # # 调整字符间距
    # font = fontforge.open(output_font_path)
    # font.autoWidth(0, 0, 2048)

    # font.generate(output_font_path, "ttf")

def check_font(file_path):
    font = fontforge.open(file_path)

    # 打印基本信息
    print("Font name:", font.fontname)
    print("Family name:", font.familyname)
    print("Full name:", font.fullname)
    glyph_count = sum(1 for _ in font.glyphs())
    print("Glyph count:", glyph_count)

    # 检查每个字形的基本属性
    for glyph in font.glyphs():
        print("Glyph:", glyph.glyphname, "Unicode:", glyph.unicode)

    # 使用FontForge检验生成字体
    problems = font.validate()
    if problems != 0:
        print("Validation found problems:", problems)
    else:
        print("No validation problems found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate font from svg images.")
    parser.add_argument('svg_directory', type=str, help='Directory containing the svg images')
    parser.add_argument('output_font_path', type=str, help='Output path for the generated font file')
    args = parser.parse_args()
    print(f'Generate Font: ')
    generate_font(args.svg_directory, args.output_font_path)
    check_font(args.output_font_path)