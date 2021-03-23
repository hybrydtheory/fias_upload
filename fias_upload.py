import codecs

from dadata import Dadata

token = "e277bc42a2d2df54feb153d6e79d66eb7f5daa50"
dadata = Dadata(token)
result = dadata.find_by_id("address", 'e1b73599-ccad-4dea-b8db-c81d0082207f')
print(result)

