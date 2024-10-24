def backtracking2(i: int, n: int) -> None:
    if i<1:
        return
    backtracking2(i-1, n)  # Decrement i instead of n
    print(i)

if __name__ == "__main__":
    backtracking2(5, 5)  # Call with i starting at 5