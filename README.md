# NLPCorpus Analysis-Alignment

In this internship we contributed to the institute’s on going project Anusaaraka. We worked on module Corpus Analysis and Bilingual Corpus Alignment and had the task to provide the institute with data to be used by Anusaaraka. What we learned in this internship is to code better using python. Combination of these two languages together solved the problems that we faced.

Here we are making a strong corpus consisiting of bilingual sentence alignments(ENG & HND in this case) in order to feed Anusaaraka a ML based language transalation software, which employs algorithms derived from Panini Ashtadhyai(Grammer Rules).
In today's Information Age large volumes of information are available in English – whether it be information for competitive exams or general reading. However, many people whose primary language is Hindi or any other Indian language are unable to access information in English. Anusaaraka aims to bridge this language barrier by allowing a user to enter an English text into Anusaaraka and read it in an Indian language of their choice.

In order to make a structured corpus we will first make individual corpus of Hindi & English in form of txt files. Presently it will be raw in nature and hence will need to be tokenized which will be done by means of final_para2tokensentence.py which can easily process txt files of two languages(in this HND & ENG).
eg.

raw_khnd_path_hnd= 'INSERT YOUR PATH HERE /hin_sen_'+str(i)

After this it will be served to Microsoft API for statistical analysis & Champollion Tool Kit V1.2 which is a ready-to-use parallel text sentence alignment tool for as many language pairs as possible.
However the result is not that much satisfied and will look something like this as shown in ENG_align.txt ; Hence to further tune we will take help of C code wriiten in arrangehndeng.c which will produce output as shown in ENG_final_align.txt

After the data analytics and obtained statistics we focused on the aspect of increasing the efficiency and accuracy of the machine. The machine used was Champollion 1.2 which was trained through various aspects like training a dictionary, deploying a morph and the machine later produces an accuracy of 93.4% from 61%.
Morever if we can visualize the reasons for occuring ommissions we can manually correct it by making our own set of dictionary and feeding it to the Champollion Tool Kit which will look like the files ending.txt ending1.txt ending3.txt


Alignment tools : Microsoft’s Bilingual Sentence Aligner that uses unsupervised method to produce results. This API was created in Perl language and worked better if sentences provided contained same/similar words. It uses mathematical expressions to produce result. We did not use it because the data that we provided it contained various sanskrit words that were once per page and it was difficult to align them through unsupervised method.

We used Champollion 1.2 toolkit that uses supervised method to produce results. We trained this tool to meet our results. Before training the results were around 65% approx and after adding dictionary and updating codes it gave us 94% results. Champollion is open source software and we used it because it gave better results than Microsoft’s Bilingual Alignment tool.


Now I'm trying to automate the whole process consisting of all the scripts & libraries which we performed individually and is listed above.
        
