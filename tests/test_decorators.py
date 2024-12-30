import os
from pathlib import Path

import pytest
from freezegun import freeze_time

from src.decorators import log


def test_log_output_to_console(capsys):
    @freeze_time("30.12.24 09:55:54.150358")
    @log()
    def func(a, b):
        if b == 0:
            raise ValueError("Делить на ноль нельзя")
        else:
            return a / b

    func(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "func error Делить на ноль нельзя. Inputs: (1, 0) {}\n"
    func(1, 1)
    captured = capsys.readouterr()
    assert (
        captured.out == "func ok\n"
        "Start dade and time: 30.12.24 09:55:54.150358\n"
        "Stop dade and time: 30.12.24 09:55:54.150358\n"
        "Time for work: 0:00:00 сек\n"
    )


def test_log_output_to_file():
    @freeze_time("30.12.24 09:55:54.150358")
    @log("test_output_to_file.txt")
    def func(a, b):
        if b == 0:
            raise ValueError("Делить на ноль нельзя")
        else:
            return a / b

    func(1, 0)
    with open(
        os.path.join(Path(__file__).parent.parent, "test_output_to_file.txt"), mode="r", encoding="utf-8"
    ) as file:
        data = file.read().split("\n")
        assert data[-2] == "func error Делить на ноль нельзя. Inputs: (1, 0) {}"

    func(1, 1)
    with open(
        os.path.join(Path(__file__).parent.parent, "test_output_to_file.txt"), mode="r", encoding="utf-8"
    ) as file:
        data = file.read().split("\n")
        assert data[-2] == "Time for work: 0:00:00 сек"


def test_log_error_1():
    with pytest.raises(ValueError):

        @log("filename")
        def func(a, b):
            if b == 0:
                raise ValueError("Делить на ноль нельзя")
            else:
                return a / b

        func(1, 2)


def test_log_error_2():
    with pytest.raises(ValueError):

        @log("filename")
        def func(a, b):
            if b == 0:
                raise ValueError("Делить на ноль нельзя")
            else:
                return a / b

        func(1, 0)
