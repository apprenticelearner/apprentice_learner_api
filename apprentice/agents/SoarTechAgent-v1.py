class BaseAgent(object):
    """
    This is essentially an abstract class for apprentice learner agents.
    """

    def __init__(self, feature_set, function_set):
        self.last_state = None
        pass

    def request(self, state):
        """
        Accepts a JSON object representing the state.

        Returns a dictionary containing selection, action, and inputs.
        """
        if self.last_state is None:
            return self.request_diff(state, [])

        pos_diff = state - self.last_state
        neg_diff = self.last_state - state

        return self.request_diff(pos_diff, neg_diff)

    def request_diff(self, state_pos_diff, state_neg_diff):
        """
        Accepts a JSON object representing diffs from the previously requested
        state. Useful for more efficiently making requests when the state
        changes only a little bit.

        Returns a dictionary containing selection, action, and inputs.
        """
        raise NotImplementedError("request function not implemented")

    def train(self, state, selection, action, inputs, reward, skill_label,
              foci_of_attention):
        """
        Accepts a JSON object representing the state, a string representing the
        skill label, a list of strings representing the foas, a string
        representing the selection, a string representing the action, list of
        strings representing the inputs, and a boolean correctness.
        """

        raise NotImplementedError("train function not implemented")

    def train_diff(self, state_pos_diff, state_neg_diff, selection, action,
                   inputs, reward, skill_label, foci_of_attention):
        """
        Accepts a JSON object representing the state, a string representing the
        skill label, a list of strings representing the foas, a string
        representing the selection, a string representing the action, list of
        strings representing the inputs, and a boolean correctness.
        """

        raise NotImplementedError("train_diff function not implemented")

    def check(self, state, selection, action, inputs):
        """
        Accepts a JSON object representing the state, a string representing the
        selection, a string representing the action, list of strings
        representing the inputs.

        Uses the learned model to determine the correctness of the provided sai
        in the provided state. Returns a boolean.
        """
        raise NotImplementedError("check function not implemented")
