# -*- mode: python ; coding: utf-8 -*-

import os
import sys
import glob

if os.name == 'nt':
    icon = os.path.abspath('icon.ico')
elif sys.platform == 'darwin':
    icon = os.path.abspath('icon.icns')
else:
    icon = None

block_cipher = None

#notebooks = [(x, 'app_notebooks') for x in glob.glob(os.path.join('app_notebooks', '*.ipynb'))]

a = Analysis(['start_glue.py'],
             pathex=['start-glue'],
             binaries=[],
             #datas=notebooks,
             hiddenimports=['PyQt5',
                            'PyQt5.sip',
                            'ipykernel',
                            'ipykernel.datapub',
                            'bqplot',
                            'nbformat',
                            'nbconvert',
                            'numpy',
                            'scipy',
                            'astropy'],
             hookspath=['hooks'],
             runtime_hooks=[],
             excludes=['tkinter', 'PyQt5.QtQml'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='start_glue',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False,
          icon=icon)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='start_glue')

app = BUNDLE(coll,
             name='glue.app',
             icon=icon,
             info_plist={
             'NSHighResolutionCapable': 'True'
             },
             bundle_identifier='org.qt-project.Qt.QtWebEngineCore')
