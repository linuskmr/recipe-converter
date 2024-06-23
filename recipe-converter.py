# Takes a .txt/md recipe with the slogan "For/Für N portions/waffles/crepes/..." and converts all quantities according to the target amount of portions.

import re
import sys
import argparse
from pathlib import Path

argparser = argparse.ArgumentParser(description='Takes a .txt/md recipe with the slogan "For/Für N portions/waffles/crepes/..." and converts all quantities according to the target amount of portions.')
argparser.add_argument('-n', metavar='TARGET_PORTIONS', type=int, required=True, help='Number of target portions')
argparser.add_argument('recipe', type=argparse.FileType('r'), help='Path to recipe file')
cli_args = argparser.parse_args()
target_portions = cli_args.n
recipe = cli_args.recipe.read()

# Regex for matching `For/Für N portions/waffles/crepes/...`
portions_regex = r"(für|for) (\d+) (.+)"
portions_match = re.search(portions_regex, recipe, flags=re.IGNORECASE)
if not portions_match:
    print("No portion information found")
    exit()
    
# Replace original portion number with target value
recipe = re.sub(portions_regex, rf"\1 {target_portions} \3", recipe, flags=re.IGNORECASE)

# Calculate conversion factor for all quantities in the recipe
recipe_portions = int(portions_match[2])
portions_conversion_factor = float(target_portions) / float(recipe_portions)

def amount_conversion(amount_recipe_match: re.Match) -> str:
    amount_recipe, unit = amount_recipe_match.groups()

    # We don't want to resize °C or min ;)
    if unit not in ['g', 'ml', 'packet', 'TSP', 'TL']:
        return amount_recipe_match[0]
    
    # Convert German decimal separator to English, so float() can parse it
    amount_recipe = amount_recipe.replace(',', '.')
    amount_recipe = float(amount_recipe)
    amount_converted = amount_recipe * portions_conversion_factor
    return f"{amount_converted}{unit}"

# Regex for matching quantity values like `150ml` and `3.5g`, but not `14.` (enumeration)
# Explanation:
# \d+ - One or more digits at the start
# (?:[\.,]\d+)? - Decimal part, might be omitted
#   ?: - Non-matching group
#   [\.,] - Decimal separator (English dot (escaped) or German comma)
#   \d+ - Followed by one or more digits
#   ? - Decimal part might be omitted
# \s? - Number might be followed by a space
# \w+ - Unit
amounts_regex = r"(\d+(?:[\.,]\d+)?)\s?(\w+)"
recipe = re.sub(amounts_regex, amount_conversion, recipe)

print(recipe)
