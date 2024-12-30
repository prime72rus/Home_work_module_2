import os
from datetime import datetime
from functools import wraps
from pathlib import Path
from typing import Any, Callable


def log(filename: str = "") -> Callable[[Any], Any]:
    def log_wrapper(function: Callable[[Any], Any]) -> Any:
        @wraps(function)
        def log_inner(*args: Any, **kwargs: Any) -> Any:
            try:
                start_datetime = datetime.now()
                result = function(*args, **kwargs)
                stop_datetime = datetime.now()
                time_delta = stop_datetime - start_datetime
            except Exception as error_type:
                if filename == "":
                    print(f"{function.__name__} error {error_type}. Inputs: {args} {kwargs}")
                elif filename.split(".").pop() == "txt":
                    with open(
                        os.path.join(Path(__file__).parent.parent, filename), mode="a", encoding="utf-8"
                    ) as log_file:
                        log_file.write(f"{function.__name__} error {error_type}. Inputs: {args} {kwargs}\n")
                else:
                    raise ValueError("Неверное имя или расширение файла")
            else:
                if filename == "":
                    print(f"{function.__name__} ok")
                    print(f"Start dade and time: {start_datetime.strftime("%d.%m.%y %H:%M:%S.%f")}")
                    print(f"Stop dade and time: {stop_datetime.strftime("%d.%m.%y %H:%M:%S.%f")}")
                    print(f"Time for work: {time_delta} сек")
                elif filename.split(".").pop() == "txt":
                    with open(
                        os.path.join(Path(__file__).parent.parent, filename), mode="a", encoding="utf-8"
                    ) as log_file:
                        log_file.write(f"{function.__name__} ok\n")
                        log_file.write(f"Start dade and time: {start_datetime.strftime("%d.%m.%y %H:%M:%S.%f\n")}")
                        log_file.write(f"Stop dade and time: {stop_datetime.strftime("%d.%m.%y %H:%M:%S.%f\n")}")
                        log_file.write(f"Time for work: {time_delta} сек\n")
                else:
                    raise ValueError("Неверное имя или расширение файла")
                return result

        return log_inner

    return log_wrapper
