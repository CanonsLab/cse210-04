import random

from game.directing.director import Director
from game.services.video_service import VideoService
from game.services.keyboard_service import KeyboardService
from game.shared.point import Point
from game.shared.color import Color
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.artifact import Artifact
from game.casting.player import Player

CAPTION = "GREED GAME"
CELL_SIZE = 15
FONT_SIZE = 15
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 12
COLS = 60
ROWS = 1
DEFAULT_ARTIFACTS = 10




def main():

    # create the cast
    cast = Cast()

    # create the artifacts
    for i in range(DEFAULT_ARTIFACTS): 
        x = random.randint(1, COLS - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        artifact = Artifact()
        t = artifact.Get_Type()
        if t == 0:
            artifact.set_text("O")
        else:
            artifact.set_text("*")
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_velocity(Point(0 , 15))
        cast.add_actor('artifacts', artifact)

    position = Point(450, MAX_Y-CELL_SIZE)
    position.scale(CELL_SIZE)
    color = Color(255, 255, 255)
    player = Player()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(color)
    player.set_position(position)
    cast.add_actor("player0", player)

    
        

    # Start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(video_service, keyboard_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()