"""CLI Tasks reproduction gate (pipeline.clitasks_repro, unchanged) for shipped zips, on the configured repro workspace:
stock Harbor, the oracle must score 1.0 and the untouched fixture 0.0.
usage: python orchestration/repro.py <zip> [<zip> ...]"""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from orchestration import config  # noqa: E402
from pipeline import policy  # noqa: E402
policy.CLITASKS_REPRO_WORKSPACE = config.repro_workspace()
from pipeline import clitasks_repro  # noqa: E402
sys.exit(clitasks_repro.main(sys.argv[1:]))
