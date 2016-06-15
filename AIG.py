import random
import math
import copy

####### Zmienne #######

punkt=[]
listapunktow=[]
okrag=[]
populacja = []
tempPopulacja = []
suma = float("inf")
wynik=[]
prawdopobienstwo = 0
liczba_osobnikow = 0


####### Parametry #######

print('\nMenu: \n')
print('  1. Prawdopodobieństwo równe 50%')
print('  2. Prawdopodobieństwo równe 3%')
print('  3. Prawdopodobieństwo równe 0.1%')
opcja = input('\nWybierz prawdopodobieństwo: ')
liczba_osobnikow = input('Podaj początkową liczbę osobników(min. 2): ')

if (opcja == 1):
        prawdopobienstwo = 0.50
elif (opcja == 2):
        prawdopobienstwo = 0.03
elif (opcja == 3):
        prawdopobienstwo = 0.001


####### Funkcje #######

def krzyzowanie(*params):	
	if (random.random()>prawdopobienstwo):
		nowy1 = [params[0][0],params[1][1]]
		nowy2 = [params[1][0],params[0][1]]

		populacja.append(nowy1)
		populacja.append(nowy2)

def funkcja():
	global suma
	tmpsuma = 0

	
	for mojokrag in populacja:
		for mojpkt in listapunktow:
			odleglosc = math.sqrt((mojpkt[0]-mojokrag[1][0])**2+(mojpkt[1]-mojokrag[1][1])**2)
			tmpsuma = tmpsuma + abs(mojokrag[0]-odleglosc)**2
		if tmpsuma<suma:
			suma = tmpsuma
			wynik.append(mojokrag)
	return wynik


for x in range (0,10):
	punkt.append(round(random.random(),3))
	punkt.append(round(random.random(),3))
	
	listapunktow.append(punkt)

	punkt=[]

for x in range(0,int(liczba_osobnikow)):
	punkt.append(round(random.random(),3))
	punkt.append(round(random.random(),3))

	okrag.append(round(random.random(),3))
	okrag.append(punkt)

	populacja.append(okrag)
	punkt=[]
	okrag=[]

####### Main #######

print ('\nWylosowane punkty:\n',listapunktow)
nowasuma = suma
while True:
	tempPopulacja = copy.deepcopy(populacja)

	while True:
		if not tempPopulacja:
			break
		osobnik1=random.choice(tempPopulacja)
		tempPopulacja.remove(osobnik1)
		osobnik2=random.choice(tempPopulacja)
		tempPopulacja.remove(osobnik2)
	
		krzyzowanie(osobnik1,osobnik2)
	
	result = funkcja()
	if abs(nowasuma-suma)<= 0.3:
		print ('\n\nRozwiązanie:\n\n\tOkrąg [Promień, Środek[x,y]]: ',result)
		break
	
	nowasuma=suma

print ('\n\tMinimalna wartosc wynosi:',suma)
print ('\n\tLiczba osobników w populacji:',len(populacja))

	
