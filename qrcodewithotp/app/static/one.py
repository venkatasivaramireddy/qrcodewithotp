n=input()
lista=[]
for i in range(int(n)):
    lista.append(input())

dictionary={}

for i in range(int(n)):
    if lista[i] in dictionary:
        dictionary[lista[i]]=dictionary.get(lista[i])+1
    else:
        dictionary[lista[i]]=1
for w in sorted(dictionary, key=dictionary.get, reverse=True):
      print (w)