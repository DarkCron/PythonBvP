import math

w = int(input("Rectangle width: "))
h = int(input("Rectangle height: "))

rect_area = w * h;
rect_perimeter = w*2 + h*2;

rect_diagonal = math.sqrt(math.pow(w, 2) + math.pow(h, 2))

print("Rectangle area: %.2f, Rectangle perimeter: %.2f" % (rect_area,rect_perimeter))
print("Rectangle diagonal: %.2f" % rect_diagonal)