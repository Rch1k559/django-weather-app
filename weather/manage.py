#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set the default Django settings module for the 'weather' project.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')
    try:
        # Import the function that executes Django management commands.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise an informative error if Django is not installed or not available.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Execute the command-line utility with the provided arguments.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # If the script is executed directly, run the main function.
    main()