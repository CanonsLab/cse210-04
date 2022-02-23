
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """
    
    def __init__(self, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()
        

    def _get_inputs(self):
        pass

    def _do_updates(self, cast):
        actors = cast.get_all_actors()
        x = self._video_service.get_width()
        y = self._video_service.get_height()
        for i in actors:
            i.move_next(x, y)
        player_character = cast.get_first_actor('player0')
        compare = player_character.get_position()
        for i in actors:
            if compare.equals(i.get_position()) and i != cast.get_first_actor('player0'):
                i.Collision()
                #this is for points
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
  