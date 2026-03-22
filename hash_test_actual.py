import random


def hash_algorithm(messsage, modulo_value):
    ## improment: use a secure method for seed generation
    
    random.seed(123)
    
    # Initialize the hash value
    
    count=0
    
    hasharray=[]
    
    # Iterate over each character in the input string
    hashvalue=0
    for characters in message:
        
        

        
        # Update the hash value using a combination of bitwise operations
        # << bit shift left, >>bit shift right
       # Update the hash value using a combination of bitwise operations
        #>>bit shift right
       ## ^ is xor

        hashvalue = hashvalue ^((hashvalue >> 5) ^(hashvalue << 10) ^(ord(characters) + random.randint(0, 255)))
        hashvalue=(hashvalue * 31 + ord(characters)) 
        
        hashvalue=hashvalue**4% modulo_value

        
        
        hasharray.append(hashvalue)
           
     
    
   
    hexConversion = hex(sum(hasharray))[2:]  # Remove '0x' prefix

    while True:
        if len(hexConversion)>64:
            hexConversion=hexConversion[1:]
            
        else:
             break
   
    
    
    paddAmount = 64 - len(hexConversion)
   
    ##padding amount cant be negative 
    if paddAmount>0:
        
        
        # Generate random hexadecimal digits for padding
        padd = [hex(random.randint(0, 15))[2:] for i in range(paddAmount)]
       
            ##start at 0 step through 2 charachters at a time
        split_string = [hexConversion[i:i+2] for i in range(0, len(hexConversion), 2)]
        
        split_copy = split_string.copy()

        # Iterate over the copy
        for _ in padd:
            # Select a random element from padd and insert it into split_string
            split_string.insert(random.randint(0, len(split_string)), random.choice(padd))

            
        finalhash = ''.join(split_string)
    
    
        return finalhash


    else:

        return hexConversion



while True:
    message = input("Enter in stuff: ")
    modulo = 10**70
    x=hash_algorithm(message, modulo)
    
    print(x)
    
