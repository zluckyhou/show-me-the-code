#coding=utf-8
#第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里![http://tieba.baidu.com/p/2166231880]日本妹子图片 :-)

import requests
from bs4 import BeautifulSoup
import os

url = 'http://tieba.baidu.com/p/2166231880'

def download_url(url):
	#获取网页内容
	html = requests.get(url).content.decode('utf-8')

def get_pictures(url):
	html = download_url(url)
	#解析网页
	soup = BeautifulSoup(html,'lxml')

	#获取图片链接,要下载的图片在评论中，所以首先获取评论内容
	groups = soup.find_all('div',attrs = {'class':'d_post_content j_d_post_content  clearfix'})

	#有些评论里只有文字，没有图片链接，这种评论很容易排除，有些评论中有表情，而表情也是放在链接中的，这类链接需要特别处理

	pictures = []
	for group in groups:
		picture = []
		links = group.find_all('img')
		if len(links) > 5:
			for link in links:
				picture.append(link['src'])
		pictures.extend(picture)

	#只提取后缀是.jpg的链接
	pictures = [picture for picture in pictures if os.path.splitext(picture)[1] == '.jpg']

	for i in range(len(pictures)):
		r = requests.get(pictures[i])
		image = r.content
		with open('meizi_{}.jpg'.format(i),'wb') as f:
			f.write(image)

if __name__ == '__main__':
	get_pictures()



