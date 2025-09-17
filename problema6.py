def problem6(input_string: str) -> bool:
    """
    Simulates a PDA for the language L = {a^i b^j c^k a | i, j > 0; k = j}.
    
    The PDA works as follows:
    1. Reads one or more 'a's (i > 0).
    2. Reads one or more 'b's (j > 0) and pushes a marker 'B' for each 'b' onto the stack.
    3. Reads 'c's. For each 'c', it pops a 'B' from the stack.
    4. If the stack is empty after reading 'c's and the next char is 'a', it moves to the final state.
    5. The string must end after that final 'a'.

    Args:
        input_string: The string to be checked.

    Returns:
        True if the string is accepted, False otherwise.
    """
    stack = []
    # Using an index to iterate through the string
    i = 0
    n = len(input_string)
    
    # State 1: Reading initial 'a's (i > 0)
    if i >= n or input_string[i] != 'a':
        return False # Must start with at least one 'a'
    i += 1
    while i < n and input_string[i] == 'a':
        i += 1
        
    # State 2: Reading 'b's and pushing to stack (j > 0)
    if i >= n or input_string[i] != 'b':
        return False # Must have at least one 'b'
    stack.append('B')
    i += 1
    while i < n and input_string[i] == 'b':
        stack.append('B')
        i += 1
        
    # State 3: Reading 'c's and popping from stack (k = j)
    while i < n and input_string[i] == 'c':
        if not stack:
            return False # More 'c's than 'b's
        stack.pop()
        i += 1
        
    # After reading 'c's, the stack must not be empty
    if not stack:
        # This means we might have popped the last B.
        # But if there were more c's this would have failed already.
        # Let's re-verify the logic.
        pass # This check is tricky. We check stack after the loop.
    
    # Let's adjust the logic slightly. Pop must succeed for every c.
    # The stack being empty is checked after the 'c' block.
    
    # State 4: Check for final 'a'
    if i >= n or input_string[i] != 'a':
        return False # Must have a final 'a'
    i += 1
    
    # Final check: The string must be fully consumed and the stack must be empty.
    return i == n and not stack

# --- Example Usage ---
print("\nProblem 6:")
print(f"Accepts 'abbcca': {problem6('abbcca')}")
print(f"Accepts 'aaabcca': {problem6('aaabcca')}")
print(f"Rejects 'abca': {problem6('abca')}")      # j != k
print(f"Rejects 'abbca': {problem6('abbca')}")     # j != k
print(f"Rejects 'bca': {problem6('bca')}")         # i=0
print(f"Rejects 'aca': {problem6('aca')}")         # j=0
print(f"Rejects 'abbcc': {problem6('abbcc')}")     # no final 'a'