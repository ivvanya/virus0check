from PIL import Image
from PIL.ExifTags import TAGS


def file_img_info(file) -> str:
    out = str()
    out += "File Information:\n"
    image = Image.open(file)
    info_dict = {
        "File name": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }

    for label, value in info_dict.items():
        out += f"{label:25}: {value}\n"

    exif_data = image.getexif()
    for tag_id in exif_data:
        tag = TAGS.get(tag_id, tag_id)
        data = exif_data.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
        out += f"{tag:25}: {data}\n"

    return out
