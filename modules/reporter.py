import matplotlib.pyplot as plt

def generate_report(df, cleaned_file, report_file="reports/report.txt"):
    duplicates = df.duplicated().sum()
    missing = df.isnull().sum().sum()
    negative_amounts = (df['transaction_amount'] < 0).sum()

    with open(report_file, "w") as f:
        f.write(f"Cleaned File: {cleaned_file}\n")
        f.write(f"Rows: {len(df)}, Columns: {len(df.columns)}\n")
        f.write(f"Duplicates removed: {duplicates}\n")
        f.write(f"Missing values handled: {missing}\n")
        f.write(f"Negative transaction amounts fixed: {negative_amounts}\n")
    print(f"Report saved: {report_file}")

    # Optional: small chart
    plt.bar(["Duplicates", "Missing", "Negative Amounts"], [duplicates, missing, negative_amounts])
    plt.title("Cleaning Summary")
    plt.savefig("reports/summary_chart.png")
    plt.close()
