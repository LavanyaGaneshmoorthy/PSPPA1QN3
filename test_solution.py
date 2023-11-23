# test_solution.py

from solution import swap_and_encrypt

def test_swap_and_encrypt():
    scroll1 = "Hello, Elara's Scroll!"
    scroll2 = "Greetings, Orion's Scroll!"
    lunar_phase = 3

    result1, result2 = swap_and_encrypt(scroll1, scroll2, lunar_phase)

    expected_result1 = "Juhhwlqjv, Rulrq'v Vfuroo!"
    expected_result2 = "Ebiil, Bixox'p Pzolii!"

    assert result1 == expected_result1
    assert result2 == expected_result2
