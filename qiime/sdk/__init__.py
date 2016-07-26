# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from .method import Method
from .plugin_manager import PluginManager
from .provenance import Provenance
from .visualizer import Visualizer
from .result import Result, Artifact, Visualization
from ..core.util import parse_type

__all__ = ['Result', 'Artifact', 'Visualization', 'Method', 'Visualizer',
           'PluginManager', 'Provenance', 'parse_type']

# Various URLs
CITATION = 'http://www.ncbi.nlm.nih.gov/pubmed/20383131'
HELP_URL = 'http://2.qiime.org'
CONDA_CHANNEL = 'https://anaconda.org/qiime2'
