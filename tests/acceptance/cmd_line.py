import sys
import os
import cProfile, pstats, StringIO


def main():
    drive, path = os.path.splitdrive(os.path.abspath(__file__))
    paths = path.split('\\')
    anvil_path = os.path.join(*[drive, '\\'] + paths[:-3])
    anvil_tests_path = os.path.join(*[drive, '\\'] + paths[:-2])
    env_path = os.path.join(os.getenv('HOME'), 'Envs\\anvil\\Lib\\site-packages')
    sys.path.append(anvil_path)
    sys.path.append(env_path)
    sys.path.append(anvil_tests_path)
    print('\n\nAdded paths:\n\n%s\n%s\n%s\n\n' % (anvil_path, env_path, anvil_tests_path))

    import anvil
    import tests
    import tests.acceptance.test_biped_average_time as t
    anvil.log.set_all_log_levels(anvil.log.logging.CRITICAL)

    pr = cProfile.Profile()
    pr.enable()

    # r.TestBaseRig.build_dependencies()
    t.TestProfileBiped.from_template_file(t.TestProfileBiped.TPOSE)

    pr.disable()
    s = StringIO.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats(20)
    ps.dump_stats(os.path.join(os.getenv('HOME'), 'anvil', 'runstats.prof'))


if __name__ == '__main__':
    main()
