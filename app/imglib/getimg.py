import re
import random
from PIL import Image, ImageDraw, ImageFont

LINE_CHAR_COUNT = 20*2 
CHAR_SIZE = 35
TABLE_WIDTH = 5

def line_break(line):
    ret = ''
    width = 0
    for c in line:
        if len(c.encode('utf8')) == 3:  # 中文
            if LINE_CHAR_COUNT == width + 1:  # 剩余位置不够一个汉字
                width = 2
                ret += '\n' + c
            else: # 中文宽度加2，注意换行边界
                width += 2
                ret += c
        else:
            if c == '\t':
                space_c = TABLE_WIDTH - width % TABLE_WIDTH  # 已有长度对TABLE_WIDTH取余
                ret += ' ' * space_c
                width += space_c
            elif c == '\n':
                width = 0
                ret += c
            else:
                width += 1
                ret += c
        if width >= LINE_CHAR_COUNT:
            ret += '\n'
            width = 0
    if ret.endswith('\n'):
        return ret
    return ret + '\n'

def getImg(content,name):
    output_str = content
    output_str = line_break(output_str+'\n')
    d_font = ImageFont.truetype('SourceHanSansCN-VF.ttf', CHAR_SIZE)
    lines = output_str.count('\n')

    image = Image.new("L", (LINE_CHAR_COUNT*CHAR_SIZE // 2, CHAR_SIZE*lines), "white")
    draw_table = ImageDraw.Draw(im=image)
    draw_table.text(xy=(0, 0), text=output_str, fill='#000000', font= d_font, spacing=4)
    #image.save('../../static/tmp/'+name, 'PNG')
    image.save(name,'PNG')
    image.close()

getImg('意大利天文学家朱塞普·皮亚齐在西西里岛的天文台发现位于主小行星带的矮行星谷神星并以刻瑞斯命名，这是第一颗被发现的小行星。','qwq.png')