import converters
from converters import kgs_to_lbs
from utils import find_max

kgs_to_lbs(100)
converters.lbs_kg(30)
converters.kgs_to_lbs(20)
print(converters.lbs_kg(80))

numbers = [10, 20, 2, 39]
max = str(find_max(numbers))
print("the maximum number is " + max)
