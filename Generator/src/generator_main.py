import argparse
import os
from preprocess import preprocess_image, preprocess_image_otsu
from bitmap import bitmap_to_svg

def main(input_dir, output_font_path):
    parent_dir = os.path.dirname(os.path.dirname(input_dir))  # 获取输入目录的上两级目录
    processed_dir = os.path.join(parent_dir, 'processed')  # 在上两级目录中创建 processed 文件夹
    svg_dir = os.path.join(parent_dir, 'char_svg')  # 在上两级目录中创建 char_svg 文件夹
    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(svg_dir, exist_ok=True)

    # 处理输入目录中的所有图像
    for image_filename in os.listdir(input_dir):
        if image_filename.endswith('.png'):
            base_name = os.path.splitext(image_filename)[0]
            processed_image_path = os.path.join(processed_dir, f'{base_name}_processed.png')
            svg_path = os.path.join(svg_dir, f'{base_name}.svg')

            # print(base_name, processed_image_path, svg_path)
            
            # 图像预处理和转换
            # 采用 otsu 方法二值化
            # preprocess_image(os.path.join(input_dir, image_filename), processed_image_path)
            preprocess_image_otsu(os.path.join(input_dir, image_filename), processed_image_path)
            bitmap_to_svg(processed_image_path, svg_path)

    print(svg_dir)
    print(output_font_path)
    
    # 生成字体文件
    os.system(f'ffpython ./Generator/src/generate_font.py {svg_dir} {output_font_path}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate font from images.")
    parser.add_argument('input_dir', type=str, help='Directory containing the images')
    parser.add_argument('output_font_path', type=str, help='Output path for the generated font file')
    args = parser.parse_args()
    main(args.input_dir, args.output_font_path)
