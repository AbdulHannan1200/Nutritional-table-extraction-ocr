import cv2
import numpy as np
from skimage import restoration


def adjust_brightness_contrast(image, brightness=0, contrast=0):
    beta = brightness
    alpha = 131 * (contrast + 127) / (127 * (131 - contrast))
    return cv2.addWeighted(image, alpha, image, 0, beta)

def Preprocess_nutrition_label_with_adjustments(image_path):
    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_result = clahe.apply(image)
    
    # Apply brightness and contrast adjustment
    adjusted = adjust_brightness_contrast(clahe_result, brightness=10, contrast=30)
    
    return adjusted

# preprocessed_image  = Preprocess_nutrition_label_with_adjustments('1.png')
# cv2.imshow('Preprocessed Image', preprocessed_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()