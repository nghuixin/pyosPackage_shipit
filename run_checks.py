import pandas as pd

from pyospackage_nghuixin.example import (
add_numbers
)
from pyospackage_nghuixin.data_quality_check import (
count_missing,
missing_summary
)

results = add_numbers(11,23)
print(results)

num_none = count_missing([None, None, 1, 2, None, 4, None, None])
print(num_none)

df = pd.DataFrame({
    "Age ": [25, None, 30, None],
    "Score Value": [88, 92, None, 78]
})


print("NAs:\n", missing_summary(df))