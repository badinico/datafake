import argparse
import time
import faker as fk
from colorama import init, Fore
import sqlite3

fake = fk.Faker()
init(autoreset=True)  # Inicializar colorama con autoreset=True para reiniciar los estilos después de cada impresión.

count = 0

def insert(sleep_time=1.0):  # Cambiar el tipo de sleep_time a float
    while True:
        try:
            email = fake.email()
            password = fake.password()
            name = fake.name()
            global count
            count += 1
            print(f"{Fore.GREEN}Inserting {count} data...{Fore.RESET}")
            time.sleep(sleep_time)
            print(f"{Fore.YELLOW}Data inserted!{Fore.RESET}")
            print(f"Email: {Fore.CYAN}{email}{Fore.RESET}")
            print(f"Password: {Fore.CYAN}{password}{Fore.RESET}")
            print(f"Name: {Fore.CYAN}{name}{Fore.RESET}")
            print()
            
            #TIENE QUE GUARDAR REGISTRO POR REGISTRO EN UNA DBSQLITE
            db = sqlite3.connect("test.db")
            cursor = db.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT, name TEXT)")
            cursor.execute("INSERT INTO users VALUES (?,?,?)", (email, password, name))
            db.commit()            
        except KeyboardInterrupt:
            print(f"{Fore.RED}Program stopped!{Fore.RESET}")
            break

def main():
    parser = argparse.ArgumentParser(description="Generate fake data with a specified sleep time.")
    parser.add_argument("sleep_time", type=float, help="Time to sleep between data inserts")  # Cambiar el tipo a float
    args = parser.parse_args()

    insert(args.sleep_time)

if __name__ == "__main__":
    main()
