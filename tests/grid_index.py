test = {
  'name': 'grid-index',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from main import *
          >>> board1 = create_board(6, 7) # a connect-four board has 6 rows and 7 columns
          >>> len(board1)
          c352d198d88e2da6c25d87b14e8b646d
          # locked
          >>> len(board1[0])
          9a517f3fe5cf0433352f53860ae5631a
          # locked
          >>> board2 = [[1, 2, 3],
          ...           [3, 1, 0],
          ...           [0, 2, 1]]
          >>> board2[0][0]
          68bbf6425ec317c61fa86d72f7f12cf1
          # locked
          >>> board[2][1]
          cccf2ee0c4d019ba16be8500158ff169
          # locked
          >>> board[1][0]
          a55a0a48d25a1d5df26746e1bd67ec47
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
