from abc import ABC, abstractmethod

class Transport(ABC):
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return 'Se ha despachado por camion'
    
class Ship(Transport):
    def deliver(self):
        return 'Se ha despachado por barco'

class Logistic(ABC):

    def plan_delivery(self):
        transport = self.createTransport()
        print(transport.deliver())

    def createTransport(self) -> Transport:
        pass

class RoadLogistic(Logistic):
    def createTransport(self) -> Transport:
        return Truck()
    
class SeaLogistic(Logistic):
    def createTransport(self) -> Transport:
        return Ship()
    
if __name__ == '__main__':
    ship = RoadLogistic()
    ship.plan_delivery()