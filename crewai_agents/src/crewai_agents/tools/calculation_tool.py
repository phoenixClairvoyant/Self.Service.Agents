from llama_index.core.tools import FunctionTool




def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b


def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b


# Create a FunctionTool from the multiply function
multiplier = FunctionTool.from_defaults(fn=multiply)
addition = FunctionTool.from_defaults(fn=add)