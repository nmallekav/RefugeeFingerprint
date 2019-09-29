from PIL import Image
import imagehash


def get_hash(filename):
    h = imagehash.average_hash(Image.open(filename))
    return h

#otherhash = imagehash.average_hash(Image.open('other.bmp'))
#print(otherhash)
#print(hash == otherhash)
#print(hash - otherhash)