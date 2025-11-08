from detect_dust import detect_dust
from efficiency_calc import calc_efficiency

# Add your image names
image_list = [
    "images/solar_dusty1.jpg",
    "images/solar_dusty2.jpg",
    "images/solar_dusty3.jpg",
    "images/solar_dusty4.jpg"
]

for image_path in image_list:
    print("\n🟩 Processing:", image_path)
    gray, blur, dust_mask, img = detect_dust(image_path)
    calc_efficiency(gray, blur)
