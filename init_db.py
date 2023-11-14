# Import your Flask application
from app import app, db

# Create and push an application context
app.app_context().push()

# Now you can run commands that require the application context
db.create_all()
