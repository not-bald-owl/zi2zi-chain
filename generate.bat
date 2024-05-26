@echo off
REM Usage:
REM This batch script is specifically used for creating a TTF font file from generated font images.
REM It is assumed that the font images have already been generated and are ready for processing.

REM Parameters:
REM %1: Project directory name - Specifies the directory where the project is stored.
REM %2: Inference directory - Directory where the inferred font images are saved.
REM %3: Output TTF file name - Name of the output TTF font file, saved in the specified project directory.

REM Check if the correct number of parameters is passed; exit if false.
if "%~3"=="" (
    echo Incorrect number of parameters
    echo Usage: %0 [project directory name] [inference output image directory] [output TTF file name]
    exit /b
)

REM Input parameters
set "full_dir_name=%1"
set "infer_dir=%2"
set "output_ttf_name=%3"

REM Create TTF font file
echo Generating TTF...
echo parameters: %infer_dir% %full_dir_name%%output_ttf_name%.ttf
python .\Generator\src\generator_main.py %infer_dir% %full_dir_name%\%output_ttf_name%.ttf
echo TTF font successfully generated.
