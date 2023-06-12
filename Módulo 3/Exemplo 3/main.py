import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]         #Em seguida, cria lista de cores, que são lsitas de cores do 
green = [0,1,0,1]        #tipo RGB. Finalmente, você faz um loop, criando um botão btn
blue = [0,0,1,1]         #para cada iteração.
purple = [1,0,1,1]

class HBoxLayoutExample(App):
	def build(self):
		layout = BoxLayout(padding=10)
		colors = [red, green, blue, purple]

		for i in range(5):
			btn = Button(text=f"Este é o botão #{i+1}", #Para tornar as coisas um pouco mais 
			    background_color = random.choice(colors)
                )                                       #divertidas, você define background_color
													    #para uma cor aleatória.
			layout.add_widget(btn)
		return layout

if __name__ == "__main__":
	app = HBoxLayoutExample()
	app.run()