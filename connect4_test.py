import unittest
from connect4 import ConnectFour,Player

class TestConnectFourMethods(unittest.TestCase):

    def setUp(self):
        # Create players and ConnectFour instance
        player1 = Player('X')
        player2 = Player('O')
        self.connect_four = ConnectFour(player1, player2, None) 

    def test_valid_move(self):
        # Test valid moves
        self.assertTrue(self.connect_four.is_valid_move(0))
        self.assertTrue(self.connect_four.is_valid_move(3))
        self.assertTrue(self.connect_four.is_valid_move(6))

        # Test invalid moves
        self.connect_four.board[0][0] = 'X'  
        self.assertFalse(self.connect_four.is_valid_move(0))
        self.assertTrue(self.connect_four.is_valid_move(1))
        self.assertTrue(self.connect_four.is_valid_move(2))

    def test_check_win_horizontal(self):
        # Test horizontal win
        self.connect_four.board[0][0] = 'X'
        self.connect_four.board[0][1] = 'X'
        self.connect_four.board[0][2] = 'X'
        self.connect_four.board[0][3] = 'X'
        self.assertTrue(self.connect_four.check_win(0, 3))

    def test_check_win_horizontal3(self):
        # Test horizontal win
        self.connect_four.board[2][0] = 'X'
        self.connect_four.board[2][1] = 'X'
        self.connect_four.board[2][2] = 'X'
        self.connect_four.board[2][3] = 'X'
        self.assertTrue(self.connect_four.check_win(2, 3))

    def test_check_win_horizontal3(self):
        # Test horizontal win
        self.connect_four.board[5][0] = 'X'
        self.connect_four.board[5][1] = 'X'
        self.connect_four.board[5][2] = 'X'
        self.connect_four.board[5][3] = 'X'
        self.assertTrue(self.connect_four.check_win(5, 3))

    def test_check_win_vertical(self):
        # Test vertical win
        self.connect_four.board[5][0] = 'X'
        self.connect_four.board[4][0] = 'X'
        self.connect_four.board[3][0] = 'X'
        self.connect_four.board[2][0] = 'X'
        self.assertTrue(self.connect_four.check_win(2, 0))

    def test_check_win_vertical2(self):
        # Test vertical win
        self.connect_four.board[5][3] = 'X'
        self.connect_four.board[4][3] = 'X'
        self.connect_four.board[3][3] = 'X'
        self.connect_four.board[2][3] = 'X'
        self.assertTrue(self.connect_four.check_win(2, 3))
    
    def test_check_win_vertical3(self):
        # Test vertical win
        self.connect_four.board[5][6] = 'X'
        self.connect_four.board[4][6] = 'X'
        self.connect_four.board[3][6] = 'X'
        self.connect_four.board[2][6] = 'X'
        self.assertTrue(self.connect_four.check_win(2, 6))
    
    def test_check_win_vertical_false1(self):
        # Test vertical false
        self.connect_four.board[5][6] = 'X'
        self.connect_four.board[4][6] = 'X'
        self.connect_four.board[3][6] = 'O'
        self.connect_four.board[2][6] = 'X'
        
        self.assertFalse(self.connect_four.check_win(5, 6))

    def test_check_win_diagonal1(self):
        # Test diagonal win
        self.connect_four.board[5][5] = 'X'
        self.connect_four.board[4][4] = 'X'
        self.connect_four.board[3][3] = 'X'
        self.connect_four.board[2][2] = 'X'
        self.assertTrue(self.connect_four.check_win(2, 2))

    def test_check_win_diagonal2(self):
        # Test diagonal win
        self.connect_four.board[5][0] = 'X'
        self.connect_four.board[4][1] = 'X'
        self.connect_four.board[3][2] = 'X'
        self.connect_four.board[2][3] = 'X'
        self.assertTrue(self.connect_four.check_win(2, 3))

    def test_check_win_diagonal_fallse1(self):
        # Test diagonal false
        self.connect_four.board[5][5] = 'X'
        self.connect_four.board[4][4] = 'O'
        self.connect_four.board[3][3] = 'X'
        self.connect_four.board[2][2] = 'X'
        self.assertFalse(self.connect_four.check_win(2, 2))

    def test_check_win_diagonal_false2(self):
        # Test diagonal false
        self.connect_four.board[5][0] = 'X'
        self.connect_four.board[4][1] = 'X'
        self.connect_four.board[3][2] = 'O'
        self.connect_four.board[2][3] = 'X'
        self.assertFalse(self.connect_four.check_win(2, 3))


    def test_is_board_full(self):
        # Test when the board is not full
        self.assertFalse(self.connect_four.is_board_full())

        # Fill the board to make it full
        for col in range(7):
            for row in range(6):
                self.connect_four.board[row][col] = 'X'

        # Test when the board is full
        self.assertTrue(self.connect_four.is_board_full())

    def test_switch_player(self):
        # Test switching players
        self.assertEqual(self.connect_four.current_player, self.connect_four.players[0])
        self.connect_four.switch_player()
        self.assertEqual(self.connect_four.current_player, self.connect_four.players[1])
        self.connect_four.switch_player()
        self.assertEqual(self.connect_four.current_player, self.connect_four.players[0])


if __name__ == '__main__':
    unittest.main()
