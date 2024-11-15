import requests
import json
import time

# Array of 100 sentences
correct = 1

sentences = [
    "He's not waking up, no matter what I do!",
    "She fell down the stairs and isn't moving.",
    "He's clutching his chest and can't breathe properly.",
    "She's having a seizure and I don't know what to do!",
    "He suddenly can't move the left side of his body.",
    "Her fever is dangerously high and won't come down.",
    "He's become violent and I'm afraid he'll hurt himself or me.",
    "She wandered off and I can't find her anywhere.",
    "I think he swallowed some cleaning products!",
    "She's been vomiting non-stop for hours.",
    "There's blood in his urine and he's in pain.",
    "She suddenly can't see anything.",
    "He's complaining of the worst headache of his life.",
    "He's seeing things that aren't there and is terrified.",
    "She's talking about ending her life.",
    "He fainted and I can't get him to come around.",
    "She's having what looks like an allergic reaction.",
    "His skin and eyes have turned yellow.",
    "She has a severe rash all over her body.",
    "He's coughing up blood.",
    "She's shaking uncontrollably and feels very cold.",
    "I think he might have broken his hip in a fall.",
    "She has a large, unexplained bruise on her head.",
    "He's bleeding heavily and I can't get it to stop.",
    "She's so dizzy she can't stand up.",
    "He suddenly can't speak or understand what I'm saying.",
    "She's complaining of severe stomach pain.",
    "He's having trouble breathing and his lips are turning blue.",
    "I think she might have had a stroke.",
    "He's showing signs of a heart attack.",
    "She has severe burns from spilling hot water.",
    "He's not making any sense and seems completely disoriented.",
    "She's having a severe asthma attack and her inhaler isn't helping.",
    "I think he might have overdosed on his medication.",
    "She's having a severe panic attack and can't calm down.",
    "He's become completely unresponsive to any stimuli.",
    "She's having hallucinations and is very agitated.",
    "He's showing signs of severe dehydration.",
    "He's having severe withdrawal symptoms.",
    "She's fallen and hit her head hard on the floor.",
    "He's having difficulty swallowing and is drooling excessively.",
    "I think she might have had an aneurysm.",
    "He's showing signs of a diabetic emergency.",
    "He's become combative and I can't control him.",
    "He's having severe tremors that won't stop.",
    "He's showing signs of internal bleeding.",
    "He's having severe chest pains that radiate to his arm.",
    "She's become completely catatonic.",
    "She's having severe mood swings and talking about harming herself.",
    "He's showing signs of liver failure.",
    "I think she might have had a pulmonary embolism.",
    "He's having a severe allergic reaction to a new medication.",
    "She's become extremely lethargic and won't respond to me.",
    "I think he might have appendicitis.",
    "She's having severe vertigo and can't stop vomiting.",
    "He's showing signs of a severe urinary tract infection.",
    "He's having severe dental pain and his face is swollen.",
    "She's had a sudden loss of hearing in both ears.",
    "She's showing signs of severe malnutrition.",
    "He's having difficulty breathing and his chest feels tight.",
    "I think she might have had a transient ischemic attack.",
    "She's having severe muscle spasms and cramping.",
    "He's become extremely agitated and is pacing non-stop.",
    "She's having severe night terrors and won't sleep.",
    "She's showing signs of severe anxiety and can't be calmed down.",
    "He's having difficulty with basic tasks he could do yesterday.",
    "I think she might have a brain tumor.",
    "He is attacking me!",
    "Im bleeding so much",
    "Ahh, Help!",
    "I smell smoke! Is that a fire!",
    "Ah, its burning!",
    "Stop hitting her please!",
    "Ah he is overdosing",
    "Im losing consciousness",
    "Dont drink that! Thats Bleach!",
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