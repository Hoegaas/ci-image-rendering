from yaml_filename_validation import find_file_in_repo
from is_unrendered_image import find_repo_image_files
def main():
    result = find_file_in_repo()
    print(result)
    find_repo_image_files()
if __name__ == "__main__":
    main()