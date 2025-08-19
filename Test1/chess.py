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
        self.turn = "w"  # w = beli, b = crni

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
            self.board[to_row][to_col] = piece
            self.board[from_row][from_col] = "--"
            self.turn = "b" if self.turn == "w" else "w"
        else:
            messagebox.showinfo("Neispravan potez", "Taj potez nije dozvoljen po pravilima šaha.")

    def is_valid_move(self, piece, fr, fc, tr, tc):
        target = self.board[tr][tc]
        dx, dy = tr - fr, tc - fc
        color = piece[0]
        kind = piece[1]

        # Ne možeš jesti svoju figuru
        if target != "--" and target[0] == color:
            return False

        if kind == "p":  # Pijun
            direction = -1 if color == "w" else 1
            start_row = 6 if color == "w" else 1

            # Napred 1
            if dx == direction and fc == tc and self.board[tr][tc] == "--":
                return True
            # Napred 2
            if fr == start_row and dx == 2 * direction and fc == tc and \
                    self.board[fr + direction][fc] == "--" and self.board[tr][tc] == "--":
                return True
            # Dijagonalno jedenje
            if dx == direction and abs(dy) == 1 and target != "--" and target[0] != color:
                return True
            return False

        elif kind == "r":  # Top
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

        elif kind == "n":  # Skakač (konj)
            return (abs(dx), abs(dy)) in [(2, 1), (1, 2)]

        elif kind == "b":  # Lovac
            if abs(dx) != abs(dy):
                return False
            step_x = 1 if dx > 0 else -1
            step_y = 1 if dy > 0 else -1
            for i in range(1, abs(dx)):
                if self.board[fr + i * step_x][fc + i * step_y] != "--":
                    return False
            return True

        elif kind == "q":  # Kraljica
            if fr == tr or fc == tc:
                return self.is_valid_move(color + "r", fr, fc, tr, tc)
            elif abs(dx) == abs(dy):
                return self.is_valid_move(color + "b", fr, fc, tr, tc)
            return False

        elif kind == "k":  # Kralj
            return abs(dx) <= 1 and abs(dy) <= 1

        return False


if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()