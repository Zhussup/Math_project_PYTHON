from manim import *

class GoldenSection(Scene):
    def construct(self):

        self.camera.frame_width = 16
        self.camera.frame_height = 9


        segment_length = 6
        golden_ratio = (1 + np.sqrt(5)) / 2

        start = LEFT * segment_length / 2
        end = RIGHT * segment_length / 2
        golden_point = start + (end - start) / golden_ratio


        segment = Line(start, end, color=BLUE)
        golden_dot = Dot(golden_point, color=RED)
        golden_label = MathTex(r"\varphi", color=RED).next_to(golden_dot, UP)


        self.play(Create(segment))
        self.play(FadeIn(golden_dot), Write(golden_label))


        left_length = Brace(Line(start, golden_point), DOWN)
        left_label = left_length.get_text(r"$\frac{a}{\varphi}$")

        right_length = Brace(Line(golden_point, end), DOWN)
        right_label = right_length.get_text(r"$\frac{a}{\varphi} + 1$")

        self.play(FadeIn(left_length, right_length))
        self.play(Write(left_label), Write(right_label))

        self.wait(2)


class GoldenRectangleFromSquare(Scene):
    def construct(self):

        self.camera.frame_width = 16
        self.camera.frame_height = 9


        side_length = 4
        golden_ratio = (1 + np.sqrt(5)) / 2

        A = LEFT * side_length / 2 + UP * side_length / 2
        B = RIGHT * side_length / 2 + UP * side_length / 2
        C = RIGHT * side_length / 2 + DOWN * side_length / 2
        D = LEFT * side_length / 2 + DOWN * side_length / 2


        square = Polygon(A, B, C, D, color=BLUE)


        golden_point = B + RIGHT * (side_length * (golden_ratio - 1))

        golden_rect = Polygon(B, golden_point, golden_point + DOWN * side_length, C, color=GOLD)


        golden_arc = ArcBetweenPoints(B, golden_point, angle=-PI / 2, color=RED)  # Дуга


        self.play(Create(square))
        self.wait(1)
        self.play(Create(golden_arc))
        self.wait(1)
        self.play(Create(golden_rect))
        self.wait(5)



class GoldenRectangleProperty(Scene):
    def construct(self):
        self.camera.frame_width = 20
        self.camera.frame_height = 10

        phi = (1 + np.sqrt(5)) / 2  

        width = 8
        height = width / phi  

        bottom_left = LEFT * width / 2 + DOWN * height / 2
        top_right = RIGHT * width / 2 + UP * height / 2

        golden_rect = Rectangle(width=width, height=height, color=GOLD)

        self.play(Create(golden_rect))
        self.wait(1)


        current_width = width
        current_height = height
        current_corner = bottom_left

        squares = []
        rects = []

        for _ in range(5):

            square_size = current_height  

            square = Square(side_length=square_size, color=BLUE).move_to(
                current_corner + RIGHT * square_size / 2 + UP * square_size / 2
            )
            squares.append(square)


            current_width = current_width - square_size
            new_rect = Rectangle(width=current_width, height=current_height, color=GREEN)
            

            new_rect.next_to(square, RIGHT, buff=0)
            rects.append(new_rect)


            current_corner = current_corner + RIGHT * square_size

            self.play(Create(square))
            self.wait(0.5)
            self.play(Create(new_rect))
            self.wait(0.5)

            current_height = current_width / phi

        self.wait(2)

class GoldenRectangleSequence(Scene):
    def construct(self):
        self.camera.frame_height = 10
        self.camera.frame_width = 20


        phi = (1 + 5**0.5) / 2
        width = 6
        height = width / phi
        
        golden_rect = Rectangle(width=width, height=height, color=BLUE)
        golden_rect.move_to(ORIGIN)
        
        self.play(Create(golden_rect))
        self.wait(1)
        
        x, y = -width / 2, height / 2
        square_size = height
        squares = []
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        direction_index = 0
        
        for _ in range(6):
            square = Square(side_length=square_size, color=YELLOW)
            square.move_to([x + square_size / 2, y - square_size / 2, 0])
            squares.append(square)
            self.play(Create(square))
            

            dx, dy = directions[direction_index]
            x += dx * square_size
            y += dy * square_size
            square_size = square_size / phi
            direction_index = (direction_index + 1) % 4
        
        self.wait(2)
        

        spiral = ParametricFunction(
            lambda t: [0.5 * (phi ** (t / PI)) * np.cos(t),
                       0.5 * (phi ** (t / PI)) * np.sin(t), 0],
            t_range=[0, 4 * PI],
            color=RED
        )
        
        self.play(Create(spiral))
        self.wait(3)
