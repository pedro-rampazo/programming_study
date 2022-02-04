"""
Crie uma classe agenda  que pode armazenar 10 pessoas e seja capaz de realizar as seguintes operações:

    - void armazenaPessoa(String nome, int idade, float altura);
    - void removePessoa(String nome);
    - int buscaPessoa(String nome); // informa em que posição da agenda está a pessoa
    - void imprimeAgenda(); // imprime dados de todas as pessoas da agenda
    - void imprimePessoa(int index); // imprime os dados da pessoa que está na posição "i" da agenda 
"""
class Agenda:

    def __init__(self):
        self.__agenda_list = []

    
    def storePerson(self, name, age, height):
        if len(self.__agenda_list) <= 9:
            person_dict = {"name": name, "age": age, "height": height}
            self.__agenda_list.append(person_dict)

    
    def removePerson(self, name):
        for val in range(len(self.agenda_list)):
            if self.__agenda_list[val]["name"] == name:
                del self.__agenda_list[val]
                break
    
    
    def searchPerson(self, name):
        for val in range(len(self.agenda_list)):
            if self.__agenda_list[val]["name"] == name:
                print(f"A posição de {name} é: {val}")
                break
    

    def printAgenda(self):
        for val in range(len(self.__agenda_list)):
            self.printPerson(val)
    

    def printPerson(self, index):
        for key, mval in self.__agenda_list[index].items():
            print(f"{key}: {mval}")

registro_um = Agenda()
registro_um.storePerson("Pedro", 21, 1.75)
registro_um.storePerson("João", 27, 1.82)
registro_um.printAgenda()

