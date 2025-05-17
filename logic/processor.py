import pandas as pd
import numpy as np
import re
from pandas.api.types import CategoricalDtype

def preprocess_financial_longform(df: pd.DataFrame) -> pd.DataFrame:
    time_cols = df.columns[2:]

    df_long = df.melt(
        id_vars=['Indicator', 'StockID'],
        value_vars=time_cols,
        var_name='Period',
        value_name='Value'
    )

    df_long['Value'] = (
        df_long['Value'].astype(str)
        .str.replace(',', '')
        .str.replace('\n', '')
        .replace('', pd.NA)
        .astype(float)
    )
    df_long.dropna(subset=['Value'], inplace=True)

    period_order = [
        'Q1_2023', 'Q2_2023', 'Q3_2023', 'Q4_2023',
        'Q1_2024', 'Q2_2024', 'Q3_2024', 'Q4_2024'
    ]
    period_type = CategoricalDtype(categories=period_order, ordered=True)
    df_long['Period'] = df_long['Period'].astype(period_type)

    return df_long

def get_indicator_groups():
    return {
        'Khả năng sinh lời': [
            'Tỷ suất sinh lợi trên tổng tài sản bình quân (ROAA)\n%',
            'Tỷ suất lợi nhuận trên vốn chủ sở hữu bình quân (ROEA)\n%',
            'Tỷ suất lợi nhuận gộp biên\n%',
            'Tỷ suất sinh lợi trên doanh thu thuần\n%'
        ],
        'Khả năng thanh toán': [
            'Tỷ số thanh toán hiện hành (ngắn hạn)\nLần',
            'Tỷ số thanh toán nhanh\nLần',
            'Tỷ số thanh toán bằng tiền mặt\nLần'
        ],
        'Đòn bẩy tài chính': [
            'Tỷ số Nợ trên Tổng tài sản\n%',
            'Tỷ số Nợ trên Vốn chủ sở hữu\n%'
        ],
        'Hiệu quả hoạt động': [
            'Vòng quay tổng tài sản (Hiệu suất sử dụng toàn bộ tài sản)\nVòng',
            'Vòng quay hàng tồn kho\nVòng',
            'Vòng quay phải thu khách hàng\nVòng'
        ],
        'Chỉ số thị trường': [
            'Chỉ số giá thị trường trên thu nhập (P/E)\nLần',
            'Chỉ số giá thị trường trên giá trị sổ sách (P/B)\nLần',
            'Beta\nLần'
        ]
    }

def extract_unit(indicator_list):
    units = set()
    for ind in indicator_list:
        match = re.search(r'\n(.+)', ind)
        if match:
            units.add(match.group(1))
    return ', '.join(units) if units else ''