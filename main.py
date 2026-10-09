from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class OTCSignalApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="OTC SIGNAL",
            font_size=32
        )
        layout.add_widget(title)

        eurusd = Button(
            text="EUR/USD OTC\nWAIT",
            font_size=22
        )
        layout.add_widget(eurusd)

        audcad = Button(
            text="AUD/CAD OTC\nWAIT",
            font_size=22
        )
        layout.add_widget(audcad)

        info = Label(
            text="Сигнал: ожидаем анализ",
            font_size=18
        )
        layout.add_widget(info)

        return layout


if __name__ == "__main__":
    OTCSignalApp().run()
