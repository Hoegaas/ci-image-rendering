'''
    A dictionary, mapped pairs of input_image_ext / output_image exts
        ...This is the on only purposeful data structure for the script...
    We'll start with identifying any one-to-many pairs..
        (PNG -> JPG) - straight forward-ish... however:
        (SVG/PNG -> SVG/PNG/JPEG) involves three modules
            (1) render SVG -> PNG -> JPEG
            (2) render the PNG to PNG
            (3) write the PNG -> SVG
            (4) write the SVG -> SVG
'''
import os, yaml
from pathlib import Path
def find_galleryze_yaml(yaml_filename):
    for path in os.getcwd().rglob(yaml_filename):
        if path is None or len(path) == 0 or path.parent is not os.getcwd():
            return path
        else:
            return None
def filter_supported_exts(yaml_target_ext, valid_exts):
    return len([p for p in yaml_target_ext
            if p in valid_exts])
def read_image_extensions(parent_path, valid_image_exts):
    with open(parent_path, 'r') as f:
        return filter_supported_exts(yaml.safe_load(f).get(
            'image_extensions', []),valid_image_exts)
def create_yaml_render_dictionary(filtered_output_exts):
    return 42
def load_render_targets(path="galleryze.yaml"):
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    filtered_output_exts = filter_supported_exts(data.get(
        "render_targets", {}).get("image_extensions", []))
    dict = create_yaml_render_dictionary(filtered_output_exts)
def make_render_output_dir(render_output_dir):
    path = (Path(render_output_dir).mkdir(parents=False, exist_ok=True))
    print(path)