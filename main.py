from random import choice

def name_drawer(names=list) -> None:
    while len(names):
        input('Press enter to draw a name')

        name_drawn = choice(names)
        names.remove(name_drawn)

        print(f'Drawn name: {name_drawn}')


if __name__ == '__main__':
    name_drawer(
        names=[
            'Uchiha Sasuke',
            'Uzumaki Naruto',
            'Haruno Sakura',
            'Hatake Kakashi',
            'Jiraya',
            'Tsunade',
            'Namikaze Minato',
        ]
    )
