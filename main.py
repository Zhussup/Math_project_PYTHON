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
      
        side_length = 4  # Сторона квадрата
        golden_ratio = (1 + np.sqrt(5)) / 2  # Золотое сечение

        # Точки квадрата
        A = LEFT * side_length / 2 + UP * side_length / 2
        B = RIGHT * side_length / 2 + UP * side_length / 2
        C = RIGHT * side_length / 2 + DOWN * side_length / 2
        D = LEFT * side_length / 2 + DOWN * side_length / 2

        # квадрат
        square = Polygon(A, B, C, D, color=BLUE)

        # Находим точку золотого деления
        golden_point = B + RIGHT * (side_length * (golden_ratio - 1))

        # Создаем золотой прямоугольник
        golden_rect = Polygon(B, golden_point, golden_point + DOWN * side_length, C, color=GOLD)

        # Оформление построения
        golden_arc = ArcBetweenPoints(B, golden_point, angle=-PI / 2, color=RED)  # Дуга

        # Анимации
        self.play(Create(square))  # Рисуем квадрат
        self.wait(1)
        self.play(Create(golden_arc))  # Добавляем дугу
        self.wait(1)
        self.play(Create(golden_rect))  # Добавляем золотой прямоугольник
        self.wait(5)



class GoldenRectangleProperty(Scene):
    def construct(self):
        self.camera.frame_width = 20
        self.camera.frame_height = 10

        phi = (1 + np.sqrt(5)) / 2  

        # Размер начального золотого прямоугольника
        width = 8
        height = width / phi  

        # Начальные координаты (верхний левый угол)
        bottom_left = LEFT * width / 2 + DOWN * height / 2
        top_right = RIGHT * width / 2 + UP * height / 2

        # Создаем основной золотой прямоугольник
        golden_rect = Rectangle(width=width, height=height, color=GOLD)

        # Добавляем золотой прямоугольник на сцену
        self.play(Create(golden_rect))
        self.wait(1)

        # Последовательность отрезания квадратов
        current_width = width
        current_height = height
        current_corner = bottom_left  # Нижний левый угол начального прямоугольника

        squares = []  # Список хранения квадратов
        rects = []  # золотой прямоугольник

        for _ in range(5):  # 5 шагов отрезания
            # Размер квадрата
            square_size = current_height  

            # Определяем вершины квадрата
            square = Square(side_length=square_size, color=BLUE).move_to(
                current_corner + RIGHT * square_size / 2 + UP * square_size / 2
            )
            squares.append(square)

            # Вычисляем размеры и позиции
            current_width = current_width - square_size  # Новая ширина прямоугольника
            new_rect = Rectangle(width=current_width, height=current_height, color=GREEN)
            
            # Устанавливаем новую позицию
            new_rect.next_to(square, RIGHT, buff=0)
            rects.append(new_rect)

            # Смещаем угол
            current_corner = current_corner + RIGHT * square_size

            # Анимация отрезания
            self.play(Create(square))
            self.wait(0.5)
            self.play(Create(new_rect))
            self.wait(0.5)

            # Обновляем
            current_height = current_width / phi

        self.wait(2)

class GoldenRectangleSequence(Scene):
    def construct(self):
        self.camera.frame_height = 10
        self.camera.frame_width = 20

        # размеры золотого прямоугольника
        phi = (1 + 5**0.5) / 2  # сечение
        width = 6
        height = width / phi
        
        # золотой прямоугольник
        golden_rect = Rectangle(width=width, height=height, color=BLUE)
        golden_rect.move_to(ORIGIN)
        
        self.play(Create(golden_rect))
        self.wait(1)
        
        # Разбиваем на квадраты
        x, y = -width / 2, height / 2
        square_size = height
        squares = []
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # Направления: вправо, вниз, влево, вверх
        direction_index = 0  # движения вправо
        
        for _ in range(6):
            square = Square(side_length=square_size, color=YELLOW)
            square.move_to([x + square_size / 2, y - square_size / 2, 0])
            squares.append(square)
            self.play(Create(square))
            
            # координаты для следующего квадрата
            dx, dy = directions[direction_index]
            x += dx * square_size
            y += dy * square_size
            square_size = square_size / phi
            direction_index = (direction_index + 1) % 4  # Меняем направление
        
        self.wait(2)
        
        # логарифмическую спираль
        spiral = ParametricFunction(
            lambda t: [0.5 * (phi ** (t / PI)) * np.cos(t),
                       0.5 * (phi ** (t / PI)) * np.sin(t), 0],
            t_range=[0, 4 * PI],
            color=RED
        )
        
        self.play(Create(spiral))
        self.wait(3)
