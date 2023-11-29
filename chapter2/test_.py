from main2 import *
import pytest


class TestPrintVarFunction:
    @pytest.mark.parametrize("n,expected", [(1, 1), (2, 2), (3, 3)])
    def test_print_var(self, n, expected):
        assert print_var(n) == expected

    def test_print_var_incorrect(self):
        assert print_var(3) != 4


class TestPrintText:
    @pytest.mark.parametrize("text,n,expected", [("coleslaw",1, "coleslaw"),("meow",2, "meowmeow"),("hi",5, "hihihihihi")])
    def test_print_text_x_times(self, text,n, expected):
        assert print_text_x_times(text, n) == expected

