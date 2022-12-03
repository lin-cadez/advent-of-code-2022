import string
letters = ["Space-holder"] + [x for x in string.ascii_lowercase] + [x for x in string.ascii_uppercase]
total=0
with open ("test.txt","r") as file:
  for line in file:
    s1 = line[:len(line)//2]
    s2 = line[len(line)//2:]
    common="".join(set(s1).intersection(s2))
    total=total+letters.index(common)
print("first part", total)




    
    

   





