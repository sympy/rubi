from sympy.core.basic import Basic
from sympy.core.symbol import symbols

x = symbols('x')


def _test_args(obj):
    all_basic = all(isinstance(arg, Basic) for arg in obj.args)
    # Ideally obj.func(*obj.args) would always recreate the object, but for
    # now, we only require it for objects with non-empty .args
    recreatable = not obj.args or obj.func(*obj.args) == obj
    return all_basic and recreatable

def test_sympy__integrals__rubi__symbol__matchpyWC():
    from rubi.symbol import matchpyWC
    assert _test_args(matchpyWC(1, True, 'a'))


def test_sympy__integrals__rubi__utility_function__rubi_unevaluated_expr():
    from rubi.utility_function import rubi_unevaluated_expr
    a = symbols('a')
    assert _test_args(rubi_unevaluated_expr(a))


def test_sympy__integrals__rubi__utility_function__rubi_exp():
    from rubi.utility_function import rubi_exp
    assert _test_args(rubi_exp(5))


def test_sympy__integrals__rubi__utility_function__rubi_log():
    from rubi.utility_function import rubi_log
    assert _test_args(rubi_log(5))


def test_sympy__integrals__rubi__utility_function__Int():
    from rubi.utility_function import Int
    assert _test_args(Int(5, x))


def test_sympy__integrals__rubi__utility_function__Util_Coefficient():
    from rubi.utility_function import Util_Coefficient
    a, x = symbols('a x')
    assert _test_args(Util_Coefficient(a, x))


def test_sympy__integrals__rubi__utility_function__Gamma():
    from rubi.utility_function import Gamma
    assert _test_args(Gamma(x))


def test_sympy__integrals__rubi__utility_function__Util_Part():
    from rubi.utility_function import Util_Part
    a, b = symbols('a b')
    assert _test_args(Util_Part(a + b, 0))


def test_sympy__integrals__rubi__utility_function__PolyGamma():
    from rubi.utility_function import PolyGamma
    assert _test_args(PolyGamma(1, x))


def test_sympy__integrals__rubi__utility_function__ProductLog():
    from rubi.utility_function import ProductLog
    assert _test_args(ProductLog(1))
