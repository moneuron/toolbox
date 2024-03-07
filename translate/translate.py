###################
INPUT_L = 'en'
OUTPUT_L = 'fa'
###################

from deep_translator import GoogleTranslator
path = input("Enter the path: ")
out = path.split('.')[0]
output = ''
with open(path, "r") as file:
    lines = file.readlines()
    for line in lines:
        l = line.replace("\n", ' ')
        output += l
output = output.replace(".", ". \n")
    
def strSplit(in_str, count):
    result = []
    cur_pos = 0
    while cur_pos < len(in_str):
        substr = in_str[cur_pos:cur_pos + count]
        result.append(substr)
        cur_pos += count
    return result

outlist = strSplit(output, 4999)
translated = ''
for _ in outlist:
    o = GoogleTranslator(source = INPUT_L, target = OUTPUT_L).translate(_)
    translated += o
with open(f'translated_{out}.txt', "w") as file:
    file.write(translated)
