import os
import sys
from app import app

def main():
    try:
        port = int(os.environ.get('PORT', 8000))
        debug = os.environ.get('FLASK_ENV') == 'development'
        app.run(host='0.0.0.0', port=port, debug=debug)
    except Exception as e:
        print(f"Error starting application: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()