"""
The main file that performs all the functions described in the file particle_systems_functions and Disc class.
"""
from particle_systems_functions import *

window = pygame.display.set_mode((width, height))
not_used_discs = []


def main():
    pygame.init()
    pygame.display.set_caption('Particle systems')
    clock = pygame.time.Clock()

    mouse_down = False
    running = True

    asked_values = asking_about_grav_points()
    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
        adding_disc_into_list()

        for disc in discs:
            disc.moving_position()
            grav_points_list = making_grav_points(asked_values)
            this_force_list = making_force_from_grav_points_list(grav_points_list, disc)
            if mouse_down:
                changed_force_list = changing_grav_force(this_force_list)
                for changed_force in changed_force_list:
                    disc.add_force(changed_force)
            else:
                for this_force in this_force_list:
                    disc.add_force(this_force)
            disc.moving_velocity()
            # disc.checking_out_of_position()
            disc.Fw = [0, 0]
            disc.life_duration += 1

            if disc.life_duration == 1000:
                removing_disc_from_list(disc)

        window.fill((0, 0, 0))
        grav_points_list = making_grav_points(asked_values)
        for grav_point in grav_points_list:
            drawing_disc(grav_point)

        for disc in discs:
            drawing_disc(disc)

        pygame.display.update()


if __name__ == "__main__":
    main()
