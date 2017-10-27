#save this file as random_int.py
from random import randint
def randlist(r):
	alapha = ["A","b","B","c","C","d"]
	uses = [0,0,0,0,0,0]
	c = alapha[r]
	return c
	
def main():
	done = False
	while done == False:
		r = randint(0,5)
		c = randlist(r)
		print(c,end="")
main()
