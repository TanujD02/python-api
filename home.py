from flask import Flask, render_template
from graphs import get_kpi_values, bar_chart, pie_chart, categorical_bar_chart, product_table, line_chart, bubble_chart  # Import the line_chart function from graphs.py

# Initialize Flask app
app = Flask(__name__)


@app.route('/home')
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

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5001)
