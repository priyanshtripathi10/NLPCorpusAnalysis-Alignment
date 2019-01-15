#Code_written_&_devloped_by_Priyansh_Tripathi
#This pyhton script takes raw txt files of two languages(here ENG & HND) as input and first produce tokenized sentences from them individually.
#After this it produces another file having sentence aligned from both languages

for i in range(1,912):
    try:
        raw_khnd_path_hnd= '/home/priyanshtripathi10/Desktop/le maza le/a/hin_sen_'+str(i)
        raw_khnd_hnd= open(raw_khnd_path_hnd, 'rt')
        data_hnd=raw_khnd_hnd.read()
        #data_hnd = data.replace('|', '. ')                                                       #Can be used if txt file consist of phrases in hindi
        raw_khnd_hnd.close()

                                  
        from nltk import sent_tokenize
        sentences_hnd= sent_tokenize(data_hnd)                                                    #Split into sentences
        #print(sentences_hnd[0])

        khnd_hnd=open('/home/priyanshtripathi10/Desktop/le maza le/b/HND_sen'+str(i),'w')         #Tokenized sentence splitted file
        for i in sentences_hnd:
            print(i)
            khnd_hnd.write(i)
            khnd_hnd.write('\n')
        khnd_hnd.close()
    except Exception as e:
        print(e)

for j in range(1,912):
    try:
        raw_khnd_path_eng= '/home/priyanshtripathi10/Desktop/le maza le/a/eng_sen_'+str(j)
        raw_khnd_eng= open(raw_khnd_path_eng, 'rt')
        data_eng=raw_khnd_eng.read()
        #data_hnd = data.replace('|', '. ')                                                       #Can be used if txt file consist of phrases in hindi
        raw_khnd_eng.close()

                                  
        from nltk import sent_tokenize
        sentences_eng= sent_tokenize(data_eng)                                                    #Split into sentences
        #print(sentences_eng[0])

        khnd_eng=open('/home/priyanshtripathi10/Desktop/le maza le/b/ENG_sen'+str(j),'w')         #Tokenized sentence splitted file
        for j in sentences_eng:
            print(j)
            khnd_eng.write(j)
            khnd_eng.write('\n')
        khnd_eng.close()


    except Exception as e:
        print(e)    
