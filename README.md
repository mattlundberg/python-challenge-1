# Food Ordering System

A Python command-line application for ordering food and drinks. This system provides an interactive menu interface where users can browse items by category, select quantities, and get order totals.

## Features

- Interactive menu system with 4 categories:
  - Meals (burgers, chicken dishes)
  - Snacks (chips, popcorn, nuts, etc.)
  - Drinks (hot and cold beverages) 
  - Desserts (ice cream, cakes, etc.)
- Easy item selection by number
- Quantity selection with validation
- Running order total and summary
- Clean formatted display of orders
- Option to add multiple items

## Usage

1. Run `python menu.py`
2. Select a category number from the main menu
3. Choose an item by entering its number
4. Specify quantity (press Enter for quantity of 1)
5. Review your order summary
6. Choose to add more items or complete order
7. Get final receipt with total

## Implementation Details

The system uses:
- Nested dictionaries to organize menu items and categories
- Input validation to ensure valid selections
- Dynamic spacing for clean table formatting
- Running total calculation
- Clear order summaries and receipt printing

## Requirements

- Python 3.x
- No external dependencies

## Author

Matthew Lundberg
