#coding = utf-8
#第 0010 题：使用 Python 生成类似于下图中的字母验证码图片

from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random
import string

#随机字母
def rndChar():
	all_letters = string.ascii_letters + string.digits
	return random.choice(all_letters)

#随机颜色1:填充背景色

def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色3：字母颜色
def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#生成验证码图片
width = 60*4
height = 60
#生成空白图片
image = Image.new('RGB',(width,height),(255,255,255))
#填充背景
#设置字体
font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf',36)
#创建draw对象
draw = ImageDraw.Draw(image)
#填充像素
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill = rndColor())
#填充字母
for t in range(4):
	draw.text((60*t+10,10),rndChar(),font = font,fill = rndColor2())

#模糊处理
image = image.filter(ImageFilter.BLUR)
image.save('captcha.jpg','jpeg')






