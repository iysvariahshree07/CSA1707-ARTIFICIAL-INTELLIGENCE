% Facts
fruit(apple, red).
fruit(banana, yellow).
fruit(orange, orange).
fruit(grapes, green).
fruit(grapes, purple).
fruit(mango, yellow).

% Rule: Get fruit by color
fruit_by_color(Color, Fruit) :- fruit(Fruit, Color).
