from copy import copy
from enum import StrEnum


class Jug:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_level = 0

    def fill(self):
        self.current_level = self.capacity

    def empty(self):
        self.current_level = 0

    def is_empty(self):
        return self.current_level == 0

    def is_full(self):
        return self.current_level == self.capacity

    def transfer_to(self, other_jug: "Jug"):
        transfer_amount = min(self.current_level, other_jug.capacity - other_jug.current_level)
        self.current_level -= transfer_amount
        other_jug.current_level += transfer_amount


class WaterJugSolverStep:
    def __init__(self, jug_x: Jug, jug_y: Jug):
        self.jug_x = copy(jug_x)
        self.jug_y = copy(jug_y)


class WaterJugSolverStatus(StrEnum):
    FOUND = "FOUND"
    NOT_FOUND = "NOT_FOUND"
    ERROR = "ERROR"


class JugTooSmallException(Exception):
    def __init__(self, reason: str) -> None:
        self.reason = reason


class WaterJugResult:
    def __init__(self):
        self.steps: list[WaterJugSolverStep] = []
        self.status = WaterJugSolverStatus.NOT_FOUND

    def add_step(self, jug_x: Jug, jug_y: Jug):
        self.steps.append(WaterJugSolverStep(jug_x, jug_y))

    def error(self, reason: str):
        self.status = WaterJugSolverStatus.ERROR
        self.reason = reason
        raise JugTooSmallException(reason)

    def found(self):
        self.status = WaterJugSolverStatus.FOUND

    def not_found(self):
        self.status = WaterJugSolverStatus.NOT_FOUND

    def was_processed(self, level_x: Jug, level_y: Jug):
        query = filter(
            lambda step: step.jug_x.current_level == level_x and step.jug_y.current_level == level_y,
            self.steps,
        )
        was = next(query, False)
        return was


class WaterJugSolver:
    def __init__(self, jug_x_capacity: int, jug_y_capacity: int, target_amount: int):
        self.jug_x = Jug(jug_x_capacity)
        self.jug_y = Jug(jug_y_capacity)
        self.target_amount = target_amount

    def solve(self):
        result = WaterJugResult()
        if self.jug_x.capacity < self.target_amount and self.jug_y.capacity < self.target_amount:
            result.error(
                f"Jugs are too small to hold {self.target_amount} galons. Maximun value is {max(self.jug_x.capacity, self.jug_y.capacity)} galons"
            )

        while (
            self.jug_x.current_level != self.target_amount
            and self.jug_y.current_level != self.target_amount
            and not result.was_processed(self.jug_x.current_level, self.jug_y.current_level)
        ):
            result.add_step(self.jug_x, self.jug_y)

            # Fill jug X if it's empty
            if self.jug_x.is_empty():
                self.jug_x.fill()
            # Pour water from jug X to jug Y
            elif not self.jug_x.is_empty() and not self.jug_y.is_full():
                self.jug_x.transfer_to(self.jug_y)
            # Empty jug Y if it's full
            elif self.jug_y.is_full():
                self.jug_y.empty()

        if self.jug_x.current_level == self.target_amount or self.jug_y.current_level == self.target_amount:
            result.add_step(self.jug_x, self.jug_y)
            result.found()
        else:
            result.not_found()

        return result
