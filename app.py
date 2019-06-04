from flask import Flask, request, render_template
from accounts_processing import FinancialStructure


app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['TESTING'] = True


@app.route("/", methods=['GET'])
def index():
    """Home page."""
    return render_template('index.html')


@app.route('/accounts/')
def accounts():
    data = {
        'baseurl': 'https://tech-test-api.valsys.io',
        'tickers': '/tickers',
        'structure': '/structure?ticker=',
        'index': 1,
        'accounts': ["IncomeStatement", "EarningsPerShare",
                     "DividendsDeclaredPerCommonShare"]
    }
    fs = FinancialStructure(
        data['baseurl'], data['tickers'], data['structure'], data['accounts'])
    result = fs.getAccountValue(data['index'], data['accounts'])
    account_name = data['accounts'][-1]
    response = account_name + ': ' + str(result)
    return render_template('accounts.html', result=response)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
