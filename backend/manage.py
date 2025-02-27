#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    import os
    import sys

    # Adiciona o caminho do backend no sys.path
    sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

    if __name__ == '__main__':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)



if __name__ == '__main__':
    main()
