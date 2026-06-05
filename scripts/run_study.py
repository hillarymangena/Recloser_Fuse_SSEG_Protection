"""
run_study.py
Project 2 — Recloser-Fuse Coordination with SSEG
Western Cape 11 kV Distribution Feeder

Orchestrates OpenDSS fault study execution, result extraction, and plotting.
Each section of the study is called as a separate function to keep the
execution flow traceable and results reproducible.

Usage:
    python run_study.py --section 2          # Baseline fault study
    python run_study.py --section 3          # Post-SSEG fault study
    python run_study.py --section 4 --opt A  # Philosophy option evaluation
"""

import opendssdirect as dss
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).parent.parent
DSS_DIR      = PROJECT_ROOT / "dss"
OUTPUTS_DIR  = PROJECT_ROOT / "outputs"
PLOTS_DIR    = OUTPUTS_DIR / "plots"
REPORTS_DIR  = OUTPUTS_DIR / "reports"

MASTER_DSS   = DSS_DIR / "master.dss"


def initialise_opendss() -> bool:
    """Start the OpenDSS engine and load the master file."""
    dss.Basic.Start(0)
    dss.run_command(f'Redirect "{MASTER_DSS}"')
    if dss.Solution.Converged():
        print(f"OpenDSS engine v{dss.__version__} — solution converged.")
        return True
    print("WARNING: solution did not converge — check DSS files.")
    return False


def main():
    parser = argparse.ArgumentParser(description="Project 2 protection study runner")
    parser.add_argument("--section", type=int, choices=[2, 3, 4, 5], required=True)
    parser.add_argument("--opt", type=str, choices=["A", "B", "C"], default=None)
    args = parser.parse_args()

    if not initialise_opendss():
        return

    # Section-specific runners will be imported and called here as each
    # section is built out. Stubs are added progressively.
    print(f"Section {args.section} runner — to be implemented.")


if __name__ == "__main__":
    main()
