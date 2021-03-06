"""
Kevin Wu p6 r23
NOTE: Micheal might use this as part of his project for his game sharing platform.

********************
Sources

CS111
cs111.wellesley.edu/~cs111/archive/cs111_spring15/public_html/labs/lab12/tkintercolor.html
Documentation of all tkinter color names

********************
"""

from tkinter import * 
import sys
import copy
import urllib.request
import urllib.parse
import hashlib
import json

payload = {
    'password': hashlib.sha512('123'.encode()).hexdigest(),
    'id' : '123'
           }
data = urllib.parse.urlencode(payload)
data = data.encode('ascii')
json.dumps(payload).encode('utf8')
response = urllib.request.urlopen('http://chessgame.pythonanywhere.com/game/123', data) 
html = response.read().decode('utf-8')

print(html)

class ChessPiece(Label):
    def __init__(self, master, pieceName, pieceImage, position, activated=True):
        Label.__init__(self, master, image=pieceImage, height=60, width=60)
        self.bind("<Button-1>", self.master.get_click)
        self.position = position
        self.pieceName = pieceName
        self.master = master


class ChessGrid(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.bind("<Button-1>", self.flip)
        self.master = master
        self.wpawn = PhotoImage(file="w_pawn.gif")
        self.wrook = PhotoImage(file="w_rook.gif")
        self.wbishop = PhotoImage(file="w_bishop.gif")
        self.wknight = PhotoImage(file="w_knight.gif")
        self.wking = PhotoImage(file="w_king.gif")
        self.wqueen = PhotoImage(file="w_queen.gif")
        self.bpawn = PhotoImage(file="b_pawn.gif")
        self.brook = PhotoImage(file="b_rook.gif")
        self.bbishop = PhotoImage(file="b_bishop.gif")
        self.bknight = PhotoImage(file="b_knight.gif")
        self.bking = PhotoImage(file="b_king.gif")
        self.bqueen = PhotoImage(file="b_queen.gif")
        self.blanksquare = PhotoImage()
        self.board = [[None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None]]
        for i in range(8):
            for x in range(8):
                self.board[i][x] = ChessPiece(self, "", self.blanksquare, [i, x])
        for i in range(8):
            self.board[i][1] = ChessPiece(self, "wPawn", self.wpawn, [i, 1])
        for i in [0, 7]:
            for x in [0]:
                self.board[i][x] = ChessPiece(self, "wRook", self.wrook, [i, x])
        for i in [1, 6]:
            for x in [0]:
                self.board[i][x] = ChessPiece(self, "wKnight", self.wknight, [i, x])
        for i in [2, 5]:
            for x in [0]:
                self.board[i][x] = ChessPiece(self, "wBishop", self.wbishop, [i, x])
        self.board[3][0] = ChessPiece(self, "wQueen", self.wqueen, [3, 0])
        self.board[4][0] = ChessPiece(self, "wKing", self.wking, [4, 0])
        for i in range(8):
            self.board[i][6] = ChessPiece(self, "bPawn", self.bpawn, [i, 6])
        for i in [0, 7]:
            for x in [7]:
                self.board[i][x] = ChessPiece(self, "bRook", self.brook, [i, x])
        for i in [1, 6]:
            for x in [7]:
                self.board[i][x] = ChessPiece(self, "bKnight", self.bknight, [i, x])
        for i in [2, 5]:
            for x in [7]:
                self.board[i][x] = ChessPiece(self, "bBishop", self.bbishop, [i, x])
        self.board[3][7] = ChessPiece(self, "bQueen", self.bqueen, [3, 7])
        self.board[4][7] = ChessPiece(self, "bKing", self.bking, [4, 7])
        for i in range(8):
            for x in range(8):
                self.board[i][x].grid(row=7 - x, column=i)
        for i in self.board:
            for j in i:
                j.config(bg="antique white")
        for i in [0, 2, 4, 6]:
            for x in [0, 2, 4, 6]:
                self.board[i][x].config(bg="green4")
                self.board[i + 1][x + 1].config(bg="green4")
        self.turn = 0

    def flip(self):
        self.turn = 1 - self.turn
        if self.turn == 0:
            for i in range(8):
                for x in range(8):
                    self.board[i][x].grid_forget()
                    self.board[i][x].grid(row=7 - x, column=i)
            for i in self.board:
                for j in i:
                    j.config(bg="antique white")
            for i in [0, 2, 4, 6]:
                for x in [0, 2, 4, 6]:
                    self.board[i][x].config(bg="green4")
                    self.board[i + 1][x + 1].config(bg="green4")
        elif self.turn == 1:
            for i in range(8):
                for x in range(8):
                    self.board[i][x].grid_forget()
                    self.board[i][x].grid(row=x, column=i)
            for i in self.board:
                for j in i:
                    j.config(bg="green4")
            for i in [0, 2, 4, 6]:
                for x in [0, 2, 4, 6]:
                    self.board[i][x].config(bg="antique white")
                    self.board[i + 1][x + 1].config(bg="antique white")

    def set_up_board(self, strboard):
        for i in range(8):
            for x in range(8):
                self.board[i][x].config(image=
                                        [self.wrook, self.wpawn, self.wbishop, self.wknight, self.wking, self.wqueen,
                                         self.brook, self.bpawn, self.bbishop, self.bknight, self.bking, self.bqueen,
                                         self.blanksquare][
                                            ["wRook", "wPawn", "wBishop", "wKnight", "wKing", "wQueen",
                                             "bRook", "bPawn", "bBishop", "bKnight", "bKing", "bQueen", ""].index(
                                                strboard[i][x])])

    def reset_bg(self):
        for i in self.board:
            for j in i:
                j.config(bg="antique white")
        for i in [0, 2, 4, 6]:
            for x in [0, 2, 4, 6]:
                self.board[i][x].config(bg="green4")
                self.board[i + 1][x + 1].config(bg="green4")

    def get_click(self, event):
        self.master.get_click(event)


'''
class promotionMenu(Frame):
    def __init__(self, color):
        Frame.__init__(self)
        self.pieceTypes = ['Rook', 'Knight', 'Queen', 'Bishop']
        self.wpawn = PhotoImage(file="w_pawn.gif")
        self.wrook = PhotoImage(file="w_rook.gif")
        self.wbishop = PhotoImage(file="w_bishop.gif")
        self.wknight = PhotoImage(file="w_knight.gif")
        self.wking = PhotoImage(file="w_king.gif")
        self.wqueen = PhotoImage(file="w_queen.gif")
        self.bpawn = PhotoImage(file="b_pawn.gif")
        self.brook = PhotoImage(file="b_rook.gif")
        self.bbishop = PhotoImage(file="b_bishop.gif")
        self.bknight = PhotoImage(file="b_knight.gif")
        self.bking = PhotoImage(file="b_king.gif")
        self.bqueen = PhotoImage(file="b_queen.gif")
        self.pieceImages = [
                            [PhotoImage(file="w_rook.gif"), PhotoImage(file="b_rook.gif")],
                            [PhotoImage(file="w_knight.gif"), PhotoImage(file="b_knight.gif")],
                            [PhotoImage(file="w_queen.gif"), PhotoImage(file="b_queen.gif")],
                            [PhotoImage(file="w_bishop.gif"), PhotoImage(file="b_bishop.gif")]
                            ]
        self.pieces = []
        for i in range(len(self.pieceTypes)):
            self.pieces.append(ChessPiece(self, color + self.pieceTypes[i], self.pieceImages[i][['w', 'b'].index(color)], [i,0]))
            self.pieces[i].grid(column=i)

    def get_click(self, event):
        print('MEMES')
'''


class ChessFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.tkGrid = ChessGrid(self)
        self.tkGrid.pack()
        self.turnColor = 0
        self.strboard = [['wRook', 'wPawn', '', '', '', '', 'bPawn', 'bRook'],
                         ['wKnight', 'wPawn', '', '', '', '', 'bPawn', 'bKnight'],
                         ['wBishop', 'wPawn', '', '', '', '', 'bPawn', 'bBishop'],
                         ['wQueen', 'wPawn', '', '', '', '', 'bPawn', 'bQueen'],
                         ['wKing', 'wPawn', '', '', '', '', 'bPawn', 'bKing'],
                         ['wBishop', 'wPawn', '', '', '', '', 'bPawn', 'bBishop'],
                         ['wKnight', 'wPawn', '', '', '', '', 'bPawn', 'bKnight'],
                         ['wRook', 'wPawn', '', '', '', '', 'bPawn', 'bRook']]
        self.isPieceSelected = False
        self.pieceSelectedPosition = None
        self.wKingCastleKingside = True
        self.bKingCastleQueenside = True
        self.bKingCastleKingside = True
        self.wKingCastleQueenside = True
        self.enPassant = None       

    def update_board(self, board):
        # This function is also for validation and is similar to do_move
        self.strboard = copy.deepcopy(board)

    def do_move(self, initial, second):
        self.strboard[second[0]][second[1]] = self.strboard[initial[0]][initial[1]]
        self.strboard[initial[0]][initial[1]] = ''
        self.tkGrid.set_up_board(self.strboard)

    def moves_exist(self, color):
        # This method will be used for checking for stalemates and/or checkmates
        for i in range(8):
            for x in range(8):
                pieceName = self.strboard[i][x]
                if ['w', 'b', ' '].index((pieceName + " ")[0]) == color:
                    # You don't need to check for castling because the no castling through check rule exists
                    possible_moves = []
                    for second in self.find_moves([i, x]):
                        possible_moves.append([[i, x], second])
                    for move in possible_moves:
                        if self.validate_move(move[0], move[1]):
                            return True
        return False

    def is_check(self, color):
        # Checks to see if the player with color color has check on the other player
        for i in range(8):
            for x in range(8):
                if ["w", "b", " "].index(
                        (self.strboard[i][x] + " ")[0]) == color:

                    for z in self.find_moves([i, x]):
                        if (self.strboard[z[0]][z[1]] + " ")[1:] == "King ":
                            return True
        return False

    def validate_move(self, initial, second):
        # This function will work by creating another chessFrame that has the board with the move done, then it will
        # see whether or not it leaves your king in check or not.
        validationBoard = ChessFrame()
        validationBoard.update_board(self.strboard)
        validationBoard.do_move(initial, second)
        validationBoard.turnColor = 1 - self.turnColor

        if validationBoard.is_check(1 - self.turnColor):
            return False

        # print(self.strboard)
        return True

    def exists_highlighted(self):
        for i in range(8):
            for x in range(8):
                if self.tkGrid.board[i][x]['bg'] in ['red3', 'red2']:
                    return True
        return False

    def get_click(self, event):
        if self.isPieceSelected:
            # This prevents enforcement of touch move rule
            if self.pieceSelectedPosition == event.widget.position:
                self.isPieceSelected = False
                self.pieceSelectedPosition = None
                self.tkGrid.reset_bg()
                return

            # This prevents illegal moves
            if not(self.validate_move(self.pieceSelectedPosition, event.widget.position)):
                messagebox.showerror('Chess', 'Invalid Move', parent=self)
                return

            # If this if statement returns true, that means it wasn't highlighted
            # as part of the valid moves before implementing check
            if not (self.tkGrid.board[event.widget.position[0]][event.widget.position[1]]['bg'] in ["red3",
                                                                                                    "red2"]):
                messagebox.showerror('Chess', 'Invalid Move', parent=self)
                # print("RIP")
                return

            # print(self.pieceSelectedPosition[1], event.widget.position[1])
            # The following code will handle allowing en passant.
            if self.pieceName[1:] == 'Pawn ' and self.strboard[event.widget.position[0]][event.widget.position[1]] == '' and self.enPassant:
                self.do_move(self.pieceSelectedPosition, event.widget.position)
                self.strboard[event.widget.position[0]][event.widget.position[1]-['b', 'w'].index(self.pieceName[0])*2+1] = ''
                self.tkGrid.board[event.widget.position[0]][event.widget.position[1]-['b', 'w'].index(self.pieceName[0])*2+1].config(image=self.tkGrid.blanksquare)
                self.enPassant = None
                self.tkGrid.reset_bg()
                self.isPieceSelected = False
                self.pieceSelectedPosition = None
                self.turnColor = 1 - self.turnColor
                if self.moves_exist(self.turnColor) == False:
                    if self.is_check(1 - self.turnColor):
                        messagebox.showinfo("Chess", "Game Over, {} wins!".format(['white', 'black'][1 - self.turnColor]))
                    else:
                        messagebox.showinfo("Chess", "Game Over, Stalemate")
                    self.destroy()
                return
            
            if (self.pieceName)[1:] == "Pawn ":
                if (self.pieceName + " ")[0] == "w" and self.pieceSelectedPosition[1] == 1 and event.widget.position[1] == 3:
                    self.enPassant = event.widget.position
                    # print("Success!")
                elif self.pieceSelectedPosition[1] == 6 and event.widget.position[1] == 4:
                    self.enPassant = event.widget.position
                    # print("Success!")
                else:
                    self.enPassant = None

                # Now that that is done, I will now do AUTO PROMOTION
                if event.widget.position[1] == 7:
                    self.tkGrid.board[self.pieceSelectedPosition[0]][self.pieceSelectedPosition[1]].config(image=self.tkGrid.wqueen)
                    self.strboard[self.pieceSelectedPosition[0]][self.pieceSelectedPosition[1]] = self.pieceName[0] + 'Queen'
                if event.widget.position[1] == 0:
                    self.tkGrid.board[self.pieceSelectedPosition[0]][self.pieceSelectedPosition[1]].config(image=self.tkGrid.bqueen)
                    self.strboard[self.pieceSelectedPosition[0]][self.pieceSelectedPosition[1]] = self.pieceName[0] + 'Queen'
                    

            # This will do handling for invalidating castling after king/rook has been moved
            if self.pieceName == "wKing ":
                self.wKingCastleQueenside = False
                self.wKingCastleKingside = False
            if self.pieceName == "bKing ":
                self.bKingCastleQueenside = False
                self.bKingCastleKingside = False
            if self.pieceName == "wRook " and self.pieceSelectedPosition == [7, 0]:
                self.wKingCastleKingside = False
            if self.pieceName == "wRook " and self.pieceSelectedPosition == [0, 0]:
                self.wKingCastleQueenside = False
            if self.pieceName == "bRook " and self.pieceSelectedPosition == [7, 0]:
                self.bKingCastleKingside = False
            if self.pieceName == "bRook " and self.pieceSelectedPosition == [0, 0]:
                self.bKingCastleQueenside = False

            # Now we will do handling for valid/invalid moves
            # print("YAY")
            self.do_move(self.pieceSelectedPosition, event.widget.position)
            self.tkGrid.reset_bg()
            self.isPieceSelected = False
            self.pieceSelectedPosition = None
            self.turnColor = 1 - self.turnColor
            
            # Now we have to do handling for stalemate and checks
            if self.moves_exist(self.turnColor) == False:
                if self.is_check(1 - self.turnColor):
                    messagebox.showinfo("Chess", "Game Over, {} wins!".format(['white', 'black'][1 - self.turnColor]))
                else:
                    messagebox.showinfo("Chess", "Game Over, Stalemate")
                self.destroy()
        else:
            # print(self.strboard[event.widget.position[0]][event.widget.position[1]])
            pieceName = self.strboard[event.widget.position[0]][event.widget.position[1]] + " "

            if ["w", "b", " "].index(pieceName[0]) != self.turnColor:
                return
            # This prevents the opponent from moving your pieces.

            positions = self.find_moves(event.widget.position)
            if positions == None:
                return
            # This prevents you from crashing the program
            # (just in case I wrote something wrong and instead of an empty list it gives you a NoneType)
            # This big if statement will handle castling
            if pieceName[1:] == "King ":
                # print("xd")
                # print(self.wKingCastleQueenside)
                # print(self.wKingCastleKingside)
                # So here I'm going to write code to handle the no castling in check move
                # print(self.is_check(1 - self.turnColor))
                if self.is_check(1 - self.turnColor):
                    positions = self.find_moves(event.widget.position)
                else:
                    # print(self.turnColor)
                    # So here I'm going to do checking to see if you can castle Kingside
                    currentCanCastleKingside = False
                    currentCanCastleQueenside = False
                    if self.turnColor == 0 and self.wKingCastleKingside:
                        # This will check to see if the squares are unoccupied
                        for i in range(1, 3):
                            # print(self.validate_move(event.widget.position,
                                                     # [event.widget.position[0] + i, event.widget.position[1]]))
                            if not (self.strboard[event.widget.position[0] + i][
                                event.widget.position[1]]) and self.validate_move(event.widget.position,
                                                                                  [event.widget.position[0] + i,
                                                                                   event.widget.position[1]]):
                                if i == 2:
                                    currentCanCastleKingside = True
                            else:
                                break
                    if self.turnColor == 0 and self.wKingCastleQueenside:
                        # This will check to see if the squares are unoccupied
                        # print("hi")
                        for i in range(1, 3):
                            if not (self.strboard[event.widget.position[0] - i][event.widget.position[1]]):
                                if i == 2:
                                    currentCanCastleQueenside = True
                            else:
                                break
                    if self.turnColor == 1 and self.bKingCastleQueenside:
                        # This will check to see if the squares are unoccupied
                        for i in range(1, 3):
                            if not (self.strboard[event.widget.position[0] - i][event.widget.position[1]]):
                                if i == 2:
                                    currentCanCastleQueenside = True
                            else:
                                break

                    if self.turnColor == 1 and self.bKingCastleKingside:
                        # This will check to see if the squares are unoccupied
                        for i in range(1, 3):
                            if not (self.strboard[event.widget.position[0] + i][event.widget.position[1]]):
                                if i == 2:
                                    currentCanCastleKingside = True
                            else:
                                break

                    positions = self.find_moves(event.widget.position, castleKingside=currentCanCastleKingside,
                                                castleQueenside=currentCanCastleQueenside)
            if type(self.enPassant) == list:
                # The logic I will use is that if the piece is of the oppositie color and they are
                # right next to eachother, then I will add the en passant to positions.
                # print(event.widget.position, self.enPassant)
                if event.widget.position[1] == self.enPassant[1] and abs(event.widget.position[0]-self.enPassant[0]) == 1:
                    positions.append([self.enPassant[0], self.enPassant[1]+['b', 'w'].index(pieceName[0])*2-1])
            
            self.isPieceSelected = True
            self.pieceSelectedPosition = event.widget.position
            self.pieceName = pieceName
            
            for i in positions:
                if self.tkGrid.board[i[0]][i[1]]['bg'] == "green4":
                    self.tkGrid.board[i[0]][i[1]].config(bg="red3")
                elif self.tkGrid.board[i[0]][i[1]]['bg'] == "antique white":
                    self.tkGrid.board[i[0]][i[1]].config(bg="red2")

            # This will prevent misclicks on pieces from messing you up
            if not (self.exists_highlighted()):
                self.isPieceSelected = False
                self.pieceSelectedPosition = None
                self.tkGrid.reset_bg()
                return

    def find_moves(self, pos, castleKingside=False, castleQueenside=False):
        pieceName = (self.strboard[pos[0]][pos[1]] + " ")[1:]
        if pieceName == "Pawn ":
            return self.pawn_moves(pos)
        elif pieceName == "Bishop ":
            return self.bishop_moves(pos)
        elif pieceName == "Rook ":
            return self.rook_moves(pos)
        elif pieceName == "Knight ":
            return self.knight_moves(pos)
        elif pieceName == "Queen ":
            return self.queen_moves(pos)
        elif pieceName == "King ":
            return self.king_moves(pos, castleKingside=castleKingside, castleQueenside=castleQueenside)

    def remove_pawns(self):
        for i in range(8):
            for x in range(8):
                if 'Pawn' in self.strboard[i][x]:
                    self.strboard[i][x] = ""
                    self.tkGrid.board[i][x].config(image=self.tkGrid.blanksquare)

    def pawn_moves(self, pos):
        possible_moves = []
        a = pos[0]
        b = pos[1]
        if self.turnColor == 0:
            if self.strboard[a][b][0] == "b":
                return []
            if b == 1:
                try:
                    if "b" in self.strboard[a][b + 1] or "w" in self.strboard[a][b + 1]:
                        pass
                    elif "b" in self.strboard[a][b + 2] or "w" in self.strboard[a][b + 2]:
                        possible_moves.append([a, b + 1])
                    else:
                        possible_moves.extend([[a, b + 1], [a, b + 2]])
                except (TypeError, IndexError):
                    pass
                try:
                    if "b" in self.strboard[a + 1][b + 1] and "b" in self.strboard[a - 1][b + 1] and a - 1 >= 0:
                        possible_moves.append([a + 1, b + 1])
                        possible_moves.append([a - 1, b + 1])
                except (TypeError, IndexError):
                    pass
                try:
                    if "b" in self.strboard[a + 1][b + 1]:
                        possible_moves.append([a + 1, b + 1])
                except (TypeError, IndexError):
                    pass
                try:
                    if "b" in self.strboard[a - 1][b + 1] and a - 1 >= 0:
                        possible_moves.append([a - 1, b + 1])
                except (TypeError, IndexError):
                    pass
            else:
                try:
                    if "b" in self.strboard[a][b + 1] or "w" in self.strboard[a][b + 1]:
                        pass
                    else:
                        possible_moves.append([a, b + 1])
                except (TypeError, IndexError):
                    pass
                try:
                    if "b" in self.strboard[a + 1][b + 1] and "b" in self.strboard[a - 1][b + 1]:
                        possible_moves.extend([[a + 1, b + 1], [a - 1, b + 1]])
                except (TypeError, IndexError):
                    pass
                try:
                    if "b" in self.strboard[a + 1][b + 1]:
                        possible_moves.append([a + 1, b + 1])
                except (TypeError, IndexError):
                    pass
                try:
                    if "b" in self.strboard[a - 1][b + 1]:
                        possible_moves.append([a - 1, b + 1])
                except (TypeError, IndexError):
                    pass
        else:
            if self.strboard[a][b][0] == "w":
                return []
            if b == 6:
                try:
                    if "w" in self.strboard[a][b - 1] or "b" in self.strboard[a][b - 1]:
                        pass
                    elif "w" in self.strboard[a][b - 2] or "b" in self.strboard[a][b - 2]:
                        possible_moves.append([a, b - 1])
                    else:
                        possible_moves.append([a, b - 1])
                        possible_moves.append([a, b - 2])
                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a - 1][b - 1] and "w" in self.strboard[a - 1][
                        b - 1] and a - 1 >= 0 and not (self.strboard[a + 1][b - 1] == "bPawn") and not (
                            self.strboard[a - 1][b - 1] == "bPawn"):
                        possible_moves.append([a + 1, b - 1])
                        possible_moves.append([a - 1, b - 1])

                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a + 1][b - 1] and not (self.strboard[a + 1][b - 1] == "bPawn"):
                        possible_moves.append([a + 1, b - 1])
                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a - 1][b - 1] and a - 1 >= 0 and not (
                            self.strboard[a - 1][b - 1] == "bPawn"):
                        possible_moves.append([a - 1, b - 1])
                except (TypeError, IndexError):
                    pass
            else:
                if "w" in self.strboard[a][b - 1] or "b" in self.strboard[a][b - 1]:
                    pass
                else:
                    possible_moves.append([a, b - 1])
                try:
                    if "w" in self.strboard[a + 1][b - 1] and "w" in self.strboard[a - 1][
                        b - 1] and a - 1 > -0 and not (self.strboard[a + 1][b - 1] == "bPawn") and not (
                            self.strboard[a - 1][b - 1] == "bPawn"):
                        possible_moves.append([a + 1, b - 1])
                        possible_moves.append([a - 1, b - 1])
                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a + 1][b - 1] and not (self.strboard[a + 1][b - 1] == "bPawn"):
                        possible_moves.append([a + 1, b - 1])
                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a - 1][b - 1] and not (
                            self.strboard[a - 1][b - 1] == "bPawn") and a - 1 >= 0:
                        possible_moves.append([a - 1, b - 1])
                except (TypeError, IndexError):
                    pass
        return possible_moves

    def bishop_moves(self, pos):
        possible_moves = []
        a = pos[0]
        b = pos[1]
        colors = ["w", "b"]
        piece_color = self.strboard[a][b][0]
        opposite_piece_color = colors[1 - colors.index(piece_color)]
        try:
            for i in range(1, 8):
                current_string = self.strboard[a + i][b - i] + " "
                if current_string[0] == opposite_piece_color and b - i >= 0:
                    possible_moves.append([a + i, b - i])
                    break
                elif current_string[0] == piece_color:
                    break
                elif b - i < 0:
                    break
                else:
                    possible_moves.append([a + i, b - i])
        except IndexError:
            pass
        try:
            for i in range(1, 8):
                current_string = self.strboard[a - i][b - i] + " "
                if current_string[0] == opposite_piece_color and b - i >= 0 and a - i >= 0:
                    possible_moves.append([a - i, b - i])
                    break
                elif current_string[0] == piece_color:
                    break
                elif b - i < 0:
                    break
                elif a - i < 0:
                    break
                else:
                    possible_moves.append([a - i, b - i])
        except IndexError:
            pass
        try:
            for i in range(1, 8):
                current_string = self.strboard[a + i][b + i] + " "
                if current_string[0] == opposite_piece_color:
                    possible_moves.append([a + i, b + i])
                    break
                elif current_string[0] == piece_color:
                    break
                else:
                    possible_moves.append([a + i, b + i])
        except IndexError:
            pass
        try:
            for i in range(1, 8):
                current_string = self.strboard[a - i][b + i] + " "
                if current_string[0] == opposite_piece_color and a - i >= 0:
                    # print('yay')
                    possible_moves.append([a - i, b + i])
                    break
                elif current_string[0] == piece_color:
                    break
                elif a - i < 0:
                    break
                else:
                    possible_moves.append([a - i, b + i])
        except IndexError:
            pass
        return possible_moves

    def knight_moves(self, pos):
        possible_moves = []
        a = pos[0]
        b = pos[1]
        colors = ["w", "b"]
        piece_color = self.strboard[a][b][0]
        opposite_piece_color = colors[1 - colors.index(piece_color)]
        for i in [2, 1, -2, -1]:
            for x in [2, 1, -2, -1]:
                if abs(i) != abs(x):
                    try:
                        if (self.strboard[a + i][b + x] + " ")[0] == opposite_piece_color and a + i >= 0 and b + x >= 0:
                            possible_moves.append([a + i, b + x])
                        elif (self.strboard[a + i][b + x] + " ")[0] == piece_color:
                            pass
                        elif a + i < 0:
                            pass
                        elif b + x < 0:
                            pass
                        else:
                            possible_moves.append([a + i, b + x])
                    except IndexError:
                        pass
        return possible_moves

    def rook_moves(self, pos):
        possible_moves = []
        a = pos[0]
        b = pos[1]
        colors = ["w", "b"]
        piece_color = self.strboard[a][b][0]
        opposite_piece_color = colors[1 - colors.index(piece_color)]
        try:
            for i in range(1, 8):
                currentString = self.strboard[a][b + i] + " "
                if currentString[0] == opposite_piece_color:
                    possible_moves.append([a, b + i])
                    break
                elif currentString[0] == piece_color:
                    break
                else:
                    possible_moves.append([a, b + i])
        except IndexError:
            pass
        try:
            for i in range(1, 8):
                currentString = self.strboard[a + i][b] + " "
                if currentString[0] == opposite_piece_color:
                    possible_moves.append([a + i, b])
                    break
                elif currentString[0] == piece_color:
                    break
                else:
                    possible_moves.append([a + i, b])
        except IndexError:
            pass
        try:
            for i in range(1, 8):
                currentString = self.strboard[a - i][b] + " "
                if currentString[0] == opposite_piece_color and a - i >= 0:
                    possible_moves.append([a - i, b])
                    break
                elif currentString[0] == piece_color and a - i >= 0:
                    break
                elif a - 1 < 0:
                    break
                else:
                    possible_moves.append([a - i, b])
        except IndexError:
            pass
        try:
            for i in range(1, 8):
                currentString = self.strboard[a][b - i] + " "
                if currentString[0] == opposite_piece_color and b - i >= 0:
                    possible_moves.append([a, b - i])
                    break
                elif currentString[0] == piece_color:
                    break
                elif b - i < 0:
                    break
                else:
                    possible_moves.append([a, b - i])
        except IndexError:
            pass
        return possible_moves

    def queen_moves(self, pos):
        return self.bishop_moves(pos) + self.rook_moves(pos)
        # this works because a queen is basically a rook and a bishop on one square

    def king_moves(self, pos, castleKingside=False, castleQueenside=False):
        possible_moves = []
        a = pos[0]
        b = pos[1]
        piece_color = self.strboard[a][b][0]
        if castleKingside:
            possible_moves.append([a + 2, b])
        if castleQueenside:
            possible_moves.append([a - 2, b])
        for i in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                if not (i == 0 and x == 0) and a + i < 8 and b + x < 8 and (self.strboard[a + i][b + x] + " ")[
                    0] != piece_color and not (
                        a + i < 0 or b + x < 0):
                    possible_moves.append([a + i, b + x])
        return possible_moves

root = Tk()
chessFrame = ChessFrame()
chessFrame.pack()
root.mainloop()

'''
This is old code that I'm keeping here so that I can source from this.
class ChessGame(Frame):
    def chessCallback(self, event):
        ls = list(event.position)
        ls = list(position)
        a = int(ls[0])
        b = int(ls[1])
        x = self.strboard[a][b]
        if self.isPieceSelected == True:
            if self.board[a][b].cget('bg') == "red":
                self.strboard[a][b] = self.pieceSelected[0] + self.pieceSelected[1].upper() + self.pieceSelected[2:]
                self.strboard[int(self.pieceSelectedLocation[0])][int(self.pieceSelectedLocation[1])] = ""
                if self.turn % 2 == 1:
                    if self.wKingInCheck():
                        self.strboard[a][b] = self.archivedstrboard[a][b]
                        self.strboard[int(self.pieceSelectedLocation[0])][int(self.pieceSelectedLocation[1])] = \
                        self.pieceSelected[0] + self.pieceSelected[1].upper() + self.pieceSelected[2:]
                        self.isPieceSelected = False
                        self.pieceSelected = None
                        for i in self.board:
                            for j in i:
                                j.config(bg="antique white")
                    else:
                        if self.pieceSelected=="wPawn" and self.pieceSelectedLocation[1]==1 and self.b==3:
                            self.enPassant=str(a)+str(b)
                            self.enPassantColor="w"
                        exec("self.board[a][b].config(image=self." + self.pieceSelected + ")")
                        self.board[int(self.pieceSelectedLocation[0])][int(self.pieceSelectedLocation[1])].config(
                            image=self.blanksquare, height=60, width=60)
                        self.archivedstrboard = self.strboard
                        if self.pieceSelected == "wking":
                            if a == 6 and self.wCastleKingside:
                                self.strboard[5][0] = "wRook"
                                self.strboard[7][0] = ""
                                self.board[5][0].config(image=self.wrook)
                                self.board[7][0].config(image=self.blanksquare, width=60, height=60)
                                self.wCastleQueenside = False
                                self.wCastleKingside = False
                            elif a == 2 and self.wCastleQueenside:
                                self.strboard[3][0] = "wRook"
                                self.strboard[0][0] = ""
                                self.board[3][0].config(image=self.wrook)
                                self.board[0][0].config(image=self.blanksquare, width=60, height=60)
                                self.wCastleQueenside = False
                                self.wCastleKingside = False
                        elif self.pieceSelected == "wrook" and self.pieceSelectedLocation[0] == 7 and \
                                        self.pieceSelectedLocation[1] == 0 and self.wCastleKingside == True:
                            self.wCastleKingside = False
                        elif self.pieceSelected == "wrook" and self.pieceSelectedLocation[0] == 0 and \
                                        self.pieceSelectedLocation[1] == 0 and self.wCastleQueenside == True:
                            self.wCastleQueenside = False
                        if self.pieceSelected == "wpawn" and b == 7:
                            self.wPawnPromotion(a, b)
                        elif self.pieceSelected == "bpawn" and b == 0:
                            self.bPawnPromotion(a, b)
                        else:
                            for i in self.board:
                                for j in i:
                                    j.config(bg="antique white")
                            self.isPieceSelected = False
                            self.pieceSelected = None
                            self.turnOver = True
                            self.turn += 1
                            self.do_move(self.root)
                elif self.turn % 2 == 0:
                    if self.bKingInCheck():
                        self.strboard[a][b] = self.archivedstrboard[a][b]
                        self.strboard[int(self.pieceSelectedLocation[0])][int(self.pieceSelectedLocation[1])] = \
                        self.pieceSelected[0] + self.pieceSelected[1].upper() + self.pieceSelected[2:]
                        self.isPieceSelected = False
                        self.pieceSelected = None
                        for i in self.board:
                            for j in i:
                                j.config(bg="antique white")
                    else:
                        if self.pieceSelected=="bPawn" and self.pieceSelectedLocation[1]==1 and self.b==3:
                            self.enPassant=str(a)+str(b)
                            self.enPassantColor="b"
                        exec("self.board[a][b].config(image=self." + self.pieceSelected + ")")
                        self.board[int(self.pieceSelectedLocation[0])][int(self.pieceSelectedLocation[1])].config(
                            image=self.blanksquare, height=60, width=60)
                        self.archivedstrboard = self.strboard
                        if self.pieceSelected == "wking":
                            self.CastleQueenside = False
                            self.CastleKingside = False
                        elif self.pieceSelected == "bking":
                            if a == 6 and self.bCastleKingside:
                                self.strboard[5][7] = "bRook"
                                self.strboard[7][7] = ""
                                self.board[5][7].config(image=self.brook)
                                self.board[7][7].config(image=self.blanksquare, width=60, height=60)
                                self.bCastleQueenside = False
                                self.bCastleKingside = False
                            elif a == 2 and self.bCastleQueenside:
                                self.strboard[3][7] = "bRook"
                                self.strboard[0][7] = ""
                                self.board[3][7].config(image=self.brook)
                                self.board[0][7].config(image=self.blanksquare, width=60, height=60)
                                self.bCastleQueenside = False
                                self.bCastleKingside = False
                        elif self.pieceSelected == "brook" and self.pieceSelectedLocation[0] == 7 and \
                                        self.pieceSelectedLocation[1] == 7 and self.bCastleKingside == True:
                            self.wCastleKingside = False
                        elif self.pieceSelected == "brook" and self.pieceSelectedLocation[0] == 0 and \
                                        self.pieceSelectedLocation[1] == 7 and self.bCastleQueenside == True:
                            self.wCastleQueenside = False
                        if self.pieceSelected == "wpawn" and b == 7:
                            self.wPawnPromotion(a, b)
                        elif self.pieceSelected == "bpawn" and b == 0:
                            self.bPawnPromotion(a, b)
                        else:
                            for i in self.board:
                                for j in i:
                                    j.config(bg="antique white")
                            self.isPieceSelected = False
                            self.pieceSelected = None
                            self.turnOver = True
                            self.turn += 1
                            self.do_move(root)
            elif self.noMoves():
                self.isPieceSelected = False
                self.pieceSelected = None
                self.turnOver = False
        elif x == "wPawn" and self.turn % 2 == 1:
            if b == 1:
                try:
                    if "b" in self.strboard[a][b + 1] or "w" in self.strboard[a][b + 1]:
                        pass
                    elif "b" in self.strboard[a][b + 2] or "w" in self.strboard[a][b + 2]:
                        self.board[a][b + 1].config(bg="red")
                    else:
                        self.board[a][b + 1].config(bg="red")
                        self.board[a][b + 2].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "b" in self.strboard[a + 1][b + 1] and "b" in self.strboard[a - 1][b + 1] and a - 1 >= 0:
                        self.board[a + 1][b + 1].config(bg="red")
                        self.board[a - 1][b + 1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "b" in self.strboard[a + 1][b + 1]:
                        self.board[a + 1][b + 1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "b" in self.strboard[a - 1][b + 1] and a - 1 >= 0:
                        self.board[a - 1][b + 1].config(bg="red")
                except (TypeError, IndexError):
                    pass
            else:
                if "b" in self.strboard[a][b + 1] or "w" in self.strboard[a][b + 1]:
                    pass
                else:
                    self.board[a][b + 1].config(bg="red")
                try:
                    if "b" in self.strboard[a + 1][b + 1] and "b" in self.strboard[a - 1][b + 1]:
                        self.board[a + 1][b + 1].config(bg="red")
                        self.board[a - 1][b + 1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "b" in self.strboard[a + 1][b + 1]:
                        self.board[a + 1][b + 1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "b" in self.strboard[a - 1][b + 1]:
                        self.board[a - 1][b + 1].config(bg="red")
                except (TypeError, IndexError):
                    pass
            self.isPieceSelected = True
            self.pieceSelected = "wpawn"
            self.pieceSelectedLocation = ls
        elif x == "bPawn" and self.turn % 2 == 0:
            if b == 6:
                try:
                    if "w" in self.strboard[a][b - 1] or "b" in self.strboard[a][b - 1]:
                        pass
                    elif "w" in self.strboard[a][b - 2] or "b" in self.strboard[a][b - 2]:
                        self.board[a][b - 1].config(bg="red")
                    else:
                        self.board[a][b - 1].config(bg="red")
                        self.board[a][b - 2].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a - 1][b - 1] and "w" in self.strboard[a - 1][
                                b - 1] and a - 1 >= 0 and not (self.strboard[a + 1][b - 1] == "bPawn") and not (
                        self.strboard[a - 1][b - 1] == "bPawn"):
                        self.board[a + 1][b - 1].config(bg="red")
                        self.board[a - 1][b - 1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a + 1][b - 1] and not (self.strboard[a + 1][b - 1] == "bPawn"):
                        self.board[a + 1][b - 1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a - 1][b - 1] and a - 1 >= 0 and not (
                        self.strboard[a - 1][b - 1] == "bPawn"):
                        self.board[a - 1][b - 1].config(bg="red")
                except (TypeError, IndexError):
                    pass
            else:
                if "w" in self.strboard[a][b - 1] or "b" in self.strboard[a][b - 1]:
                    pass
                else:
                    self.board[a][b - 1].config(bg="red")
                try:
                    if "w" in self.strboard[a + 1][b - 1] and "w" in self.strboard[a - 1][
                                b - 1] and a - 1 > -0 and not (self.strboard[a + 1][b - 1] == "bPawn") and not (
                        self.strboard[a - 1][b - 1] == "bPawn"):
                        self.board[a + 1][b - 1].config(bg="red")
                        self.board[a - 1][b - 1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a + 1][b - 1] and not (self.strboard[a + 1][b - 1] == "bPawn"):
                        self.board[a + 1][b - 1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a - 1][b - 1] and not (
                        self.strboard[a - 1][b - 1] == "bPawn") and a - 1 >= 0:
                        self.board[a - 1][b - 1].config(bg="red")
                except (TypeError, IndexError):
                    pass
            self.isPieceSelected = True
            self.pieceSelected = "bpawn"
            self.pieceSelectedLocation = ls
        elif x == "wRook" and self.turn % 2 == 1:
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a][b + i] + " "
                    if currentString[0] == "b":
                        self.board[a][b + i].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    else:
                        self.board[a][b + i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a + i][b] + " "
                    if currentString[0] == "b":
                        self.board[a + i][b].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    else:
                        self.board[a + i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a - i][b] + " "
                    if currentString[0] == "b" and a - i >= 0:
                        self.board[a - i][b].config(bg="red")
                        break
                    elif currentString[0] == "w" and a - i >= 0:
                        break
                    elif a - 1 < 0:
                        break
                    else:
                        self.board[a - i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a][b - i] + " "
                    if currentString[0] == "b" and b - i >= 0:
                        self.board[a][b - i].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    elif b - i < 0:
                        break
                    else:
                        self.board[a][b - i].config(bg="red")
            except IndexError:
                pass
            self.isPieceSelected = True
            self.pieceSelected = "wrook"
            self.pieceSelectedLocation = ls
        elif x == "wQueen" and self.turn % 2 == 1:
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a + i][b - i] + " "
                    if currentString[0] == "b" and b - i >= 0:
                        self.board[a + i][b - i].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    elif b - i < 0:
                        break
                    else:
                        self.board[a + i][b - i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a - i][b - i] + " "
                    if currentString[0] == "b" and b - i >= 0 and a - i >= 0:
                        self.board[a - i][b - i].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    elif b - i < 0:
                        break
                    elif a - i < 0:
                        break
                    else:
                        self.board[a - i][b - i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a + i][b + i] + " "
                    if currentString[0] == "b":
                        self.board[a + i][b + i].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    else:
                        self.board[a + i][b + i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a - i][b + i] + " "
                    if currentString[0] == "b" and a - i >= 0:
                        self.board[a - i][b - i].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    elif a - i < 0:
                        break
                    else:
                        self.board[a - i][b + i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a][b + i] + " "
                    if currentString[0] == "b":
                        self.board[a][b + i].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    else:
                        self.board[a][b + i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a + i][b] + " "
                    if currentString[0] == "b":
                        self.board[a + i][b].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    else:
                        self.board[a + i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a - i][b] + " "
                    if currentString[0] == "b" and a - i >= 0:
                        self.board[a - i][b].config(bg="red")
                        break
                    elif currentString[0] == "w" and a - i >= 0:
                        break
                    elif a - 1 < 0:
                        break
                    else:
                        self.board[a - i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a][b - i] + " "
                    if currentString[0] == "b" and b - i >= 0:
                        self.board[a][b - i].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    elif b - i < 0:
                        break
                    else:
                        self.board[a][b - i].config(bg="red")
            except IndexError:
                pass
            self.isPieceSelected = True
            self.pieceSelected = "wqueen"
            self.pieceSelectedLocation = ls
        elif x == "bRook" and self.turn % 2 == 0:
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a][b + i] + " "
                    if currentString[0] == "w":
                        self.board[a][b + i].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    else:
                        self.board[a][b + i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a + i][b] + " "
                    if currentString[0] == "w":
                        self.board[a + i][b].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    else:
                        self.board[a + i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a - i][b] + " "
                    if currentString[0] == "w" and a - i >= 0:
                        self.board[a - i][b].config(bg="red")
                        break
                    elif currentString[0] == "b" and a - i >= 0:
                        break
                    elif a - i < 0:
                        break
                    else:
                        self.board[a - i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a][b - i] + " "
                    if currentString[0] == "w" and b - 1 >= 0:
                        self.board[a][b - i].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    elif b - i < 0:
                        break
                    else:
                        self.board[a][b - i].config(bg="red")
            except IndexError:
                pass
            self.isPieceSelected = True
            self.pieceSelected = "brook"
            self.pieceSelectedLocation = ls
        elif x == "bBishop" and self.turn % 2 == 0:
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a + i][b - i] + " "
                    if currentString[0] == "w" and b - i >= 0:
                        self.board[a + i][b - i].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    elif b - i < 0:
                        break
                    else:
                        self.board[a + i][b - i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a - i][b - i] + " "
                    if currentString[0] == "w" and b - i >= 0 and a - i >= 0:
                        self.board[a - i][b - i].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    elif b - i < 0:
                        break
                    elif a - i < 0:
                        break
                    else:
                        self.board[a - i][b - i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a + i][b + i] + " "
                    if currentString[0] == "w":
                        self.board[a + i][b + i].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    else:
                        self.board[a + i][b + i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a - i][b + i] + " "
                    if currentString[0] == "w" and a - i >= 0:
                        self.board[a - i][b - i].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    elif a - i < 0:
                        break
                    else:
                        self.board[a - i][b + i].config(bg="red")
            except IndexError:
                pass
            self.isPieceSelected = True
            self.pieceSelected = "bbishop"
            self.pieceSelectedLocation = ls
        elif x == "bQueen" and self.turn % 2  == 0:
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a][b + i] + " "
                    if currentString[0] == "w":
                        self.board[a][b + i].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    else:
                        self.board[a][b + i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a + i][b] + " "
                    if currentString[0] == "w":
                        self.board[a + i][b].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    else:
                        self.board[a + i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a - i][b] + " "
                    if currentString[0] == "w" and a - i >= 0:
                        self.board[a - i][b].config(bg="red")
                        break
                    elif currentString[0] == "b" and a - i >= 0:
                        break
                    elif a - i < 0:
                        break
                    else:
                        self.board[a - i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a][b - i] + " "
                    if currentString[0] == "w" and b - 1 >= 0:
                        self.board[a][b - i].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    elif b - i < 0:
                        break
                    else:
                        self.board[a][b - i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a + i][b - i] + " "
                    if currentString[0] == "w" and b - i >= 0:
                        self.board[a + i][b - i].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    elif b - i < 0:
                        break
                    else:
                        self.board[a + i][b - i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a - i][b - i] + " "
                    if currentString[0] == "w" and b - i >= 0 and a - i >= 0:
                        self.board[a - i][b - i].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    elif b - i < 0:
                        break
                    elif a - i < 0:
                        break
                    else:
                        self.board[a - i][b - i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a + i][b + i] + " "
                    if currentString[0] == "w":
                        self.board[a + i][b + i].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    else:
                        self.board[a + i][b + i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a - i][b + i] + " "
                    if currentString[0] == "w" and a - i >= 0:
                        self.board[a - i][b - i].config(bg="red")
                        break
                    elif currentString[0] == "b":
                        break
                    elif a - i < 0:
                        break
                    else:
                        self.board[a - i][b + i].config(bg="red")
            except IndexError:
                pass
            self.isPieceSelected = True
            self.pieceSelected = "bqueen"
            self.pieceSelectedLocation = ls
        elif x == "wBishop" and self.turn % 2 == 1:
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a + i][b - i] + " "
                    if currentString[0] == "b" and b - i >= 0:
                        self.board[a + i][b - i].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    elif b - i < 0:
                        break
                    else:
                        self.board[a + i][b - i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a - i][b - i] + " "
                    if currentString[0] == "b" and b - i >= 0 and a - i >= 0:
                        self.board[a - i][b - i].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    elif b - i < 0:
                        break
                    elif a - i < 0:
                        break
                    else:
                        self.board[a - i][b - i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a + i][b + i] + " "
                    if currentString[0] == "b":
                        self.board[a + i][b + i].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    else:
                        self.board[a + i][b + i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1, 8):
                    currentString = self.strboard[a - i][b + i] + " "
                    if currentString[0] == "b" and a - i >= 0:
                        self.board[a - i][b - i].config(bg="red")
                        break
                    elif currentString[0] == "w":
                        break
                    elif a - i < 0:
                        break
                    else:
                        self.board[a - i][b + i].config(bg="red")
            except IndexError:
                pass
            self.isPieceSelected = True
            self.pieceSelected = "wbishop"
            self.pieceSelectedLocation = ls
        elif x == "wKnight" and self.turn % 2 == 1:
            for i in [2, 1, -2, -1]:
                for x in [2, 1, -2, -1]:
                    if abs(i) != abs(x):
                        try:
                            if (self.strboard[a + i][b + x] + " ")[0] == "b" and a + i >= 0 and b + x >= 0:
                                self.board[a + i][b + x].config(bg="red")
                            elif (self.strboard[a + i][b + x] + " ")[0] == "w":
                                pass
                            elif a + i < 0:
                                pass
                            elif b + x < 0:
                                pass
                            else:
                                self.board[a + i][b + x].config(bg="red")
                        except IndexError:
                            pass
            self.isPieceSelected = True
            self.pieceSelected = "wknight"
            self.pieceSelectedLocation = ls
        elif x == "bKnight" and self.turn % 2 == 0:
            for i in [2, 1, -2, -1]:
                for x in [2, 1, -2, -1]:
                    if abs(i) != abs(x):
                        try:
                            if (self.strboard[a + i][b + x] + " ")[0] == "w" and a + i >= 0 and b + x >= 0:
                                self.board[a + i][b + x].config(bg="red")
                            elif (self.strboard[a + i][b + x] + " ")[0] == "b":
                                pass
                            elif a + i < 0:
                                pass
                            elif b + x < 0:
                                pass
                            else:
                                self.board[a + i][b + x].config(bg="red")
                        except IndexError:
                            pass
            self.isPieceSelected = True
            self.pieceSelected = "bknight"
            self.pieceSelectedLocation = ls
        elif x == "wKing" and self.turn % 2 == 1:
            for i in [1, -1, 0]:
                for x in [1, -1, 0]:
                    if i != 0 or x != 0:
                        try:
                            currentString = self.strboard[a + i][b + x] + " "
                            if currentString[0] == "b" and a + i >= 0 and b + x >= 0:
                                self.board[a + i][b + x].config(bg="red")
                            elif currentString[0] == "w":
                                pass
                            elif a + i < 0:
                                pass
                            elif b + x < 0:
                                pass
                            else:
                                self.board[a + i][b + x].config(bg="red")
                        except IndexError:
                            pass
            if self.wCastleKingside and self.strboard[5][0] == "" and self.strboard[6][0] == "":
                self.board[6][0].config(bg="red")
            if self.wCastleQueenside and self.strboard[2][0] == "" and self.strboard[3][0] == "" and self.strboard[1][
                0] == "":
                self.board[2][0].config(bg="red")
            self.isPieceSelected = True
            self.pieceSelected = "wking"
            self.pieceSelectedLocation = ls
        elif x == "bKing" and self.turn % 2 == 0:
            for i in [1, -1, 0]:
                for x in [1, -1, 0]:
                    if i != 0 or x != 0:
                        try:
                            currentString = self.strboard[a + i][b + x] + " "
                            if currentString[0] == "w" and a + i >= 0 and b + x >= 0:
                                self.board[a + i][b + x].config(bg="red")
                            elif currentString[0] == "b":
                                pass
                            elif a + i < 0:
                                pass
                            elif b + x < 0:
                                pass
                            else:
                                self.board[a + i][b + x].config(bg="red")
                        except IndexError:
                            pass
            if self.bCastleKingside and self.strboard[5][7] == "" and self.strboard[6][7] == "":
                self.board[6][7].config(bg="red")
            if self.bCastleQueenside and self.strboard[2][7] == "" and self.strboard[3][7] == "" and self.strboard[1][
                0] == "":
                self.board[2][7].config(bg="red")
            self.isPieceSelected = True
            self.pieceSelected = "bking"
            self.pieceSelectedLocation = ls
        else:
            pass
    def __init__(self, root):
        Frame.__init__(root)
        self.wpawn = PhotoImage(file="w_pawn.gif")
        self.wrook = PhotoImage(file="w_rook.gif")
        self.wbishop = PhotoImage(file="w_bishop.gif")
        self.wknight = PhotoImage(file="w_knight.gif")
        self.wking = PhotoImage(file="w_king.gif")
        self.wqueen = PhotoImage(file="w_queen.gif")
        self.root = root
        self.winMessage = Label(root)
        self.bpawn = PhotoImage(file="b_pawn.gif")
        self.brook = PhotoImage(file="b_rook.gif")
        self.bbishop = PhotoImage(file="b_bishop.gif")
        self.bknight = PhotoImage(file="b_knight.gif")
        self.bking = PhotoImage(file="b_king.gif")
        self.bqueen = PhotoImage(file="b_queen.gif")
        self.blanksquare = PhotoImage()
        self.board = [[None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None]]
        self.strboard = [["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""],
                         ["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""]]
        for i in range(8):
            for x in range(8):
                self.board[i][x] = Button(root)
                self.board[i][x].config(image=self.blanksquare, height=60, width=60)
                self.board[i][x] = ChessPiece(self, "", self.blanksquare, [i, x])
        for i in range(8):
            self.board[i][1] = Button(root)
            self.board[i][1].config(image=self.wpawn, command=self.generic_button_click)
            self.strboard[i][1] = "wPawn"
        for i in [0, 7]:
            for x in [0]:
                self.board[i][x] = Button(root)
                self.board[i][x].config(image=self.wrook)
                self.strboard[i][x] = "wRook"
        for i in [1, 6]:
            for x in [0]:
                self.board[i][x] = Button(root)
                self.board[i][x].config(image=self.wknight)
                self.strboard[i][x] = "wKnight"
        for i in [2, 5]:
            for x in [0]:
                self.board[i][x] = Button(root)
                self.board[i][x].config(image=self.wbishop)
                self.strboard[i][x] = "wBishop"
        self.board[3][0] = Button(root)
        self.board[3][0].config(image=self.wqueen)
        self.strboard[3][0] = "wQueen"
        self.board[4][0] = Button(root)
        self.board[4][0].config(image=self.wking)
        self.strboard[4][0] = "wKing"
        for i in range(8):
            self.board[i][6] = Button(root)
            self.board[i][6].config(image=self.bpawn)
            self.strboard[i][6] = "bPawn"
        for i in [0, 7]:
            for x in [7]:
                self.board[i][x] = Button(root)
                self.board[i][x].config(image=self.brook)
                self.strboard[i][x] = "bRook"
        for i in [1, 6]:
            for x in [7]:
                self.board[i][x] = Button(root)
                self.board[i][x].config(image=self.bknight)
                self.strboard[i][x] = "bKnight"
        for i in [2, 5]:
            for x in [7]:
                self.board[i][x] = Button(root)
                self.board[i][x].config(image=self.bbishop)
                self.strboard[i][x] = "bBishop"
        self.board[3][7] = Button(root)
        self.board[3][7].config(image=self.bqueen)
        self.strboard[3][7] = "bQueen"
        self.board[4][7] = Button(root)
        self.board[4][7].config(image=self.bking)
        self.strboard[4][7] = "bKing"
        self.archivedstrboard = self.strboard
        self.turn = 1
        self.isPieceSelected = False
        self.pieceSelected = None
        self.notGameOver = True
        self.turnOver = False
        self.pieceSelectedLocation = None
        self.wCastleKingside = True
        self.wCastleQueenside = True
        self.bCastleKingside = True
        self.bCastleQueenside = True
        self.enPassant = None
        self.enPassantColor = None
        for i in self.board:
            for j in i:
                j.config(bg="antique white")
                #        while self.notGameOver:
        self.do_move(root)
    def noMoves(self):
        for i in range(8):
            for x in range(8):
                if self.board[i][x].cget('bg') == "red":
                    return False
        return True
    def bPawnKnight(self):
        self.board[self.a][self.b].config(image=self.bknight)
        self.strboard[self.a][self.b] = "bKnight"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="antique white")
        self.isPieceSelected = False
        self.pieceSelected = None
        self.turnOver = True
        self.turn += 1
        self.do_move(root)
    def bPawnBishop(self):
        self.board[self.a][self.b].config(image=self.bbishop)
        self.strboard[self.a][self.b] = "bBishop"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="antique white")
        self.isPieceSelected = False
        self.pieceSelected = None
        self.turnOver = True
        self.turn += 1
        self.do_move(root)
    def bPawnQueen(self):
        self.board[self.a][self.b].config(image=self.bqueen)
        self.strboard[self.a][self.b] = "bQueen"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="antique white")
        self.isPieceSelected = False
        self.pieceSelected = None
        self.turnOver = True
        self.turn += 1
        self.do_move(root)
    def bPawnRook(self):
        self.board[self.a][self.b].config(image=self.brook)
        self.strboard[self.a][self.b] = "bRook"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="antique white")
        self.isPieceSelected = False
        self.pieceSelected = None
        self.turnOver = True
        self.turn += 1
        self.do_move(root)
    def wPawnKnight(self):
        self.board[self.a][self.b].config(image=self.wknight)
        self.strboard[self.a][self.b] = "wKnight"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="antique white")
        self.isPieceSelected = False
        self.pieceSelected = None
        self.turnOver = True
        self.turn += 1
        self.do_move(root)
    def wPawnBishop(self):
        self.board[self.a][self.b].config(image=self.wbishop)
        self.strboard[self.a][self.b] = "wBishop"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="antique white")
        self.isPieceSelected = False
        self.pieceSelected = None
        self.turnOver = True
        self.turn += 1
        self.do_move(root)
    def wPawnQueen(self):
        self.board[self.a][self.b].config(image=self.wqueen)
        self.strboard[self.a][self.b] = "wQueen"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="antique white")
        self.isPieceSelected = False
        self.pieceSelected = None
        self.turnOver = True
        self.turn += 1
        self.do_move(root)
    def wPawnRook(self):
        self.board[self.a][self.b].config(image=self.wrook)
        self.strboard[self.a][self.b] = "wRook"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="antique white")
        self.isPieceSelected = False
        self.pieceSelected = None
        self.turnOver = True
        self.turn += 1
        self.do_move(root)
    def wPawnPromotion(self, a, b):
        self.promotionWindow = Toplevel()
        self.promotionWindow.wm_title("Promotion")
        self.promotionGrid = []
        self.promotionGrid.append(Button(self.promotionWindow, image=self.wqueen, command=self.wPawnQueen))
        self.promotionGrid.append(Button(self.promotionWindow, image=self.wrook, command=self.wPawnRook))
        self.promotionGrid.append(Button(self.promotionWindow, image=self.wbishop, command=self.wPawnBishop))
        self.promotionGrid.append(Button(self.promotionWindow, image=self.wknight, command=self.wPawnKnight))
        self.a = a
        self.b = b
        for i in range(4):
            self.promotionGrid[i].grid(column=i, row=0)
    def bPawnPromotion(self, a, b):
        self.promotionWindow = Toplevel()
        self.promotionWindow.wm_title("Promotion")
        self.a = a
        self.b = b
        self.promotionGrid = []
        self.promotionGrid.append(Button(self.promotionWindow, image=self.bqueen, command=self.bPawnQueen))
        self.promotionGrid.append(Button(self.promotionWindow, image=self.brook, command=self.bPawnRook))
        self.promotionGrid.append(Button(self.promotionWindow, image=self.bbishop, command=self.bPawnBishop))
        self.promotionGrid.append(Button(self.promotionWindow, image=self.bknight, command=self.bPawnKnight))
        for i in range(4):
            self.promotionGrid[i].grid(column=i, row=0)
    def wKingInCheck(self):
        return False
    def bKingInCheck(self):
        return False
    def do_move(self, root):
        for i in range(8):
            for x in range(8):
                self.board[i][x].grid_forget()
        if self.turn % 2 == 1:
            if self.b_won(root):
                self.winMessage.config(text="Black Wins!!!")
                self.winMessage.pack()
            for i in range(8):
                for x in range(8):
                    self.board[i][x].grid(column=i, row=7 - x)
            for i in range(8):
                for x in range(8):
                    if i == 0:
                        exec("self.board[" + str(i) + "][" + str(
                            x) + "].config(command=lambda: generic_button_click('0'+str(" + str(x) + "),root))")
                    else:
                        exec("self.board[" + str(i) + "][" + str(
                            x) + "].config(command=lambda: generic_button_click(str(" + str(i) + str(x) + "),root))")
        elif self.turn % 2 == 0:
            if self.w_won(root):
                self.winMessage.config(text="White Wins!!!")
                self.winMessage.pack()
            for i in range(8):
                for x in range(8):
                    self.board[i][x].grid(column=7 - i, row=x)
    def b_won(self, root):
        for i in range(8):
            for x in range(8):
                if self.strboard[i][x] == "wKing":
                    return False
        return True
    def w_won(self, root):
        for i in range(8):
            for x in range(8):
                if self.strboard[i][x] == "bKing":
                    return False
        return True
root = Tk()
root.wm_title("Chess Game")
chess = ChessGame(root)
root.mainloop()
'''
