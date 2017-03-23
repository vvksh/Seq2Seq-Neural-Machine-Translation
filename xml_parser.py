import xml.etree.ElementTree as ET



def populate_en_fr_dic(): 
	dic = {}
	tree = ET.parse('eng-fra.tei')
	root = tree.getroot()
	text=root[1]
	body = text[0]
	print(body)
	for entry in body:
		english = entry[0][0].text
		try:

			french = entry[-1][0][0].text
			print(french)
			dic[english] = french
		except:
			print("HAHHAHAHHAHAHAHAHHAHA")
			print(english)
	return dic

def convert_file_to_french(en_filename, fr_filename, dic):
	source = open(en_filename) 
	lines = source.readlines()
	fr_lines = []
	for line in lines:
		words = line.split()
		fr_words = []
		for word in words:
			word = word.strip()
			
			if word in dic.keys():
				fr_words.append(dic[word])
			else:
				fr_words.append(word)			
			
			
			
		fr_line = ' '.join(str(elem) for elem in fr_words) + '\n'
		fr_lines.append(fr_line)

	translated = open("translated.txt",'a+')
	for line in fr_lines:
		translated.write(line)

dic = populate_en_fr_dic()
convert_file_to_french("experimental","translated.txt",dic)
