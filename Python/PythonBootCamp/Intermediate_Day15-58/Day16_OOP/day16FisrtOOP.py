


"""
This code chunk demonstrates how to work with Classes in including
how to create objectes from a class. Also it shows how to work with static/dynamic
class attritubtes & methods
"""

# class TestClass002:
#     # Class Object Attribute - Static
#     member_ship = True
    
#     # Defines dynamic attributes
#     def __init__(self, name, player_class, char_level):
#         if (self.member_ship):
#         # if (TestClass002.member_ship):
#             self.name = name # attributes
#             self.player_class = player_class
#             self.char_level = char_level

#     def run(self):
#         print('Run for your LIFE!!!')
#         return ''
    
#     def shout(self):
#         print(f'my name is {self.name}')
#         return ''
    
#     @classmethod
#     def adding_things(cls, num1, num2):
#         # return num1 + num2
#         return cls('Skull Crusher', 'Barbarian', num1 + num2) 

#     # This doesn't have access to the class and it's attributes & Methods
#     @staticmethod
#     def adding_things2(num1, num2):
#         return num1 + num2     

# print("Before any object has been instantiated")
# print(TestClass002.adding_things(5,2))
# player3 = TestClass002.adding_things(5,2)
# print(player3.name)
# print(player3.player_class)
# print(player3.char_level)

# player1 = TestClass002(name='Melzanis The Great', player_class='Warlock', char_level=45)
# player2 = TestClass002(name='Avemi Taybr', player_class='Warrior', char_level=60)

# print(player1)
# print(player1.name)
# print(player1.player_class)
# print(player1.char_level)
# print(player1.run())
# print(player1.shout())
# print(player1.adding_things(5,34))

# print(player2)
# print(player2.name)
# print(player2.player_class)
# print(player2.char_level)
# print(player2.run())
# print(player2.shout())
# print(player2.adding_things(74,14))


"""
This demonstrates how Inheritance works
"""
# class TestClass003():
    
#     def __init__(self, email):
#         self.email = email
    
#     def sing_in(self):
#         print('logged in')
    
#     # def attack(self):
#     #     print('Swing your fists!')

# class Wizard(TestClass003):
#     def __init__(self, name, power, email):
#         # TestClass003.__init__(self, email)
#         super().__init__(email) # Instead of using TestClass003.__init__(self, email) use this format
#         self.name = name
#         self.power = power
#         # self.email = email
    
#     def attack(self):
#         # TestClass003.attack(self)
#         print(f'attaching with power of {self.power}')

# class Archer(TestClass003):
#     def __init__(self, name, num_arrows, email):
#         super().__init__(email)
#         self.name = name
#         self.num_arrows = num_arrows
    
#     def attack(self):
#         print(f'attaching with arrows: arrows left - {self.num_arrows}')

# wizard = Wizard('Melzanis', 50, 'melzanisTheGreat@wizardmail.com')
# # archer = Archer('Viper', 100)
# archer = Archer('Viper', 100, 'viperBullsEye@archersmail.com')
# # print(wizard.sing_in())

# wizard.attack()
# print(wizard.email)
# archer.attack()
# print(archer.email)

"""
This is suppose to demonstrate Polymorphism
"""
# def player_attack(char):
#     char.attack()

# player_attack(wizard)
# player_attack(archer)

# for char in  [wizard, archer]:
#     char.attack()


"""
The code below will demonstrate how dunder methods work
"""

# class Toy:
    
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#         self.toy_dict = {
#             'name': 'Yoyo',
#             'color': 'blue',
#             'has_pets': False
#         }

#     """
#     Don't change these dunder methods unless you really have to
#     """        
#     def __str__(self):
#         return f'{self.color}'
    
#     def __len__(self):
#         return 5
    
#     # def __del__(self):
#     #     print('Deleted!!')
    
#     def __call__(self):
#         print('YESS!!!')
    
#     def __getitem__(self, i):
#         return self.toy_dict[i]

# action_figure = Toy('red', 0)
# print(action_figure.__str__())
# print(str(action_figure))
# print(len(action_figure))
# # del action_figure
# # print(action_figure())
# action_figure()
# print(action_figure['name'])



# class SuperList(list):
    
#     def __len__(self):
#         return 1000

# super_list1 = SuperList()

# print(len(super_list1))
# super_list1.append(5)
# print(super_list1[0])
# print(issubclass(SuperList, list))


"""
Demonstrating how to detail with muiltiple inheritance
"""
# class TestClass003():
    
#     def sing_in(self):
#         print('logged in')
    
#     # def attack(self):
#     #     print('Swing your fists!')

# class Wizard(TestClass003):
#     def __init__(self, name, power):
#         # TestClass003.__init__(self, email)
#         self.name = name
#         self.power = power
#         # self.email = email
    
#     def power_attack(self):
#         # TestClass003.attack(self)
#         print(f'attaching with power of {self.power}')
    
#     def check_power_lvl(self):
#         print(f'Currnt power level is at {self.power}')

# class Archer(TestClass003):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
    
#     def arrow_attack(self):
#         print(f'attaching with arrows: arrows left - {self.num_arrows}')
    
#     def check_arrows(self):
#         print(f'{self.num_arrows} remaining')
    
#     def run(self):
#         print('Quickly dashing away... zoom')

# class HybridBorg(Wizard, Archer):    
#     def __init__(self, name, power, num_arrows):
#         Wizard.__init__(self, name, power)
#         Archer.__init__(self, name, num_arrows)

# wizard = Wizard('Melzanis', 50)
# # wizard = Wizard('Melzanis', 50, 'melzanisTheGreat@wizardmail.com')
# archer = Archer('Viper', 100)
# # archer = Archer('Viper', 100, 'viperBullsEye@archersmail.com')
# # print(wizard.sing_in())

# wizard.power_attack()
# # print(wizard.email)
# archer.arrow_attack()
# # print(archer.email)

# hb1 = HybridBorg('Cyborg001', 50, 100)

# print(hb1.name)
# hb1.arrow_attack()
# hb1.run()
# hb1.check_arrows()
# hb1.power_attack()

"""
# MRO - Method Resolution Order
"""

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num) # Prints one because of the order starting from class D
print(D.mro()) # Checks the MRO order of a class
print(D.__str__)
print(C.num)
print(B.num)






































































# import turtle

# franklin = turtle.Turtle()

# from turtle import Turtle, Screen

# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)

# myScreen = Screen()

# print(myScreen.canvheight)
# myScreen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()

# table.add_column("Pokemon Name", ["Pikachu", "Bulbasaur", "Charmander"])
# table.add_column("Class", ["Electric", "Grass", "Fire"])

# table.align = "r"

# print(table)

# # Basic structure of the blueprint of building a class
# class TestClass001:
#     pass

# print(TestClass001)

# # Instantiates an instances of the TestClass001 class
# obj001 = TestClass001()

# print(obj001)












