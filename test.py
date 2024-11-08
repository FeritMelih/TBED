import requests
import json

# Array of 100 sentences
correct = 0

sentences = [
    "What are some tips for creating a relaxing bedtime routine?",
    "How can I help her maintain connections with grandchildren?",
    "What are some strategies for managing paranoia or suspicion?",
    "How can I encourage him to express his feelings?",
    "What are some good ways to incorporate art therapy into daily activities?",
    "How can I manage household chores while providing care?",
    "What are some tips for creating a memory-friendly home environment?",
    "How can I help her feel secure when I need to leave the house?",
    "What are some strategies for managing anger or frustration in dementia patients?",
    "How can I encourage him to try new activities?",
    "Lets eat some steak!"
    ]

# URL for the POST request
url = "http://127.0.0.1:9111"

# Array to store the ratings
ratings = []

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

correctNum = 0

falsePositive = 0

falseNegative = 0

allNum = 0

# Iterate through each sentence
for sentence in sentences:
    # Prepare the JSON payload
    payload = {
        "message": sentence
    }

    try:
        # Send POST request
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the rating
            rating = data['emergency']

            if(int(rating)==correct):
                correctNum=correctNum+1
            if correct==1 and int(rating)!=1:
                falseNegative=falseNegative+1

            if correct==0 and int(rating)!=0:
                falsePositive=falsePositive+1
            
            
            
            allNum=allNum+1
                
            
            # Add the rating to our list
            ratings.append(rating)
            
            print(f"Processed sentence: '{sentence}'. Rating: {rating}")
        else:
            print(f"Error processing sentence: '{sentence}'. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error sending request for sentence: '{sentence}'. Error: {e}")

# Print all ratings
# print("\nAll ratings:")
print(f"CorrectNum: {correctNum}")
print(f"AllNum: {allNum}")
print(f"FalsePositive: {falsePositive}")
print(f"AllNum: {falseNegative}")
print(f"Correct Percentage: {correctNum/allNum*100}%")


# for i, rating in enumerate(ratings, 1):
#     print(f"Sentence {i}: {rating}")

# You can do further processing with the ratings array here if needed