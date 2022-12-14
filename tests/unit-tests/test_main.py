import tempfile
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

from faim.main import main


def test_main_prepare_synthetic_data() -> None:
    # GIVEN temporary location for stored data
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir = Path(temp_dir)

        with patch("faim.main.OUTPUT_DIR", temp_dir):
            expected_prepared_data_directory = Path(
                f"{temp_dir}/synthetic/2groups/{datetime.today().strftime('%Y-%m-%d')}"
            )

            # WHEN prepare-data invoked via CLI
            main(["--prepare-data", "synthetic-generated"])

            # THEN prepared dataset exists
            assert (expected_prepared_data_directory / "dataset.csv").exists()
