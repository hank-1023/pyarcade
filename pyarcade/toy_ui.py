import curses

from pyarcade.client import *
from curses import ascii


class UserInterface:
    def __init__(self, window):
        self.client = Client()
        self.window = window
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
        self.show_main_menu()

    def show_main_menu(self):
        self.client.end_game()
        menu = ['Hidden Sequence', "Mine Sweeper", "War", "Scores", "Exit"]
        selected_row = 0
        menu_functions = [self.show_hidden_sequence, self.show_mine_sweeper,
                          self.show_war, self.show_scores, None]

        self.update_menu_ui(menu, selected_row)

        self.wait_input(menu, selected_row, menu_functions)

    def show_hidden_sequence(self):
        if self.client.game_type is None:
            self.client.start_game(GameType.HIDDEN_SEQUENCE)
        elif self.client.get_game_state() != GameState.PENDING:
            self.show_game_state()
            return

        menu = ['Hidden Sequence', "Input Here", "Exit"]
        selected_row = 1
        self.update_menu_ui(menu, selected_row)
        self.wait_input(menu, selected_row, [self.show_hidden_sequence,
                                             self.show_text_input, self.show_main_menu])

    def show_mine_sweeper(self):
        if self.client.game_type is None:
            self.client.start_game(GameType.MINE_SWEEPER)
        elif self.client.get_game_state() != GameState.PENDING:
            self.show_game_state()
            return

        menu = ['Mine Sweeper', "Input Here", "Exit"]
        selected_row = 1
        self.update_menu_ui(menu, selected_row)
        self.wait_input(menu, selected_row, [self.show_mine_sweeper,
                                             self.show_text_input, self.show_main_menu])

    def show_war(self):
        if self.client.game_type is None:
            self.client.start_game(GameType.WAR)
        elif self.client.get_game_state() != GameState.PENDING:
            self.show_game_state()
            return

        menu = ['War', "Input Here", "Exit"]
        selected_row = 1
        self.update_menu_ui(menu, selected_row)
        self.wait_input(menu, selected_row, [self.show_war,
                                             self.show_text_input, self.show_main_menu])

    def show_scores(self):
        menu = ["Exit"]
        selected_row = 0
        self.update_menu_ui(menu, selected_row)

        all_history = self.client.get_all_history()
        history_string = "Overall, you've won " + str(all_history["Win"]) \
                         + " times!\nYou've lost " + str(all_history["Lose"]) + " times. "
        self.window.addstr(2, 0, history_string)

        self.wait_input(menu, selected_row, [self.show_main_menu])

    def show_text_input(self):
        curses.echo()
        prompt = ""
        help_string = "You can type \"reset\" to reset game, \"clear\" to clear game\n" \
                      "Invalid inputs will be ignored"
        game_type = self.client.game_type
        if game_type == GameType.HIDDEN_SEQUENCE:
            prompt = "Please input 4 digits: "
        elif game_type == GameType.MINE_SWEEPER:
            prompt = "Please input two numbers separated by comma (1 based): "
        elif game_type == GameType.WAR:
            prompt = "Please type in \"deal\" to deal: "

        self.window.clear()
        self.window.addstr(0, 0, help_string)
        self.window.addstr(3, 0, prompt)

        buffer = ""
        while True:
            key = self.window.getch()
            if key == curses.KEY_ENTER or key == 10:
                break
            buffer += ascii.unctrl(key)
        self.client.parse_execute_input(buffer)

        if game_type == GameType.HIDDEN_SEQUENCE:
            self.show_hidden_sequence()
        elif game_type == GameType.MINE_SWEEPER:
            self.show_mine_sweeper()
        elif game_type == GameType.WAR:
            self.show_war()

    def show_game_state(self):
        menu = ["Exit"]
        selected_row = 0

        game_state = self.client.get_game_state()
        game_state_string = ""
        if game_state == GameState.WIN:
            game_state_string = "You've Won!!!"
        elif game_state == GameState.LOSE:
            game_state_string = "You've Lost."
        elif game_state == GameState.TIE:
            game_state_string = "You've tied with the computer!"

        self.client.end_game()
        self.update_menu_ui(menu, selected_row)
        self.window.addstr(2, 0, game_state_string)
        self.wait_input(menu, selected_row, [self.show_main_menu])

    def wait_input(self, menu: [int], selected_row: int, menu_functions_cbs):
        while True:
            key = self.window.getch()

            if key == curses.KEY_UP and len(menu) != 1:
                selected_row = max(0, selected_row - 1)
                self.update_menu_ui(menu, selected_row)
            elif key == curses.KEY_DOWN and len(menu) != 1:
                selected_row = min(len(menu) - 1, selected_row + 1)
                self.update_menu_ui(menu, selected_row)
            elif key == curses.KEY_ENTER or key == 10:
                break

        if menu_functions_cbs[selected_row]:
            menu_functions_cbs[selected_row]()

    def update_menu_ui(self, menu: [str], selected_row: int):
        self.window.clear()
        # No echos in menu typed screens
        curses.noecho()

        for index, item in enumerate(menu):
            if index == selected_row:
                self.window.attron(curses.color_pair(1))
                self.window.addstr(index, 0, item)
                self.window.attroff(curses.color_pair(1))
            else:
                self.window.addstr(index, 0, item)

        display_data = self.client.get_display_data()
        self.window.addstr(len(menu) + 1, 0, display_data)

        self.window.refresh()
