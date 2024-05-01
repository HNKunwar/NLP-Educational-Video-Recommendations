
## Usage/Examples

```javascript

Run index.py to get recommendations in a JSON format with Title, Similarity, and Link fields.

Use test.py flask server to experiment locally. 
[glove.840B.300d.txt performs much better but slower]


```

### Example Input

```
What is the Pythagorean theorem? The Pythagorean theorem states that in a right triangle, the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides. How do you find the area of a circle? The area of a circle is calculated using the formula A = πr^2, where A is the area and r is the radius of the circle.
```

### Example Output 
Structured by Test.py* 

Index.py gives JSON response in  Title, Similarity, Link format.
```
Relevant videos for Math:
Title: Area of a Rectangle, Triangle, Circle & Sector, Trapezoid, Square, Parallelogram, Rhombus, Geometry
Similarity: 0.9639917818534853
Link: https://www.youtube.com/watch?v=JnLDmw3bbuw

Title: How To Calculate The Perimeter of a Semicircle
Similarity: 0.9637592226629333
Link: https://www.youtube.com/watch?v=SJAIheSLV3I

Title: Surface Area of a Pyramid & Volume of Square Pyramids & Triangular Pyramids
Similarity: 0.9596864596096373
Link: https://www.youtube.com/watch?v=x8wEnG4GURQ

Title: Circles - Area, Circumference, Radius & Diameter Explained!
Similarity: 0.9591162178071383
Link: https://www.youtube.com/watch?v=D4nGkWOPb6M
...
```
