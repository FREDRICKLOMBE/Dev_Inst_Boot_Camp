import math
import sys

## 🌟 Daily Challenge: Circle
# Create circles using a radius or diameter, then add, compare and sort them.


class Circle:
    """Represent a circle created from either a numeric radius or diameter."""

    def __init__(self, radius=None, diameter=None):
        """Set one finite, non-negative radius or diameter; return None."""
        if (radius is None) == (diameter is None):
            raise ValueError("Give either a radius or a diameter, not both.")

        if diameter is not None:
            self.diameter = diameter
        else:
            self.radius = radius

    @property
    def radius(self):
        """Return the circle's numeric radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius to a finite, non-negative number value; return None."""
        if not isinstance(value, (int, float)):
            raise TypeError("The radius must be a number.")
        if not math.isfinite(value) or value < 0:
            raise ValueError("The radius must be a finite, non-negative number.")
        self._radius = value

    @property
    def diameter(self):
        """Return the numeric diameter, equal to twice the radius."""
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        """Set diameter from numeric value and update the radius; return None."""
        if not isinstance(value, (int, float)):
            raise TypeError("The diameter must be a number.")
        self.radius = value / 2

    def area(self):
        """Return the circle's area as a float in square units."""
        return math.pi * self.radius ** 2

    def __str__(self):
        """Return a readable string describing the radius and diameter."""
        return f"Circle with radius {self.radius:g} and diameter {self.diameter:g}"

    def __repr__(self):
        """Return a compact string showing the class name and radius."""
        return f"Circle(radius={self.radius:g})"

    def __add__(self, other):
        """Return a new Circle with summed radii, or NotImplemented for other types."""
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        """Return whether this Circle is larger than other, or NotImplemented."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

    def __eq__(self, other):
        """Return whether other is a Circle of equal radius, or NotImplemented."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        """Return whether this Circle is smaller than other, or NotImplemented."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius


""" 🌟 Bonus: Draw the sorted circles """
def draw_circles(circles):
    """Draw an iterable of Circle objects in ascending size order; return None."""
    # Turtle is included with standard Python installations that support Tk.
    import turtle

    sorted_circles = sorted(circles)
    if not sorted_circles:
        return

    screen = turtle.Screen()
    screen.title("Sorted Circles")
    screen.setup(width=1000, height=500)

    pen = turtle.Turtle()
    pen.speed(0)
    colors = ["blue", "green", "orange", "purple", "red"]

    # Scale the circles together so they fit inside the window.
    total_diameter = sum(circle.diameter for circle in sorted_circles)
    largest_radius = max(circle.radius for circle in sorted_circles)
    gap = min(30, 400 / len(sorted_circles))
    available_width = 900 - gap * (len(sorted_circles) - 1)
    scale = min(
        available_width / total_diameter if total_diameter else 1,
        160 / largest_radius if largest_radius else 1,
    )
    drawing_width = total_diameter * scale + gap * (len(sorted_circles) - 1)
    x = -drawing_width / 2

    for index, circle in enumerate(sorted_circles):
        drawing_radius = circle.radius * scale
        center_x = x + drawing_radius
        pen.penup()
        pen.goto(center_x, -drawing_radius)
        pen.pendown()
        pen.color(colors[index % len(colors)])
        pen.circle(drawing_radius)

        pen.penup()
        pen.goto(center_x, -drawing_radius - 25)
        pen.write(f"r = {circle.radius:g}", align="center", font=("Arial", 12, "normal"))
        x += drawing_radius * 2 + gap

    pen.hideturtle()
    screen.exitonclick()


if __name__ == "__main__":
    """ Create Circle Instances """
    circle_1 = Circle(radius=3)
    circle_2 = Circle(diameter=10)
    circle_3 = Circle(radius=7)
    circle_4 = Circle(diameter=6)

    """ Display the radius, diameter and area """
    print(circle_1)
    print(repr(circle_2))
    print(f"Radius: {circle_2.radius:g}")
    print(f"Diameter: {circle_2.diameter:g}")
    print(f"Area: {circle_1.area():.2f}")

    """ Add two circles to create a new circle """
    new_circle = circle_1 + circle_2
    print(new_circle)  # Radius 8, diameter 16
    print(circle_1)    # The original radius is still 3
    print(circle_2)    # The original radius is still 5

    """ Compare Circle Instances """
    print(circle_2 > circle_1)   # True
    print(circle_1 > circle_3)   # False
    print(circle_1 == circle_4) # True
    print(circle_1 == circle_2) # False

    """ Store circles in a list and sort them """
    all_circles = [circle_3, circle_1, new_circle, circle_2, circle_4]
    sorted_circles = sorted(all_circles)
    print(sorted_circles)  # Radii: 3, 3, 5, 7, 8

    """ Test the property setters """
    circle_4.diameter = 12
    print(circle_4.radius)    # 6.0
    circle_4.radius = 4
    print(circle_4.diameter)  # 8

    # Run the optional drawing with: py DailyChallenge_Circle.py --draw
    # Click inside the drawing window to close it.
    if "--draw" in sys.argv:
        draw_circles(all_circles)
