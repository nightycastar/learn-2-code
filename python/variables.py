# String
text : str = 'Hello, World!'

# Integer
number : int = 12345

# Float
decimal : 67.89

# Boolean
condition : bool = True

# List
to_buy : list[str] = ["Egg","Cheese","Flour"]
print(to_buy[-1])

# Tuple
math_pie = tuple[int, int] = (3.14, 2.718)
print(f'Circle with r=7 area: {math_pie[0]*(7**2)}')

# Dict
price : dict[str,float] = {
  "Egg": 2.3,
  "Milk": 4.5,
  "Sausage": 6.2
}
print(f'Price of Egg = ${price["Egg"]}')

# None
what_now = None