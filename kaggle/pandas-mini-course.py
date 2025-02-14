import pandas as pd

data_frame = pd.DataFrame(
    {
        'Yes': [50, 21],
        'No': [131, 2]
    }, index=['Product A', 'Product B']
)

print(data_frame)
