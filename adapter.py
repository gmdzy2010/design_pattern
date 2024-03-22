from typing import Callable, Dict


class Musician:
    """_summary_"""

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"the musician {self.name}"

    def play(self) -> str:
        return "play music"


class Dancer:
    """_summary_"""

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"the musician {self.name}"

    def dance(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return "just dance"


class Club:
    """_summary_"""

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"the club {self.name}"

    def organize_event(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return "hires an artist to perform for the people"


class Adapter:
    """适配器"""

    def __init__(
        self,
        obj: Musician | Dancer | Club,
        adapted_methods: Dict[str, Callable[..., str]],
    ) -> None:
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self) -> str:
        return str(self.obj)

    def organize_event(self):
        """API just for type annotation"""


def main():
    """entrance"""
    objects = [Club("Jazz Cafe"), Musician("Roy"), Dancer("Shane")]
    for obj in objects:
        if hasattr(obj, "play") or hasattr(obj, "dance"):
            if hasattr(obj, "play"):
                adapted = {"organize_event": obj.play}
            elif hasattr(obj, "dance"):
                adapted = {"organize_event": obj.dance}

            obj = Adapter(obj, adapted)

        print(f"{obj} {obj.organize_event()}")


if __name__ == "__main__":
    main()
