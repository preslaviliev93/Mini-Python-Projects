"""
This script will extract meta data from images

"""
from PIL import Image
from PIL.ExifTags import TAGS


class ExifExtractor:
    def __init__(self, image_path):
        self.image_path = image_path

    def extract_data(self):
        image = Image.open(self.image_path)
        exif_data = image.getexif()
        if exif_data:
            metadata = {}

            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                metadata[tag_name] = value
            return metadata
        return f'Error or no meta data found for {self.image_path}'


img_path = ''
meta_extractor = ExifExtractor(img_path)
data = meta_extractor.extract_data()
for k, v in data.items():
    print(f'{k} -> {v}')
