
class Person(object):
    '''Creates a person class to inherit from in Player and Enemy
    '''
    def __init__(self, x, y):
        '''Inititializes position
        '''
        self.x = x
        self.y = y

    def get_position(self):
        '''Returns own position
        '''
        return [self.x, self.y]

    def set_position(self, x, y):
        '''Sets new Position
        '''
        self.x = x
        self.y =y
