# ProcessDigital

**ProcessDigital** is a project focused on image processing for breast cancer detection. This repository contains scripts to separate RGB channels from images.

## How It Works

1. **Separate RGB Channels**: The script extracts red, green, and blue channels from input images.
2. **Input Images**: Place your PNG images in the `input_images` directory.
3. **Output Images**: After running the script, processed images will be saved in the `output_images` directory.

## Usage

### Steps to Run

1. Ensure you have the required libraries installed. Use:

   ```bash
   pip install -r requirements.txt
   ```

2. Update the image names in `separate_channels.py` to match your input images.
3. Run the script:

   ```bash
   python src/preprocessing/separate_channels.py
   ```

## Output

The output will include images for each channel, saved as `img1_red.png`, `img1_green.png`, and `img1_blue.png`, etc.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.
