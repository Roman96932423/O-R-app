import flet as ft
from random import choice


def main(page: ft.Page):
    page.title = "O&R"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def create_text( u_text='', u_size=0, u_color='', u_italic=False):
        return ft.Text(u_text, size=u_size, color=u_color, italic=u_italic)

    player_points = 0
    computer_points = 0
    actions = ['Eagle', 'Tail']

    result = create_text('Result', 40)
    player_choice = create_text("Player choice: ", 23)
    computer_choice = create_text("Computer choice: ", 23)
    player_result = create_text(player_points, 23)
    computer_result = create_text(computer_points, 23)

    def eagle(event):
        computer_answer = choice(actions)
        player_choice.value = f"Player choice: {actions[0]}"
        computer_choice.value = f"Computer choice: {computer_answer}"

        if actions[0] in player_choice.value and actions[0] == 'Eagle':
            if actions[0] == computer_answer:
                result.value = "You win"
                player_result.value += 1

        if actions[0] in player_choice.value and actions[0] == 'Eagle':
            if actions[0] != computer_answer:
                result.value = "You lose"
                computer_result.value += 1

        page.update()

    def tail(event):
        computer_answer = choice(actions)
        player_choice.value = f"Player choice: {actions[1]}"
        computer_choice.value = f"Computer choice: {computer_answer}"

        if actions[1] in player_choice.value and actions[1] == 'Tail':
            if actions[1] == computer_answer:
                result.value = "You win"
                player_result.value += 1

        if actions[1] in player_choice.value and actions[1] == 'Tail':
            if actions[1] != computer_answer:
                result.value = "You lose"
                computer_result.value += 1

        page.update()

    page.add(
        ft.Row(
            [
                result
            ],
            spacing=150,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                player_result,
                computer_result
            ],
            spacing=150,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                player_choice,
                computer_choice
            ],
            spacing=150,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.OutlinedButton('Eagle', width=200, height=50, on_click=eagle),
                ft.OutlinedButton('Tail', width=200, height=50, on_click=tail),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                create_text("Author by Roman", 18, u_italic=True)
            ],
            alignment=ft.MainAxisAlignment.END
        )
    )


ft.app(target=main)
