""" Recursion 
TC - O(N)
SC - O(N)
"""
def recursion(i:int,n:int):
    if i > n:
            return
    print("Recursion!")
    recursion(i+1,n)




if __name__=="__main__" :
    recursion(1,4)

#-----------------------------------------------------------------#

