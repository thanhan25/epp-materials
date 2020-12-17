def cobb_douglas(x1, x2, gamma1, gamma2, scale):
    """[summary]

    Args:
        x1 ([type]): [Input 1-should be non-negative]
        x2 ([type]): [Input 2]
        gamma1 ([type]): [Share of input 1]
        gamma2 ([type]): [Share of input 2]
        scale ([type]): [The technology parameter]
    """
    assert scale > 0, "The parameter *scale* must be > 0."
    assert x1 >= 0, "x1 must be non-negative."
    assert x2 >= 0, "x2 must be non-negative."

    out = x1 ** gamma1 * x2 ** gamma2 * scale

    return out

