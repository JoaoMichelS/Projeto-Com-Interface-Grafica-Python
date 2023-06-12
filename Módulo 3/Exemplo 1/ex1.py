from kivy.app import App               #Perceba que todo aplicativo Kivy precisa da
from kivy.uix.label import Label       #subclasse App e da função build(). É aqui que   
									   #você colocará seu código de interface do usuário
									   #ou fará chamadas para outras funções que definem
									   #seu código de interface usuário.
class MainApp(App):
	def build(self):                        #Neste caso, crie um widget do tipo label e passe 
		label = Label(text='Hello World!',  #como parâmetro: text_ size_hint, e pos_hint (es-
					size_hint=(.5, .5),     #tes dois últimos argumentos não são obrigatórios).
					pos_hint={'center_x': .5, 'center_y': .5}) #O comando size_hint informa ao Kivy
		return label                        #as proporções a serem usadas ao criar o widget.
                                            #Para isso são necessário dois números:
                                            #O primeiro número (x): refere-se à largura do
                                            #controle. O segundo número (y): refere-se à altura
                                            #do controle.
if __name__ == '__main__':
	app = MainApp()
	app.run()