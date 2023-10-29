import math
import random
from game.locator import Locator


class Geometry:
    """
    Класс Geometry представляет собой базовый класс для геометрических объектов. В текущей версии не имеет
    дополнительных атрибутов или методов.
    """

    def __init__(self):
        """
        Конструктор класса Geometry. Создает объект Geometry.
        """

    def get_line_parameters(self, point1, point2):
        """
        Метод, вычисляющий параметры линии и возвращающий их в виде словаря.

        Возвращает:
        - line_parameters (dict): Словарь с параметрами линии.
        """
        x1, y1 = point1
        x2, y2 = point2
        line_parameters = {}

        if x1 == x2:
            line_parameters['x'] = x1
        elif y1 == y2:
            line_parameters['y'] = y1
        else:
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1
            line_parameters['slope'] = {'k': slope, 'b': intercept}

        return line_parameters

    def check_points_on_line(self, buffer):
        """
        Возвращает линию, которая описывает крайние точки прямой.
        Если ни одна точка не лежит на одной прямой, то возвращает False.
        """
        if len(buffer) != 4:
            # Если в буфере нет четырёх точек, возвращаем False
            return False

        max_line = None

        for i in range(4):
            for j in range(i + 1, 4):
                # Проверяем каждую пару точек (i, j)
                line_params = self.get_line_parameters(buffer[i], buffer[j])

                # Проверяем, лежит ли каждая точка на этой линии
                points_on_line = [point for point in buffer if (
                        point[0] == line_params.get('x') or
                        point[1] == line_params.get('y') or
                        (line_params.get('slope') and
                         point[1] == line_params['slope']['k'] * point[0] + line_params['slope']['b']))]

                if not max_line or len(points_on_line) > len(max_line[0]):
                    # Если текущая линия содержит больше точек, чем максимальная линия
                    max_line = (points_on_line, buffer[i], buffer[j])

        if max_line:
            # Возвращаем крайние точки линии
            return (min(max_line[0], key=lambda x: x[0]), max(max_line[0], key=lambda x: x[0]))
        else:
            # Проверяем, что все точки лежат на одной прямой
            line_params = self.get_line_parameters(buffer[0], buffer[1])
            all_on_line = all(
                point[0] == line_params.get('x') or
                point[1] == line_params.get('y') or
                (line_params.get('slope') and
                 point[1] == line_params['slope']['k'] * point[0] + line_params['slope']['b'])
                for point in buffer
            )
            if all_on_line:
                return (buffer[0], buffer[1])
            else:
                return False

    def are_lines_overlap(self, line1, line2, tolerance=1):
        """
        Проверяет перекрытие двух линий с учетом допустимого отклонения параметров.

        Аргументы:
        - line1 (list[tuple[float, float]]): Первая линия.
        - line2 (list[tuple[float, float]]): Вторая линия.
        - tolerance (float): Допустимое отклонение параметров линий.

        Возвращает:
        - True, если две линии перекрываются, иначе False.
        """
        line1_params = self.get_line_parameters(line1[0], line1[1])
        line2_params = self.get_line_parameters(line2[0], line2[1])

        # Проверяем перекрытие на основе параметров линий и допустимого отклонения
        if 'x' in line1_params:
            return abs(line1_params['x'] - line2_params.get('x', 0)) <= tolerance
        elif 'y' in line1_params:
            return abs(line1_params['y'] - line2_params.get('y', 0)) <= tolerance
        elif 'slope' in line1_params and 'slope' in line2_params:
            k1, b1 = line1_params['slope']['k'], line1_params['slope']['b']
            k2, b2 = line2_params['slope']['k'], line2_params['slope']['b']
            return abs(k1 - k2) <= tolerance and abs(b1 - b2) <= tolerance

        return False

    def combine_collinear_lines(self, lines, local_line, tolerance=1):
        """
        Объединяет коллинеарные линии в одну линию.

        Аргументы:
        - lines (list[list[tuple[float, float]]): Список линий для объединения.
        - local_line (list[tuple[float, float]]): Линия, заданная крайними точками.
        - tolerance (float): Допустимое отклонение параметров для считания линий коллинеарными.

        Возвращает:
        - Список объединенных коллинеарных линий.
        """
        # Реализация объединения коллинеарных линий с новой линией
        for i, existing_line in enumerate(lines):
            if self.are_lines_overlap(local_line, existing_line, tolerance):
                # Если линии коллинеарны, объединяем их
                x1 = min(local_line[0][0], existing_line[0][0])
                y1 = min(local_line[0][1], existing_line[0][1])
                x2 = max(local_line[1][0], existing_line[1][0])
                y2 = max(local_line[1][1], existing_line[1][1])
                lines[i] = [(x1, y1), (x2, y2)]
                return lines  # Выход из функции после объединения

        # Если линия не коллинеарна ни с одной линией, добавляем ее к списку
        lines.append(local_line)
        return lines


class Line(Geometry):
    """
    Класс Line представляет собой геометрическую линию между двумя точками.

    Атрибуты:
    - point1 (tuple): Кортеж, представляющий первую точку линии в формате (x, y).
    - point2 (tuple): Кортеж, представляющий вторую точку линии в формате (x, y).
    - line_parameters (dict): Словарь, содержащий параметры линии (например, x, y, slope).

    Методы:
    - get_line_parameters(): Вычисляет параметры линии и возвращает их в виде словаря.

    """

    def __init__(self, point1, point2):
        """
        Конструктор класса Line. Создает объект Line между двумя точками.

        Аргументы:
        - point1 (tuple): Первая точка линии в формате (x, y).
        - point2 (tuple): Вторая точка линии в формате (x, y).
        """
        super().__init__()
        self.point1 = point1
        self.point2 = point2
        # self.line_parameters = self.get_line_parameters()


class Circle(Geometry):
    """
    Класс Circle представляет собой геометрический объект - окружность. В текущей версии не имеет дополнительных
    атрибутов или методов.
    """

    def __init__(self):
        """
        Конструктор класса Circle. Создает объект Circle.
        """
        super().__init__()


class Train:
    """
    Класс Train представляет собой модель поезда, управляемого автоматически или вручную.

    Атрибуты:
    - x (float): Координата x текущего положения поезда.
    - y (float): Координата y текущего положения поезда.
    - alpha (float): Угол поворота поезда относительно оси x.
    - v_max (float): Максимальная скорость поезда.
    - locator (Locator): Объект Locator, предоставляющий данные о расположении поезда.

    Методы:
    - update(x, y): Обновляет координаты поезда и получает точки на объекте.
    - info(): Возвращает информацию о измеренных объектах и точках.
    - processing(): Выбор режима движения (автоматический или ручной).
    - manual_update(x, y, alpha): Обновление координат поезда в ручном режиме.
    - processing_auto(): Автоматическое движение поезда на основе данных локатора.
    """

    def __init__(self, x0: float, y0: float, alpha0: float, v_max: float, locator: Locator):
        """
        Конструктор класса Train. Создает объект поезда с заданными параметрами.

        Аргументы:
        - x0 (float): Начальная координата x.
        - y0 (float): Начальная координата y.
        - alpha0 (float): Начальный угол поворота поезда.
        - v_max (float): Максимальная скорость поезда.
        - locator (Locator): Объект Locator для получения данных о расположении поезда.
        """

        self.alpha = alpha0  # строительная ось от оси x против часовой стрелки
        self.x = x0
        self.y = y0

        self.v_max = v_max
        self.locator = locator
        self.geometry = Geometry()

        self.v = 10
        self.turn = 1
        self.points = []
        self.oneturncount = 0
        self.alpha_buffer = 0
        self.move_counter = 0

        self.auto = True
        self.shape = None
        self.rotation = True
        self.distance = None

        self.point_buffer_list = []
        self.lines = []

    def get_line(self):
        if self.lines:
            self.point_buffer_list.sort()
            local_line = self.geometry.check_points_on_line(buffer=self.point_buffer_list)
            if local_line:
                self.lines = self.geometry.combine_collinear_lines(local_line=local_line, lines=self.lines)
        else:
            self.point_buffer_list.sort()
            local_line = self.geometry.check_points_on_line(buffer=self.point_buffer_list)
            self.lines.append(local_line)

    def determine_figure(self):
        self.get_line()

    def update(self, x: float, y: float):
        """
        Метод обновления координат поезда и получения точек на объекте.

        Аргументы:
        - x (float): Новая координата x.
        - y (float): Новая координата y.
        """

        # TODO в будющих версиях боты сами будут счислять свое положение
        if self.auto:
            self.x = x
            self.y = y

        # дергаем измерение локатора
        measurement = self.locator.measurement

        if measurement['query']:  # запрос
            x_q, y_q, alpha_q = measurement['query'][0]
            self.distance = measurement['distance']

            if self.distance:
                new_point = (
                    x_q + self.distance * math.cos(alpha_q),
                    y_q + self.distance * math.sin(alpha_q)
                )
                self.points.append(new_point)
                self.point_buffer_list.append(new_point)
                if len(self.point_buffer_list) == 4:
                    self.determine_figure()
                    self.point_buffer_list.pop(0)
            else:
                if self.point_buffer_list:
                    self.point_buffer_list.clear()
        else:
            self.distance = None

    def info(self) -> dict:
        """
        Метод, возвращающий информацию о измеренных объектах и точках.

        Возвращает:
        - info (dict): Словарь с информацией о поезде и измеренных объектах.
        """

        # TODO!
        color1 = (255, 0, 0)
        color2 = (0, 120, 0)
        color3 = (255, 0, 150)
        line1 = [(100, 200,), (100, 300), color1]
        line2 = [(150, 250), (150, 350), color2]
        line3 = [(0, 0), (500, 500), color3]
        circle1 = ((100, 200), 20, color3)  # (point, radius)
        circle2 = ((200, 400), 30, color3)  # (point, radius)
        circle3 = ((400, 600), 40, color2)  # (point, radius)

        figures = {
            "lines": self.lines,  # не замкнутая
            "circles": [circle1, circle2, circle3],
            "points": []
        }

        return {
            "params": (self.x, self.y, self.v, self.alpha),
            "maps": figures
        }

    def processing(self):
        """
        Метод для выбора режима движения (автоматического или ручного) поезда.
        """

        if self.auto:
            self.processing_auto()

    def manual_update(self, x: float, y: float, alpha: float):
        """
        Метод для обновления координат поезда в ручном режиме.

        Аргументы:
        - x (float): Приращение координаты x.
        - y (float): Приращение координаты y.
        - alpha (float): Приращение угла поворота.
        """

        if not self.auto:
            self.x += x
            self.y += y
            self.alpha += alpha

        self.locator.make_query(self.x, self.y, self.alpha)

    def processing_auto(self):
        """
        Метод для автоматического движения поезда на основе данных локатора.
        """

        if self.auto:
            if self.move_counter % 300 == 0:
                self.rotation = True

            if self.distance:
                if self.distance < 30:
                    if random.randint(0, 1) == 0:
                        self.alpha += math.pi + random.uniform(- math.pi / 3, math.pi / 3)
                    else:
                        self.alpha += - math.pi + random.uniform(- math.pi / 3, math.pi / 3)

            if self.rotation:
                if self.alpha_buffer > 2 * math.pi:
                    if random.randint(0, 1) == 0:
                        self.alpha += 2 * math.pi / 3 + random.uniform(- math.pi / 3, math.pi / 3)
                    else:
                        self.alpha += - 2 * math.pi / 3 + random.uniform(- math.pi / 3, math.pi / 3)

                    self.alpha_buffer = 0
                    self.rotation = False

                self.alpha += math.radians(5)
                self.alpha_buffer += math.radians(5)
            else:
                self.x += self.v * math.cos(self.alpha)
                self.y += self.v * math.sin(self.alpha)

            self.move_counter += 1

        self.locator.make_query(self.x, self.y, self.alpha)
