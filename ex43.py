from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
            "You died. You kinda suck at this.",
            "Your Mom would be proud...if she was smarter",
            "Such a luser.",
            "I have a small puppy that's better at this.",
            "You're worse than your dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
             The Gothons of Planet Percal #25 have invaded your ship and destroyed
             your entire crew. You are the last surviving member and your last mission
             is to get the neutron destoyer bomb from the weapons armory
             put it in the bridge blah bla hblah. Somebody is blocking you what do you do?
             """))
        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                You killed him. but you died too
            """))
            return 'death'
        elif action == 'dodge!':
            print("You die")

            return 'death'
        elif action == "joke":
            print("you win")
            return "laser_weapon_armory"

        else:
            print("Fuck Off")
            return 'central_corridor'
class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'death': Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
