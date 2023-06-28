import asyncio
from utils.image_utils import text2image
from utils.message_builder import image

def msg_merge(my_dict={}, *args):
    
    text = my_dict["msg"]
    text += "\n"
    for arg in args:
        count = 0
        if len(f"{arg}") > 20:
            for i in f"{arg}":
                text += i
                count += 1
                if count % 20 == 0:
                    text += "\n"
        else:       
            text += f"{arg}"
    my_dict["msg"] = text
    return text

async def get_answer(my_dict, bot, event, up_limit):
    msg = my_dict["msg"]
    log = my_dict["log"]
    log += msg
    my_dict["log"] = log
    if msg != "":
        await push_msg(bot, event, msg)
    my_dict["msg"] = ""
    time_count = 0
    condition = True
    while condition and time_count <= 1200:
        await asyncio.sleep(1)
        time_count += 1
        id = my_dict["answer_id"]
        if my_dict["answer"].get(id):
            id += 1
            my_dict["answer_id"] = id
            answer_list = []
            for i in range(up_limit):
                answer_list.append(str(i))
            for i in my_dict["answer"][id - 1]:
                condition = False
                if i not in answer_list:
                    condition = True    
            if condition:
                continue
            text = my_dict["log"]
            text += "\n选择"
            text += my_dict["answer"][id - 1]
            my_dict["log"] = text
            return my_dict["answer"][id - 1]
            
        
        

async def push_msg(bot, event, msg):
    await bot.send(event,image(b64=(await text2image(msg, color="#f9f6f2", padding=10)).pic2bs4()))

async def push_image(my_dict, bot, event, _image):
    msg = my_dict["msg"]
    log = my_dict["log"]
    log += msg
    my_dict["log"] = log
    await push_msg(bot, event, msg)
    my_dict["msg"] = ""
    await bot.send(event,image(b64=_image))