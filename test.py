import requests
import json
import time
import Test_Emergency
import Test_Non_Emergency

# Array of 100 sentences
correct = 1

sentences = Test_Emergency.getEmergencyArray()
# sentences = Test_Non_Emergency.getNonEmergencyArray()

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

total_time = 0
for sentence in sentences:
    # Prepare the JSON payload
    payload = {
        "message": sentence
    }

    try:
        # Start timer for this request
        start_time = time.time()
        
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
            
            # Calculate time taken for this request
            request_time = time.time() - start_time
            total_time += request_time
            
            print(f"Processed sentence: '{sentence}'. Rating: {rating}. Time: {request_time:.2f}s")
        else:
            print(f"Error processing sentence: '{sentence}'. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error sending request for sentence: '{sentence}'. Error: {e}")

# Print average time per request
if allNum > 0:
    avg_time = total_time / allNum
    print(f"\nAverage time per request: {avg_time:.2f}s")
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