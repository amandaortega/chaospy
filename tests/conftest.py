import pytest


@pytest.fixture
def error_threshold():
    return 10e-10


@pytest.fixture
def assert_threshold(error_threshold, calc_absolute_error):
    def wrapper(inputs, outputs):
        err_sum = calc_absolute_error(inputs, outputs)
        assert err_sum < error_threshold, f"Outputs: {outputs}, Error: {err_sum :.3f}"

    return wrapper


@pytest.fixture
def calc_absolute_error():
    def wrapper(test: tuple = None, pred: tuple = None) -> float:
        """Calculate absolute error for test checking.

        Parameters
        ----------
        test : tuple
            coordinates array of theoretical values.
        pred : tuple
            coordinates array of calculated values.

        Returns
        -------
        err: float
            Absolute error: sum[(Xi - Yi) / Xi] / 3.

        """
        err_sum = 0
        for e1, e2 in zip(test, pred):
            div = e2 if e1 == 0 else e1
            try:
                err_sum += (e1 - e2)**2 / div**2
            except ZeroDivisionError:
                pass
        return err_sum / 3

    return wrapper
