# Ignorare le righe fino alla 31
from typing import Any, Callable, List, Tuple, Dict, Union
import sys
from unittest import result
import json
import math


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Esegue un test e controlla il risultato
def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "succeeded" if (result == expected) else "failed"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(f'{color}Test on {func_str} on input {args_str} {test_outcome}. Output: {result_str} Expected: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERROR: {func_str}({args_str}) => {error_str}')


# Helper functions
def load_json(filename):
    with open(filename) as f:
        return json.load(f)


# Helper functions
def save_json(filename, js):
    with open(filename, 'w') as f:
        json.dump(js, f, indent=2)

# Questo esercizio differisce dai precedenti perchè implementeremo sia funzione
# che classi.
# Implementare la classe Shape che ha un metodo area2() che calcola l'area
# al quadrato chiamando il metodo area(), e la funzione color() che ritorna una
# una tuple (g,g,g) dove g è un valore tra 0 e 1 passato al construttore come
# un parametro di nome gray.
# Implementare la classe Circle, derivata da Shape, che ha un costruttore che
# prende il raggio radius e il colore gray, e implementa il metodo area().
# Implementare la classe Polygon, derivata da Shape, che ha un metodo sides()
# che ritorna il numero di lati.
# Implementare la classe Square, derivata da Polygon, che ha un costruttore che
# prende il lato side e il colore gray e implementa area() e sides().
# Implementare la classe Triangle, derivata da Polygon, che ha un costruttore
# che prende il lato side e il colore gray e implementa area() e sides().
# L'area e sqrt(3)/4 l^2.
# In tutti i construttori i parametri sono opzionali e inizializzati a 1.
# Per ogni classe, aggiungere il metodo `repr` che stampa la chiamata al
# construttore che ha creato quell'oggetto. Ad esempio, Circle.repr(self),
# stampa 'Circle(radius=..., gray=...)' con i valori relativi; e il metodo
# __eq__ che verifica se due oggetti della stessa classe sono uguali.


class Shape:
    def __init__(self, gray):
        self.gray = gray
        
    def area2(self):
        return self.area()**2
    
    def color(self):
        return (self.gray, self.gray, self.gray)
    
    def __repr__(self):
        return f'{self.__class__.__name__}(gray={self.gray})'


class Circle(Shape):
    def __init__(self, radius, gray=1):
        super().__init__(gray)
        self.radius = radius
        
    def area(self):
        return math.pi*self.radius
    
    def __repr__(self):
        return super().__repr__()[:-1]+f', radius={self.radius})'
    

class Polygon(Shape):
    def __init__(self, num_sides):
        self.num_sides = num_sides
    
    def sides(self):
        return self.num_sides

    def __repr__(self):
        return super().__repr__()[:-1]+f', num_sides={self.num_sides})'


class Square(Polygon):
    def __init__(self, side, gray=1):
        super().__init__(4)
        self.side = side
        self.gray = gray
        
    def area(self):
        return self.side**2
    
    def __repr__(self):
        return super().__repr__()[:-1]+f', side={self.side})'

class Triangle(Polygon):
    def __init__(self, side, gray=1):
        super().__init__(3)
        self.side = side
        self.gray = gray
    
    def area(self):
        return math.sqrt(3)/4*self.side**2
    
    def __repr__(self):
        return super().__repr__()[:-1]+f', side={self.side})'


# Implementare una funzione che prende una shape e ne calcola l'area al quadrato.
def get_area2(shape: Shape):
    return shape.area2()


# Implementare una funzione che prende una lista di shapes e ne calcola 
# la somma delle aree.
def get_area(shapes: List[Shape]):
    return sum(shape.area() for shape in shapes)


# Implementare una funzione che prende una lista di shapes e ne calcola il
# numero do lati, saltando le shapes che non hanno lati, come il Circle.
def get_sides(shapes: List[Shape]):
    return sum(shape.sides() if type(shape) != Circle else 0 for shape in shapes)


# Implementare una funzione che conta il numero di Square in una lista di Shape.
def count_square(shapes: List[Shape]):
    return sum(1 if type(shape) == Square else 0 for shape in shapes)


# Implementare una funzione che conta il numero di Polygon in una lista di Shape.
def count_poly(shapes: List[Shape]):
    count = 0
    for shape in shapes:
        if type(shape) == Square or type(shape) == Triangle:
            count += 1
    return count


# Implementare una funzione che carica una file JSON e ritorna una lista di
# Shapes. Il file JSON è formato da una lista di dizionari che hanno come
# chiavi i parametri dei construttori e una chiave aggiuntiva '__type__'
# con il nome della classe. Per caricare un json usate load_json(filename).
# Suggerimento: usare **kwargs per semplicità.
def from_json(filename: str) -> List[Shape]:
    fr = load_json(filename)
    print(fr)
    for shape in fr:
        print(shape)
        shape['__type__'](**shape)
        

# Implementare una funzione che converte una lista di Shapes in una lista
# di dizionari che hanno come chiavi i parametri dei construttori e la chiave
# __type__ descritta sopra.
# Per implementarlo, si può usare isinstance() per fare ogni classe separatemente,
# oppure usare vars() per elecare le variabili di ogni classe e type().__name__
# per il nome del tipo.
def to_dict(shapes: List[Shape]) -> List[dict]:
    shape_list = []
    for shape in shapes:
        shape_dict = {}
        shape_dict['__type__'] = shape.__class__.__name__
#        fro k, v in vars(shape).items()


# Implementare una funzione che converte una lista di Shapes in una lista
# di dizionari che hanno come chiavi i parametri dei construttori e la chiave
# __type__ descritta sopra. Per salvare un Json usate save_json(filename, js).
# Basta salvare i dizionari scritti da to_dict().
def to_json(filename: str, shapes: List[Shape]) -> None:
    pass


# Test funzioni
check_test(get_area2, 1, Square(side=1))
check_test(get_area, 2, [Square(side=1), Square(side=1)])
check_test(get_area, 4.574605355482013, [Square(
    side=1), Circle(radius=1), Triangle(side=1)])
check_test(get_sides, 7, [Square(side=1), Circle(radius=1), Triangle(side=1)])
check_test(count_square, 1, [Square(side=1),
           Circle(radius=1), Triangle(side=1)])
check_test(count_poly, 2, [Square(side=1), Circle(radius=1), Triangle(side=1)])
check_test(from_json, [Square(side=1, gray=0), Circle(
    radius=1), Triangle(side=1)], 'shapes.json')
check_test(to_dict, [{'__type__': 'Square', 'side': 1, 'gray': 0}, {'__type__': 'Circle', 'radius': 1, 'gray': 1}, {
           '__type__': 'Triangle', 'side': 1, 'gray': 1}], [Square(side=1, gray=0), Circle(radius=1), Triangle(side=1)])
check_test(to_json, None, 'shapes_out.json', [
           Square(side=1, gray=0), Circle(radius=1), Triangle(side=1)])
