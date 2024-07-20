import cv2
from paddleocr import PaddleOCR,draw_ocr
from PIL import Image, ImageDraw, ImageFont
import os, os.path

BASE_PATH = os.getcwd()
print("BASE_PATH", BASE_PATH)
font_path = BASE_PATH + "/app/Modules/OcrModule/Roboto-Regular.ttf"

# font_path = '/media/hannan/New Volume/D/Nutrition_Table_OCR/FastApi-Server/app/Modules/OcrModule/Roboto-Regular.ttf'

ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=False)# need to run only once to download and load model into memory


def merge_boxes_texts(boxes, texts, scores, threshold=10):
    """
    Merge boxes that have approximately the same y-axis values,
    and concatenate the texts and average the scores.
    """
    merged_boxes = []
    merged_texts = []
    merged_scores = []
    
    current_box = boxes[0]
    current_text = texts[0]
    current_scores = [scores[0]]
    
    for i in range(1, len(boxes)):
        box = boxes[i]
        if abs(current_box[0][1] - box[0][1]) < threshold:  # Check if y-values are close
            # Merge boxes horizontally
            current_box[0][0] = min(current_box[0][0], box[0][0])
            current_box[1][0] = max(current_box[1][0], box[1][0])
            current_box[2][0] = max(current_box[2][0], box[2][0])
            current_box[3][0] = min(current_box[3][0], box[3][0])
            # Concatenate texts and append scores
            current_text += " " + texts[i]
            current_scores.append(scores[i])
        else:
            merged_boxes.append(current_box)
            merged_texts.append(current_text)
            merged_scores.append(sum(current_scores) / len(current_scores))  # Average score
            current_box = box
            current_text = texts[i]
            current_scores = [scores[i]]
    
    # Append the last merged box
    merged_boxes.append(current_box)
    merged_texts.append(current_text)
    merged_scores.append(sum(current_scores) / len(current_scores))
    
    return merged_boxes, merged_texts, merged_scores
    
def Detect_text_pil_1_row(image_path):

    print("Image Path, going for OCR", image_path)

    result = ocr.ocr(image_path, cls=True)

    image = Image.open(image_path).convert('RGB')

    # Draw result
    boxes = [line[0] for line in result[0]]
    txts = [line[1][0] for line in result[0]]
    scores = [line[1][1] for line in result[0]]

    # Sort boxes by y-axis (top-left corner)
    boxes = sorted(boxes, key=lambda box: box[0][1])

    # Merge boxes with similar y-axis values and concatenate texts and scores
    merged_boxes, merged_texts, merged_scores = merge_boxes_texts(boxes, txts, scores)

    print("YAHA TAK AGYA")

    im_show = draw_ocr(image, merged_boxes, merged_texts, merged_scores, font_path=font_path)
    im_show = Image.fromarray(im_show)
    im_show.save('result.jpg')

    print("Image save hogae")


    for line in zip(merged_boxes, merged_texts, merged_scores):
        print(line)

    return im_show, merged_texts

# im_show, merged_texts = Detect_text_pil_1_row('1.png')