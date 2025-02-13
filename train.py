from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import os

# Initialize ChatBot
chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'  # Store trained data in SQLite
)

# Initialize Trainers
list_trainer = ListTrainer(chatbot)
corpus_trainer = ChatterBotCorpusTrainer(chatbot)

# Custom Training Data
conversation = [
    "Hello", "Hi there! How can I assist you?",
    "Hi", "Hello! How can I help you?",
    "What is your name?", "I am WaibyGPT, your college enquiry assistant!",
    "Who can use this chatbot?", "Students, Faculty, Parents, and Visitors can ask me queries.",
    "How do I contact the administration?", "You can contact the administration via the official college website or email.",
    "How are you doing?", "I'm doing great!",
    "That is good to hear", "Thank you.",
    "You're welcome", "You're welcome!",
    "Your name?", "I'm WaibyGPT Bot.",
    "Who made you?", "I was created by Nuwaib.",

    ### Admission Queries
    "How can I apply for admission?", "You can apply for admission online through the college website.",
    "What is the last date for admission?", "The admission deadline is usually announced on the official college website.",
    "What are the eligibility criteria for admission?", "Eligibility criteria vary by course. Please check the official admission brochure.",
    "Is there an entrance exam for admission?", "Some courses require an entrance exam. Check the admissions page for details.",

    ### Course Queries
    "What courses does the college offer?", "We offer undergraduate, postgraduate, and diploma programs in various fields.",
    "Can I change my course after admission?", "Course changes are subject to availability and approval from the administration.",
    "Are there any online courses available?", "Yes, we offer online certification and diploma courses.",

    ### Fee Structure
    "What is the fee structure for different courses?", "The fee structure varies by course. Please visit the Fees section on our website.",
    "Can I pay the fees in installments?", "Yes, the college provides installment payment options for students.",
    "Are there any scholarships available?", "Yes, we offer merit-based and need-based scholarships.",
    "How do I apply for a scholarship?", "You can apply through the scholarship portal on the college website.",

    ### Hostel & Accommodation
    "Is hostel accommodation available?", "Yes, we provide hostel facilities for both boys and girls.",
    "What are the hostel charges?", "Hostel charges vary based on the type of room and facilities provided.",
    "Can I choose my roommate in the hostel?", "Roommate requests can be submitted during the hostel application process.",
    "Is outside food allowed in the hostel?", "Outside food is generally not allowed in the hostel.",

    ### Exam & Results
    "How can I check my exam results?", "Exam results are available on the student portal.",
    "What is the passing criteria for exams?", "Students must secure a minimum percentage as per the course requirements.",
    "How do I apply for re-evaluation of my exam paper?", "Re-evaluation requests can be submitted through the examination department.",
    "When are the semester exams conducted?", "Semester exams are conducted twice a year, in May-June and November-December.",

    ### Placements & Internships
    "Does the college provide placement assistance?", "Yes, we have a dedicated placement cell to assist students with job placements.",
    "Which companies visit the campus for placements?", "Top companies from IT, finance, healthcare, and other industries visit our campus.",
    "Is an internship mandatory in the final year?", "Yes, most courses require students to complete an internship.",
    "How do I apply for an internship?", "You can apply for internships through the college placement portal.",

    ### Library & Facilities
    "Is there a library in the college?", "Yes, we have a well-equipped library with a wide range of books and journals.",
    "Can I borrow books from the library?", "Yes, students can borrow books using their library card.",
    "Is Wi-Fi available on campus?", "Yes, free Wi-Fi is available across the campus.",
    "Are sports facilities available?", "Yes, we have sports facilities including a gym, football ground, and indoor games.",

    ### Miscellaneous
    "How do I get a student ID card?", "Student ID cards are issued after successful admission.",
    "Can I get a duplicate ID card if I lose mine?", "Yes, you can apply for a duplicate ID card by submitting a request to the administration.",
    "Is there medical assistance available on campus?", "Yes, we have a health center for medical emergencies.",
    "What should I do in case of ragging?", "Ragging is strictly prohibited. Report any incidents to the anti-ragging committee immediately."

]

# Train chatbot with custom conversation
print("Training chatbot with custom data...")
list_trainer.train(conversation)

# Train chatbot with built-in corpus data (English, greetings, and conversations)
print("Training chatbot with corpus data...")
corpus_trainer.train("chatterbot.corpus.english")

print("Training complete! Chatbot is ready.")
