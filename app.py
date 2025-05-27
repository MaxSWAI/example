from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 임시 데이터 (실제 서비스에서는 데이터베이스나 외부 API 사용)
DOCUMENTS = [
    "인공지능은 미래 기술의 핵심입니다.",
    "머신러닝은 인공지능의 한 분야입니다.",
    "자연어 처리(NLP)는 텍스트 데이터를 분석합니다.",
    "AI 검색 서비스는 정보 접근성을 향상시킵니다.",
    "GitHub와 Render는 개발 및 배포에 유용합니다."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '').lower()
    results = []
    
    if query:
        for doc in DOCUMENTS:
            if query in doc.lower():
                results.append(doc)
    
    return jsonify(results=results)

if __name__ == '__main__':
    app.run(debug=True)
