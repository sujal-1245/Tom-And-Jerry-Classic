from flask import Flask, render_template, request, jsonify
from game_logic import get_ai_move

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ai-move', methods=['POST'])
def ai_move():
    data = request.get_json()
    cat_pos = tuple(data['cat'])
    mouse_pos = tuple(data['mouse'])
    cheese_pos = tuple(data['cheese'])
    difficulty = data.get('difficulty', 'intermediate')

    new_cat_pos = get_ai_move(cat_pos, mouse_pos, cheese_pos, difficulty)
    return jsonify({'cat': new_cat_pos})


if __name__ == '__main__':
    app.run(debug=True)
