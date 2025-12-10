# Discription

This project investigates the performance, efficiency, and optimization behavior of BERT fine-tuning across heterogeneous accelerators—AWS Trainium (Trn1-2xlarge) and NVIDIA GPUs (T4, L4, A100). Our goal is to understand how these platforms differ in throughput, utilization, compilation overhead, and cost when training the same Transformer workload.

We conduct a series of system-level experiments including batch-size scaling, sequence-length tuning, Neuron compiler optimization (O1/O2/O3), SWAP-enabled memory extension, stochastic rounding, learning-rate and LLRD tuning, roofline modeling, and profiling on both hardware families (Neuron Profiler and PyTorch+Nsight).

Our optimized pipeline achieves 5.5–7.3× speedup across all devices and improves accuracy from 92.9% to 94.65%. The study highlights where Trainium excels (large batches, static shapes, long workloads) and where NVIDIA GPUs remain more efficient (small workloads, dynamic shapes, short training). Cost-per-epoch analysis further reveals practical guidelines for choosing the best accelerator for real-world fine-tuning tasks.

# Milestones

| Milestone                           | Description                                                  | Status      |
| ----------------------------------- | ------------------------------------------------------------ | ----------- |
| **Dataset Preparation**             | Load, tokenize, and preprocess *dair-ai/emotion* dataset uniformly across devices | ✅ Completed |
| **Baseline Training (All Devices)** | Establish baseline throughput, accuracy, and train time on Trn1, T4, L4, A100 | ✅ Completed |
| **Hardware Profiling**              | Collect compute/memory traces using Neuron Profiler and PyTorch Profiler | ✅ Completed |
| **Roofline Analysis**               | Build Trainium/GPU roofline to analyze memory-bound vs compute-bound behavior | ✅ Completed |
| **Batch-Size Scaling (8→64)**       | Evaluate scaling effects and identify stalls/TE under-utilization | ✅ Completed |
| **Sequence-Length Tuning**          | Measure impact of L=16/32/64/128 on performance and compilation | ✅ Completed |
| **SWAP-Enabled Large Batch**        | Use SWAP to enable batch=64 beyond physical RAM limits       | ✅ Completed |
| **Neuron Compiler Optimization**    | Test `--optlevel` (O1/O2/O3), static-shape constraints, warm-cache effects | ✅ Completed |
| **Learning Rate & LLRD Tuning**     | Compare LR schedules and decay factors to stabilize accuracy | ✅ Completed |
| **GPU Warp Scheduling Study**       | Compare GPU warp scheduler with Trainium TE behavior at small batches | ✅ Completed |
| **End-to-End Optimization**         | Achieve final 5.5–7.3× speedup and improved accuracy         | ✅ Completed |
| **Cost Analysis**                   | Compare cost/epoch, samples/sec·$ ratios for all accelerators | ✅ Completed |
| **Final Report & Slides**           | Summarize results, figures, and insights for presentation    | ✅ Completed |

# Repository and Code Structure

### `Experiment` folder

- This folder contains the `.md` file containing the experiment and profile results

### `Pictures` folder

- This folder contains the pictures illustrated in the presentation and report

### `Nvidia` folder

- This folder contains the code used to do experiment on Nvidia platforms.
- `baseline.ipynb` is the main experiment file.

### `Trainium` folder

- This folder contains the code used to do experiment on Trainium platforms.
- `baseline.ipynb` is the main experiment file.
- `train.py` is the code for training.

# Running Commands

You have to first launch an instance `trn1-2xlarge` with `huggingdace-neuron` AMI

For Trainium Code, you can tune the experiment by changing code in `baseline.ipynb` and `train.py`

- Batch size: Change `--per_device_train_batch_size`

- Padding: Change `--train_max_length`

- Stochastic Rounding: Set env `NEURON_RT_STOCHASTIC_ROUNDING_EN=1`

- Compiler: Uncomment the following lines in `train_modified.py`

  - ```
    # compiler_flags = "--model-type=transformer --distribution-strategy=llm-training --optlevel=3"
    # os.environ["NEURON_CC_FLAGS"] = compiler_flags
    ```

- Learning Rate: Change `--learning_rate`

- Accuracy: Run `eval.py`



For Nvidia Code, change parameter in `/Nvidia/baseline.ipynb` accordingly.

The guide for running profile on Trainium is very complicated. If you want to know how to profile or want to see a demo, email Yuheng Wu (yw5372@nyu.edu).

# Results

See `results.pdf`, which is a scratch on our report