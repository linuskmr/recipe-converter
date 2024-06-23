# recipe-converter

Takes a .txt/md recipe with the slogan "For/Für N portions/waffles/crepes/..." and converts all quantities according to the target amount of portions.


## Example

Consider the following recipe named `waffles.md`:

```
For 10 waffles:

1. Put 125g warm butter in a bowl
2. Add 100g sugar
3. Add a packet of vanilla sugar
4. Mix everything
5. Add 3 eggs
6. Mix everything
7. Add 250g flour
8. Add 1TSP baking powder
9. Add a pinch of salt
10. Mix everything
11. Add 200ml milk
12. Mix everything
13. Preheat the waffle iron
14. Put dough on the waffle iron
15. Bake for 1-2 minutes
```

If you now want to make 12 waffles, you can run the `recipe-converter` like this:

```
$ python3 recipe-converter.py -n 12 examples/waffles.md
```

Which will output:

```
For 12 waffles:

1. Put 150.0g warm butter in a bowl
2. Add 120.0g sugar
3. Add a packet of vanilla sugar
4. Mix everything
5. Add 3 eggs
6. Mix everything
7. Add 300.0g flour
8. Add 1TSP baking powder
9. Add a pinch of salt
10. Mix everything
11. Add 240.0ml milk
12. Mix everything
13. Preheat the waffle iron
14. Put dough on the waffle iron
15. Bake for 1-2 minutes
```