import pytest
from state import (
    make_counter, make_accumulator, make_history_counter,
    make_adder, make_minmax_tracker, make_two_way_counter
)


class TestMakeCounter:
    def test_basic(self):
        c = make_counter()
        assert c() == 1
        assert c() == 2
        assert c() == 3

    def test_start(self):
        c = make_counter(start=10)
        assert c() == 11
        assert c() == 12

    def test_step(self):
        c = make_counter(step=5)
        assert c() == 5
        assert c() == 10

    def test_start_and_step(self):
        c = make_counter(start=10, step=5)
        assert c() == 15
        assert c() == 20

    def test_independent(self):
        a = make_counter()
        b = make_counter()
        a()
        a()
        assert a() == 3
        assert b() == 1


class TestMakeAccumulator:
    def test_basic(self):
        acc = make_accumulator(5)
        assert acc(10) == 15
        assert acc(10) == 25

    def test_default_initial(self):
        acc = make_accumulator()
        assert acc(3) == 3
        assert acc(3) == 6

    def test_negative(self):
        acc = make_accumulator(20)
        assert acc(-5) == 15
        assert acc(0) == 15

    def test_independent(self):
        a = make_accumulator(0)
        b = make_accumulator(0)
        a(10)
        assert b(1) == 1


class TestMakeHistoryCounter:
    def test_basic(self):
        tick, history = make_history_counter()
        tick()
        tick()
        tick()
        assert history() == [1, 2, 3]

    def test_history_grows(self):
        tick, history = make_history_counter()
        tick()
        assert history() == [1]
        tick()
        assert history() == [1, 2]

    def test_history_is_copy(self):
        tick, history = make_history_counter()
        tick()
        h = history()
        h.append(999)
        assert history() == [1]

    def test_independent(self):
        tick1, history1 = make_history_counter()
        tick2, history2 = make_history_counter()
        tick1()
        tick1()
        tick2()
        assert history1() == [1, 2]
        assert history2() == [1]


class TestMakeAdder:
    def test_basic(self):
        add, reset = make_adder()
        assert add(5) == 5
        assert add(3) == 8
        assert add(2) == 10

    def test_reset(self):
        add, reset = make_adder()
        add(5)
        add(3)
        reset()
        assert add(1) == 1

    def test_independent(self):
        add1, reset1 = make_adder()
        add2, reset2 = make_adder()
        add1(10)
        assert add2(1) == 1


class TestMakeMinmaxTracker:
    def test_basic(self):
        track = make_minmax_tracker()
        assert track(5) == (5, 5)
        assert track(2) == (2, 5)
        assert track(9) == (2, 9)
        assert track(3) == (2, 9)

    def test_no_arg(self):
        track = make_minmax_tracker()
        track(5)
        track(2)
        assert track() == (2, 5)

    def test_single_value(self):
        track = make_minmax_tracker()
        assert track(42) == (42, 42)

    def test_independent(self):
        t1 = make_minmax_tracker()
        t2 = make_minmax_tracker()
        t1(100)
        assert t2(1) == (1, 1)


class TestMakeTwoWayCounter:
    def test_initial(self):
        up, down, value = make_two_way_counter()
        assert value() == 0

    def test_up(self):
        up, down, value = make_two_way_counter()
        up()
        up()
        up()
        assert value() == 3

    def test_down(self):
        up, down, value = make_two_way_counter()
        up()
        up()
        down()
        assert value() == 1

    def test_negative(self):
        up, down, value = make_two_way_counter()
        down()
        down()
        assert value() == -2

    def test_independent(self):
        up1, down1, value1 = make_two_way_counter()
        up2, down2, value2 = make_two_way_counter()
        up1()
        up1()
        assert value2() == 0
