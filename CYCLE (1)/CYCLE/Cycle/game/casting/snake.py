import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, id):
        super().__init__()
        self._segments = []
        # FCO - Have an  id to identify one snake from another
        self._id = id 
        self._prepare_body()

    def get_segments(self):
        """Gets the segments of the snake's body segments

        Returns:
            _segments: A list of segments
        """
        return self._segments

    def move_next(self):
        """Moves all the segments one space to the same direction
        """
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """Gets the snake's head

        Returns:
            _segments[0]: The first element of the segments list
        """
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        """Makes the sake's tail grow

        Args:
            number_of_segments (int): The number of segments of the snake's body
        """
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            
            #segment.set_color(constants.GREEN)
            # Using self._id to identify each snake and give it the right color
            if self._id % 2 == 0: 
                segment.set_color(constants.GREEN)
            else:
                segment.set_color(constants.RED)

            self._segments.append(segment)

    def turn_head(self, velocity):
        """Makes the snake's head turn

        Args:
            velocity (Point): The given velocity
        """
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        """Sets the positions of the bodies of snakes
        """
        # Using self._id to get the start point of the snakes
        if self._id == 1:
            x = int(constants.MAX_X - 600)
        else:
            x = int(constants.MAX_X - 300)
        
        y = int(constants.MAX_Y / 2) 

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"

        
            # color = constants.YELLOW if i == 0 else constants.GREEN
            
            # self._id to identify the colors
            if i == 0:
                color = constants.YELLOW
            
            elif self._id % 2 == 0:
                color = constants.GREEN
            else:
                color = constants.RED
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)