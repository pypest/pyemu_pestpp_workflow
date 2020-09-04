# Remove the temp directory and then create a fresh one
import os
import shutil
import pyemu


def get_notebooks():
    return [f for f in os.listdir(".") if f.endswith('.ipynb')]


def run_notebook(fn):
    #pth = os.path.join(nbdir, fn)
    pth = fn
    cmd = 'jupyter ' + 'nbconvert ' + \
          '--ExecutePreprocessor.kernel_name=python ' + \
          '--ExecutePreprocessor.timeout=6000 ' + '--to ' + 'notebook ' + \
          '--execute ' + '{} '.format(pth) + \
          '--output ' + '{}'.format(fn)
    
    #ival = os.system(cmd)
    ival = pyemu.os_utils.run(cmd,cwd=nbdir)
    print(ival,cmd)
    assert ival == 0 or ival is None, 'could not run {}'.format(fn)


def test_notebooks():
    files = get_notebooks()

    for fn in files:
        yield run_notebook, fn

if __name__ == '__main__':
    files = get_notebooks()
    for fn in files:
        run_notebook(fn)
