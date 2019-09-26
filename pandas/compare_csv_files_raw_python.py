""" Comparing two csv files ising raw python code """

file_list = ['datasets/wine_reviews.csv', 'datasets/wine_reviews.csv']

f1 = open(file_list[0], encoding='utf-8').readlines()
f2 = open(file_list[1], encoding='utf-8').readlines()

#fName = open('output.csv', 'a')
def compare():
	r = 0
	for _ in range(2):
	    for row in f1:
	        if row in f2:
	            print(row)
	            if r == 6:
	                break
	        r += 1
