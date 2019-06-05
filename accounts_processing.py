import sys
from urllib import request as req
import json


class FinancialStructure():

    def __init__(self, baseurl, tickers, structure, accounts):
        self.baseurl = baseurl
        self.tickers = tickers
        self.structure = structure
        self.accounts = accounts

    def loadJsonResponse(self, url):
        """ Handle json request
        """
        return json.load(req.urlopen(url))

    def getSupportedTickers(self, index):
        """ get all given supported tickers
        """
        url = self.baseurl + self.tickers
        return self.loadJsonResponse(url)["supported companies"][index]

    def getCompFinStruct(self, index):
        """ return the financial structure from a specified company ticker
        """
        company = self.getSupportedTickers(index).lower()
        fin_struct = self.loadJsonResponse(
            self.baseurl + self.structure + f'{company}')[company]['core']
        return fin_struct

    def iterateJson(self, iterable, accounts):
        """Returns an iterator that returns an account value
        of a (nested) iterable from a given list of accounts.
        Arguments:
            - iterable: <list> or <dictionary>
            - returned: account "value"
        Returns:
            - <iterator>
        """
        accounts = self.accounts
        
        if isinstance(iterable, dict):
            for key, value in iterable.items():
                for account in accounts:
                    if key == account:
                        if not (isinstance(value, dict) or isinstance(value, list)):
                            if isinstance(value, (int, float)):
                                yield value
                                break
                            else:
                                raise ValueError(
                                    "The returned account value is neither an integer nor a float'.")
                for acc in self.iterateJson(value, accounts=accounts):
                    if isinstance(acc, (int, float)):
                        yield acc
                        break
                    else:
                        raise ValueError(
                            "The returned account value is neither an integer nor a float'."
                        )
        elif isinstance(iterable, list):
            for el in iterable:
                for acc in self.iterateJson(el, accounts=accounts):
                    yield acc

    def getAccountValue(self, index, accounts):
        accounts = self.accounts
        try:
            result = str(list(self.iterateJson(self.getCompFinStruct(index), accounts))[0])
            return result
        except IndexError:
            result = "The returned account doesn't hold any value. Please try again with another set of accounts"
            return result
        return False
