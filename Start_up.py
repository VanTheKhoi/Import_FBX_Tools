# import site
# path = r'YOUR_PATH'
# site.addsitedir(path)

try:
    from importlib import reload #Fixed bug in python 3
except:
    pass

from Import_Fbx_Tools.Controls import Import_Fbx_Controls as Import_Fbx_Controls
reload(Import_Fbx_Controls)

try:
    my_window.close()
    my_window.deleteLater()
except:
    pass

my_window = Import_Fbx_Controls.Import_Fbx()
my_window.show()