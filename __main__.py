import random

from game.directing.director import Director
from game.services.video_service import VideoService
from game.shared.point import Point
from game.shared.color import Color
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.artifact import Artifact

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
        gem_and_rock = (chr(42), chr(79))
        text = random.choice(gem_and_rock)
        

        x = random.randint(1, COLS - 1)
        y = ROWS
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        artifact = Actor()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        cast.add_actor('artifacts', artifact)
        

    # Start the game
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()