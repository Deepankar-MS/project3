"""Core functionality for proj3."""

from proj2 import enhanced_greet


def super_greet(name: str) -> str:
    """Return a super greeting using proj2."""
    enhanced = enhanced_greet(name)
    return f"{enhanced} Supercharged by proj3!"
