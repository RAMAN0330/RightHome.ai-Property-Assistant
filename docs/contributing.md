# Contributing to RightHome.ai

Thank you for your interest in contributing to RightHome.ai! This document provides guidelines and instructions for contributing to the project.

## Table of Contents
1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Process](#development-process)
4. [Pull Request Process](#pull-request-process)
5. [Style Guidelines](#style-guidelines)
6. [Testing](#testing)
7. [Documentation](#documentation)

## Code of Conduct

### Our Pledge
We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards
- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other community members

## Getting Started

### Prerequisites
1. Python 3.8 or higher
2. Git
3. Virtual environment tool
4. IDE (VS Code recommended)

### Setup Development Environment
1. Fork the repository
2. Clone your fork:
```bash
git clone https://github.com/yourusername/RightHome.git
cd RightHome
```

3. Set up virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Set up pre-commit hooks:
```bash
pre-commit install
```

## Development Process

### Branches
- `main`: Production-ready code
- `develop`: Development branch
- Feature branches: `feature/your-feature-name`
- Bug fix branches: `fix/bug-description`

### Workflow
1. Create a new branch from `develop`
2. Make your changes
3. Write/update tests
4. Update documentation
5. Submit a pull request

### Commit Messages
Follow conventional commits:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test updates
- `chore`: Maintenance tasks

Example:
```
feat(property-analysis): add new scoring algorithm

- Implemented weighted scoring
- Added unit tests
- Updated documentation
```

## Pull Request Process

1. **Before Submitting**
   - Update documentation
   - Add/update tests
   - Run all tests locally
   - Format code according to style guide
   - Resolve merge conflicts

2. **PR Template**
   ```markdown
   ## Description
   [Description of changes]

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update

   ## Testing
   - [ ] Unit tests added/updated
   - [ ] Integration tests added/updated
   - [ ] Manual testing performed

   ## Documentation
   - [ ] README updated
   - [ ] API docs updated
   - [ ] Comments added/updated
   ```

3. **Review Process**
   - At least one maintainer review required
   - Address all review comments
   - Pass all CI checks

## Style Guidelines

### Python Code Style
- Follow PEP 8
- Use type hints
- Maximum line length: 88 characters
- Use descriptive variable names
- Document all public functions/methods

### Example
```python
from typing import Dict, List

def analyze_property(
    property_data: Dict[str, Any],
    weights: Dict[str, float]
) -> Dict[str, float]:
    """
    Analyze property based on given weights.

    Args:
        property_data: Property information dictionary
        weights: Feature importance weights

    Returns:
        Dictionary containing analysis scores
    """
    # Implementation
```

### Documentation Style
- Use Google-style docstrings
- Include examples in docstrings
- Keep documentation up-to-date
- Write clear commit messages

## Testing

### Test Structure
```
tests/
├── unit/
│   ├── test_property_bot.py
│   └── test_visualizer.py
├── integration/
│   └── test_analysis_chain.py
└── conftest.py
```

### Writing Tests
```python
import pytest
from src.chatbot.property_bot import PropertyBot

def test_property_analysis():
    """Test property analysis with valid input."""
    bot = PropertyBot()
    result = bot.analyze_property(valid_property_data)
    assert "score" in result
    assert 0 <= result["score"] <= 100
```

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_property_bot.py

# Run with coverage
pytest --cov=src tests/
```

## Documentation

### API Documentation
- Document all public APIs
- Include type hints
- Provide usage examples
- Document exceptions

### Code Comments
- Explain complex algorithms
- Document assumptions
- Note potential issues
- Include references

### README Updates
- Keep installation instructions current
- Document new features
- Update troubleshooting guide
- Maintain changelog

## Release Process

1. **Version Bump**
   - Update version in `setup.py`
   - Update CHANGELOG.md
   - Create release branch

2. **Testing**
   - Run full test suite
   - Perform manual testing
   - Check documentation

3. **Release**
   - Merge to main
   - Create GitHub release
   - Update documentation

## Security
- Validate user inputs
- Implement rate limiting
- Follow security best practices
- Keep dependencies updated

## Questions?

- Open an issue for bugs
- Use discussions for questions
- Join our community chat
- Contact maintainers directly

Thank you for contributing to RightHome.ai!
