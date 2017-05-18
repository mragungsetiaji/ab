from pokemon import *
from trainer import trainer

class battle(object):
    def __init__(self, trainer1_name, trainer2_name):
        ash = trainer(trainer1_name)
        misty = trainer(trainer2_name)

        pika = pikachu()
        char = charmander()
        bulb = bulbasaur()
        ash.add_pokemon()
        misty.add_pokemon(pika)
        misty.add_pokemon(bulb)

        ash.make_move(0, misty, 0, "tackle")
        pika.status()
        ash.show_all_pokemon()
        misty.show_all_pokemon()

        misty.make_move(0, ash, 0, "thunder_shock")
        char.status()

        ash.show_all_pokemon()
        misty.show_all_pokemon()