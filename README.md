# Recloser–Fuse Coordination on an 11 kV Feeder with Rooftop Solar (SSEG)

**Protection Engineering Project Series · SA / SADC Region**

## Overview

A full protection coordination study of an 11 kV suburban distribution feeder
experiencing SSEG (rooftop solar PV) penetration under NRS 097-2-1:2024.

The study demonstrates how SSEG infeed degrades recloser-fuse coordination,
quantifies the degradation, and evaluates three protection philosophy options.

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
| 2       | Pre-SSEG baseline network and fault study     | Pending  |
| 3       | SSEG integration and coordination degradation | Pending  |
| 4       | Protection philosophy decision                | Pending  |
| 5       | Senior analysis and stress testing            | Pending  |

## Standards Referenced

- NRS 097-2-1:2024 — SSEG interconnection
- NRS 034 — Distribution network planning
- IEC 60255 — Measuring relays and protection equipment
- IEEE 1547-2018 — DER interconnection

## Running the Study

    source opendss_env/bin/activate
    python scripts/run_study.py --section 2
