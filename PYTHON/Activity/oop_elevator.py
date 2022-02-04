"""
Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio. A classe deve
armazenar o andar atual (térreo = 0), total de andares no prédio, excluindo o térro, capacidade do elevador, e quantas
pessoas estão presentes nele.

A classe deve também disponibilizar os seguintes métodos:

    - Inicializa: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores
    sempre começam no térreo);
    - Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
    - Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);   
    - Sobe: para subir um andar (não deve subir se já estiver no último andar);
    - Desce: para descer um andar (não deve descer se já estiver no térreo);
    - Encapsular todos os atributos da classe(criar os métodos set e get).
"""
class Elevator:

    def __init__(self, total_floors, elevator_capacity):
        self.current_floor = 0
        self.total_floors = total_floors
        self.elevator_capacity = elevator_capacity
        self.amount_people = 0
    

    def getCurrentFloor(self):
        return self.current_floor
    
    
    def getTotalFloors(self):
        return self.total_floors
    

    def getElevatorCapacity(self):
        return self.elevator_capacity
    

    def getAmountPeople(self):
        return self.amount_people
    
    
    def setCurrentFloor(self, new_current_floor):
        self.current_floor = new_current_floor
    

    def setTotalFloors(self, new_total_floors):
        self.total_floors = new_total_floors
    

    def setElevatorCapacity(self, new_elevator_capacity):
        self.elevator_capacity = new_elevator_capacity


    def setAmountPeople(self, new_amount_people):
        self.amount_people = new_amount_people


    def getinElevator(self):
        if self.amount_people < self.elevator_capacity:
            self.amount_people += 1
            print("A person entered the elevator")
        else:
            print("The aren't people in elevator!")
    

    def getoffElevator(self):
        if self.amount_people > 0:
            self.amount_people -= 1
            print("Someone came out in the elevator")
        else:
            print("The elevator is already empty!")
    

    def upElevator(self):
        if self.current_floor < self.total_floors:
            self.current_floor += 1
            print(f"Floor {self.current_floor}")
        else:
            print("The elevator is already in the last floor!")
    

    def downElevator(self):
        if self.current_floor > 0:
            self.current_floor -= 1
            print(f"Floor {self.current_floor}")
        else:
            print("The elevator is on the ground floor!")
    