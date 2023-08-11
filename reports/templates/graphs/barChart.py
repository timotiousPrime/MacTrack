from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.transform import factor_cmap
from bokeh.palettes import Bright6
from bokeh.embed import components
import math

def get_graph_components(x_axis_list, y_axis_list):
    script, div = None, None
    # Raise a try/ except incase there's any issue with the data we provided
    try:

        source = ColumnDataSource(
            data=dict(
                x_axis_list=x_axis_list, 
                y_axis_list=y_axis_list
            )
        )
        plot = figure(
            sizing_mode="stretch_width", 
            x_range=x_axis_list, 
            height=300, 
            toolbar_location=None, 
            title="Job Times"
        )

        # Style the graph
        plot.title.align = "center"
        plot.title.text_font_size = "1.5em"
        plot.xaxis.major_label_orientation = math.pi / 4

        plot.vbar(x="x_axis_list",
            top="y_axis_list",
            width=0.4,
            source=source,
            )

        script, div = components(plot)

    except Exception as e:
        print(e)


    return (script, div)