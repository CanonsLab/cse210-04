import random
from game.shared.point import Point
from game.shared.color import Color
from game.casting.artifact import Artifact

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """
    
    def __init__(self, video_service, keyboard_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._keyboard_service = keyboard_service
        self._score = 0

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()
        

    def _get_inputs(self, cast):
        player = cast.get_first_actor('player0')
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)

    def _do_updates(self, cast):
        actors = cast.get_all_actors()
        x = self._video_service.get_width()
        y = self._video_service.get_height()
        for i in actors:
            i.move_next(x, y, cast)
        if len(cast.get_actors('artifacts')) < 50:
            x = random.randint(1, 60 - 1)
            y = 0
            position = Point(x, y)
            position = position.scale(15)

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
            artifact.set_font_size(15)
            artifact.set_color(color)
            artifact.set_position(position)
            artifact.set_velocity(Point(0 , 15))
            cast.add_actor('artifacts', artifact)
        player_character = cast.get_first_actor('player0')
        compare = player_character.get_position()
        for i in actors:
            if compare.equals(i.get_position()) and i != cast.get_first_actor('player0'):
                self._score += i.Collision()
                print(f"Your score is {self._score}.")
                cast.remove_actor("artifacts", i)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
  