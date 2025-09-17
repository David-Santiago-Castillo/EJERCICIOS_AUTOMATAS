def problem4(input_string: str) -> bool:
    """
    Simulates a DFA for the language L3 = L1 U L2, where
    L1 = {(01)^n | n >= 0} and L2 = {(10)^n | n >= 0}.
    This is the language of alternating 0s and 1s.

    - q0: Start state, accepting (for empty string).
    - q1: Expecting a '1' next.
    - q2: Expecting a '0' next.
    - q3: Trap state.

    Args:
        input_string: The string to be checked.

    Returns:
        True if the string is accepted, False otherwise.
    """
    # Empty string is accepted
    if not input_string:
        return True

    # Initial state
    start_state = 'q0'
    # Accepting states
    accept_states = {'q0', 'q1', 'q2'} # All non-trap states can be final

    # Transition function
    transitions = {
        'q0': {'0': 'q1', '1': 'q2'},
        'q1': {'0': 'q3', '1': 'q0'},
        'q2': {'0': 'q0', '1': 'q3'},
        'q3': {'0': 'q3', '1': 'q3'}
    }

    # Start simulation
    current_state = start_state
    
    # Process the string
    for char in input_string:
        current_state = transitions[current_state][char]
        
    # Check for acceptance
    return current_state in accept_states

# --- Example Usage ---
print("\nProblem 4:")
print(f"Accepts '': {problem4('')}")
print(f"Accepts '0101': {problem4('0101')}")
print(f"Accepts '10101': {problem4('10101')}")
print(f"Rejects '00': {problem4('00')}")
print(f"Rejects '1001': {problem4('1001')}")
print(f"Rejects '011': {problem4('011')}")