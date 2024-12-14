# Installation Guide

This guide will walk you through the process of setting up RightHome.ai on your local machine.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/RightHome.git
cd RightHome
```

### 2. Set Up Virtual Environment

#### On macOS/Linux:
```bash
python3 -m venv env
source env/bin/activate
```

#### On Windows:
```bash
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages:
- streamlit
- plotly
- pandas
- numpy
- pydantic

### 4. Run the Application

```bash
python -m streamlit run src/app.py
```

## Verification

To verify your installation:

1. Activate your virtual environment (if not already activated)
2. Run the application:
```bash
python -m streamlit run src/app.py
```
3. Open your browser to the URL shown in the terminal (usually http://localhost:8501)

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**
   - Solution: Ensure you're in the virtual environment and have run `pip install -r requirements.txt`

2. **Streamlit Command Not Found**
   - Solution: Ensure streamlit is installed: `pip install streamlit`

3. **Import Errors**
   - Solution: Check that your Python path includes the project root directory

### Getting Help

If you encounter any issues:
1. Check the error message in the terminal
2. Refer to the project's GitHub Issues page
3. Contact the development team

## Next Steps

After installation:
1. Read the [User Guide](user_guide.md)
2. Explore the [API Documentation](api.md)
3. Check out [Contributing Guidelines](contributing.md)
