"""
    A file containing the functions needed to run the program particle_system_main.
    Included functions:
    - drawing_disc
    - calc_distance
    - unit_vector
    - gravity_force
    - adding_disc_into_list
    - removing_disc_from_list
    - changing_gravity_force
    - asking_about_grav_points
    - making_grav_points
    - changing_grav_force
    - making_force_from_grav_points_list
"""

from Disc import *
import pygame
import math

window = pygame.display.set_mode((width, height))
discs = []
G = 1


def drawing_disc(disc):
    """
    Function that draws disc, the argument of the function is the disk that we want to draw using
    the built-in function pygame.
    """
    pygame.draw.circle(window, disc.color, [int(disc.disc_pos[0]), int(disc.disc_pos[1])], disc.r)


def calc_distance(p1, p2):
    """
    Calculates and returns the distance between two points.
    :param p1: point 1 from two points between which we want to calculate the distance
    :param p2: point 2 from two points between which we want to calculate the distance
    :return: distance between two given points
    """
    distance = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
    return distance


def unit_vector(disc1, disc2):
    """
    Calculates and returns unit vector between two discs.
    :param disc1: disc 1 from two discs between which we want to calculate unit vector
    :param disc2: disc 2 from two discs between which we want to calculate unit vector
    :return: unit vector in the form of a vector
    """
    d = calc_distance(disc1.disc_pos, disc2.disc_pos)
    vector = [disc2.disc_pos[0] - disc1.disc_pos[0], disc2.disc_pos[1] - disc1.disc_pos[1]]
    nx = vector[0] / d
    ny = vector[1] / d
    n = [nx, ny]
    return n


def gravity_force(disc1, disc2):
    """
    Calculates and returns gravity force between two discs.
    :param disc1: disc 1 from two discs between which we want to calculate gravity force
    :param disc2: disc 2 from two discs between which we want to calculate gravity force
    :return: gravity force in the form of a vector
    """
    n = unit_vector(disc1, disc2)
    dist = calc_distance(disc1.disc_pos, disc2.disc_pos)
    gravity_force_x = G * disc1.m * disc2.m / dist * dist * n[0]
    gravity_force_y = G * disc1.m * disc2.m / dist * dist * n[1]
    return [gravity_force_x, gravity_force_y]


def adding_disc_into_list():
    """
    Adds a disc to the list of discs.
    """
    discs.append(Disc())


def removing_disc_from_list(disc):
    """
    Removes a disc from the list of discs.
    :param disc: disc that will be removed from the list
    """
    disc_index = discs.index(disc)
    discs.pop(disc_index)


def changing_gravity_force(gravity_force_for_changing):
    """
    Changes the force of gravity on the repulsive one.
    :param gravity_force_for_changing: gravity force that will be changed
    :return: changed gravity force in the form of vector
    """
    [x, y] = gravity_force_for_changing
    gravity_force_for_changing = [-x, -y]
    return gravity_force_for_changing


def asking_about_grav_points():
    """
    The function asks the user how many gravitational points he wants to create and in what location.
    :return: asked values in the form of a list that includes number of gravity points and their positions
    """
    grav_point_pos = []
    asked_values = []
    number_of_grav_points = int(input("How many gravity points do you want?: "))
    if number_of_grav_points <= 10:
        for grav_point in range(number_of_grav_points):
            print("Gravity point:")
            grav_point_pos_x = int(input("Position of gravity point, on x axis: "))
            grav_point_pos_y = int(input("Position of gravity point, on y axis: "))
            grav_point_pos.append([grav_point_pos_x, grav_point_pos_y])
            asked_values = [number_of_grav_points, grav_point_pos]
    else:
        print("Are you sure that you want so many gravity points? Just checking.")
        number_of_grav_points = int(input("How many gravity points do you want?: "))
        if number_of_grav_points <= 10:
            for grav_point in range(number_of_grav_points):
                print("Gravity point:")
                grav_point_pos_x = int(input("Position of gravity point, on x axis: "))
                grav_point_pos_y = int(input("Position of gravity point, on y axis: "))
                grav_point_pos.append([grav_point_pos_x, grav_point_pos_y])
                asked_values = [number_of_grav_points, grav_point_pos]
    return asked_values


def making_grav_points(lista):
    """
    Create gravity points. Gravity points are same as discs, but in one, concrete position.
    :param lista: list of gravity points that will be created
    :return: list of created gravity points
    """
    grav_points_list = []
    grav_point_pos = lista[1]
    for one_grav_point in grav_point_pos:
        grav_point = Disc()
        grav_point.m = 40
        grav_point.r = 10
        grav_point.color = (0, 0, 0)
        grav_point.disc_pos = [one_grav_point[0], one_grav_point[1]]
        grav_points_list.append(grav_point)
    return grav_points_list


def changing_grav_force(grav_force_list):
    """
    Creates list of changed gravity force from list of gravity force using function changing_gravity_force.
    :param grav_force_list: list of gravity force
    :return: list of changed gravity forces
    """
    for this_force in grav_force_list:
        changed_force_list = []
        changed_force = changing_gravity_force(this_force)
        changed_force_list.append(changed_force)
        return changed_force_list


def making_force_from_grav_points_list(grav_points_list, disc):
    """
    Makes and returns gravity force between each gravity point and disc.
    :param grav_points_list: gravity point that will be needed to calculate gravity force between him and disc
    :param disc: disc that will be needed to calculate gravity force between him and gravity point
    :return: created list of forces between gravity points and discs
    """
    this_force_list = []
    for grav_point in grav_points_list:
        this_force = gravity_force(disc, grav_point)
        this_force_list.append(this_force)
    print(this_force_list)
    return this_force_list
