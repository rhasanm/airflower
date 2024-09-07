import subprocess
import os
import re

def adjust_imports(file_path):
    """Adjust import statements in generated Python files."""
    with open(file_path, 'r') as file:
        content = file.readlines()

    new_lines = []
    for line in content:
        # Match import statements related to *_pb2
        match = re.match(r'^import (\w+_pb2)\s+as\s+(\w+__pb2)$', line)
        if match:
            module_name = match.group(1)
            alias_name = match.group(2)
            new_line = f'from airflower_protobufs import {module_name} as {alias_name}\n'
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(new_lines)

def generate_protobufs():
    """Generate protobuf Python files and adjust import statements."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    proto_dir = os.path.join(base_dir, '..', 'airflower_protobufs', 'protos')
    out_dir = os.path.join(base_dir, '..', 'airflower_protobufs')

    os.makedirs(out_dir, exist_ok=True)

    proto_files = [os.path.join(proto_dir, f) for f in os.listdir(proto_dir) if f.endswith('.proto')]

    if not proto_files:
        raise FileNotFoundError("No .proto files found in the proto directory.")

    command = [
        'python', '-m', 'grpc_tools.protoc',
        f'-I{proto_dir}',
        f'--python_out={out_dir}',
        f'--grpc_python_out={out_dir}',
        f'--pyi_out={out_dir}'
    ] + proto_files

    print(f"Running command: {' '.join(command)}")
    subprocess.run(command, check=True)

    # Adjust imports in generated files
    for file_name in os.listdir(out_dir):
        if file_name.endswith('_pb2.py') or file_name.endswith('_pb2_grpc.py'):
            file_path = os.path.join(out_dir, file_name)
            adjust_imports(file_path)

if __name__ == '__main__':
    generate_protobufs()
