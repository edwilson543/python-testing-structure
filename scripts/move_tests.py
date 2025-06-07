import pathlib
import typing


SRC = pathlib.Path(__file__).parents[1] / "src"
INTEGRATION_TESTS = SRC.parent / "tests" / "integration"


def collect_test_files() -> typing.Generator[pathlib.Path]:
    for path in SRC.rglob("test_*"):
        if path.is_file():
            yield path


def move_test_file_to_dedicated_package(path: pathlib.Path) -> None:
    relative_path = path.relative_to(SRC)

    new_location = _maybe_remove_tests_part_of_path(INTEGRATION_TESTS / relative_path)
    new_location.parent.mkdir(parents=True, exist_ok=True)

    path.rename(new_location)


def create_init_files(directory: pathlib.Path) -> None:
    for path in directory.rglob("*"):
        if path.is_dir():
            init_filepath = path / "__init__.py"
            init_filepath.touch()


def _maybe_remove_tests_part_of_path(path: pathlib.Path) -> pathlib.Path:
    """
    Convert e.g. `src/foo/tests/test_something.py` to `src/foo/test_something.py`.
    """
    relative_path = path.relative_to(INTEGRATION_TESTS)
    relative_path_less_tests = [part for part in relative_path.parts if part != "tests"]
    return INTEGRATION_TESTS / pathlib.Path(*relative_path_less_tests)


if __name__ == "__main__":
    for test_filepath in collect_test_files():
        move_test_file_to_dedicated_package(test_filepath)
    create_init_files(INTEGRATION_TESTS)
