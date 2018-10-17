#!/usr/bin/env python
#COMMENT FROM GIT 2 USER
import os
import sys
#COMMENT FROM GIT 1 USER
#SAMPLE COMMENT BY USER2
#SAMPLE COMMENT BY USER1
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sample_project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
	#END OF METHOD
