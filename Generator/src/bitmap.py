import os
from PIL import Image

def bitmap_to_svg(bitmap_path, svg_path):
    # print(bitmap_path, svg_path)
    # 转换图像格式为 BMP
    bmp_path = bitmap_path.replace('.png', '.bmp')
    image = Image.open(bitmap_path)
    image.save(bmp_path)

    # 使用 potrace 的优化参数将 BMP 转换为 SVG
    # --opttolerance 0.2
    # 作用：控制曲线优化的容忍度。数值较低时，输出的曲线更忠实于位图的边缘，可能使曲线平滑度较低。
    # --alphamax 3.5
    # 作用：控制输出矢量图像中曲线角的平滑度。数值越高，曲线越平滑（越少棱角）。
    # 参数：最大角度设置，可达最高4.0。
    # --opttolerance 0.4 --alphamax 2.5

    # Windows版本：直接运行下述代码
    os.system(f'.\\Generator\\potrace\\bin\\potrace.exe {bmp_path} -s -o {svg_path}')

    # Linux版本：需要安装potrace（见Generator README），并注册进入路径
    # os.system(f'potrace {bmp_path} -s -o {svg_path}')
