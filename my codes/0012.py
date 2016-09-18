#coding = utf-8

with open('filtered_words.txt') as f:
	words = f.read().strip().split()

def filter():
	sentence = input('input a sentence: ')
	flag = True
	strs = '**'
	for word in words:
		if word in sentence:
			flag = False
			start = sentence.index(word)
			end = start+len(word)
			break
	if flag:
		print (sentence)
	else:
		print (sentence[:start] + strs + sentence[end:])