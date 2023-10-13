# import json

# with open('C:/Users/DEBASHISH THAKUR/Desktop/project/card.json', 'r') as json_file:
#     dataset = json.load(json_file)

# encoder_inputs = [ ]
# for example in dataset:
#     encoder_inputs.append(example["question_toks"])

# print(encoder_inputs)

source_tokenizer = {
    'this': 1,
    'is': 2,
    'an': 3,
    'example': 4,
    'source': 5,
    'language': 6,
    # Other source language tokens...
}
for word, i in source_tokenizer.items():
    print(word, i)