from PyInstaller.utils.hooks import collect_data_files, copy_metadata

datas = collect_data_files('glue_vispy_viewers')
datas += copy_metadata('glue-vispy-viewers')