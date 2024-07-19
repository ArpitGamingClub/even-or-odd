a = 2
b = 10
if a > b:
      game.splash("A is grater than b")
elif a < b:
      game.splash("A is less than B")
else:
      game.splash("A is equal to B")
def on_update():
    pass
game.on_update(on_update)
def on_update_interval():
    pass
game.on_update_interval(500, on_update_interval)
1 + 1