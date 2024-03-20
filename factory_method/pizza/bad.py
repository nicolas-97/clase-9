class Pizza:
    def prepare(self):
        pass

    def bake(self):
        pass
    
    def cut(self):
        pass
    
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

class SimplePizzaFactory:
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



class PizzaStore:
    def orderPizzaOld(self) -> PizzaNapolitana:
        pizza = PizzaNapolitana()
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    def ordePizzaBetter(self,factory: SimplePizzaFactory, type) -> Pizza:
        
        pizza = factory.createPizza('napolitana')
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
    
    #Abierto cerrado abierto para extension cerrado para modificaciön

