from pyospackage_nghuixin.example import (
add_numbers
)
from pyospackage_nghuixin.data_quality_check import (
count_missing
)

results = add_numbers(11,23)
print(results)

num_none = count_missing([None, None, 1, 2, None, 4, None, None])
print(num_none)