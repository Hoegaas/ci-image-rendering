import os
import yaml
def find_galleryze_yaml(yaml_filename):
    for path in os.getcwd().rglob(yaml_filename):
        if path is None or len(path) == 0 and path.parent is not os.getcwd():
            return path
        else:
            return None
def filter_supported_exts(any_image_ext, valid_image_exts):
    return len([p for p in any_image_ext
            if p in valid_image_exts])
def read_image_extensions(parent_path, valid_image_exts):
    with open(parent_path, 'r') as f:
        return filter_supported_exts(yaml.safe_load(f).get(
            'image_extensions', []),valid_image_exts)