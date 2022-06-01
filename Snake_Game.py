"""
`Snake_Game.py` implementiert die Logik des Spiels Snake.
Diese besteht hauptsächlich aus zwei Funktionen, die in jedem
Durchlauf der Game Loop aufgerufen werden:

* `update()` aktualisiert den internen Game-State.

* `show()` zeigt den aktuellen Game State auf einem Screen an.
"""
import pygame
import numpy as np


SCREEN_SIZE_X = 60
SCREEN_SIZE_Y = 60


class Game:
    """
    This class implements the snake game,
    including the internal state, logic and user interface.
    """

    def __init__(self):
        """
        Constructor:
        game_continues: Bool
            Indictates, if the game is running.
        snake_list:
            list of coordinates of the snake.
        food_pos:
            food position.
        movement_dir:
            Direction, in which the snake is moving.
            Possible values are: {'l', 'r', 'u', 'd'}.
        screen:
            pygame-Screen, on which the game is shown.
        """

        # initialize all the classes properties here...

        self.screen = pygame.display.set_mode((10*SCREEN_SIZE_X, 10*SCREEN_SIZE_Y))

    def update(self):
        """
        Update the game-state.
        """
        # read in keyboard input.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # what happens, if you quit the game?

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # what happens, if you press the left arrow?

                elif event.key == pygame.K_RIGHT:
                    # what happens, if you press the right arrow?

                elif event.key == pygame.K_UP:
                    # what happens, if you press the up arrow key?
                elif event.key == pygame.K_DOWN:
                    # what happens, if you press the down arrow?

                elif event.key == pygame.K_ESCAPE:
                    # what happens, if you press ESC

        # The snake has to move in every step,
        # depending on the direction of the snake...


        # Optional: Make the snake re-enter on the other side, if it leaves the screen.


        # test, the snake bites into itself.


        # test, if food is eaten and optionally respawn food.

        # Optional: print score, if game ends.

    def show(self):
        """
        Zeige den Game-State auf dem Bildschirm an.
        """
        # fill the screen with a black background
        self.screen.fill((0, 0, 0))

        # draw snake (using draw_rectangle, usecolour = (255, 255, 255))

        # draw food (using draw_rectangle, usecolour = (255, 0, 0))

        # display the screen
        pygame.display.update()

    def draw_rectangle(self,
                       pos,
                       colour):
        """
        Zeichne ein Quadrat in der gegebenen Farbe & Position.

        pos:
            Position, im Format [x_position, y_position]
        colour:
            RGB-Wert einer Farbe, z.B. (255, 255, 255) für weiß.
        """
        pygame.draw.rect(self.screen,
                         colour,
                         pygame.Rect(10 * pos[0],
                                     10 * pos[1],
                                     9,
                                     9))
