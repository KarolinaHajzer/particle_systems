from unittest import TestCase
from particle_systems_functions import *
from Disc import *
import types


class ParticleSystemsFunctionsTest(TestCase):
    def test_calc_distance(self):
        p1 = [3, 5]
        p2 = [2, 4]
        function_result = calc_distance(p1, p2)
        d = math.sqrt((-1*-1) + (-1*-1))
        assert function_result == d

    def test_unit_vector(self):
        disc1 = Disc()
        disc2 = Disc()
        disc1.disc_pos = [3, 5]
        disc2.disc_pos = [2, 4]
        d = math.sqrt((-1 * -1) + (-1 * -1))
        v = [-1, -1]
        nx = v[0] / d
        ny = v[1] / d
        n = [nx, ny]
        function_result = unit_vector(disc1, disc2)
        assert n == function_result

    def test_gravity_force(self):
        disc1 = Disc()
        disc2 = Disc()
        disc1.disc_pos = [3, 5]
        disc2.disc_pos = [2, 4]
        disc1.m = 2
        disc2.m = 3
        G = 1
        n = unit_vector(disc1, disc2)
        dist = calc_distance(disc1.disc_pos, disc2.disc_pos)
        gravity_force_x = G * disc1.m * disc2.m / dist * dist * n[0]
        gravity_force_y = G * disc1.m * disc2.m / dist * dist * n[1]
        function_result = gravity_force(disc1, disc2)
        assert [gravity_force_x, gravity_force_y] == function_result

    def test_adding_disc_into_list(self):
        list_of_discs = []
        d = list_of_discs.append(Disc())
        function_result = adding_disc_into_list()
        assert d == function_result

    def test_removing_disc_from_list(self):
        are_equal = False
        disc1 = Disc()
        length1 = len(discs)
        discs.append(disc1)
        index = discs.index(disc1)
        discs.pop(index)
        length2 = len(discs)
        discs.append(disc1)
        removing_disc_from_list(disc1)
        length3 = len(discs)
        if length1 == length2 and length2 == length3:
            are_equal = True
        self.assertTrue(are_equal)

    def test_changing_gravity_force(self):
        list_of_gravity_force_for_changing = [2, 3]
        function_result = changing_gravity_force(list_of_gravity_force_for_changing)
        assert [-2, -3] == function_result

    def test_making_grav_points(self):
        grav_points_list = []
        lista = [2, [[150, 200], [500, 450]]]
        grav_point_pos = lista[1]
        for one_grav_point in grav_point_pos:
            grav_point = Disc()
            grav_point.m = 40
            grav_point.r = 10
            grav_point.color = (0, 0, 0)
            grav_point.disc_pos = [one_grav_point[0], one_grav_point[1]]
            grav_points_list.append(grav_point)
        function_result = making_grav_points(lista)
        assert len(grav_points_list) == len(function_result)

    def test_changing_grav_force(self):
        grav_force_list = [[2, 3]]
        changed_grav_force_list = [[-2, -3]]
        assert changed_grav_force_list == changing_grav_force(grav_force_list)
