# Contents:
- [A migration script](./scripts/move_tests.py) - to move test files from source code directories to a dedicated package
- [Structure validation tests](./tests/project/test_project_structure.py) - to ensure that:
    - Tests packages mirror the project structure exactly
    - No new test files are added to source code directories accidentally

# Benefits:
- A consistent testing approach establishes the foundation for a high quality test suite and reliable software
- Reduces "where should I put my tests" decision fatigue, which is bad for productivity
- Ability to apply custom linting rules for tests (e.g. stop `mypy` forcing you to annotate every test's return 
type as `None`, which wastes time)
- Easier to exclude tests from production builds (e.g. Docker images)
- Tests are easier to find - you can search for the file `foo/test_some_code.py`

For example, given a project with the following structure:
```text
root/
    src/
        proj/
            foo/
                some_code.py
                test_some_code.py
            bar/
                some_more_code.py
                tests/
                    test_some_more_code.py
```

Convert it to the following:
```text
root/
    src/
        proj/
            foo/
                some_code.py
            bar/
                some_more_code.py
    tests/
        integration/ # Or whatever the existing tests are.
            proj/
                foo/
                    test_some_code.py
                bar/
                    test_some_more_code.py
```

And then pin / burndown to this structure using the tests in [test_project_structure.py](./tests/project/test_project_structure.py)
