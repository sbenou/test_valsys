import unittest
import pytest
import requests
import requests_mock
import json


class TestHTTPRequest(unittest.TestCase):
    def test_context_manager(self):
        with requests_mock.Mocker() as mock_request:
            mock_request.get("https://tech-test-api.valsys.io", text="Hi there! Welcome to the Valsys tech test landing page - we hope you have fun with the task! :)")
            response = requests.get("https://tech-test-api.valsys.io")

        assert response.text == "Hi there! Welcome to the Valsys tech test landing page - we hope you have fun with the task! :)"


@pytest.fixture
def base_url():
    return "https://tech-test-api.valsys.io"

@pytest.fixture
def given_index():
    return 1


accounts = ["IncomeStatement", "EarningsPerShare",
            "EarningsFromContinuingOperationsPerCommonShareBasic"]


@pytest.mark.parametrize("company, structure, tickers, accounts", "SBUX", "/structure?ticker={SBUX}", "/tickers", ["IncomeStatement", "EarningsPerShare",
            "EarningsFromContinuingOperationsPerCommonShareBasic"])
def test_list_valid_company(base_url, given_index, company, structure, tickers, accounts):
	url = base_url + "/structure?ticker={SBUX}" + structure
	resp = requests.get(url)
	j = json.loads(resp.text)
	assert resp.status_code == 200, resp.text
	assert j == "SBUX"


def test_SupportedTickers_valid_tickers(base_url, given_index):
	url = base_url + '/tickers' 
	resp = requests.get(url)["supported companies"][given_index]
	j = json.loads(resp.text)
	assert resp.status_code == 200, resp.text
	assert j['tickers'] == "/tickers", resp.text

def test_SupportedTickers_no_index(base_url):
	url = base_url + "" 
	resp = requests.get(url)["supported companies"][given_index]
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.text
	assert j['error'] == "Index not provided", resp.text

def test_SupportedTickers_no_tickers(base_url, given_index):
	url = base_url + "" 
	resp = requests.get(url)["supported companies"][given_index]
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.text
	assert j['error'] == "Tickers not provided", resp.text

def test_CompFinStruct_no_company(base_url, given_index):
	url = base_url
	company = ""
	fin_struct = requests.get(
		base_url + "" + f'{company}')[company]['core']
	resp = fin_struct
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.text
	assert j['error'] == "Missing structure", resp.text

def test_CompFinStruct_no_struct(base_url, given_index):
	url = base_url
	company = "SBUX"
	fin_struct = requests.get(
		base_url + "" + f'{company}')[company]['core']
	resp = fin_struct
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.text
	assert j['error'] == "Missing structure", resp.text

def test_CompFinStruct_valid_struct_and_company(base_url, given_index):
	url = base_url
	company = "SBUX"
	fin_struct = requests.get(
		base_url + '/tickers' + f'{company}')[company]['core']
	resp = fin_struct
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.text
	assert j['error'] == "Missing structure", resp.text

def test_iterateJson_valid(iterable, accounts):
	accounts = accounts
	if isinstance(iterable, dict):
		for key, value in iterable.items():
			for account in accounts:
				if key == account:
					if not (isinstance(value, dict) or isinstance(value, list)):
						if isinstance(value, int):
							yield value
							break
						else:
							raise ValueError(
								"The returned account value is not an integer'.")
			for acc in test_iterateJson_valid(value, accounts=accounts):
				if isinstance(acc, int):
					yield acc
					break
	elif isinstance(iterable, list):
		for el in iterable:
			for acc in test_iterateJson_valid(el, accounts=accounts):
				yield acc
	resp = acc
	j = json.loads(resp.text)
	assert resp.status_code == 200, resp.text
	assert j == 78, resp.text

def test_getAccountValue_valid(self, index, accounts):
	url = base_url
	company = "SBUX"
	fin_struct = requests.get(
		base_url + "" + f'{company}')[company]['core']
	fs = fin_struct
	resp = str(list(test_getAccountValue_valid(fs))[0])
	j = json.loads(resp.text)
	assert resp.status_code == 200, resp.text
	assert j == 78, resp.text



if __name__ == '__main__':
	unittest.main()