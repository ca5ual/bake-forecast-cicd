from bake_forecast.forecast import get_average_bakes
from pathlib import Path
import pytest


def test_valid_csv(tmp_path: Path):
    file = tmp_path / "data.csv"
    file.write_text("day;quantity_sold\nMonday;10\nMonday;20\nTuesday;5\n")

    from unittest.mock import patch

    with patch("bake_forecast.forecast.datetime") as mock_dt:
        mock_dt.today.return_value.strftime.return_value = "Monday"
        result = get_average_bakes(file)

    assert result == 15.0  # (10 + 20) / 2


def test_empty_csv(tmp_path: Path):
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("day;quantity_sold\n")

    from unittest.mock import patch

    with patch("bake_forecast.forecast.datetime") as mock_dt:
        mock_dt.today.return_value.strftime.return_value = "Thirsday"
        empty_result = get_average_bakes(empty_file)

    assert empty_result == 0.0


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        get_average_bakes(Path("non_existent.csv"))
