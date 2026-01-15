from rpg01 import *


numero = input("inserisci un numero: ")
numero = int(numero)

if (numero%2 ==0 ) :
    {
        print("il numero è pari")
    }
else :
    {
        print("il numero è dispari")
    }


titolo = "comedormire"
autore = "marcaurelio"

print(f"Titolo: {titolo} , Autore:{autore}")

print(autore[:6])


a = 3
y = 30


miaLista = [1,2,3,4,5]
print(miaLista[:2])

# print((a > banana) or ( a < y)   ) 

while numero < 10 :
    print(numero)
    numero+=1
else:
    print("do") 


l = []
for i in range(10 , 30 ,2):
    if i > 25 :
        break
    l.append(i)
print(l)



numeri = [1,2,3,4,5,6,7,8,9]

numeri = [i * i for i in numeri if i % 2 == 1]

print(numeri)
print(len(numeri))

l = [f for f in range(10,30) if f<25 and f % 2 ==1] #dispari
print(l)

l = [f for f in range(10,30) if f<25 and f % 2 ==0] #pari
print(l)



s = "python"
myDict = {i : ord(i) for i in s}
print(myDict)




y = 12
z=5
def trasforma() :
    global z
    y=10
    z=7
    print(y)
    print(z)
    
trasforma()
print(y)
print(z)



def outer():
    y=20
    def inner():
        nonlocal y
        y = 50
        print(y)


    inner()
    print(y)

outer()


class MyClass():
    counter=0

    def __init__(self):
        MyClass.counter +=1

    @classmethod
    def numIniz(cls):
     print(f"Il numero di volte che la classe è stata inizializzata è: {cls.counter}")
    
    @staticmethod
    def somma(x , y):
      z = x + y
      print(f"La somma dei numeri inseriti è {z}")
   
    """
    Il decoratore classmethod viene utilizzato nel momento in cui vogliamo fare riferimento a un metodo della classe senza 
    inizializzarla magari per avere un parametro interno o magari per richiamare un metodo specifico che non deve lavorare a livello di istanza, 
    questo viene indicato dal fatto che per convenzione i metodi segnati dal decoratore classmethod accettando sempre come valore cls 
    ovvero che fà riferimento all'intera classe

    invece il decoratore staticmethod non fa riferimento ne alla classe che alla singola istanza, lo si potrebbe definire una libreria,
    esempio mettiamo caso che io voglia eseguire una radice quadrata ma ho bisogno della libreria esterna math che ha il metodo math.sqrt(),
    in questo caso posso richiamare il metodo e fornigli i valori senza fare riferimento alla classe stessa math o alla singola istanza 
    che rappresenta il metodo sqrt. In conclusione è utile per eseguire operazioni o servizi in maniera minimale , 
    come sopra per fare calcoli ad esempio o scrivere a schermo dei messagi specifici
    """
   
m1 = MyClass()
m2 = MyClass()
MyClass().somma(3,5)
MyClass.numIniz()


class Superiore():
    @staticmethod
    def supscrivo():
        print("da in cima")
class Inferiore(Superiore):
    @staticmethod
    def infscrivo():
        print("da sottoclasse")

class SuperInf(Inferiore):
    @staticmethod
    def superinfscrivo():
        print("dalla base")
    


m3 = SuperInf()
m2 = Inferiore()
m1 = Superiore()

m3.superinfscrivo()
m3.infscrivo()
m3.supscrivo()

# m2.superinfscrivo() non può
m2.infscrivo()
m2.supscrivo()

# m1.superinfscrivo() non può
# m1.infscrivo()
m1.supscrivo()

class Superiore():
    def __init__(self, messaggio):
        self.messaggio = messaggio
    def printmessaggio(self):
        print(self.messaggio)

class Inferiore(Superiore):
    def __init__(self, messaggio, valore):
        super().__init__(messaggio)
        self.valore = valore

    def calcolodivisione(self):
        x = float(input("inserisci il numero per il quale vuoi trovare la metà: "))
        x=x/2
        print(f"La metà del numero dato è: {x}")

m1 = Inferiore("ciao" , 30)

m1.printmessaggio()
m1.calcolodivisione()



class MyClass():
    def __init__(self, messaggio):
        self.amessaggio = messaggio
    
    def get(self):
        return (self.amessaggio)

    def set(self , nuovomessaggio):
        self.amessaggio = nuovomessaggio

    attributo = property(get , set)


m1 = MyClass("ciao")
print(m1.get())

m1.attributo = "nero"
print(m1.get())
m1.attributo="neri"
print(m1.attributo)
m1.set("ciao")
print(m1.get())


class MyClass():
    def __init__(self, messaggio):
        self.amessaggio = messaggio
    
    @property
    def attr(self):
        return (self.amessaggio)

    @attr.setter
    def attr(self , nuovomessaggio):
        self.amessaggio = nuovomessaggio

m1 = MyClass("ciao")
print(m1.attr)
m1.attr= "bello"
print(m1.attr)


def f(a , b):
    return a // b

try:
    print(f(4,0))
except ZeroDivisionError as eccezionebrutta:
    print(eccezionebrutta.args) 



class MyClass:
    def __new__(cls, baba):
        cls.baba = baba
        print(f"Chiamato __new__{cls.baba}")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        
        print(f"Chiamato __init__{ value}") 
        

# Creazione dell'oggetto
obj = MyClass(10)


lista = []
i = 1

while i < 300 :
    lista.append(i)
    i *= 2

print(lista)

class Iteratore():
    def __iter__(self):
        self.myattribute = 2
        return self
    def __next__(self):
        if self.myattribute < 300 :
            n = self.myattribute
            self.myattribute *= 2
            return n
        else :
            raise StopIteration

myiter = iter(Iteratore())

for i in myiter:
    print(i)

     
