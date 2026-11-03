"""Test per la gerarchia di eccezioni custom di Agentic Crypto Trader."""

from __future__ import annotations

import pytest

from src.core.exceptions import ExchangeError, LlmError, NewsError, TradingError


def test_trading_error_is_exception() -> None:
    """TradingError deve essere una sottoclasse di Exception."""
    assert issubclass(TradingError, Exception)


def test_exchange_error_is_trading_error() -> None:
    """ExchangeError deve essere una sottoclasse di TradingError."""
    assert issubclass(ExchangeError, TradingError)


def test_llm_error_is_trading_error() -> None:
    """LlmError deve essere una sottoclasse di TradingError."""
    assert issubclass(LlmError, TradingError)


def test_llm_error_is_runtime_error() -> None:
    """LlmError deve essere una sottoclasse di RuntimeError per backward compatibility."""
    assert issubclass(LlmError, RuntimeError)


def test_trading_error_is_catchable_as_exception() -> None:
    """Le eccezioni derivate da TradingError devono essere catturabili come Exception."""
    with pytest.raises(Exception):
        raise ExchangeError("binance offline")


def test_llm_error_is_catchable_as_runtime_error() -> None:
    """LlmError deve essere catturabile da un except RuntimeError (backward compat)."""
    with pytest.raises(RuntimeError):
        raise LlmError("risposta vuota")


def test_exchange_error_is_not_runtime_error() -> None:
    """ExchangeError NON deve essere un RuntimeError: le due categorie sono distinte."""
    assert not issubclass(ExchangeError, RuntimeError)


def test_news_error_is_trading_error() -> None:
    """NewsError deve essere una sottoclasse di TradingError."""
    assert issubclass(NewsError, TradingError)
