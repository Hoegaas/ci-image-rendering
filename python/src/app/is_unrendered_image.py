import os, yaml
from pathlib import Path
def filter_unsupported_exts(yaml_image_ext, valid_exts):        # helper function for several rounds of filters invalid extensions.
    return list(filter(lambda p:
        p not in valid_exts, yaml_image_ext))
def read_image_extensions(parent_path, valid_image_exts):       # gets all image extensions for the parent working dir
    with open(parent_path, 'r') as f:
        return filter_unsupported_exts(yaml.safe_load(f).get(
            'image_extensions', []),valid_image_exts)
def load_render_targets(path="galleryze.yaml"):                 # parses all the segments related to setting image extensions in yaml
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    filtered_output_exts = filter_unsupported_exts(data.get(
        "render_targets", {}).get("image_extensions", []))
def is_config_yaml(yaml_filename):                              # you only need one parsing func for yaml segments ... (see above)
    for path in os.getcwd().rglob(yaml_filename):
        if path is None:
            return None
        else:
            return path
def create_yaml_render_dictionary(filtered_output_exts):        # sets a dictionary which dicates the algorithm for re-rendering
    return 42
def make_render_output_dir(render_output_dir):                  # creates an output dir in the parent path of the config yaml        
    path = (Path(render_output_dir)
            .mkdir(parents=False, exist_ok=True))
    print(path)
'''
    There are a few functions before rendering:
        getting the path of the yaml if it exists anywhere within the repo
        reading/parsing out different segments in the yaml
        identifying and validating un-renderedn images within the parent dir
        filtering every yaml segment for the supported image extensions
        populating a dictionary for each type of supported rendering
        ...this dictionary is the entire data structure of the script...
        ...pretty much...
'''                                                 