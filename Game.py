from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(
    model = "plane",
    texture = "grass",
    collider = "mesh",
    scale = (1000, 1, 1000)
)

player = FirstPersonController()

app.run()
