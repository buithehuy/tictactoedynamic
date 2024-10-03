class TicTacToe:
    def __init__(self, size=4, win_length=4):
        self.size = size
        self.win_length = win_length
        self.dp = {}

    def check_winner(self, board):
        # Check rows and columns
        for i in range(self.size):
            for j in range(self.size - self.win_length + 1):
                if all(board[i][j + k] == 1 for k in range(self.win_length)):  # Player 1 (X)
                    return 1
                if all(board[j + k][i] == 1 for k in range(self.win_length)):  # Player 1 (X)
                    return 1
                if all(board[i][j + k] == 2 for k in range(self.win_length)):  # Player 2 (O)
                    return -1
                if all(board[j + k][i] == 2 for k in range(self.win_length)):  # Player 2 (O)
                    return -1

        # Check diagonals
        for i in range(self.size - self.win_length + 1):
            for j in range(self.size - self.win_length + 1):
                if all(board[i + k][j + k] == 1 for k in range(self.win_length)):  # Player 1 (X)
                    return 1
                if all(board[i + k][j + k] == 2 for k in range(self.win_length)):  # Player 2 (O)
                    return -1
                if all(board[i + k][j + self.win_length - 1 - k] == 1 for k in range(self.win_length)):  # Player 1 (X)
                    return 1
                if all(board[i + k][j + self.win_length - 1 - k] == 2 for k in range(self.win_length)):  # Player 2 (O)
                    return -1

        # Check for a draw
        if all(board[i][j] != 0 for i in range(self.size) for j in range(self.size)):
            return 0

        return None  # Game is still ongoing

    def minimax(self, board, is_player_one):
        state_key = tuple(tuple(row) for row in board)

        # Check if the state is already computed
        if state_key in self.dp:
            return self.dp[state_key]

        winner = self.check_winner(board)
        if winner is not None:
            return winner

        if is_player_one:
            best_score = float('-inf')
            for i in range(self.size):
                for j in range(self.size):
                    if board[i][j] == 0:  # Empty cell
                        board[i][j] = 1  # Player 1 (X)
                        score = self.minimax(board, False)
                        board[i][j] = 0  # Undo move
                        best_score = max(best_score, score)
            self.dp[state_key] = best_score
            return best_score
        else:
            best_score = float('inf')
            for i in range(self.size):
                for j in range(self.size):
                    if board[i][j] == 0:  # Empty cell
                        board[i][j] = 2  # Player 2 (O)
                        score = self.minimax(board, True)
                        board[i][j] = 0  # Undo move
                        best_score = min(best_score, score)
            self.dp[state_key] = best_score
            return best_score

    def reset(self):
        self.dp.clear()

# Example Usage
if __name__ == "__main__":
    # Create a 4x4 Tic-Tac-Toe game
    game_4x4 = TicTacToe(size=4, win_length=4)

    # Initialize the board
    board_4x4 = [[0]*4 for _ in range(4)]

    # Player 1's turn (X)
    board_4x4[0][0] = 1
    board_4x4[0][1] = 1
    board_4x4[1][0] = 1

    # Player 2's turn (O)
    board_4x4[1][1] = 2

    # Use minimax to evaluate the current state
    result_4x4 = game_4x4.minimax(board_4x4, True)
    print("4x4 Tic-Tac-Toe Result:", result_4x4)

    # Create a 5x5 Tic-Tac-Toe game
    game_5x5 = TicTacToe(size=5, win_length=5)

    # Initialize the board
    board_5x5 = [[0]*5 for _ in range(5)]

    # Example moves
    board_5x5[0][0] = 1
    board_5x5[0][1] = 1
    board_5x5[1][0] = 1
    board_5x5[1][1] = 2

    # Use minimax to evaluate the current state
    result_5x5 = game_5x5.minimax(board_5x5, True)
    print("5x5 Tic-Tac-Toe Result:", result_5x5)
