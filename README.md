```markdown
# ProcessDigital

This repository contains scripts for image processing tasks related to breast cancer detection and analysis.

## Requirements

Make sure to install the necessary dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

### Separate Channels

To separate the RGB channels of an image, use the `separate_channels.py` script.

1. Place your input images in the `input_images` directory.
2. Update the `image_names` list in `separate_channels.py` to match your image filenames (without the extension).
3. Run the script:

```bash
python src/preprocessing/separate_channels.py
```

### Output

The processed images will be saved in the `output_images` directory. Each channel will be saved as a separate PNG file (e.g., `img1_red.png`, `img1_green.png`, `img1_blue.png`).

## Contributing

Feel free to submit issues or pull requests if you have improvements or suggestions!