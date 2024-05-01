[![NLP Youtube Educational Videos Recommendations]

Recommends educational videos based on a string of text by giving 9 videos with the highest similarity scores. For ex. text from a PDF/PPT page etc (meant to be for a concatenation of flashcards term definitions but will work for any text string). 

Currently, it only supports Math, Biology, Chemistry, Physics, Economics, and (some) Computer Science since it pulls from a database curated for binary classification tasks.


Note index.py returns in a JSON Title, Similarity, Link format. 
These are outputs structured by test.py

Input: "What is the Pythagorean theorem? The Pythagorean theorem states that in a right triangle, the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides. How do you find the area of a circle? The area of a circle is calculated using the formula A = πr^2, where A is the area and r is the radius of the circle."

Response "Relevant videos for Math:
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
.... 
"

Input: "What is photosynthesis? Photosynthesis is the process by which plants and other organisms convert light energy into chemical energy that can be used to fuel the organisms' activities. What is the function of the mitochondria? Mitochondria are organelles found in the cells of eukaryotic organisms, and they are responsible for generating most of the cell's supply of adenosine triphosphate (ATP), which is the main energy currency of the cell."

Response: "Title: Intro To Cells: Animals & Plants | Cells | Biology | FuseSchool
Similarity: 0.9618723646234579
Link: https://www.youtube.com/watch?v=LdKcTtabr6Y

Title: Introduction to Oxidative Phosphorylation
Similarity: 0.9576389658595119
Link: https://www.youtube.com/watch?v=kI9rD9bO6wU

Title: Introduction to Oxidative Phosphorylation
Similarity: 0.957493050951614
Link: https://www.youtube.com/watch?v=kI9rD9bO6wU

Title: Prokaryotic vs Eukaryotic: The Differences | Cells | Biology | FuseSchool
Similarity: 0.9547536730583213
Link: https://www.youtube.com/watch?v=kGd-5HSDo6g
..."

Input: "Who was the first President of the United States? George Washington was the first President of the United States, serving from 1789 to 1797. What was the main cause of World War I? The main cause of World War I was a combination of factors, including nationalism, imperialism, militarism, and the complex system of alliances between European nations."

Response: "Relevant videos for History:
Title: Precursors to European and World Unification
Similarity: 0.9655772134762125
Link: https://www.youtube.com/watch?v=BVlRzhRT8jU

Title: World War II: Crash Course European History #38
Similarity: 0.9647892745664718
Link: https://www.youtube.com/watch?v=Hs_JMydrxZM

Title: Independence movements in the 20th Century | World History | Khan Academy
Similarity: 0.9633038900684981
Link: https://www.youtube.com/watch?v=8xIA10NQakI

Title: The Mexican-American War | AP US History | Khan Academy
Similarity: 0.9631973047782963
Link: https://www.youtube.com/watch?v=QKRYLUlGlWc

Title: Antietam part 2
Similarity: 0.9631377142440147
Link: https://www.youtube.com/watch?v=k4uSZ6sonCU

Title: The Soviet Bloc Unwinds: Crash Course European History #46
Similarity: 0.9630569644830755
Link: https://www.youtube.com/watch?v=aStaPgdvIdI

Title: The Second World War, Part One: Ethiopia and Spain, 1935-9
Similarity: 0.9626086077806819
Link: https://www.youtube.com/watch?v=bPIv0bVmRiQ

Title: The First World War, Part Three: The Transformation of Central Europe
Similarity: 0.9623940056976714
Link: https://www.youtube.com/watch?v=kCrot5HCA0s

Title: The Roads to World War I: Crash Course European History #32
Similarity: 0.9623478874713448
Link: https://www.youtube.com/watch?v=KGlmlSTn-eM
"

