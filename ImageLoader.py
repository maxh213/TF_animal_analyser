import glob
from Image import Image

class ImageLoader(object): 
    def __init__(self, image_batch_size_for_each_class):
        self.images_loaded = 0
        self.image_batch_size_for_each_class = image_batch_size_for_each_class
        self.class_urls, self.class_labels = self.get_urls_and_labels_for_each_class()

    def increment_images_loaded(self, amount=1):
        self.images_loaded += amount

    def set_image_batch_size_for_each_class(self, image_batch_size_for_each_class):
        self.image_batch_size_for_each_class = image_batch_size_for_each_class

    def get_image_urls(self, filepath):
        with open(filepath) as f:
            return f.readlines()

    def get_label_from_filepath(self, filepath):
        filepath = filepath.split("/")[1]
        filepath = filepath.split(".")[0]
        return filepath        

    def get_url_files(self):
        return glob.glob("animal_picture_urls/*.txt")

    def get_urls_and_labels_for_each_class(self):
        """I realise this breaks the single responsibility principle but it's more efficient!"""
        class_urls = [] 
        class_labels = []
        url_files = self.get_url_files()
        for url_file in url_files:
            class_urls.append(self.get_image_urls(url_file))
            class_labels.append(self.get_label_from_filepath(url_file))
        return class_urls, class_labels

    def get_next_image_batch(self):
        images = []
        for class_url, class_label in zip(self.class_urls, self.class_labels):
            for i in range(self.images_loaded, self.image_batch_size_for_each_class):
                try:
                    images.append(Image(class_url[i], class_label))
                except KeyboardInterrupt:
                    raise
                except:
                    print ("unable to retrieve: " + class_url[i])
        self.increment_images_loaded(self.image_batch_size_for_each_class)
        return images
