import click
import numpy as np
from numpy import pi
import pandas as pd

# create a group. command 'smallangle' is linked to this function
@click.group()
def group():
    pass

@group.command()
@click.option(
    "-n",
    "--number",
    default = 10 
)
def sin(number):
    """Calculate the sinus of NUMBER amount of steps between 0 and 2pi.

    NUMBER is the amount of steps between 0 and 2pi.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@group.command()
@click.option(
    "-n",
    "--number",
    default =- 10
)
def tan(number):
    """Calculate the tangens of NUMBER amount of steps between 0 and 2pi.

    NUMBER is the amount of steps between 0 and 2pi.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    group()