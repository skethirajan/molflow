"""Tests for molflow."""

from __future__ import annotations

import molflow


def test_version() -> None:
    """Test that version is defined."""
    assert hasattr(molflow, "__version__")
    assert isinstance(molflow.__version__, str)


def test_all_exports() -> None:
    """Test that __all__ is defined."""
    assert hasattr(molflow, "__all__")
    assert isinstance(molflow.__all__, list)
