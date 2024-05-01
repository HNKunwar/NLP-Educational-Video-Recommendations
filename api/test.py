import requests
import json


math_content = "What is the Pythagorean theorem? The Pythagorean theorem states that in a right triangle, the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides. How do you find the area of a circle? The area of a circle is calculated using the formula A = πr^2, where A is the area and r is the radius of the circle."


biology_content = "What is photosynthesis? Photosynthesis is the process by which plants and other organisms convert light energy into chemical energy that can be used to fuel the organisms' activities. What is the function of the mitochondria? Mitochondria are organelles found in the cells of eukaryotic organisms, and they are responsible for generating most of the cell's supply of adenosine triphosphate (ATP), which is the main energy currency of the cell."


history_content = "Who was the first President of the United States? George Washington was the first President of the United States, serving from 1789 to 1797. What was the main cause of World War I? The main cause of World War I was a combination of factors, including nationalism, imperialism, militarism, and the complex system of alliances between European nations."


def send_query(subject, content):
    url = "http://127.0.0.1:5000/relevant-videos"
    headers = {"Content-Type": "application/json"}
    data = {"content": content}

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(f"Response Code: {response.status_code}")


    try:
        response_content = response.json()
    except ValueError:
        print("Invalid Response:")
        print(response.text)
        return

    if response.status_code == 200:
        print(f"Relevant videos for {subject}:")
        for video in response_content:
            print(f"Title: {video['Title']}")
            print(f"Similarity: {video['Similarity']}")
            print(f"Link: {video['Link']}")
            print()
    else:
        print(f"Error: {response.status_code}")

# Send queries for each subject
send_query("Math", math_content)
print()
send_query("Biology", biology_content)
print()
send_query("History", history_content)