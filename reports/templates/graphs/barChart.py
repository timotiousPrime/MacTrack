from bokeh.models import ColumnDataSource, FactorRange, BoxZoomTool, WheelZoomTool, ResetTool, CustomJS, Select
from bokeh.plotting import figure, show 
from bokeh.transform import factor_cmap
from bokeh.layouts import column, row
from bokeh.palettes import Bright6, Spectral, Plasma
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
    
def get_stacked_graph_components(xRange, vertStack, data):
    script, div = None, None

    source = ColumnDataSource(data)


    plot = figure(
        x_range=FactorRange(*xRange), 
        height = 500, 
        sizing_mode="stretch_width",
        title="Task Times",
        toolbar_location=None,
        tools= [BoxZoomTool(), WheelZoomTool(), ResetTool()],
        # tools="hover",
        tooltips="$name: @$name")
    
    descCount = len(vertStack)
    graphColors = Plasma[descCount]
    
    plot.vbar_stack(vertStack, x="colData", width=0.9, color=graphColors, source=source, legend_label=vertStack)

    plot.y_range.start = 0
    plot.x_range.range_padding = 0.05
    plot.xaxis.major_label_orientation = math.pi/2
    plot.xgrid.grid_line_color = None
    plot.axis.minor_tick_line_color = None
    plot.outline_line_color = None
    plot.legend.location = "top_left"
    plot.legend.orientation = "horizontal"

    # Widget Settings
    select_widget = Select(title='Category:', value="All", options=['All'] + vertStack)
    # auto_complete_input = AutocompleteInput(title="Select a desceription", completions=description_list, search_strategy="includes")

    # Define a CustomJS callback to filter data based on the select widget
    callback = CustomJS(args=dict(source=source), code="""
        var data = source.data;
        var category = cb_obj.value;
        var x = data['Des'];
        var y = data['Adm'];
        var cat = data['colData'];
        console.log("x: ",cb_obj.value)
        console.log("length: ", x.length)
        for (var i = 0; i < x.length; i++) {
            if (category === "All" || category === cat[i]) {
                x[i] = x[i];
                y[i] = y[i];
            } else {
                x[i] = Number.NaN;
                y[i] = Number.NaN;
            }
        }
        source.change.emit();
    """)

    select_widget.js_on_change("value", callback)

    layout = column(select_widget, row(plot))

    script, div = components(plot, select_widget)

    return (script, div)



def get_test_stacked_graph_components(xRange, vertStack, data):
    script, div = None, None

    source = ColumnDataSource(data)


    plot = figure(
        x_range=FactorRange(*xRange), 
        height = 500, 
        sizing_mode="stretch_width",
        title="Task Times",
        toolbar_location=None,
        tools= [BoxZoomTool(), WheelZoomTool(), ResetTool()],
        # tools="hover",
        tooltips="$name: @$name")
    
    descCount = len(vertStack)
    graphColors = Plasma[descCount]
    
    plot.vbar_stack(vertStack, x="colData", width=0.9, color=graphColors, source=source, legend_label=vertStack)

    plot.y_range.start = 0
    plot.x_range.range_padding = 0.05
    plot.xaxis.major_label_orientation = math.pi/2
    plot.xgrid.grid_line_color = None
    plot.axis.minor_tick_line_color = None
    plot.outline_line_color = None
    plot.legend.location = "top_left"
    plot.legend.orientation = "horizontal"

    # Widget Settings
    select_widget = Select(title='Category:', value="All", options=['All'] + vertStack)
    # auto_complete_input = AutocompleteInput(title="Select a desceription", completions=description_list, search_strategy="includes")

    # Define a CustomJS callback to filter data based on the select widget
    callback = CustomJS(args=dict(source=source), code="""
        var data = source.data;
        var category = cb_obj.value;
        var x = data['Des'];
        var y = data['Adm'];
        var cat = data['colData'];
        console.log("data: ", data)
        console.log("length: ", x.length)
        for (var i = 0; i < x.length; i++) {
            if (category === "All" || category === cat[i]) {
                x[i] = x[i];
                y[i] = y[i];
            } else {
                x[i] = Number.NaN;
                y[i] = Number.NaN;
            }
        }
        source.change.emit();
    """)

    select_widget.js_on_change("value", callback)

    layout = column(select_widget, plot)

    script, div = components(layout)

    return (script, div)