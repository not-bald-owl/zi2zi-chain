@echo off
REM Usage:
REM This batch script is used for running model inference to generate font images and then creates a TTF font file from those images.
REM It assumes that a trained model and necessary files are already available.

REM Parameters:
REM %1: Generation level (infer) - Controls the stages to execute in this script.
REM %2: Project directory name - Specifies the project directory.
REM %3: Source font file - Path to the source TTF/OTF font file.
REM %4: Text file for inference - Path to the text file containing text for generating font images.
REM %5: Inference directory - Directory where the inferred font images will be saved.
REM %6: Output TTF file name - Name of the output TTF font file, saved in the specified project directory.
REM %7: GPU IDs - Specifies the GPU to be used, for example, "cuda:0".
REM %8: Model checkpoint - Specifies the checkpoint of the model to use for inference.

REM Check if the correct number of parameters is passed; exit if false.
if "%~8"=="" (
    echo Incorrect number of parameters
    echo Usage: %0 [generation level] [project directory name] [source font] [text file for inference] [inference output image directory] [output TTF file name] [GPU IDs] [model checkpoint]
    exit /b
)

REM Input parameters
set "genlevel=%1"
set "full_dir_name=%2"
set "src_font=%3"
set "src_txt_file=%4"
set "infer_dir=%5"
set "output_ttf_name=%6"
set "gpu_ids=%7"
set "resume_model=%8"

REM Only run inference and create the font if the generation level is set to 'infer'
if "%genlevel%"=="infer" (
    echo Running inference...
    REM Run inference to generate font images
    python infer.py --experiment_dir=./%full_dir_name% ^
                    --gpu_ids=%gpu_ids% ^
                    --batch_size=32 ^
                    --resume=%resume_model% ^
                    --from_txt2 ^
                    --src_font=%src_font% ^
                    --src_txt_file=%src_txt_file% ^
                    --infer_dir=%infer_dir%

    REM Create TTF font file
    echo Generating TTF...
    echo parameters: %infer_dir% %full_dir_name%\%output_ttf_name%.ttf
    python .\Generator\src\main.py %infer_dir% %full_dir_name%\%output_ttf_name%.ttf
    echo TTF font successfully generated.
)
