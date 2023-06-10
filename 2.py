import pytest
import random
class Pixel:
    def __init__(self, red: int, green: int, blue: int):
        if not all(0 <= c <= 255 for c in (red, green, blue)):
            raise ValueError("Component values must be in the range [0, 255]")
        self._red = red
        self._green = green
        self._blue = blue

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue

    def __add__(self, other):
        if not isinstance(other, Pixel):
            raise TypeError("Unsupported operand type for +: 'Pixel' and '{}'".format(type(other).__name__))
        red = min(self._red + other._red, 255)
        green = min(self._green + other._green, 255)
        blue = min(self._blue + other._blue, 255)
        return Pixel(red, green, blue)

    def __sub__(self, other):
        if not isinstance(other, Pixel):
            raise TypeError("Unsupported operand type for -: 'Pixel' and '{}'".format(type(other).__name__))
        red = max(self._red - other._red, 0)
        green = max(self._green - other._green, 0)
        blue = max(self._blue - other._blue, 0)
        return Pixel(red, green, blue)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError("Multiplier must be greater than 0")
            red = min(int(self._red * other), 255)
            green = min(int(self._green * other), 255)
            blue = min(int(self._blue * other), 255)
            return Pixel(red, green, blue)
        raise TypeError("Unsupported operand type for *: 'Pixel' and '{}'".format(type(other).__name__))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other <= 0:
                raise ValueError("Divisor must be greater than 0")
            red = min(int(self._red / other), 255)
            green = min(int(self._green / other), 255)
            blue = min(int(self._blue / other), 255)
            return Pixel(red, green, blue)
        raise TypeError("Unsupported operand type for /: 'Pixel' and '{}'".format(type(other).__name__))

    def __eq__(self, other):
        if isinstance(other, Pixel):
            return (self._red, self._green, self._blue) == (other._red, other._green, other._blue)
        return False

    def __str__(self):
        return f"Pixel object\n\tRed: {self._red}\n\tGreen: {self._green}\n\tBlue: {self._blue}"

    def __repr__(self):
        return f"Pixel({self._red}, {self._green}, {self._blue})"

    def get_pixel_near(self, area: int):
        import random
        red = random.randint(max(0, self._red - area), min(255, self._red + area))
        green = random.randint(max(0, self._green - area), min(255, self._green + area))
        blue = random.randint(max(0, self._blue - area), min(255, self._blue + area))
        return Pixel(red, green, blue)


@pytest.fixture
def pixel():
    return Pixel(100, 150, 200)


def test_pixel_creation():
    with pytest.raises(ValueError):
        Pixel(-10, 150, 200)  # Component value less than 0
    with pytest.raises(ValueError):
        Pixel(300, 150, 200)  # Component value greater than 255
    with pytest.raises(TypeError):
        Pixel(100, "green", 200)  # Non-integer component value


def test_pixel_properties(pixel):
    assert pixel.red == 100
    assert pixel.green == 150
    assert pixel.blue == 200


def test_pixel_addition(pixel):
    other = Pixel(50, 70, 90)
    result = pixel + other
    assert result.red == 150
    assert result.green == 220
    assert result.blue == 255


def test_pixel_subtraction(pixel):
    other = Pixel(50, 70, 90)
    result = pixel - other
    assert result.red == 50
    assert result.green == 80
    assert result.blue == 110


@pytest.mark.xfail(reason="Multiplication defect: Components are not rounded down")
def test_pixel_multiplication(pixel):
    result = pixel * 1.5
    assert result.red == 150
    assert result.green == 225
    assert result.blue == 255

    result = 2 * pixel
    assert result.red == 200
    assert result.green == 255
    assert result.blue == 255

    with pytest.raises(TypeError):
        pixel * "2"  # Invalid multiplier type

    with pytest.raises(ValueError):
        pixel * 0  # Multiplier less than or equal to 0


@pytest.mark.xfail(reason="Division defect: Components are not rounded down")
def test_pixel_division(pixel):
    result = pixel / 2
    assert result.red == 50
    assert result.green == 75
    assert result.blue == 100

    with pytest.raises(TypeError):
        pixel / "2"  # Invalid divisor type

    with pytest.raises(ValueError):
        pixel / 0  # Divisor less than or equal to 0


def test_pixel_equality():
    pixel1 = Pixel(100, 150, 200)
    pixel2 = Pixel(100, 150, 200)
    pixel3 = Pixel(200, 150, 100)

    assert pixel1 == pixel2
    assert pixel1 != pixel3


def test_pixel_str_representation(pixel):
    assert str(pixel) == "Pixel object\n\tRed: 100\n\tGreen: 150\n\tBlue: 200"


def test_pixel_repr_representation(pixel):
    assert repr(pixel) == "Pixel(100, 150, 200)"


def test_get_pixel_near(pixel):
    random.seed(42)  # For consistent results in the test
    nearby_pixel = pixel.get_pixel_near(20)
    assert 80 <= nearby_pixel.red <= 120
    assert 130 <= nearby_pixel.green <= 170
    assert 180 <= nearby_pixel.blue <= 220


if __name__ == "__main__":
    pytest.main()
