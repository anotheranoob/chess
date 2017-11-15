from tkinter import *
import time
import sys
def generic_button_click(position, root):
    chess.generic_button_click(position, root)
class Main:
    def noMoves(self):
        for i in range(8):
            for x in range(8):
                if self.board[i][x].cget('bg')=="red":
                    return False
        return True

    def bPawnKnight(self):
        self.board[self.a][self.b].config(image=self.bknight)
        self.strboard[self.a][self.b]="bKnight"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="burlywood3")
        self.isPieceSelected=False
        self.pieceSelected=None
        self.turnOver=True
        self.turn+=1
        self.do_move(root)

    def bPawnBishop(self):
        self.board[self.a][self.b].config(image=self.bbishop)
        self.strboard[self.a][self.b]="bBishop"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="burlywood3")
        self.isPieceSelected=False
        self.pieceSelected=None
        self.turnOver=True
        self.turn+=1
        self.do_move(root)

    def bPawnQueen(self):
        self.board[self.a][self.b].config(image=self.bqueen)
        self.strboard[self.a][self.b]="bQueen"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="burlywood3")
        self.isPieceSelected=False
        self.pieceSelected=None
        self.turnOver=True
        self.turn+=1
        self.do_move(root)

    def bPawnRook(self):
        self.board[self.a][self.b].config(image=self.brook)
        self.strboard[self.a][self.b]="bRook"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="burlywood3")
        self.isPieceSelected=False
        self.pieceSelected=None
        self.turnOver=True
        self.turn+=1
        self.do_move(root)

    def wPawnKnight(self):
        self.board[self.a][self.b].config(image=self.wknight)
        self.strboard[self.a][self.b]="wKnight"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="burlywood3")
        self.isPieceSelected=False
        self.pieceSelected=None
        self.turnOver=True
        self.turn+=1
        self.do_move(root)
        
    def wPawnBishop(self):
        self.board[self.a][self.b].config(image=self.wbishop)
        self.strboard[self.a][self.b]="wBishop"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="burlywood3")
        self.isPieceSelected=False
        self.pieceSelected=None
        self.turnOver=True
        self.turn+=1
        self.do_move(root)

    def wPawnQueen(self):
        self.board[self.a][self.b].config(image=self.wqueen)
        self.strboard[self.a][self.b]="wQueen"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="burlywood3")
        self.isPieceSelected=False
        self.pieceSelected=None
        self.turnOver=True
        self.turn+=1
        self.do_move(root)

    def wPawnRook(self):
        self.board[self.a][self.b].config(image=self.wrook)
        self.strboard[self.a][self.b]="wRook"
        self.promotionWindow.destroy()
        for i in self.board:
            for j in i:
                j.config(bg="burlywood3")
        self.isPieceSelected=False
        self.pieceSelected=None
        self.turnOver=True
        self.turn+=1
        self.do_move(root)

    def wPawnPromotion(self, a, b):
        self.promotionWindow=Toplevel()
        self.promotionWindow.wm_title("Promotion")
        self.promotionGrid=[]
        self.promotionGrid.append(Button(self.promotionWindow, image=self.wqueen, command=self.wPawnQueen))
        self.promotionGrid.append(Button(self.promotionWindow, image=self.wrook, command=self.wPawnRook))
        self.promotionGrid.append(Button(self.promotionWindow, image=self.wbishop, command=self.wPawnBishop))
        self.promotionGrid.append(Button(self.promotionWindow, image=self.wknight, command=self.wPawnKnight))
        self.a=a
        self.b=b
        for i in range(4):
            self.promotionGrid[i].grid(column=i, row=0)

    def bPawnPromotion(self, a, b):
        self.promotionWindow=Toplevel()
        self.promotionWindow.wm_title("Promotion")
        self.a=a
        self.b=b
        self.promotionGrid=[]
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

    def generic_button_click(self, position, root):
        ls=list(position)
        a=int(ls[0])
        b=int(ls[1])
        x=self.strboard[a][b]
        self.archivedstrboard=self.strboard
        if self.isPieceSelected==True:
            if self.board[a][b].cget('bg')=="red":
                self.strboard[a][b]=self.pieceSelected[0]+self.pieceSelected[1].upper()+self.pieceSelected[2:]
                self.strboard[int(self.pieceSelectedLocation[0])][int(self.pieceSelectedLocation[1])]=""
                if self.turn%2==1:
                    if self.wKingInCheck():
                        self.strboard[a][b]=self.archivedstrboard[a][b]
                        self.strboard[int(self.pieceSelectedLocation[0])][int(self.pieceSelectedLocation[1])]=self.pieceSelected[0]+self.pieceSelected[1].upper()+self.pieceSelected[2:]
                        self.isPieceSelected=False
                        self.pieceSelected=None
                        for i in self.board:
                            for j in i:
                                j.config(bg="burlywood3")
                    else:
                        if self.pieceSelected=="wpawn" and self.pieceSelectedLocation[1]=='1' and b==3:
                            self.enPassant=str(a)+str(b)
                            self.enPassantColor="w"
                        exec("self.board[a][b].config(image=self."+self.pieceSelected+")")
                        self.board[int(self.pieceSelectedLocation[0])][int(self.pieceSelectedLocation[1])].config(image=self.blanksquare, height=60, width=60)
                        self.archivedstrboard=self.strboard
                        if self.pieceSelected=="wking":
                            if a==6 and self.wCastleKingside:
                                self.strboard[5][0]="wRook"
                                self.strboard[7][0]=""
                                self.board[5][0].config(image=self.wrook)
                                self.board[7][0].config(image=self.blanksquare, width=60, height=60)
                                self.wCastleQueenside=False
                                self.wCastleKingside=False
                            elif a==2 and self.wCastleQueenside:
                                self.strboard[3][0]="wRook"
                                self.strboard[0][0]=""
                                self.board[3][0].config(image=self.wrook)
                                self.board[0][0].config(image=self.blanksquare, width=60, height=60)
                                self.wCastleQueenside=False
                                self.wCastleKingside=False
                        elif self.pieceSelected=="wrook" and self.pieceSelectedLocation[0]==7 and self.pieceSelectedLocation[1]==0 and self.wCastleKingside==True:
                            self.wCastleKingside=False
                        elif self.pieceSelected=="wrook" and self.pieceSelectedLocation[0]==0 and self.pieceSelectedLocation[1]==0 and self.wCastleQueenside==True:
                            self.wCastleQueenside=False
                        if self.pieceSelected=="wpawn" and b==7:
                            self.wPawnPromotion(a,b)
                        elif self.pieceSelected=="bpawn" and b==0:
                            self.bPawnPromotion(a,b)
                        else:
                            for i in self.board:
                                for j in i:
                                    j.config(bg="burlywood3")
                            self.isPieceSelected=False
                            self.pieceSelected=None
                            self.turnOver=True
                            self.turn+=1
                            self.do_move(root)
                elif self.turn%2 ==0:
                    if self.bKingInCheck():
                        self.strboard=self.archivedstrboard
                        self.isPieceSelected=False
                        self.pieceSelected=None
                        for i in self.board:
                            for j in i:
                                j.config(bg="burlywood3")
                    else:
                        if self.pieceSelected=="bpawn" and self.pieceSelectedLocation[1]=='6' and b==4:
                            self.enPassant=str(a)+str(b)
                            self.enPassantColor="b"
                        if self.pieceSelected=="bpawn" and self.pieceSelectedLocation[0]!=a and x=="":
                            self.board[a][b+1].config(image=self.blanksquare, width=60, height=60, bg="green")
                        print(a)
                        print(self.pieceSelectedLocation[0])
                        print(self.archivedstrboard[a][b])
                        print(self.strboard)
                        exec("self.board[a][b].config(image=self."+self.pieceSelected+")")
                        self.board[int(self.pieceSelectedLocation[0])][int(self.pieceSelectedLocation[1])].config(image=self.blanksquare, height=60, width=60)
                        self.archivedstrboard=self.strboard
                        if self.pieceSelected=="wking":
                            self.CastleQueenside=False
                            self.CastleKingside=False
                        elif self.pieceSelected=="bking":
                            if a==6 and self.bCastleKingside:
                                self.strboard[5][7]="bRook"
                                self.strboard[7][7]=""
                                self.board[5][7].config(image=self.brook)
                                self.board[7][7].config(image=self.blanksquare, width=60, height=60)
                                self.bCastleQueenside=False
                                self.bCastleKingside=False
                            elif a==2 and self.bCastleQueenside:
                                self.strboard[3][7]="bRook"
                                self.strboard[0][7]=""
                                self.board[3][7].config(image=self.brook)
                                self.board[0][7].config(image=self.blanksquare, width=60, height=60)
                                self.bCastleQueenside=False
                                self.bCastleKingside=False
                        elif self.pieceSelected=="brook" and self.pieceSelectedLocation[0]==7 and self.pieceSelectedLocation[1]==7 and self.bCastleKingside==True:
                            self.wCastleKingside=False
                        elif self.pieceSelected=="brook" and self.pieceSelectedLocation[0]==0 and self.pieceSelectedLocation[1]==7 and self.bCastleQueenside==True:
                            self.wCastleQueenside=False
                        if self.pieceSelected=="wpawn" and b==7:
                            self.wPawnPromotion(a,b)
                        elif self.pieceSelected=="bpawn" and b==0:
                            self.bPawnPromotion(a,b)
                        else:
                            for i in self.board:
                                for j in i:
                                    j.config(bg="burlywood3")
                            self.isPieceSelected=False
                            self.pieceSelected=None
                            self.turnOver=True
                            self.turn+=1
                            self.do_move(root)
            elif self.noMoves():
                self.isPieceSelected=False
                self.pieceSelected=None
                self.turnOver=False
        elif x=="wPawn" and self.turn%2==1 :
            if b==1:
                try:
                    if "b" in self.strboard[a][b+1] or "w" in self.strboard[a][b+1]:
                        pass
                    elif "b" in self.strboard[a][b+2] or "w" in self.strboard[a][b+2]:
                        self.board[a][b+1].config(bg="red")
                    else:
                        self.board[a][b+1].config(bg="red")
                        self.board[a][b+2].config(bg="red")
                except (TypeError, IndexError):
                    pass                
                try:
                    if "b" in self.strboard[a+1][b+1]:
                        self.board[a+1][b+1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "b" in self.strboard[a-1][b+1] and a-1>=0:
                        self.board[a-1][b+1].config(bg="red")
                except (TypeError, IndexError):
                    pass
            else:
                if "b" in self.strboard[a][b+1] or "w" in self.strboard[a][b+1]:
                    pass
                else:
                    self.board[a][b+1].config(bg="red")
                try:
                    if "b" in self.strboard[a+1][b+1]:
                        self.board[a+1][b+1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "b" in self.strboard[a-1][b+1]:
                        self.board[a-1][b+1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if self.enPassantColor=="b" and a+1==int(self.enPassant[0]) and b==int(self.enPassant[1]):
                        self.board[a+1][b+1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if self.enPassantColor=="b" and a-1==int(self.enPassant[0]) and b==int(self.enPassant[1]) and a-1>0:
                        self.board[a-1][b+1].config(bg="red")
                except (TypeError, IndexError):
                    pass
            self.isPieceSelected=True
            self.pieceSelected="wpawn"
            self.pieceSelectedLocation=ls
        elif x=="bPawn" and self.turn%2==0 :
            if b==6:
                try:
                    if "w" in self.strboard[a][b-1] or "b" in self.strboard[a][b-1]:
                        pass
                    elif "w" in self.strboard[a][b-2] or "b" in self.strboard[a][b-2]:
                        self.board[a][b-1].config(bg="red")
                    else:
                        self.board[a][b-1].config(bg="red")
                        self.board[a][b-2].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a+1][b-1] and not(self.strboard[a+1][b-1]=="bPawn"):
                        self.board[a+1][b-1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a-1][b-1] and a-1>=0 and not(self.strboard[a-1][b-1]=="bPawn"):
                        self.board[a-1][b-1].config(bg="red")
                except (TypeError, IndexError):
                    pass
            else:
                if "w" in self.strboard[a][b-1] or "b" in self.strboard[a][b-1]:
                    pass
                else:
                    self.board[a][b-1].config(bg="red")
                try:
                    if "w" in self.strboard[a+1][b-1] and "w" in self.strboard[a-1][b-1] and a-1>-0 and not(self.strboard[a+1][b-1]=="bPawn") and not(self.strboard[a-1][b-1]=="bPawn"):
                        self.board[a+1][b-1].config(bg="red")
                        self.board[a-1][b-1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a+1][b-1] and not(self.strboard[a+1][b-1]=="bPawn"):
                        self.board[a+1][b-1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if "w" in self.strboard[a-1][b-1] and not(self.strboard[a-1][b-1]=="bPawn") and a-1>=0:
                        self.board[a-1][b-1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if self.enPassantColor=="w" and a+1==int(self.enPassant[0]) and b==int(self.enPassant[1]):
                        self.board[a+1][b-1].config(bg="red")
                except (TypeError, IndexError):
                    pass
                try:
                    if self.enPassantColor=="w" and a-1==int(self.enPassant[0]) and b==int(self.enPassant[1]) and a-1>0:
                        self.board[a-1][b-1].config(bg="red")
                except (TypeError, IndexError):
                    pass
            self.isPieceSelected=True
            self.pieceSelected="bpawn"
            self.pieceSelectedLocation=ls
        elif x=="wRook" and self.turn%2==1:
            try:
                for i in range(1,8):
                    currentString=self.strboard[a][b+i]+" "
                    if currentString[0]=="b":
                        self.board[a][b+i].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    else:
                        self.board[a][b+i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a+i][b]+" "
                    if currentString[0]=="b":
                        self.board[a+i][b].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    else:
                        self.board[a+i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a-i][b]+" "
                    if currentString[0]=="b" and a-i>=0:
                        self.board[a-i][b].config(bg="red")
                        break
                    elif currentString[0]=="w" and a-i>=0:
                        break
                    elif a-1<0:
                        break
                    else:
                        self.board[a-i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a][b-i]+" "
                    if currentString[0]=="b" and b-i>=0:
                        self.board[a][b-i].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    elif b-i<0:
                        break
                    else:
                        self.board[a][b-i].config(bg="red")
            except IndexError:
                pass
            self.isPieceSelected=True
            self.pieceSelected="wrook"
            self.pieceSelectedLocation=ls
        elif x=="wQueen" and self.turn%2==1:
            try:
                for i in range(1,8):
                    currentString=self.strboard[a+i][b-i]+" "
                    if currentString[0]=="b" and b-i>=0:
                        self.board[a+i][b-i].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    elif b-i<0:
                        break
                    else:
                        self.board[a+i][b-i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a-i][b-i]+" "
                    if currentString[0]=="b" and b-i>=0 and a-i>=0:
                        self.board[a-i][b-i].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    elif b-i<0:
                        break
                    elif a-i<0:
                        break
                    else:
                        self.board[a-i][b-i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a+i][b+i]+" "
                    if currentString[0]=="b":
                        self.board[a+i][b+i].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    else:
                        self.board[a+i][b+i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a-i][b+i]+" "
                    if currentString[0]=="b" and a-i>=0:
                        self.board[a-i][b-i].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    elif a-i<0:
                        break
                    else:
                        self.board[a-i][b+i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a][b+i]+" "
                    if currentString[0]=="b":
                        self.board[a][b+i].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    else:
                        self.board[a][b+i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a+i][b]+" "
                    if currentString[0]=="b":
                        self.board[a+i][b].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    else:
                        self.board[a+i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a-i][b]+" "
                    if currentString[0]=="b" and a-i>=0:
                        self.board[a-i][b].config(bg="red")
                        break
                    elif currentString[0]=="w" and a-i>=0:
                        break
                    elif a-1<0:
                        break
                    else:
                        self.board[a-i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a][b-i]+" "
                    if currentString[0]=="b" and b-i>=0:
                        self.board[a][b-i].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    elif b-i<0:
                        break
                    else:
                        self.board[a][b-i].config(bg="red")
            except IndexError:
                pass
            self.isPieceSelected=True
            self.pieceSelected="wqueen"
            self.pieceSelectedLocation=ls


        elif x=="bRook" and self.turn%2==0:
            try:
                for i in range(1,8):
                    currentString=self.strboard[a][b+i]+" "
                    if currentString[0]=="w":
                        self.board[a][b+i].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    else:
                        self.board[a][b+i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a+i][b]+" "
                    if currentString[0]=="w":
                        self.board[a+i][b].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    else:
                        self.board[a+i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a-i][b]+" "
                    if currentString[0]=="w" and a-i>=0:
                        self.board[a-i][b].config(bg="red")
                        break
                    elif currentString[0]=="b" and a-i>=0:
                        break
                    elif a-i<0:
                        break
                    else:
                        self.board[a-i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a][b-i]+" "
                    if currentString[0]=="w" and b-1>=0:
                        self.board[a][b-i].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    elif b-i<0:
                        break
                    else:
                        self.board[a][b-i].config(bg="red")
            except IndexError:
                pass
            self.isPieceSelected=True
            self.pieceSelected="brook"
            self.pieceSelectedLocation=ls
        elif x=="bBishop" and self.turn%2==0:
            try:
                for i in range(1,8):
                    currentString=self.strboard[a+i][b-i]+" "
                    if currentString[0]=="w" and b-i>=0:
                        self.board[a+i][b-i].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    elif b-i<0:
                        break
                    else:
                        self.board[a+i][b-i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a-i][b-i]+" "
                    if currentString[0]=="w" and b-i>=0 and a-i>=0:
                        self.board[a-i][b-i].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    elif b-i<0:
                        break
                    elif a-i<0:
                        break
                    else:
                        self.board[a-i][b-i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a+i][b+i]+" "
                    if currentString[0]=="w":
                        self.board[a+i][b+i].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    else:
                        self.board[a+i][b+i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a-i][b+i]+" "
                    if currentString[0]=="w" and a-i>=0:
                        self.board[a-i][b-i].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    elif a-i<0:
                        break
                    else:
                        self.board[a-i][b+i].config(bg="red")
            except IndexError:
                pass
            self.isPieceSelected=True
            self.pieceSelected="bbishop"
            self.pieceSelectedLocation=ls
        elif x=="bQueen" and self.turn%2==0:
            try:
                for i in range(1,8):
                    currentString=self.strboard[a][b+i]+" "
                    if currentString[0]=="w":
                        self.board[a][b+i].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    else:
                        self.board[a][b+i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a+i][b]+" "
                    if currentString[0]=="w":
                        self.board[a+i][b].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    else:
                        self.board[a+i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a-i][b]+" "
                    if currentString[0]=="w" and a-i>=0:
                        self.board[a-i][b].config(bg="red")
                        break
                    elif currentString[0]=="b" and a-i>=0:
                        break
                    elif a-i<0:
                        break
                    else:
                        self.board[a-i][b].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a][b-i]+" "
                    if currentString[0]=="w" and b-1>=0:
                        self.board[a][b-i].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    elif b-i<0:
                        break
                    else:
                        self.board[a][b-i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a+i][b-i]+" "
                    if currentString[0]=="w" and b-i>=0:
                        self.board[a+i][b-i].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    elif b-i<0:
                        break
                    else:
                        self.board[a+i][b-i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a-i][b-i]+" "
                    if currentString[0]=="w" and b-i>=0 and a-i>=0:
                        self.board[a-i][b-i].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    elif b-i<0:
                        break
                    elif a-i<0:
                        break
                    else:
                        self.board[a-i][b-i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a+i][b+i]+" "
                    if currentString[0]=="w":
                        self.board[a+i][b+i].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    else:
                        self.board[a+i][b+i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a-i][b+i]+" "
                    if currentString[0]=="w" and a-i>=0:
                        self.board[a-i][b-i].config(bg="red")
                        break
                    elif currentString[0]=="b":
                        break
                    elif a-i<0:
                        break
                    else:
                        self.board[a-i][b+i].config(bg="red")
            except IndexError:
                pass
            self.isPieceSelected=True
            self.pieceSelected="bqueen"
            self.pieceSelectedLocation=ls

        elif x=="wBishop" and self.turn%2==1:
            try:
                for i in range(1,8):
                    currentString=self.strboard[a+i][b-i]+" "
                    if currentString[0]=="b" and b-i>=0:
                        self.board[a+i][b-i].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    elif b-i<0:
                        break
                    else:
                        self.board[a+i][b-i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a-i][b-i]+" "
                    if currentString[0]=="b" and b-i>=0 and a-i>=0:
                        self.board[a-i][b-i].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    elif b-i<0:
                        break
                    elif a-i<0:
                        break
                    else:
                        self.board[a-i][b-i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a+i][b+i]+" "
                    if currentString[0]=="b":
                        self.board[a+i][b+i].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    else:
                        self.board[a+i][b+i].config(bg="red")
            except IndexError:
                pass
            try:
                for i in range(1,8):
                    currentString=self.strboard[a-i][b+i]+" "
                    if currentString[0]=="b" and a-i>=0:
                        self.board[a-i][b-i].config(bg="red")
                        break
                    elif currentString[0]=="w":
                        break
                    elif a-i<0:
                        break
                    else:
                        self.board[a-i][b+i].config(bg="red")
            except IndexError:
                pass
            self.isPieceSelected=True
            self.pieceSelected="wbishop"
            self.pieceSelectedLocation=ls
        elif x=="wKnight" and self.turn%2==1:
            for i in [2,1,-2,-1]:
                for x in [2,1,-2,-1]:
                    if abs(i)!=abs(x):
                        try:                            
                            if (self.strboard[a+i][b+x]+" ")[0]=="b" and a+i>=0 and b+x>=0:
                                self.board[a+i][b+x].config(bg="red")
                            elif (self.strboard[a+i][b+x]+" ")[0]=="w":
                                pass
                            elif a+i<0:
                                pass
                            elif b+x<0:
                                pass
                            else:
                                self.board[a+i][b+x].config(bg="red")
                        except IndexError:
                            pass                            
            self.isPieceSelected=True
            self.pieceSelected="wknight"
            self.pieceSelectedLocation=ls

        elif x=="bKnight" and self.turn%2==0:
            for i in [2,1,-2,-1]:
                for x in [2,1,-2,-1]:
                    if abs(i)!=abs(x):
                        try:                            
                            if (self.strboard[a+i][b+x]+" ")[0]=="w" and a+i>=0 and b+x>=0:
                                self.board[a+i][b+x].config(bg="red")
                            elif (self.strboard[a+i][b+x]+" ")[0]=="b":
                                pass
                            elif a+i<0:
                                pass
                            elif b+x<0:
                                pass
                            else:
                                self.board[a+i][b+x].config(bg="red")
                        except IndexError:
                            pass                            
            self.isPieceSelected=True
            self.pieceSelected="bknight"
            self.pieceSelectedLocation=ls

        elif x=="wKing" and self.turn%2==1:
            for i in [1,-1,0]:
                for x in [1,-1,0]:
                    if i!=0 or x!=0:
                        try:
                            currentString=self.strboard[a+i][b+x]+" "
                            if currentString[0]=="b" and a+i>=0 and b+x>=0:
                                self.board[a+i][b+x].config(bg="red")
                            elif currentString[0]=="w":
                                pass
                            elif a+i<0:
                                pass
                            elif b+x<0:
                                pass
                            else:
                                self.board[a+i][b+x].config(bg="red")
                        except IndexError:
                            pass
            if self.wCastleKingside and self.strboard[5][0]=="" and self.strboard[6][0]=="":
                self.board[6][0].config(bg="red")
            if self.wCastleQueenside and self.strboard[2][0]=="" and self.strboard[3][0]=="" and self.strboard[1][0]=="":
                self.board[2][0].config(bg="red")
            self.isPieceSelected=True
            self.pieceSelected="wking"
            self.pieceSelectedLocation=ls

        elif x=="bKing" and self.turn%2==0:
            for i in [1,-1,0]:
                for x in [1,-1,0]:
                    if i!=0 or x!=0:
                        try:
                            currentString=self.strboard[a+i][b+x]+" "
                            if currentString[0]=="w" and a+i>=0 and b+x>=0:
                                self.board[a+i][b+x].config(bg="red")
                            elif currentString[0]=="b":
                                pass
                            elif a+i<0:
                                pass
                            elif b+x<0:
                                pass
                            else:
                                self.board[a+i][b+x].config(bg="red")
                        except IndexError:
                            pass
            if self.bCastleKingside and self.strboard[5][7]=="" and self.strboard[6][7]=="":
                self.board[6][7].config(bg="red")
            if self.bCastleQueenside and self.strboard[2][7]=="" and self.strboard[3][7]=="" and self.strboard[1][0]=="":
                self.board[2][7].config(bg="red")
            self.isPieceSelected=True
            self.pieceSelected="bking"
            self.pieceSelectedLocation=ls

        else:
            pass
    def do_move(self, root):
        for i in range(8):
            for x in range(8):
                self.board[i][x].grid_forget()
        if self.turn%2==1:
            if self.b_won(root):
                self.winMessage.config(text="Black Wins!!!")
                self.winMessage.pack()
                sys.exit()
                time.sleep(3)
            for i in range(8):
                for x in range(8):
                    self.board[i][x].grid(column=i, row=7-x)
            for i in range(8):
                for x in range(8):
                    if i==0:
                        exec("self.board["+str(i)+"]["+str(x)+"].config(command=lambda: generic_button_click('0'+str("+str(x)+"),root))")
                    else:
                        exec("self.board["+str(i)+"]["+str(x)+"].config(command=lambda: generic_button_click(str("+str(i)+str(x)+"),root))")
        elif self.turn%2==0:
            if self.w_won(root):
                self.winMessage.config(text="White Wins!!!")
                self.winMessage.pack()
                sys.exit()
                time.sleep(3)
            for i in range(8):
                for x in range(8):
                    self.board[i][x].grid(column=7-i, row=x)

    def b_won(self,root):
        for i in range(8):
            for x in range(8):
                if self.strboard[i][x]=="wKing":
                    return False
        return True
    
    def w_won(self,root):
        for i in range(8):
            for x in range(8):
                if self.strboard[i][x]=="bKing":
                    return False
        return True
    def __init__(self, root):
        self.wpawn=PhotoImage(file="w_pawn.gif")
        self.wrook=PhotoImage(file="w_rook.gif")
        self.wbishop=PhotoImage(file="w_bishop.gif")
        self.wknight=PhotoImage(file="w_knight.gif")
        self.wking=PhotoImage(file="w_king.gif")
        self.wqueen=PhotoImage(file="w_queen.gif")

        self.winMessage=Label(root)
        
        self.bpawn=PhotoImage(file="b_pawn.gif")
        self.brook=PhotoImage(file="b_rook.gif")
        self.bbishop=PhotoImage(file="b_bishop.gif")
        self.bknight=PhotoImage(file="b_knight.gif")
        self.bking=PhotoImage(file="b_king.gif")
        self.bqueen=PhotoImage(file="b_queen.gif")
        self.blanksquare=PhotoImage()
        self.board=[[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None]]
        self.strboard=[["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""]]
        for i in range(8):
            for x in range(8):
                self.board[i][x]=Button(root)
                self.board[i][x].config(image=self.blanksquare, height=60, width=60)
        for i in range(8):
            self.board[i][1]=Button(root)
            self.board[i][1].config(image=self.wpawn, command=lambda: self.generic_button_click())
            self.strboard[i][1]="wPawn"
        for i in [0,7]:
            for x in [0]:
                self.board[i][x]=Button(root)
                self.board[i][x].config(image=self.wrook)
                self.strboard[i][x]="wRook"
        for i in [1,6]:
            for x in [0]:
                self.board[i][x]=Button(root)
                self.board[i][x].config(image=self.wknight)
                self.strboard[i][x]="wKnight"
        for i in [2,5]:
            for x in [0]:
                self.board[i][x]=Button(root)
                self.board[i][x].config(image=self.wbishop)
                self.strboard[i][x]="wBishop"
        self.board[3][0]=Button(root)
        self.board[3][0].config(image=self.wqueen)
        self.strboard[3][0]="wQueen"
        self.board[4][0]=Button(root)
        self.board[4][0].config(image=self.wking)
        self.strboard[4][0]="wKing"
        for i in range(8):
            self.board[i][6]=Button(root)
            self.board[i][6].config(image=self.bpawn)
            self.strboard[i][6]="bPawn"
        for i in [0,7]:
            for x in [7]:
                self.board[i][x]=Button(root)
                self.board[i][x].config(image=self.brook)
                self.strboard[i][x]="bRook"
        for i in [1,6]:
            for x in [7]:
                self.board[i][x]=Button(root)
                self.board[i][x].config(image=self.bknight)
                self.strboard[i][x]="bKnight"
        for i in [2,5]:
            for x in [7]:
                self.board[i][x]=Button(root)
                self.board[i][x].config(image=self.bbishop)
                self.strboard[i][x]="bBishop"
        self.board[3][7]=Button(root)
        self.board[3][7].config(image=self.bqueen)
        self.strboard[3][7]="bQueen"
        self.board[4][7]=Button(root)
        self.board[4][7].config(image=self.bking)
        self.strboard[4][7]="bKing"
        self.archivedstrboard=self.strboard
        self.turn=1
        self.isPieceSelected=False
        self.pieceSelected=None
        self.notGameOver=True
        self.turnOver=False
        self.pieceSelectedLocation=None
        self.wCastleKingside=True
        self.wCastleQueenside=True
        self.bCastleKingside=True
        self.bCastleQueenside=True
        self.enPassant=None
        self.enPassantColor=None
        for i in self.board:
            for j in i:
                j.config(bg="burlywood3")
#        while self.notGameOver:
        self.do_move(root)
root=Tk()
root.wm_title("Chess Game")
chess=Main(root)
root.mainloop()
