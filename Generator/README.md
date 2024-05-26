# Font-Generator

![example](readme-asset/image.png)

Generate Font from png file:

Name png chracter files in their unicode name, such as "0.png" and "零.png"; put them in source directory, and convert it.

```
FontGenerator
├──fonts          font file output directory
├──images         input image store directory
├──potrace        svg generate software
├──readme-asset   assets
└──src            source code
```

Fast Run:

```sh
python src/main.py ..\\images\\source-directory ..\\fonts\\destination-font-name.ttf
```

## Requirements

To run this program, please install these requirements:

```
opencv-python
pillow
numpy
```

and these software:

### Potrace

unzip the package in `/potrace/installer`, and copy the executable file into `/potrace/bin`.

### FontForge

I really recommand using this program under Linux enviroment. It is inconvinient to use fontforge as a python extention under Windows. 

**update:**

change the method using fontforge to *ffpython*. 

Install fontforge under Windows, add it's bin fold's path into var *PATH*, and enjoy it!

## Parameters

### Functions: preprocess_image, preprocess_image_otsu

- **`enhance(2.0)`**: Enhances image contrast. `2.0` increases contrast; higher values yield more contrast.
- **`medianBlur(img_np, 5)`**: Reduces image noise. `5` is the kernel size; larger values increase smoothness.
- **`adaptiveThreshold(..., 21, 5)`**:
  - `21`: Kernel size for local thresholding; larger values smooth the result.
  - `5`: Constant subtracted from mean or weighted mean in thresholding.
- **`threshold(..., cv2.THRESH_OTSU)`**: Applies Otsu's method to find an optimal threshold value automatically.

### Function: bitmap_to_svg

- **`--opttolerance 0.2`**: Curve optimization tolerance in Potrace. Lower values retain more bitmap details.
- **`--alphamax 3.5`**: Maximum angle for curve smoothing in Potrace. Higher values result in smoother curves.

## License

Apache 2.0