class Color:
    color_count = 0
    def __init__(self, red, blue, yellow) -> None:
        Color.color_count += 1
        self.red = red
        self.blue = blue
        self.yellow = yellow

red = Color(255,0,0)

print(red.red)
print(red.blue)
print(red.yellow)