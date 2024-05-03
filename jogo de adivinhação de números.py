import flet as ft 
import random 

numero_certo = random.randint(0,100)
numero_certo = int(numero_certo)
print(numero_certo)


def main(page: ft.page):
    page.title =  'Jogo de adivinhar numero' #Titulo Pagina
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #Deixar no centro
    def reiniciar(e):
        ...
    def confirmar_numero(e):
        txt_tentativas.value = str(int(txt_tentativas.value) + 1) #Soma Mais uma  tentativa
        page.update()

        txt_numero.value = int(txt_numero.value)
        if numero_certo == txt_numero.value:
                page.add(
                    ft.Text('Acertou'),
                )

        if txt_numero.value > numero_certo:
            page.add(
                ft.Text(f'O numero {txt_numero.value} e maior que o numero correto')
            )

        if txt_numero.value < numero_certo:
            page.add(
                ft.Text(f'O numero {txt_numero.value} e menor que o numero correto')
            )

        if txt_tentativas.value == '5':

            page.add(
                ft.Text('Voce Perdeu'),
                ft.ElevatedButton(text='Reiniciar', on_click=reiniciar),
            )
            page.update()

    txt_tentativas = ft.Text(value="0")
    txt_numero = ft.TextField(label='Adivinhe o numero correto',)
    buton = ft.ElevatedButton(text='Confiar Numero', on_click=confirmar_numero)


    page.add(
        ft.Row(
            [
            txt_tentativas,
            txt_numero,
            buton,
            
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)