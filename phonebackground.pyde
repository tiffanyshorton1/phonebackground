def setup():
    size( 800, 800)
    x = 10
    background(255, 255, 255)
    img = loadImage("emoji heart.jpg")
    while x < 800:
        y = 20 
        while y < 800:
            if x % 200 == 0:
                fill(0, 0, 0)
            else:
                fill(255, 255, 255)
            image(img, x, y, 50, 50)
            if y % 300 == 0:
                fill (56, 45, 85)
                rect(x, y, 20, 20)
            y = y + 100
        x = x + 100
