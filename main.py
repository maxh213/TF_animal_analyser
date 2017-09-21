from Image import Image
import glob

# tbh i should load in a few images at a time rather than all of them
def setup_images():
    url_files = get_animal_url_files()
    images = []
    for url_file in url_files:
        urls = get_image_urls(url_file)
        for url in urls:
            label = get_label_from_filepath(url_file)
            try:
                images.append(Image(url, label))
            except:
                #make it so it doesn't count ctrl c as an exception
                print("unable to retrieve: " + url)
        
    print(images[0].get_label())

def get_image_urls(filepath):
    with open(filepath) as f:
        return f.readlines()

def get_label_from_filepath(filepath):
    filepath = filepath.split("/")[1]
    filepath = filepath.split(".")[0]
    return filepath

def get_animal_url_files():
    return glob.glob("animal_picture_urls/*.txt")

def main():
    setup_images()

if __name__ == '__main__':
    main()

