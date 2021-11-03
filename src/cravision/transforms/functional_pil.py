from PIL import Image

from typing import (
    Any,
    List,
)


def _is_pil_image(img: Any) -> bool:
    return isinstance(img, Image.Image)


def get_image_size(img: Any) -> List[int]:
    if _is_pil_image(img):
        return list(img.size)
    raise TypeError(f"Unexpected type{type(img)}")


def get_image_num_channels(img: Any) -> int:
    if _is_pil_image(img):
        if img.mode == '1' or img.mode == 'L':
            return 1
        elif img.mode == 'RGB' or img.mode == 'LAB' or img.mode == 'HSV':
            return 3
        elif img.mode == 'RGBA' or img.mode == 'CMYK' or img.mode == 'YCbCr':
            return 4
        else:
            raise TypeError(f"Unsupported mode of Image.Image {img.mode}")
    raise TypeError(f"Unexpected type{type(img)}")
