class Toy:
    """a toy class that have a color and age"""

    def __init__(self, color, age):
        self._color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': True
        }

    def __str__(self):
        """Set the string return of the object"""
        return f'{self._color}'

    def __len__(self):
        """Return the length of the class"""
        return 5

    def __call__(self):
        return 'Yess?'

    def __getitem__(self, i):
        """return the value of the item from the dictionary selected(my_dict in our case)"""
        return self.my_dict[i]


# action_figure = Toy('red', 0)
# print(action_figure.__str__())
# print(str(action_figure))
# print(len(action_figure))
# print(action_figure())
# print(action_figure['name'])


class SuperList(list):
    """A list that enhance a list object but retuns 1000 each time it is called the len method."""

    def __len__(self):
        return 1000


super_list = SuperList()

super_list.append(5)

print(super_list[0])
