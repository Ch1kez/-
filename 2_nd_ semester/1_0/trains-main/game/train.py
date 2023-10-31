import math
import copy
import random
from typing import List


class Circle:
    def __init__(self):
        self.radius = 0
        self.not_line = True
        self.center_point = []


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.line_parameters = self.get_line_parameters()

    def get_line_parameters(self):
        x1, y1 = self.point1
        x2, y2 = self.point2
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


class Train:

    def __init__(self, alpha0, x0, y0, v_max, locator):
        self.alpha = alpha0
        self.x = x0
        self.y = y0
        self.v_max = v_max
        self.locator = locator
        self.v = 5
        self.shape = None
        self.distance = None
        self.maps = []
        self.auto = True
        self.rotation = True
        self.points_buffer = []
        self.points_counter = 0
        self.alpha_buffer = 0
        self.move_counter = 0
        self.points = []
        self.lines = []
        self.circles = []
        self.red = [(255, 0, 0)]
        self.green = [(0, 255, 0)]

    @staticmethod
    def dist_btwn_pnts(point1, point2):
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

    def update(self, x, y):
        if self.auto:
            self.x = x
            self.y = y

        updated_data = self.locator.measurement
        # print(updated_data)

        if updated_data['query']:
            _x, _y, _alpha = updated_data['query'][0]
            self.distance = updated_data['distance']

            if self.distance:
                new_touch_point = (
                    _x + self.distance * math.cos(_alpha),
                    _y + self.distance * math.sin(_alpha)
                )
                self.points.append(new_touch_point)

                self.points_buffer.append(new_touch_point)

                if len(self.points_buffer) == 4:
                    self.get_figures()
                    self.points_buffer.pop(0)
            else:
                if self.points_buffer:
                    self.points_buffer = []
        else:
            self.distance = None

    def info(self):
        # print(len(self.lines))
        if self.lines:
            self.lines = self.combine_collinear_lines(self.lines)
        figures = {
            "lines": self.lines,
            "circles": [],
            "points": []
        }
        print(figures['lines'])
        return {
            'params': (self.x, self.y, self.v, self.alpha),
            'maps': figures
        }

    def processing(self):
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

    def manual_update(self, x: float, y: float, alpha: float):
        if not self.auto:
            self.x += x
            self.y += y
            self.alpha += alpha

        self.locator.make_query(self.x, self.y, self.alpha)

    def get_line(self) -> bool:
        local_points = copy.copy(self.points_buffer)
        is_line = False
        eps = 0.0009

        for i in range(2):
            if local_points[i] == local_points[i + 1]:
                return is_line

            if len(local_points) > 1 and self.dist_btwn_pnts(local_points[i], local_points[i + 1]) > 50:
                return is_line

            if len(local_points) > 2 and self.dist_btwn_pnts(local_points[i + 1], local_points[i + 1]) > 50:
                return is_line

            general_line = Line(point1=local_points[i], point2=local_points[i + 2])
            other_line = Line(point1=local_points[i], point2=local_points[i + 1])
            buff_line = []

            if 'slope' in general_line.line_parameters.keys() and 'slope' in other_line.line_parameters.keys():
                equ1 = general_line.line_parameters['slope']
                equ2 = other_line.line_parameters['slope']
                tg_fi = (equ2['k'] - equ1['k']) / (1 + equ2['k'] * equ1['k'])

                if math.fabs(math.atan(tg_fi)) < 0.01:
                    if self.lines and len(self.lines[-1]) > 1 and self.lines[-1][-2] == local_points[i] and \
                            self.lines[-1][-1] == local_points[i + 1]:
                        self.lines[-1].append(local_points[i + 2])
                    else:
                        buff_line.append(local_points[i])
                        buff_line.append(local_points[i + 1])
                        buff_line.append(local_points[i + 2])
                        self.lines.append(buff_line)

                    is_line = True

            elif 'x' in general_line.line_parameters.keys() and 'x' in other_line.line_parameters.keys():
                if - eps < general_line.line_parameters['x'] - other_line.line_parameters['x'] < eps:
                    if self.lines and len(self.lines[-1]) > 1 and self.lines[-1][-2] == local_points[i] and \
                            self.lines[-1][-1] == local_points[i + 1]:
                        self.lines[-1].append(local_points[i + 2])
                    else:
                        buff_line.append(local_points[i])
                        buff_line.append(local_points[i + 1])
                        buff_line.append(local_points[i + 2])
                        self.lines.append(buff_line)

                    is_line = True

            elif 'y' in general_line.line_parameters.keys() and 'y' in other_line.line_parameters.keys():
                if - eps < general_line.line_parameters['y'] - other_line.line_parameters['y'] < eps:
                    if self.lines and len(self.lines[-1]) > 1 and self.lines[-1][-2] == local_points[i] and \
                            self.lines[-1][-1] == local_points[i + 1]:
                        self.lines[-1].append(local_points[i + 2])
                    else:
                        buff_line.append(local_points[i])
                        buff_line.append(local_points[i + 1])
                        buff_line.append(local_points[i + 2])
                        self.lines.append(buff_line)

                    is_line = True

        return is_line

    def get_straight_angle(self) -> bool:
        if len(self.points_buffer) < 3:
            return False

        p1, p2, p3 = self.points_buffer[-3], self.points_buffer[-2], self.points_buffer[-1]

        angle = self.calculate_angle(p1, p2, p3)

        if 85 < angle < 95:
            self.lines.append([p1, p2, p3])
            return True

        return False

    @staticmethod
    def calculate_angle(p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]) -> float:
        vector1 = (p1[0] - p2[0], p1[1] - p2[1])
        vector2 = (p3[0] - p2[0], p3[1] - p2[1])

        dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
        magnitude1 = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)
        magnitude2 = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)

        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0  # Вернуть 0, если один из векторов имеет нулевую длину.

        angle = math.degrees(math.acos(max(min(dot_product / (magnitude1 * magnitude2), 1), -1)))
        return angle

    def calculate_mean_parameters(self, line):
        # Проверяем, что у нас есть хотя бы две точки
        if len(line) < 2:
            return None  # Возвращаем None, если только одна точка

        # Инициализируем суммы координат
        sum_x = 0
        sum_y = 0

        for x, y in line:
            sum_x += x
            sum_y += y

        # Рассчитываем средние значения x и y
        x_mean = sum_x / len(line)
        y_mean = sum_y / len(line)

        return x_mean, y_mean

    def are_lines_collinear(self, line1, line2, epsilon=0.1):
        # Проверка, лежат ли линии на одной прямой.
        k1, b1 = self.calculate_mean_parameters(line1)
        k2, b2 = self.calculate_mean_parameters(line2)
        return abs(k1 - k2) < epsilon and abs(b1 - b2) < epsilon

    def combine_collinear_lines(self, lines):
        combined_lines = [lines[0]]

        for line in lines[1:]:
            if self.are_lines_collinear(combined_lines[-1], line):
                combined_lines[-1].extend(line)
            else:
                combined_lines.append(line)

        return combined_lines

    def get_figures(self):
        if len(self.points_buffer) < 3:
            return

        type_figure = None  # Инициализируем type_figure значением по умолчанию None
        color = None
        name = None

        if len(self.points_buffer) == 3:
            if self.get_straight_angle():
                self.points_counter = 0
                return

        is_line = self.get_line()

        if is_line:
            type_figure = 'lines'
            color = self.red
            name = f'Line{len(self.lines)}'
            if self.points_buffer:
                self.points_buffer.pop()
        elif self.get_straight_angle():
            type_figure = 'lines'
            color = self.green
            name = f'StraightAngle{len(self.lines)}'
            self.lines.pop()

        if type_figure:
            self.maps.append({
                'type': type_figure,
                'color': color,
                'name': name
            })

        if len(self.points_buffer) == 1:
            self.points_buffer.pop()

        self.points_counter = 0
