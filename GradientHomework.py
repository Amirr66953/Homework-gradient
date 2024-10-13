import numpy as np
from PIL import Image

def create_gradient_image(point1, point2, size=(220, 220)):
    x1, y1 = point1
    x2, y2 = point2
    gradient = np.zeros((size[0], size[1], 3), dtype=np.uint8)
    
    for y in range(size[0]):
        for x in range(size[1]):
            ratio = ((x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)) / ((x2 - x1)**2 + (y2 - y1)**2)
            ratio = max(0, min(1, ratio))
            new_color = (1 - ratio) * np.array(color_left) + ratio * np.array(color_right)
            gradient[y, x] = new_color
            
    image = Image.fromarray(gradient)
    return image

color_left = (0, 255, 0)
color_right = (255, 255, 255)
point1 = (0,0)
point2 = (219,219)
gradient_image = create_gradient_image(point1, point2)
gradient_image.save('gradient_image.png')
gradient_image.show()
