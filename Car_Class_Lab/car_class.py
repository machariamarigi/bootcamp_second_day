class Car(object):
    """
        A Car class that can be used to instantiate various vehicles
            Arguments:
                Vehicle name
                Vehicle Model
                Vehicle Type
            Default attributes set on different conditions
                Speed
                Number of wheels
                Number of doors
                Speed
    """

    def __init__(self, name='General', model='GM', type=None):
        self.name = name
        self.model = model
        self.type = type
        self.speed = 0

        if self.type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

        if self.name in ['Porshe', 'Koenigsegg']:
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

    # Check car type
    def is_saloon(self):
        return self.type != 'trailer'

    # method to drive a car
    def drive(self, speed):
        if self.type == 'trailer':
            self.speed = 77
        else:
            self.speed = pow(10, speed)

        return self
