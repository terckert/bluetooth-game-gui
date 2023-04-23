from functools import partial
from kivy.app               import App 
from kivy.uix.button        import Button
from kivy.uix.widget        import Widget
from kivy.uix.label         import Label
from kivy.uix.gridlayout    import GridLayout
from kivy.uix.textinput     import TextInput


# Global variables
columns  = 4
rows     = 4
gridSize = columns * rows


class Gameboard(GridLayout):


    # Initialize keywords with infinite keywords
    def __init__(self, **kwargs):
        super(Gameboard, self).__init__(**kwargs) # Call inherited class

        self.cols = columns # setting the number of columns in the grid
        self.rows = rows
        self.lights = [LightButton(i) for i in range(gridSize)]
        for i in range(gridSize):
            self.add_widget(self.lights[i])

    
class LightButton(Button):
    
    def __init__(self, lightNo, **kwargs):
        super().__init__(**kwargs)
        self.lightNo = lightNo
        self.text = f"Light {self.lightNo}"
        self.bind(on_press=self.game_move)
        print(self)
    
    def game_move(self, second):
        print(f'You pressed "Light {self.lightNo}".')


class TimsBluetooth(App):
    
    def build(self):
        app = Gameboard()
        return app

class MainViewWindow(Widget):
    pass

class ConnectionButton(Button):
    pass

class InformationWindow(Label):
    pass

if __name__ == "__main__":    
    TimsBluetooth().run()