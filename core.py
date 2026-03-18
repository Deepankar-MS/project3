"""Core functionality for project3."""

from project2 import enhanced_greet


def super_greet(name: str) -> str:
    """Return a super greeting using project2."""
    enhanced = enhanced_greet(name)
    return f"{enhanced} Supercharged by project3!"
