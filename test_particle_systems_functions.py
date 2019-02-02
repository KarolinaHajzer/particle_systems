from unittest import TestCase

# Grupujemy importy, patrz narzędzie isort
from Disc import Disc

# Nie importujemy wszystkiego z modułu
from particle_systems_functions import (
    adding_disc_into_list,
    calc_distance,
    changing_grav_force,
    changing_gravity_force,
    discs,
    gravity_force,
    making_grav_points,
    removing_disc_from_list,
    unit_vector,
)


class ParticleSystemsFunctionsTest(TestCase):
    def test_calc_distance(self):
        # Nie powtarzaj kodu funkcji w teście
        # Nie twórz zmiennych, które użyjesz tylko raz
        function_result = calc_distance([3, 5], [2, 4])

        # Ta zmienna ma sens bo jeśli w jednej linii jest zbyt wiele
        # operacji, to potem nie wiadomo co nawaliło.
        # assertEqual jest fajny bo porówna cokolwiek mu damy
        self.assertEqual(function_result, 1.4142135623730951)

    # Rozdzielanie faz testu. Komentarze są zbędne i służą tylko celom
    # edukacyjnym :)
    def test_unit_vector(self):
        # Arrange
        disc1, disc2 = self._prepare_discs()

        # Act
        function_result = unit_vector(disc1, disc2)

        # Assert
        self.assertEqual(
            function_result,
            [-0.7071067811865475, -0.7071067811865475],
        )

    def test_gravity_force(self):
        disc1, disc2 = self._prepare_discs()
        disc1.m = 2
        disc2.m = 3

        function_result = gravity_force(disc1, disc2)

        self.assertEqual(
            function_result,
            [-4.242640687119285, -4.242640687119285],
        )

    # Funkcje pomocnicze pomagają uwspólniać powtarzające się części kodu
    # Warto je robić gdy kod powtarza się w trzech miejscach, więc
    # w tym przypadku jest to lekki overkill
    @staticmethod
    def _prepare_discs():
        disc1 = Disc()
        disc2 = Disc()
        disc1.disc_pos = [3, 5]
        disc2.disc_pos = [2, 4]
        return disc1, disc2

    def test_adding_disc_into_list(self):
        adding_disc_into_list()

        self.assertEqual(len(discs), 1)
        disc_vars = self._get_disc_vars(discs[0])
        self.assertEqual(disc_vars, {
            'disc_pos': [100, 50],
            'Fw': [0, 0],
            'life_duration': 0,
        })

    def test_removing_disc_from_list(self):
        disc1 = Disc()
        length1 = len(discs)
        discs.append(disc1)
        index = discs.index(disc1)
        discs.pop(index)
        length2 = len(discs)
        discs.append(disc1)
        removing_disc_from_list(disc1)
        length3 = len(discs)

        self.assertEqual(length1, length2)
        self.assertEqual(length2, length3)

    def test_changing_gravity_force(self):
        function_result = changing_gravity_force([2, 3])

        self.assertEqual(function_result, [-2, -3])

    def test_making_grav_points(self):
        function_result = making_grav_points([2, [[150, 200], [500, 450]]])

        self.assertEqual(len(function_result), 2)
        # Tak nie rób. Zamiast tego można by było zdefiniować operator
        # porównania na obiektach Disc
        disc_vars = self._get_disc_vars(function_result[0])
        self.assertEqual(disc_vars, {
            'disc_pos': [150, 200],
            'Fw': [0, 0],
            'life_duration': 0,
        })
        disc_vars = self._get_disc_vars(function_result[1])
        self.assertEqual(disc_vars, {
            'disc_pos': [500, 450],
            'Fw': [0, 0],
            'life_duration': 0,
        })

    def test_changing_grav_force(self):
        changed_grav_force_list = changing_grav_force([[2, 3]])

        self.assertEqual(changed_grav_force_list, [[-2, -3]])

    @staticmethod
    def _get_disc_vars(disc):
        disc_vars = vars(disc)
        del disc_vars['v']
        del disc_vars['r']
        del disc_vars['color']
        del disc_vars['m']
        return disc_vars
