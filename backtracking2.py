"""Backtracking in reverset n to 1"""

def backtracking(i:int,n:int)->None:
    if n<1:
        return
    print(n)
    backtracking(i,n-1)



if __name__=="__main__":
    backtracking(1,5)

print("------------------------------------------------------------------------")


