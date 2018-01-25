from tests.base_test import cleanup_nodes
import test_build_biped
from pycallgraph.output import GraphvizOutput


class TestProfileBiped(test_build_biped.TestBaseTemplateRigs):
    def test_pycall_graph(self):
        try:
            from pycallgraph import PyCallGraph
            with cleanup_nodes():
                with PyCallGraph(output=GraphvizOutput()):
                    self.from_template_file(self.TPOSE)
        except ImportError:
            pass

    def test_cprofiler(self):
        try:
            import cProfile as profile

            with cleanup_nodes():
                profile.runctx('self.from_template_file(self.TPOSE)', globals(), locals())
        except ImportError:
            pass

    # def test_cprofiler_quiet_logging(self):
    #    with cleanup_nodes():
    #        cProfile.run('self.from_template_file(self.TPOSE)')
