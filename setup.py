from cx_Freeze import setup, Executable

base = None

executables = [Executable("flashcards.py", base=base, icon = "sushi.ico")]

options = {
    'build_exe': {
        "includes": ["tkinter","random"],
        'packages': [],
        'include_files': ['./data/vocabulary.csv', './data/indices.txt']
    },
}

setup(
    name = "flashcards",
    options = options,
    version = "1.0",
    description = 'Japanese vocabulary tool',
    executables = executables
)