from pathlib import Path
import shutil
from threading import Thread
from datetime import datetime


def parser(path: Path):
    for file in path.iterdir():
        if file.is_dir():
            thread = Thread(target=parser, args=(file,))
            thread.start()
        elif file.is_file():
            transfer(file)


def transfer(path: Path):
    if path.suffix == '':
        path_to_directory = path.parent.joinpath('Unknown')
    else:
        path_to_directory = path.parent.joinpath(path.suffix.removeprefix('.'))

    path_to_directory.mkdir(exist_ok=True, parents=True)
    print(f'Created directory -> {path_to_directory.name}')
    shutil.move(path, path_to_directory)
    print(f'File {path.name} successfully moved!')


if __name__ == '__main__':
    path = Path(input('Enter the full path to the folder -> '))
    start = datetime.now()

    try:
        parser(path)
    except FileNotFoundError:
        print('You entered the wrong path!')
    except NotADirectoryError:
        print('This is not a directory!')
    except:
        print('Unexpected error!')

    finish = datetime.now()
    print(f'\nTime -> {finish - start}')
