# Contributing to stable-worldmodel

Thank you for your interest in contributing to stable-worldmodel! We welcome contributions from the community.

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/hpenedones/stable-worldmodel.git
cd stable-worldmodel
```

2. Set up your development environment:
```bash
uv venv --python=3.10
source .venv/bin/activate
uv sync --all-extras --group dev
```

3. Install pre-commit hooks:
```bash
uv run pre-commit install
```

## Making Changes

1. Create a new branch for your changes:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes following the code style guidelines below.

3. Run tests to ensure everything works:
```bash
uv run --group dev pytest
```

4. Run the linter and formatter:
```bash
uv run ruff check .
uv run ruff format .
```

## Code Style

- We use [Ruff](https://github.com/astral-sh/ruff) for linting and formatting
- Follow Google-style docstrings
- Line length: 79 characters
- Use single quotes for strings
- Add type hints to all function signatures

## Testing

- Write tests for new features and bug fixes
- Place tests in the `tests/` directory mirroring the source structure
- Use pytest for all tests
- Aim for meaningful test coverage, especially for core functionality

## Pull Request Process

1. Update documentation if you're adding or changing features
2. Ensure all tests pass
3. Update the docstrings and type hints as needed
4. Create a pull request with a clear description of your changes
5. Link any relevant issues in your pull request description

## Code of Conduct

Please note that this project follows a Code of Conduct. By participating, you are expected to uphold this code.

## Questions?

If you have questions, please [file an issue](https://github.com/hpenedones/stable-worldmodel/issues) or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
