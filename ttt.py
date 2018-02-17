#!/usr/bin/env python3
import sys,os
import curses

def ttt(stdscr):

    key = 0

    first_player = True

    MAX_SIZE_X = 3
    MAX_SIZE_Y = 3

    board = [[' ' for x in range(MAX_SIZE_X)] for y in range(MAX_SIZE_Y)]

    board_pos_x = 0
    board_pos_y = 0

    screen_pos_x = 0
    screen_pos_y = 0

    board_row =" | | "
    board_division ="-+-+-"

    stdscr.clear()
    stdscr.refresh()

    #press 'q' to exit
    while (key != ord('q')):


        stdscr.clear()
        height, width = stdscr.getmaxyx()

        #manages input
        if key == curses.KEY_RIGHT:
            board_pos_x = board_pos_x + 1
        elif key == curses.KEY_LEFT:
            board_pos_x = board_pos_x - 1
        elif key == curses.KEY_DOWN:
            board_pos_y = board_pos_y + 1
        elif key == curses.KEY_UP:
            board_pos_y = board_pos_y - 1
        elif (key == ord(' ') and board[board_pos_x][board_pos_y] == ' '):
            if first_player:
                board[board_pos_x][board_pos_y] = 'X'
                first_player = False
            else:
                board[board_pos_x][board_pos_y] = 'O'
                first_player = True


        #clamps board_pos_x and board_pos_y
        board_pos_x = max(board_pos_x,0)
        board_pos_x = min(board_pos_x,MAX_SIZE_X-1)
        board_pos_y = max(board_pos_y,0)
        board_pos_y = min(board_pos_y,MAX_SIZE_Y-1)

        #build screen
        info_bar_1 = "Use arrow keys + space bar | Press q to quit"
        if first_player:
            info_bar_2 = "X player turn"
        else:
            info_bar_2 = "O player turn "

            #draw screen
        stdscr.addstr(6,1,info_bar_1)
        stdscr.addstr(7,1,info_bar_2)

        stdscr.addstr(0,0,board_row)
        stdscr.addstr(1,0,board_division)
        stdscr.addstr(2,0,board_row)
        stdscr.addstr(3,0,board_division)
        stdscr.addstr(4,0,board_row)

        stdscr.addstr(0,0,board[0][0])
        stdscr.addstr(0,2,board[1][0])
        stdscr.addstr(0,4,board[2][0])

        stdscr.addstr(2,0,board[0][1])
        stdscr.addstr(2,2,board[1][1])
        stdscr.addstr(2,4,board[2][1])

        stdscr.addstr(4,0,board[0][2])
        stdscr.addstr(4,2,board[1][2])
        stdscr.addstr(4,4,board[2][2])

        #moves cursor
        screen_pos_x = board_pos_x * 2
        screen_pos_y = board_pos_y * 2
        stdscr.move(screen_pos_y, screen_pos_x)

        #refresh screen
        stdscr.refresh()
        #gets input
        key = stdscr.getch()

def main():
    curses.wrapper(ttt)

if __name__ == "__main__":
    main()
