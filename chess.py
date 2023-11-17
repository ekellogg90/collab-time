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


class ChessGame:

    def __init__(self) -> None:
        
        # State Variables
        self.game_board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]

        self.last_move_result: str = "\n ###############  NEW GAME  ############### \n"
        self.white_turn: bool = True
        self.game_is_active: bool = True
        return

    def print_board_state(self):
        # Loop over each piece and print in a grid
        print("===========================================")
        for i, row in enumerate(self.game_board):
            print("|| " + " | ".join(row) + " ||")
            if i != (GRID_SIZE-1):
                print("-------------------------------------------")
        print("===========================================")
    
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

        # Promp for next move "White:", "Black:"
        user_input = input("What should I print?")
        # Input should be chess notation
        # Game state only changes if the input move is legal
        print(user_input)

        # TODO Return true if game is still active

        return False
    
    @staticmethod
    def is_legal_move(move: str, piece: str, game_board) -> bool:
        # Return True if move is legal, given the piece, color, and game board state
        raise NotImplementedError
    
    @staticmethod
    def is_obstructed(game_board, start_pos, ending_pos) -> bool:
        # When given a board state, starting position, and ending position, return true if any pieces obstruct the path from start to end
        raise NotImplementedError
    
    @staticmethod
    def get_white_score(game_board) -> float:
        # Given the game-board, return the net score for white
        score = 0
        for row in game_board:
            for piece in row:
                # Split the string into parts
                team, piece_type = piece
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
