# encoding: utf-8

import argparse
import qtciutil

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Build Arg Parser')
  parser.add_argument('--pro_file', '-p', type=str, required=True,
                      help='pro path', metavar='$CI_PROJECT_DIR/test/something.pro')
  parser.add_argument('--build_dir', '-b', type=str, required=True,
                      help='build directory', metavar='$CI_PROJECT_DIR/build')
  parser.add_argument('--dist_dir', '-d', type=str, required=True,
                      help='dist directory', metavar='$CI_PROJECT_DIR/dist')
  args = vars(parser.parse_args())
  pro_file = args['pro_file']
  build_dir = args['build_dir']
  dist_dir = args['dist_dir']
  qtciutil.unit_test(pro_file, build_dir, dist_dir)

# python test.py -p F:/workspace/l2m2/xxx/test/test.pro -b F:/workspace/l2m2/xxx/test/build -d F:/workspace/l2m2/xxx/dist