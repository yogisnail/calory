import pandas as pd

df = pd.read_excel('/home/yeganeh/calory/data/df.xlsx')

def find_calories(food_name, amount):
    try:
        row = df.loc[df['FoodName'] == food_name].iloc[0]

        calories_per_100g = row['calory']
        calories = (amount / 100) * calories_per_100g

        return calories
    except IndexError:
        return 'Food not found'

food_name = input('Food name: ')
amount = float(input('Amount (grams): '))

result = find_calories(food_name, amount)
print(f'Calories for {amount} grams of {food_name}: {result}')
