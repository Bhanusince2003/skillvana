from dotenv import load_dotenv
import os
from flask import Flask
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 
client = genai.Client(api_key=GEMINI_API_KEY)

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Skillvana AI Career App! 🚀</h1>"

@app.route('/career')
def career():
    return """
    <h1>🚀 Your AI Career Path (ECE Student)</h1>
    <h2>Phase 1: Foundation (3 months)</h2>
    <ul>
        <li>Python Master → Flask/Django</li>
        <li>Git + GitHub (✅ DONE!)</li>
        <li>HTML/CSS + Bootstrap</li>
    </ul>
    
    <h2>Phase 2: AI/ML (6 months)</h2>
    <ul>
        <li>NumPy, Pandas, Matplotlib</li>
        <li>Scikit-learn → ML Models</li>
        <li>OpenAI API → ChatGPT</li>
    </ul>
    
    <h2>💰 Target Salary: ₹15-25LPA</h2>
    <p>Full-Stack AI Engineer</p>
    """

@app.route('/skills')
def skills():
    return """
    <h1>💻 Skillvana Tech Skills Priority</h1>
    <h2>Priority 1 (Learn NOW)</h2>
    <ul>
        <li>✅ Python + Flask (DONE!)</li>
        <li>✅ Git + GitHub (DONE!)</li>
        <li>HTML/CSS Basics</li>
    </ul>
    
    <h2>Priority 2 (Next Month)</h2>
    <ul>
        <li>JavaScript + React</li>
        <li>PostgreSQL Database</li>
        <li>Docker Deployment</li>
    </ul>
    
    <a href="/">← Home</a> | <a href="/career">Career</a>
    """
@app.route('/test-gemini')
def test_gemini():
    prompt = """
You are Skillvana's AI mentor for Indian ECE students.

Task: Create a 1‑month AI/ML roadmap.

Output format (very strict):
1. Use Markdown.
2. Start with heading: ## 6-Month AI Roadmap
3. Then give day by day steps(1-30).
4. Under each step, add 2 bullet points explaining what to do that month.
5. Keep every bullet short (max 15 words).

Student details:
- Branch: ECE
- Year: 2nd
- Goal: AI engineer in 2 years.
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    # show Markdown text as preformatted for now
    return f"<pre>{response.text}</pre>"

if __name__ == '__main__':
    app.run(debug=True)