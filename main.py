from Snake_Game import *
from time import sleep

game = Game()

# init py game
pygame.init()


while game.game_continues:

    game.update()
    game.show()

    sleep(0.05)

