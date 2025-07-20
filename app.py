from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").lower()

    if user_msg in ["start", "hi", "hello", "talk more?"]:
        return jsonify({
            "response": "Welcome to Planto.ai Assistant! What would you like to do today?",
            "buttons": ["Learn AI", "Build Projects", "Just Exploring", "Facing a Problem?"]
        })

    # Learn AI path
    if user_msg == "learn ai":
        return jsonify({
            "response": "Awesome! What level are you currently at?",
            "buttons": ["Beginner", "Intermediate", "Advanced"]
        })

    if user_msg == "beginner":
        return jsonify({
            "response": "We recommend starting with our beginner-friendly courses, daily challenges, and curated playlists to get started with AI fundamentals.",
            "buttons": ["Talk more?"]
        })

    if user_msg == "intermediate":
        return jsonify({
            "response": "Great! Try building real-world projects, participating in hackathons, and using our AI assistant to explore deeper concepts.",
            "buttons": ["Talk more?"]
        })

    if user_msg == "advanced":
        return jsonify({
            "response": "Explore advanced problem-solving tasks, contribute to open-source AI, or use Planto Copilot to accelerate your research or product ideas.",
            "buttons": ["Talk more?"]
        })

    # Build Projects path
    if user_msg == "build projects":
        return jsonify({
            "response": "Great! What kind of projects do you want to work on?",
            "buttons": ["AI Projects", "Web Development", "Data Science"]
        })

    if user_msg == "ai projects":
        return jsonify({
            "response": "You can use Planto Copilot to generate AI project ideas and build step-by-step with guided tasks and tutorials.",
            "buttons": ["Talk more?"]
        })

    if user_msg == "web development":
        return jsonify({
            "response": "Check out our collection of beginner to advanced web projects, and use our prompt generator for HTML, CSS, and JS code snippets.",
            "buttons": ["Talk more?"]
        })

    if user_msg == "data science":
        return jsonify({
            "response": "We have curated tasks and project flows for Data Cleaning, EDA, Visualization, and Model Training. Dive in!",
            "buttons": ["Talk more?"]
        })

    # Just Exploring path
    if user_msg == "just exploring":
        return jsonify({
            "response": "Explore our tools like Copilot, Prompt Playground, Resume Builder, and more!",
            "buttons": ["Try Copilot", "Use Prompt Playground", "Explore Resume Tools"]
        })

    if user_msg == "try copilot":
        return jsonify({
            "response": "Planto Copilot helps you code faster, build smarter, and learn along the way. Start any task and Copilot will assist you step-by-step.",
            "buttons": ["Talk more?"]
        })

    if user_msg == "use prompt playground":
        return jsonify({
            "response": "The Prompt Playground lets you experiment with different AI prompts and understand how to build smarter inputs for better outputs.",
            "buttons": ["Talk more?"]
        })

    if user_msg == "explore resume tools":
        return jsonify({
            "response": "Use our Resume Builder to generate your resume from projects, auto-fill sections, and even get job-matching insights.",
            "buttons": ["Talk more?"]
        })

    # Problem Solving Path
    if user_msg == "facing a problem?":
        return jsonify({
            "response": "What's the problem you're facing?",
            "buttons": ["Can't Learn", "No Project Ideas", "Low Motivation", "Time Management"]
        })

    if user_msg == "can't learn":
        return jsonify({
            "response": "Try our personalized learning tracks, small tasks, and gamified learning tools to stay motivated.",
            "buttons": ["Talk more?"]
        })

    if user_msg == "no project ideas":
        return jsonify({
            "response": "Browse Planto.ai's project library or generate ideas with Copilot AI.",
            "buttons": ["Talk more?"]
        })

    if user_msg == "low motivation":
        return jsonify({
            "response": "Set small goals, join the Planto community, and track your daily progress.",
            "buttons": ["Talk more?"]
        })

    if user_msg == "time management":
        return jsonify({
            "response": "Use our AI Task Scheduler to plan and balance your learning efficiently.",
            "buttons": ["Talk more?"]
        })

    return jsonify({
        "response": "Sorry, I didn't understand that. Please choose one of the options.",
        "buttons": ["Learn AI", "Build Projects", "Just Exploring", "Facing a Problem?"]
    })

if __name__ == "__main__":
    app.run(debug=True)
