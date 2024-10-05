import pickle

a = {"name": "John", "age": 30, "city": "New York"}
# with open("results.txt", "w") as f:
#     f.write(str(a))

# with open("results.txt", "r") as f:
#     data = f.read()
#     print(data)
#     print(type(data))

# with open("results.txt", "wb") as f:
#     pickle.dump(a, f)

with open("results.txt", "rb") as f:
    data = pickle.load(f)
    print(data)
    print(type(data))
