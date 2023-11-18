"""
Simple CLI Chess Game

* Board and pieces rendered in the command line
* Accepts input in chess notation (i.e. Rg3)
* If the move is illegal an informative message is printed
"""
import pytest

# Support variables
GRID_SIZE = 8
# TODO Update allowed moves to y, x form
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
        # Prompt for next move
        piece, target = self.get_user_input()
        # Get indices of source location
        source_position = self.get_indices_from_piece(piece, self.game_board)
        print("source position: ", source_position)
        # Get indices of target location
        target_position = self.get_indices_from_location(target)
        print("target position: ", target_position)
        # Compute the move
        move = (target_position[0]-source_position[0], target_position[1]-source_position[1])
        print("move: ", move)
        # Game state only changes if the input move is legal
        self.execute_move(source_position, target_position)
        # Update game flow
        self.white_turn = not self.white_turn
        self.last_move_result = "\n" + "last move: " + piece + target + "\n"

        # TODO Return true if game is still active

        return True
    
    def get_user_input(self) -> tuple:
        # Prompt user to input directions (i.e. wp4 d4)
        print("White: " if self.white_turn else "Black: ")
        # Prompt user for piece & piece number and target location
        user_input = input("give piece and target location (i.e. wp4 d4): ")
        # TODO Perform checks to make sure input is valid, handle if not
        # TODO Add w or b if not present, or throw error until it's added by user
        return user_input.split(" ")
    
    def execute_move(self, source_position, target_position) -> None:
        src_y, src_x = source_position
        tar_y, tar_x = target_position
        # Move piece to new spot
        self.game_board[tar_y][tar_x] = self.game_board[src_y][src_x]
        # Replace original spot with empty cell
        self.game_board[src_y][src_x] = "   "
        return
    
    @staticmethod
    def get_indices_from_location(location: str) -> tuple:
        # Accepts a-h + 1-8
        x_loc_, y_loc_ = location
        for y, y_loc in enumerate(ROW_NAMES):
            for x, x_loc in enumerate(COLUMN_NAMES):
                if x_loc==x_loc_ and y_loc==y_loc_:
                    return y, x
        return (None, None)
    
    @staticmethod
    def get_indices_from_piece(piece: str, game_board) -> tuple:
        # search game board for piece location
        for y, row in enumerate(game_board):
            for x, cell_contents in enumerate(row):
                if cell_contents == piece:
                    return y, x
        return (None, None)

        # Receive desired move from user
    def list_possible_moves(self, game_board, white_turn) -> list:
        # Given the team and gameboard, list all possible moves
        #     How to do this?
        #     Loop over the gameboard and look for pieces of the active team
        #     For each white piece, test each allowed move
        #     If the allowed move is legal, keep it in the list
        team = "w" if white_turn else "b"
        for y, row in enumerate(game_board):
            for x, piece in enumerate(row):
                if team in piece:
                    team, piece_type, piece_number = piece
                    # TODO Test each allowed-move

                    

        pass
    
    @staticmethod
    def is_legal_move(move, piece: str, game_board) -> bool:
        # Return True if move is legal, given the piece, color, and game board state
        return True
    
    @staticmethod
    def is_obstructed(game_board, start_pos, ending_pos) -> bool:
        # When given a board state, starting position, and ending position, return true if any pieces obstruct the path from start to end
        return False
    
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
