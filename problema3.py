def problem3(input_string: str) -> bool:
    """
    Simulates an FA for a language with complex rules based on parity.

    The state is represented by a tuple (parity_of_ones, parity_of_trailing_zeros).
    - q0: even 1s, even trailing 0s (also the start state for no 1s seen yet).
    - q1: even 1s, odd trailing 0s.
    - q2: odd 1s, even trailing 0s.
    - q3: odd 1s, odd trailing 0s.

    Acceptance rules:
    1. No 1s -> must have even 0s (state q0).
    2. Even (>0) 1s -> must end in odd 0s (state q1).
    3. Odd 1s -> must end in even 0s (state q2).

    Args:
        input_string: The string to be checked.

    Returns:
        True if the string is accepted, False otherwise.
    """
    # Count the number of '1's to distinguish rule 1 from rule 2
    num_ones = input_string.count('1')

    # Rule 1: No '1's at all
    if num_ones == 0:
        # Must have an even number of 0's
        return input_string.count('0') % 2 == 0

    # For rules 2 and 3, we simulate the FA
    # Initial state (even 1s, even trailing 0s)
    current_state = 'q0'
    
    # Transition function
    transitions = {
        # State: (parity_of_1s, parity_of_trailing_0s)
        # q0: (even, even)
        'q0': {'0': 'q1', '1': 'q2'},
        # q1: (even, odd)
        'q1': {'0': 'q0', '1': 'q3'},
        # q2: (odd, even)
        'q2': {'0': 'q3', '1': 'q0'},
        # q3: (odd, odd)
        'q3': {'0': 'q2', '1': 'q1'}
    }

    # Process the string
    for char in input_string:
        current_state = transitions[current_state][char]

    # Check acceptance based on final state and number of '1's
    # Rule 2: Even (>0) number of 1s
    if num_ones > 0 and num_ones % 2 == 0:
        # Must end with an odd number of 0s (state q1)
        return current_state == 'q1'
    # Rule 3: Odd number of 1s
    elif num_ones % 2 != 0:
        # Must end with an even number of 0s (state q2)
        return current_state == 'q2'
    
    return False

# --- Example Usage ---
print("\nProblem 3:")
print(f"Accepts '00': {problem3('00')}")        # Rule 1
print(f"Accepts '11000': {problem3('11000')}")  # Rule 2
print(f"Accepts '100': {problem3('100')}")      # Rule 3
print(f"Accepts '010': {problem3('010')}")      # Rule 3
print(f"Rejects '0': {problem3('0')}")          # Rule 1 fail
print(f"Rejects '1100': {problem3('1100')}")    # Rule 2 fail
print(f"Rejects '10': {problem3('10')}")        # Rule 3 fail