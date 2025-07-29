# import modułów
try:
    import lastRace
    import seasons
    import drivers
    import constructors
    import circuits
except ImportError:
    print(f"Błąd podczas importowania modułów.")
    exit(1)

# menu
print("""
1 - wyniki ostatniego wyścigu
2 - lista sezonów
3 - wyszukiwarka kierowców
4 - wyszukiwarka konstruktorów
5 - lista torów
""")
try:
    choice = int(input("Wybierz opcję: "))

    if choice == 1:
        lastRace.showResults()
    elif choice == 2:
        seasons.showList()
    elif choice == 3:
        drivers.search()
    elif choice == 4:
        constructors.search()
    elif choice == 5:
        circuits.showList()
    else:
        raise Exception("Błędna opcja!")
except ValueError:
    print("Błędna opcja!")