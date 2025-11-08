import numpy as np

def calc_efficiency(gray, blur):
    original_brightness = np.mean(gray)
    blur_brightness = np.mean(blur)
    efficiency = (blur_brightness / original_brightness) * 100
    print(f"Estimated Efficiency: {efficiency:.2f}%")
