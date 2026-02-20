"""Utility functions for data management.

This module provides helper functions for managing cache directories and
other data-related utilities.
"""

import os
from pathlib import Path


def get_cache_dir() -> Path:
    """Get the cache directory for stable_worldmodel data."""
    cache_dir = os.getenv("STABLEWM_HOME", os.path.expanduser("~/.stable_worldmodel"))
    os.makedirs(cache_dir, exist_ok=True)
    return Path(cache_dir)
