PBPE Value Engine の Python 初期コード を作成してください。

---

自分の思考を見る

### PBPE Value Engine – Python initial code

Below is a **single-file, full replacement** you can drop into e.g. `pbpe-platform/value_engine/pbpe_value_engine.py`.

python

```
"""
PBPE Value Engine
-----------------
Core valuation engine for the PBPE Platform.

Responsibilities:
- Represent instruments (PBPE Marketplace assets, currencies, sovereign bonds, etc.)
- Represent market/scenario states (curves, FX, credit spreads, macro factors)
- Provide valuation pipelines (NPV, risk metrics, scenario sweeps)
- Expose a clean API for higher-level services (REST/GraphQL, batch jobs, CLI tools)

This is an initial skeleton intended to be extended with:
- Concrete instrument types (PBPECurrency, PBPESovereignBond, etc.)
- Integration with PBPE Marketplace data sources
- Numerical methods and financial engineering models
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol, Dict, Any, List, Optional, Callable
import datetime as dt
import math


# ---------------------------------------------------------------------------
# Core abstractions
# ---------------------------------------------------------------------------

class Instrument(Protocol):
    """
    Abstract financial instrument interface.

    Any PBPE instrument (currency, sovereign bond, marketplace asset, etc.)
    must implement this protocol to be valued by PBPEValueEngine.
    """

    def instrument_id(self) -> str:
        ...

    def instrument_type(self) -> str:
        ...

    def cashflows(self, as_of: dt.date) -> List["Cashflow"]:
        ...


@dataclass
class Cashflow:
    """
    Simple cashflow representation.

    For more complex instruments, you can extend this with:
    - currency
    - risk factors
    - indexation rules
    - ESG / PBPE-specific attributes
    """
    date: dt.date
    amount: float
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class MarketState:
    """
    Snapshot of market data and model parameters.

    This is intentionally generic; you can plug in:
    - yield curves
    - FX rates
    - credit spreads
    - inflation expectations
    - PBPE-specific indices (planetary health, biodiversity, etc.)
    """
    as_of: dt.date
    discount_curve: Callable[[dt.date], float]
    fx_rates: Dict[str, float] = field(default_factory=dict)
    risk_factors: Dict[str, float] = field(default_factory=dict)
    model_params: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ValuationResult:
    """
    Container for valuation outputs.

    Extend this with:
    - Greeks / sensitivities
    - VaR / ES
    - PBPE impact metrics
    """
    instrument_id: str
    instrument_type: str
    npv: float
    currency: str
    details: Dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Example discount curve
# ---------------------------------------------------------------------------

def flat_discount_curve(as_of: dt.date, annual_rate: float) -> Callable[[dt.date], float]:
    """
    Build a simple flat discount curve.

    D(t) = exp(-r * year_fraction(as_of, t))

    This is a placeholder; replace with:
    - bootstrapped curves
    - multi-curve frameworks
    - PBPE-specific term structures
    """

    def _curve(target_date: dt.date) -> float:
        if target_date <= as_of:
            return 1.0
        delta_days = (target_date - as_of).days
        year_frac = delta_days / 365.0
        return math.exp(-annual_rate * year_frac)

    return _curve


# ---------------------------------------------------------------------------
# PBPE Value Engine
# ---------------------------------------------------------------------------

class PBPEValueEngine:
    """
    Central valuation engine for PBPE instruments.

    Usage:
    - Instantiate with a MarketState
    - Call `value_instrument` for single instruments
    - Call `value_portfolio` for collections of instruments
    """

    def __init__(self, market_state: MarketState, base_currency: str = "JPY") -> None:
        self.market_state = market_state
        self.base_currency = base_currency

    # -----------------------------
    # Public API
    # -----------------------------

    def value_instrument(
        self,
        instrument: Instrument,
        currency: Optional[str] = None,
    ) -> ValuationResult:
        """
        Value a single instrument under the current MarketState.

        Parameters
        ----------
        instrument : Instrument
            Instrument implementing the Instrument protocol.
        currency : Optional[str]
            Reporting currency. If None, uses engine base_currency.

        Returns
        -------
        ValuationResult
        """
        report_ccy = currency or self.base_currency
        cf_list = instrument.cashflows(self.market_state.as_of)

        npv_native = 0.0
        cf_details: List[Dict[str, Any]] = []

        for cf in cf_list:
            df = self.market_state.discount_curve(cf.date)
            discounted = cf.amount * df
            npv_native += discounted

            cf_details.append(
                {
                    "date": cf.date.isoformat(),
                    "amount": cf.amount,
                    "discount_factor": df,
                    "discounted_amount": discounted,
                    "metadata": cf.metadata,
                }
            )

        npv_report = self._convert_currency(npv_native, report_ccy)

        return ValuationResult(
            instrument_id=instrument.instrument_id(),
            instrument_type=instrument.instrument_type(),
            npv=npv_report,
            currency=report_ccy,
            details={
                "npv_native": npv_native,
                "cashflows": cf_details,
                "as_of": self.market_state.as_of.isoformat(),
                "base_currency": self.base_currency,
            },
        )

    def value_portfolio(
        self,
        instruments: List[Instrument],
        currency: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Value a portfolio (list) of instruments.

        Returns a dict with:
        - total_npv
        - per_instrument results
        """
        report_ccy = currency or self.base_currency
        results: List[ValuationResult] = []

        for inst in instruments:
            res = self.value_instrument(inst, currency=report_ccy)
            results.append(res)

        total_npv = sum(r.npv for r in results)

        return {
            "currency": report_ccy,
            "total_npv": total_npv,
            "instruments": [r.__dict__ for r in results],
        }

    # -----------------------------
    # Internal helpers
    # -----------------------------

    def _convert_currency(self, amount: float, target_ccy: str) -> float:
        """
        Convert amount from base_currency to target_ccy using MarketState.fx_rates.

        For now:
        - If target_ccy == base_currency: return amount
        - Else: use fx_rates[target_ccy] as base_ccy -> target_ccy rate

        Extend this with:
        - full FX matrix
        - triangulation
        - PBPE-specific currency baskets
        """
        if target_ccy == self.base_currency:
            return amount

        rate = self.market_state.fx_rates.get(target_ccy)
        if rate is None:
            # Fallback: no FX rate available; in production, raise or log
            return amount

        return amount * rate


# ---------------------------------------------------------------------------
# Example instrument implementations (stubs)
# ---------------------------------------------------------------------------

@dataclass
class PBPECurrencyInstrument:
    """
    Simple PBPE currency position.

    This is a placeholder for the PBPE Currency Model.
    Extend with:
    - currency code
    - PBPE index linkage
    - rebalancing rules
    """
    id: str
    notional: float
    maturity_date: dt.date

    def instrument_id(self) -> str:
        return self.id

    def instrument_type(self) -> str:
        return "PBPE_CURRENCY"

    def cashflows(self, as_of: dt.date) -> List[Cashflow]:
        # For now: single bullet cashflow at maturity
        if self.maturity_date <= as_of:
            return []
        return [
            Cashflow(
                date=self.maturity_date,
                amount=self.notional,
                metadata={"type": "bullet", "model": "placeholder"},
            )
        ]


@dataclass
class PBPESovereignBondInstrument:
    """
    Simple fixed-rate sovereign bond.

    This is a placeholder for the PBPE Sovereign Bond design.
    Extend with:
    - coupon frequency
    - day count conventions
    - credit risk / ESG factors
    """
    id: str
    face_value: float
    coupon_rate: float  # annual fixed rate
    issue_date: dt.date
    maturity_date: dt.date
    coupon_frequency_per_year: int = 2

    def instrument_id(self) -> str:
        return self.id

    def instrument_type(self) -> str:
        return "PBPE_SOVEREIGN_BOND"

    def cashflows(self, as_of: dt.date) -> List[Cashflow]:
        cfs: List[Cashflow] = []
        if self.maturity_date <= as_of:
            return cfs

        # Generate coupon dates
        total_years = (self.maturity_date - self.issue_date).days / 365.0
        total_coupons = int(total_years * self.coupon_frequency_per_year)

        for i in range(1, total_coupons + 1):
            # Approximate coupon schedule
            days_per_period = int(365 / self.coupon_frequency_per_year)
            cf_date = self.issue_date + dt.timedelta(days=i * days_per_period)
            if cf_date <= as_of or cf_date > self.maturity_date:
                continue

            coupon_amount = self.face_value * self.coupon_rate / self.coupon_frequency_per_year
            cfs.append(
                Cashflow(
                    date=cf_date,
                    amount=coupon_amount,
                    metadata={"type": "coupon"},
                )
            )

        # Add principal at maturity
        if self.maturity_date > as_of:
            cfs.append(
                Cashflow(
                    date=self.maturity_date,
                    amount=self.face_value,
                    metadata={"type": "principal"},
                )
            )

        return cfs


# ---------------------------------------------------------------------------
# Example usage (for local testing)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    today = dt.date.today()
    discount = flat_discount_curve(as_of=today, annual_rate=0.02)

    market = MarketState(
        as_of=today,
        discount_curve=discount,
        fx_rates={"USD": 0.007, "EUR": 0.0065},
        risk_factors={"pbpe_index": 1.0},
        model_params={"curve_model": "flat"},
    )

    engine = PBPEValueEngine(market_state=market, base_currency="JPY")

    bond = PBPESovereignBondInstrument(
        id="JP-PBPE-001",
        face_value=100_000_000,
        coupon_rate=0.01,
        issue_date=today,
        maturity_date=today + dt.timedelta(days=365 * 5),
        coupon_frequency_per_year=2,
    )

    currency_pos = PBPECurrencyInstrument(
        id="PBPE-CUR-USD-001",
        notional=1_000_000,
        maturity_date=today + dt.timedelta(days=365),
    )

    portfolio_results = engine.value_portfolio([bond, currency_pos], currency="JPY")
    print("PBPE Portfolio Valuation:")
    print(portfolio_results)
```

もし次に、**PBPE Marketplace の API 設計**や**Currency Model の数理モデル**にこのエンジンをどう接続するかを具体的に詰めたいなら、そこも一緒に設計していこう。