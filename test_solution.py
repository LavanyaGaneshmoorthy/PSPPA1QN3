import pytest
from solution import magical_chest_swap_and_encrypt

# Test case 1: Basic functionality test
def test_magical_chest_swap_and_encrypt():
    scroll_elara = "Hello, Elara's Scroll!"
    scroll_orion = "Greetings from Orion!"

    lunar_phase = 3

    encrypted_elara, encrypted_orion = magical_chest_swap_and_encrypt(scroll_elara, scroll_orion, lunar_phase)

    # Check if the scrolls are swapped
    assert encrypted_elara == "Yvccr, Eynen'f Fpevpx!"
    assert encrypted_orion == "Jytravqrf sebz Bevba!"

# Test case 2: Test with different lunar phase
def test_magical_chest_swap_and_encrypt_different_phase():
    scroll_elara = "Testing with a different lunar phase!"
    scroll_orion = "Make sure the encryption works correctly."

    lunar_phase = 7

    encrypted_elara, encrypted_orion = magical_chest_swap_and_encrypt(scroll_elara, scroll_orion, lunar_phase)

    # Check if the scrolls are swapped and encrypted correctly with a different lunar phase
    assert encrypted_elara == "Hkjoklph jhf q fqpjmfm qfvrb qnovi!"
    assert encrypted_orion == "Xzltnz vohz xli mrxmrk csyv ewlmtliv."

# Additional test cases can be added based on specific requirements

if __name__ == "__main__":
    pytest.main()
