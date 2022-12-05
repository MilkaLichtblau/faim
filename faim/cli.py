from pathlib import Path
from typing import Tuple

import typer

app = typer.Typer(name="faim", help="FAIM CLI")
experiment_app = typer.Typer(name="experiment", help="reproduce experiments found in FAIM paper by Zehlike et al.")
app.add_typer(experiment_app)

synthetic_two_group_normal_experiment_app = typer.Typer(
    name="synthetic-two-group-normal",
    help="experiment with synthetic two-group data generated with prediction and ground truth scores sampled "
    "from a two dimensional normal distribution (synthetic dataset from in paper)",
)
experiment_app.add_typer(synthetic_two_group_normal_experiment_app)
compas_experiment_app = typer.Typer(name="compas", help="experiment with compas data")
experiment_app.add_typer(compas_experiment_app)
zalando_experiment_app = typer.Typer(name="zalando", help="experiment with Zalando data (coming soon)")
experiment_app.add_typer(zalando_experiment_app, name="zalando")

train_app = typer.Typer(name="train", help="train a FAIM post processing model")
app.add_typer(train_app)

post_process_app = typer.Typer(name="transform-scores", help="transform scores (with group-ids) given a FAIM model")
app.add_typer(post_process_app)


@synthetic_two_group_normal_experiment_app.command(
    "prepare-data", help="Generate two group synthetic distribution sampling from a 2-D correlated normal distribution."
)
def prepare_synthetic_two_group_normal_experiment_dataset(
    output_dir: Path = typer.Option(Path("prepared-data/synthetic-2groups"), help="prepared data output directory"),
    group1: Tuple[str, int, float, float, float] = typer.Option(
        ("disadvantaged", 100000, -1, -3, 0.8),
        help="group 1 statistics: number of examples, mean ground truth score, mean predicted score, and covariance between the two",
    ),
    group2: Tuple[str, int, float, float, float] = typer.Option(
        ("privileged", 100000, 1, 2, 0.8),
        help="group 2 statistics: number of examples, mean ground truth score, mean predicted score, and covariance between the two",
    ),
) -> None:
    ...


if __name__ == "__main__":
    app()
