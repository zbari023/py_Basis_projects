
# for Schleife
for x in range(5):   # im Kopf steht ein range-funktion, die Start, Ende und den zählerschritt enthält
    print(x)
#
lag=["python","php","css","html"]
for y in lag:
    print(y,end=" ") # in horizontal way

# other way
lag=["python","php","css","html"]
for y in range(len(lag)):
    print(lag[y],end=" ")