import tkinter as tk
from tkinter import messagebox

BOARD_SIZE = 8
TILE_SIZE = 60

PIECES = {
    "br": "♜", "bn": "♞", "bb": "♝", "bq": "♛", "bk": "♚", "bp": "♟",
    "wr": "♖", "wn": "♘", "wb": "♗", "wq": "♕", "wk": "♔", "wp": "♙",
    "--": ""
}

INITIAL_BOARD = [
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp"] * 8,
    ["--"] * 8,
    ["--"] * 8,
    ["--"] * 8,
    ["--"] * 8,
    ["wp"] * 8,
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
]


class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Šah sa pravilima - Tkinter")

        self.canvas = tk.Canvas(root, width=BOARD_SIZE * TILE_SIZE, height=BOARD_SIZE * TILE_SIZE)
        self.canvas.pack()

        self.board = [row[:] for row in INITIAL_BOARD]
        self.selected = None
        self.turn = "w"

        self.moved = {
            "wk": False, "bk": False,
            "wr0": False, "wr7": False,
            "br0": False, "br7": False
        }

        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        colors = ["#EEEED2", "#769656"]

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x1 = col * TILE_SIZE
                y1 = row * TILE_SIZE
                x2 = x1 + TILE_SIZE
                y2 = y1 + TILE_SIZE

                color = colors[(row + col) % 2]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

                piece = self.board[row][col]
                if piece != "--":
                    self.canvas.create_text(
                        x1 + TILE_SIZE // 2,
                        y1 + TILE_SIZE // 2,
                        text=PIECES[piece],
                        font=("Arial", 32),
                        fill="black" if piece[0] == "b" else "white"
                    )

    def on_click(self, event):
        col = event.x // TILE_SIZE
        row = event.y // TILE_SIZE

        if self.selected:
            sel_row, sel_col = self.selected
            if (sel_row, sel_col) != (row, col):
                self.try_move(sel_row, sel_col, row, col)
            self.selected = None
        else:
            piece = self.board[row][col]
            if piece != "--" and piece[0] == self.turn:
                self.selected = (row, col)

        self.draw_board()

    def try_move(self, from_row, from_col, to_row, to_col):
        piece = self.board[from_row][from_col]
        if self.is_valid_move(piece, from_row, from_col, to_row, to_col):
            captured = self.board[to_row][to_col]
            self.board[to_row][to_col] = piece
            self.board[from_row][from_col] = "--"

            # Rokada - pomeri topa
            if piece[1] == "k" and abs(to_col - from_col) == 2:
                if to_col > from_col:  # mala rokada
                    self.board[to_row][to_col - 1] = self.board[to_row][7]
                    self.board[to_row][7] = "--"
                else:  # velika rokada
                    self.board[to_row][to_col + 1] = self.board[to_row][0]
                    self.board[to_row][0] = "--"

            # Ne možeš se sam staviti u šah
            if self.is_in_check(self.turn):
                self.board[from_row][from_col] = piece
                self.board[to_row][to_col] = captured
                if piece[1] == "k" and abs(to_col - from_col) == 2:
                    # poništi i rokadu topa
                    if to_col > from_col:
                        self.board[to_row][7] = self.board[to_row][to_col - 1]
                        self.board[to_row][to_col - 1] = "--"
                    else:
                        self.board[to_row][0] = self.board[to_row][to_col + 1]
                        self.board[to_row][to_col + 1] = "--"
                messagebox.showinfo("Neispravan potez", "Ne možeš se sam staviti u šah.")
                return

            # Zabeleži pomeranja
            if piece == "wk":
                self.moved["wk"] = True
            elif piece == "bk":
                self.moved["bk"] = True
            elif piece == "wr" and from_row == 7 and from_col == 0:
                self.moved["wr0"] = True
            elif piece == "wr" and from_row == 7 and from_col == 7:
                self.moved["wr7"] = True
            elif piece == "br" and from_row == 0 and from_col == 0:
                self.moved["br0"] = True
            elif piece == "br" and from_row == 0 and from_col == 7:
                self.moved["br7"] = True

            # Promena poteza
            self.turn = "b" if self.turn == "w" else "w"

            # Mat proveri
            if self.is_in_check(self.turn) and not self.has_valid_moves(self.turn):
                messagebox.showinfo("Kraj igre", f"Mat! {'Beli' if self.turn == 'b' else 'Crni'} je pobedio.")
        else:
            messagebox.showinfo("Neispravan potez", "Taj potez nije dozvoljen po pravilima šaha.")

    def is_valid_move(self, piece, fr, fc, tr, tc):
        target = self.board[tr][tc]
        dx, dy = tr - fr, tc - fc
        color = piece[0]
        kind = piece[1]

        if target != "--" and target[0] == color:
            return False

        if kind == "p":
            direction = -1 if color == "w" else 1
            start_row = 6 if color == "w" else 1

            if dx == direction and fc == tc and self.board[tr][tc] == "--":
                return True
            if fr == start_row and dx == 2 * direction and fc == tc and \
                    self.board[fr + direction][fc] == "--" and self.board[tr][tc] == "--":
                return True
            if dx == direction and abs(dy) == 1 and target != "--" and target[0] != color:
                return True
            return False

        elif kind == "r":
            if fr != tr and fc != tc:
                return False
            if fr == tr:
                step = 1 if tc > fc else -1
                for c in range(fc + step, tc, step):
                    if self.board[fr][c] != "--":
                        return False
            else:
                step = 1 if tr > fr else -1
                for r in range(fr + step, tr, step):
                    if self.board[r][fc] != "--":
                        return False
            return True

        elif kind == "n":
            return (abs(dx), abs(dy)) in [(2, 1), (1, 2)]

        elif kind == "b":
            if abs(dx) != abs(dy):
                return False
            step_x = 1 if dx > 0 else -1
            step_y = 1 if dy > 0 else -1
            for i in range(1, abs(dx)):
                if self.board[fr + i * step_x][fc + i * step_y] != "--":
                    return False
            return True

        elif kind == "q":
            if fr == tr or fc == tc:
                return self.is_valid_move(color + "r", fr, fc, tr, tc)
            elif abs(dx) == abs(dy):
                return self.is_valid_move(color + "b", fr, fc, tr, tc)
            return False

        elif kind == "k":
            # Običan potez
            if abs(dx) <= 1 and abs(dy) <= 1:
                return True

            # Rokada
            if color == "w" and fr == 7 and fc == 4:
                if not self.moved["wk"] and dx == 0:
                    if dy == 2 and not self.moved["wr7"] and \
                            self.board[7][5] == "--" and self.board[7][6] == "--" and \
                            not self.is_in_check(color) and \
                            not self.square_under_attack(7, 5, "b") and \
                            not self.square_under_attack(7, 6, "b"):
                        return True
                    if dy == -2 and not self.moved["wr0"] and \
                            self.board[7][3] == "--" and self.board[7][2] == "--" and self.board[7][1] == "--" and \
                            not self.is_in_check(color) and \
                            not self.square_under_attack(7, 3, "b") and \
                            not self.square_under_attack(7, 2, "b"):
                        return True

            if color == "b" and fr == 0 and fc == 4:
                if not self.moved["bk"] and dx == 0:
                    if dy == 2 and not self.moved["br7"] and \
                            self.board[0][5] == "--" and self.board[0][6] == "--" and \
                            not self.is_in_check(color) and \
                            not self.square_under_attack(0, 5, "w") and \
                            not self.square_under_attack(0, 6, "w"):
                        return True
                    if dy == -2 and not self.moved["br0"] and \
                            self.board[0][3] == "--" and self.board[0][2] == "--" and self.board[0][1] == "--" and \
                            not self.is_in_check(color) and \
                            not self.square_under_attack(0, 3, "w") and \
                            not self.square_under_attack(0, 2, "w"):
                        return True
            return False

        return False

    def find_king(self, color):
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if self.board[r][c] == color + "k":
                    return (r, c)
        return None

    def is_in_check(self, color):
        king_pos = self.find_king(color)
        if not king_pos:
            return True
        kr, kc = king_pos
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                piece = self.board[r][c]
                if piece != "--" and piece[0] != color:
                    if self.is_valid_move(piece, r, c, kr, kc):
                        return True
        return False

    def square_under_attack(self, row, col, by_color):
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                piece = self.board[r][c]
                if piece != "--" and piece[0] == by_color:
                    if self.is_valid_move(piece, r, c, row, col):
                        return True
        return False

    def has_valid_moves(self, color):
        for r1 in range(BOARD_SIZE):
            for c1 in range(BOARD_SIZE):
                piece = self.board[r1][c1]
                if piece != "--" and piece[0] == color:
                    for r2 in range(BOARD_SIZE):
                        for c2 in range(BOARD_SIZE):
                            if (r1, c1) != (r2, c2) and self.is_valid_move(piece, r1, c1, r2, c2):
                                backup_from = self.board[r1][c1]
                                backup_to = self.board[r2][c2]
                                self.board[r2][c2] = piece
                                self.board[r1][c1] = "--"

                                in_check = self.is_in_check(color)

                                self.board[r1][c1] = backup_from
                                self.board[r2][c2] = backup_to

                                if not in_check:
                                    return True
        return False


if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()