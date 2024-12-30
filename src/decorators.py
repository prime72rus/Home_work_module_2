import os
from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str = "") -> Callable[[Any], Any]:
    def log_wrapper(function: Callable[[Any], Any]) -> Any:
        @wraps(function)
        def log_inner(*args: Any, **kwargs: Any) -> Any:
            try:
                time_begin = datetime.now()
                result = function(*args, **kwargs)
                time_end = datetime.now()
                time_delta = time_end - time_begin
            except Exception as error_type:
                if filename == "":
                    print(f"{function.__name__} error {error_type}. Inputs: {args} {kwargs}")
                elif filename.split(".").pop() == "txt":
                    with open(
                        os.path.join(os.path.dirname(__file__), filename), mode="a", encoding="utf-8"
                    ) as log_file:
                        log_file.write(f"{function.__name__} error {error_type}. Inputs: {args} {kwargs}\n")
                else:
                    raise ValueError("Неверное имя или расширение файла")
            else:
                if filename == "":
                    print(f"{function.__name__} ok")
                    print(f"Time of start: {time_begin.strftime("%d.%m.%y %H:%M:%S.%f")}")
                    print(f"Time of end: {time_end.strftime("%d.%m.%y %H:%M:%S.%f")}")
                    print(f"Time for work: {time_delta} сек")
                elif filename.split(".").pop() == "txt":
                    with open(
                        os.path.join(os.path.dirname(__file__), filename), mode="a", encoding="utf-8"
                    ) as log_file:
                        log_file.write(f"{function.__name__} ok\n")
                        log_file.write(f"Time of start: {time_begin.strftime("%d.%m.%y %H:%M:%S.%f\n")}")
                        log_file.write(f"Time of end: {time_end.strftime("%d.%m.%y %H:%M:%S.%f\n")}")
                        log_file.write(f"Time for work: {time_delta} сек\n")
                else:
                    raise ValueError("Неверное имя или расширение файла")
                return result

        return log_inner

    return log_wrapper
