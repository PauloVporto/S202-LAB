import sys
from teacher_crud import TeacherCRUD
from database import Database

class CLI:
    def __init__(self):
        self.db = Database("bolt://localhost:7687")
        self.teacher_crud = TeacherCRUD(self.db)

    def menu(self):
        print("1. Create Teacher")
        print("2. Read Teacher")
        print("3. Update Teacher")
        print("4. Delete Teacher")
        print("5. Exit")
        choice = input("Enter choice: ")
        return choice

    def run(self):
        while True:
            choice = self.menu()
            if choice == '1':
                name = input("Enter name: ")
                ano_nasc = int(input("Enter ano_nasc: "))
                cpf = input("Enter cpf: ")
                self.teacher_crud.create(name, ano_nasc, cpf)
            elif choice == '2':
                name = input("Enter name: ")
                print(self.teacher_crud.read(name))
            elif choice == '3':
                name = input("Enter name: ")
                new_cpf = input("Enter new cpf: ")
                print(self.teacher_crud.update(name, new_cpf))
            elif choice == '4':
                name = input("Enter name: ")
                self.teacher_crud.delete(name)
            elif choice == '5':
                self.db.close()
                sys.exit()
            else:
                print("Invalid choice")

if __name__ == "__main__":
    cli = CLI()
    cli.run()
