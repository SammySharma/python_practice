#backtracking
def backtracking(i:int,n:int):
    if i < 1:
        return
    backtracking(i-1,n)
    print(i)


if __name__=="__main__":
    backtracking(3,3)


