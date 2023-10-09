from flask import Flask
from blueprints.main import main_bp
from blueprints.edit import edit_bp
from blueprints.page1 import page1_bp
from blueprints.page2 import page2_bp
from blueprints.add import add_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(edit_bp)
app.register_blueprint(page1_bp)
app.register_blueprint(page2_bp)
app.register_blueprint(add_bp)



if __name__ == '__main__':
    app.run()

