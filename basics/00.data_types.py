# comment more info: https://learnxinyminutes.com/docs/python3/

2 + 2    # hit enter & you shall see the result

four = 2 + 2    # we can keep it in the memory


# assignment
imie = "Adam"

len(imie) 
4

# some functions only make sense when used with data:
imie.upper()
# 'ADAM'
imie.swapcase()
# 'aDAM'
imie.find('a')
# 2
imie.find('d')
# 1
imie.find('m')
# 3
imie.find('A')
# 0

imie[0] # what is the letter at the first place in the string
# "A"

# An expression: combining some variables together. Expression has a value that can be used 
powitanie = "Cześć " + imie + "!" 

wiek = 25

w_kieszeni = 3.50
print(type(w_kieszeni))

print(f"{imie} ma {wiek} lat i {w_kieszeni} zł w kieszeni")

goscie = ["Paula", "Aga", "Kamil"]

goscie[0]
goscie[1]

goscie.append("Janusz")
goscie.<tab><tab>
# goscie.append(   goscie.extend(   goscie.remove(
# goscie.clear(    goscie.index(    goscie.reverse(
# goscie.copy(     goscie.insert(   goscie.sort(
# goscie.count(    goscie.pop(      
goscie
# ['Paula', 'Aga', 'Kamil', 'Janusz']
goscie.reverse()
goscie
# ['Janusz', 'Kamil', 'Aga', 'Paula']
goscie.sort()
goscie
# ['Aga', 'Janusz', 'Kamil', 'Paula']
goscie.append("Klemens")
goscie
# ['Aga', 'Janusz', 'Kamil', 'Paula', 'Klemens']
goscie.pop()
# 'Klemens'
goscie
# ['Aga', 'Janusz', 'Kamil', 'Paula']







studentka = {
        "imie" : "Oksana",
        "wiek" : 20,
        "zainteresowania": ["dyskoteki", "chłopaki", "ogólnie takie takie", "ale w miarę to nauka mnie najbardziej kręci"]
        }

# compose / substitute, just like math:
print(goscie[0])

index = 0

goscie[index] # watch for correct "[", "("
# [] is for a position within list, () is for calling functions, like len("me") or grouping expressions like c*(a+b) 

len(goscie[index])
