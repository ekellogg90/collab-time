"""
Simple CLI Chess Game

* Board and pieces rendered in the command line
* Accepts input in chess notation (i.e. Rg3)
* If the move is illegal an informative message is printed
"""
import pytest

# Support variables
GRID_SIZE = 8
ALLOWED_MOVES = {
    "K": [(-1, 0), (1, 0), (0, -1), (0, 1)],
    "Q": [(0, i) for i in range(-(GRID_SIZE+1), GRID_SIZE) if i!=0] + # vertical moves
         [(i, 0) for i in range(-(GRID_SIZE+1), GRID_SIZE) if i!=0] + # horizontal moves
         [(i, i) for i in range(-(GRID_SIZE+1), GRID_SIZE) if i!=0] + # diagonal moves part 1
         [(-i, i) for i in range(-(GRID_SIZE+1), GRID_SIZE) if i!=0], # diagonal moves part 2
    "R": [(0, i) for i in range(-(GRID_SIZE+1), GRID_SIZE) if i!=0] + # vertical moves
         [(i, 0) for i in range(-(GRID_SIZE+1), GRID_SIZE) if i!=0], # horizontal moves
    "B": [(i, i) for i in range(-(GRID_SIZE+1), GRID_SIZE) if i!=0] + # diagonal moves part 1
         [(-i, i) for i in range(-(GRID_SIZE+1), GRID_SIZE) if i!=0], # diagonal moves part 2
    "N": [(-2, 1), (2, 1), (1, -2), (1, 2), (2, -1), (-2, -1), (-1, 2), (-1, -2)],
    "p": [(0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
}

PIECE_POINTS = {
    "K": 100, # Arbitrarily high
    "Q": 9,
    "R": 5,
    "B": 3,
    "N": 3,
    "p": 1
}

COLUMN_NAMES = ["a", "b", "c", "d", "e", "f", "g", "h"]
ROW_NAMES = ["8", "7", "6", "5", "4", "3", "2", "1"]

class ChessGame:

    def __init__(self) -> None:
        
        # State Variables
        self.game_board = [
            ["bR2", "bN2", "bB2", "bQ1", "bK1", "bB1", "bN1", "bR1"],
            ["bp8", "bp7", "bp6", "bp5", "bp4", "bp3", "bp2", "bp1"],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7", "wp8"],
            ["wR1", "wN1", "wB1", "wQ1", "wK1", "wB2", "wN2", "wR2"],
        ]

        self.last_move_result: str = "\n ###############  NEW GAME  ############### \n"
        self.white_turn: bool = True
        self.game_is_active: bool = True
        return

    def print_board_state(self):
        # Loop over each piece and print in a grid
        print("=====================================================")
        for i, row in enumerate(self.game_board):
            print(ROW_NAMES[i], "|| " + " | ".join(row) + " ||")
            if i != (GRID_SIZE-1):
                print("-----------------------------------------------------")
        print("=====================================================")
        print("  || ", "  |  ".join(COLUMN_NAMES)," ||")
    
    def describe_game_state(self) -> None:
        print(self.last_move_result)
        return
    
    def take_step(self) -> bool:
        """
        This method is called to allow the user to see the game state and input moves
        Return True if game is still active
        """

        # Describe state of game in text (i.e. "Game Over, White Wins", "Black Checks White" etc)
        self.describe_game_state()

        # Print board state
        self.print_board_state()

        # Prompt for next move "White:", "Black:"
        move = input("White: " if self.white_turn else "Black: ")
        # Input should be chess notation
        # Game state only changes if the input move is legal
        print(move)
        # Prompt user for next move
        # Find where piece is on the board
        # Move piece to new location
        # Print updated game board

        # Check that move is valid
        # if self.is_legal_move():

        

        # TODO Return true if game is still active

        return False
    
    @staticmethod
    def get_location(move: str, piece: str, game_board, white_turn) -> list:
        # create piece name
        piece_name = ("w" if white_turn else "b") + piece
        # search game board for piece location

        # return location of piece

        # Receive desired move from user
    
    @staticmethod
    def is_legal_move(move: str, piece: str, game_board) -> bool:
        # Return True if move is legal, given the piece, color, and game board state

        raise NotImplementedError
    
    @staticmethod
    def is_obstructed(game_board, start_pos, ending_pos) -> bool:
        # When given a board state, starting position, and ending position, return true if any pieces obstruct the path from start to end
        raise NotImplementedError
    
    @staticmethod
    def is_check(game_board, team: str) -> bool:
        # Check if we put opponent in check or our move puts ourself in check
        raise NotImplementedError
    
    @staticmethod
    def pawn_promote(game_board, team: str) -> str:
        # If white pawn reaches A8 - H8, ask White player which piece they want to replace pawn with
        # If black pawn reaches A1 - H8, ask Black player which piece they want to replace pawn with
        # Return decision or p for no promotion
        raise NotImplementedError
    
    @staticmethod
    def get_white_score(game_board) -> float:
        # Given the game-board, return the net score for white
        score = 0
        for row in game_board:
            for piece in row:
                # Split the string into parts
                team, piece_type, piece_number = piece
                if piece_type not in PIECE_POINTS:
                    continue
                if team == "w":
                    score += PIECE_POINTS[piece_type]
                else:
                    score -= PIECE_POINTS[piece_type]
        return score


def test_starting_score():
    game = ChessGame()
    assert ChessGame.get_white_score(game.game_board) == 0


if __name__=="__main__":

    # Initialize game
    game = ChessGame()

    # Take steps until game is over
    while game.take_step():
        pass
