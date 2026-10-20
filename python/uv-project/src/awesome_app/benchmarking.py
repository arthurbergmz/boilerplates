from __future__ import annotations

from statistics import mean
from time import perf_counter


def _workload(name: str) -> str:
    return f"hello, {name}!"


def run_benchmark(name: str, warmup: int, iterations: int) -> dict[str, float | int]:
    """Run warmup + measured iterations and report lightweight metrics."""
    if warmup < 0:
        raise ValueError("warmup must be >= 0")
    if iterations <= 0:
        raise ValueError("iterations must be > 0")

    for _ in range(warmup):
        _workload(name)

    samples_ms: list[float] = []
    for _ in range(iterations):
        t0 = perf_counter()
        _workload(name)
        t1 = perf_counter()
        samples_ms.append((t1 - t0) * 1000.0)

    avg_ms = mean(samples_ms)
    p95_ms = sorted(samples_ms)[max(0, int(0.95 * len(samples_ms)) - 1)]

    return {
        "warmup": warmup,
        "iterations": iterations,
        "avg_latency_ms": round(avg_ms, 6),
        "p95_latency_ms": round(p95_ms, 6),
        "throughput_ops_s": round(1000.0 / avg_ms, 3) if avg_ms > 0 else float("inf"),
    }
