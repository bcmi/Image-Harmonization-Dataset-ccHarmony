import polynomial_matching as pm
import cv2
import os

# load polynomial matching coefficient from .npy
m = pm.polyCoeff()

# transform an image
image = cv2.imread('8D5U5531.jpg')
m.read_npy('polynomial_matching_coefficients/8D5U5531.npy')    
transformed = m.transform(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))   # must in RGB color space
output = cv2.cvtColor(transformed, cv2.COLOR_RGB2BGR)
cv2.imwrite('8D5U5531_new.jpg', output)


        