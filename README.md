# scrapingYahoo
Um programa feito em python com flask e selenium para buscar dados de ações por região

imports:
pip install requests2
pip install lxml
pip install beautifulsoup
pip install selenium
pip install flask

Rodar o arquivo flask.py

abrir postman e fazer chamada:
{seu endereço do running mode}/stocks?region="region"

Exemplo:
http://127.0.0.1:5000/stocks?region="Austria"

Response:
{
    "Stocks": [
        {
            "Symbol": "AAPL.VI",
            "Name": "Apple Inc.",
            "Price (Intraday)": 101.84
        },
        {
            "Symbol": "MSFT.VI",
            "Name": "Microsoft Corporation",
            "Price (Intraday)": 203.0
        },
        {
            "Symbol": "AMZN.VI",
            "Name": "Amazon.com, Inc.",
            "Price (Intraday)": 2634.5
        },
        {
            "Symbol": "GOOC.VI",
            "Name": "Alphabet Inc.",
            "Price (Intraday)": 1971.4
        },
        {
            "Symbol": "GOOA.VI",
            "Name": "Alphabet Inc.",
            "Price (Intraday)": 1929.6
        },
        {
            "Symbol": "FB.VI",
            "Name": "Facebook, Inc.",
            "Price (Intraday)": 268.65
        },
        {
            "Symbol": "NNND.VI",
            "Name": "Tencent Holdings Limited",
            "Price (Intraday)": 65.99
        },
        {
            "Symbol": "NNN1.VI",
            "Name": "Tencent Holdings Limited",
            "Price (Intraday)": 64.8
        },
        {
            "Symbol": "BRKB.VI",
            "Name": "Berkshire Hathaway Inc.",
            "Price (Intraday)": 237.6
        },
        {
            "Symbol": "BRKA.VI",
            "Name": "Berkshire Hathaway Inc.",
            "Price (Intraday)": 357500.0
        },
        {
            "Symbol": "TSLA.VI",
            "Name": "Tesla, Inc.",
            "Price (Intraday)": 509.6
        },
        {
            "Symbol": "AHLA.VI",
            "Name": "Alibaba Group Holding Limited",
            "Price (Intraday)": 178.9
        },
        {
            "Symbol": "JPM.VI",
            "Name": "JPMorgan Chase & Co.",
            "Price (Intraday)": 135.68
        },
        {
            "Symbol": "VISA.VI",
            "Name": "Visa Inc.",
            "Price (Intraday)": 185.84
        },
        {
            "Symbol": "TSFA.VI",
            "Name": "Taiwan Semiconductor Manufacturing Company Limited",
            "Price (Intraday)": 96.7
        },
        {
            "Symbol": "SSUN.VI",
            "Name": "Samsung Electronics Co., Ltd.",
            "Price (Intraday)": 1356.0
        },
        {
            "Symbol": "SSU.VI",
            "Name": "Samsung Electronics Co., Ltd.",
            "Price (Intraday)": 1495.0
        },
        {
            "Symbol": "JNJ.VI",
            "Name": "Johnson & Johnson",
            "Price (Intraday)": 135.62
        },
        {
            "Symbol": "BOAC.VI",
            "Name": "Bank of America Corporation",
            "Price (Intraday)": 35.19
        },
        {
            "Symbol": "MC.VI",
            "Name": "LVMH Mo\u00ebt Hennessy - Louis Vuitton, Soci\u00e9t\u00e9 Europ\u00e9enne",
            "Price (Intraday)": 658.1
        },
        {
            "Symbol": "WMT.VI",
            "Name": "Walmart Inc.",
            "Price (Intraday)": 116.06
        },
        {
            "Symbol": "NVDA.VI",
            "Name": "NVIDIA Corporation",
            "Price (Intraday)": 524.0
        },
        {
            "Symbol": "UNH.VI",
            "Name": "UnitedHealth Group Incorporated",
            "Price (Intraday)": 334.85
        },
        {
            "Symbol": "ICK.VI",
            "Name": "Industrial and Commercial Bank of China Limited",
            "Price (Intraday)": 0.542
        },
        {
            "Symbol": "MAST.VI",
            "Name": "Mastercard Incorporated",
            "Price (Intraday)": 296.3
        }
    ]
}


