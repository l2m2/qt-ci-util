# encoding: utf-8

import argparse
import sys
import qtciutil

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Build Arg Parser')
  parser.add_argument('--pro_file', '-p', type=str, required=True,
                      help='pro path', metavar='$CI_PROJECT_DIR/src/something.pro')
  parser.add_argument('--build_dir', '-b', type=str, required=True,
                      help='build directory', metavar='$CI_PROJECT_DIR/build')
  parser.add_argument('--mode', '-m', type=str, required=True,
                      help='debug or release', metavar='release')
  args = vars(parser.parse_args())
  pro_file = args['pro_file']
  build_dir = args['build_dir']
  mode = args['mode']
  qtciutil.build(pro_file, build_dir, mode)

# python build.py -p F:/workspace/l2m2/xxx/src/xxx.pro -b F:/workspace/l2m2/xxx/build -m debug
# python build.py -p F:/workspace/l2m2/xxx/src/xxx.pro -b F:/workspace/l2m2/xxx/build -m release