# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
# ]
# ///

from pathlib import Path
from typing import Final

import requests


_SOURCE_FILE_URL: Final = \
	'https://raw.githubusercontent.com/astral-sh/ruff/HEAD/crates/ty_vendored/ty_extensions/ty_extensions.pyi'

_PROJECT_ROOT: Final = Path(__file__).parent
_TY_EXTENSIONS_PYI: Final = _PROJECT_ROOT / 'src' / 'ty_extensions' / '__init__.pyi'


def main() -> None:
	new_file_content = requests.get(_SOURCE_FILE_URL).text
	_TY_EXTENSIONS_PYI.write_text(new_file_content, encoding = 'utf-8')


if __name__ == '__main__':
	main()
