import pytesseract
import requests
from PIL import Image
from PIL import ImageFilter
import re, datetime
from datetime import datetime

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def process_image(url):
    image = _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)


def _get_image(url):
    return Image.open(url)

def get_date(url):
    sms = process_image(url)
    match = re.search('((\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/ |,|.|-](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/ |,|.|-]\d{2,4})', sms)
    
    count=0
    while True:
        #Year With Century
        try:
            date = datetime.strptime(match.group(),'%d-%m-%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%d/%m/%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%d.%m.%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%Y-%m-%d').date()
            if date != None:
                count=count+1
        except:
            pass
        
        try:
            date = datetime.strptime(match.group(),'%Y/%m/%d').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%Y.%m.%d').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%m-%d-%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%m/%d/%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%m.%d.%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        
        #Decimal Years from Here onwards
        
        try:
            date = datetime.strptime(match.group(),'%d-%m-%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%d/%m/%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%d.%m.%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%y-%m-%d').date()
            if date != None:
                count=count+1
        except:
            pass
        
        try:
            date = datetime.strptime(match.group(),'%y/%m/%d').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%y.%m.%d').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%m-%d-%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%m/%d/%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%m.%d.%y').date()
            if date != None:
                count=count+1
        except:
            pass
        # Abbreviated Months and Years without Century Hereafter
        try:
            date = datetime.strptime(match.group(),'%d-%b-%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%d/%b/%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%d.%b.%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%y-%b-%d').date()
            if date != None:
                count=count+1
        except:
            pass
        
        try:
            date = datetime.strptime(match.group(),'%y/%b/%d').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%y.%b.%d').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%b-%d-%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%b/%d/%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%b.%d.%y').date()
            if date != None:
                count=count+1
        except:
            pass
        # Abbreviated months with Century years
        try:
            date = datetime.strptime(match.group(),'%d-%b-%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%d/%b/%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%d.%b.%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%Y-%b-%d').date()
            if date != None:
                count=count+1
        except:
            pass
        
        try:
            date = datetime.strptime(match.group(),'%Y/%b/%d').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%Y.%b.%d').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%b-%d-%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%b/%d/%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%b.%d.%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        #Full months without century years
        try:
            date = datetime.strptime(match.group(),'%d-%B-%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%d/%B/%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%d.%B.%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%y-%B-%d').date()
            if date != None:
                count=count+1
        except:
            pass
        
        try:
            date = datetime.strptime(match.group(),'%y/%B/%d').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%y.%B.%d').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%B-%d-%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%B/%d/%y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%B.%d.%y').date()
            if date != None:
                count=count+1
        except:
            pass
        #Full months with century years
        try:
            date = datetime.strptime(match.group(),'%d-%B-%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%d/%B/%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%d.%B.%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%Y-%B-%d').date()
            if date != None:
                count=count+1
        except:
            pass
        
        try:
            date = datetime.strptime(match.group(),'%Y/%B/%d').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%Y.%B.%d').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%B-%d-%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%B/%d/%Y').date()
            if date != None:
                count=count+1
        except:
            pass
        try:
            date = datetime.strptime(match.group(),'%B.%d.%Y').date()
            if date != None:
                count=count+1            
        except:
            pass
        #Breaking the While Loop Here
        if count > 0:
            break
        elif count == 0:
            date = 'Null'
            break
    return date
