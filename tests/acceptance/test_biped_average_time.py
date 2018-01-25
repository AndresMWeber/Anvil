from tests.base_test import TestBase, cleanup_nodes
import test_build_biped
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import cProfile as profile
import unittest


@unittest.skip
class TestProfileBiped(test_build_biped.TestBaseTemplateRigs):
    def test_pycall_graph(self):
        with cleanup_nodes():
            with PyCallGraph(output=GraphvizOutput()):
                self.from_template_file(self.TPOSE)

    def test_cprofiler(self):
        with cleanup_nodes():
            profile.runctx('self.from_template_file(self.TPOSE)', globals(), locals())

    # def test_cprofiler_quiet_logging(self):
    #    with cleanup_nodes():
    #        cProfile.run('self.from_template_file(self.TPOSE)')
