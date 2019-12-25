# qt-ci-util
Some basic python methods for building CI for qt projects.

## Usage

```
pip install qtciutil
```

Script example:

```python
import qtciutil
# Get Qt Version
qt_version_str = qtciutil.qt_version()
# Build Qt Project
qtciutil.build('/home/l2m2/workspace/xxx/src/xxx.pro', '/home/l2m2/workspace/xxx/build', 'debug')
```