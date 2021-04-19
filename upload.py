import os
import json
from django.db.models.fields import files
import requests


def Main():
    rootdir = 'C:/Users/brian/Desktop/galleries'

    jsondir = 'C:/Users/brian/Documents/Code/dokasphotos.com/public/photos.json'

    vault_url = 'http://127.0.0.1:8000/upload/'

    jsondata = json.load(open(jsondir))

    galleries = os.listdir(rootdir)

    i = -1
    for subdir, dirs, files in os.walk(rootdir):
        if i == -1:
            i += 1
            continue
        print(f'\nGallery: {galleries[i]}')

        for file in files:
            for photodata in jsondata[galleries[i]]:
                if file == photodata['img']+".jpg":
                    name = photodata['name']
                    gallery = galleries[i]
                    img = photodata['img']+'.jpg'
                    print(f'Gallery: {gallery}, Name: {name}, IMG: {img}')
                    file_dir = os.path.join(subdir, img)
                    print(f'File: {file_dir}')
                    post = requests.post(vault_url, headers={'access-token': 'zz+5^jas@(u42%^$ptyol!$47w*18*!2p*t=r!n9+mchtzdm%z'}, data={'name': name, 'gallery': gallery}, files={'file': open(file_dir, 'rb')})
                    print(post.status_code)                    
            #         break
            #     break
            # break
        i += 1


if __name__ == "__main__":
    # post = requests.post('http://15.222.77.108:8000/upload/', headers={'access-token': 'zz+5^jas@(u42%^$ptyol!$47w*18*!2p*t=r!n9+mchtzdm%z'}, data={'name': 'TEST_NAME1', 'gallery': 'TEST_GALLERY'}, files={'file': open('C:/Users/brian/Desktop/galleries\zion\Valley-Floor.jpg', 'rb')})
    # print(post.text)
    Main()

