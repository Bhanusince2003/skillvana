from flask import Flask
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

if __name__ == '__main__':
    app.run(debug=True)
