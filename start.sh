export FLASK_ENV=production
gunicorn "app:create_app()" --bind localhost:5000 --workers=3 --log-level INFO
