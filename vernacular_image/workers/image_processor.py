from wand.image import Image 
from wand.drawing import Drawing 
from wand.color import Color 
from redis import Redis


redisStore = Redis(host='redis', port=6379, db=1)


class ImageProcessor(object):

    @classmethod
    def create_banner(cls, config, language):
        title = config["title"][language]
        font = config["fonts"][language]
        style = config["style"]
        with Drawing() as draw: 
            with Image(filename='/vernacular_image/asset/{}.png'.format(config["id"])) as image: 
                draw.font = '/vernacular_image/asset/fonts/{}'.format(font)
                draw.font_size = 160
                draw.fill_color = style["fill_color"]
                draw.stroke_color = style["stroke_color"]
                draw.stroke_width = style.get("stroke_width",2)
                draw.text_alignment = "center"
                draw.text(style["x"], style["y"], title) 
                draw(image) 
                filename = "/media/{}_{}.png".format(config["id"], language)
                image.save(filename = filename)
                redisStore.set("idx:{}:{}".format(config["id"], language), filename)
