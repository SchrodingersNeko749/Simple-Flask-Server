import os
from flask import Flask, render_template
import importlib.util

app = Flask(__name__)

def load_routes():
    routes = []
    base_path = os.path.dirname(os.path.realpath(__file__))
    routes_path = os.path.join(base_path, 'routes')

    for root, dirs, files in os.walk(routes_path):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                module_name = file.replace('.py', '')
                module_path = os.path.join(root, file)
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                routes.append(module.route)

    return routes

@app.route('/')
def index():
    return 'Welcome to the Flask Server!'

@app.route('/tools')
def show_tools():
    routes = []

    base_path = os.path.dirname(os.path.realpath(__file__))
    tools_path = os.path.join(base_path, 'routes')

    for root, dirs, files in os.walk(tools_path):
        for file in files:
            if file.endswith('.py'):
                route = os.path.join(root, file.replace('.py', ''))
                routes.append(route.replace(tools_path, '').replace('\\', '/'))

    return render_template("tools.html", routes=routes)

if __name__ == '__main__':
    routes = load_routes()
    for route in routes:
        app.register_blueprint(route)

    app.run()