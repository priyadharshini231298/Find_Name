import docx
from textblob import TextBlob
doc = docx.Document('Naveen_Senior-Trainer_Profile.docx')
lst=[]
for para in doc.paragraphs:
	print(para.text)
	blob=TextBlob(para.text)
	for words,tag in blob.tags:
		if tag=='JJ' or tag=='NNP':
			lst.append(words)
print("Document Name:",lst[0],lst[1],lst[2])



