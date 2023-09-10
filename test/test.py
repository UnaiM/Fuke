import os
import pprint
import sys

SCRIPT_PATH = os.path.dirname(__file__)

sys.path.append(os.path.dirname(SCRIPT_PATH))
import fuke


nuke = fuke.Fuke()
nuke.scriptOpen(os.path.join(SCRIPT_PATH, 'lens.nk'))
for node in nuke.allNodes():
    print(node.Class())
    pprint.pprint({x: y.valueAt(1001) for x, y in node.knobs().items()})
    print()
