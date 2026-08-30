# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
# ]
# ///

from pathlib import Path
from typing import Final

import requests


_BASE_URL: Final = 'https://raw.githubusercontent.com/astral-sh/ruff/HEAD/crates/ty_vendored/ty_extensions/'
_FILE_NAMES: Final = [
	'__init__.pyi',
	'_internal.pyi',
	'pydantic.pyi',
]

_PROJECT_ROOT: Final = Path(__file__).parent
_PACKAGE: Final = _PROJECT_ROOT / 'src' / 'ty_extensions'


def main() -> None:
	for file_name in _FILE_NAMES:
		url = f'{_BASE_URL}/{file_name}'

		new_file_content = requests.get(url).text
		(_PACKAGE / file_name).write_text(new_file_content, encoding = 'utf-8')


if __name__ == '__main__':
	main()
