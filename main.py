from Image import Image
from ImageLoader import ImageLoader

def main():
    image_loader = ImageLoader(3)
    images = image_loader.get_next_image_batch()

    print (len(images))
    print (images[0].get_label()) 
    print (images[-1].get_label())
    pink = []
    tiel = []
    for i in images:
        if (i.get_label() == "cockatiel"):
            tiel.append(i)
        elif (i.get_label() == "pink_cockatoo"):
            pink.append(i)
    
    print (len(pink))
    print (len(tiel))
            
        

if __name__ == '__main__':
    main()
