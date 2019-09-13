# Napisz program kalkulator

# Jakie **dane** musimy znać?:
# dwie liczby
# operacja: + - * /
# wynik

# Jak **działa** kalkulator?
# **wprowadzamy** _liczby_
# **wprowadzamy** _operację_
# wykonujemy obliczenia (_na liczbach_, _w zależności_ od **operacji**)
# **wyświetlamy** wynik

# i/o: input, output: jakie dane wczytujemy? Jakie dane wyświetlamy?
# przetwarzanie: jakie operacje wykonujemy na danych


# zaślepkowe dane:
liczba1 = 2
liczba2 = 5
operacja = "+"
wynik = 7


def wyswietl_wynik(wynik):
  print(wynik) 
  # dlaczego print wewnątrz funkcji? czy to nie nadmiar? Nie, bo ... :)
  # -> https://github.com/sepandhaghighi/art
  # -> https://github.com/pwaller/pyfiglet

wyswietl_wynik(9)

def wprowadz_liczby():
  pass

# wersja 2. Zwraca poprawny wynik, ale tylko w jednym przypadku
def wykonaj_operacje(liczba1, liczba2, operacja):
  wynik = liczba1 + liczba2
  return wynik

  # od razu sprawdzamy
wynik = wykonaj_operacje(1, 2, '+')
print(wynik)



# Wersja 3. Prawie gotowa. Jak wykonać instrukcję w zalezności od podanej operacji?
def wykonaj_operacje_3(liczba1, liczba2, operacja):
  wynik = liczba1 + liczba2
  wynik = liczba1 - liczba2
  wynik = liczba1 * liczba2
  wynik = liczba1 / liczba2
  return wynik



