# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from __future__ import annotations
from typing import List
from typing import (
    List,
    Optional,
)


def Brauer(dp: float, voidage: float, vs: float, rho: float, mu: float, L: float = ...) -> float: ...


def Carman(dp: float, voidage: float, vs: float, rho: float, mu: float, L: float = ...) -> float: ...


def Erdim_Akgiray_Demir(
    dp: float,
    voidage: float,
    vs: float,
    rho: float,
    mu: float,
    L: float = ...
) -> float: ...


def Ergun(dp: float, voidage: float, vs: float, rho: float, mu: float, L: float = ...) -> float: ...


def Fahien_Schriver(dp: float, voidage: float, vs: float, rho: float, mu: float, L: float = ...) -> float: ...


def Guo_Sun(dp: float, voidage: float, vs: float, rho: float, mu: float, Dt: float, L: float = ...) -> float: ...


def Harrison_Brunner_Hecker(
    dp: float,
    voidage: float,
    vs: float,
    rho: float,
    mu: float,
    L: int = ...,
    Dt: Optional[float] = ...
) -> float: ...


def Hicks(dp: float, voidage: float, vs: float, rho: float, mu: float, L: float = ...) -> float: ...


def Idelchik(dp: float, voidage: float, vs: float, rho: float, mu: float, L: float = ...) -> float: ...


def Jones_Krier(dp: float, voidage: float, vs: float, rho: float, mu: float, L: float = ...) -> float: ...


def KTA(dp: float, voidage: float, vs: float, rho: float, mu: float, L: float = ...) -> float: ...


def Kuo_Nydegger(dp: float, voidage: float, vs: float, rho: float, mu: float, L: float = ...) -> float: ...


def Montillet_Akkari_Comiti(
    dp: float,
    voidage: float,
    vs: float,
    rho: float,
    mu: float,
    L: float = ...,
    Dt: Optional[float] = ...
) -> float: ...


def Tallmadge(dp: float, voidage: float, vs: float, rho: float, mu: float, L: float = ...) -> float: ...


def dP_packed_bed(
    dp: float,
    voidage: float,
    vs: float,
    rho: float,
    mu: float,
    L: int = ...,
    Dt: Optional[float] = ...,
    sphericity: Optional[float] = ...,
    Method: Optional[str] = ...
) -> float: ...


def dP_packed_bed_methods(
    dp: float,
    voidage: float,
    vs: float,
    rho: float,
    mu: float,
    L: float = ...,
    Dt: Optional[float] = ...,
    check_ranges: bool = ...
) -> List[str]: ...


def voidage_Benyahia_Oneil(Dpe: float, Dt: float, sphericity: float) -> float: ...


def voidage_Benyahia_Oneil_cylindrical(Dpe: float, Dt: float, sphericity: float) -> float: ...


def voidage_Benyahia_Oneil_spherical(Dp: float, Dt: float) -> float: ...

__all__: List[str]