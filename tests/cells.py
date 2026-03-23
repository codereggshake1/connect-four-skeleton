test = {
  'name': 'cells',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
            >>> from main import *

            >>> board = [[-1, -1, -1],
            ...           [-1, 1, 0],
            ...           [0, 0, 1]]
            >>> player0 = 0
            >>> player1 = 1
            >>> board[2][1] == player1
            77ea9ef26b25e1d0ff94c7935175bdc4
            # locked
            >>> board = [[-1, -1, -1],
            ...           [-1, 1, 0],
            ...           [0, 0, 1]]
            >>> board[2][1] == player0
            2498e6203aaac702eb1bb28ffee36c44
            # locked
            >>> board = [[-1, -1, -1],
            ...           [-1, 1, 0],
            ...           [0, 0, 1]]
            >>> board[0][1] == player1
            77ea9ef26b25e1d0ff94c7935175bdc4
            # locked
            >>> board = [[-1, -1, -1],
            ...           [-1, 1, 0],
            ...           [0, 0, 1]]
            >>> board[0][1] == player0
            77ea9ef26b25e1d0ff94c7935175bdc4
            # locked
            >>> board = [[-1, -1, -1],
            ...           [-1, 1, 0],
            ...           [0, 0, 1]]
            >>> (board[0][1] == player0) or (board[0][1] == player1) # neither player's, so empty
            77ea9ef26b25e1d0ff94c7935175bdc4
            # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
