
# coding: utf-8

# In[1]:


def termfrequency(sentence1, sentence2):

    question_dict ={}
    sentence1_words = sentence1[0].split()
    sentence2_words = sentence2[0].split()
    searchtermfreq = []
    i = 0

    for key in sentence1_words:
        question_dict[key] = question_dict.get(key,0) + 1

    for key in set(sentence2_words):
        value =  question_dict.get(key,0)
        if value >= 1:
            value = 1
        searchtermfreq.append(value)

#     print (question_dict)
#     print (searchtermfreq)
    return sum(searchtermfreq)

termfrequency(['What is the step by step guide to invest in share market in india?'], ['What is the step by step guide to invest in share market?'])



# In[ ]:
