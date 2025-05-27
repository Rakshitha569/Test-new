import random
import time
import threading

class Player:
    """
    Represents a player in the Snakes and Ladders game.
    Each player has a name, a position on the board, and a lock to ensure thread safety.
    """
    def __init__(self, name, color):
        self.name = name
        self.position = 0
        self.lock = threading.Lock()
        self.color = color  # Assign a color to the player

    def __repr__(self):
        return f"Player(name='{self.name}', position={self.position}, color='{self.color}')"

class SnakesAndLadders:
    """
    A complex Snakes and Ladders game with multiple players, configurable board size,
    snakes, ladders, and game modes. Supports multi-threading for concurrent gameplay.
    """
    def __init__(self, board_size=100, num_snakes=10, num_ladders=10, num_players=2, game_mode="normal"):
        """
        Initializes the game with a specified board size, number of snakes and ladders,
        number of players, and game mode.
        """
        self.board_size = board_size
        self.snakes = self.generate_snakes(num_snakes)
        self.ladders = self.generate_ladders(num_ladders)
        self.players = [Player(f"Player {i+1}", self.get_player_color(i)) for i in range(num_players)]
        self.game_over = False
        self.game_mode = game_mode  # "normal", "aggressive", "strategic"
        self.board_lock = threading.Lock()  # Lock for board access
        self.move_delay = 1  # Delay between moves in seconds
        self.colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan']  # Player colors

    def get_player_color(self, player_index):
        """
        Assigns a unique color to each player.
        """
        return self.colors[player_index % len(self.colors)]

    def generate_snakes(self, num_snakes):
        """
        Generates snakes on the board, ensuring that snakes do not start at the beginning
        or end of the board, and that snakes and ladders do not overlap.
        """
        snakes = {}
        while len(snakes) < num_snakes:
            start = random.randint(10, self.board_size - 10)
            end = random.randint(2, start - 2)
            if start not in self.ladders and end not in self.ladders and start not in snakes and end not in snakes:
                snakes[start] = end
        return snakes

    def generate_ladders(self, num_ladders):
        """
        Generates ladders on the board, ensuring that ladders do not start at the beginning
        or end of the board, and that snakes and ladders do not overlap.
        """
        ladders = {}
        while len(ladders) < num_ladders:
            start = random.randint(2, self.board_size - 10)
            end = random.randint(start + 2, self.board_size - 2)
            if start not in self.snakes and end not in self.snakes and start not in ladders and end not in ladders:
                ladders[start] = end
        return ladders

    def roll_dice(self):
        """
        Simulates rolling a six-sided dice.
        """
        return random.randint(1, 6)

    def move_player(self, player):
        """
        Moves a player on the board based on the dice roll and game mode.
        """
        dice_roll = self.roll_dice()
        print(f"{player.name} rolled a {dice_roll}")

        with player.lock:
            new_position = player.position + dice_roll

            if new_position > self.board_size:
                print(f"{player.name} cannot move past the end of the board.")
                return

            print(f"{player.name} moving from {player.position} to {new_position}")
            player.position = new_position

            if player.position in self.snakes:
                print(f"{player.name} landed on a snake! Sliding down from {player.position} to {self.snakes[player.position]}")
                player.position = self.snakes[player.position]
            elif player.position in self.ladders:
                print(f"{player.name} landed on a ladder! Climbing up from {player.position} to {self.ladders[player.position]}")
                player.position = self.ladders[player.position]

            if player.position == self.board_size:
                print(f"{player.name} has won the game!")
                self.game_over = True

    def strategic_move(self, player, dice_roll):
        """
        Implements a strategic move where the player tries to avoid snakes and aim for ladders.
        """
        new_position = player.position + dice_roll
        if new_position > self.board_size:
            return

        # Check if the new position has a snake
        if new_position in self.snakes:
            # Try to find an alternative move to avoid the snake
            alternative_moves = []
            for i in range(1, 7):
                alt_position = player.position + i
                if alt_position <= self.board_size and alt_position not in self.snakes:
                    alternative_moves.append((i, alt_position))

            if alternative_moves:
                # Choose the move that gets the player closest to a ladder or furthest from a snake
                best_move = max(alternative_moves, key=lambda move: self.ladders.get(move[1], 0) - self.snakes.get(move[1], 0))
                dice_roll = best_move[0]
                new_position = player.position + dice_roll
                print(f"{player.name} strategically moved to avoid a snake.")
            else:
                print(f"{player.name} had no choice but to land on a snake.")

        player.position = new_position

    def aggressive_move(self, player, dice_roll):
        """
        Implements an aggressive move where the player aims to land on the same square as another player,
        forcing them to move back.
        """
        new_position = player.position + dice_roll
        if new_position > self.board_size:
            return

        # Check if any other player is on the new position
        for other_player in self.players:
            if other_player != player and other_player.position == new_position:
                print(f"{player.name} aggressively landed on {other_player.name}! Sending them back to 0.")
                other_player.position = 0

        player.position = new_position

    def play_turn(self, player):
        """
        Plays a turn for a given player based on the game mode.
        """
        if self.game_over:
            return

        with self.board_lock:
            print(f"\n{player.name}'s turn (Position: {player.position})")
            dice_roll = self.roll_dice()
            print(f"{player.name} rolled a {dice_roll}")

            with player.lock:
                new_position = player.position + dice_roll

                if new_position > self.board_size:
                    print(f"{player.name} cannot move past the end of the board.")
                    return

                print(f"{player.name} moving from {player.position} to {new_position}")

                if self.game_mode == "strategic":
                    self.strategic_move(player, dice_roll)
                elif self.game_mode == "aggressive":
                    self.aggressive_move(player, dice_roll)
                else:
                    player.position = new_position

                if player.position in self.snakes:
                    print(f"{player.name} landed on a snake! Sliding down from {player.position} to {self.snakes[player.position]}")
                    player.position = self.snakes[player.position]
                elif player.position in self.ladders:
                    print(f"{player.name} landed on a ladder! Climbing up from {player.position} to {self.ladders[player.position]}")
                    player.position = self.ladders[player.position]

                if player.position == self.board_size:
                    print(f"{player.name} has won the game!")
                    self.game_over = True

    def play_game(self):
        """
        Starts and runs the Snakes and Ladders game until a player wins.
        Uses multi-threading to allow players to take turns concurrently.
        """
        print("Starting Snakes and Ladders game...")
        threads = []
        while not self.game_over:
            for player in self.players:
                thread = threading.Thread(target=self.play_turn, args=(player,))
                threads.append(thread)
                thread.start()
                time.sleep(self.move_delay)  # Add a delay between player turns

            for thread in threads:
                thread.join()  # Wait for all threads to complete

            threads = []  # Clear the threads list for the next round

        print("Game over!")

# Example Usage:
if __name__ == "__main__":
    # Configure the game
    board_size = 100
    num_snakes = 15
    num_ladders = 15
    num_players = 4
    game_mode = "strategic"  # Can be "normal", "aggressive", or "strategic"

    # Initialize and start the game
    game = SnakesAndLadders(board_size, num_snakes, num_ladders, num_players, game_mode)
    game.play_game()
