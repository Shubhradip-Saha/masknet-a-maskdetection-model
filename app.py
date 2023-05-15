from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/run_script')
def run_script():
    try:
        # Run your Python script using subprocess module
        result = subprocess.check_output(['python', 'your_script.py'], shell=True)
        return result
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
