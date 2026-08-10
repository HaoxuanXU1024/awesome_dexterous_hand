# Awesome Dexterous Hand Papers

An arXiv-first reading list for three tightly scoped directions:

1. **Dexterous-hand reinforcement learning (RL)**
2. **Unified latent/action spaces for dexterous hands**
3. **Dexterous hands with tactile sensing**

The five subsections under every direction intentionally follow the same order: **CVPR 2026**, **ICML 2026**, **ECCV 2026**, **Recent arXiv**, and **Former / foundational**. Each entry gives the full paper title, a one-sentence insight, and one direct PDF link. Recent arXiv entries are sorted newest first and grouped by month.

## Contents

- [Dexterous-hand RL](#1-dexterous-hand-rl)
- [Unified latent/action spaces](#2-unified-latentaction-spaces)
- [Dexterous hand + tactile sensing](#3-dexterous-hand--tactile-sensing)

## 1. Dexterous-hand RL

### CVPR 2026

| Title | PDF | Insight |
|---|---|---|
| DemoFunGrasp: Universal Dexterous Functional Grasping via Demonstration-Editing Reinforcement Learning | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_DemoFunGrasp_Universal_Dexterous_Functional_Grasping_via_Demonstration-Editing_Reinforcement_Learning_CVPR_2026_paper.pdf) | Factorizes functional grasping into style and affordance, then turns one demonstration into a one-step RL editing problem. |
| DextER: Language-driven Dexterous Grasp Generation with Embodied Reasoning | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_DextER_Language-driven_Dexterous_Grasp_Generation_with_Embodied_Reasoning_CVPR_2026_paper.pdf) | Uses embodied reasoning to connect language-level intent to physically executable multi-finger grasps. |
| AdaDexTrack: Dynamic Modulation for Adaptive and Generalizable Dexterous Manipulation Tracking | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Adalibieke_AdaDexTrack_Dynamic_Modulation_for_Adaptive_and_Generalizable_Dexterous_Manipulation_Tracking_CVPR_2026_paper.pdf) | Dynamically modulates tracking features so a dexterous policy can follow diverse motions under distribution shift. |

### ICML 2026

Adjacent policy-learning methods are included for context and marked **adjacent**.

| Title | PDF | Insight |
|---|---|---|
| FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation | [PDF](https://arxiv.org/pdf/2606.20867) | Conditions VLA adaptation on future task context to improve sample efficiency during policy refinement. |
| VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models | [PDF](https://arxiv.org/pdf/2512.22539) | Provides a reproducible evaluation harness for comparing VLA policies across tasks and embodiments. |
| See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model | [PDF](https://arxiv.org/pdf/2605.11817) | Retains contact-relevant visual tokens with differentiable resampling instead of dropping fixed image blocks. |

### ECCV 2026

- No dexterous-hand papers listed yet.

### Recent arXiv (2025-2026)

<table>
  <thead>
    <tr><th>Month</th><th>Title</th><th>PDF</th><th>Insight</th></tr>
  </thead>
  <tbody>
    <tr><td rowspan="1"><strong>2026-08</strong></td><td><strong>01</strong> DexMani: Human-Derived Manipulability Guidance for Dexterous Rotation</td><td><a href="https://arxiv.org/pdf/2608.00554">PDF</a></td><td>Transfers human contact-conditioned manipulability evolution into a cross-embodiment prior that guides RL for robust in-hand rotation.</td></tr>
    <tr><td rowspan="4"><strong>2026-07</strong></td><td><strong>13</strong> Towards Human-level Dexterous Teleoperation</td><td><a href="https://arxiv.org/pdf/2607.11481">PDF</a></td><td>Learns a subgoal-conditioned contact controller with a hybrid reward and single-stage RL, enabling long-horizon in-hand teleoperation.</td></tr>
    <tr><td><strong>13</strong> REGRIND: A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation</td><td><a href="https://arxiv.org/pdf/2607.11874">PDF</a></td><td>Retargets one human hand-object demonstration into contact-preserving references and learns a residual RL policy around them.</td></tr>
    <tr><td><strong>13</strong> Robust In-Hand Manipulation via Priors in Reinforcement Learning and Mechanical Design</td><td><a href="https://arxiv.org/pdf/2607.12105">PDF</a></td><td>Shapes RL with global grasp-quality and local fingertip-curvature priors to improve rolling stability and disturbance rejection.</td></tr>
    <tr><td><strong>07</strong> LAMP: Latent Motion Prior-Guided Real-World Learning for Dexterous Hand Manipulation</td><td><a href="https://arxiv.org/pdf/2607.06323">PDF</a></td><td>Constrains online residual RL to a history-conditioned latent motion prior so exploration stays near contact-consistent actions.</td></tr>
    <tr><td rowspan="2"><strong>2026-06</strong></td><td><strong>22</strong> Learning Dexterous Manipulation Using Contact Wrench Guidance From Human Demonstration</td><td><a href="https://arxiv.org/pdf/2607.00033">PDF</a></td><td>Guides RL in an object-centric contact-wrench space so human demonstrations transfer to long-horizon bimanual and whole-body dexterous tasks.</td></tr>
    <tr><td><strong>08</strong> DexPIE: Stable Dexterous Policy Improvement from Real-World Experience</td><td><a href="https://arxiv.org/pdf/2606.09615">PDF</a></td><td>Uses intervention-aware data collection and staged policy improvement to make real-world dexterous adaptation stable.</td></tr>
    <tr><td rowspan="1"><strong>2026-05</strong></td><td><strong>28</strong> BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models</td><td><a href="https://arxiv.org/pdf/2605.30226">PDF</a></td><td>Bootstraps a dexterous VLA offline and improves it online through residual RL rather than relearning from scratch.</td></tr>
    <tr><td rowspan="1"><strong>2026-04</strong></td><td><strong>24</strong> RL Token: Bootstrapping Online RL with Vision-Language-Action Models</td><td><a href="https://arxiv.org/pdf/2604.23073">PDF</a></td><td>Exposes a compact token from a frozen VLA for sample-efficient online RL fine-tuning on precision manipulation tasks.</td></tr>
    <tr><td rowspan="2"><strong>2026-03</strong></td><td><strong>11</strong> ContactExplorer: Contact Coverage-Guided Exploration for General-Purpose Dexterous Manipulation</td><td><a href="https://arxiv.org/pdf/2603.10971">PDF</a></td><td>Shapes RL exploration with a contact-coverage objective that deliberately discovers new finger-object contact patterns.</td></tr>
    <tr><td><strong>01</strong> D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping</td><td><a href="https://arxiv.org/pdf/2603.01151">PDF</a></td><td>Differentiates through a real-to-sim-to-real loop so grasping policies can adapt contact dynamics with less real-robot data.</td></tr>
    <tr><td rowspan="1"><strong>2026-01</strong></td><td><strong>06</strong> Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation</td><td><a href="https://arxiv.org/pdf/2601.02778">PDF</a></td><td>Combines dense tactile and joint-torque feedback with joint-wise dynamics adaptation for zero-shot sim-to-real RL.</td></tr>
    <tr><td rowspan="1"><strong>2025-11</strong></td><td><strong>03</strong> GenDexHand: Generative Simulation for Dexterous Hands</td><td><a href="https://arxiv.org/pdf/2511.01791">PDF</a></td><td>Closes a VLM-guided environment-generation loop and decomposes tasks for scalable sequential RL training.</td></tr>
    <tr><td rowspan="2"><strong>2025-10</strong></td><td><strong>14</strong> Learning to Grasp Anything by Playing with Random Toys</td><td><a href="https://arxiv.org/pdf/2510.12866">PDF</a></td><td>Shows that object-centric visual pooling and simple compositional toys can produce strong zero-shot grasp generalization, including dexterous hands.</td></tr>
    <tr><td><strong>09</strong> DEXNDM: Closing the Reality Gap for Dexterous In-Hand Rotation via Joint-Wise Neural Dynamics Model</td><td><a href="https://arxiv.org/pdf/2510.08556">PDF</a></td><td>Factorizes real-world dynamics by joint and trains a residual policy that generalizes in-hand rotation across objects and wrist poses.</td></tr>
    <tr><td rowspan="1"><strong>2025-07</strong></td><td><strong>09</strong> Hierarchical Reinforcement Learning for Articulated Tool Manipulation with Multifingered Hand</td><td><a href="https://arxiv.org/pdf/2507.06822">PDF</a></td><td>Splits long-horizon tool use into reusable subskills so high-DoF hand control becomes tractable.</td></tr>
    <tr><td rowspan="1"><strong>2025-04</strong></td><td><strong>30</strong> Multi-Goal Dexterous Hand Manipulation using Probabilistic Model-based Reinforcement Learning</td><td><a href="https://arxiv.org/pdf/2504.21585">PDF</a></td><td>Learns a probabilistic dynamics model to plan one policy over multiple dexterous manipulation goals.</td></tr>
    <tr><td rowspan="1"><strong>2025-02</strong></td><td><strong>06</strong> DexterityGen: Foundation Controller for Unprecedented Dexterity</td><td><a href="https://arxiv.org/pdf/2502.04307">PDF</a></td><td>Uses a foundation controller trained on diverse dexterous behaviors as a reusable prior for downstream RL and skill composition.</td></tr>
  </tbody>
</table>

### Former / foundational

| Title | PDF | Insight |
|---|---|---|
| Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations | [PDF](https://arxiv.org/pdf/1709.10087) | Combines demonstrations with deep RL to learn high-DoF manipulation from both task rewards and expert behavior. |
| Learning Dexterous In-Hand Manipulation | [PDF](https://arxiv.org/pdf/1808.00177) | The Dactyl line demonstrates large-scale model-free RL for robust in-hand reorientation on a Shadow Hand. |
| Dexterous In-Hand Manipulation of Slender Cylindrical Objects through Deep Reinforcement Learning with Tactile Sensing | [PDF](https://arxiv.org/pdf/2304.05141) | Adds tactile feedback to deep RL for rotating thin objects that are difficult to control visually. |
| Bi-Touch: Bimanual Tactile Manipulation with Sim-to-Real Deep Reinforcement Learning | [PDF](https://arxiv.org/pdf/2307.06423) | Uses bimanual tactile observations and sim-to-real RL for coordinated contact-rich manipulation. |
| AnyRotate: Gravity-Invariant In-Hand Object Rotation with Sim-to-Real Touch | [PDF](https://arxiv.org/pdf/2405.07391) | Uses touch-aware RL and gravity-invariant training to rotate objects under varied hand orientations. |
| Cross-Embodiment Dexterous Grasping with Reinforcement Learning | [PDF](https://arxiv.org/pdf/2410.02479) | Learns a universal grasping policy across heterogeneous hands through an embodiment-agnostic representation. |

## 2. Unified latent/action spaces

### CVPR 2026

| Title | PDF | Insight |
|---|---|---|
| UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_UniDex_A_Robot_Foundation_Suite_for_Universal_Dexterous_Hand_Control_CVPR_2026_paper.pdf) | Builds a 50K-trajectory, eight-hand dataset and a unified VLA/action interface for cross-hand control. |
| Cross-Hand Latent Representation for Vision-Language-Action Models | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_Cross-Hand_Latent_Representation_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf) | Learns an embodiment-invariant latent action space that plugs into standard VLA architectures. |
| Structural Action Transformer for 3D Dexterous Manipulation | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Lei_Structural_Action_Transformer_for_3D_Dexterous_Manipulation_CVPR_2026_paper.pdf) | Injects hand-object structure into action tokens so the policy models coordinated 3D finger motions rather than a flat joint vector. |
| Dexterous World Models | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf) | Establishes a world-modeling benchmark and generative dynamics formulation for dexterous hand-object interaction. |

### ICML 2026

Adjacent methods for latent predictive and action interfaces are included for context.

| Title | PDF | Insight |
|---|---|---|
| Structured 4D Latent Predictive Model for Robot Planning | [PDF](https://arxiv.org/pdf/2607.01166) | Predicts structured 4D latent states that support long-horizon robot planning. |
| World Guidance: World Modeling in Condition Space for Action Generation | [PDF](https://arxiv.org/pdf/2602.22010) | Models action-conditioned future structure in a compact condition space and uses it to guide generation. |
| See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model | [PDF](https://arxiv.org/pdf/2605.11817) | Compresses visual tokens while preserving the geometry needed by manipulation policies. |

### ECCV 2026

- No unified-latent/action-space papers listed yet.

### Recent arXiv (2025-2026)

<table>
  <thead>
    <tr><th>Month</th><th>Title</th><th>PDF</th><th>Insight</th></tr>
  </thead>
  <tbody>
    <tr><td rowspan="7"><strong>2026-08</strong></td><td><strong>07</strong> C2Dex: Contact-Consistent Reconstruction and Retargeting for Dexterous Manipulation from Monocular Video</td><td><a href="https://arxiv.org/pdf/2608.07045">PDF</a></td><td>Recovers stable object-centric contacts from monocular human videos and transfers them as explicit constraints across dexterous hand embodiments.</td></tr>
    <tr><td><strong>05</strong> VLAff: Vision-Language-Affordance Model for Unified Actionable Affordances</td><td><a href="https://arxiv.org/pdf/2608.05215">PDF</a></td><td>Aligns visual, grasp, and trajectory affordances from human videos in one actionable representation for cross-embodiment robot manipulation.</td></tr>
    <tr><td><strong>04</strong> RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation</td><td><a href="https://arxiv.org/pdf/2608.03387">PDF</a></td><td>Distills generated egocentric videos into geometry-preserving whole-body humanoid skills with closed-loop re-grounding for dexterous interaction.</td></tr>
    <tr><td><strong>04</strong> SiMDex: Mining Similar Egocentric Videos for Cross-Embodiment Dexterous Manipulation</td><td><a href="https://arxiv.org/pdf/2608.04196">PDF</a></td><td>Mines task-relevant human videos in a morphology-agnostic action space to improve VLA post-training for dexterous manipulation.</td></tr>
    <tr><td><strong>04</strong> DigitCode: Symbolic Tokenization of Hand Motion by Anatomical Units</td><td><a href="https://arxiv.org/pdf/2608.03127">PDF</a></td><td>Builds a hierarchical symbolic code for anatomically valid hand motion, offering a compact discrete interface for hand generation and transfer.</td></tr>
    <tr><td><strong>03</strong> Teleopit: A Full-Embodiment Humanoid Teleoperation System</td><td><a href="https://arxiv.org/pdf/2608.01834">PDF</a></td><td>Maps VR body, hand, and head signals to multiple dexterous hands with a history-aware retargeter and failure-aware rewind.</td></tr>
    <tr><td><strong>03</strong> MANGO-Grasp: Mahalanobis Fields over Geometry-Oriented 3D Gaussians for Cross-Embodiment Dexterous Grasping</td><td><a href="https://arxiv.org/pdf/2608.02014">PDF</a></td><td>Uses geometry-oriented Gaussian primitives and morpho-kinematic hand descriptors to optimize one zero-shot grasp formulation across embodiments.</td></tr>
    <tr><td rowspan="9"><strong>2026-07</strong></td><td><strong>30</strong> UniCross: Unified Cross-Skill Dexterous Manipulation Synthesis</td><td><a href="https://arxiv.org/pdf/2607.28198">PDF</a></td><td>Puts grasping, relocation, in-hand rotation, and translation in one shared state-action formulation for cross-skill and cross-hand composition.</td></tr>
    <tr><td><strong>30</strong> DexDirect: Direct Kinesthetic Arm Guidance for Efficient Dexterous Demonstration Collection</td><td><a href="https://arxiv.org/pdf/2607.27784">PDF</a></td><td>Combines kinesthetic arm guidance with webcam hand retargeting to collect high-success dexterous demonstrations with low setup cost.</td></tr>
    <tr><td><strong>17</strong> Handroid: Bridging Dexterous Hand and Humanoid</td><td><a href="https://arxiv.org/pdf/2607.16187">PDF</a></td><td>Reconfigures one 27-DoF platform between a dexterous hand and humanoid while retaining a unified control and learning stack.</td></tr>
    <tr><td><strong>13</strong> GraspGraphNet: Graph-Structured Multi-Embodiment Dexterous Grasp Generation</td><td><a href="https://arxiv.org/pdf/2607.11031">PDF</a></td><td>Represents each hand as a kinematic graph and generates executable grasps directly across different hand topologies without retargeting.</td></tr>
    <tr><td><strong>09</strong> DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation</td><td><a href="https://arxiv.org/pdf/2607.08751">PDF</a></td><td>Provides 100 tasks, six hands, and multimodal demonstrations to benchmark cross-task and cross-embodiment dexterous policies.</td></tr>
    <tr><td><strong>09</strong> AnyDexRT: Calibration-Free Dexterous Hand Retargeting with Few-Shot Human Guidance</td><td><a href="https://arxiv.org/pdf/2607.08341">PDF</a></td><td>Learns calibration-free fingertip correspondences and contact-aware refinement for retargeting human motion across dexterous hands.</td></tr>
    <tr><td><strong>07</strong> RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation</td><td><a href="https://arxiv.org/pdf/2607.06558">PDF</a></td><td>Uses hand-pose streams as embodiment-agnostic action labels to generate scalable digital teleoperation data for dexterous Sim2Real.</td></tr>
    <tr><td><strong>05</strong> Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models</td><td><a href="https://arxiv.org/pdf/2607.04546">PDF</a></td><td>Predicts future segmentation masks before rendering RGB, narrowing the sim-to-real gap for controllable 23-DoF dexterous world models.</td></tr>
    <tr><td><strong>03</strong> Cross-Embodiment Robot Manipulation via a Unified Hand Action Space</td><td><a href="https://arxiv.org/pdf/2607.03570">PDF</a></td><td>Defines a shared hand action coordinate system and embodiment-specific decoders for zero-shot transfer.</td></tr>
    <tr><td rowspan="6"><strong>2026-06</strong></td><td><strong>22</strong> LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation</td><td><a href="https://arxiv.org/pdf/2606.23685">PDF</a></td><td>Aligns human-hand trajectories and robot actions in a latent physical-reasoning space for scalable pretraining.</td></tr>
    <tr><td><strong>21</strong> EgoSteer: A Full-Stack System Towards Steerable Dexterous Manipulation from Egocentric Videos</td><td><a href="https://arxiv.org/pdf/2607.09701">PDF</a></td><td>Combines egocentric human-video pretraining, a world-model-enhanced VLA, and DAgger to steer dexterous policies across tasks and embodiments.</td></tr>
    <tr><td><strong>20</strong> KITE: Decoupling Kinematics and Interaction for Zero-Shot Cross-Embodiment Manipulation</td><td><a href="https://arxiv.org/pdf/2606.22113">PDF</a></td><td>Separates embodiment-independent interaction intent from a kinematic decoder that adapts to unseen hands.</td></tr>
    <tr><td><strong>10</strong> LUCID: Learning Embodiment-Agnostic Intent Models from Unstructured Human Videos for Scalable Dexterous Robot Skill Acquisition</td><td><a href="https://arxiv.org/pdf/2606.11628">PDF</a></td><td>Learns a shared intent interface from videos, then decodes it into different robot embodiments.</td></tr>
    <tr><td><strong>10</strong> InDex: Empowering VLA Models with Intent-Conditioned Arm-Hand Coordination for Dexterous Manipulation</td><td><a href="https://arxiv.org/pdf/2606.12109">PDF</a></td><td>Separates when to establish contact from how to realize it with morphology-specific fingers.</td></tr>
    <tr><td><strong>09</strong> UniDexTok: A Unified Dexterous Hand Tokenizer from Real Data</td><td><a href="https://arxiv.org/pdf/2606.10683">PDF</a></td><td>Converts heterogeneous hand states into a shared discrete codebook that enables joint VLA training.</td></tr>
    <tr><td rowspan="2"><strong>2026-03</strong></td><td><strong>17</strong> DexGrasp-Zero: A Morphology-Aligned Policy for Zero-Shot Cross-Embodiment Dexterous Grasping</td><td><a href="https://arxiv.org/pdf/2603.16806">PDF</a></td><td>Conditions a universal grasp policy directly on hand morphology to avoid per-hand retargeting errors.</td></tr>
    <tr><td><strong>15</strong> One-Policy-Fits-All: Geometry-Aware Action Latents for Cross-Embodiment Manipulation</td><td><a href="https://arxiv.org/pdf/2603.14522">PDF</a></td><td>Encodes action intent in geometry-aware latents so one policy can serve grippers and high-DoF hands.</td></tr>
    <tr><td rowspan="4"><strong>2026-02</strong></td><td><strong>28</strong> UniHM: Unified Dexterous Hand Manipulation with Vision Language Model</td><td><a href="https://arxiv.org/pdf/2603.00732">PDF</a></td><td>Introduces a unified hand tokenizer and trains language-conditioned manipulation from human-object sequences.</td></tr>
    <tr><td><strong>18</strong> One Hand to Rule Them All: Canonical Representations for Unified Dexterous Manipulation</td><td><a href="https://arxiv.org/pdf/2602.16712">PDF</a></td><td>Parameterizes hand morphology and learns a smooth latent manifold that interpolates across kinematic designs.</td></tr>
    <tr><td><strong>10</strong> DexImit: Learning Bimanual Dexterous Manipulation from Monocular Human Videos</td><td><a href="https://arxiv.org/pdf/2602.10105">PDF</a></td><td>Converts monocular human videos into physically plausible bimanual robot trajectories for cross-embodiment pretraining.</td></tr>
    <tr><td><strong>09</strong> DexFormer: Cross-Embodied Dexterous Manipulation via History-Conditioned Transformer</td><td><a href="https://arxiv.org/pdf/2602.08278">PDF</a></td><td>Uses action history as a compact bridge for transferring manipulation skills between hands.</td></tr>
    <tr><td rowspan="3"><strong>2026-01</strong></td><td><strong>31</strong> UniMorphGrasp: Diffusion Model with Morphology-Awareness for Cross-Embodiment Dexterous Grasp Generation</td><td><a href="https://arxiv.org/pdf/2602.00915">PDF</a></td><td>Maps different hands into a canonical human-like pose space before morphology-conditioned diffusion generation.</td></tr>
    <tr><td><strong>13</strong> FSAG: Enhancing Human-to-Dexterous-Hand Finger-Specific Affordance Grounding via Diffusion Models</td><td><a href="https://arxiv.org/pdf/2601.08246">PDF</a></td><td>Grounds finger-specific affordances from pretrained diffusion priors without requiring a large robot grasp dataset.</td></tr>
    <tr><td><strong>08</strong> Generate, Transfer, Adapt: Learning Functional Dexterous Grasping from a Single Human Demonstration</td><td><a href="https://arxiv.org/pdf/2601.05243">PDF</a></td><td>Builds a correspondence-based data engine that transfers one human functional grasp to many novel objects and robot hands.</td></tr>
    <tr><td rowspan="1"><strong>2025-10</strong></td><td><strong>07</strong> MachaGrasp: Morphology-Aware Cross-Embodiment Dexterous Hand Articulation Generation for Grasping</td><td><a href="https://arxiv.org/pdf/2510.06068">PDF</a></td><td>Uses morphology embeddings and eigengrasp bases to decode low-dimensional articulation coefficients.</td></tr>
    <tr><td rowspan="1"><strong>2025-09</strong></td><td><strong>29</strong> CEDex: Cross-Embodiment Dexterous Grasp Generation at Scale from Human-like Contact Representations</td><td><a href="https://arxiv.org/pdf/2509.24661">PDF</a></td><td>Represents contact in a human-like coordinate system to scale grasp generation across non-identical hands.</td></tr>
    <tr><td rowspan="1"><strong>2025-07</strong></td><td><strong>03</strong> DexVLG: Dexterous Vision-Language-Grasp Model at Scale</td><td><a href="https://arxiv.org/pdf/2507.02747">PDF</a></td><td>Scales language-grounded grasp prediction with a 170M-pose synthetic dataset and part-level semantic supervision.</td></tr>
    <tr><td rowspan="1"><strong>2025-06</strong></td><td><strong>17</strong> Latent Action Diffusion for Cross-Embodiment Manipulation</td><td><a href="https://arxiv.org/pdf/2506.14608">PDF</a></td><td>Learns contrastively aligned latent actions shared by anthropomorphic hands, human hands, and parallel grippers.</td></tr>
    <tr><td rowspan="2"><strong>2025-05</strong></td><td><strong>30</strong> DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation</td><td><a href="https://arxiv.org/pdf/2505.24853">PDF</a></td><td>Retargets human demonstrations through a functional, contact-aware representation for bimanual hands.</td></tr>
    <tr><td><strong>02</strong> DexFlow: A Unified Approach for Dexterous Hand Pose Retargeting and Interaction</td><td><a href="https://arxiv.org/pdf/2505.01083">PDF</a></td><td>Couples retargeting with hand-object interaction modeling instead of optimizing hand pose in isolation.</td></tr>
    <tr><td rowspan="1"><strong>2025-03</strong></td><td><strong>10</strong> Geometric Retargeting: A Principled, Ultrafast Neural Hand Retargeting Algorithm</td><td><a href="https://arxiv.org/pdf/2503.07541">PDF</a></td><td>Learns a 1 kHz, calibration-light mapping from human keypoints to robot-hand keypoints.</td></tr>
    <tr><td rowspan="1"><strong>2025-02</strong></td><td><strong>28</strong> DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping</td><td><a href="https://arxiv.org/pdf/2502.20900">PDF</a></td><td>Uses a hierarchical VLM planner and diffusion action controller to make language-guided grasping robust to clutter and disturbances.</td></tr>
  </tbody>
</table>

### Former / foundational

| Title | PDF | Insight |
|---|---|---|
| Learning Cross-Hand Policies of High-DOF Reaching and Grasping | [PDF](https://arxiv.org/pdf/2404.09150) | Uses gripper-agnostic keypoint displacements followed by hand-specific adaptation for cross-hand reaching and grasping. |
| FunGrasp: Functional Grasping for Diverse Dexterous Hands | [PDF](https://arxiv.org/pdf/2411.16755) | Grounds language and object-part affordances in a representation that supports functional grasps across hand designs. |
| DexDiffuser: Generating Dexterous Grasps with Diffusion Models | [PDF](https://arxiv.org/pdf/2402.02989) | Shows that diffusion in a structured grasp space can generate diverse, physically valid multi-finger poses. |
| Dexterous Functional Pre-Grasp Manipulation with Diffusion Policy | [PDF](https://arxiv.org/pdf/2403.12421) | Learns preparatory hand motions that make downstream functional grasping easier for a diffusion policy. |
| Cross-Embodiment Dexterous Grasping with Reinforcement Learning | [PDF](https://arxiv.org/pdf/2410.02479) | A foundational universal-policy formulation that separates hand morphology from shared grasp behavior. |
| D(R,O) Grasp: A Unified Representation of Robot and Object Interaction for Cross-Embodiment Dexterous Grasping | [PDF](https://arxiv.org/pdf/2410.01702) | Encodes robot-object interaction in a shared representation that separates morphology from grasp intent. |

## 3. Dexterous hand + tactile sensing

### CVPR 2026

| Title | PDF | Insight |
|---|---|---|
| ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.pdf) | Adds force-aware hybrid position/force control so a VLA can react to contact instead of treating it as visual noise. |
| AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.pdf) | Injects tactile features adaptively at the layer and timestep where contact feedback matters most. |
| Seeing Through Touch: Tactile-Driven Visual Localization of Material Regions | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Seeing_Through_Touch_Tactile-Driven_Visual_Localization_of_Material_Regions_CVPR_2026_paper.pdf) | Uses touch to localize material regions in the visual scene, improving perception when appearance alone is ambiguous. |
| Hoi! - A Multimodal Dataset for Force-Grounded, Cross-View Articulated Manipulation | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Engelbracht_Hoi_-_A_Multimodal_Dataset_for_Force-Grounded_Cross-View_Articulated_Manipulation_CVPR_2026_paper.pdf) | Aligns force, vision, and articulated-object motion across views to make contact dynamics learnable. |

### ICML 2026

- No direct dexterous-hand+tactile paper listed yet.

### ECCV 2026

- No dexterous-hand+tactile papers listed yet.

### Recent arXiv (2025-2026)

<table>
  <thead>
    <tr><th>Month</th><th>Title</th><th>PDF</th><th>Insight</th></tr>
  </thead>
  <tbody>
    <tr><td rowspan="3"><strong>2026-08</strong></td><td><strong>07</strong> Detection and Ranging of Transient Extrinsic Contacts Based on 6D Dynamic Tactile Sensing</td><td><a href="https://arxiv.org/pdf/2608.07075">PDF</a></td><td>Uses a compact 6D dynamic tactile sensor at gripper tips to detect and localize transient contacts during manipulation.</td></tr>
    <tr><td><strong>03</strong> ReTouch: Empowering Contact-Rich Dexterous Manipulation with Online-Refined Tactile Prediction</td><td><a href="https://arxiv.org/pdf/2608.01824">PDF</a></td><td>Refines tactile predictions online during execution so contact-rich policies can recover from sensor and dynamics mismatch.</td></tr>
    <tr><td><strong>03</strong> Semantic Haptic Feedback Enhances Dexterous Robotic Teleoperation</td><td><a href="https://arxiv.org/pdf/2608.02780">PDF</a></td><td>Encodes robot states as abstract haptic patterns through wristbands, reducing workload during bimanual dexterous teleoperation.</td></tr>
    <tr><td rowspan="10"><strong>2026-07</strong></td><td><strong>30</strong> TacWAM: Anchor-Guided World Action Model with Mechanics-Aware Tactile Prediction</td><td><a href="https://arxiv.org/pdf/2607.28391">PDF</a></td><td>Predicts mechanics-aware tactile futures in a shared latent space while preventing future privileged signals from leaking into action generation.</td></tr>
    <tr><td><strong>25</strong> Pose-Aware Modeling to Mitigate Pose-Related Artifacts in Tactile Gloves</td><td><a href="https://arxiv.org/pdf/2607.22964">PDF</a></td><td>Uses hand pose to remove pose-induced artifacts from tactile gloves, lowering minimum detectable force across users and glove designs.</td></tr>
    <tr><td><strong>20</strong> Predicting Grasping Compliance in Robotic Hands through Analytical-Model-Informed Neural Networks</td><td><a href="https://arxiv.org/pdf/2607.17541">PDF</a></td><td>Combines analytical mechanics with neural learning to predict forceful grasp compliance and tool displacement in an underactuated robotic hand.</td></tr>
    <tr><td><strong>16</strong> VTAP Gripper: Synergizing Fingertip Sensing and a Visuo-Tactile Active Palm for Dexterous In-Hand Manipulation</td><td><a href="https://arxiv.org/pdf/2607.15448">PDF</a></td><td>Combines an active visuo-tactile palm, fingertip arrays, and gesture-conditioned retargeting for contact-rich in-hand manipulation.</td></tr>
    <tr><td><strong>16</strong> KineFuse: Kinematic-Aware Haptic Fusion for In-Hand Occluded-Object Pose Tracking</td><td><a href="https://arxiv.org/pdf/2607.14842">PDF</a></td><td>Fuses structured finger-level proprioception, force-torque, and contact tokens with vision to improve occluded object-pose tracking.</td></tr>
    <tr><td><strong>10</strong> TactiDex: A Real-World Tactile-Guided Benchmark for Human-Like Dexterous Manipulation</td><td><a href="https://arxiv.org/pdf/2607.09190">PDF</a></td><td>Provides real-world tasks and evaluation protocols that explicitly test tactile-guided human-like dexterity.</td></tr>
    <tr><td><strong>08</strong> TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation</td><td><a href="https://arxiv.org/pdf/2607.07287">PDF</a></td><td>Unifies tactile forecasting and fast reactive control in one predictive foundation model.</td></tr>
    <tr><td><strong>03</strong> Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation</td><td><a href="https://arxiv.org/pdf/2607.03529">PDF</a></td><td>Treats motor current as a learnable contact signal for compliance when dedicated tactile sensors are unavailable.</td></tr>
    <tr><td><strong>03</strong> CoorGrasp: Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty</td><td><a href="https://arxiv.org/pdf/2607.03557">PDF</a></td><td>Uses tactile-driven model-predictive control and coordinated force regulation to execute dexterous grasps robustly under uncertainty.</td></tr>
    <tr><td><strong>01</strong> Human-Centric Transferable Tactile Pre-Training for Dexterous Robotic Manipulation</td><td><a href="https://arxiv.org/pdf/2607.01067">PDF</a></td><td>Pretrains tactile-action representations on large-scale human data and transfers them to fine-grained robot manipulation through unified spaces.</td></tr>
    <tr><td rowspan="6"><strong>2026-06</strong></td><td><strong>30</strong> RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation</td><td><a href="https://arxiv.org/pdf/2606.31836">PDF</a></td><td>Releases aligned visual, tactile, and action trajectories for dual-arm humanoids with dexterous hands.</td></tr>
    <tr><td><strong>30</strong> UniTacVLA: Unified Tactile Understanding and Prediction in Vision-Language-Action Models</td><td><a href="https://arxiv.org/pdf/2606.31723">PDF</a></td><td>Learns a shared tactile representation that supports both semantic understanding and future-contact prediction in VLAs.</td></tr>
    <tr><td><strong>25</strong> VibeAct: Vibration to Actions for Contact-Rich Reactive Robot Dexterity</td><td><a href="https://arxiv.org/pdf/2606.27344">PDF</a></td><td>Converts high-frequency vibration cues into reactive actions for slip-sensitive dexterous tasks.</td></tr>
    <tr><td><strong>15</strong> T-Rex: Tactile-Reactive Dexterous Manipulation</td><td><a href="https://arxiv.org/pdf/2606.17055">PDF</a></td><td>Builds a fast tactile reflex layer that complements slower visuomotor planning for contact transitions.</td></tr>
    <tr><td><strong>14</strong> Transferring Contact, Not Just Motion: Compliant Grasping Across Dexterous Hands</td><td><a href="https://arxiv.org/pdf/2606.15516">PDF</a></td><td>Transfers a shared hand-pose latent together with calibrated effort signals, preserving contact regulation across morphologies.</td></tr>
    <tr><td><strong>10</strong> Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning</td><td><a href="https://arxiv.org/pdf/2606.11767">PDF</a></td><td>Trains tactile-only grasping through a geometry-consistent real2sim2real pipeline.</td></tr>
    <tr><td rowspan="6"><strong>2026-03</strong></td><td><strong>19</strong> OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation</td><td><a href="https://arxiv.org/pdf/2603.19201">PDF</a></td><td>Learns a visuo-tactile world model and a high-rate reflex controller that closes the loop on predicted contact states.</td></tr>
    <tr><td><strong>18</strong> DexViTac: Collecting Human Visuo-Tactile-Kinematic Demonstrations for Contact-Rich Dexterous Manipulation</td><td><a href="https://arxiv.org/pdf/2603.17851">PDF</a></td><td>Couples first-person vision, dense tactile sensing, and hand kinematics in a portable data-collection system.</td></tr>
    <tr><td><strong>16</strong> HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing</td><td><a href="https://arxiv.org/pdf/2603.15257">PDF</a></td><td>Distills tactile experience into a VLA so deployment can remain tactile-free while retaining contact knowledge.</td></tr>
    <tr><td><strong>14</strong> TransDex: Pre-training Visuo-Tactile Policy with Point Cloud Reconstruction for Dexterous Manipulation of Transparent Objects</td><td><a href="https://arxiv.org/pdf/2603.13869">PDF</a></td><td>Uses point-cloud reconstruction as pretraining to recover geometry hidden by transparent-object and hand occlusions.</td></tr>
    <tr><td><strong>10</strong> ReTac-ACT: A State-Gated Vision-Tactile Fusion Transformer for Precision Assembly</td><td><a href="https://arxiv.org/pdf/2603.09565">PDF</a></td><td>Gates tactile reliance with proprioception and reconstructs contact signals for sub-millimeter assembly corrections.</td></tr>
    <tr><td><strong>04</strong> PTLD: Sim-to-Real Privileged Tactile Latent Distillation for Dexterous Manipulation</td><td><a href="https://arxiv.org/pdf/2603.04531">PDF</a></td><td>Distills privileged simulated tactile signals into deployable latent representations for real hands.</td></tr>
    <tr><td rowspan="2"><strong>2026-02</strong></td><td><strong>10</strong> AnyTouch 2: General Optical Tactile Representation Learning for Dynamic Tactile Perception</td><td><a href="https://arxiv.org/pdf/2602.09617">PDF</a></td><td>Pretrains a sensor-agnostic optical-tactile encoder for dynamic contact understanding.</td></tr>
    <tr><td><strong>05</strong> DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter</td><td><a href="https://arxiv.org/pdf/2602.05513">PDF</a></td><td>Adds tactile as a plug-in adapter to a multimodal diffusion policy, preserving a reusable visual backbone.</td></tr>
    <tr><td rowspan="2"><strong>2025-12</strong></td><td><strong>24</strong> UniTacHand: Unified Spatio-Tactile Representation for Human to Robotic Hand Skill Transfer</td><td><a href="https://arxiv.org/pdf/2512.21233">PDF</a></td><td>Aligns human glove touch with robot-hand tactile signals for cross-domain skill transfer.</td></tr>
    <tr><td><strong>18</strong> OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction</td><td><a href="https://arxiv.org/pdf/2512.16842">PDF</a></td><td>Releases an egocentric full-hand touch dataset that links where, when, and how forcefully a human hand contacts objects.</td></tr>
    <tr><td rowspan="1"><strong>2025-08</strong></td><td><strong>12</strong> OmniVTLA: Vision-Tactile-Language-Action Model with Semantic-Aligned Tactile Sensing</td><td><a href="https://arxiv.org/pdf/2508.08706">PDF</a></td><td>Aligns tactile features with language and vision so tactile observations can support semantic task generalization.</td></tr>
    <tr><td rowspan="2"><strong>2025-07</strong></td><td><strong>14</strong> Demonstrating the Octopi-1.5 Visual-Tactile-Language Model</td><td><a href="https://arxiv.org/pdf/2507.09985">PDF</a></td><td>Demonstrates a visual-tactile-language model that grounds tactile observations in language-conditioned manipulation.</td></tr>
    <tr><td><strong>12</strong> Tactile-VLA: Unlocking Vision-Language-Action Model's Physical Knowledge for Tactile Generalization</td><td><a href="https://arxiv.org/pdf/2507.09160">PDF</a></td><td>Connects a VLA's implicit physical knowledge to tactile feedback with a hybrid position-force controller and few demonstrations.</td></tr>
    <tr><td rowspan="1"><strong>2025-05</strong></td><td><strong>09</strong> APPLE: Toward General Active Perception via Reinforcement Learning</td><td><a href="https://arxiv.org/pdf/2505.06182">PDF</a></td><td>Jointly trains a transformer perception module and an RL exploration policy, including active tactile perception tasks.</td></tr>
  </tbody>
</table>

### Former / foundational

| Title | PDF | Insight |
|---|---|---|
| Canonical Representation and Force-Based Pretraining of 3D Tactile for Dexterous Visuo-Tactile Policy Learning | [PDF](https://arxiv.org/pdf/2409.17549) | Uses canonical 3D tactile coordinates and force-based pretraining to make full-hand tactile features transferable. |
| 3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing | [PDF](https://arxiv.org/pdf/2410.24091) | Fuses vision and tactile feedback for fine-grained manipulation under visual occlusion. |
| Dexterity from Touch: Self-Supervised Pre-Training of Tactile Representations with Robotic Play | [PDF](https://arxiv.org/pdf/2303.12076) | Learns tactile features from unlabeled robot play instead of task-specific annotations. |
| See to Touch: Learning Tactile Dexterity through Visual Incentives | [PDF](https://arxiv.org/pdf/2309.12300) | Uses visual goals to shape tactile representations and improve contact-rich dexterity. |
| Robot Synesthesia: In-Hand Manipulation with Visuotactile Sensing | [PDF](https://arxiv.org/pdf/2312.01853) | Shows that synchronized vision and touch enable robust in-hand manipulation under severe occlusion. |
| DexTouch: Learning to Seek and Manipulate Objects with Tactile Dexterity | [PDF](https://arxiv.org/pdf/2401.12496) | Frames tactile exploration and manipulation as one closed-loop dexterous policy. |
| Bi-Touch: Bimanual Tactile Manipulation with Sim-to-Real Deep Reinforcement Learning | [PDF](https://arxiv.org/pdf/2307.06423) | Demonstrates that tactile feedback can make bimanual sim-to-real dexterous control robust. |
| All the Feels: A Dexterous Hand with Large-Area Tactile Sensing | [PDF](https://arxiv.org/pdf/2210.15658) | Introduces full-hand tactile coverage that exposes contact patterns beyond fingertips. |
