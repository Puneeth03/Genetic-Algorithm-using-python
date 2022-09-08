from collections import OrderedDict

#changing decimal to binary
def changeToBinary(inte): 
    return format(inte, "b")

#changing binary to decimal
def changeToDecimal(bina):
    return int(bina,2)

#shifting bits for generation of new generation
#offset is number of bits to be changed
def shiftBits(parent1, parent2, offset):
    if(len(parent1)<4):
        parent1 = "0"*(4-len(parent1)) + parent1
    if(len(parent2)<4):
        parent2 = "0"*(4-len(parent2)) + parent2
    
    child1 = parent1[:-offset] + parent2[-offset:]
    child2 = parent2[:-offset] + parent1[-offset:]
    
    return child1, child2

#calculation of value of y for x
def calculate_x_value(x):
    #define the function to find a optimized value
    #considering this polynomial to find the optimized maximum 
    y = (x**4 - 90*(x**3) + 1755*(x**2) + 26190*x -727056)/(-10000)
    return y

#Generating next generation 
def calculate_nextgen(parent1, parent2):
    parent1 = changeToBinary(parent1)
    parent2 = changeToBinary(parent2)

    child1, child2 = shiftBits(parent1,parent2,3)
    child3, child4 = shiftBits(parent1,parent2,2)

    child1 = changeToDecimal(child1)
    child2 = changeToDecimal(child2)
    child3 = changeToDecimal(child3)
    child4 = changeToDecimal(child4)
    
    #print(str(child1) + " " + str(child2))
    
    child1_value = calculate_x_value(child1)
    child2_value = calculate_x_value(child2)
    child3_value = calculate_x_value(child3)
    child4_value = calculate_x_value(child4)
    
    
    child_details = [(child1, child1_value), (child2, child2_value), (child3, child3_value), (child4, child4_value)]
    return child_details
    
#define different range for x
range_array = list(range(-50,51,10))
range_array_length = len(range_array)

#list of values of x and value of y for x
output_array = list()

#appending values of x and y for x
for x in range_array:
    x_value = calculate_x_value(x)
    output_array.append((x,x_value))
    
print("Values of x and y for initial values: ")
print(output_array)

#sorting to find sorted to find fittest values for y of x
output_array = (sorted(output_array, key=lambda item: item[1], reverse=True))

print("First sorted values of x and y :")
print(output_array)

counter = 0

#Mention the number of generations to find
g_no = int(input('Enter the maximum number of generations to find the respective children'))
while(counter != g_no):
    #Passing values of first to fittest parents to find the child
    next_gen_child_details = calculate_nextgen(output_array[0][0] , output_array[1][0])
    
    #Replacing the 2 fittest child with 2 previous generation 
    output_array[-1] = next_gen_child_details[0]
    output_array[-2] = next_gen_child_details[1]
    output_array[-3] = next_gen_child_details[2]
    output_array[-4] = next_gen_child_details[3]
    
    #Sorting the new generation to again find the fittest
    output_array = sorted(output_array, key=lambda item: item[1], reverse=True)
    
    print(str(counter+1) + "th Generation")
    print(output_array)
    
    counter += 1