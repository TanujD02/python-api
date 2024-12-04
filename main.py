from flask import Flask, request, jsonify
from graphs import get_kpi_values, bar_chart, pie_chart, categorical_bar_chart, product_table, line_chart, bubble_chart
import plotly.graph_objects as go

app = Flask(__name__)


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