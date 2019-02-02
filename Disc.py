import random

dt = 0.1
width = 1200
height = 700


class Disc:
    """
    Class that defines all discs and their functions used in particle_system_main
    """
    def __init__(self):
        """
        Initialization of all variables of the class Disc.
        """
        self.r = random.randint(4, 7)
        self.v = [random.randint(-1, 1), random.randint(-1, 1)]
        self.disc_pos = [100, 50]
        self.color = (random.randint(5, 255), (random.randint(5, 255)), (random.randint(5, 255)))
        self.m = self.r * 2
        self.Fw = [0, 0]
        self.life_duration = 0

    def moving_velocity(self):
        """
        Method that calculates velocity of the disc.
        """
        self.v[0] = self.v[0] + (self.Fw[0] / self.m * dt)
        self.v[1] = self.v[1] + (self.Fw[1] / self.m * dt)

    def add_force(self, force):
        """
        Adds force to the resultant force.
        :param force: force that will be added
        """
        self.Fw[0] += force[0]
        self.Fw[1] += force[1]

    def moving_position(self):
        """
        Calculates position of the disc.
        """
        self.disc_pos[0] += self.v[0] * dt
        self.disc_pos[1] += self.v[1] * dt

    def checking_out_of_position(self):
        """
        A method that causes the disk to be reflected if it approaches the window wall.
        """
        if self.disc_pos[0] < self.r or self.disc_pos[0] + self.r > width:
            self.v[0] = -self.v[0]

        if self.disc_pos[1] < self.r or self.disc_pos[1] + self.r > height:
            self.v[1] = -self.v[1]
