from PIL import Image
from PIL import ImageFilter
import pytesseract

if __name__ == "__main__":
    image = Image.open('ValidNumber.aspx.gif')
    image = image.convert('RGB')
    image = image.filter(ImageFilter.MedianFilter(3))
    image.save('ValidNumber.jpg')
    jpgImg = Image.open('ValidNumber.jpg')


    code = pytesseract.image_to_string(jpgImg)
    print ('code len: ', len(code))
    print ('code: '+code)
    

