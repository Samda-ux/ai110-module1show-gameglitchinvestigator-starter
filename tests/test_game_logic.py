from streamlit.testing.v1 import AppTest
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_score_changes_when_swapping_difficulty():
    # Score from a Normal game should reset when swapping to Easy
    at = AppTest.from_file("app.py").run()
    assert at.session_state.difficulty == "Normal"

    # Make a wrong guess on Normal so the score moves away from 0
    wrong = "1" if at.session_state.secret != 1 else "2"
    at.text_input[0].input(wrong)
    at.button[0].click().run()  # "Submit Guess"
    assert at.session_state.score == -5

    # Swap to Easy and check the score changed (reset to 0)
    at.sidebar.selectbox[0].set_value("Easy").run()
    assert at.session_state.difficulty == "Easy"
    assert at.session_state.score == 0
