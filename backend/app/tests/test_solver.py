import pytest
from water_jud_riddle import Jug, JugTooSmallException, WaterJugSolver, WaterJugSolverStatus


def test_1_1_1():
    solver = WaterJugSolver(jug_x_capacity=1, jug_y_capacity=1, target_amount=1)
    result = solver.solve()

    assert result.status == WaterJugSolverStatus.FOUND
    steps = result.steps
    assert len(steps) == 2
    assert steps[0].jug_x.current_level == 0
    assert steps[0].jug_y.current_level == 0

    assert steps[1].jug_x.current_level == 1
    assert steps[1].jug_y.current_level == 0


def test_jug_too_small():
    solver = WaterJugSolver(jug_x_capacity=1, jug_y_capacity=1, target_amount=10)
    with pytest.raises(JugTooSmallException):
        solver.solve()


def test_2_4_1_not_found():
    solver = WaterJugSolver(jug_x_capacity=2, jug_y_capacity=4, target_amount=1)
    result = solver.solve()

    assert result.status == WaterJugSolverStatus.NOT_FOUND
    steps = result.steps
    assert len(steps) == 6


def test_2_5_3_not_found():
    solver = WaterJugSolver(jug_x_capacity=2, jug_y_capacity=4, target_amount=1)
    result = solver.solve()

    assert result.status == WaterJugSolverStatus.NOT_FOUND
    steps = result.steps
