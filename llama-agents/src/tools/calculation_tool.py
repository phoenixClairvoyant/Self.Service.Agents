from crewai_tools import tool


@tool("Multiplication Tool")
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b

@tool("Addition Tool")
def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b

