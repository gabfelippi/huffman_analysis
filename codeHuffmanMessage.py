import math

message = "MUITOBEM" #message to be codified
dict_coded_message = {"A":"1", "B":"001", "R":"000", "C":"011", "D":"0100", "!":"0101"} #dictionary of symbols and its codes (yep gonna do the huffman's tree by hand I don't know how to code it yet)

def symbolAbsoluteFrequency(message):
#A dictionary with every character of the message and its absolute frequency value
    message = list(message) #converts the string into a list of characters of the message
    counter = [] #opens a list of characters in the message
    absolute_frequency = {} #opens a dictionary of absolute frequencies (char:afreq)
    for symbol in message: #iterates the characters in the message
        if not symbol in counter: #appends the symbols in the counter list
            counter.append(symbol)
    for symbol in counter: #computes the absolute frequency of each character in the message
        absolute_frequency.setdefault(symbol, message.count(symbol))
    return absolute_frequency #returns a dictionary of characters and its absolute frequency values

def symbolRelativeFrequency(message):
#A dictionary with every character of the message and its relative frequency value
    absolute_frequency = symbolAbsoluteFrequency(message) #gets the absolute frequence value of the message
    relative_frequency = {} #dictionary of relative frequencies (char:rfreq)
    message_lenght = len(message) #defines the total lenght of the message
    for symbol in absolute_frequency: #computes the relative frequency of each character in the message
        p = absolute_frequency.get(symbol) / message_lenght #gets the value of each key in the absolute frequency of coded symbols and divise by the lenght of the message 
        relative_frequency.setdefault(symbol, p) #defines the key as the symbol and the value as the division of absolute frequency by the lenght of the message
    return relative_frequency #returns a dictionary of characters and its relative frequency values

def symbolLenght(dictionary):
#A list with the lenght of every coded symbol in the dictionary code
    coded_symbol_lenght = [] #list of lenghts of coded symbols in the dictionary code
    for value in dictionary: #iterates to get the lenght of each coded symbol in the dictionary code
        coded_symbol_lenght.append(len(dictionary.get(value))) #gets the lenght of the value of each key in the dictionary code and appends it in a list
    return coded_symbol_lenght #returns the list of lenghts of each coded symbol in the dicitonary code

def meanCodeLenght(dictionary, message):
#The mean code lenght of a message and its dictionary code
    coded_symbol_lenght = symbolLenght(dictionary) #gets the lenght of all symbols in the dictionary
    frequency = symbolRelativeFrequency(message) #gets the relative frequencies of the given message
    frequency = list(frequency.values()) #gets all the values of the relative frequencies and do a list of them
    mean_code_lenght = [] #opens a list to get the code lenght
    for i, j in zip(frequency, coded_symbol_lenght): #iterates the frequency to the code lenght
        mean_code_lenght.append(i * j) #multiplies the frequency to the code lenght
    return sum(mean_code_lenght) #returns a sum of all code lenghts

def entropy(message):
#The entropy of a message
    frequency = symbolRelativeFrequency(message) #gets the relative frequencies of the given message
    frequency = list(frequency.values()) #gets all the values of the relative frequencies and do a list of them
    entropy = [] #opens a list to get the entropy of each code
    for value in frequency: #iterates the relative frequencies to get its entropy
        entropy.append(value * math.log(value, 2)) #do the f*ckin log2
    return sum(entropy) * (-1) #returns the sum of the entropies

def efficiency(message, dictionary):
#The efficiency of the coded message
    code_entropy = entropy(message) #gets the entropy of the message
    mean_code_lenght = meanCodeLenght(dictionary, message) #gets the mean lenght of the code
    return code_entropy / mean_code_lenght #returns the efficiency of the code

print(f'A mensagem é: {message}')
print(f'A frequência absoluta dos símbolos é: {symbolAbsoluteFrequency(message)}')
print(f'A frequência relativa dos símbolos é: {symbolRelativeFrequency(message)}')
print(f'O comprimento do código dos símbolos são: {sum(symbolLenght(dict_coded_message))}')
print(f'O comprimento médio dos símbolos do código é: {meanCodeLenght(dict_coded_message, message):.2%}')
print(f'A entropia do código é: {entropy(message):.2%}')
print(f'A eficiência do código é: {efficiency(message, dict_coded_message):.2%}')