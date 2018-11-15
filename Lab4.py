"""
CS 2302
Emilio Ramirez
Lab 4 A
Diego Aguirre,  Manoj Saha
Last Date Modified: Novemeber 14th, 2018
Purpose:  Use a hash table to improve the running time of algorithm from previous lab
"""
import math
import time
from Node import Node 

def load_factor(table):
    """
    this method is in charge of solving for the load factor of a given hashtable

    Parameters:
        table: hashtable that contains nodes and deals with collisions by chaining
    Returns:
        returns nothing but does print out the load factor of the given table.

    """
    total_Nodes = 0

    for i in range(len(table)):
        itter = table[i]
        while itter != None:
            total_Nodes +=1
            itter = itter.next
    print("the load factor is: " + str((total_Nodes)/ len(table)) )
    return

def average_distrubution_true(table):
    """
    This method is incharge of solving for the average distrubution of values on a hashtable
    that is on average how many Nodes are at a given node in the given hash table.

    Parameters:
        table: the hash table that contains nodes and deal with collisions by chaining
    Returns:
        total_nodes/len(lengths): total number of nodes divided by the number of non empty hash table entrees
    """ 
    lengths = []
    total_nodes = 0
    counter = 0
    for i in range(len(table)):
        counter = 0
        itter = table[i]
        while itter != None:
            counter += 1
            itter = itter.next
        if counter != 0:
            lengths.append(counter)
    for i in lengths:
        total_nodes += i
    return total_nodes/len(lengths)



def insert(table, name, embedding):
    """
    method that is used to insert an element into a hash table

    Parameters:
        table: the hash table to which the element will be added
        name: the name of the elemnt that is going to be added
        embedding: embedding that corresponds to the element that is going to be added.
    Returns:
        table: the hash table that now containss a node with characteristics described in parameters.



    """
    location = hash_function2(name, len(table))  # change this line to choose which function will be used currently set to hash_function2
    table[location] = Node(name, embedding, table[location])
    return table

    

def hash_function1( value, length):
    """
    One  of three hash functions that is used to convert a given word into an index in a hashtable

    Parameters:
        value: word that is to be hashed
        length: length of the hashTable
    Returns:
        total % length: possible index in hashtable that is given by hashing given value.
    """
    i = 0
    total =  float(0)
    while len(value) > 1:
        Char_value = ord(value[0]) # ascii number of first character in string is saved
        total = (float(math.pow(26,i)) * float(Char_value)) +total # total is set equal to (26^i)* Char_value plus previous total( where i is the current letters index in the  initial word)
        value = value[1:]   # sets the string equal to the substring of the current string formed by dropping the first character
        i+=1
    if len(value) ==1:   # code rewritten to avoid index out-of-bounds but does the same as previous while loop except does not create a substring.
        Char_value = ord(value[0])
        total = (float(math.pow(26,i)* float(Char_value)))+ total
    return int(total) % length
        
def hash_function2( value, length):
    """
    One  of three hash functions that is used to convert a given word into an index in a hashtable

    Parameters:
        value: word that is to be hashed
        length: length of the hashTable
    Returns:
        total % length: possible index in hashtable that is given by hashing given value.
    """    
    total =  float(1) # setting total to 1 intially is important as if it were zero all values would be hashed to zero
    for i in range(len(value)):
        Char_value = ord(value[i]) #ascii number of character i in string is saved 
        total = Char_value * (total+1) # total+1 is multiplied by Char_Value
    return int(total) % length

def hash_function3( value, length):
    """
    One  of three hash functions that is used to convert a given word into an index in a hashtable

    Parameters:
        value: word that is to be hashed
        length: length of the hashTable
    Returns:
        total % length: possible index in hashtable that is given by hashing given value.
    """    
    total =  0 
    for i in range(len(value)):
        Char_value = ord(value[i]) #ascii number of character i in string is saved 
        total = Char_value + total # total is set equal to Char_Value + total
    return int(total) % length
             

def Get_Words(filename):
    """
    This method reads a file with the given name and creates a hash table that will store all of the words
    found in the file along with the coresponding words embeding

    Parameters:
        filename: name of the file that contains a word followed by 50 float point values( each seperated with a space)
                  in each of its lines
    Returns:
        table: The now populated hash table.
    """

    table = [None]*544721 # since expected number of inputs is known before hand the number 544721  was choosen as it gives a load factor close to .75
                          # and also because it is a prime number resulting in less overlapping when remainder is used.
    with open(filename, encoding ="utf8")as file:
        for line in file:
            values = line.split()
            name = values.pop(0)
            table = insert (table, name, values)
        return table


def main():

    start_time = time.time()  
    table = Get_Words("glove6Btxt") # the name in the quatation marks is the name of the file that while be used to get the words from
    print("--- %s seconds ---" % (time.time() - start_time))
    temp = average_distrubution_true(table)
    print(str(temp) + " is the average distribution")
    load_factor(table)
main()
