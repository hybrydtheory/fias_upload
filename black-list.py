import codecs
from dadata import Dadata

input_file = 'output.XML'
out_file = 'address.XML'


with open(r"output.XML", "r") as file:
    for line in file:
        line = line.strip()
        ID = ('\"' + str(line) + '\"')
        with open(out_file, 'w') as out_file:
            while True:
                token = "e277bc42a2d2df54feb153d6e79d66eb7f5daa50"
                dadata = Dadata(token)
                result = dadata.find_by_id("address", ID)
                out_file.write(str(result) + "\r")