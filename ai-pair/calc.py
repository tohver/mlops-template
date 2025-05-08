#!/usr/bin/env python3
"""
Module to create calculation functions for the AI Pair project: addition, subtraction,
multiplication, and division.
The module will also be invoked to as a command line script using  click.
"""

import click

def add(a, b):
    """
    Function to add two numbers.
    
    Args:
        a (int, float): First number.
        b (int, float): Second number.
    
    Returns:
        int, float: Sum of a and b.
    """
    return a + b
def subtract(a, b):
    """
    Function to subtract two numbers.
    """
    return a - b
def multiply(a, b):
    """
    Function to multiply two numbers.
    """
    return a * b
def divide(a, b):
    """
    Function to divide two numbers.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


#build a click group
@click.group()
def cli():
    """
    Command line interface for the calculator.
    """
    pass

# build a click command
@cli.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)

def add_command(a, b):
    """
    Command line interface for addition.
    """
    # Invoke the function with colored output from click. 
    click.echo(click.style(f"The result of adding {a} and {b} is: {add(a,b)}", fg="green"))

@cli.command("subtract")
@click.argument("a", type=int)
@click.argument("b", type=int)
def subtract_command(a, b):
    """
    Command line interface for subtraction.
    """
    result = subtract(a, b)
    click.echo(f"The result of subtracting {b} from {a} is: {result}")

@cli.command("multiply")
@click.argument("a", type=int)
@click.argument("b", type=int)  
def multiply_command(a, b):
    """
    Command line interface for multiplication.
    """
    result = multiply(a, b)
    click.echo(f"The result of multiplying {a} and {b} is: {result}")

@cli.command("divide")
@click.argument("a", type=int)
@click.argument("b", type=int)  
def divide_command(a, b):
    """
    Command line interface for division.
    """
    try:
        result = divide(a, b)
        click.echo(f"The result of dividing {a} by {b} is: {result}")
    except ValueError as e:
        click.echo(e)

if __name__ == "__main__":  
    cli()










# def calculate(a, b, operation):
#     """
#     Function to perform a calculation based on the operation provided.   
#     """
#     if operation == 'add':
#         return add(a, b)
#     elif operation == 'subtract':
#         return subtract(a, b)
#     elif operation == 'multiply':
#         return multiply(a, b)
#     elif operation == 'divide':
#         return divide(a, b)
#     else:
#         raise ValueError("Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'.")
# def main():
#     """
#     Main function to test the calculation functions.
#     """
#     a = 10
#     b = 5
#     print(f"Addition: {calculate(a, b, 'add')}")
#     print(f"Subtraction: {calculate(a, b, 'subtract')}")
#     print(f"Multiplication: {calculate(a, b, 'multiply')}")
#     print(f"Division: {calculate(a, b, 'divide')}")
# if __name__ == "__main__":
#     main()
# # This code is part of the AI Pair project and is licensed under the MIT License.
