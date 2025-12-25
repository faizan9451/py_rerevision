"""def recursion(n):
    if n==0 or n==1:
        return 1
    return n*recursion(n-1)
  
print(recursion(5))"""




def listing(list,idx=0):
    if list == len(list):
        return
    
    listing(list,idx+1)


    

hello=["faizan",2,3,4,5]
listing(hello)    