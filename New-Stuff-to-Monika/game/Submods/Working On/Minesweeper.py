from math import ceil
import random
from tkinter.ttk import Button, Frame, Style
import tkinter as tk


class Cell(object):
	def __init__(self, row, column):
		self.__adjacent_mine_count = 0
		self.__cleared = False
		self.__coordinates = [row, column]
		self.__flagged = False
		self.__mine = None

	def clear(self):
		self.__cleared = True

	def get_adjacent_count(self):
		return self.__adjacent_mine_count

	def get_coordinates(self):
		return self.__coordinates

	def get_mine(self):
		return self.__mine

	def has_mine(self):
		return self.__mine is not None

	def is_cleared(self):
		return self.__cleared is True

	def is_flagged(self):
		return self.__flagged is True

	def set_adjacent_count(self, mine_count):
		if isinstance(mine_count, int):
			self.__adjacent_mine_count = mine_count

	def set_flagged_status(self, value=True):
		self.__flagged = value
		if self.has_mine():
			mine = self.__mine
			if value is True:
				mine.disarm()
			else:
				mine.arm()

	def set_mine(self, mine):
		if not self.has_mine() and isinstance(mine, Mine):
			self.__mine = mine


class Game(object):
	def __init__(self):
		self.__lost = False
		self.interface = Interface()

	def is_lost(self):
		return self.__lost

	def reset(self):
		pass  # @todo: re-initialize board

	def set_lost(self):
		self.__lost = True


class Interface(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.button_frame = None
		self.__minefield = None
		self.parent = parent
		self.buttons = list()
		self.initUI()

	def click_action(self, event, coordinates, recursive=True):
		minefield = self.__minefield
		button = self.buttons[coordinates[0]][coordinates[1]]
		cell = minefield.get_cell(coordinates)
		if cell.is_cleared() or (cell.is_flagged() and self.is_left_click(event.num)):
			return
		if self.is_left_click(event.num):
			minefield.action_triggered(coordinates)
		else:
			minefield.action_flagged(coordinates)

		status = minefield.evaluate()

		# continue playing condition
		if status is None:
			flag_style = 'TButton' if not cell.is_flagged() else 'Flagged.TButton'
			selected_style = 'Cleared.TButton' if self.is_left_click(event.num) else flag_style
			button.config(style=selected_style)
			if self.is_left_click(event.num):
				if cell.get_adjacent_count() > 0:
					button.config(text=str(cell.get_adjacent_count()))
				if recursive:
					for adjacent_square in minefield.get_surrounding_cells(coordinates):
						recursive = True if adjacent_square.get_adjacent_count() == 0 else False
						adjacent_coordinates = adjacent_square.get_coordinates()
						if not adjacent_square.has_mine():
							self.click_action(event, [adjacent_coordinates[0], adjacent_coordinates[1]], recursive)

		# failure playing condition
		elif status is False:
			button.config(style='Triggered.TButton')
			for row in range(minefield.get_row_count()):
				for column in range(minefield.get_column_count()):
					if row == coordinates[0] and column == coordinates[1]:
						continue
					tmp_cell = minefield.get_cell([row, column])
					if tmp_cell.has_mine():
						mine_button = self.buttons[row][column]
						mine_button.config(style='Revealed.TButton')

		# @todo: handle complete playing condition
		elif status is True:
			selected_style = 'Cleared.TButton' if self.is_left_click(event.num) else 'Flagged.TButton'
			button.config(style=selected_style)
			# @todo: update minefield display to show success

	def initUI(self):
		self.parent.title("Minesweeper")
		s = Style()
		s.theme_use('classic')
		s.configure('TButton', width=2, padding=(0, 0, 0, 0), background='#b9b9b9', relief=tk.FLAT)
		s.map('TButton', background=[('disabled', '#555555'), ('pressed', '#777777'), ('active', '#a8a8a8')])
		s.configure('Cleared.TButton', background='white')
		s.map('Cleared.TButton', background=[('active', 'white')])
		s.configure('Flagged.TButton', background='0066ff')
		s.map('Flagged.TButton', background=[('active', '#0044dd')])
		s.configure('Revealed.TButton', background='black')
		s.map('Revealed.TButton', background=[('active', 'black')])
		s.configure('Triggered.TButton', background='red')
		s.map('Triggered.TButton', background=[('active', 'red')])
		minefield = Minefield()
		self.__minefield = minefield

		# self.button_frame = Frame(self.parent)
		for i in range(minefield.get_row_count()):
			self.rowconfigure(i, pad=0)
		for i in range(minefield.get_column_count()):
			self.columnconfigure(i, pad=0)

		for row in range(minefield.get_row_count()):
			self.buttons.append(list())
			for column in range(minefield.get_column_count()):
				cell = minefield.get_cell([row, column])
				coordinates = cell.get_coordinates()
				button = Button(self, style='TButton')

				def run(event, self=self, internal_coordinates=coordinates):
					return self.click_action(event, internal_coordinates)

				button.bind('<Button-1>', run)
				button.bind('<Button-2>', run)
				button.bind('<Button-3>', run)
				button.grid(row=row, column=column)
				self.buttons[row].append(button)

		self.pack()

	def is_left_click(self, button_id):
		return button_id == 1


class Mine(object):
	def __init__(self):
		self.__armed = True
		self.__triggered = False

	def arm(self):
		self.__armed = True

	def disarm(self):
		self.__armed = False
	
	def is_disarmed(self):
		return self.__armed is False
		
	def is_triggered(self):
		return self.__triggered is True
	
	def trigger(self):
		self.__triggered = True


class Minefield(object):
	def __init__(self, rows=None, columns=None):
		self.__columns = 9 if not (columns is not None and isinstance(columns, int) and columns > 0) else columns
		self.__rows = 9 if not (rows is not None and isinstance(rows, int) and rows > 0) else rows
		self.__flag_count = 0
		self.__flag_limit = int(ceil((self.__columns * self.__rows) / 10.0))
		self.__matrix = list()
		self.__mine_limit = self.__flag_limit
		self.__populated = False

		for row in range(self.__rows):
			self.__matrix.append(list())
			for column in range(self.__columns):
				self.__matrix[row].append(Cell(row, column))

	def action_flagged(self, coordinates):
		cell = self.get_cell(coordinates)
		if not self.is_populated():
			self.populate()
		if cell.is_flagged():
			cell.set_flagged_status(False)
			self.__flag_count -= 1
		elif self.__flag_count < self.__flag_limit and not cell.is_flagged():
			cell.set_flagged_status()
			self.__flag_count += 1

	def action_triggered(self, coordinates):
		cell = self.get_cell(coordinates)
		if not self.is_populated():
			cell.clear()
			self.populate(coordinates)
		elif cell.has_mine():
			mine = cell.get_mine()
			mine.trigger()
		else:
			cell.clear()

	def evaluate(self):
		result = True
		for row in range(self.get_row_count()):
			for column in range(self.get_column_count()):
				cell = self.get_cell([row, column])
				if cell.has_mine():
					mine = cell.get_mine()
					if mine.is_triggered():
						return False
					if not cell.is_flagged() or not mine.is_disarmed():
						result = None
				else:
					if not cell.is_cleared():
						result = None
		# sanity check
		if self.__flag_count != self.__flag_limit:
			result = None

		return result

	def get_cell(self, coordinates):
		row = coordinates[0]
		column = coordinates[1]
		return self.__matrix[row][column]

	def get_column_count(self):
		return self.__columns

	def get_row_count(self):
		return self.__rows

	def get_surrounding_cells(self, coordinates):
		adjacent = list()
		if coordinates is None or not isinstance(coordinates, list) or len(coordinates) != 2:
			return adjacent

		row = coordinates[0]
		column = coordinates[1]

		for i_row in range(row - 1, row + 2):
			for i_col in range(column - 1, column + 2):
				if i_row >= 0 and i_col >= 0 and i_row < self.__rows and i_col < self.__columns:
					cell = self.__matrix[i_row][i_col]
					if i_row == row and i_col == column:
						continue
					adjacent.append(cell)

		return adjacent

	def is_populated(self):
		return self.__populated is True

	def populate(self, initial_coordinates=None):
		mine_count = 0
		while mine_count < self.__mine_limit:
			for row in range(self.__rows):
				for column in range(self.__columns):
					if initial_coordinates is not None:
						if row == initial_coordinates[0] and column == initial_coordinates[1]:
							continue
					if mine_count < self.__mine_limit and random.randint(1, 10) == random.randint(1, 10):
						cell = self.get_cell([row, column])
						cell.set_mine(Mine())
						mine_count += 1

		for row in range(self.__rows):
			for column in range(self.__columns):
				mine_count = 0
				for cell in self.get_surrounding_cells([row, column]):
					if cell.has_mine():
						mine_count += 1

				if mine_count > 0:
					cell = self.get_cell([row, column])
					cell.set_adjacent_count(mine_count)

		self.__populated = True

if '__main__' == __name__:
	root = tk.Tk()
	app = Interface(root)
	root.wm_attributes('-topmost', 1)
	root.mainloop()
