# Valsys Tech Test

Hi there! Thanks for taking the time to do our test, we really appreciate it. If you have any questions or find the test unclear then don’t hesitate to contact us.

## Task

We frequently have to structure convoluted data structures and relationships, turning them into queryable
objects. One example of this is parsing a company’s financial structure when creating a valuation model. Using
our test API, create an application that allows a user to specify a company ticker and property - your application
should return the total sum of all child properties.

## API Overview

```bash
base_url = https://tech-test-api.valsys.io
```

This will return a list supported tickers.

```bash
/tickers
```

This returns the specified company’s financial structure, this is the object to parse.

```bash
/structure?ticker={}
```

## Requirements

Spend as much time as you’d like on the given task. The app should be written in Python 3, use any and as
many frameworks/libraries you would like, just make sure to include them in a requirements.txt file. The app
should run either as an API or CLI. Your code should run in one step. Please include a readme with any
information you’d like us to know, improvements you would make to your implementation (if any) and changes
you would make to the test itself (if any). Please enure the readme file is easy to find!

## User story

As a user:

I can specify a company ticker and property So that I can view the specified property and the sum of all it’s child properties

## Submission

Please create a new repository for your code submission and commit as you build. Once you are finished,
please send the link to your repository to your contact at Valsys.

## FAQ

> What is a property ?

Look through the API responses and play with the JSON structure. A property is any item in the JSON, for our
use case, it’s any financial item.

> Which of the properties can be taken as input to my application?

Using this JSON blob as a proxy:

```JSON
{"sbux":
    {"core":
        [{"IncomeStatement":
            {"common":
                [{"EarningsPerShare":
                    {"line items":
                        {"DividendsDeclaredPerCommonShare":78}
                    }
                }]
            }
        }]
    }
}
```

Your application should be able to take "IncomeStatement", "EarningsPerShare", and
"DividendsDeclaredPerCommonShare" as an input and return 78 in all cases here. All child properties should
be added.
