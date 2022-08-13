import math

dict_coded_message = {"1":"0000", "2":"0000", "3":"0100", "4":"0000", "5":"0000", "6":"0000", "7":"0000", "8": "0000", "9":"00000"} #dictionary of symbols and its codes (yep gonna do the huffman's tree by hand I don't know how to code it yet)
frequency_symbols = {"1":0.24, "2":0.16, "3":0.13, "4":0.12, "5":0.09, "6":0.08, "7":0.07, "8":0.06, "9":0.05}

def symbolLenght(dictionary):
#A list with the lenght of every coded symbol in the dictionary code
    coded_symbol_lenght = [] #opens a list of lenghts of coded symbols in the dictionary code
    for value in dictionary: #iterates to get the lenght of each coded symbol in the dictionary code
        coded_symbol_lenght.append(len(dictionary.get(value))) #gets the lenght of the value of each key in the dictionary code and appends it in a list
    return coded_symbol_lenght #returns the list of lenghts of each coded symbol in the dicitonary code

def meanCodeLenght(dictionary, frequency_symbols):
#The mean code lenght of a message and its dictionary code
    coded_symbol_lenght = symbolLenght(dictionary) #gets the lenght of all symbols in the dictionary
    frequency = list(frequency_symbols.values()) #gets all the values of the relative frequencies and do a list of them
    mean_code_lenght = [] #opens a list to get the code lenght
    for i, j in zip(frequency, coded_symbol_lenght): #iterates the frequency to the code lenght
        mean_code_lenght.append(i * j) #multiplies the frequency to the code lenght
    return sum(mean_code_lenght) #returns a sum of all code lenghts

def entropy(frequency_symbols):
#The entropy of a message
    frequency = list(frequency_symbols.values()) #gets all the values of the relative frequencies and do a list of them
    entropy = [] #opens a list to get the entropy of each code
    for value in frequency: #iterates the relative frequencies to get its entropy
        entropy.append(value * math.log(value, 2)) #does the f*ckin log2
    return sum(entropy) * (-1) #returns the sum of the entropies

def efficiency(frequency_symbols, dictionary):
#The efficiency of the coded message
    code_entropy = entropy(frequency_symbols) #gets the entropy of the code
    mean_code_lenght = meanCodeLenght(dictionary, frequency_symbols) #gets the mean lenght of the code
    return code_entropy / mean_code_lenght #returns the efficiency of the code

print(f'O comprimento do código dos símbolos é: {sum(symbolLenght(dict_coded_message))}')
print(f'O comprimento médio dos símbolos do código é: {meanCodeLenght(dict_coded_message, frequency_symbols):.2f}')
print(f'A entropia do código é: {entropy(frequency_symbols):.2f}')
print(f'A eficiência do código é: {efficiency(frequency_symbols, dict_coded_message):.2%}')