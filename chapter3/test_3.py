from main3 import *
import pytest

class TestCountTip:

    def test_count_tip_default(self):
        assert count_tip(100) == 5

    def test_count_tip_float(self):
        assert count_tip(4.7) == 0.24

    def test_count_tip_negative(self):
        with pytest.raises(ValueError, match="Negative number is not allowed"):
            count_tip(-10)

    @pytest.mark.parametrize("ammount, no_persons, percent,expected", [(200, 3, 15, 1),(230, 5, 1, 1),(333, 7, 17, 1)])
    def test_count_tip(self, ammount, no_persons, percent, expected):
        assert count_tip(ammount, no_persons, percent) == expected

    def test_count_tip_incorrect(self):
        assert count_tip(3) != 4

    def test_count_tip_missing_ammount(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'ammount'"):
            count_tip()

    def test_count_tip_string(self):
        with pytest.raises(TypeError, match="Value must be a number"):
            count_tip("abc")