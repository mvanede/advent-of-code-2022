class Position:
    def __init__(self, x=0, y=0, allow_negative = True):
        self.x = x
        self.y = y
        self.allow_negative = allow_negative

    @property
    def tuple(self):
        return (self.x, self.y)
    
    def check_validity(self):
        if not self.allow_negative and (self.x < 0 or self.y < 0):
            raise ValueError
        
    def move(self, xdiff, ydiff):
        self.x += xdiff
        self.y += ydiff
        self.check_validity()

    def move_dir(self, direction, steps):
        if direction == 'U':
            self.y -= steps
        elif direction == 'D':
            self.y += steps
        if direction == 'L':
            self.x -= steps
        if direction == 'R':
            self.x += steps

        self.check_validity()

    def __str__(self):
        return '{}, {}'.format(self.x, self.y)