#defining spearman correlateion function
def spearman(n,x,y):
    #createing sorted array to give rank to numbers
    s_x = sorted(x)
    s_y = sorted(y)
    
    #creating dictionary to arrange numbers corresponding to rank
    rank_x = {}
    rank_y = {}
    
    #.index function in sorted array provides the rank to each element of x
    for i in x:
        rank_x[i] = s_x.index(i)+1
    for i in y:
        rank_y[i] = s_y.index(i)+1
    
    #calculation of di**2 --> di = rank of x - rank of y
    di=0
    for i in range(n):
        di = di + (rank_x[x[i]]-rank_y[y[i]])**2
    
    #main formulae  of spearmann rank correlation
    num = 6*di
    den = (n**3)-n
    out = 1 - (num/den)
    
    return out
        
  
n = int(input())
X = list(map(float,input().split()))
Y = list(map(float,input().split()))

print(round(spearman(n,X,Y),3))
       
 
