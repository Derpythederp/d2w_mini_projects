from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):

    random.seed(seed)

    return [random.randint(0, 9) for i in range(number)]

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array

	array = gen_random_int(number, seed) 
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.

	array_str = array.join(",") + "." 

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"
	document.getElementById("generate").innerHTML = array_str

def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

def bubble_sort(array):
	count = 0
    ###
    ### YOUR CODE HERE
    ###
	l_arr = len(array)
	swapped = True  
	
	for i in range(l_arr-1):
		if swapped is True:
			swapped = False
			for j in range(1, l_arr - i):
				count += 1
				if array[j-1] > array[j]:
					swap(array, j-1, j)
					swapped = True
	return count

def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	array_str = document.getElementById("generate").innerHTML
	array = [int(i) for i in array_str.rstrip(".").split(",")]
	bubble_sort(array)
	array_str = array.join(",") + "." 
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	array = [int(i.strip()) for i in value.rstrip(".").split(",")]
	bubble_sort(array)
    
	array_str = array.join(",") + "." 

	document.getElementById("sorted").innerHTML = array_str


