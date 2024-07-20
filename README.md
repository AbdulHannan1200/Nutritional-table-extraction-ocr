# Nutrition Table OCR

This project uses the OCR technique to detect and extract text from images of nutrition tables. It includes functionality to correct image tilt and more pre-processing steps, merge horizontally aligned text boxes into single rows, and integrate with FastAPI for a seamless API experience.

## Features

- Detect and extract text from images using PaddleOCR.
- Correct image tilt to ensure tabular data is aligned along the x-axis and y-axis.
- Merge text boxes that are aligned horizontally.
- Provide text and confidence scores for each merged box.
- Integrated with FastAPI for easy API access.

## Requirements

- Python 3.7+
- PaddleOCR
- FastAPI
- OpenCV
- Pillow
- Numpy

# Installation

## 1. Clone the repository:
- git clone https://github.com/AbdulHannan1200/Nutritional-table-extraction-ocr.git
- cd Nutritional-table-extraction-ocr

## 2. Create & activate a virtual environment:
conda create --name nutrition python=3.7
conda activate nutrition

## 3. Install the required packages:
pip install -r requirements.txt

# Usage
## Running the FastAPI server

### Start the FastAPI server:
uvicorn app:app --reload

The API will be accessible at <b>http://0.0.0.0:8003/</b>.

### API Endpoints
The API document will be accessible at <b>http://0.0.0.0:8003/docs/</b>.

# Contributing

- Fork the repository.
- Create a new branch: git checkout -b my-new-feature.
- Commit your changes: git commit -am 'Add some feature'.
- Push to the branch: git push origin my-new-feature.
- Submit a pull request.

# Acknowledgments

- PaddleOCR -> https://github.com/PaddlePaddle/PaddleOCR
- FastAPI -> https://github.com/tiangolo/fastapi
