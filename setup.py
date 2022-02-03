import cx_Freeze

executables=[cx_Freeze.Executable("PET ARCADE.py")]

cx_Freeze.setup(
    name="PET ARCADE Game",
    options={"build_exe":{"packages":["pygame"],
                        "include_files":["bird","dino","menu","snake","space","ka1.ttf"]}},
    executables=executables

)     