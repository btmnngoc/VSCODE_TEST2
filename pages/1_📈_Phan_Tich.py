import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from logic.data_loader import load_financial_metrics
from logic.processor import (
    preprocess_financial_longform,
    get_indicator_groups,
    extract_unit
)
from config import FINANCIAL_METRIC_PATH

# Cấu hình style biểu đồ
def configure_plot_style():
    custom_palette = ['#004c97', '#f2a900', '#f45d01', '#7ec8e3']
    sns.set_style("whitegrid")
    sns.set_palette(sns.color_palette(custom_palette))

    plt.rcParams.update({
        'figure.figsize': (12, 6),
        'axes.titlesize': 18,
        'axes.labelsize': 14,
        'xtick.labelsize': 11,
        'ytick.labelsize': 11,
        'legend.fontsize': 11,
        'font.family': 'DejaVu Sans',
        'lines.linewidth': 2.5,
        'lines.markersize': 8
    })

def main():
    st.title("📈 Phân Tích Chỉ Số Tài Chính - FPT")

    configure_plot_style()
    df_raw = load_financial_metrics(FINANCIAL_METRIC_PATH)
    df_long = preprocess_financial_longform(df_raw)

    df_fpt = df_long[df_long['StockID'] == 'FPT']
    groups = get_indicator_groups()
    palette = ['#004c97', '#f2a900', '#f45d01', '#7ec8e3']

    for group_name, indicators in groups.items():
        sub = df_fpt[df_fpt['Indicator'].isin(indicators)]
        if sub.empty:
            continue

        y_unit = extract_unit(indicators)
        fig, ax = plt.subplots()

        for idx, indicator in enumerate(indicators):
            line_data = sub[sub['Indicator'] == indicator]
            if line_data.empty:
                continue
            sns.lineplot(
                data=line_data,
                x='Period',
                y='Value',
                label=indicator.split('\n')[0],
                color=palette[idx % len(palette)],
                marker='o',
                ax=ax
            )

        ax.set_title(f"{group_name} (FPT)", fontweight='bold')
        ax.set_xlabel("Kỳ báo cáo")
        ax.set_ylabel(f"Giá trị ({y_unit})")
        ax.legend(title="Chỉ số", bbox_to_anchor=(1.02, 1), loc="upper left")
        st.pyplot(fig)

if __name__ == "__main__":
    main()