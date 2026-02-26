import pandas as pd
import numpy as np
import random

def generate_fake_data(rows=20, filename="sample_data.xlsx"):
    data = pd.DataFrame({
        "Client Name": [random.choice(["Alice", "Bob", "Charlie", "David"]) for _ in range(rows)],
        "Transaction Amount": [random.choice([100, 200, "N/A", -50, 0]) for _ in range(rows)],
        "Join Date": [random.choice(["2023-01-01", "01/02/2023", "15-03-2023", "2024-12-01"]) for _ in range(rows)]
    })
    data.to_excel(filename, index=False)
    print(f"Fake data generated: {filename}")
    return filename
