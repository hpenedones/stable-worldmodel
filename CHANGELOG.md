# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- CONTRIBUTING.md with development setup and contribution guidelines
- CODE_OF_CONDUCT.md based on Contributor Covenant
- SECURITY.md with vulnerability reporting instructions
- CHANGELOG.md for tracking version history
- Module docstrings to core __init__.py files
- Enhanced installation guide in README with multiple installation options
- Code coverage reporting in CI/CD pipeline
- Ruff linting enforcement in CI/CD pipeline
- Additional project classifiers and keywords in pyproject.toml

### Changed
- Updated repository URLs in pyproject.toml and README to point to fork
- Fixed pre-commit pydocstyle configuration to properly check docstrings
- Enhanced README with troubleshooting section

### Fixed
- Pre-commit pydocstyle hook exclude pattern (was excluding all files)

## [0.0.4] - 2025-02-XX

### Changed
- Conditionally include proprioceptive data in IQL/IVL dataset and model processing

## [0.0.3] - Previous Release

See git history for details on earlier versions.

[Unreleased]: https://github.com/hpenedones/stable-worldmodel/compare/v0.0.4...HEAD
[0.0.4]: https://github.com/hpenedones/stable-worldmodel/releases/tag/v0.0.4
