'''
Created on 08-Apr-2020

@author: Deepak Shajan
'''
import math

def convert_to_binary__array(number, max_bit_size):
    
    binary_value_short = bin(number)[2:] # [2:] to chop off the "0b" part 
    binary_value_long = []
    
    for _ in range(max_bit_size + 1 - len(binary_value_short)): # fill zeros to the left
        binary_value_long.append(0)
    for c in binary_value_short: # append the actual binary value
        binary_value_long.append(1 if c=='1' else 0)
    
    return binary_value_long

def convert_to_binary_array_by_concat(first_number, second_number, max_bit_size):
    
    input_number_binary_long = []
    first_binary_value_short = bin(first_number)[2:] # [2:] to chop off the "0b" part 
    second_binary_value_short = bin(second_number)[2:]
    
    for _ in range(max_bit_size-len(first_binary_value_short)): # fill zeros to the left
        input_number_binary_long.append(0)
    for c in first_binary_value_short: # append the actual binary value
        input_number_binary_long.append(1 if c=='1' else 0)
    for _ in range(max_bit_size-len(second_binary_value_short)):
        input_number_binary_long.append(0)
    for c in second_binary_value_short:
        input_number_binary_long.append(1 if c=='1' else 0)
    
    return input_number_binary_long


def convert_binary_array_to_decimal(binary_array):
    
    decimal_value = 0;
    highest_index = len(binary_array)-1
    
    for i in range(highest_index+1):
        decimal_value += math.pow(2, i)*binary_array[highest_index-i]
        
    return int(decimal_value)

def convert_to_binary_array(approximate_binary_array):
    
    binary_array = []
    for i in range(len(approximate_binary_array)):
        binary_array.append(0 if approximate_binary_array[i]<0.5 else 1)
    return binary_array
        

