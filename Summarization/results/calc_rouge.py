import spacy
import os
from nltk.translate.bleu_score import sentence_bleu
import re
from rouge import Rouge 

nlp = spacy.load('en')

output_baseline = open("output_baseline_rouge.txt", "w")
output_new = open("output_new_rouge.txt", "w")
top_summaries = open("top_summaries_rouge.txt", "w")

d = dict()
	
for i in range(7054):
	f1 = open("/home/amit/Desktop/b4_________decode_test_500maxenc_4beam_35mindec_40maxdec_ckpt-238410/decoded/" + str(i).zfill(6) + "_decoded.txt")
	f2 = open("/home/amit/Desktop/aftr________decode_test_500maxenc_4beam_35mindec_40maxdec_ckpt-238410/decoded/" + str(i).zfill(6) + "_decoded.txt")
	f3 = open("/home/amit/Desktop/aftr________decode_test_500maxenc_4beam_35mindec_40maxdec_ckpt-238410/reference/" + str(i).zfill(6) + "_reference.txt")
	

	doc1 = f1.read()
	doc2 = f2.read()
	doc3 = f3.read()

	rouge = Rouge()
	similarity1 = rouge.get_scores(doc1, doc3)
	similarity2 = rouge.get_scores(doc2, doc3)
	
	sim1_1f = similarity1[0]['rouge-1']['f']
	sim2_1f = similarity2[0]['rouge-1']['f']
	
	sim1 = sim1_1f
	sim2 = sim2_1f
	
	if sim2 > sim1:
		d[sim2 - sim1] = i

	output_baseline.write(str(sim1) + "\n")
	output_new.write(str(sim2) + "\n")
	
	f1.close()
	f2.close()
	f3.close()
	
	
output_baseline.close()
output_new.close()

top_summaries.write("Total number of summaries which performed better than baseline: " + str(len(d)) + "\n")

nd = sorted(d, reverse=True)[:50]
for i in nd:
	top_summaries.write(str(d[i]) + "\n")
	
top_summaries.close()
