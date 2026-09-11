'''
Object State Persistence with Pickle
Scenario
A machine learning experiment tracker records trained model hyperparameters and validation metrics. 
Researchers need to serialize experiment sessions to disk and reload them seamlessly.

Problem Description
Create a class ExperimentSnapshot with:
Attributes: experiment_id (str), model_type (str), hyperparameters (dict), metrics (dict), timestamp (str).
Method get_best_metric(metric_name): Returns the numeric score for metric_name from metrics.
Create two helper functions:
save_experiment(snapshot, file_path): Serializes the ExperimentSnapshot object to file_path in binary mode using pickle.dump().
load_experiment(file_path): Deserializes and returns the ExperimentSnapshot instance from file_path. If the file does not exist, 
raises FileNotFoundError.
Example Walkthrough
exp = ExperimentSnapshot(
    experiment_id="EXP-2026-001",
    model_type="RandomForest",
    hyperparameters={"n_estimators": 100, "max_depth": 10},
    metrics={"accuracy": 0.942, "f1_score": 0.938},
    timestamp="2026-09-01 10:00:00"
)

save_experiment(exp, "experiment_01.pkl")

restored_exp = load_experiment("experiment_01.pkl")
print(restored_exp.model_type)                    # Output: RandomForest
print(restored_exp.get_best_metric("accuracy"))   # Output: 0.942

'''
import pickle


class ExperimentSnapshot:

    def __init__(
        self,
        experiment_id,
        model_type,
        hyperparameters,
        metrics,
        timestamp
    ):
        self.experiment_id = experiment_id
        self.model_type = model_type
        self.hyperparameters = hyperparameters
        self.metrics = metrics
        self.timestamp = timestamp

    def get_best_metric(self, metric_name):
        return self.metrics[metric_name]


def save_experiment(snapshot, file_path):

    with open(file_path, mode="wb") as file:
        pickle.dump(snapshot, file)


def load_experiment(file_path):

    with open(file_path, mode="rb") as file:
        snapshot = pickle.load(file)

    return snapshot




exp = ExperimentSnapshot(
    experiment_id="EXP-2026-001",
    model_type="RandomForest",
    hyperparameters={
        "n_estimators": 100,
        "max_depth": 10
    },
    metrics={
        "accuracy": 0.942,
        "f1_score": 0.938
    },
    timestamp="2026-09-01 10:00:00"
)


save_experiment(exp, "experiment_01.pkl")

restored_exp = load_experiment("experiment_01.pkl")

print(restored_exp.model_type)
print(restored_exp.get_best_metric("accuracy"))