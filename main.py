import perspective as perspective
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective.point_x = NumericProperty(0)
    perspective.point_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        print("INIT W:" + str(self.width) + " H " + str(self.height))


class galaxyApp(App):
    pass


galaxyApp().run()