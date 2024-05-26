#!/bin/bash

# 使用说明：
# 本脚本用于运行模型推理，生成字体图片，然后从这些图片创建TTF字体文件。
# 假设已有训练好的模型和必要的文件。
#
# 参数说明：
#   $1: 生成层级（infer）- 控制脚本执行哪些阶段。
#   $2: 项目目录名称 - 指定项目目录。
#   $3: 源字体文件 - 源TTF/OTF字体文件的路径。
#   $4: 推理用文本文件 - 包含用于生成字体图片的文本的文件路径。
#   $5: 推理目录 - 保存推理生成的字体图片的目录。
#   $6: 输出的TTF文件名 - 输出的TTF字体文件的名称，保存在指定的项目目录中。
#   $7: GPU编号 - 指定使用的GPU，例如 "cuda:0"。
#   $8: 模型检查点 - 指定用于推理的模型的检查点。

# 检查传递的参数数量是否正确；如果不正确，则退出。
if [ "$#" -ne 8 ]; then
    echo "参数数量不正确"
    echo "使用方法: $0 [生成层级] [项目目录名称] [源字体] [推理用文本文件] [推理输出图片目录] [输出的TTF文件名] [推理采用模型检查点]"
    exit 1
fi

# 输入参数
genlevel=$1
full_dir_name=$2
src_font=$3
src_txt_file=$4
infer_dir=$5
output_ttf_name=$6
gpu_ids=$7
resume_model=$8

# 仅当生成层级设置为 'infer' 时，运行推理并创建字体
if [ "$genlevel" = "infer" ]; then
  echo "正在运行推理..."
  # 运行推理生成字体图片
  python infer.py --experiment_dir=./$full_dir_name \
                  --gpu_ids=cuda:0 \
                  --batch_size=32 \
                  --resume=$resume_model \
                  --from_txt2 \
                  --src_font=$src_font \
                  --src_txt_file=$src_txt_file \
                  --infer_dir=$infer_dir

  # 创建TTF字体文件
  echo "生成 TTF..."
  python ./Generator/src/main.py $infer_dir ./$full_dir_name/$output_ttf_name.ttf
  echo "TTF字体成功生成。"
fi
