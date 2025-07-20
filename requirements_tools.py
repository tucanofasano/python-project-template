import subprocess
import platform
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent

def get_venv_pip_path(project_dir: Path) -> Path:
    if platform.system() == 'Windows':
        return project_dir / 'venv' / 'Scripts' / 'pip.exe'
    else:
        return project_dir / 'venv' / 'bin' / 'pip'

def print_command_usage():
    print("Usage: python requirements_tools.py [save|install] [project_dir]")


def save(project_dir: Path):
    pip_path = get_venv_pip_path(project_dir)
    if not pip_path.exists():
        print(f'❌ pip not found at {pip_path}')
        return
    
    req_file = project_dir / 'requirements.txt'
    with open(req_file, 'w') as file:
        subprocess.run([str(pip_path), 'freeze'], stdout=file, check=True)
    
    print(f'✅ Saved requirements to {req_file}')

def install(project_dir: Path = PROJECT_DIR):
    pip_path = get_venv_pip_path(project_dir)
    if not pip_path.exists():
        print(f'❌ pip not found at {pip_path}')
        return
    
    req_file = project_dir / 'requirements.txt'
    if not req_file.exists():
        print(f'❌ {req_file} not found.')
        return
    
    subprocess.run([str(pip_path), 'install', '-r', str(req_file)], check=True)
    print(f'✅ Installed requirements from {req_file}')


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print_command_usage()
        sys.exit(1)
    
    command_type = sys.argv[1]
    project_dir = PROJECT_DIR

    if len(sys.argv) >= 3:
        project_dir = Path(sys.argv[2]).resolve()

    if command_type == "save":
        save(project_dir)
    elif command_type == "install":
        install(project_dir)
    else:
        print(f"Unknown command: {command_type}")
        print_command_usage()
        sys.exit(1)
