import re
import string
import itertools
import sys
# print("Hello world")

cleaned_text=[]
unigrams = dict()
bigrams = dict()
trigrams = dict()
quadgrams = dict()

def gen_pre_string(sentence):
  length =len(sentence.split())
  if (length==4): return sentence.split()[0]+" "+sentence.split()[1]+" "+sentence.split()[2]
  if (length==3): return sentence.split()[0]+" "+sentence.split()[1]
  if (length==2): return sentence.split()[0]
  if (length==1): return ""

def gen_post_string(sentence):
  length =len(sentence.split())
  if (length==4): return sentence.split()[1]+" "+sentence.split()[2]+" "+sentence.split()[3]
  if (length==3): return sentence.split()[1]+" "+sentence.split()[2]
  if (length==2): return sentence.split()[1]
  if (length==1): return ""

def first_term(sentence):
  count=0
  count1=0
  count2=0
  d=0.75
  length = len(sentence.split())
  if (length == 4):
    if sentence in quadgrams: count = quadgrams[sentence]
    else: count = 0
    numerator = max(count-d,0)
    if gen_pre_string(sentence) in trigrams: denominator = trigrams[gen_pre_string(sentence)]
    else: return 0
  elif (length == 3):
    for i in quadgrams:
      if(sentence.split()[0]==i.split()[1] and sentence.split()[1]==i.split()[2] and sentence.split()[2]==i.split()[3]):
        count1+=1
    for j in trigrams:
      if(sentence.split()[0]==j.split()[1] and sentence.split()[1]==j.split()[2]):
        count2+=trigrams[j]
    numerator = max(count1-d,0)
    denominator = count2
  elif (length == 2):
    for i in trigrams:
      if(sentence.split()[0]==i.split()[1] and sentence.split()[1]==i.split()[2]):
        count1+=1
    for i in bigrams:
      if(sentence.split()[0]==i.split()[1]):
        count2+=bigrams[i]
    numerator = max(count1-d,0)
    denominator = count2
  elif (length == 1):
    for i in bigrams:
      if(sentence.split()[0]==i.split()[1]):
        count1+=1
    for i in unigrams:
        count2+=unigrams[i]
    numerator = max(count1-d,0)
    denominator = count2
  if numerator==0: return 0
  else:
    return numerator/denominator

def mle_probability(sentence):
    length = len(sentence.split())
    numerator = 0
    denominator = 0
    if (length==4):
        if sentence in quadgrams: numerator = quadgrams[sentence]
        if gen_pre_string(sentence) in trigrams: denominator = trigrams[gen_pre_string(sentence)]
    if (length==3):
        if sentence in trigrams: numerator = trigrams[sentence]
        if gen_pre_string(sentence) in bigrams: denominator = bigrams[gen_pre_string(sentence)]
    if (length==2):
        if sentence in bigrams: numerator = bigrams[sentence]
        if gen_pre_string(sentence) in unigrams: denominator = unigrams[gen_pre_string(sentence)]
    if (length==1):
        if sentence in unigrams: numerator = unigrams[sentence]
    if (numerator==0) or (denominator==0): return 0
    else: return numerator/denominator

def kneyser_lambda(sentence):
  length =len(sentence.split())
  count=0
  d = 0.75
  if (length == 4):
    for i in quadgrams:
      if(sentence.split()[0]==i.split()[0] and sentence.split()[1]==i.split()[1] and sentence.split()[2]==i.split()[2]):
        count+=1
    numerator = d*count
    if gen_pre_string(sentence) in trigrams: denominator = trigrams[gen_pre_string(sentence)]
    else: return 0
  elif (length == 3):
    for i in trigrams:
      if(sentence.split()[0]==i.split()[0] and sentence.split()[1]==i.split()[1]):
        count+=1
    numerator = d*count
    if gen_pre_string(sentence) in bigrams: denominator = bigrams[gen_pre_string(sentence)]
    else: return 0
  elif (length == 2):
    for i in bigrams:
      if (sentence.split()[0]==i.split()[0]):
        count+=1
    numerator = d*count
    if gen_pre_string(sentence) in unigrams: denominator = unigrams[gen_pre_string(sentence)]
    else: return 0
  else:
    numerator = len(unigrams)*d #kneyser_lambda of empty string is d
    denominator = len(unigrams)
  if numerator==0: return 0
  else:
      return numerator/denominator

def witten_lambda(sentence):
  length =len(sentence.split())
  count = 0
  if (length==4):
      if gen_pre_string(sentence) in trigrams: numerator = trigrams[gen_pre_string(sentence)]
      else : numerator = 0
      for i in quadgrams:
        if(sentence.split()[0]==i.split()[0] and sentence.split()[1]==i.split()[1] and sentence.split()[2]==i.split()[2]):
          count+=1
      denominator = numerator + count
  if (length==3):
      if gen_pre_string(sentence) in bigrams: numerator = bigrams[gen_pre_string(sentence)]
      else : numerator = 0
      for i in trigrams:
        if(sentence.split()[0]==i.split()[0] and sentence.split()[1]==i.split()[1]):
          count+=1
      denominator = numerator + count
  if (length==2):
      if gen_pre_string(sentence) in unigrams: numerator = unigrams[gen_pre_string(sentence)]
      else : numerator = 0
      for i in bigrams:
        if(sentence.split()[0]==i.split()[0]):
          count+=1
      denominator = numerator + count
  if (length==1):
      numerator = 1
      denominator = 2*len(unigrams)
  if (numerator==0) or (denominator==0): return 0
  else: return numerator/denominator

def calc_kneyser_probability(sentence):
  length = len(sentence.split())
  if (length >=2): return first_term(sentence) + kneyser_lambda(sentence)*calc_kneyser_probability(gen_post_string(sentence))
  else: return first_term(sentence) + (kneyser_lambda(sentence)/len(unigrams))

def calc_witten_probability(sentence):
    length = len(sentence.split())
    if (length >=2): return witten_lambda(sentence)*mle_probability(sentence) + (1-witten_lambda(sentence))*calc_witten_probability(gen_post_string(sentence))
    else: return witten_lambda(sentence)*mle_probability(sentence) + (1-witten_lambda(sentence))*(1/(2*len(unigrams)))

def kneyser(sentence):
  fourgrams = []
  output = 1
  for i in range(0,len(sentence.split())-3):
    fourgrams.append(sentence.split()[i]+" "+sentence.split()[i+1]+" "+sentence.split()[i+2]+" "+sentence.split()[i+3])
  for i in fourgrams:
    if i in quadgrams: output*=calc_kneyser_probability(i)
    elif gen_post_string(i) in trigrams: output*=calc_kneyser_probability(gen_post_string(i))
    elif gen_post_string(gen_post_string(i)) in bigrams: output*=calc_kneyser_probability(gen_post_string(gen_post_string(i)))
    else : output*=calc_kneyser_probability(i.split()[0])
  return output

def witten(sentence):
   fourgrams = []
   output = 1
   for i in range(0,len(sentence.split())-3):
     fourgrams.append(sentence.split()[i]+" "+sentence.split()[i+1]+" "+sentence.split()[i+2]+" "+sentence.split()[i+3])
   for i in fourgrams:
     output*=calc_witten_probability(i)
   return output

def start(input):
    # make the text lowercase
    input = input.lower()
    # remove punctuations
    input = re.sub("[^a-zA-Z ]", "", input)
    input = input.replace("  "," ")
    # adding start and end tags
    input = "<s> "+input+" </s>"
    if (sys.argv[1]=="k"): probability = kneyser(input)
    elif (sys.argv[1]=="w"): probability = witten(input)
    else: print("Wrong input format")
    perplexity = probability**(-1/len(input.split()))
    print("Probability of the sentence is ",probability)
    print("Perplexity of the sentence is ",perplexity)

def clean_text(text):
    if(text.find("_")==-1): #to remove POS tags
        # make the text lowercase
        new_text = text.lower()
        # remove punctuations
        new_text = re.sub("[^a-zA-Z ]", "", new_text)
        new_text = new_text.replace("  "," ")
        # adding start and end tags
        new_text = "<s> "+new_text+" </s>"
        # remove empty strings
        x = new_text.isspace()
        if(not x):
            cleaned_text.append(new_text)
            # generating and counting grams
            for i in range(0,len(new_text.split())):
                temp1 = new_text.split()[i]
                if temp1 in unigrams: unigrams[temp1]+=1
                else: unigrams[temp1]=1
                if (i < len(new_text.split())-1):
                    temp2 = new_text.split()[i]+" "+new_text.split()[i+1]
                    if temp2 in bigrams: bigrams[temp2]+=1
                    else: bigrams[temp2]=1
                if (i < len(new_text.split())-2):
                    temp3 = new_text.split()[i]+" "+new_text.split()[i+1]+" "+new_text.split()[i+2]
                    if temp3 in trigrams: trigrams[temp3]+=1
                    else: trigrams[temp3]=1
                if (i < len(new_text.split())-3):
                    temp4 = new_text.split()[i]+" "+new_text.split()[i+1]+" "+new_text.split()[i+2]+" "+new_text.split()[i+3]
                    if temp4 in quadgrams: quadgrams[temp4]+=1
                    else: quadgrams[temp4]=1

# take input
input_sentence = input("Enter the sentence: ")

# load corpus
filename = sys.argv[2]
file = open(filename, 'rt')
for x in file:
    clean_text(x)
# clean_text("here i am and there i am.")
text = file.read()
file.close()

# To find the probabilities and perplexities of all train sentences
# plsfile = open("train_health.txt", 'rt')
# average_perplexity = 0
# counter = 0
# for i in plsfile:
#     if (counter==1000): break
#     if(counter>484):
#         y = start(i)
#         x = i.rstrip("\n") + "   " + str(y) + "\n"
#         print(x,counter,end='\r')
#         with open("health_witten_train2.txt",'a') as f: f.write(x)
#         average_perplexity += y
#     counter+=1

# print(average_perplexity/1000)
# with open("health_witten_train.txt",'a') as f : f.write("Average: "+str(average_perplexity/1000))

print("Number of unigrams: ",len(unigrams))
print("Number of bigrams: ",len(bigrams))
print("Number of trigrams: ",len(trigrams))
print("Number of quadgrams: ",len(quadgrams))

start(input_sentence)
