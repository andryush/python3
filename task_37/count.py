import sys

sentense = sys.argv[1]
sentense = sentense.replace('!','')
sentense = sentense.replace(' ,','')
sentense = sentense.replace('.','')
sentense = sentense.replace('  ','')
sentense = sentense.replace('?','')
sentense = sentense.split()

print(len(sentense))
