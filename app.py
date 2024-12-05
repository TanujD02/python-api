from flask import Flask, request, jsonify, render_template
from graphs import get_kpi_values, bar_chart, pie_chart, categorical_bar_chart, product_table, line_chart, bubble_chart  # Import the line_chart function from graphs.py
import plotly.graph_objects as go

app = Flask(__name__)


@app.route('/')
def home():
    # Fetch the KPI values and graph HTMLs
    kpi_values = get_kpi_values()
    bar_html = line_chart()
    pie_html = pie_chart()
    cat_bar_html = categorical_bar_chart()
    table_html = product_table()
    line_html = line_chart()
    bubble_html = bubble_chart()

    # Render the home page and pass the data to the template
    return render_template('home.html', kpi_values=kpi_values,
                           bar_html=bar_html, pie_html=pie_html,
                           cat_bar_html=cat_bar_html, table_html=table_html,
                           line_html=line_html, bubble_html=bubble_html)


# Create an API route to display the graph
@app.route('/api/line-chart', methods=['GET'])
def api_line_chart():
    # Call the line_chart function and return the graph as HTML
    return line_chart()

@app.route('/api/bar-chart')
def bar_chart():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[10, 20, 30], mode='lines'))
    return fig.to_json()  # Serve Plotly figure as JSON




if __name__ == "__main__":
    app.run(debug=True, port=5000)