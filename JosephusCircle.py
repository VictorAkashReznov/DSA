def josephus_circle(n,k):
    if(n==1):
        return 0
    return (josephus_circle(n-1,k)+k)%n

k=josephus_circle(4,2)
print(k)
    
        
    
