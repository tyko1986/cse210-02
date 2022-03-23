import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._id_game_over = 0
        # have a Counter to make the snakes grow
        self._counter = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            #self._handle_food_collision(cast)
            self._handle_segment_collision(cast)

            # FCO - We add a method to handle the sollision between the snakes and another to make the snake grow
            self._handle_opponent_collision(cast) 
            self._grow(cast)

            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score and moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("snakes")
        head = snake.get_head()

        if head.get_position().equals(food.get_position()):
            points = food.get_points()
            snake.grow_tail(points)
            score.add_points(points)
            food.reset()

        # FCO - in case of having food in the game the second snake would eat the food
        snake2 = cast.get_second_actor("snakes")
        head2 = snake2.get_head()

        if head2.get_position().equals(food.get_position()):
            points = food.get_points()
            snake2.grow_tail(points)
            score.add_points(points)
            food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._id_game_over = 1

        snake2 = cast.get_second_actor("snakes")
        head2 = snake2.get_segments()[0]
        segments2 = snake2.get_segments()[1:]
        
        for segment in segments2:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._id_game_over = 2

    # FCO - Define a method to handle if any of the snakes hits the opponent snake
    def _handle_opponent_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its opponents segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake1 = cast.get_first_actor("snakes")
        snake2 = cast.get_second_actor("snakes")

        head1 = snake1.get_segments()[0]
        segments2 = snake2.get_segments()
        
        for segment in segments2:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._id_game_over = 1

        head2 = snake2.get_segments()[0]
        segments1 = snake1.get_segments()
        for segment in segments1:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._id_game_over = 2

    # Mothod grow, using the counter to make the snakes grow every certain time
    def _grow(self, cast):
        """Makes the snakes grow one character per every few seconds.

        Args:
            cast (Cast): The cast of actors in the game
        """
        if self._counter % 7 == 0: # because the counter is raising it is going to grow the tail of each snake every time the conter can be exatly divided by 7
            snake1 = cast.get_first_actor("snakes")
            snake2 = cast.get_second_actor("snakes")
            snake1.grow_tail(1)
            snake2.grow_tail(1)
        self._counter += 1 # add 1 every time it updates
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            if self._id_game_over == 1:
                snake = cast.get_first_actor("snakes")
            else:
                snake = cast.get_second_actor("snakes")
            
            segments = snake.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()

            #message.set_text("Game Over!") and the name of the winner snake
            
            if self._id_game_over == 1:
                message.set_text("Game Over! Green Wins")
            else:
                message.set_text("Game Over! Red Wins")

            message.set_position(position)
            cast.add_actor("messages", message)

            # It keeps the color of the winning snake
            for segment in segments:
                segment.set_color(constants.WHITE)
            #food.set_color(constants.WHITE)