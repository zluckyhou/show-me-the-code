#codint = utf-8
#第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import string
import random
all_letters = string.ascii_uppercase + string.digits
def get_code():
	code = ''
	for i in range(10):
		code += random.choice(all_letters)
	return code

codes = set()
while i<200:
	code = get_code()
	if code not in codes:
		codes.add(code)
		i +=1
		print (code)

