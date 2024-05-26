from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np

def preprocess_image(image_path, output_path):
    # 打开和转换图像为灰度
    img = Image.open(image_path).convert('L')
    # 增强对比度
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)
    # 锐化处理
    img = img.filter(ImageFilter.SHARPEN)
    # 自适应阈值二值化
    img_np = np.array(img)
    img_np = cv2.medianBlur(img_np, 5)
    # 21：局部区域的大小，用于计算每个像素的阈值。数值越大，考虑的像素越多，图像的平滑度越高。
    # 5：从平均值或加权平均值中减去的常数，对边缘锐度和噪声有一定影响
    img_np = cv2.adaptiveThreshold(img_np, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 5)
    img = Image.fromarray(img_np)
    img.save(output_path)

def preprocess_image_otsu(image_path, output_path):
    # print(image_path, output_path)
    # 打开并转换图像为灰度
    img = Image.open(image_path).convert('L')
    # 增强对比度, 参数：2.0 表示将对比度提高两倍，数值越大对比度增强越明显。
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)
    # 锐化处理
    img = img.filter(ImageFilter.SHARPEN)
    # 将PIL图像转换为NumPy数组
    img_np = np.array(img)
    # 使用中值滤波减少噪声, 参数：n 是滤波器的核心大小，表示使用nxn像素区域计算中值。核心尺寸越大，图像越平滑。
    img_np = cv2.medianBlur(img_np, 7)
    # 使用Otsu's阈值方法, 作用：自适应阈值法进行图像二值化，适用于具有不同光照条件的图像。
    _, img_np = cv2.threshold(img_np, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # 将NumPy数组转换回PIL图像
    img = Image.fromarray(img_np)
    img.save(output_path)
