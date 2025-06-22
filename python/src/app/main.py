from is_unrendered_image import find_galleryze_yaml, read_image_extensions
valid_image_exts = ['.svg', '.jpeg', '.jpg', '.png']
#invalid_image_exts_log = []
yaml_name = "galleryze.yaml/"
yaml_path = find_galleryze_yaml(yaml_name)
render_output_dir = yaml_path.parent + "galleryzed-images/"
valid_image_exts = read_image_extensions(
    yaml_path.parent, valid_image_exts)
def main():
    if yaml_path is None:
        print("no file extention in yaml")
        return
    if len(valid_image_exts()) == 0:
        print("no supported image exts in repo")
        return
    print(valid_image_exts)
    print("path: " + yaml_path + 
          "\n parent path: " + yaml_path.parent)
if __name__ == "__main__":
    main()