import os
from flask import Flask, request, render_template
from accounts_processing import FinancialStructure
import json


app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['TESTING'] = True


@app.route("/", methods=['GET'])
def index():
    """Home page."""
    return render_template('index.html')


@app.route('/accounts/')
def accounts():
    error = None

    # start one off settings: we assume here that a json file with params details would exist and be provided
    # the idea is changes in accounts for testing purposes are made in the params.json to see what happen ...
    params = {
        'baseurl': 'https://tech-test-api.valsys.io',
        'tickers': '/tickers',
        'structure': '/structure?ticker=',
        'index': 1,
        'accounts': ["IncomeStatement", "EarningsPerShare",
                    "DividendsDeclaredPerCommonShare"]
    }

    path = './params.json'
    if not os.path.exists(path):
        with open('./params.json', 'w') as f:
            f.write(json.dumps(params))
    # end of one off settings


    with open(path, 'r') as jfile:
        data = json.load(jfile)
        print(data)

    fs = FinancialStructure(
        data['baseurl'], data['tickers'], data['structure'], data['accounts'])
    result = fs.getAccountValue(data['index'], data['accounts'])
    account_name = data['accounts'][-1]
    try:
        response = account_name + ': ' + str(result)
    except IndexError:
        error = "An error has occured", 500
        return render_template('index.html', error=error)
    return render_template('accounts.html', result=response, error=error)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
