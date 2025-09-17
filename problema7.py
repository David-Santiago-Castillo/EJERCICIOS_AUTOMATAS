def problem7(input_string: str) -> bool:
    """
    Simulates a PDA for the language L = {w | n_a(w) >= n_b(w)}.
    
    The PDA uses the stack to keep track of the excess of 'a's over 'b's.
    - When an 'a' is read, push a marker 'A' onto the stack.
    - When a 'b' is read:
        - If the stack is not empty (i.e., there's an excess of 'a's), pop an 'A'.
        - If the stack is empty, it means we have seen more 'b's than 'a's,
          so we must push a 'B' to track the deficit of 'a's.
          
    At the end of the string, the string is accepted if the stack is empty
    or contains only 'A's. If it contains any 'B's, it means n_b > n_a,
    and the string is rejected.

    Args:
        input_string: The string to be checked.

    Returns:
        True if the string is accepted, False otherwise.
    """
    stack = []
    
    # Process the input string character by character
    for char in input_string:
        if char == 'a':
            # If we see a 'b' deficit, an 'a' cancels it out.
            # Otherwise, add to the 'a' surplus.
            if stack and stack[-1] == 'B':
                stack.pop()
            else:
                stack.append('A')
        elif char == 'b':
            # If we see an 'a' surplus, a 'b' cancels it out.
            # Otherwise, add to the 'b' deficit.
            if stack and stack[-1] == 'A':
                stack.pop()
            else:
                stack.append('B')
    
    # After processing the entire string, check the stack.
    # The string is accepted if there is no 'b' deficit.
    # This means the stack should not contain any 'B's.
    if 'B' in stack:
        return False
    else:
        return True

# --- Example Usage ---
print("\nProblem 7:")
print(f"Accepts 'aab': {problem7('aab')}")
print(f"Accepts 'abab': {problem7('abab')}")
print(f"Accepts '': {problem7('')}")
print(f"Accepts 'aaabb': {problem7('aaabb')}")
print(f"Rejects 'b': {problem7('b')}")
print(f"Rejects 'abb': {problem7('abb')}")
print(f"Rejects 'bab': {problem7('bab')}")