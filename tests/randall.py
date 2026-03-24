test = {
  'name': 'randall',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from game_ai import *
          >>> from tests.utils.testing_utils import *
          >>> random.seed(37) # seed for deterministic testing
          >>> board1 = [[-1, -1, -1],
          ...           [-1, 1, 0],
          ...           [-1, 1, 1]]
          >>> props1 = proportions(board1, 0, randall) # see utils > testing_utils.py for this function
          >>> is_uniform(props1) # see utils > testing_utils.py for this function
          True
          >>> abs(sum(props1) - 1) <= .01 # props sum to 1
          True
          >>> board2 = [[-1, 1, -1, 1, -1],
          ...           [-1, 0, 0, 1, -1],
          ...           [1, 1, 1, 0, -1],
          ...           [0, 1, 1, -1, 1]]
          
          >>> props2 = proportions(board2, 0, randall)
          >>> is_uniform(props2)
          True
          >>> abs(sum(props2) - 1) <= .01 # props sum to 1
          True
          >>> board3 = [[1, 1, 1, 1, -1],
          ...           [1, 0, 0, 1, 1],
          ...           [1, 1, 1, 0, 1],
          ...           [0, 1, 1, -1, 1]]
          >>> props3 = proportions(board3, 0, randall)
          >>> is_uniform(props3)
          True
          >>> abs(sum(props2) - 1) <= .01 # props sum to 1
          True
          """,
          'hidden': False,
          'locked': False,
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
