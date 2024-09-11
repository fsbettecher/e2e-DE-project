# Importando as bibliotecas
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Importando variáveis de ambiente

load_dotenv()

commodities = ['CL=F', 'GC=F', 'SI=F']

host = os.getenv('DB_HOST_PROD')
port = os.getenv('DB_PORT_PROD')
db_name = os.getenv('DB_NAME_PROD')
db_user = os.getenv('DB_USER_PROD')
password = os.getenv('DB_PASS_PROD')
schema = os.getenv('DB_SCHEMA_PROD')

database_url = f"postgresql://{db_user}:{password}@{host}:{port}/{db_name}"

engine = create_engine(database_url)

def search_commodities_data(symbol, period='5d', interval='1d'):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period=period, interval=interval)[['Close']]
    data['simbolo'] = symbol

    return data


def search_all_data(commodities):
    all_data = []
    for symbol in commodities:
        data = search_commodities_data(symbol)
        all_data.append(data)
    
    return pd.concat(all_data)


def save_on_postgres(df):
    df.to_sql('commodities', con=engine, schema=schema, if_exists='append', index=True, index_label='Date')

if __name__ == "__main__":
    concat_data = search_all_data(commodities)
    save_on_postgres(concat_data)

# Pegando a cotação dos ativos


# Concatenando os ativos


# Salvando no banco de dados