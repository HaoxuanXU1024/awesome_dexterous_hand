# Awesome Dexterous Hand Papers

An arXiv-first reading list for three tightly scoped directions:

1. **Dexterous-hand reinforcement learning (RL)**
2. **Unified latent/action spaces for dexterous hands**
3. **Dexterous hands with tactile sensing**

The five subsections under every direction intentionally follow the same order: **CVPR 2026**, **ICML 2026**, **ECCV 2026**, **Recent arXiv**, and **Former / foundational**. Each entry gives the full paper title, a one-sentence insight, and one direct PDF link.

## Contents

- [Dexterous-hand RL](#1-dexterous-hand-rl)
- [Unified latent/action spaces](#2-unified-latentaction-spaces)
- [Dexterous hand + tactile sensing](#3-dexterous-hand--tactile-sensing)

## 1. Dexterous-hand RL

### CVPR 2026

- DemoFunGrasp: Universal Dexterous Functional Grasping via Demonstration-Editing Reinforcement Learning ([PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_DemoFunGrasp_Universal_Dexterous_Functional_Grasping_via_Demonstration-Editing_Reinforcement_Learning_CVPR_2026_paper.pdf)) - Factorizes functional grasping into style and affordance, then turns one demonstration into a one-step RL editing problem.
- DextER: Language-driven Dexterous Grasp Generation with Embodied Reasoning ([PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_DextER_Language-driven_Dexterous_Grasp_Generation_with_Embodied_Reasoning_CVPR_2026_paper.pdf)) - Uses embodied reasoning to connect language-level intent to physically executable multi-finger grasps.
- AdaDexTrack: Dynamic Modulation for Adaptive and Generalizable Dexterous Manipulation Tracking ([PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Adalibieke_AdaDexTrack_Dynamic_Modulation_for_Adaptive_and_Generalizable_Dexterous_Manipulation_Tracking_CVPR_2026_paper.pdf)) - Dynamically modulates tracking features so a dexterous policy can follow diverse motions under distribution shift.

### ICML 2026

Adjacent policy-learning methods are included for context and marked **adjacent**.

- FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation ([PDF](https://arxiv.org/pdf/2606.20867)) - Conditions VLA adaptation on future task context to improve sample efficiency during policy refinement.
- VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models ([PDF](https://arxiv.org/pdf/2512.22539)) - Provides a reproducible evaluation harness for comparing VLA policies across tasks and embodiments.
- See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model ([PDF](https://arxiv.org/pdf/2605.11817)) - Retains contact-relevant visual tokens with differentiable resampling instead of dropping fixed image blocks.

### ECCV 2026

- No dexterous-hand papers listed yet.

### Recent arXiv (2025-2026)

- 2026-08-01 - DexMani: Human-Derived Manipulability Guidance for Dexterous Rotation ([PDF](https://arxiv.org/pdf/2608.00554)) - Transfers human contact-conditioned manipulability evolution into a cross-embodiment prior that guides RL for robust in-hand rotation.
- 2026-07-13 - Towards Human-level Dexterous Teleoperation ([PDF](https://arxiv.org/pdf/2607.11481)) - Learns a subgoal-conditioned contact controller with a hybrid reward and single-stage RL, enabling long-horizon in-hand teleoperation.
- 2026-07-13 - REGRIND: A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation ([PDF](https://arxiv.org/pdf/2607.11874)) - Retargets one human hand-object demonstration into contact-preserving references and learns a residual RL policy around them.
- 2026-07-13 - Robust In-Hand Manipulation via Priors in Reinforcement Learning and Mechanical Design ([PDF](https://arxiv.org/pdf/2607.12105)) - Shapes RL with global grasp-quality and local fingertip-curvature priors to improve rolling stability and disturbance rejection.
- 2026-07-07 - LAMP: Latent Motion Prior-Guided Real-World Learning for Dexterous Hand Manipulation ([PDF](https://arxiv.org/pdf/2607.06323)) - Constrains online residual RL to a history-conditioned latent motion prior so exploration stays near contact-consistent actions.
- 2026-06-22 - Learning Dexterous Manipulation Using Contact Wrench Guidance From Human Demonstration ([PDF](https://arxiv.org/pdf/2607.00033)) - Guides RL in an object-centric contact-wrench space so human demonstrations transfer to long-horizon bimanual and whole-body dexterous tasks.
- 2026-06-08 - DexPIE: Stable Dexterous Policy Improvement from Real-World Experience ([PDF](https://arxiv.org/pdf/2606.09615)) - Uses intervention-aware data collection and staged policy improvement to make real-world dexterous adaptation stable.
- 2026-05-28 - BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models ([PDF](https://arxiv.org/pdf/2605.30226)) - Bootstraps a dexterous VLA offline and improves it online through residual RL rather than relearning from scratch.
- 2026-04-24 - RL Token: Bootstrapping Online RL with Vision-Language-Action Models ([PDF](https://arxiv.org/pdf/2604.23073)) - Exposes a compact token from a frozen VLA for sample-efficient online RL fine-tuning on precision manipulation tasks.
- 2026-03-11 - ContactExplorer: Contact Coverage-Guided Exploration for General-Purpose Dexterous Manipulation ([PDF](https://arxiv.org/pdf/2603.10971)) - Shapes RL exploration with a contact-coverage objective that deliberately discovers new finger-object contact patterns.
- 2026-03-01 - D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping ([PDF](https://arxiv.org/pdf/2603.01151)) - Differentiates through a real-to-sim-to-real loop so grasping policies can adapt contact dynamics with less real-robot data.
- 2026-01-06 - Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation ([PDF](https://arxiv.org/pdf/2601.02778)) - Combines dense tactile and joint-torque feedback with joint-wise dynamics adaptation for zero-shot sim-to-real RL.
- 2025-11-03 - GenDexHand: Generative Simulation for Dexterous Hands ([PDF](https://arxiv.org/pdf/2511.01791)) - Closes a VLM-guided environment-generation loop and decomposes tasks for scalable sequential RL training.
- 2025-10-14 - Learning to Grasp Anything by Playing with Random Toys ([PDF](https://arxiv.org/pdf/2510.12866)) - Shows that object-centric visual pooling and simple compositional toys can produce strong zero-shot grasp generalization, including dexterous hands.
- 2025-10-09 - DEXNDM: Closing the Reality Gap for Dexterous In-Hand Rotation via Joint-Wise Neural Dynamics Model ([PDF](https://arxiv.org/pdf/2510.08556)) - Factorizes real-world dynamics by joint and trains a residual policy that generalizes in-hand rotation across objects and wrist poses.
- 2025-07-09 - Hierarchical Reinforcement Learning for Articulated Tool Manipulation with Multifingered Hand ([PDF](https://arxiv.org/pdf/2507.06822)) - Splits long-horizon tool use into reusable subskills so high-DoF hand control becomes tractable.
- 2025-04-30 - Multi-Goal Dexterous Hand Manipulation using Probabilistic Model-based Reinforcement Learning ([PDF](https://arxiv.org/pdf/2504.21585)) - Learns a probabilistic dynamics model to plan one policy over multiple dexterous manipulation goals.
- 2025-02-06 - DexterityGen: Foundation Controller for Unprecedented Dexterity ([PDF](https://arxiv.org/pdf/2502.04307)) - Uses a foundation controller trained on diverse dexterous behaviors as a reusable prior for downstream RL and skill composition.

### Former / foundational

- Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations ([PDF](https://arxiv.org/pdf/1709.10087)) - Combines demonstrations with deep RL to learn high-DoF manipulation from both task rewards and expert behavior.
- Learning Dexterous In-Hand Manipulation ([PDF](https://arxiv.org/pdf/1808.00177)) - The Dactyl line demonstrates large-scale model-free RL for robust in-hand reorientation on a Shadow Hand.
- Dexterous In-Hand Manipulation of Slender Cylindrical Objects through Deep Reinforcement Learning with Tactile Sensing ([PDF](https://arxiv.org/pdf/2304.05141)) - Adds tactile feedback to deep RL for rotating thin objects that are difficult to control visually.
- Bi-Touch: Bimanual Tactile Manipulation with Sim-to-Real Deep Reinforcement Learning ([PDF](https://arxiv.org/pdf/2307.06423)) - Uses bimanual tactile observations and sim-to-real RL for coordinated contact-rich manipulation.
- AnyRotate: Gravity-Invariant In-Hand Object Rotation with Sim-to-Real Touch ([PDF](https://arxiv.org/pdf/2405.07391)) - Uses touch-aware RL and gravity-invariant training to rotate objects under varied hand orientations.
- Cross-Embodiment Dexterous Grasping with Reinforcement Learning ([PDF](https://arxiv.org/pdf/2410.02479)) - Learns a universal grasping policy across heterogeneous hands through an embodiment-agnostic representation.

## 2. Unified latent/action spaces

### CVPR 2026

- UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos ([PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_UniDex_A_Robot_Foundation_Suite_for_Universal_Dexterous_Hand_Control_CVPR_2026_paper.pdf)) - Builds a 50K-trajectory, eight-hand dataset and a unified VLA/action interface for cross-hand control.
- Cross-Hand Latent Representation for Vision-Language-Action Models ([PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_Cross-Hand_Latent_Representation_for_Vision-Language-Action_Models_CVPR_2026_paper.pdf)) - Learns an embodiment-invariant latent action space that plugs into standard VLA architectures.
- Structural Action Transformer for 3D Dexterous Manipulation ([PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Lei_Structural_Action_Transformer_for_3D_Dexterous_Manipulation_CVPR_2026_paper.pdf)) - Injects hand-object structure into action tokens so the policy models coordinated 3D finger motions rather than a flat joint vector.
- Dexterous World Models ([PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Dexterous_World_Models_CVPR_2026_paper.pdf)) - Establishes a world-modeling benchmark and generative dynamics formulation for dexterous hand-object interaction.

### ICML 2026

Adjacent methods for latent predictive and action interfaces are included for context.

- Structured 4D Latent Predictive Model for Robot Planning ([PDF](https://arxiv.org/pdf/2607.01166)) - Predicts structured 4D latent states that support long-horizon robot planning.
- World Guidance: World Modeling in Condition Space for Action Generation ([PDF](https://arxiv.org/pdf/2602.22010)) - Models action-conditioned future structure in a compact condition space and uses it to guide generation.
- See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model ([PDF](https://arxiv.org/pdf/2605.11817)) - Compresses visual tokens while preserving the geometry needed by manipulation policies.

### ECCV 2026

- No unified-latent/action-space papers listed yet.

### Recent arXiv (2025-2026)

- 2026-08-04 - RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation ([PDF](https://arxiv.org/pdf/2608.03387)) - Distills generated egocentric videos into geometry-preserving whole-body humanoid skills with closed-loop re-grounding for dexterous interaction.
- 2026-08-03 - Teleopit: A Full-Embodiment Humanoid Teleoperation System ([PDF](https://arxiv.org/pdf/2608.01834)) - Maps VR body, hand, and head signals to multiple dexterous hands with a history-aware retargeter and failure-aware rewind.
- 2026-07-30 - UniCross: Unified Cross-Skill Dexterous Manipulation Synthesis ([PDF](https://arxiv.org/pdf/2607.28198)) - Puts grasping, relocation, in-hand rotation, and translation in one shared state-action formulation for cross-skill and cross-hand composition.
- 2026-07-30 - DexDirect: Direct Kinesthetic Arm Guidance for Efficient Dexterous Demonstration Collection ([PDF](https://arxiv.org/pdf/2607.27784)) - Combines kinesthetic arm guidance with webcam hand retargeting to collect high-success dexterous demonstrations with low setup cost.
- 2026-07-17 - Handroid: Bridging Dexterous Hand and Humanoid ([PDF](https://arxiv.org/pdf/2607.16187)) - Reconfigures one 27-DoF platform between a dexterous hand and humanoid while retaining a unified control and learning stack.
- 2026-07-13 - GraspGraphNet: Graph-Structured Multi-Embodiment Dexterous Grasp Generation ([PDF](https://arxiv.org/pdf/2607.11031)) - Represents each hand as a kinematic graph and generates executable grasps directly across different hand topologies without retargeting.
- 2026-07-09 - DexVerse: A Modular Benchmark for Multi-Task, Multi-Embodiment Dexterous Manipulation ([PDF](https://arxiv.org/pdf/2607.08751)) - Provides 100 tasks, six hands, and multimodal demonstrations to benchmark cross-task and cross-embodiment dexterous policies.
- 2026-07-09 - AnyDexRT: Calibration-Free Dexterous Hand Retargeting with Few-Shot Human Guidance ([PDF](https://arxiv.org/pdf/2607.08341)) - Learns calibration-free fingertip correspondences and contact-aware refinement for retargeting human motion across dexterous hands.
- 2026-07-07 - RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation ([PDF](https://arxiv.org/pdf/2607.06558)) - Uses hand-pose streams as embodiment-agnostic action labels to generate scalable digital teleoperation data for dexterous Sim2Real.
- 2026-07-05 - Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models ([PDF](https://arxiv.org/pdf/2607.04546)) - Predicts future segmentation masks before rendering RGB, narrowing the sim-to-real gap for controllable 23-DoF dexterous world models.
- 2026-07-03 - Cross-Embodiment Robot Manipulation via a Unified Hand Action Space ([PDF](https://arxiv.org/pdf/2607.03570)) - Defines a shared hand action coordinate system and embodiment-specific decoders for zero-shot transfer.
- 2026-06-22 - LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation ([PDF](https://arxiv.org/pdf/2606.23685)) - Aligns human-hand trajectories and robot actions in a latent physical-reasoning space for scalable pretraining.
- 2026-06-21 - EgoSteer: A Full-Stack System Towards Steerable Dexterous Manipulation from Egocentric Videos ([PDF](https://arxiv.org/pdf/2607.09701)) - Combines egocentric human-video pretraining, a world-model-enhanced VLA, and DAgger to steer dexterous policies across tasks and embodiments.
- 2026-06-20 - KITE: Decoupling Kinematics and Interaction for Zero-Shot Cross-Embodiment Manipulation ([PDF](https://arxiv.org/pdf/2606.22113)) - Separates embodiment-independent interaction intent from a kinematic decoder that adapts to unseen hands.
- 2026-06-10 - LUCID: Learning Embodiment-Agnostic Intent Models from Unstructured Human Videos for Scalable Dexterous Robot Skill Acquisition ([PDF](https://arxiv.org/pdf/2606.11628)) - Learns a shared intent interface from videos, then decodes it into different robot embodiments.
- 2026-06-10 - InDex: Empowering VLA Models with Intent-Conditioned Arm-Hand Coordination for Dexterous Manipulation ([PDF](https://arxiv.org/pdf/2606.12109)) - Separates when to establish contact from how to realize it with morphology-specific fingers.
- 2026-06-09 - UniDexTok: A Unified Dexterous Hand Tokenizer from Real Data ([PDF](https://arxiv.org/pdf/2606.10683)) - Converts heterogeneous hand states into a shared discrete codebook that enables joint VLA training.
- 2026-03-17 - DexGrasp-Zero: A Morphology-Aligned Policy for Zero-Shot Cross-Embodiment Dexterous Grasping ([PDF](https://arxiv.org/pdf/2603.16806)) - Conditions a universal grasp policy directly on hand morphology to avoid per-hand retargeting errors.
- 2026-03-15 - One-Policy-Fits-All: Geometry-Aware Action Latents for Cross-Embodiment Manipulation ([PDF](https://arxiv.org/pdf/2603.14522)) - Encodes action intent in geometry-aware latents so one policy can serve grippers and high-DoF hands.
- 2026-02-28 - UniHM: Unified Dexterous Hand Manipulation with Vision Language Model ([PDF](https://arxiv.org/pdf/2603.00732)) - Introduces a unified hand tokenizer and trains language-conditioned manipulation from human-object sequences.
- 2026-02-18 - One Hand to Rule Them All: Canonical Representations for Unified Dexterous Manipulation ([PDF](https://arxiv.org/pdf/2602.16712)) - Parameterizes hand morphology and learns a smooth latent manifold that interpolates across kinematic designs.
- 2026-02-10 - DexImit: Learning Bimanual Dexterous Manipulation from Monocular Human Videos ([PDF](https://arxiv.org/pdf/2602.10105)) - Converts monocular human videos into physically plausible bimanual robot trajectories for cross-embodiment pretraining.
- 2026-02-09 - DexFormer: Cross-Embodied Dexterous Manipulation via History-Conditioned Transformer ([PDF](https://arxiv.org/pdf/2602.08278)) - Uses action history as a compact bridge for transferring manipulation skills between hands.
- 2026-01-31 - UniMorphGrasp: Diffusion Model with Morphology-Awareness for Cross-Embodiment Dexterous Grasp Generation ([PDF](https://arxiv.org/pdf/2602.00915)) - Maps different hands into a canonical human-like pose space before morphology-conditioned diffusion generation.
- 2026-01-13 - FSAG: Enhancing Human-to-Dexterous-Hand Finger-Specific Affordance Grounding via Diffusion Models ([PDF](https://arxiv.org/pdf/2601.08246)) - Grounds finger-specific affordances from pretrained diffusion priors without requiring a large robot grasp dataset.
- 2026-01-08 - Generate, Transfer, Adapt: Learning Functional Dexterous Grasping from a Single Human Demonstration ([PDF](https://arxiv.org/pdf/2601.05243)) - Builds a correspondence-based data engine that transfers one human functional grasp to many novel objects and robot hands.
- 2025-10-07 - MachaGrasp: Morphology-Aware Cross-Embodiment Dexterous Hand Articulation Generation for Grasping ([PDF](https://arxiv.org/pdf/2510.06068)) - Uses morphology embeddings and eigengrasp bases to decode low-dimensional articulation coefficients.
- 2025-09-29 - CEDex: Cross-Embodiment Dexterous Grasp Generation at Scale from Human-like Contact Representations ([PDF](https://arxiv.org/pdf/2509.24661)) - Represents contact in a human-like coordinate system to scale grasp generation across non-identical hands.
- 2025-07-03 - DexVLG: Dexterous Vision-Language-Grasp Model at Scale ([PDF](https://arxiv.org/pdf/2507.02747)) - Scales language-grounded grasp prediction with a 170M-pose synthetic dataset and part-level semantic supervision.
- 2025-06-17 - Latent Action Diffusion for Cross-Embodiment Manipulation ([PDF](https://arxiv.org/pdf/2506.14608)) - Learns contrastively aligned latent actions shared by anthropomorphic hands, human hands, and parallel grippers.
- 2025-05-30 - DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation ([PDF](https://arxiv.org/pdf/2505.24853)) - Retargets human demonstrations through a functional, contact-aware representation for bimanual hands.
- 2025-05-02 - DexFlow: A Unified Approach for Dexterous Hand Pose Retargeting and Interaction ([PDF](https://arxiv.org/pdf/2505.01083)) - Couples retargeting with hand-object interaction modeling instead of optimizing hand pose in isolation.
- 2025-03-10 - Geometric Retargeting: A Principled, Ultrafast Neural Hand Retargeting Algorithm ([PDF](https://arxiv.org/pdf/2503.07541)) - Learns a 1 kHz, calibration-light mapping from human keypoints to robot-hand keypoints.
- 2025-02-28 - DexGraspVLA: A Vision-Language-Action Framework Towards General Dexterous Grasping ([PDF](https://arxiv.org/pdf/2502.20900)) - Uses a hierarchical VLM planner and diffusion action controller to make language-guided grasping robust to clutter and disturbances.

### Former / foundational

- Learning Cross-Hand Policies of High-DOF Reaching and Grasping ([PDF](https://arxiv.org/pdf/2404.09150)) - Uses gripper-agnostic keypoint displacements followed by hand-specific adaptation for cross-hand reaching and grasping.
- FunGrasp: Functional Grasping for Diverse Dexterous Hands ([PDF](https://arxiv.org/pdf/2411.16755)) - Grounds language and object-part affordances in a representation that supports functional grasps across hand designs.
- DexDiffuser: Generating Dexterous Grasps with Diffusion Models ([PDF](https://arxiv.org/pdf/2402.02989)) - Shows that diffusion in a structured grasp space can generate diverse, physically valid multi-finger poses.
- Dexterous Functional Pre-Grasp Manipulation with Diffusion Policy ([PDF](https://arxiv.org/pdf/2403.12421)) - Learns preparatory hand motions that make downstream functional grasping easier for a diffusion policy.
- Cross-Embodiment Dexterous Grasping with Reinforcement Learning ([PDF](https://arxiv.org/pdf/2410.02479)) - A foundational universal-policy formulation that separates hand morphology from shared grasp behavior.
- D(R,O) Grasp: A Unified Representation of Robot and Object Interaction for Cross-Embodiment Dexterous Grasping ([PDF](https://arxiv.org/pdf/2410.01702)) - Encodes robot-object interaction in a shared representation that separates morphology from grasp intent.

## 3. Dexterous hand + tactile sensing

### CVPR 2026

- ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation ([PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ForceVLA2_Unleashing_Hybrid_Force-Position_Control_with_Force_Awareness_for_Contact-Rich_CVPR_2026_paper.pdf)) - Adds force-aware hybrid position/force control so a VLA can react to contact instead of treating it as visual noise.
- AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models ([PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_AT-VLA_Adaptive_Tactile_Injection_for_Enhanced_Feedback_Reaction_in_Vision-Language-Action_CVPR_2026_paper.pdf)) - Injects tactile features adaptively at the layer and timestep where contact feedback matters most.
- Seeing Through Touch: Tactile-Driven Visual Localization of Material Regions ([PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Kim_Seeing_Through_Touch_Tactile-Driven_Visual_Localization_of_Material_Regions_CVPR_2026_paper.pdf)) - Uses touch to localize material regions in the visual scene, improving perception when appearance alone is ambiguous.
- Hoi! - A Multimodal Dataset for Force-Grounded, Cross-View Articulated Manipulation ([PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Engelbracht_Hoi_-_A_Multimodal_Dataset_for_Force-Grounded_Cross-View_Articulated_Manipulation_CVPR_2026_paper.pdf)) - Aligns force, vision, and articulated-object motion across views to make contact dynamics learnable.

### ICML 2026

- No direct dexterous-hand+tactile paper listed yet.

### ECCV 2026

- No dexterous-hand+tactile papers listed yet.

### Recent arXiv (2025-2026)

- 2026-08-03 - ReTouch: Empowering Contact-Rich Dexterous Manipulation with Online-Refined Tactile Prediction ([PDF](https://arxiv.org/pdf/2608.01824)) - Refines tactile predictions online during execution so contact-rich policies can recover from sensor and dynamics mismatch.
- 2026-08-03 - Semantic Haptic Feedback Enhances Dexterous Robotic Teleoperation ([PDF](https://arxiv.org/pdf/2608.02780)) - Encodes robot states as abstract haptic patterns through wristbands, reducing workload during bimanual dexterous teleoperation.
- 2026-07-30 - TacWAM: Anchor-Guided World Action Model with Mechanics-Aware Tactile Prediction ([PDF](https://arxiv.org/pdf/2607.28391)) - Predicts mechanics-aware tactile futures in a shared latent space while preventing future privileged signals from leaking into action generation.
- 2026-07-25 - Pose-Aware Modeling to Mitigate Pose-Related Artifacts in Tactile Gloves ([PDF](https://arxiv.org/pdf/2607.22964)) - Uses hand pose to remove pose-induced artifacts from tactile gloves, lowering minimum detectable force across users and glove designs.
- 2026-07-20 - Predicting Grasping Compliance in Robotic Hands through Analytical-Model-Informed Neural Networks ([PDF](https://arxiv.org/pdf/2607.17541)) - Combines analytical mechanics with neural learning to predict forceful grasp compliance and tool displacement in an underactuated robotic hand.
- 2026-07-16 - VTAP Gripper: Synergizing Fingertip Sensing and a Visuo-Tactile Active Palm for Dexterous In-Hand Manipulation ([PDF](https://arxiv.org/pdf/2607.15448)) - Combines an active visuo-tactile palm, fingertip arrays, and gesture-conditioned retargeting for contact-rich in-hand manipulation.
- 2026-07-16 - KineFuse: Kinematic-Aware Haptic Fusion for In-Hand Occluded-Object Pose Tracking ([PDF](https://arxiv.org/pdf/2607.14842)) - Fuses structured finger-level proprioception, force-torque, and contact tokens with vision to improve occluded object-pose tracking.
- 2026-07-10 - TactiDex: A Real-World Tactile-Guided Benchmark for Human-Like Dexterous Manipulation ([PDF](https://arxiv.org/pdf/2607.09190)) - Provides real-world tasks and evaluation protocols that explicitly test tactile-guided human-like dexterity.
- 2026-07-08 - TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation ([PDF](https://arxiv.org/pdf/2607.07287)) - Unifies tactile forecasting and fast reactive control in one predictive foundation model.
- 2026-07-03 - Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation ([PDF](https://arxiv.org/pdf/2607.03529)) - Treats motor current as a learnable contact signal for compliance when dedicated tactile sensors are unavailable.
- 2026-07-03 - CoorGrasp: Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty ([PDF](https://arxiv.org/pdf/2607.03557)) - Uses tactile-driven model-predictive control and coordinated force regulation to execute dexterous grasps robustly under uncertainty.
- 2026-07-01 - Human-Centric Transferable Tactile Pre-Training for Dexterous Robotic Manipulation ([PDF](https://arxiv.org/pdf/2607.01067)) - Pretrains tactile-action representations on large-scale human data and transfers them to fine-grained robot manipulation through unified spaces.
- 2026-06-30 - RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation ([PDF](https://arxiv.org/pdf/2606.31836)) - Releases aligned visual, tactile, and action trajectories for dual-arm humanoids with dexterous hands.
- 2026-06-30 - UniTacVLA: Unified Tactile Understanding and Prediction in Vision-Language-Action Models ([PDF](https://arxiv.org/pdf/2606.31723)) - Learns a shared tactile representation that supports both semantic understanding and future-contact prediction in VLAs.
- 2026-06-25 - VibeAct: Vibration to Actions for Contact-Rich Reactive Robot Dexterity ([PDF](https://arxiv.org/pdf/2606.27344)) - Converts high-frequency vibration cues into reactive actions for slip-sensitive dexterous tasks.
- 2026-06-15 - T-Rex: Tactile-Reactive Dexterous Manipulation ([PDF](https://arxiv.org/pdf/2606.17055)) - Builds a fast tactile reflex layer that complements slower visuomotor planning for contact transitions.
- 2026-06-14 - Transferring Contact, Not Just Motion: Compliant Grasping Across Dexterous Hands ([PDF](https://arxiv.org/pdf/2606.15516)) - Transfers a shared hand-pose latent together with calibrated effort signals, preserving contact regulation across morphologies.
- 2026-06-10 - Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning ([PDF](https://arxiv.org/pdf/2606.11767)) - Trains tactile-only grasping through a geometry-consistent real2sim2real pipeline.
- 2026-03-19 - OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation ([PDF](https://arxiv.org/pdf/2603.19201)) - Learns a visuo-tactile world model and a high-rate reflex controller that closes the loop on predicted contact states.
- 2026-03-18 - DexViTac: Collecting Human Visuo-Tactile-Kinematic Demonstrations for Contact-Rich Dexterous Manipulation ([PDF](https://arxiv.org/pdf/2603.17851)) - Couples first-person vision, dense tactile sensing, and hand kinematics in a portable data-collection system.
- 2026-03-16 - HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing ([PDF](https://arxiv.org/pdf/2603.15257)) - Distills tactile experience into a VLA so deployment can remain tactile-free while retaining contact knowledge.
- 2026-03-14 - TransDex: Pre-training Visuo-Tactile Policy with Point Cloud Reconstruction for Dexterous Manipulation of Transparent Objects ([PDF](https://arxiv.org/pdf/2603.13869)) - Uses point-cloud reconstruction as pretraining to recover geometry hidden by transparent-object and hand occlusions.
- 2026-03-10 - ReTac-ACT: A State-Gated Vision-Tactile Fusion Transformer for Precision Assembly ([PDF](https://arxiv.org/pdf/2603.09565)) - Gates tactile reliance with proprioception and reconstructs contact signals for sub-millimeter assembly corrections.
- 2026-03-04 - PTLD: Sim-to-Real Privileged Tactile Latent Distillation for Dexterous Manipulation ([PDF](https://arxiv.org/pdf/2603.04531)) - Distills privileged simulated tactile signals into deployable latent representations for real hands.
- 2026-02-10 - AnyTouch 2: General Optical Tactile Representation Learning for Dynamic Tactile Perception ([PDF](https://arxiv.org/pdf/2602.09617)) - Pretrains a sensor-agnostic optical-tactile encoder for dynamic contact understanding.
- 2026-02-05 - DECO: Decoupled Multimodal Diffusion Transformer for Bimanual Dexterous Manipulation with a Plugin Tactile Adapter ([PDF](https://arxiv.org/pdf/2602.05513)) - Adds tactile as a plug-in adapter to a multimodal diffusion policy, preserving a reusable visual backbone.
- 2025-12-24 - UniTacHand: Unified Spatio-Tactile Representation for Human to Robotic Hand Skill Transfer ([PDF](https://arxiv.org/pdf/2512.21233)) - Aligns human glove touch with robot-hand tactile signals for cross-domain skill transfer.
- 2025-12-18 - OPENTOUCH: Bringing Full-Hand Touch to Real-World Interaction ([PDF](https://arxiv.org/pdf/2512.16842)) - Releases an egocentric full-hand touch dataset that links where, when, and how forcefully a human hand contacts objects.
- 2025-08-12 - OmniVTLA: Vision-Tactile-Language-Action Model with Semantic-Aligned Tactile Sensing ([PDF](https://arxiv.org/pdf/2508.08706)) - Aligns tactile features with language and vision so tactile observations can support semantic task generalization.
- 2025-07-14 - Demonstrating the Octopi-1.5 Visual-Tactile-Language Model ([PDF](https://arxiv.org/pdf/2507.09985)) - Demonstrates a visual-tactile-language model that grounds tactile observations in language-conditioned manipulation.
- 2025-07-12 - Tactile-VLA: Unlocking Vision-Language-Action Model's Physical Knowledge for Tactile Generalization ([PDF](https://arxiv.org/pdf/2507.09160)) - Connects a VLA's implicit physical knowledge to tactile feedback with a hybrid position-force controller and few demonstrations.
- 2025-05-09 - APPLE: Toward General Active Perception via Reinforcement Learning ([PDF](https://arxiv.org/pdf/2505.06182)) - Jointly trains a transformer perception module and an RL exploration policy, including active tactile perception tasks.

### Former / foundational

- Canonical Representation and Force-Based Pretraining of 3D Tactile for Dexterous Visuo-Tactile Policy Learning ([PDF](https://arxiv.org/pdf/2409.17549)) - Uses canonical 3D tactile coordinates and force-based pretraining to make full-hand tactile features transferable.
- 3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing ([PDF](https://arxiv.org/pdf/2410.24091)) - Fuses vision and tactile feedback for fine-grained manipulation under visual occlusion.
- Dexterity from Touch: Self-Supervised Pre-Training of Tactile Representations with Robotic Play ([PDF](https://arxiv.org/pdf/2303.12076)) - Learns tactile features from unlabeled robot play instead of task-specific annotations.
- See to Touch: Learning Tactile Dexterity through Visual Incentives ([PDF](https://arxiv.org/pdf/2309.12300)) - Uses visual goals to shape tactile representations and improve contact-rich dexterity.
- Robot Synesthesia: In-Hand Manipulation with Visuotactile Sensing ([PDF](https://arxiv.org/pdf/2312.01853)) - Shows that synchronized vision and touch enable robust in-hand manipulation under severe occlusion.
- DexTouch: Learning to Seek and Manipulate Objects with Tactile Dexterity ([PDF](https://arxiv.org/pdf/2401.12496)) - Frames tactile exploration and manipulation as one closed-loop dexterous policy.
- Bi-Touch: Bimanual Tactile Manipulation with Sim-to-Real Deep Reinforcement Learning ([PDF](https://arxiv.org/pdf/2307.06423)) - Demonstrates that tactile feedback can make bimanual sim-to-real dexterous control robust.
- All the Feels: A Dexterous Hand with Large-Area Tactile Sensing ([PDF](https://arxiv.org/pdf/2210.15658)) - Introduces full-hand tactile coverage that exposes contact patterns beyond fingertips.
