class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
    
    def place_piece(self, piece, x, y):
        if self.is_in_bounds(x, y):
            self.grid[y][x] = piece
            piece.position = (x, y)
    
    def move_piece(self, piece, new_x, new_y):
        if self.is_in_bounds(new_x, new_y) and self.grid[new_y][new_x] is None:
            old_x, old_y = piece.position
            self.grid[old_y][old_x] = None
            self.place_piece(piece, new_x, new_y)
    
    def is_in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

class Piece:
    def __init__(self, name, player, position=None):
        self.name = name
        self.player = player
        self.position = position

    def possible_moves(self, board):
        """Return a list of possible moves for this piece on the board"""
        raise NotImplementedError("This method should be overridden by subclasses")

class Player:
    def __init__(self, name):
        self.name = name
        self.pieces = []

    def add_piece(self, piece):
        self.pieces.append(piece)

class Game:
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.current_player_index = 0

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def is_game_over(self):
        """Determine if the game is over based on variant-specific rules"""
        raise NotImplementedError("This method should be overridden by subclasses")

class GameManager:
    def __init__(self, game_variant, num_players):
        self.game_variant = game_variant
        self.num_players = num_players
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.board = self.initialize_board(game_variant)
        self.game = self.initialize_game()

    def initialize_board(self, game_variant):
        """Initialize the board based on the variant"""
        if game_variant == "Chess":
            return Board(8, 8)
        # Add more game variants here
        # ...
    
    def initialize_game(self):
        """Initialize the game with pieces, rules, etc."""
        # Depending on the variant, set up the game rules and pieces
        # ...
        return Game(self.board, self.players)

    def start_game(self):
        while not self.game.is_game_over():
            current_player = self.players[self.game.current_player_index]
            # Handle player move
            self.game.next_turn()

# Example usage
game_manager = GameManager("Chess", 2)
game_manager.start_game()
