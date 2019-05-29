# Copyright 2018 The TensorFlow Authors All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Contextual bandit algorithm that selects an action uniformly at random."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

from core.bandits.core.bandit_algorithm import BanditAlgorithm


class UniformSampling(BanditAlgorithm):
  """Defines a baseline; returns one action uniformly at random."""

  def __init__(self, name, hparams):
    """Creates a UniformSampling object.

    Args:
      name: Name of the algorithm.
      hparams: Hyper-parameters, including the number of arms (num_actions).
    """

    self.name = name
    self.hparams = hparams

  def action(self, context):
    """Selects an action uniformly at random."""
    return np.random.choice(range(self.hparams.num_actions))
