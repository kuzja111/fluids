# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from __future__ import annotations
from typing import List
from typing import (
    Optional,
)


def Fritzsche(
    SG: float,
    Tavg: float,
    L: Optional[float] = ...,
    D: Optional[float] = ...,
    P1: Optional[float] = ...,
    P2: Optional[float] = ...,
    Q: Optional[float] = ...,
    Ts: float = ...,
    Ps: float = ...,
    Zavg: float = ...,
    E: float = ...
) -> float: ...


def IGT(
    SG: float,
    Tavg: float,
    mu: float,
    L: Optional[float] = ...,
    D: Optional[float] = ...,
    P1: Optional[float] = ...,
    P2: Optional[float] = ...,
    Q: Optional[float] = ...,
    Ts: float = ...,
    Ps: float = ...,
    Zavg: float = ...,
    E: float = ...
) -> float: ...


def Muller(
    SG: float,
    Tavg: float,
    mu: float,
    L: Optional[float] = ...,
    D: Optional[float] = ...,
    P1: Optional[float] = ...,
    P2: Optional[float] = ...,
    Q: Optional[float] = ...,
    Ts: float = ...,
    Ps: float = ...,
    Zavg: float = ...,
    E: float = ...
) -> float: ...


def Oliphant(
    SG: float,
    Tavg: float,
    L: Optional[float] = ...,
    D: Optional[float] = ...,
    P1: Optional[float] = ...,
    P2: Optional[float] = ...,
    Q: Optional[float] = ...,
    Ts: float = ...,
    Ps: float = ...,
    Zavg: float = ...,
    E: float = ...
) -> float: ...


def P_critical_flow(P: float, k: float) -> float: ...


def P_isothermal_critical_flow(P: float, fd: float, D: float, L: float) -> float: ...


def P_stagnation(P: float, T: float, Tst: float, k: float) -> float: ...


def P_upstream_isothermal_critical_flow(P: float, fd: float, D: float, L: float) -> float: ...


def Panhandle_A(
    SG: float,
    Tavg: float,
    L: Optional[float] = ...,
    D: Optional[float] = ...,
    P1: Optional[float] = ...,
    P2: Optional[float] = ...,
    Q: Optional[float] = ...,
    Ts: float = ...,
    Ps: float = ...,
    Zavg: float = ...,
    E: float = ...
) -> float: ...


def Panhandle_B(
    SG: float,
    Tavg: float,
    L: Optional[float] = ...,
    D: Optional[float] = ...,
    P1: Optional[float] = ...,
    P2: Optional[float] = ...,
    Q: Optional[float] = ...,
    Ts: float = ...,
    Ps: float = ...,
    Zavg: float = ...,
    E: float = ...
) -> float: ...


def Spitzglass_high(
    SG: float,
    Tavg: float,
    L: Optional[float] = ...,
    D: Optional[float] = ...,
    P1: Optional[float] = ...,
    P2: Optional[float] = ...,
    Q: Optional[float] = ...,
    Ts: float = ...,
    Ps: float = ...,
    Zavg: float = ...,
    E: float = ...
) -> float: ...


def Spitzglass_low(
    SG: float,
    Tavg: float,
    L: Optional[float] = ...,
    D: Optional[float] = ...,
    P1: Optional[float] = ...,
    P2: Optional[float] = ...,
    Q: Optional[float] = ...,
    Ts: float = ...,
    Ps: float = ...,
    Zavg: float = ...,
    E: float = ...
) -> float: ...


def T_critical_flow(T: float, k: float) -> float: ...


def T_stagnation(T: float, P: float, Pst: float, k: float) -> float: ...


def T_stagnation_ideal(T: float, V: float, Cp: float) -> float: ...


def Weymouth(
    SG: float,
    Tavg: float,
    L: Optional[float] = ...,
    D: Optional[float] = ...,
    P1: Optional[float] = ...,
    P2: Optional[float] = ...,
    Q: Optional[float] = ...,
    Ts: float = ...,
    Ps: float = ...,
    Zavg: float = ...,
    E: float = ...
) -> float: ...


def _to_solve_Oliphant(
    D: float,
    Q: float,
    SG: float,
    Tavg: float,
    L: float,
    P1: float,
    P2: float,
    Ts: float,
    Ps: float,
    Zavg: float,
    E: float
) -> float: ...


def _to_solve_Spitzglass_high(
    D: float,
    Q: float,
    SG: float,
    Tavg: float,
    L: float,
    P1: float,
    P2: float,
    Ts: float,
    Ps: float,
    Zavg: float,
    E: float
) -> float: ...


def _to_solve_Spitzglass_low(
    D: float,
    Q: float,
    SG: float,
    Tavg: float,
    L: float,
    P1: float,
    P2: float,
    Ts: float,
    Ps: float,
    Zavg: float,
    E: float
) -> float: ...


def is_critical_flow(P1: float, P2: float, k: float) -> bool: ...


def isentropic_T_rise_compression(
    T1: float,
    P1: float,
    P2: float,
    k: float,
    eta: float = ...
) -> float: ...


def isentropic_efficiency(
    P1: float,
    P2: float,
    k: float,
    eta_s: Optional[float] = ...,
    eta_p: Optional[float] = ...
) -> float: ...


def isentropic_work_compression(
    T1: Optional[float],
    k: float,
    Z: float = ...,
    P1: Optional[float] = ...,
    P2: Optional[float] = ...,
    W: Optional[float] = ...,
    eta: Optional[float] = ...
) -> float: ...


def isothermal_gas(
    rho: float,
    fd: float,
    P1: Optional[float] = ...,
    P2: Optional[float] = ...,
    L: Optional[float] = ...,
    D: Optional[float] = ...,
    m: Optional[float] = ...
) -> float: ...


def isothermal_gas_err_D(D: float, m: float, rho: float, fd: float, P1: float, P2: float, L: float) -> float: ...


def isothermal_gas_err_P1(
    P1: float,
    fd: float,
    rho: float,
    P2: float,
    L: float,
    D: float,
    m: float
) -> float: ...


def isothermal_gas_err_P2(
    P2: float,
    rho: float,
    fd: float,
    P1: float,
    L: float,
    D: float,
    m: float
) -> float: ...


def isothermal_gas_err_P2_basis(
    P1: float,
    P2: float,
    rho: float,
    fd: float,
    m: float,
    L: float,
    D: float
) -> float: ...


def isothermal_work_compression(P1: float, P2: float, T: float, Z: float = ...) -> float: ...


def polytropic_exponent(k: float, n: Optional[float] = ..., eta_p: Optional[float] = ...) -> float: ...


def stagnation_energy(V: float) -> float: ...

__all__: List[str]