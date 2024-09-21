#Python quiz game
print("================= BOOST YOUR KNOWLEDGE =================")



# Define the questions, options, and answers
questions = [
    {
        "question": "1.Who is known as the Father of Geometry?",
        "options": ["A. Euclid", "B. Pythagoras", "C. Aristotle", "D. Archimedes"],
        "answer": "A"
    },
    {
        "question": "2.Greenland is part of which country?",
        "options": ["A. Iceland", "B. Norway", "C. Denmark", "D. Sweden"],
        "answer": "C"
    },
    {
        "question": "3.Which is the biggest animal on earth?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Shark", "D. Giraffe"],
        "answer": "B"
    },
    {
        "question": "4.When is National Girl Child Day in India celebrated?",
        "options": ["A. 24th January", "B. 8th March", "C. 15th August", "D. 5th June"],
        "answer": "A"
    },
    {
        "question": "5.Who is known as the 'Nightingale of India'?",
        "options": ["A. Indira Gandhi", "B. Sarojini Naidu", "C. Mother Teresa", "D. Rani Lakshmibai"],
        "answer": "B"
    },
    {
        "question": "6.How many days does a leap year have?",
        "options": ["A. 365", "B. 366", "C. 364", "D. 367"],
        "answer": "B"
    },
    {
        "question": "7.Who built the world’s first aeroplane?",
        "options": ["A. Wright Brothers", "B. Leonardo da Vinci", "C. Charles Lindbergh", "D. The Montgolfier Brothers"],
        "answer": "A"
    },
    {
        "question": "8.The Taj Mahal is situated on the banks of which river?",
        "options": ["A. Yamuna", "B. Ganges", "C. Brahmaputra", "D. Yamuna"],
        "answer": "A"
    },
    {
        "question": "9.Who are the founders of Google?",
        "options": ["A. Larry Page and Sergey Brin", "B. Steve Jobs and Steve Wozniak", "C. Bill Gates and Paul Allen", "D. Mark Zuckerberg and Eduardo Saverin"],
        "answer": "A"
    },
    {
        "question": "10.In which year was Facebook founded?",
        "options": ["A. 2004", "B. 2005", "C. 2006", "D. 2007"],
        "answer": "A"
    },
    {
        "question": "11.Who wrote the Mahabharata?",
        "options": ["A. Vyasa", "B. Valmiki", "C. Kalidasa", "D. Tulsidas"],
        "answer": "A"
    },
    {
        "question": "12.Which is the smallest ocean?",
        "options": ["A. Pacific Ocean", "B. Atlantic Ocean", "C. Indian Ocean", "D. Arctic Ocean"],
        "answer": "D"
    },
    {
        "question": "13.How many days does it take for the Moon to make one revolution around the Earth?",
        "options": ["A. 27.3 days", "B. 28 days", "C. 30 days", "D. 29.5 days"],
        "answer": "A"
    },
    {
        "question": "14.Which organ is responsible for the purification of blood in the human body?",
        "options": ["A. Liver", "B. Kidney", "C. Heart", "D. Lungs"],
        "answer": "B"
    },
    {
        "question": "15.When is World Environment Day celebrated?",
        "options": ["A. 22nd April", "B. 5th June", "C. 15th August", "D. 1st December"],
        "answer": "B"
    },
    {
        "question": "16.What are two types of eclipses?",
        "options": ["A. Solar eclipse and lunar eclipse", "B. Partial eclipse and total eclipse", "C. Penumbral eclipse and annular eclipse", "D. Total eclipse and annular eclipse"],
        "answer": "A"
    },
    {
        "question": "17.What is the full form of CPU?",
        "options": ["A. Central Processing Unit", "B. Central Power Unit", "C. Computer Processing Unit", "D. Central Program Unit"],
        "answer": "A"
    },
    {
        "question": "18.What do you call a shape that has six sides?",
        "options": ["A. Pentagon", "B. Hexagon", "C. Octagon", "D. Quadrilateral"],
        "answer": "B"
    },
    {
        "question": "19.Who is known as the 'Iron Man of India'?",
        "options": ["A. Jawaharlal Nehru", "B. Sardar Vallabhbhai Patel", "C. Mahatma Gandhi", "D. B.R. Ambedkar"],
        "answer": "B"
    },
    {
        "question": "20.Who is known as the 'Missile Man of India'?",
        "options": ["A. Vikram Sarabhai", "B. APJ Abdul Kalam", "C. Homi Bhabha", "D. Rajeev Gandhi"],
        "answer": "B"
    },
    {
        "question": "21.Which part of the human body has the smallest bone?",
        "options": ["A. Ear", "B. Nose", "C. Finger", "D. Toe"],
        "answer": "A"
    },
    {
        "question": "22.Which African country is famous for its chocolate?",
        "options": ["A. Ivory Coast", "B. Ghana", "C. Nigeria", "D. Kenya"],
        "answer": "B"
    },
    {
        "question": "23.In which country are the Giza Pyramids located?",
        "options": ["A. Egypt", "B. Sudan", "C. Libya", "D. Saudi Arabia"],
        "answer": "A"
    },
    {
        "question": "24.Which is the densest forest in the world?",
        "options": ["A. Congo Basin", "B. Amazon Rainforest", "C. Taiga", "D. Valdivian Temperate Rainforest"],
        "answer": "B"
    },
    {
        "question": "25.Which is the most sensitive organ in the human body?",
        "options": ["A. Eye", "B. Skin", "C. Ear", "D. Tongue"],
        "answer": "B"
    },
    {
        "question": "26.Who invented the television?",
        "options": ["A. Nikola Tesla", "B. John Logie Baird", "C. Guglielmo Marconi", "D. Alexander Graham Bell"],
        "answer": "B"
    },
    {
        "question": "27.Which animal is known as the ship of the desert?",
        "options": ["A. Horse", "B. Camel", "C. Elephant", "D. Donkey"],
        "answer": "B"
    },
    {
        "question": "28.Which is the tallest waterfall in the world?",
        "options": ["A. Niagara Falls", "B. Angel Falls", "C. Victoria Falls", "D. Yosemite Falls"],
        "answer": "B"
    },
    {
        "question": "29.The Olympic Games are held after a gap of how many years?",
        "options": ["A. 2 years", "B. 4 years", "C. 6 years", "D. 8 years"],
        "answer": "B"
    },
    {
        "question": "30.Where were the first Summer Olympics held?",
        "options": ["A. Athens", "B. Rome", "C. Paris", "D. London"],
        "answer": "A"
    },
    {
        "question": "31.Where is the Leaning Tower of Pisa located?",
        "options": ["A. Italy", "B. France", "C. Spain", "D. Greece"],
        "answer": "A"
    },
    {
        "question": "32.Where is the Louvre Museum situated?",
        "options": ["A. London", "B. New York", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "33.Which river is nicknamed 'Sorrow of China'?",
        "options": ["A. Yellow River", "B. Yangtze River", "C. Mekong River", "D. Pearl River"],
        "answer": "A"
    },
    {
        "question": "34.Where is the world's tallest building, Burj Khalifa, located?",
        "options": ["A. Abu Dhabi", "B. Dubai", "C. Doha", "D. Riyadh"],
        "answer": "B"
    },
    {
        "question": "35.Who is known as the father of C (programming) Language?",
        "options": ["A. Dennis Ritchie", "B. Bjarne Stroustrup", "C. James Gosling", "D. Guido van Rossum"],
        "answer": "A"
    },
    {
        "question": "36.Which blood cells in our body help to fight infections?",
        "options": ["A. Red Blood Cells", "B. White Blood Cells", "C. Platelets", "D. Plasma"],
        "answer": "B"
    },
    {
        "question": "37.What is the capital of Belgium?",
        "options": ["A. Amsterdam", "B. Brussels", "C. Luxembourg", "D. Paris"],
        "answer": "B"
    },
    {
        "question": "38.Who wrote the book 'Discovery of India'?",
        "options": ["A. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. Rabindranath Tagore", "D. S. Radhakrishnan"],
        "answer": "A"
    },
    {
        "question": "39.Who invented the telescope?",
        "options": ["A. Galileo Galilei", "B. Isaac Newton", "C. Johannes Kepler", "D. Tycho Brahe"],
        "answer": "A"
    },
    {
        "question": "40.Which is the highest dam in India?",
        "options": ["A. Bhakra Nangal Dam", "B. Tehri Dam", "C. Sardar Sarovar Dam", "D. Nagarjuna Sagar Dam"],
        "answer": "B"
    },
    {
        "question": "41.Which is the largest country in terms of population?",
        "options": ["A. India", "B. China", "C. USA", "D. Indonesia"],
        "answer": "B"
    },
    {
        "question": "42.Which is the largest delta in the world?",
        "options": ["A. Ganges-Brahmaputra Delta", "B. Nile Delta", "C. Mississippi Delta", "D. Danube Delta"],
        "answer": "A"
    },
    {
        "question": "43.Which sport is the Durand Cup related to?",
        "options": ["A. Cricket", "B. Football", "C. Tennis", "D. Hockey"],
        "answer": "B"
    },
    {
        "question": "44.When is World Red Cross Day celebrated?",
        "options": ["A. 4th May", "B. 8th March", "C. 5th June", "D. 22nd April"],
        "answer": "A"
    },
    {
        "question": "45.Which country is known as the 'Land of Cakes'?",
        "options": ["A. England", "B. Scotland", "C. Ireland", "D. Wales"],
        "answer": "B"
    },
    {
        "question": "46.Who is the author of ‘Romeo and Juliet’?",
        "options": ["A. William Shakespeare", "B. Charles Dickens", "C. J.K. Rowling", "D. Jane Austen"],
        "answer": "A"
    },
    {
        "question": "47.Which is the fastest bird in the world?",
        "options": ["A. Peregrine Falcon", "B. Golden Eagle", "C. Albatross", "D. Bald Eagle"],
        "answer": "A"
    },
    {
        "question": "48.The Statue of Liberty was a gift to the USA from which country?",
        "options": ["A. France", "B. Germany", "C. Italy", "D. Spain"],
        "answer": "A"
    },
    {
        "question": "49.Which state is known as the Orchid Paradise of India?",
        "options": ["A. Sikkim", "B. Arunachal Pradesh", "C. Meghalaya", "D. Nagaland"],
        "answer": "B"
    },
    {
        "question": "50.Which country awards the Nobel Prize?",
        "options": ["A. Sweden", "B. Norway", "C. Denmark", "D. Switzerland"],
        "answer": "A"
    },
    {
        "question": "51.What is the currency of Malaysia?",
        "options": ["A. Ringgit", "B. Peso", "C. Dollar", "D. Yen"],
        "answer": "A"
    },
    {
        "question": "52.How many consonants are there in the English alphabet?",
        "options": ["A. 21", "B. 20", "C. 22", "D. 23"],
        "answer": "A"
    },
    {
        "question": "53.When is Earth Day celebrated?",
        "options": ["A. 22nd April", "B. 5th June", "C. 1st January", "D. 15th August"],
        "answer": "A"
    },
    {
        "question": "54.Which is the largest desert in India?",
        "options": ["A. Thar Desert", "B. Great Indian Desert", "C. Kutch Desert", "D. Rann of Kutch"],
        "answer": "A"
    },
    {
        "question": "55.What do you call the place where bees are kept?",
        "options": ["A. Apiary", "B. Aviary", "C. Farm", "D. Greenhouse"],
        "answer": "A"
    }
]
print("***************Quiz contain 55 questions***************")
def display_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    return answer

def check_answer(question_data, user_answer):
    return user_answer == question_data["answer"]

def quiz():
    score = 0
    total_questions = len(questions)

    for q_data in questions:
        user_answer = display_question(q_data)
        if check_answer(q_data, user_answer):
            print("Correct!")
            score += 1
        else:
            correct_option = q_data["options"][ord(q_data["answer"]) - 65]
            print(f"Wrong! The correct answer is {correct_option}.")
        print()

    print(f"Your final score is {score}/{total_questions}")

if __name__ == "__main__":
    quiz()
