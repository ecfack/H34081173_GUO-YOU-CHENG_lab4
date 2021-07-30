import pygame
import os
import math

TOWER_IMAGE = pygame.image.load(os.path.join("images", "rapid_test.png"))


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

        self.transparent_surface = pygame.Surface((self.radius*2,self.radius*2), pygame.SRCALPHA)

    def collide(self, enemy):
        """
        Q2.2)check whether the enemy is in the circle (attack range), if the enemy is in range return True
        :param enemy: Enemy() object
        :return: Bool
        """

        """
        Hint:
        x1, y1 = enemy.get_pos()
        ...
        """

        #compute the distance between the enemy and the tower
        enemy_x,enemy_y=enemy.get_pos()
        distance=math.sqrt((enemy_x-self.center[0])**2+(enemy_y-self.center[1])**2)

        if distance<=self.radius:
            return True
        else:
            return False
        pass

    def draw_transparent(self, win):
        """
        Q1) draw the tower effect range, which is a transparent circle.
        :param win: window surface
        :return: None
        """

        # define transparency: 0~255, 0 is fully transparent
        transparency = 128
        # draw the circle on the transparent surface
        x=self.transparent_surface.get_width()/2
        y=self.transparent_surface.get_height()/2
        pygame.draw.circle(self.transparent_surface, (128, 128, 128, transparency), (x,y), self.radius)

        # blit the transparent surface into window surface
        x=self.center[0]-x
        y=self.center[1]-y
        win.blit(self.transparent_surface, (x,y))
        pass


class Tower:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(TOWER_IMAGE, (70, 70))  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower
        self.range = 150  # tower attack range
        self.damage = 2   # tower damage
        self.range_circle = Circle(self.rect.center, self.range)  # attack range circle (class Circle())
        self.cd_count = 0  # used in self.is_cool_down()
        self.cd_max_count = 60  # used in self.is_cool_down()
        self.is_selected = True  # the state of whether the tower is selected
        self.type = "tower"

    def is_cool_down(self):
        """
        Q2.1) Return whether the tower is cooling down
        (1) Use a counter to computer whether the tower is cooling down (( self.cd_count
        :return: Bool
        """

        """
        Hint:
        let counter be 0
        if the counter < max counter then
            set counter to counter + 1
        else 
            counter return to zero
        end if
        """
        # every max_count frames return False for meaning that this tower isn't cooling down
        if self.cd_count<self.cd_max_count:
            self.cd_count+=1
            return True
        else:
            self.cd_count=0
            return False
        pass

    def attack(self, enemy_group):
        """
        Q2.3) Attack the enemy.
        (1) check the the tower is cool down ((self.is_cool_down()
        (2) if the enemy is in attack range, then enemy get hurt. ((Circle.collide(), enemy.get_hurt()
        :param enemy_group: EnemyGroup()
        :return: None
        """

        # if the tower isn't cooling down
        if not(self.is_cool_down()):
            
            # check whether there is an attackable enemy in enemy_list
            enemy_list=enemy_group.get()
            for enemy in enemy_list:
                if self.range_circle.collide(enemy):

                    #attack enemy
                    enemy.get_hurt(self.damage)
                    break
        pass

    def is_clicked(self, x, y):
        """
        Bonus) Return whether the tower is clicked
        (1) If the mouse position is on the tower image, return True
        :param x: mouse pos x
        :param y: mouse pos y
        :return: Bool
        """

        # Return whether the tower is clicked
        return self.rect.collidepoint(x,y)
        pass

    def get_selected(self, is_selected):
        """
        Bonus) Change the attribute self.is_selected
        :param is_selected: Bool
        :return: None
        """
        self.is_selected = is_selected

    def draw(self, win):
        """
        Draw the tower and the range circle
        :param win:
        :return:
        """
        # draw range circle
        if self.is_selected:
            self.range_circle.draw_transparent(win)
        # draw tower
        win.blit(self.image, self.rect)


class TowerGroup:
    def __init__(self):
        self.constructed_tower = [Tower(250, 380), Tower(420, 400), Tower(600, 400)]

    def get(self):
        return self.constructed_tower

