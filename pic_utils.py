from PIL import Image, ImageDraw, ImageFont
import os
import json
from io import BytesIO
import base64
current_path = os.path.abspath(__file__)
directory = os.path.dirname(current_path)
res_dir = directory + "/resources/"
info_dir = directory + "/bless.json"

def make_card(name : str) -> Image:
    with open(info_dir, "r", encoding= "utf-8") as f:
        info = json.load(f)
    
    additon = ""
    isup = "0"
    if "2" in name:
        additon = "强化"
        isup = "1"
    
    temp = name.split("_")
    star = temp[1]
    mingtu = temp[2]
    title = temp[3]
    content = info[mingtu][title][isup]
    back_card = Image.open(res_dir + f"{star}{additon}.jpg")
    composite_image = Image.new("RGBA", back_card.size)
    composite_image.paste(back_card, (0, 0))
    content = text_warps(content, 14)
    composite_image = add_text_to_image(composite_image, content, (14,160),(190,210),12)
    composite_image = add_text_to_image(composite_image, title, (30,100),(172, 145),12)
    composite_image = add_text_to_image(composite_image, f"「{mingtu}」", (0,232),(202, 275),10, text_color=(0,0,0))
    _image = Image.open(res_dir + f"{mingtu}.png")
    composite_image = paste_image(composite_image, _image, (0,0), (composite_image.size[0] - 2,composite_image.size[1]//2),0.45,1)
    
    return composite_image 

def make_choose_bless_card(bless_list:list, gold):
    background = Image.open(res_dir + "背景.png")
    composite_image = Image.new("RGBA", background.size)
    composite_image.paste(background, (0, 0))
    card_list = []
    for i in bless_list:
        card_list.append(make_card(i))
    num = len(card_list)
    devide_size = background.size[0] // num
    count = 0
    for i in card_list:
        composite_image = paste_image(composite_image, i, (count * devide_size,0), ((count + 1) * devide_size,background.size[1]),0.7 if num > 1 else 0.3,1)
        count += 1
    composite_image = add_text_to_image(composite_image, f"宇宙碎片数量:{gold}", (background.size[0] - 300, 0), (background.size[0], 50), 25)
    composite_image = convert_png_to_jpg_with_lower_quality(composite_image, 75)
    return composite_image
    


def add_text_to_image(image:Image, text, start_coord, end_coord, text_size, text_color=(255,255,255)):
    # 计算文字区域的中心坐标
    text_box_width = end_coord[0] - start_coord[0]
    text_box_height = end_coord[1] - start_coord[1]
    text_box_center = (start_coord[0] + text_box_width // 2, start_coord[1] + text_box_height // 2)

    # 创建一个绘图对象
    draw = ImageDraw.Draw(image)

    # 设置要添加的文字
    font = ImageFont.truetype(res_dir + "yuanshen.ttf", size=text_size)

    # 计算文字的宽度和高度
    text_width, text_height = draw.textsize(text, font=font)

    # 计算文字的起始坐标
    text_start = (text_box_center[0] - text_width // 2, text_box_center[1] - text_height // 2)

    # 在图像上绘制文字
    draw.text(text_start, text, font=font, fill=text_color)

    return image


def paste_image(image, paste_image, start_coord, end_coord, size_ratio, opacity):
    # 计算粘贴区域的中心坐标
    paste_box_width = end_coord[0] - start_coord[0]
    paste_box_height = end_coord[1] - start_coord[1]
    paste_box_center = (start_coord[0] + paste_box_width // 2, start_coord[1] + paste_box_height // 2)

    

    # 计算粘贴图片的大小
    paste_width = int(paste_box_width * size_ratio)
    paste_height = int(paste_box_height * size_ratio)

    # 根据宽度或高度的最大比例进行调整
    max_ratio = max(paste_width / paste_image.width, paste_height / paste_image.height)
    paste_size = (int(paste_image.width * max_ratio), int(paste_image.height * max_ratio))
    paste_image = paste_image.resize(paste_size)

    # 设置透明度
    paste_image = paste_image.convert("RGBA")
    paste_image = paste_image.point(lambda p: p * opacity)

    # 计算粘贴图片的起始坐标
    paste_start = (paste_box_center[0] - paste_size[0] // 2, paste_box_center[1] - paste_size[1] // 2)

    # 在图像上粘贴透明图片
    image.paste(paste_image, paste_start, mask=paste_image)

    return image

def convert_png_to_jpg_with_lower_quality(image, quality):
    # 将PNG图像转换为RGB模式
    rgb_image = image.convert("RGB")

    # 创建新的JPEG图像对象，大小和原图相同
    jpeg_image = Image.new("RGB", image.size)

    # 将RGB图像粘贴到JPEG图像对象中
    jpeg_image.paste(rgb_image, (0, 0))

    # 降低JPEG图像质量并返回图像对象
    
    return jpeg_image


def text_warps(text:str , num: int):
    new_text = ""
    count = 1
    for i in text:
        new_text += i
        if count > 50:
            new_text += "..."
            break
        if count % num == 0:
            new_text += "\n"
        count += 1
    return new_text

def pic2b64(pic: Image) -> str:
    """
    说明:
        PIL图片转base64
    参数:
        :param pic: 通过PIL打开的图片文件
    """
    buf = BytesIO()
    pic.save(buf, format="PNG")
    base64_str = base64.b64encode(buf.getvalue()).decode()
    return "base64://" + base64_str




