# main.py
from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='plagiarism_detection.log', level=logging.INFO)

# Sample assignments data
assignments = [
    {"id": 1, "text": "This is the first assignment."},
    {"id": 2, "text": "This is the second assignment."},
    {"id": 3, "text": "This is the third assignment with some similarities."},
    {"id": 4, "text": "Another assignment unrelated to the previous ones."}
]

# Function to preprocess text
def preprocess_text(text):
    # Implement text preprocessing (tokenization, stop words removal, etc.)
    return text.lower()  # Placeholder for simplicity

# Function to calculate cosine similarity
def calculate_similarity(text1, text2):
    # Implement TF-IDF vectorization and cosine similarity calculation
    return 0.7  # Placeholder for simplicity

# API endpoint for submitting an assignment
@app.route('/submit_assignment', methods=['POST'])
def submit_assignment():
    data = request.get_json()
    assignment_id = data.get('id')
    assignment_text = data.get('text')
    # Preprocess assignment text
    preprocessed_text = preprocess_text(assignment_text)
    # Store assignment in the database (implementation required)
    logging.info(f"Assignment submitted - ID: {assignment_id}")
    return jsonify({"message": "Assignment submitted successfully"})

# API endpoint for checking plagiarism
@app.route('/check_plagiarism', methods=['POST'])
def check_plagiarism():
    data = request.get_json()
    assignment_id = data.get('id')
    assignment_text = data.get('text')
    # Preprocess assignment text
    preprocessed_text = preprocess_text(assignment_text)
    # Compare with other assignments
    for assignment in assignments:
        if assignment['id'] != assignment_id:
            similarity_score = calculate_similarity(preprocessed_text, assignment['text'])
            if similarity_score > 0.8:  # Threshold for plagiarism detection
                logging.warning(f"Suspicious similarity detected - Assignment ID: {assignment_id}, Similarity Score: {similarity_score}")
                return jsonify({"plagiarism_detected": True, "similar_assignment_id": assignment['id'], "similarity_score": similarity_score})
    return jsonify({"plagiarism_detected": False})

if __name__ == '__main__':
    app.run(debug=True)

