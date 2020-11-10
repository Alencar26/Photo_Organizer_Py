import os
import shutil
from datetime import datetime
from PIL import Image

extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']

def folde_path_from_photo_date(file):
    date = photo_shooting_date(file)
    return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')

def photo_shooting_date(file):
    photo = Image.open(file)
    info = photo._getexif()
    if 36867 in info:
        date = info[36867]
        date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
    else:
        date = datetime.fromtimestamp(os.path.getmtime(file))
    return date

def move_photo(file):
    new_folder = folde_path_from_photo_date(file)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    shutil.move(file, new_folder + '/' + file)

def organize():
    photos = [
        filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in extensions)
    ]
    for filename in photos:
        move_photo(filename)

print(organize())