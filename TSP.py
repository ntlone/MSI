import random
miasta = {  'Bydgoszcz': {'Gdańsk': 155, 'Olsztyn': 195, 'Warszawa': 246, 'Łódź':197, 'Poznań': 118, 'Szczecin': 253, 'Koszalin': 186},
            'Gdańsk': {'Koszalin': 176, 'Olsztyn': 148, 'Bydgoszcz': 155},
            'Olsztyn': {'Gdańsk': 148,'Warszawa': 191,'Bydgoszcz': 195},
            'Warszawa': {'Olsztyn': 191,'Łódź': 129,'Bydgoszcz': 246, 'Białystok': 192, 'Lublin': 167, 'Kielce': 168},
            'Łódź': {'Warszawa': 129,'Poznań': 204,'Bydgoszcz': 197, 'Kraków': 209, 'Kielce': 140},
            'Poznań': {'Łódź': 204,'Szczecin': 213,'Bydgoszcz': 118},
            'Szczecin': {'Poznań': 213,'Koszalin': 148,'Bydgoszcz': 253},
            'Koszalin': {'Szczecin': 148,'Gdańsk': 176,'Bydgoszcz': 186},
            'Białystok': {'Olsztyn': 209,'Lublin': 233,'Warszawa': 192},
            'Lublin': {'Białystok': 233,'Rzeszów': 152,'Warszawa': 167,'Kielce': 155},
            'Rzeszów': {'Lublin': 152, 'Kraków': 160, 'Kielce': 145},
            'Kielce': {'Rzeszów': 145, 'Lublin': 155, 'Kraków': 110, 'Łódź': 140, 'Warszawa': 168},
            'Kraków': {'Łódź': 209,'Kielce': 110,'Rzeszów': 160} }


def najkrotsza_trasa(miasta, M_poczatkowe, M_koncowe, droga=None):
        if droga is None:
            droga = []
        droga = droga + [M_poczatkowe]
        if M_poczatkowe == M_koncowe:
            return droga
        if M_poczatkowe not in miasta:
            return None
        najkrotsza = None
        for wezel in miasta[M_poczatkowe]:
            if wezel not in droga:
                M_poczatkowe = wezel
                nowa_droga = najkrotsza_trasa(miasta, M_poczatkowe, M_koncowe, droga)
                if nowa_droga:
                    if len(nowa_droga) == len(miasta):
                                        return nowa_droga
        return najkrotsza

print('\nProblem Komiwojażera\n')
print('--------------------------')
print('Lista dostępnych miast: ')
print('--------------------------')
for value in miasta.keys() :
    print ('   * ' + value)
print("\n")

M_poczatkowe = input("Podaj miasto poczatkowe: ")
M_koncowe = input("Podaj miasto koncowe: ")

path = []

b = najkrotsza_trasa(miasta, M_poczatkowe, M_koncowe)
a = 'Najkrotsza trasa ' + M_poczatkowe + ' - ' + M_koncowe + ': '

print(a + str(b))
print()
