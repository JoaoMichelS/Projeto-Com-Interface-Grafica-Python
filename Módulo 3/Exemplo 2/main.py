from kivy.app import App
from kivy.uix.image import Image, AsyncImage   #Nesse código, importamos AsyncImage do 
																							 #kivy.uix.image
class MainApp(App): #A classe AsyncImage usa muitos parâmetros diferentes, mas o que você
	def build(self):  #deseja usar é source. Isso informa ao Kivy qual imagem carregar.
	    img = AsyncImage(source='https://supermariorun.com/assets/img/stage/mario03.png',
					size_hint = (1, .5),
					pos_hint = {'center_x': .5, 'center_y': .5})
	    return img

if __name__ == '__main__':
	app = MainApp()
	app.run()