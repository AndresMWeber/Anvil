import click
import sys
import os
import cProfile, pstats, StringIO
import unittest

drive, path = os.path.splitdrive(os.path.abspath(__file__))
paths = path.split('\\')
anvil_path = os.path.join(*[drive, '\\'] + paths[:-3])
anvil_tests_path = os.path.join(*[drive, '\\'] + paths[:-2])
env_path = os.path.join(os.getenv('HOME'), 'Envs\\anvil\\Lib\\site-packages')

sys.path.append(anvil_path)
sys.path.append(env_path)
sys.path.append(anvil_tests_path)

import anvil
anvil.log.set_all_log_levels(anvil.log.logging.CRITICAL)



@click.command()
@click.option('--test_runner', default='biped', help='Which suite to run (control, biped, mvp)')
def main(test_runner='test_full_input'):
    pr = cProfile.Profile()
    pr.enable()
    locals()['run_%s' % test_runner]()

    pr.disable()
    s = StringIO.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats(20)
    ps.dump_stats(os.path.join(os.getenv('HOME'), 'anvil', 'runstats.prof'))


def run_control():
    import tests.test_control as tc
    suite = unittest.TestSuite()
    suite.addTest(tc.TestControlBuild('test_full_input'))
    unittest.TextTestRunner().run(suite)


def run_biped():
    import tests.acceptance.test_biped as t
    suite = unittest.TestSuite()
    suite.addTest(t.TestBuildBiped('test_build_with_parent_t_pose'))
    unittest.TextTestRunner().run(suite)


def run_mvp():
    import tests.acceptance.test_MVP as tm
    suite = unittest.TestSuite()
    suite.addTest(tm.TestRigEyeBuild('test_control_created'))
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    main()
