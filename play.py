import src.board as sb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1: # default setting
        game = sb.board(4) # default size is 4x4
    else:
        game = sb.board(int(sys.argv[1]))

    game.play()
