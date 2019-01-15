#Code_written_&_devloped_by_Priyansh_Tripathi
#This python script takes raw txt file as input and produces tokenized sentence splitted file as output



raw_khnd_path = '/home/priyanshtripathi10/Desktop/le maza le/hin_sen_13'
raw_khnd= open(raw_khnd_path, 'rt')
data=raw_khnd.read()
#data = data.replace('|', '. ')                                         #Can be used if txt file consist of phrases in hindi
raw_khnd.close()

                                  
from nltk import sent_tokenize
sentences = sent_tokenize(data)                                         #Split into sentences
#print(sentences[0])

khnd=open('/home/priyanshtripathi10/Desktop/le maza le/swag','w')       #Tokenized sentence splitted file
for i in sentences:
    print(i)
    khnd.write(i)
    khnd.write('\n')
khnd.close()
