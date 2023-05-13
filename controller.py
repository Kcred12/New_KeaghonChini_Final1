from PyQt5.QtWidgets import *
from view import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total = 0
        self.setupUi(self)

        # Initial values for item amounts to be used later
        self.cookie_amount = 0
        self.sandwich_amount = 0
        self.water_amount = 0

        # Hides the other elements not needed at the moment
        self.hide_order_screen()

        self.error_label.hide()

        # Connects all the buttons in the program to respective functions
        self.menu_button.clicked.connect(lambda: self.open_menu())
        self.add_button.clicked.connect(lambda: self.add_items())
        self.done_button.clicked.connect(lambda: self.finish_ordering())
        self.quit_button.clicked.connect(lambda: self.leave_program())

    def show_order_screen(self):

        """Shows every element of the order screen"""
        self.cookie_label.show()
        self.sandwich_label.show()
        self.water_label.show()
        self.receipt_label.show()
        self.cookie_entry.show()
        self.sandwich_entry.show()
        self.water_entry.show()
        self.add_button.show()
        self.done_button.show()

    def hide_order_screen(self):

        """Hides every element of the order screen"""
        self.cookie_label.hide()
        self.sandwich_label.hide()
        self.water_label.hide()
        self.receipt_label.hide()
        self.cookie_entry.hide()
        self.sandwich_entry.hide()
        self.water_entry.hide()
        self.add_button.hide()
        self.done_button.hide()

    def open_menu(self):
        """Hides the main menu and opens the order screen"""

        self.main_menu_label.hide()
        self.menu_button.hide()
        self.quit_button.hide()

        self.show_order_screen()
        self.cookie_entry.setFocus()

    def show_main_menu(self):
        """Makes the main menu visible"""

        self.main_menu_label.show()
        self.menu_button.show()
        self.quit_button.show()

    def add_items(self):
        """Adds the price of all items and amounts of items
            then displays it to the right of the ordering screen"""

        # Grabs the values from the text boxes, converts it to ints
        # and adds it to the running total
        if self.cookie_entry.text():
            self.cookie_amount += int(self.cookie_entry.text())
        else:
            self.cookie_amount += 0
        if self.sandwich_entry.text():
            self.sandwich_amount += int(self.sandwich_entry.text())
        else:
            self.sandwich_amount += 0
        if self.water_entry.text():
            self.water_amount += int(self.water_entry.text())
        else:
            self.water_amount += 0
        amount = self.cookie_amount * 1.5 + self.sandwich_amount * 4 + self.water_amount * 1
        self.total += amount

        # Sets the item count in a readable format along with the price and displays it
        self.receipt_label_text = f'{self.cookie_amount} Cookie(s)' \
                                  f'\n\n' \
                                  f'{self.sandwich_amount} Sandwich(es)' \
                                  f'\n\n' \
                                  f'{self.water_amount} Water(s)' \
                                  f'\n\n' \
                                  f'${self.total:.2f}'
        self.receipt_label.setText(self.receipt_label_text)
        self.error_label.hide()
        # Clearing the entries and setting focus allows the user
        # to input in succession without any issues
        self.cookie_entry.clear()
        self.sandwich_entry.clear()
        self.water_entry.clear()
        self.cookie_entry.setFocus()

    def finish_ordering(self):
        """Clears all data of previous order and goes to main menu"""

        self.receipt_label.clear()
        self.cookie_entry.clear()
        self.sandwich_entry.clear()
        self.water_entry.clear()
        self.total = 0
        self.cookie_amount = 0
        self.sandwich_amount = 0
        self.water_amount = 0
        self.hide_order_screen()
        self.show_main_menu()

    def leave_program(self):
        quit()
