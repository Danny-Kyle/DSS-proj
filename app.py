from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    def decision_support_system(stock_price):
        if stock_price > 100:
            decision = "Sell"
        else:
            decision = "Buy"

        return decision
    # Test with different stock prices
    # stock_prices = [120, 80, 150, 90, 110]

    # for price in stock_prices:
    # recommendation = decision_support_system(price)
    # print(f"Stock Price: {price}, Recommendation: {recommendation}")
    if request.method == 'POST':
        # Handle user input and process it with the DSS logic
        # Retrieve the user's input from the request.form dictionary
        # Perform the necessary computations and generate a recommendation
        # Return the recommendation or display it on the page
        stock_price = float(request.form.get('stock_price'))
        recommendation = decision_support_system(stock_price)
        return render_template('index.html', recommendation=recommendation)

    # Render the HTML template for the home page
    return render_template('index.html')

# Rest of the code
if __name__ == '__main__':
    app.run(debug=True)
