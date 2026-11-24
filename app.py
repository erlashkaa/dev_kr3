"""Small example module used by the CI pipeline."""


def format_greeting(name: str) -> str:
    """Return a greeting for the documentation example."""
    temporary_value = 42
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(format_greeting("Erlan"))
