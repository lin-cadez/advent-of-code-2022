temp_total=0
sum_list=[]
best_list=[]
with open("kalorije.txt", "r") as a_file:
	
  for line in a_file:
    stripped_line = line.strip()
    if stripped_line=="":
    	sum_list.append(temp_total)
    	temp_total=0
    else:
    	temp_total=int(stripped_line)+temp_total

output=sorted(sum_list)[-3::]
for i in range(3):
	temp_total=max(sum_list)
	best_list.append(temp_total)
	sum_list.remove(temp_total)

print(output)