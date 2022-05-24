import os
from PIL import Image, ImageDraw
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen.canvas import Canvas


# 进行裁剪
# 1 inch = 2.54 cm = 25.4 mm = 72 pt
# A4纸张：210 * 279 (mm) = 595.27 * 841.89 (pt)
size = 70  # mm
paper_h = 279
paper_w = 210
img_size = int(72 * size / 25.4)  # pt
draw_frame = False # 是否添加边框
draw_circle = True # 是否剪切圆形
def process_imgs(img):
    w, h = img.size
    if w > h:
        img = img.crop(((w - h) / 2, 0, (w - h) / 2 + h, h))
    else:
        img = img.crop((0, (h - w) / 2, (h - w) / 2 + w, w))
    img = img.resize((img_size, img_size))

    # 绘制吧唧图案边框
    if(draw_frame):
        draw = ImageDraw.Draw(img)
        draw.ellipse(((0, 0), (img_size, img_size)), fill=None, outline=(0, 0, 0), width=2)

    # 将白色图片粘贴到原图形上
    if(draw_circle):
        alpha_layer = Image.new('L', (img_size, img_size), 0)
        draw = ImageDraw.Draw(alpha_layer)
        draw.ellipse((0, 0, img_size, img_size), fill=255)
        # img.putalpha(alpha_layer)
        new_image = Image.new(img.mode, (img_size, img_size), color='white')
        new_image.paste(img, (0, 0), alpha_layer)
        img = new_image

    return img


# 读取所有图片
imgs = []
def read_imgs(dict):
    for filename in os.listdir(r"./" + dict):
        img = Image.open(dict + "/" + filename)
        imgs.append(process_imgs(img))
read_imgs("Images")


# 计算排列方式
border_pt = 20 # pt
padding = 10  # mm
padding_size = int(72 * padding / 25.4)  # pt
row_num = (paper_h - padding) // (size + padding_size)
col_num = (paper_w - padding) // (size + padding_size)


# 生成PDF
def getPDF():
    canvas = Canvas('baji.pdf', pagesize=A4)

    for i in range(0, len(imgs)):
        x = (i % col_num) * img_size
        y = (i // col_num) * img_size
        canvas.drawInlineImage(imgs[i], (i % col_num) * (img_size + padding_size) + border_pt, (i // col_num) * (img_size + padding_size) + border_pt, width=None, height=None)

    canvas.showPage()
    canvas.save()

getPDF()
