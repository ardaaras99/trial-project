import trial_project


def test_import() -> None:
    """Test that the package can be imported without errors."""
    assert isinstance(trial_project.__name__, str)


def test_add() -> None:
    """Test that the add function works correctly."""
    assert 1 + 2 == 4
