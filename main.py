import os
import subprocess

file_names = []
file_lines = []

def delete_tmp_files(filenames: list):
    for i in filenames:
        os.remove(f'tmp-{i}.yaml')


def create_tmp_files():
    with open('./ingress_convert.yaml', 'r') as yamlfile:
        content = yamlfile.readlines()
        num_of_lines = len(content)

    for i in range(0, num_of_lines):
        if(str(content[i]).strip() == '---'):
            file_names.append(str(str(content[i+1]).replace('### ', '')).strip())
            file_lines.append(i+2)
        
    for i in range(len(file_names)):
        tmp_file = open(f'tmp-{file_names[i]}.yaml', 'w')
        try:
            for j in range(file_lines[i], (file_lines[i+1] - 2)):
                tmp_file.write(str(content[j]))
        except IndexError:
            for j in range(file_lines[i], num_of_lines):
                tmp_file.write(str(content[j]))
        tmp_file.close()
    
    return file_names


def convert_yaml(filenames: list):
    if not os.path.exists('yaml-files-converted'):
        os.makedirs('yaml-files-converted')
    for file in filenames:
        new_file = open(f'yaml-files-converted/{file}.yaml', 'w')
        result = subprocess.run(['kubectl', 'convert', '-f', f'tmp-{file}.yaml', '--output-version', 'networking.k8s.io/v1'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        new_file.write(result)
        new_file.close()


if __name__ == "__main__":
    file_names = create_tmp_files()
    convert_yaml(file_names)
    delete_tmp_files(file_names)
