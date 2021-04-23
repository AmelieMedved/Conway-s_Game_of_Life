# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('life.py',
                          targetName='life_',
                          base = 'Win32GUI')]

includes = ['json']

options = {
	'build_exe':{
		'includes': includes,
		'build_exe': 'build_windows',
	}
}

setup(name = 'life',version='0.0.2',description="Conway's_Game_of_Life",
      executables=executables, options=options)
