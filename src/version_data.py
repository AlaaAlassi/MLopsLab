import wandb


with open ("my_artifact.txt", "w+") as fb:
    fb.write("This is a test artifact")

run = wandb.init(project="demo_artifact_1,group=experiment_1")

artifact = wandb.Artifact("my_artifact.txt", type="data",description="This is a test artifact",metadata={"key_1": "val_1"})
artifact.add_file("my_artifact.txt")
run.log_artifact(artifact)
run.finish()
# The artifact is now uploaded to W&B and can be accessed through the W&B UI.