from logic_utils import check_guess, get_range_for_difficulty, parse_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_empty_guess_is_rejected():
    assert parse_guess("") == (False, None, "Enter a guess.")


def test_non_numeric_guess_is_rejected():
    assert parse_guess("not-a-number") == (
        False,
        None,
        "That is not a number.",
    )


def test_negative_guess_is_parsed_as_a_number():
    assert parse_guess("-3") == (True, -3, None)


def test_decimal_guess_is_converted_to_an_integer():
    assert parse_guess("49.9") == (True, 49, None)


def test_difficulty_ranges_match_starter_settings():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
