import platform
import os
import subprocess


def open_external(filepath: str) -> None:
    """Open an external file with the default software.
    Args:
        filepath (str): The file path to open
    """
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))
