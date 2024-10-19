# aesop

personalized and accessible storytelling

## setup environment

```bash
# create virtual environment
pip install uv
uv venv

# activate virtual environment
source .venv/bin/activate   # mac/linux
.venv\Scripts\activate      # windows

# download all requirements.txt
uv pip install -r requirements.txt

# add package
uv pip install <package-name>
uv pip freeze > requirements.txt

# remove package
uv pip uninstall <package-name>
uv pip freeze > requirements.txt
```
