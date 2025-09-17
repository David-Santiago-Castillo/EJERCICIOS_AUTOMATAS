def problem2(input_string: str) -> bool:
    """
    Simulates a DFA for strings where the number of 'a's is even and 
    the substring 'bc' does not appear.

    The state is represented by a tuple (parity_of_a, last_char_is_b).
    - State 'q_even_none': Even 'a's, last char was not 'b'. (Start)
    - State 'q_odd_none': Odd 'a's, last char was not 'b'.
    - State 'q_even_b': Even 'a's, last char was 'b'.
    - State 'q_odd_b': Odd 'a's, last char was 'b'.
    - State 'q_trap': The substring 'bc' was found.

    Args:
        input_string: The string to be checked.

    Returns:
        True if the string is accepted, False otherwise.
    """
    # States of the DFA
    states = {'q_even_none', 'q_odd_none', 'q_even_b', 'q_odd_b', 'q_trap'}
    # Alphabet
    alphabet = {'a', 'b', 'c'}
    # Initial state (0 is even, so we start in an even state)
    start_state = 'q_even_none'
    # Accepting states (number of 'a's must be even)
    accept_states = {'q_even_none', 'q_even_b'}

    # Transition function
    transitions = {
        'q_even_none': {'a': 'q_odd_none', 'b': 'q_even_b', 'c': 'q_even_none'},
        'q_odd_none':  {'a': 'q_even_none', 'b': 'q_odd_b', 'c': 'q_odd_none'},
        'q_even_b':    {'a': 'q_odd_none', 'b': 'q_even_b', 'c': 'q_trap'},
        'q_odd_b':     {'a': 'q_even_none', 'b': 'q_odd_b', 'c': 'q_trap'},
        'q_trap':      {'a': 'q_trap', 'b': 'q_trap', 'c': 'q_trap'}
    }

    # Start simulation
    current_state = start_state
    
    # Process each character
    for char in input_string:
        if char not in alphabet:
            return False
        current_state = transitions[current_state][char]
        
    # Check for acceptance
    return current_state in accept_states

# --- Example Usage ---
print("\nProblem 2:")
print(f"Accepts 'aab': {problem2('aab')}")
print(f"Accepts 'baba': {problem2('baba')}")
print(f"Accepts '': {problem2('')}")
print(f"Rejects 'a': {problem2('a')}")
print(f"Rejects 'abc': {problem2('abc')}")
print(f"Rejects 'aabc': {problem2('aabc')}")