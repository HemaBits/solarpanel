import cv2
import matplotlib.pyplot as plt

image_path = 'dust.png'
original_img = cv2.imread(image_path)

if original_img is None:
    print(f"Error: Could not load image from {image_path}. Check the file path.")
else:
    kernel_size = (41, 41)
    blurred_img = cv2.GaussianBlur(original_img, kernel_size, 0)

    original_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
    blurred_rgb = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(original_rgb)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(blurred_rgb)
    plt.title(f'Gaussian Blurred Image (Kernel: {kernel_size[0]}x{kernel_size[1]})')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
