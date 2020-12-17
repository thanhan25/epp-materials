"""Calculate the CRRA utility value of consumption values."""


def utility_crra(argument, exponent):
    """Return the CRRA utility evaluation of *argument* where the Arrow-Pratt
    coefficient of relative risk aversion takes on the value *exponent*.

    Neither handle cases where *argument* is less than nor log utility.

    """

    assert argument >= 0, "Only positive quantities allowed for *argument*."
    assert exponent != 1, "No provision made for log utility."

    numerator = argument ** (1.0 - exponent)
    denominator = 1.0 - exponent
    out = numerator / denominator
    return out


if __name__ == "__main__":
    consumption = 1600
    coefficient_rra = 1.5
    utility = utility_crra(consumption, coefficient_rra)
    print("Utility evaluation", utility)
