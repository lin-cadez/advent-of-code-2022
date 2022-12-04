total=0
total_1=0
file = open("final.txt", "r")
input_data=file.readlines()
for i in range(len(input_data)):
  ids=input_data[i].strip().split(",")
  comp_a=ids[0].split("-")[0]
  comp_b=ids[0].split("-")[1]
  comp_x=ids[1].split("-")[0]
  comp_y=ids[1].split("-")[1]
  stevec=[]
  stevec_2=[]
  for x in range(int(comp_a), int(comp_b)+1):
    stevec.append(x)

  for y in range(int(comp_x), int(comp_y)+1):
    stevec_2.append(y)

  if set(stevec).issubset(stevec_2) or set(stevec_2).issubset(stevec):
    total_1+=1

  if set(stevec).intersection(stevec_2):
    total+=1

print("Prvi del", total_1)
print("drugi del", total)

    

    
    

   





