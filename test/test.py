from flask import Flask
app = Flask(__name__)  # Flask 객체 생성
 
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
 
if __name__ == "__main__":  # 모듈이 실행 됨을 알림
    app.run(debug=True, port=5000)  # 서버 실행, 파라미터로 debug 여부, port 설정 가능g