#### create alices private and public keys
#### encrypt alice's private key and decrypt it with


def DecimalToBinary(e):
    
    if e >= 1: ## if this statement wasnt here this would contiue indefinatly
               #### multiple values of e are created
               
        DecimalToBinary(e // 2)
    ### converts each value of e to bininary then appends array 
    arr.append(e%2)
    







def encryption(p,q,n,phi,d,arr,base):
    
    
    DecimalToBinary(e)
    if arr[0]==0:
        arr.pop(0)
    
    
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









def decryption(p,q,n,phi,e,result,arr):


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
            if i==0:
                continue
            
            result=(result**2)%n
                
            

        if val==1:
            if i==0:
                continue
                
            result= (result**2*base)%n
       
    return(result)
  







while True:

    base=int(input('key to encrypt: '))
    arr=[]
    p=89
    q=83
    n=p*q
    d=1081
    phi=(p-1)*(q-1)
    e=257

    x=encryption(p,q,n,phi,d,arr,base)
    print('Alices encrypted signature with her private key: ', x)

    arr=[]
    z=decryption(p,q,n,phi,e,x,arr)
    print('Alices decrypted signature with her public key: ', z )



