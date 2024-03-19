from pathlib import Path
from PIL import Image
import os


HTML_HEADER = '''
<!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="./style.css">

  <title>GALLERY</title>
</head>

<style>
body {
  background-image: url('assets/backgrounds/img_1.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  min-width: 300px;
}

h1 {
  text-align: center;
  font-size: 3em;
  color: rgba(255, 255, 255, 0.8);
  text-shadow: 2px 2px 4px #000000;
  backdrop-filter: blur(5px);
}

div.img-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  margin: 10px;
}

div.img-list .img-wrapper{
  margin: 10px;
  position: relative;
  max-height: 1080px;
  box-shadow: 2px 2px 6px 0px #000000;
  opacity: 0.8;
  transition: all 1s, z-index 0s;
  backdrop-filter: blur(5px);
  z-index: 0;

  @media (max-width: 600px) {
    max-height: 100px;
  }

  @media (max-width: 1200px) {
    max-height: 200px;
  }

  @media (max-width: 1920px) {
    max-height: 400px;
  }

  &:hover {
    opacity: 1;
    transform: scale(1.1);
    box-shadow: 4px 4px 12px 0px #000000;
    z-index: 1;
  }
}
</style>

<body>
'''

HTML_END = '''

</body>

</html>
'''

IMAGE_WRAPPER_START = '''<div class="img-list">'''
IMAGE_WRAPPER_END = '''</div>'''

def get_html_header(header:str='GALLERY'):
  return f'<h1>{header}</h1>'

def get_image_name(idx:int):
  return f'img_{idx}.jpg'

def strip_exif_and_copy(file_path:Path, output_file_path:Path):
  image = Image.open(file_path)

  data = list(image.getdata())
  image_without_exif = Image.new(image.mode, image.size)
  image_without_exif.putdata(data)
    
  image_without_exif.save(output_file_path)
  

  # as a good practice, close the file handler after saving the image.
  image_without_exif.close()

  
def transform_all_images(image_folder:Path, output_folder:Path):
  image_index = 0
  for root, dirs, files in os.walk(image_folder):
    for file in files:
      if file.endswith('.jpg'):
        image_index += 1
        strip_exif_and_copy(os.path.join(root, file), os.path.join(output_folder, get_image_name(image_index)))
  return image_index

def generate_image_html(image_count:int):
  html_snippets = []
  for i in range(1, image_count + 1):
    html_snippets.append(f'<a id="img_1" href="./assets/images/{get_image_name(i)}" target="_blank"><img src="./assets/images/{get_image_name(i)}" class="img-wrapper"></a>')
  return ''.join(html_snippets)

target_folder = Path('./website')
title = 'GALLERY'
image_folder = Path('./images')
background_folder = Path('./backgrounds')
asset_folder = os.path.join(target_folder, 'assets')
images_folder = os.path.join(asset_folder, 'images')
backgrounds_folder = os.path.join(asset_folder, 'backgrounds')

if not os.path.exists(target_folder):
  os.mkdir(target_folder)
if not os.path.exists(asset_folder):
  os.mkdir(asset_folder)
if not os.path.exists(images_folder):
  os.mkdir(images_folder)
if not os.path.exists(backgrounds_folder):
  os.mkdir(backgrounds_folder)

image_count = transform_all_images(image_folder, images_folder)
background_count = transform_all_images(background_folder, backgrounds_folder)

htmls = []
htmls.append(HTML_HEADER)
htmls.append(get_html_header(title))
htmls.append(IMAGE_WRAPPER_START)

htmls.append(generate_image_html(image_count))

htmls.append(IMAGE_WRAPPER_END)

htmls.append(HTML_END)

with open(os.path.join(target_folder, 'index.html'), '+w') as f:
  f.writelines(htmls)