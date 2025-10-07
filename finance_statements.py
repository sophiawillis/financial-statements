#making it into a function so that you can plug in any company

import yfinance as yf
import pandas as pd

def fin_statements(ticker):
    company = yf.Ticker(ticker)
    income = company.quarterly_financials.T
    balance = company.quarterly_balance_sheet.T
    cashflow = company.quarterly_cashflow.T

    with pd.ExcelWriter(f"{ticker} Financial Statements.xlsx") as writer:
        income.to_excel(writer, sheet_name = "Income Statement")
        balance.to_excel(writer, sheet_name = "Balance Sheet")
        cashflow.to_excel(writer, sheet_name = "Cash Flow Statement")

        print ("Finished exporting")