from flask import Flask

app = Flask(__name__)

# Global variable to store the visit counter
visit_count = 0

@app.route('/')
def hello_world():
    global visit_count
    visit_count += 1
    return f'Hello, World! You are visitor number {visit_count}'

if __name__ == '__main__':
    app.run()
