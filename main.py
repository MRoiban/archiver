import subprocess
import argparse
import os

def zip(file_path, output_path):
    subprocess.run(["7z", "a", "-t7z", "-m0=lzma2", "-mx=9", "-mfb=256", "-md=32m", "-ms=on", output_path, file_path])

def mv(file_path, output_path):
    subprocess.run(["mv", file_path, output_path])

def rm(folder_path):
    subprocess.run(["powershell", "-Command", f"Remove-Item -Path '{folder_path}' -Recurse -Force"])

def archive(paths):
    print(paths)
    for path in paths:
        if not path.endswith(".7z"):
            output_path = path + ".7z"
            zip(path, output_path)
    
    for path in paths:
        if path.endswith(".7z"):
            continue
        output_path = f"D:\\Root\\User\\Documents\\Archive\\{path}.7z"
        mv(path+".7z",output_path)
        # rm(path)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Archive files in the specified input folders.')
    parser.add_argument('input_folders', type=str, nargs='+', help='The folders containing files to archive.')
    args = parser.parse_args()

    paths = []
    for folder in args.input_folders:
        # Get all files in each input folder
        folder_paths = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        paths.extend(folder_paths)

    archive(args.input_folders)
