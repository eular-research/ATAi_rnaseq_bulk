import os
import subprocess
import yaml

# List of environments to merge
environments = [
    "/workspaces/ATAi/work/conda/env-02e912e5493401ee96c01e25c1cc2e9e",
    "/workspaces/ATAi/work/conda/env-0ed4d42aea979745229b05428392403b",
    "/workspaces/ATAi/work/conda/env-15bcbcafbc433f290c3f1944a2964818",
    "/workspaces/ATAi/work/conda/env-248d30c220c836f11b9e719864c010e3",
    "/workspaces/ATAi/work/conda/env-24cd3100ff2e2afc856ebfe4bcec757a",
    "/workspaces/ATAi/work/conda/env-280b48b715fe2a4ff84587983176f97b",
    "/workspaces/ATAi/work/conda/env-2bc204c818304aa952af4c8c6e577f71",
    "/workspaces/ATAi/work/conda/env-3b5d56f28b7df4af6d1c33dc602a1280",
    "/workspaces/ATAi/work/conda/env-4303b68aca571cfaab6c0ae855606060",
    "/workspaces/ATAi/work/conda/env-49dea791c31ead673ed2e341e1c6d206",
    "/workspaces/ATAi/work/conda/env-5378deb2578a66435a64a62464238ab2",
    "/workspaces/ATAi/work/conda/env-865439183fdfc38f229ad4739ca08e17",
    "/workspaces/ATAi/work/conda/env-8dafdac3843d8f8edf2f9907029bda58",
    "/workspaces/ATAi/work/conda/env-9010272060ace4807009551e504af614",
    "/workspaces/ATAi/work/conda/env-98aca5c7395fd1bfae8d5af850ea3545",
    "/workspaces/ATAi/work/conda/env-a050ae49755c7d5e154ba21c01d4f5f0",
    "/workspaces/ATAi/work/conda/env-a8e9dfd073e20bdebda0cd2f51fe3a39",
    "/workspaces/ATAi/work/conda/env-af31d14a70ba35b8e1664c6e78dc578a",
    "/workspaces/ATAi/work/conda/env-b1ed1237d5bc91c71de950225cd4d65c",
    "/workspaces/ATAi/work/conda/env-b9e7e4eab62d21353df0b7c36adb9f06",
    "/workspaces/ATAi/work/conda/env-bcafc3992c37424ad98c9281ceb775e4",
    "/workspaces/ATAi/work/conda/env-da7440775b635c30a88d90b34559eb3b",
    "/workspaces/ATAi/work/conda/env-dea975bc60e7d15228328deea337b765",
    "/workspaces/ATAi/work/conda/env-e9df3e1229ffdcc8b4b9e48f04ba2d94",
    "/workspaces/ATAi/work/conda/env-f9036bf12aff90859cd805f3a32a03bf"
]

# Directory to store temporary YAML files
temp_dir = "/tmp/conda_envs"
os.makedirs(temp_dir, exist_ok=True)

# Export each environment to a YAML file
for env in environments:
    env_name = env.split("/")[-1]
    yaml_file = os.path.join(temp_dir, f"{env_name}.yaml")
    subprocess.run(f"conda env export -p {env} > {yaml_file}", shell=True)

# Combine YAML files
merged_env = {
    'name': 'merged_env',
    'channels': [],
    'dependencies': []
}

# Set to keep track of unique dependencies without versions
unique_dependencies = set()

for yaml_file in os.listdir(temp_dir):
    with open(os.path.join(temp_dir, yaml_file), "r") as f:
        env_data = yaml.safe_load(f)
        if 'channels' in env_data:
            merged_env['channels'].extend(env_data['channels'])
        if 'dependencies' in env_data:
            for dep in env_data['dependencies']:
                if isinstance(dep, str):  # Ignore sub-sections like 'pip'
                    # Remove version information and channel
                    dep_name = dep.split('=')[0].split('::')[-1]
                    unique_dependencies.add(dep_name)

# Remove duplicates while preserving order
merged_env['channels'] = list(dict.fromkeys(merged_env['channels']))
merged_env['dependencies'] = list(unique_dependencies)

# Write merged YAML
with open("/tmp/merged_env.yaml", "w") as f:
    yaml.dump(merged_env, f, default_flow_style=False)

# Print the contents of the merged YAML file for debugging
with open("/tmp/merged_env.yaml", "r") as f:
    print(f.read())

# Create the new environment
subprocess.run("conda env create -f /tmp/merged_env.yaml", shell=True)
