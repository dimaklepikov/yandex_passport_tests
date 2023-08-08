# Sample UI tests for [Yandex Passport](https://passport.yandex.ru/)

## Test cases - [Google Docs](https://docs.google.com/document/d/1-6izc_yIUNymeoYirEasshHp9b0Mk3iC6OT3u8_T4e8/edit?usp=sharing)

## How to run project:
- `git clone `
- `conda create -n env name python=3.10`
- `conda activate env`
-  Set up env variables  - `LOGIN, PASSWORD`
- `pip install poetry` ([Poetry docs](https://python-poetry.org/docs/))
- `poetry install`  
- `pytest -m auth --html=report.html`

## Features:
 - Tests might be run in parallel `pytest -n 4 -m auth`
 - config file might be set up and parsed `config.ini`