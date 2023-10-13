##MODEL PARAMETERS

##count the number of input vocab size
index = 0
frequency = {}



for i in hm:
    query_toks = i["question_toks"]
    # print(query_toks)
    for j in query_toks:
        # print(j)
        
        if j not in frequency:
            frequency[j] = index
            index += 1
print((frequency))


##count the number of output vocab size

for i in hm:
    query_toks = i["query_toks"]
    # print(query_toks)
    for j in query_toks:
        # print(j)
        
        if j not in frequency:
            frequency[j] = index
            index += 1
print((frequency))

#what are the total questions?
for i in hm:
    query_toks = i["question"]
    print(query_toks)
    

##maximum output sequence length
count = []
for i in hm:
    counter = 0
    query_toks = i["query_toks"]
    print(query_toks)
    for j in query_toks:
        # print(j)
        counter+=1
    count.append(counter)
    
        # if j not in frequency:
        #     frequency[j] = index
        #     index += 1
# print((frequency))
print(max(count))

#maximum input sequence length
count = []
for i in hm:
    counter = 0
    query_toks = i["question_toks"]
    # print(query_toks)
    for j in query_toks:
        # print(j)
        counter+=1
    count.append(counter)
    
        # if j not in frequency:
        #     frequency[j] = index
        #     index += 1
# print((frequency))
print(count)