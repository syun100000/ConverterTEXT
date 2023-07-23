import sys
from cx_Freeze import setup, Executable

# 変換するPythonスクリプトの情報を記述
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# 実行可能ファイルの情報を記述
exe = Executable(
    script="script.py",
    base="Console",
    target_name="script"
)

# setup関数を呼び出して、実行可能ファイルをビルド
setup(
    name="ConverterTEXT",
    version="1.0",
    description="PDFをテキストファイルに変換するプログラム",
    options={"build_exe": build_exe_options},
    executables=[exe]
)