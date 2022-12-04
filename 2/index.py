total=0
final=0
kamen=1
papir=2
skarje=3
lost=0
draw=3
win=6
with open("final.txt", "r") as a_file:
  for line in a_file:
  	total=0
  	stripped_line = line.strip().split(" ")
  	compare_a=stripped_line[0]
  	compare_b=stripped_line[1]
  	match compare_a:
  		case "A": #kamen

  			if compare_b=="Y": #draw
  				total=kamen+draw
  			elif compare_b=="Z": #win
  				total=papir+win
  			elif compare_b=="X": #lose
  				total=skarje+lost

  		case "B": #papir
  			if compare_b=="Y": #draw
  				total=papir+draw
  			elif compare_b=="Z": #win
  				total=skarje+win
  			elif compare_b=="X": #lose
  				total=kamen+lost

  		case "C": #škarje
  			if compare_b=="Y": #draw
  				total=skarje+draw
  			elif compare_b=="Z": #win
  				total=kamen+win
  			elif compare_b=="X": #lose
  				total=papir+lost

  	final=final+total
print(final)





