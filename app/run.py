# Use Flask CLI to Run Migration Commands
#   For Bash:                     For Windows CMD:            For Windows PowerShell:
#   export FLASK_APP=run.py       set FLASK_APP=run.py        $env:FLASK_APP = "run.py"

# After setting the FLASK_APP environment variable, you should be able to run the Flask-Migrate commands:
#   flask db init
#   flask db migrate -m "Initial migration."
#   flask db upgrade
#   flask run

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
