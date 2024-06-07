import arcade, math
import arcade.color

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 750
SCREEN_TITLE = "Onde"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.count = 0

    def on_draw(self):
        arcade.start_render()
        for i in range(160):
            arcade.draw_rectangle_filled(0+10*i,600+math.tan((i+int(self.count)/10)/10)*50,10,10,arcade.color.RED,0)
        arcade.draw_rectangle_filled(0,100,1600*2,700,arcade.color.BLACK)
        for i in range(160):
            arcade.draw_rectangle_filled(0+10*i,330+math.sin((i*int(self.count)/10)/30)*90,10,10,arcade.color.YELLOW,0)
        for i in range(160):
            arcade.draw_rectangle_filled(0+10*i, math.sin((i+int(self.count)/10)/10)*50    , 10, 200, arcade.color.CYAN     , 0)
            arcade.draw_rectangle_filled(0+10*i, math.sin((150+i+int(self.count)/10)/10)*50, 10, 200, arcade.color.SEA_BLUE , 0)
            arcade.draw_rectangle_filled(0+10*i, math.sin((100+i+int(self.count)/10)/10)*50, 10, 200, arcade.color.DARK_BLUE, 0)

    def on_update(self, delta_time):
        self.count += 1

def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
