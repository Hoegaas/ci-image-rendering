from is_unrendered_image import find_galleryze_yaml,read_image_extensions,make_render_output_dir,load_render_targets
valid_image_exts = ['.svg','.jpeg','.jpg','.png']
yaml_filename = "galleryze.yaml/"
dir_name_rendered_output = "galleryzed-images/"
yaml_path = find_galleryze_yaml(yaml_filename)
render_output_dir = yaml_path.parent + dir_name_rendered_output
valid_image_exts = read_image_extensions(
    yaml_path.parent, valid_image_exts)
valid_render_target_exts = load_render_targets()
def main():
    if yaml_path is None:
        print("no galleryze.yaml")
        return
    if len(valid_image_exts()) == 0:
        print("no supported image exts in repo")
        return
    make_render_output_dir(render_output_dir)
    if len(valid_render_target_exts) == 0:
        print("no output exts set in yaml")
        return
    #print(valid_image_exts)
    print("path: " + yaml_path + 
          "\n parent path: " + yaml_path.parent)
if __name__ == "__main__":
    main()