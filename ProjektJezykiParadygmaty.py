from database import Database
from datetime import datetime

def menu():
    print("\nWybierz opcje:")
    print("1. Wyswietl wszystkie wydatki")
    print("2. Wyswietl wydatki wedlug kategorii")
    print("3. Dodaj nowy wydatek")
    print("4. Usun wydatek")
    print("5. Edytuj wydatek")
    print("6. Srednie miesieczne wydatki")
    print("7. Zakoncz")

def main():
    db = Database('monitorWydatkow.db')
    db.connect()
    db.create_table()

    while True:
        menu()
        wybor = input("Wybierz numer: ")

        if wybor == '1':
            wydatki = db.fetch_all_wydatki()
            print("\nWszystkie wydatki:")
            for wydatek in wydatki:
                print(wydatek)

        elif wybor == '2':
            kategorie = db.fetch_all("SELECT DISTINCT kategoria FROM wydatki")
            print(f"\nDostepne kategorie: ")
            for kategoria in kategorie:
                print(kategoria)
            kategoria = input("Podaj nazwe kategorii: ")
            wydatek_kategoria = db.fetch_all("SELECT * FROM wydatki WHERE kategoria = ?", (kategoria,))
            print(f"\nWydatki w kategorii {kategoria}:")
            for wydatek in wydatek_kategoria:
                print(wydatek)



        elif wybor == '3':
            kategorie = db.fetch_all("SELECT DISTINCT kategoria FROM wydatki")
            print(f"\nDostepne kategorie: ")
            for kategoria in kategorie:
                print(kategoria)
            kategoria = input("Podaj nazwe kategorii: ")
            kwota = float(input("Podaj kwote: "))
            data = input("Podaj date (rrrr-mm-dd): ")
            db.add_wydatek(kategoria, kwota, data)
            print("\nNowy wydatek zostal dodany.")


        elif wybor == '4':
            lista = []
            print("Usuwanie wydatku")
            kategorie = db.fetch_all("SELECT DISTINCT kategoria FROM wydatki")
            print(f"\nDostepne kategorie: ")
            for kategoria in kategorie:
                print(kategoria)
            kategoria = input("Podaj nazwe kategorii: ")
            wydatek_kategoria = db.fetch_all("SELECT * FROM wydatki WHERE kategoria = ?", (kategoria,))
            print(f"\nWydatki w kategorii {kategoria}:")
            for wydatek in wydatek_kategoria:
                print(wydatek)
                lista.append(int(wydatek[0]))
            id = int(input("Podaj numer id: "))
            status = 0;
            for id1 in lista:
                if (id == id1):
                    db.deleta_wydatki(id)
                    status = 1
                    break
                else:
                    status = 0

            if (status==1):
                print(f"\nUsunieto wydatek.")
            else:     
                print(f"\nPodaj poprawne ID")


        elif wybor == '5':
            lista = []
            print("Edycja wydatku")
            kategorie = db.fetch_all("SELECT DISTINCT kategoria FROM wydatki")
            print(f"\nDostepne kategorie: ")
            for kategoria in kategorie:
                print(kategoria)
            kategoria = input("Podaj nazwe kategorii: ")
            wydatek_kategoria = db.fetch_all("SELECT * FROM wydatki WHERE kategoria = ?", (kategoria,))
            print(f"\nWydatki w kategorii {kategoria}:")
            for wydatek in wydatek_kategoria:
                print(wydatek)
                lista.append(int(wydatek[0]))
            id = int(input("Podaj numer id: "))
            status = 0;
            for id1 in lista:
                if (id == id1):
                    kat = input("Podaj nowa kategorie: ")
                    kwo = input("Podaj nowa kwote: ")
                    data = input("Podaj nowa data(rrrr-mm-dd): ")
                    db.update_wydatek(id,kat,kwo,data)
                    status = 1
                    break
                else:
                    status = 0

            if (status==1):
                print(f"\nEdytowano wydatek.")
            else:     
                print(f"\nPodaj poprawne ID")
            
        elif wybor == '6':
            print("\nSrednie miesieczne wydatki:")
            x= db.get_avg_monthly()
            for y in x:
                print(y)

        elif wybor == '7':
            print("Zamykanie programu, wcisnij dowolny klawisz")
            break

        else:
            print("Nieprawidlowy wybor. Sprobuj ponownie.")

    db.close()



if __name__ == '__main__':
    main()
