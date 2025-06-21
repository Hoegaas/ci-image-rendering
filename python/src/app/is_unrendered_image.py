import os
import yaml
#image_extensions = []
yaml_filename = "galleryze.yaml"
def read_image_extensions_from_test_yaml(path):
    with open(path, 'r') as f:
        config = yaml.safe_load(f)
    return config.get('image_extensions', [])
def find_galleryze_yaml():
    for path in os.getcwd().rglob(yaml_filename):
        if path is None:
            print("e bi så ferbaina >:C")
            return
        else:
            return read_image_extensions_from_test_yaml(path)
image_extensions = find_galleryze_yaml()
print(image_extensions)