def magic():
    # yield 1
    # yield 2
    # yield 3
    counter = 0
    while True:
        yield counter
        counter += 1
        if counter >5:
            # return
            raise StopIteration('Python is cool')

x = magic()

# for i in magic():
#     print(i)

# for i in magic():
#     for j in magic():
#         print(i, j)

# print(next(x))
# print(next(x))
# print(next(x))

# for item in x:
#     print(item)

r = sum((1,2))
print(r)
r = sum([1,2])
print(r)
r = sum({1:'ala',2:'ola'})
print(r)
r = sum([x for x in range(10)])
print(r)
r = sum([1 for _ in range(10)])
print(r)
r = sum({l:None for l in range(10)})
print(r)
r = {l:None for l in range(10)}
print(r)
r= sum(x for x in range(10))
print(r)
print(list(x for x in range(10)))
print(tuple(x for x in range(10)))
print(tuple(x for x in range(20)))
