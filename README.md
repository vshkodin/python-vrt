
# Visual Regression Testing (VRT) CLI Tool

This CLI tool is designed to help with visual regression testing by comparing images from two directories (`vrt-expected` and `vrt-actual`). It also provides functionality to approve new baseline images.

## Features

- **Initialization**: Create the necessary directories for storing expected and actual images.
- **Comparison**: Compare images in the `vrt-expected` and `vrt-actual` directories and generate a difference image if discrepancies are found.
- **Approval**: Approve actual images and move them to the `vrt-expected` directory, renaming them as required.

## Installation

```bash
pip install vrt_python
```

## Usage

### 1. Initialize Directories

To set up the necessary directories (`vrt-expected` and `vrt-actual`), run:

```bash
vrt init
```

This command will create the following directories:
- `vrt-expected`: Where you store your expected baseline images.
- `vrt-actual`: Where you store the actual images to compare against the baseline.

### 2. Compare Images

To compare images between the `vrt-expected` and `vrt-actual` directories, run:

```bash
vrt compare
```

This command will:
- Compare each image in `vrt-expected` with the corresponding image in `vrt-actual`.
- Generate a difference image in the `vrt-difference` directory if discrepancies are found.
- Print the percentage of difference for each image.

### 3. Approve Actual Images

To approve the actual images and move them to the `vrt-expected` directory, run:

```bash
vrt approve
```

This command will:
- Copy images from the `vrt-actual` directory to the `vrt-expected` directory.
- Rename the images by replacing the `actual_` prefix with `expected_`.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
