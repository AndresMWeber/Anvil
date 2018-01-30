from tests.base_test import cleanup_nodes
import test_build_biped
import os
import unittest


class TestProfileBiped(test_build_biped.TestBaseTemplateRigs):
    @unittest.skipIf(os.getenv('ANVIL_PYCALLGRAPH') is None, 'Env var ANVIL_PYCALLGRAPH not set.')
    def test_pycall_graph(self):
        from pycallgraph import PyCallGraph
        from pycallgraph.output import GraphvizOutput
        with cleanup_nodes():
            with PyCallGraph(output=GraphvizOutput()):
                self.from_template_file(self.TPOSE)

    @unittest.skipIf(os.getenv('ANVIL_CPROFILE') is None, 'Env var ANVIL_CPROFILE not set.')
    def test_cprofiler(self):
        import cProfile as profile
        with cleanup_nodes():
            profile.runctx('self.from_template_file(self.TPOSE)', globals(), locals())
