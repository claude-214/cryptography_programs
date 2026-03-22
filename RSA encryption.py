




def DecimalToBinary(e):
    
    if e >= 1: ## if this statement wasnt here this would contiue indefinatly
               #### multiple values of e are created
               
        DecimalToBinary(e // 2)
    ### takes the remainder value of e and appends array 
    arr.append(e%2)
    




def encryption(p,q,n,phi,e,arr,base):
    
    
    DecimalToBinary(e)
    ## removes the intial 0 at the start of the function
    if arr[0]==0:
        arr.pop(0)
    
    ##result will be the encrypted message and  base will be the original message
    result=base

    ### i is the index and val is the value in the array


    ### sqaure and multiply method
    for i,val in enumerate(arr):
        
        
        ### if value in array is 0 
        if val==0:
            if i==0:
                continue
            
            result=(result**2)%n
                
            

        if val==1:
            if i==0:
                continue
                
            result= (result**2*base)%n
        
   
    return(result)




#### decryption

def decryption(p,q,n,phi,d,result,arr):


    base=result
    
    result=base

    DecimalToBinary(d)
    ## initial 0 dosent do anything can be removed

    if arr[0]==0:
        arr.pop(0)





    ### i is the index and val is the value in the array


    ### sqaure and multiply method
    for i,val in enumerate(arr):
        
        
        ### if value in array is 0 
        if val==0:
            ##skips the first number in the array
            if i==0:
                continue
            
            result=(result**2)%n
                
            

        if val==1:
            #skips first number in the array
            if i==0:
                continue
                
            result= (result**2*base)%n
        
    return(result)
  





## both are primes and are close together making calculatation difficult
p=  79

q= 73

n=p*q ## 5767
phi=(p-1)*(q-1) ## 5616

### e must be an element of natural numbers up to phi
### e and phi must also have a greatest common divisor of 1
e =   97 ### satisfys both of these requirements


##private key  must have this protperty d*e must be congruent to 1 mod phi
#bobs private key
d=  193

while True:
    ## need to reset the array everytime
    arr=[]
    
    base=int(input("key to encrypt: "))

    x=encryption(p,q,n,phi,e,arr,base)
    print(x)

    arr=[]
    print(decryption(p,q,n,phi,d,x,arr))

