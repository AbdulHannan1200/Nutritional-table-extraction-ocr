import os, os.path
import glob
import numpy as np
import cv2

from app.Modules.ImagePreProcessingModule.pre_processing import Preprocess_nutrition_label_with_adjustments
from app.Modules.OcrModule.ocr import Detect_text_pil_1_row
from app.Modules.PostProcessingModule.post_processing import Get_llama_respone

BASE_PATH = os.getcwd()
print("BASE_PATH", BASE_PATH)
directory_path = BASE_PATH + "/app/Database/Images_Data/"

def Parent_Func(input_image_path):

    im_show, merged_texts = Detect_text_pil_1_row(input_image_path)

    print("List Of Strings:", merged_texts)

    result_json = Get_llama_respone(merged_texts)
    result_json = eval(result_json)

    result_data = result_json["data"]

    return result_data

def Get_img_path():

    total_pngs = len(glob.glob(f"{directory_path}*.png"))
    print("Current PNGs in folder:", total_pngs)

    img_counter = total_pngs + 1
    image_path = directory_path + f"{img_counter}.png"
    return image_path

def Save_img_file(image):
    try:
        file = image.file.read()
        nparr = np.fromstring(file, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        print("shape ",img.shape)
        
        image_path = Get_img_path()

        cv2.imwrite(image_path, img)
        return True, image_path
    
    except Exception as e:
        print('Exception in save_img_file', e)
        return False, None