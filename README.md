# Gallery Builder

This is ... well just a couple files, but they are able to create a website presenting all your awesome images.

## Usage

Your python environment needs `pillow` to be installed.

For example you can use the pyproject.toml and poetry:

```bash
poetry update --no-root
```

In the Notebook build_gallery.ipynb you need to select the valid python environment with pillow being installed.

When you run the notebook, you get asked if you want to select the folders. You can do so, or you can add a `config.py` file on the root level of the repository with the following content instead:

```python
from pathlib import Path

target_folder = Path('/path/to/my/website/folder')
input_image_folder = Path('/path/to/folder/with/all/images') # Currently only supports jpg files
background_folder = Path('/path/to/folder/with/all/backgrounds') # Currently only uses the first one; supports jpg files
video_folder = Path('/path/to/folder/with/all/videos') # Currently only supports .mov files
```

The output is a folder (`target_folder`) containing html files and an assets folder containing the images.  
All images no longer contain any exif information. In the internet that might be a wise thing to do.  
You can use the content of the folder as a website or even as part of a website as long as you do not alter the structure within said folder.

Due to the javascript used to fetch the media, you need to run the website as server and can not open the html files with your browser for the same experience.

### Ordering

Currently the ordering of files is kind of stupid, if you want to modify the resulted order, you can do so within the folder `website/assets/data/media.json`

## Features

### Gallery Pages

All Images and Videos get listed on some sort of a poster wall.

Each image and video element also gets a html id equal to the file name within the asset folder, e.g. `img_1`.  
This enables you to create links to a specific images, e.g. `my-web.site/sorted#img_42`

The sorted page uses the order from `website/assets/data/media.json`, the shuffled page shuffles the order on page load or refresh.

### Reels

All Images and Videos get listed in a feed similar to YouTube shorts, TikTok or Instagram Reels.  

For videos to autoplay you need to click on the screen once so that your browser allows autoplay.

The sorted page uses the order from `website/assets/data/media.json`, the shuffled page shuffles the order on page load or refresh.
