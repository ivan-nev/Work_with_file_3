import os

def count_lines(filename, chunk_size=1<<13):
    with open(filename, encoding='utf-8') as file:
        return sum(chunk.count('\n')
                    for chunk in iter(lambda: file.read(chunk_size), ''))

def dict_sort_file(path_dir):
    sort_file = {}
    entries = os.listdir(path_dir)
    for files in entries:
        # print(files)
        sort_file[files] = count_lines(os.path.join(path_dir, files))
        # print(os.path.join(path_dir, files))
    #dict1 = {1: 1, 2: 9, 3: 4}
    sorted_tuples = sorted(sort_file.items(), key=lambda item: item[1])
    #print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
    sorted_dict = {k: v for k, v in sorted_tuples}
    return sorted_dict

def make_sort_file(sorted_dict,path_dir):
    os.remove('sort_file.txt')
    for key, value in sorted_dict.items():
        # print(key, value)
        with open('sort_file.txt', 'a', encoding='utf-8') as f:
            f.write(f'{key}\n')
            f.write(f'{value}\n')
            with open((os.path.join(path_dir, key)), 'r', encoding='utf-8') as add:
                for line in add:
                    f.write(str(line))


make_sort_file(dict_sort_file('sorted'), 'sorted')
print (count_lines('sorted/1.txt'))
