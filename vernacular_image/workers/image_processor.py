from wand.image import Image
from wand.display import display

class ImageProcessor(object):

    @classmethod
    def create_banner(cls, x, y):
        with Image(filename='/vernacular_image/workers/lisa.jpg') as img:
            print(img.size)
            for r in 1, 2, 3:
                with img.clone() as i:
                    i.resize(int(i.width * r * 0.25), int(i.height * r * 0.25))
                    i.rotate(90 * r)
                    i.save(filename='lisa-{0}.jpg'.format(r))
        return x+y