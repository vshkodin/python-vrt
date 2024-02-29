from PIL import Image
import numpy as np

class ImageDifference:
    def __init__(self, expectation_path, actual_path):
        self.expectation_path = expectation_path
        self.actual_path = actual_path
        self.img1 = None
        self.img2 = None

    def load_images(self):
        self.img1 = Image.open(self.expectation_path).convert('RGB')
        self.img2 = Image.open(self.actual_path).convert('RGB')
        if self.img1.size != self.img2.size:
            raise ValueError("Images are not the same size.")

    def calculate_difference(self):
        img1_array = np.array(self.img1)
        img2_array = np.array(self.img2)
        diff = np.abs(img1_array - img2_array)
        mask = np.any(diff > 0, axis=-1)
        difference_percentage = (np.sum(mask) / mask.size) * 100
        return mask, difference_percentage

    def apply_overlay(self, mask):
        result_array = np.array(self.img1.copy())
        purple = [128, 0, 128]  # Purple color
        result_array[mask] = purple  # Apply purple overlay where differences are found
        return result_array

    def generate_difference_image(self, difference_path):
        self.load_images()
        mask, difference_percentage = self.calculate_difference()
        print(f"Difference percentage: {difference_percentage:.2f}%")
        result_array = self.apply_overlay(mask)
        result_image = Image.fromarray(result_array)
        result_image.save(difference_path)
        return difference_percentage

# Example usage
if __name__ == "__main__":
    expectation = 'expected_screenshot.png'
    actual = 'actual_screenshot.png'
    difference = 'output_difference.png'

    image_diff = ImageDifference(expectation, actual)
    difference_percentage = image_diff.generate_difference_image(difference)
    print(f"Generated difference image with {difference_percentage:.2f}% difference.")
