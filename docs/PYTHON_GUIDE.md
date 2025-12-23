# Python Gelato Maker Guide

## Overview

The `gelato_maker.py` script is an interactive assistant that guides you through making chocolate mint gelato step-by-step.

## Features

- 📋 **Step-by-step guidance** through the entire process
- 🌡️ **Temperature tracking** with reminders
- ⏱️ **Timing assistance** for each step
- 📏 **Recipe scaling** (half batch, double batch, custom)
- 📝 **Batch logging** to track your results
- ⭐ **Rating system** to remember what worked
- 💾 **JSON export** of all your batches

## Requirements

- Python 3.8 or higher
- No external dependencies (uses standard library only)

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/chocolate-mint-gelato.git
cd chocolate-mint-gelato

# Make the script executable (optional)
chmod +x gelato_maker.py
```

## Basic Usage

```bash
python gelato_maker.py
```

The script will:
1. Ask if you want to scale the recipe
2. Display the ingredient list
3. Guide you through each step
4. Track temperatures and times
5. Save your batch results

## Scaling Recipes

When you start the script, you can scale the recipe:

```
Enter scale factor (default 1):
- 1 = Full batch (1 quart)
- 0.5 = Half batch
- 2 = Double batch
- Any positive number works!
```

The script automatically calculates all ingredient amounts.

## Step-by-Step Walkthrough

### Step 1: Mint Infusion
- Guides you through heating milk, cream, and mint
- Tracks steeping time
- Asks about mint intensity

### Step 2: Chocolate Melting
- Reminds you to add cocoa and chocolate
- Ensures smooth melting

### Step 3: Custard Cooking (Critical!)
- Guides through egg tempering
- Tracks custard temperature
- Warns about temperature ranges

### Step 4: Chilling
- Tracks how long you'll chill
- Reminds about ice bath
- Recommends optimal chilling time

### Step 5: Churning
- Tracks churning time
- Gives feedback on duration

### Step 6: Freezing
- Final instructions for storage
- Serving temperature reminders

## Batch Logging

After completing a batch, the script saves your results to `gelato_batches.json`:

```json
[
  {
    "timestamp": "2025-12-23T10:30:00",
    "scale_factor": 1.0,
    "mint_steep_time": 10,
    "custard_final_temp": 83.0,
    "chill_hours": 12.0,
    "churn_minutes": 25,
    "notes": "Perfect! Loved the mint intensity",
    "rating": 5
  }
]
```

## Viewing Your History

```bash
# Pretty print your batch history
python -m json.tool gelato_batches.json
```

## Advanced Usage

### Using as a Module

```python
from gelato_maker import Recipe, Ingredient

# Create custom recipe
recipe = Recipe(
    name="My Custom Gelato",
    yield_amount="1 quart",
    base_ingredients=[...],
    chocolate_ingredients=[...],
    optional_ingredients=[...]
)

# Scale recipe
double_batch = recipe.scale(2.0)
double_batch.display()
```

### Recipe Object

```python
from gelato_maker import Recipe, Ingredient

# Access ingredient data
recipe = Recipe(...)
for ing in recipe.base_ingredients:
    print(f"{ing.amount}{ing.unit} {ing.name}")

# Scale individual ingredient
sugar = Ingredient("sugar", 150, "g")
double_sugar = sugar.scale(2.0)  # 300g sugar
```

## Tips

### For First-Time Users
1. Have all ingredients ready before starting
2. Read through entire script output before beginning
3. Use a thermometer (highly recommended)
4. Follow timing suggestions closely

### For Experienced Users
1. Adjust mint steep time based on preference
2. Scale recipe to fit your ice cream maker
3. Track results to perfect your technique
4. Compare batch logs to see what works

## Troubleshooting

### Script Won't Run

**Error: `python: command not found`**
```bash
# Try python3
python3 gelato_maker.py
```

**Error: `ModuleNotFoundError`**
- Make sure you're using Python 3.8+
- All imports are from standard library

### Batch Log Not Saving

**Check permissions:**
```bash
# Ensure you can write to directory
ls -la gelato_batches.json
```

**File location:**
- `gelato_batches.json` is created in current directory
- Run script from repository root

## Extending the Script

### Add Custom Ingredients

```python
# In gelato_maker.py, modify _create_default_recipe()

custom_additions = [
    Ingredient("vanilla extract", 2, "tsp", "optional"),
    Ingredient("espresso powder", 15, "g", "for coffee flavor"),
]
```

### Add Temperature Alerts

```python
def _check_temperature(self, temp: float, target: float, tolerance: float):
    if abs(temp - target) <= tolerance:
        print("✅ Perfect temperature!")
    elif temp < target - tolerance:
        print("⚠️ Too cold")
    else:
        print("⚠️ Too hot")
```

### Export to CSV

```python
import csv
import json

with open('gelato_batches.json', 'r') as f:
    batches = json.load(f)

with open('gelato_batches.csv', 'w', newline='') as f:
    if batches:
        writer = csv.DictWriter(f, fieldnames=batches[0].keys())
        writer.writeheader()
        writer.writerows(batches)
```

## Examples

### Quick Start (Full Batch)

```bash
$ python gelato_maker.py
# Press Enter for scale factor 1
# Follow prompts
# Enter temperatures and times as you cook
```

### Half Batch

```bash
$ python gelato_maker.py
# Enter 0.5 for scale factor
# All ingredients automatically halved
```

### With Notes

At the end:
```
Rate your gelato (1-5 stars): 5
Any notes for next time? Increased mint to 35g, perfect intensity!
```

## API Reference

### Classes

#### `Recipe`
- `name: str` - Recipe name
- `yield_amount: str` - Expected yield
- `base_ingredients: List[Ingredient]`
- `chocolate_ingredients: List[Ingredient]`
- `optional_ingredients: List[Ingredient]`
- `scale(factor: float) -> Recipe` - Returns scaled recipe
- `display()` - Prints formatted recipe

#### `Ingredient`
- `name: str` - Ingredient name
- `amount: float` - Quantity
- `unit: str` - Measurement unit
- `notes: str` - Additional notes
- `scale(factor: float) -> Ingredient` - Returns scaled ingredient

#### `GelatoMaker`
- `run()` - Start interactive session
- `recipe: Recipe` - Current recipe
- `batch_log: dict` - Current batch data

### Enums

#### `Step`
- `MINT_INFUSION`
- `CHOCOLATE_MELTING`
- `CUSTARD_COOKING`
- `CHILLING`
- `CHURNING`
- `FREEZING`
- `COMPLETE`

## Future Enhancements

Potential additions:
- [ ] Recipe import/export
- [ ] Multiple recipe support
- [ ] Graphical batch history
- [ ] Temperature monitoring integration
- [ ] Timer automation
- [ ] Ingredient cost tracking
- [ ] Nutritional calculations
- [ ] Recipe variations library

## Contributing

Want to improve the Python script? See [CONTRIBUTING.md](../CONTRIBUTING.md)

## License

MIT License - See [LICENSE](../LICENSE)

---

Happy coding and happy gelato making! 🍦🐍

