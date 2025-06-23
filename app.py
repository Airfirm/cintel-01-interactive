import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add page options for the overall app.
ui.page_opts(title="PyShiny App with plot", fillable=True)

# create a sidebar with a slider input
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)


@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():
    # Define the number of points to generate. Use optional type hinting to indicate this is an integer.
    count_of_points: int = 437
    # set a random seed to ensure reproductivity.
    np.random.seed(3)
    # generate random data:
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    # create a histogram of the random data using matplotlib's hist() function:
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True)
