#construct dictionary from the translated word
eng_80k_list = []
eng_vocab_file = open("./data/vocab80000.from")
lines3 = eng_vocab_file.readlines()
for i in range(10000):
	word = lines3[i].strip()
	eng_80k_list.append(word)



dic_en_fr={}
dictionary_file = open("new_eng_fr_dic")
lines = dictionary_file.readlines()


# print(len(lines))
# i = 0;
for i in range(10000):
	# print i
	words = lines[i].split()
	# print(words)
	english = eng_80k_list[i]
	# print(english)
	french = " ".join([elem for elem in words[1:]])
	dic_en_fr[english] = french
	# i = i+1

dictionary_file.close()


# for word in dic_en_fr.keys():
	# print word, dic_en_fr[word]

french_80k_list = []
french_vocab_file = open("./data/vocab80000.to")
lines2 = french_vocab_file.readlines()


# for i in range(len(lines2)):
for i in range(80000):
	word = lines2[i].strip()
	word = word.replace("’","'")
	french_80k_list.append(word)







# ####
# #so far eng_80k_list = english word from 80kto, french_80k_list = french words from 80k

# for w in french_80k_list:
# 	print(w)

for w in eng_80k_list:
	# print(w)
	if w in dic_en_fr.keys():
		translation = dic_en_fr[w]
		subWords = translation.split()
		for sw in subWords:
			sw = sw.strip()
			if sw not in french_80k_list:
				print(sw)

	else:
		print('not found',w)

# 	# subWords = w.split()
# 	# for subword in subWords:
# 	# 	if subword not in french_80k_list.keys():
# 	# 		print subword


