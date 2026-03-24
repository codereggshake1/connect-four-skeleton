test = {
  'name': 'tidy',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from game_ai import *
          >>> board1 = [[-1, -1, -1],
          ...           [-1, -1, -1],
          ...           [-1, -1, -1]]
          >>> tidy(board1, 0)
          86981d2ca10397796da6c162cec98649
          # locked
          >>> board2 = [[1, -1, -1],
          ...           [1, -1, -1],
          ...           [1, 0, -1]]
          >>> tidy(board2, 0)
          68bbf6425ec317c61fa86d72f7f12cf1
          # locked
          >>> board3 = [[-1, 1, -1],
          ...           [-1, 1, 1],
          ...           [1, 0, 1]]
          >>> tidy(board3, 0)
          86981d2ca10397796da6c162cec98649
          # locked
          >>> board4 = [[0, 1, -1],
          ...           [1, 1, 1],
          ...           [0, 1, 0]]
          >>> tidy(board4, 0)
          cccf2ee0c4d019ba16be8500158ff169
          # locked
          >>> board5 = [[0, 1, 0],
          ...           [0, 1, 0],
          ...           [0, 1, 0]]
          >>> tidy(board5, 0)
          cccf2ee0c4d019ba16be8500158ff169
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
