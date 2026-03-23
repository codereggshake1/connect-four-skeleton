"""
Hash the output of the docstring to prevent peeking at the answer.

Before unlocking, a test file must have:
- `>>> ` is an expression to evaluate
- `... ` for multi-line code
- `# locked` after the output displayed by Python
- 'locked' field of the case is set to `True`

After the test file is successfully unlocked:
- the output is unscrambled
- `# locked` comments removed
- `locked' field of the case is set to 'False'
"""

import hmac
def lock(key, text):
    """Locks the given text using the given key and returns the result"""
    return hmac.new(key.encode('utf-8'), text.encode('utf-8'), digestmod='md5').hexdigest()

def hash_docstring_outputs(docstring, hash_func):
    """
    Replace docstring outputs with hashed versions.
    
    Takes a docstring with doctest examples and replaces the output
    (the line before "# locked") with a hashed version of that output.
    
    Args:
        docstring: The docstring containing doctest examples
        hash_func: A function that takes a string and returns a hash
    
    Returns:
        The modified docstring with outputs replaced by their hashes
    """
    lines = docstring.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        result.append(line)
        
        # Check if the next line contains "# locked"
        if i + 1 < len(lines) and '# locked' in lines[i + 1]:
            # The current line is the output to be hashed
            output = line.strip()
            if output:  # Only hash non-empty lines
                hashed = hash_func(output)
                # Replace the output with its hash, preserving indentation
                indent = len(line) - len(line.lstrip())
                result[-1] = ' ' * indent + hashed
        
        i += 1
    
    return '\n'.join(result)

assignment_name = 'Connect 4' # this is 'name' field of the ok config file

# TODO: replace the docstring below with yours
docstring = r"""
            >>> from main import *

            >>> board = [[-1, -1, -1],
            ...           [-1, 1, 0],
            ...           [0, 0, 1]]
            >>> player0 = 0
            >>> player1 = 1
            >>> board[2][1] == player1
            False
            # locked
            >>> board[2][1] == player0
            True
            # locked
            >>> board[0][1] == player1
            False
            # locked
            >>> board[0][1] == player0
            False
            # locked
            >>> (board[0][1] == player0) or (board[0][1] == player1) # neither player's, so empty
            False
            # locked
          """

hashed_docstring = hash_docstring_outputs(docstring, lambda s: lock(assignment_name, s))
print(hashed_docstring)