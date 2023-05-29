import sys, os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_path)


import pytest

if __name__ == '__main__':
    pytest.main(['-v', 'tests/'])