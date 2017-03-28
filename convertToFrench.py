import nltk
import sys
class convertToFrench(object):
	def __init__(self,dictionary_file):
		
		# self.uknown_vocab_file = open("unseen_fr_words_in_50k",'a+')
		# self.known_french_words = []

		# french_vocab_file = open("./data/vocab80000.to")
		# lines2 = french_vocab_file.readlines()


		# for i in range(len(lines2)):
		# for i in range(40000):
		# 	word = lines2[i].strip()
		# 	self.known_french_words.append(word)
		self.dictionary = self.createFrenchDictionary(dictionary_file)

	
	def convertToFrench(self,source_file, dest_file):
		# eng_src_file = open(source_file)
		french_dest_file = open(dest_file,'a+')

		# lines = eng_src_file.readlines()
		count = 0
		for line in open(source_file):
			french_words = []
			words = nltk.word_tokenize(line)
			for word in words:
				word = word.strip()
				# print(word)
				try:
					fr_word = self.dictionary[word]
					# fr_word = word
				except:
					try:
						fr_word = self.dictionary[word.lower()]
					except:
						# print("not found",word)
						fr_word = '_UNK'


					
				french_words.append(fr_word)
			#write french line
			if count%1000 == 0:
				print(count*100/22520376, "% completed")
			count = count+1
			fr_line = " ".join([str(elem) for elem in french_words])+"\n"
			french_dest_file.write(fr_line)

		
		# eng_src_file.close()
		french_dest_file.close()


	def createFrenchDictionary(self,dictionary_file):
		dic_en_fr={}
		dic_file = open(dictionary_file)
		lines = dic_file.readlines()


		# # print(len(lines))
		# # i = 0;
		for i in range(len(lines)):
			# print i
			words = lines[i].split()
			# print(words)
			try:
				english = words[0].strip()
			except:
				print(words,i)
			# print(english)
			# write unknown word to a separate file
			# for sub_word in words[1:]:
			# 	if sub_word not in self.known_french_words:
			# 		self.uknown_vocab_file.write(sub_word+"\n")
			french = " ".join([elem for elem in words[1:]])
			dic_en_fr[english] = french

		return dic_en_fr
	def convertToFrenchSentence(self,english_sentence):
		french_words = []
		words = nltk.word_tokenize(english_sentence)
		for word in words:
			word = word.strip()
			# print(word)
			try:
				fr_word = self.dictionary[word]
				# fr_word = word
			except:
				try:
					fr_word = self.dictionary[word.lower()]
				except:
					# print("not found",word)
					fr_word = '_UNK'


				
			french_words.append(fr_word)
		fr_line = " ".join([str(elem) for elem in french_words])
		return fr_line

	def printDictionary(self):
		for key in self.dictionary:
			print(key,self.dictionary[key])
		print("the total length is ",len(self.dictionary))


# fileConverter = convertToFrench("new_eng_fr_dic")
# # fileConverter.printDictionary()
# fileConverter.convertToFrench(sys.argv[1],sys.argv[2])
# print(fileConverter.convertToFrenchSentence("I like it"))
