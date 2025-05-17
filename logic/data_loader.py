import pandas as pd

def load_financial_metrics(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df['Indicator'] = df['Indicator'].astype(str).str.strip()
    return df