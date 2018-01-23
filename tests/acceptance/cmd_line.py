import sys
import os

drive, path = os.path.splitdrive(os.path.abspath(__file__))
paths = path.split('\\')
anvil_path = os.path.join(*[drive, '\\'] + paths[:-3])
anvil_tests_path = os.path.join(*[drive, '\\'] + paths[:-2])
env_path = 'C:\\Users\\Daemonecles\\Envs\\anvil\\Lib\\site-packages\\'
sys.path.append(anvil_path)
sys.path.append(env_path)
sys.path.append(anvil_tests_path)
print('Added paths:\n%s\n%s' % (anvil_path, env_path))

import anvil
import tests
import tests.acceptance.test_biped_average_time as t

import cProfile, pstats, StringIO

pr = cProfile.Profile()
pr.enable()
t.TestProfileBiped.from_template_file(t.TestProfileBiped.TPOSE)

pr.disable()
s = StringIO.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
ps.print_stats()
ps.dump_stats(os.path.join(os.getenv('HOME'), 'anvil', 'profiler'))
