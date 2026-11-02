# We may override built in methods
class Tester(list):
    def __str__(self): # every object has a default __str__ method used by 'print'
        return f'Tester contains {super().__str__()}'

if __name__ == '__main__':
    c1 = Tester((1,2,3,4,5))
    c1.append(99)
    c1.remove(2)
    print(c1) # use default __str__ method