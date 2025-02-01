import os
import sys

# Add the project root to the Python path
from pathlib import Path
project_root = str(Path(__file__).resolve().parent.parent.parent)
sys.path.append(project_root)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview_bot.interview_bot.settings')
application = get_wsgi_application()