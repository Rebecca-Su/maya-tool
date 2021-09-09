from maya import cmds;
from functools import partial;

def onMayaDroppedPythonFile(*args, **kwargs):
    loadNurbsUI();

def changeAllNurbColor(colorSlider, *args):
    targetColor = cmds.colorIndexSliderGrp(colorSlider, q=True,value=True);
    selectedNurbsCurve = cmds.ls(selection = True, type = "transform");
    print(selectedNurbsCurve);
    for obj in selectedNurbsCurve:
        obj = cmds.listRelatives(obj, shapes=True);
        cmds.setAttr(obj[0] + '.overrideEnabled', 1);
        cmds.setAttr(obj[0] + '.overrideColor', targetColor - 1);
   
def loadNurbsUI():     
    if cmds.window('ChangeNurbsUI', exists=True):
    		cmds.deleteUI('ChangeNurbsUI');
    window = cmds.window('ChangeNurbsUI', title="Change All Nurbs Curve Colors", iconName='Short Name', widthHeight=(400, 80) );
    
    cmds.columnLayout( adjustableColumn=True );
    colorSlider = cmds.colorIndexSliderGrp( label='Select Color', min=0, max=20, value=10 );
    
    cmds.button( label='Apply Color', command = partial(changeAllNurbColor, colorSlider));
    
    cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') );
    cmds.setParent( '..' );
    cmds.showWindow( window );