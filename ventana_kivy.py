from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import sys


class Formulario_con_Kivy(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10

        #Cajas de texto
        self.txt1 = TextInput(hint_text="Ingrese primer numero", multiline=False, input_filter="float")
        self.txt2 = TextInput(hint_text="Ingrese segundo numero", multiline=False, input_filter="float")
        self.add_widget(self.txt1)
        self.add_widget(self.txt2)

        #RadioButtons (ToggleButton con group)
        hbox_ops = BoxLayout(size_hint_y=None, height=40, spacing=5)
        self.suma = ToggleButton(text="+", group="ops")
        self.resta = ToggleButton(text="-", group="ops")
        self.multi = ToggleButton(text="*", group="ops")
        self.div = ToggleButton(text="/", group="ops")

        hbox_ops.add_widget(self.suma)
        hbox_ops.add_widget(self.resta)
        hbox_ops.add_widget(self.multi)
        hbox_ops.add_widget(self.div)
        self.add_widget(hbox_ops)

        #Botones
        hbox_btns = BoxLayout(size_hint_y=None, height=40, spacing=5)
        self.btn_ejecutar = Button(text="Ejecutar")
        self.btn_salir = Button(text="Salir")

        hbox_btns.add_widget(self.btn_ejecutar)
        hbox_btns.add_widget(self.btn_salir)
        self.add_widget(hbox_btns)

        #Resultado
        self.lbl_resultado = Label(text="Resultado: ", font_size=20)
        self.add_widget(self.lbl_resultado)

        # Eventos
        self.btn_ejecutar.bind(on_press=self.calcular)
        self.btn_salir.bind(on_press=lambda x: sys.exit(0))

    def calcular(self, instance):
        try:
            num1 = float(self.txt1.text)
            num2 = float(self.txt2.text)

            if self.suma.state == "down":
                resultado = num1 + num2
            elif self.resta.state == "down":
                resultado = num1 - num2
            elif self.multi.state == "down":
                resultado = num1 * num2
            elif self.div.state == "down":
                if num2 == 0:
                    self.mostrar_error("No se puede dividir entre cero")
                    return
                resultado = num1 / num2
            else:
                self.mostrar_error("Seleccione una operación")
                return

            self.lbl_resultado.text = f"Resultado: {resultado}"
        except ValueError:
            self.mostrar_error("Ingrese números válidos")

    def mostrar_error(self, mensaje):
        popup = Popup(title="Error",
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(300, 150))
        popup.open()


class Formulario_con_KivyApp(App):
    def build(self):
        return Formulario_con_Kivy()


if __name__ == "__main__":
    Formulario_con_KivyApp().run()