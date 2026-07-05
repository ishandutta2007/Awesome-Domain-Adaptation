import os
import re

base_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Domain-Adaptation"
pages_dir = os.path.join(base_dir, "pages")
os.makedirs(pages_dir, exist_ok=True)

pages_data = [
    ("The Statistical Moment Matching Era (Traditional Machine Learning Baseline)", "statistical_moment_matching.md", "Detailed information on Statistical Moment Matching.\n\n```mermaid\ngraph TD\nA[Source Domain] --> B[Calculate Source Moments]\nC[Target Domain] --> D[Calculate Target Moments]\nB --> E[Align Moments CORAL/MMD]\nD --> E\nE --> F[Domain-Invariant Features]\n```"),
    ("The Deep Adversarial Representation Era (DANN / Adversarial Space Mapping, ~2016–2020)", "deep_adversarial_representation.md", "Detailed information on Deep Adversarial Representation.\n\n```mermaid\ngraph TD\nA[Features] --> B[Gradient Reversal Layer]\nB --> C[Domain Discriminator]\n```"),
    ("The Self-Supervised Contrastive Alignment Era (~2020–2024)", "self_supervised_contrastive.md", "Detailed information on Self-Supervised Contrastive Alignment.\n\n```mermaid\ngraph LR\nA[Augmented View 1] --> C[Encoder]\nB[Augmented View 2] --> C\nC --> D[Contrastive Loss]\n```"),
    ("The Foundation Model & Monosemantic Dictionary Steering Era (Present)", "foundation_model_steering.md", "Detailed information on Foundation Models and Steering.\n\n```mermaid\ngraph TD\nA[Frozen Model] --> B[Sparse Autoencoder]\nB --> C[Monosemantic Features]\nC --> D[Activation Steering Vectors]\n```"),
    ("A. Unsupervised Domain Adaptation (UDA)", "uda.md", "Detailed information on Unsupervised Domain Adaptation.\n\n```mermaid\ngraph LR\nA[Labeled Source] --> C[Model]\nB[Unlabeled Target] --> C\nC --> D[Adapted Model]\n```"),
    ("B. Semi-Supervised Domain Adaptation (SSDA)", "ssda.md", "Detailed information on Semi-Supervised Domain Adaptation.\n\n```mermaid\ngraph LR\nA[Labeled Source] --> C[Model]\nB[Few Labeled Target] --> C\nD[Unlabeled Target] --> C\n```"),
    ("C. Few-Shot Domain Adaptation / In-Context Adaptation", "few_shot_da.md", "Detailed information on Few-Shot / In-Context DA.\n\n```mermaid\ngraph TD\nA[Few Target Exemplars] --> B[Prompt Prefix]\nB --> C[Frozen LLM/Transformer]\n```"),
    ("D. Source-Free Domain Adaptation (SFDA)", "sfda.md", "Detailed information on Source-Free Domain Adaptation.\n\n```mermaid\ngraph LR\nA[Pre-trained Source Model] --> B[Adaptation on Unlabeled Target]\nB --> C[Adapted Target Model]\n```"),
    ("Gradient Reversal Layers (GRL Hooks)", "grl_hooks.md", "Detailed information on Gradient Reversal Layers.\n\n```mermaid\ngraph TD\nA[Forward Pass: Identity] --> B[Backward Pass: Multiply by -lambda]\n```"),
    ("Maximum Mean Discrepancy (MMD) Regularizers", "mmd_regularizers.md", "Detailed information on MMD Regularizers.\n\n```mermaid\ngraph LR\nA[Source Features] --> C[Kernel Mapping]\nB[Target Features] --> C\nC --> D[MMD Distance]\n```"),
    ("The Negative Transfer and Capability Collapse Wall", "negative_transfer.md", "Detailed information on Negative Transfer.\n\n```mermaid\ngraph TD\nA[Over-optimization] --> B[Feature Boundary Destruction]\nB --> C[Capability Collapse]\n```"),
    ("The Distributed Cross-Domain Batch Load-Imbalance Stall", "load_imbalance.md", "Detailed information on Batch Load-Imbalance.\n\n```mermaid\ngraph LR\nA[Source Batch Fast] --> C[Wait/Stall]\nB[Target Batch Slow] --> C\nC --> D[Symmetric Tensor Bucketing]\n```"),
    ("Sim-to-Real Trajectory Adaptation for Advanced Robotics & Humanoids", "sim_to_real_robotics.md", "Detailed information on Sim-to-Real Robotics Adaptation.\n\n```mermaid\ngraph TD\nA[Simulation Environment] --> B[Domain Randomization]\nB --> C[Real World Deployment]\n```"),
    ("Cross-Camera Perception Alignment for Autonomous Vehicle Fleets", "cross_camera_av.md", "Detailed information on Cross-Camera AV Alignment.\n\n```mermaid\ngraph LR\nA[Sunlit City] --> C[Adversarial Alignment]\nB[Snowstorm] --> C\nC --> D[Robust Perception]\n```"),
    ("Cross-Institutional HIPAA-Compliant Clinical Pathology Diagnostics", "clinical_pathology.md", "Detailed information on Clinical Pathology Diagnostics.\n\n```mermaid\ngraph TD\nA[Data Center A Model] --> B[Source-Free DA]\nB --> C[Data Center B Deployment]\n```")
]

for title, filename, content in pages_data:
    filepath = os.path.join(pages_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n{content}\n")

readme_path = os.path.join(base_dir, "README.md")
with open(readme_path, 'r', encoding='utf-8') as f:
    readme_content = f.text if hasattr(f, 'text') else f.read()

# Replace titles with links
for title, filename, _ in pages_data:
    # We replace exact occurrences. Since some might be inside ** ** inside a table, we should be careful.
    # The titles in tables might be slightly altered or exact.
    # Let's use string replace on the exact text.
    readme_content = readme_content.replace(f"**{title}**", f"**[{title}](pages/{filename})**")

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("Pages created and README updated.")
