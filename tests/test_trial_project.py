import trial_project


def test_import() -> None:
    """Test that the package can be imported without errors."""
    assert isinstance(trial_project.__name__, str)
