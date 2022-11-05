import pytest

from calc.calc import Calc


class TestSum:

    def test_add_two_numbers(self):
        c = Calc()
        res = c.add(4, 5)

        assert res == 9

    def test_add_three_numbers(self):
        c = Calc()
        res = c.add(4, 5, 6)
        assert res == 14

    def test_add_many_numbers(self):
        assert Calc().add(*range(100)) == 4950

    def test_sum_no_numbers(self):
        assert Calc().add() == 0


class TestSub:
    def test_subtract_two_numbers(self):
        assert Calc().sub(10, 3) == 7


class TestMultiplication:
    def test_multiply_two_numbers(self):
        assert Calc().mul(6, 4) == 24

    def test_multiply_1_2_3_c(self):
        with pytest.raises(TypeError):
            print(Calc().mul(1, 2, 3, 'c'))

    def test_multiply_many_numbers(self):
        assert Calc().mul(*range(1, 10)) == 362880

    def test_mul_no_numbers(self):
        assert Calc().mul() == 1


class TestDivision:
    def test_division_two_number(self):
        assert Calc().div(13, 2) == 6.5

    def test_division_by_zero_returns_inf(self):
        assert Calc().div(13, 0) == 'inf'


class TestAverage:
    def test_avg_correct_average(self):
        assert Calc().avg([2, 5, 12, 98]) == 29.25

    def test_avg_removes_upper_outliers(self):
        assert Calc().avg([2, 5, 12, 98], ut=90) == pytest.approx(6.33333)

    def test_avg_removes_lower_outliers(self):
        assert Calc().avg([2, 5, 12, 98], lt=10) == pytest.approx(55)

    def test_avg_empty_list(self):
        assert Calc().avg([]) is None

    def test_avg_empty_list_after_outlier_removal(self):
        assert Calc().avg([12,98], lt = 15, ut = 90) is None

    def test_avg_manage_zero_value_lower_outliers(self):
        assert Calc().avg([-1, 0, 1], lt =0 ) ==0.5
    def test_avg_manage_zero_value_higher_outliers(self):
        assert Calc().avg([-1, 0, 1], ut =0 ) == -0.5
