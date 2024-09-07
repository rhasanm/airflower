import os
import subprocess
import glob

def generate_protos(proto_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    proto_files = glob.glob(os.path.join(proto_dir, '*.proto'))
    if not proto_files:
        raise FileNotFoundError("No .proto files found in the directory")

    command = [
        'python', '-m', 'grpc_tools.protoc',
        '-Inexus/protos=' + proto_dir,
        '--python_out=' + out_dir,
        '--grpc_python_out=' + out_dir,
    ] + proto_files

    print(f"Running command: {' '.join(command)}")
    subprocess.run(command, check=True)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    proto_dir = os.path.abspath(os.path.join(base_dir, '../../../../protos'))
    out_dir = os.path.abspath(os.path.join(base_dir, '../../'))

    generate_protos(proto_dir, out_dir)

if __name__ == '__main__':
    main()
