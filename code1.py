#creating a dictinory file refrence name keep it as Dict
Dict=dict()
#iam adding some names so Refrence i keep as names 
names=['ganesh','gopi','bheeshma','gopi','ramesh']
  for name in names:
    if name not in Dict:
      Dict[name]=1
    else:
      Dict[name]=Dict[name]+1
      print(Dict)
      
#same thing but small variation by using get
Dict=dict()
names=['ganesh','gopi','bheeshma','gopi','ramesh']
for name in names:
Dict[name]=Dict.get(name,0)+1
print(counts)
