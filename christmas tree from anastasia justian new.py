import turtle

def draw_triangle(color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

def draw_tree():
    # Gambar bagian bawah pohon
    draw_triangle("darkgreen", -100, -100, 200)
    draw_triangle("darkgreen", -80, -40, 160)
    draw_triangle("darkgreen", -60, 20, 120)
    draw_triangle("darkgreen", -40, 80, 80)

    # Gambar batang pohon
    turtle.penup()
    turtle.goto(-15, -100)
    turtle.pendown()
    turtle.fillcolor("saddlebrown")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(-50)
        turtle.left(90)
    turtle.end_fill()

def draw_star():
    turtle.penup()
    turtle.goto(-10, 160)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(20)
        turtle.right(144)
    turtle.end_fill()

def draw_ball(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(5)  # Ukuran bola hiasan
    turtle.end_fill()

def draw_lights():
    # Gambar lampu hiasan dengan posisi tetap
    positions = [(-102, -104), (-82, -44), (-62, 14), (-42, 72), (42, 72), (62, 14), (82, -44), (102, -104), (0, 72), (-20, 14), (20, 14), (-45, -44), (0, -44), (45, -44), (15, -104), (57, -104), (-15, -104), (-57, -104)]
    colors = ["red", "blue", "yellow", "orange", "purple"]

    for i, pos in enumerate(positions):
        draw_ball(pos[0], pos[1], colors[i % len(colors)])  # Menggunakan warna secara bergantian

def twinkle_lights():
    # Twinkling effect
    positions = [(-102, -104), (-82, -44), (-62, 14), (-42, 72), (42, 72), (62, 14), (82, -44), (102, -104)]
    
    # Draw lights with yellow color
    for pos in positions:
        draw_ball(pos[0], pos[1], "red")  # Draw ornaments with yellow color

    # Hide lights by drawing them with the background color
    turtle.ontimer(lambda: hide_lights(positions), 500)  # Hide lights after 500 ms
    turtle.ontimer(twinkle_lights, 1000)  # Call this function again after 1000 ms

def hide_lights(positions):
    # Hide the lights by drawing them with the background color
    for pos in positions:
        draw_ball(pos[0], pos[1], "blue")  # Draw ornaments with background color

def draw_text():
    turtle.penup()
    turtle.goto(0, -220)  # Posisi teks di bawah pohon
    turtle.pendown()
    turtle.color("red")
    turtle.write("Merry Christmas 2024 from Anastasia Justian", align="center", font=("Arial", 16, "bold", "italic"))

def main():
    turtle.speed(5)
    turtle.bgcolor("white")

    draw_tree()
    draw_star()
    draw_lights()  # Tambahkan lampu hiasan
    twinkle_lights()  # Tambahkan efek kerlap-kerlip
    draw_text()    # Tambahkan ucapan

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
