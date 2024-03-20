from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass
    @abstractmethod
    def box(self):
        pass

class PizzaNapolitana(Pizza):
    def prepare(self):
        print('Esta preparando la pizza napolitana')

    def bake(self):
        print('Esta horneando')
    
    def cut(self):
        print('Esta porcionando')
    
    def box(self):
        print('Esta alistando')

class PizzaMargarita(Pizza):
    def prepare(self):
        print('Esta preparando la pizza Margarita')

    def bake(self):
        print('Esta horneando')
    
    def cut(self):
        print('Esta porcionando')
    
    def box(self):
        print('Esta alistando')

class PizzaPepperoni(Pizza):
    def prepare(self):
        print('Esta preparando la pizza Pepperoni')

    def bake(self):
        print('Esta horneando')
    
    def cut(self):
        print('Esta porcionando')
    
    def box(self):
        print('Esta alistando')

class PizzaVegetariana(Pizza):
    def prepare(self):
        print('Esta preparando la pizza Vegetariana')

    def bake(self):
        print('Esta horneando')
    
    def cut(self):
        print('Esta porcionando')
    
    def box(self):
        print('Esta alistando')

class PizzaHawaiana(Pizza):
    def prepare(self):
        print('Esta preparando la pizza Hawaiana')

    def bake(self):
        print('Esta horneando')
    
    def cut(self):
        print('Esta porcionando')
    
    def box(self):
        print('Esta alistando')

class PizzaStore(ABC):
    def orderPizza(self, type) -> Pizza:
        pizza = self.createPizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
    
    @abstractmethod
    def createPizza(self, type) -> Pizza:
        pass


class BogotaPizzaStore(PizzaStore):
    def createPizza(self, type) -> Pizza:
        pizza = None
        if type == 'napolitana':
            pizza = PizzaNapolitana()
        elif type == 'margarita':
            pizza = PizzaMargarita()
        elif type == 'vegetariana':
            pizza = PizzaVegetariana()
        else:
            raise ValueError("Pizza no valida")
        return pizza
    
class MedellinPizzaStore(PizzaStore):
    def createPizza(self, type) -> Pizza:
        pizza = None
        if type == 'napolitana':
            pizza = PizzaNapolitana()
        elif type == 'margarita':
            pizza = PizzaMargarita()
        elif type == 'vegetariana':
            pizza = PizzaVegetariana()
        elif type == 'peperoni':
            pizza = PizzaPepperoni()
        elif type == 'hawaiana':
            pizza = PizzaHawaiana()
        else:
            raise ValueError("Tipo de pizza no valido")
        
        return pizza
    
if __name__ == "__main__":
    # Crear una tienda de pizza en Bogotá
    bogota_store = BogotaPizzaStore()
    # Ordenar una pizza napolitana
    bogota_store.orderPizza('napolitana')

    print()

    # Crear una tienda de pizza en Medellín
    medellin_store = MedellinPizzaStore()
    # Ordenar una pizza hawaiana
    medellin_store.orderPizza('hawaiana')
