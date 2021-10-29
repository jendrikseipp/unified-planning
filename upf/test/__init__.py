# Copyright 2021 AIPlan4EU project
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

import unittest
from functools import wraps
from upf.environment import get_env
from upf.model.problem_kind import ProblemKind
import upf.test.pddl.enhsp


skipIf = unittest.skipIf
SkipTest = unittest.SkipTest


class skipIfSolverNotAvailable(object):
    """Skip a test if the given solver is not available."""

    def __init__(self, solver):
        self.solver = solver

    def __call__(self, test_fun):
        msg = "%s not available" % self.solver
        cond = self.solver not in get_env().factory.solvers
        @unittest.skipIf(cond, msg)
        @wraps(test_fun)
        def wrapper(*args, **kwargs):
            return test_fun(*args, **kwargs)
        return wrapper


class skipIfNoOneshotPlannerForProblemKind(object):
    """Skip a test if there are no oneshot planner for the given problem kind."""

    def __init__(self, kind: ProblemKind):
        self.kind = kind

    def __call__(self, test_fun):
        msg = "no oneshot planner available for the given problem kind"
        cond = get_env().factory._get_solver_class('oneshot_planner', problem_kind=self.kind) is None
        @unittest.skipIf(cond, msg)
        @wraps(test_fun)
        def wrapper(*args, **kwargs):
            return test_fun(*args, **kwargs)
        return wrapper


class skipIfNoPlanValidatorForProblemKind(object):
    """Skip a test if there are no plan validator for the given problem kind."""

    def __init__(self, kind: ProblemKind):
        self.kind = kind

    def __call__(self, test_fun):
        msg = "no plan validator available for the given problem kind"
        cond = get_env().factory._get_solver_class('plan_validator', problem_kind=self.kind) is None
        @unittest.skipIf(cond, msg)
        @wraps(test_fun)
        def wrapper(*args, **kwargs):
            return test_fun(*args, **kwargs)
        return wrapper


basic_classical_kind = ProblemKind()
basic_classical_kind.set_typing('FLAT_TYPING') # type: ignore

classical_kind = ProblemKind()
classical_kind.set_typing('FLAT_TYPING') # type: ignore
classical_kind.set_conditions_kind('NEGATIVE_CONDITIONS') # type: ignore
classical_kind.set_conditions_kind('DISJUNCTIVE_CONDITIONS') # type: ignore
classical_kind.set_conditions_kind('EQUALITY') # type: ignore

full_classical_kind = ProblemKind()
full_classical_kind.set_typing('FLAT_TYPING') # type: ignore
full_classical_kind.set_conditions_kind('NEGATIVE_CONDITIONS') # type: ignore
full_classical_kind.set_conditions_kind('DISJUNCTIVE_CONDITIONS') # type: ignore
full_classical_kind.set_conditions_kind('EQUALITY') # type: ignore
full_classical_kind.set_conditions_kind('EXISTENTIAL_CONDITIONS') # type: ignore
full_classical_kind.set_conditions_kind('UNIVERSAL_CONDITIONS') # type: ignore
full_classical_kind.set_effects_kind('CONDITIONAL_EFFECTS') # type: ignore

basic_numeric_kind = ProblemKind()
basic_numeric_kind.set_typing('FLAT_TYPING') # type: ignore
basic_numeric_kind.set_numbers('DISCRETE_NUMBERS') # type: ignore
basic_numeric_kind.set_numbers('CONTINUOUS_NUMBERS') # type: ignore

full_numeric_kind = ProblemKind()
full_numeric_kind.set_typing('FLAT_TYPING') # type: ignore
full_numeric_kind.set_numbers('DISCRETE_NUMBERS') # type: ignore
full_numeric_kind.set_numbers('CONTINUOUS_NUMBERS') # type: ignore
full_numeric_kind.set_effects_kind('INCREASE_EFFECTS') # type: ignore
full_numeric_kind.set_effects_kind('DECREASE_EFFECTS') # type: ignore

basic_temporal_kind = ProblemKind()
basic_temporal_kind.set_typing('FLAT_TYPING') # type: ignore
basic_temporal_kind.set_time('CONTINUOUS_TIME') # type: ignore

full_temporal_kind = ProblemKind()
full_temporal_kind.set_typing('FLAT_TYPING') # type: ignore
full_temporal_kind.set_time('CONTINUOUS_TIME') # type: ignore
full_temporal_kind.set_time('INTERMEDIATE_CONDITIONS_AND_EFFECTS') # type: ignore
full_temporal_kind.set_time('TIMED_EFFECT') # type: ignore
full_temporal_kind.set_time('TIMED_GOALS') # type: ignore
full_temporal_kind.set_time('MAINTAIN_GOALS') # type: ignore
full_temporal_kind.set_time('DURATION_INEQUALITIES') # type: ignore


TestCase = unittest.TestCase
main = unittest.main
