# Recloser–Fuse Coordination on an 11 kV Feeder with Rooftop Solar (SSEG)

**Protection Engineering Project · SA / SADC Region**

## Overview

This project investigates the impact of rooftop solar PV penetration on an existing 11 kV fuse-saving protection scheme for a Western Cape municipality feeder, addressing one of the most operationally live protection challenges currently facing South African distribution utilities. With 520 kW of NRS 097-2-1-compliant SSEG connected across two laterals, the study demonstrates how inverter fault current contribution inverts the recloser-fuse coordination ratio, causing the fuse to blow before the recloser clears — invalidating the fuse-saving philosophy the scheme was built on. The work is modelled in OpenDSS via Python, covering pre- and post-SSEG fault studies, anti-islanding window analysis, and reclose timing safety assessment. Three remediation options are evaluated against NRS 097-2-1 compliance obligations, service continuity, and maintenance burden, culminating in a structured protection philosophy decision matrix. The recommended target-state solution — direct transfer trip from the recloser to SSEG inverters via GOOSE messaging — positions the feeder for increasing solar penetration under the current regulatory trajectory.
All scripts and DSS files are version-controlled and reproducible at zero cost. A notable limitation of OpenDSSDirect.py on Linux is the absence of native GUI plotting and full time-series dynamic simulation, which constrains the anti-islanding analysis to steady-state approximations. A professional study would supplement this with real-time digital simulation (RTDS or PSCAD) to capture inverter control loop behaviour during fault transients with the precision that utility commissioning decisions require.

## Tools

- OpenDSSDirect.py (OpenDSS engine, Python interface)
- Python 3.11+, NumPy, Pandas, Matplotlib
- Jupyter Lab (interactive analysis)
- Git / GitHub

## Project Structure

    recloser-fuse_coordination_project/
    ├── dss/
    │   ├── master.dss
    │   ├── network.dss
    │   ├── loads.dss
    │   ├── sseg.dss
    │   └── protection.dss
    ├── notebooks/
    ├── scripts/
    │   └── run_study.py
    ├── outputs/
    │   ├── plots/
    │   └── reports/
    └── data/

## Study Sections

| Section | Description                                   | Status   |
|---------|-----------------------------------------------|----------|
| 1       | Environment setup, project structure          | Complete |
| 2       | Pre-SSEG baseline network and fault study     | Complete  |
| 3       | SSEG integration and coordination degradation | Ongoing  |
| 4       | Protection philosophy decision                | Complete |
| 5       | Senior analysis and stress testing            | Ongoing  |

## Standards Referenced

- NRS 097-2-1:2024 — SSEG interconnection
- NRS 034 — Distribution network planning
- IEC 60255 — Measuring relays and protection equipment
- IEEE 1547-2018 — DER interconnection

## Running the Study

    source opendss_env/bin/activate
    python scripts/run_study.py --section 2
