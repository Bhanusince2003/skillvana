from flask import Flask , render_template , request
from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 
genai.configure(api_key=GEMINI_API_KEY)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") 


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
@app.route("/test-gemini")
def test_gemini():
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content("your prompt here")
    return response.text

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        branch = request.form["branch"]
        semester = request.form["semester"]
        interests = request.form["interests"]
        prompt = f"""You are Skillvana AI Mentor for Indian engineering students.

Create EXACTLY this STRICT Markdown format for {branch} {semester}th sem student (Interests: {interests}):

## 📅 6-Month {interests.title()} Roadmap

### Month 1: Foundation
- **Week 1:** Task 1
- **Week 1:** Task 2  
- **Week 1:** Task 3
- **Week 2:** Task 1
- **Week 2:** Task 2
- **Week 2:** Task 3
- **Week 3:** Task 1
- **Week 3:** Task 2
- **Week 3:** Task 3
- **Week 4:** PROJECT: [name] + freeCodeCamp link

### Month 2: Intermediate
[... EXACT same pattern for 6 months]

**REQUIREMENTS:**
- Indian engineering college context
- Free resources only (YouTube, freeCodeCamp, GeeksforGeeks)
- Practical projects with GitHub links
- Weekly 2-3 hours daily
- USE ONLY ##, ###, -, **BOLD** formatting

**RULES:**
- ONLY ## ### - **BOLD** formatting
- NO paragraphs or sentences
- NO numbering 1.2.3 → use - bullets only
- 3 tasks per week
- Free resources ONLY
- GitHub projects each month"""
        
        response = client.models.generate_content (  # ← YOUR GLOBAL CLIENT
            model="gemini-2.5-flash",
            contents=[{"role": "user", "parts": [{"text": prompt}]}],
        )
        roadmap = response.text
        return render_template("roadmap.html", roadmap=roadmap, interest=interests, branch=branch, semester=semester)
    
    return render_template("profile.html")



if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
