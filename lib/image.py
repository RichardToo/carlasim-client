import numpy as np
from carla.libcarla import ColorConverter


def to_rgb_array(image):
    image.convert(ColorConverter.Raw)
    array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
    array = np.reshape(array, (image.height, image.width, 4))
    array = array[:, :, :3]
    array = array[:, :, ::-1]
    return array


def save(image):
    image.save_to_disk('output/%06d.png' % image.frame)
