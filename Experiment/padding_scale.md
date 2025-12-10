[TOC]

# Batch 32 Fixed

Need to force disable cache tokenizer



## Padding 16

Accuracy: 

```
Model: ./bert-base-uncased-finetuned
Accuracy: 0.9280 (92.80%)
```

```
***** train metrics *****
  epoch                    =        3.0
  eval_loss                =     0.5527
  eval_runtime             = 0:00:02.42
  eval_samples_per_second  =   1650.083
  eval_steps_per_second    =     103.13
  total_flos               =   183787GF
  train_loss               =     0.5627
  train_runtime            = 0:02:00.56
  train_samples_per_second =    199.059
  train_steps_per_second   =      6.221
```

Stochastic Rounding on acc: 93.05%

## Padding 32

Accuracy: 94.30%

Stochastic Rounding on acc: 94.05%

```
***** train metrics *****
  epoch                    =        3.0
  eval_loss                =     0.1849
  eval_runtime             = 0:00:02.42
  eval_samples_per_second  =   1649.448
  eval_steps_per_second    =    103.091
  total_flos               =   367575GF
  train_loss               =     0.2833
  train_runtime            = 0:02:03.15
  train_samples_per_second =     194.87
  train_steps_per_second   =       6.09
```

**Summary metrics account for Logical NeuronCore config = 2**

| Group                                              | Name                                 | Value         |
| -------------------------------------------------- | ------------------------------------ | ------------- |
| overall_stats                                      | **event_count**                      | 539986        |
| **hardware_flops**                                 | 636.277 **GFLOPS**                   |               |
| **mm_arithmetic_intensity**                        | 73.09 **flops/byte**                 |               |
| **model_flops**                                    | 525.577 **GFLOPS**                   |               |
| **neuroncore_cycle_count**                         | 76753832                             |               |
| **peak_flops_bandwidth_ratio**                     | 223.78                               |               |
| **total_time**                                     | 54.82 **ms**                         |               |
| **trace_count**                                    | 2394065                              |               |
| **transpose_flops**                                | 110.7 **GFLOPS**                     |               |
| data_movement                                      | **dma_active_cycles**                | 62897996      |
| **dma_active_time**                                | 44.93 **ms**                         |               |
| **dma_active_time_percent**                        | 81.95 **%**                          |               |
| **dma_packet_time**                                | 462.33 **ms**                        |               |
| **dma_queue_count**                                | 118                                  |               |
| **dma_transfer_average_bytes**                     | 289.364 **KiB**                      |               |
| **dma_transfer_count**                             | 12745                                |               |
| **dma_transfer_time**                              | 173.37 **ms**                        |               |
| **dma_transfer_total_bytes**                       | 3.517 **GiB**                        |               |
| **dynamic_dma_packet_percent**                     | 56.39 **%**                          |               |
| **dynamic_dma_size_percent**                       | 40.18 **%**                          |               |
| **hbm_read_bytes**                                 | 3.995 **GiB**                        |               |
| **hbm_write_bytes**                                | 2.702 **GiB**                        |               |
| **input_queue_bytes**                              | 4.402 **MiB**                        |               |
| **inputs_and_weights_size_bytes**                  | 1.224 **GiB**                        |               |
| **mbu_estimated_percent**                          | 31.99 **%**                          |               |
| **mbu_min_read_util_percent**                      | 5.85 **%**                           |               |
| **output_queue_bytes**                             | 0 **B**                              |               |
| **psum_read_bytes**                                | 24.384 **MiB**                       |               |
| **psum_read_sbuf_write_bytes**                     | 14.382 **MiB**                       |               |
| **psum_read_sbuf_write_count**                     | 15171                                |               |
| **psum_write_bytes**                               | 57.041 **MiB**                       |               |
| **sbuf_read_bytes**                                | 2.732 **GiB**                        |               |
| **sbuf_write_bytes**                               | 3.637 **GiB**                        |               |
| **software_dynamic_dma_packet_count**              | 839104                               |               |
| **software_dynamic_dma_size**                      | 2.773 **GiB**                        |               |
| **spill_reload_bytes**                             | 2.034 **GiB**                        |               |
| **spill_save_bytes**                               | 1.39 **GiB**                         |               |
| **static_dma_packet_count**                        | 648906                               |               |
| **static_dma_size**                                | 4.129 **GiB**                        |               |
| **weight_queue_bytes**                             | 3.513 **GiB**                        |               |
| **weight_size_bytes**                              | 112 **KiB**                          |               |
| tensor_engine                                      | **hfu_estimated_percent**            | 12.65 **%**   |
| **matmul_instruction_count**                       | 102498                               |               |
| **mfu_estimated_percent**                          | 10.45 **%**                          |               |
| **mfu_max_achievable_estimated_percent**           | 32.66 **%**                          |               |
| **tensor_engine_active_time**                      | 11.63 **ms**                         |               |
| **tensor_engine_active_time_percent**              | 21.21 **%**                          |               |
| **tensor_engine_instruction_count**                | 206029                               |               |
| **tensor_engine_instruction_time**                 | 33.72 **ms**                         |               |
| vector_engine                                      | **vector_engine_active_time**        | 22.02 **ms**  |
| **vector_engine_active_time_percent**              | 40.17 **%**                          |               |
| **vector_engine_instruction_count**                | 59219                                |               |
| **vector_engine_instruction_time**                 | 24.69 **ms**                         |               |
| scalar_engine                                      | **activate_instruction_count**       | 43703         |
| **activate_instruction_time**                      | 19.44 **ms**                         |               |
| **scalar_engine_active_time**                      | 18.04 **ms**                         |               |
| **scalar_engine_active_time_percent**              | 32.9 **%**                           |               |
| **scalar_engine_instruction_count**                | 53397                                |               |
| **scalar_engine_instruction_time**                 | 19.63 **ms**                         |               |
| sync_engine                                        | **sync_engine_active_time**          | 409.83 **us** |
| **sync_engine_active_time_percent**                | 0.75 **%**                           |               |
| **sync_engine_instruction_count**                  | 11961                                |               |
| **sync_engine_instruction_time**                   | 409.83 **us**                        |               |
| gpsimd_engine                                      | **gpsimd_engine_active_time**        | 1.91 **ms**   |
| **gpsimd_engine_active_time_percent**              | 3.49 **%**                           |               |
| **gpsimd_engine_instruction_count**                | 22718                                |               |
| **gpsimd_engine_instruction_time**                 | 1.91 **ms**                          |               |
| cc_engine                                          | **cc_cores_instruction_active_time** | 3.11 **us**   |
| **cc_cores_instruction_active_time_percent**       | 0.0057 **%**                         |               |
| **cc_cores_instruction_count**                     | 539                                  |               |
| **cc_cores_instruction_time**                      | 45.8 **us**                          |               |
| **cc_op_active_time**                              | 14.7 **ms**                          |               |
| **cc_op_active_time_percent**                      | 26.81 **%**                          |               |
| **cc_op_count**                                    | 5                                    |               |
| **cc_op_time**                                     | 14.7 **ms**                          |               |
| system                                             | **collectives_version**              | 2.28.27 ()    |
| **compiler_version**                               | 2.21.18209.0+043b1bf7                |               |
| **driver_version**                                 | 2.24.0 ()                            |               |
| **instance_type**                                  | trn1.2xlarge                         |               |
| **nc_idx**                                         | 0                                    |               |
| **nd_idx**                                         | 0                                    |               |
| **profiler_version**                               | 2.26.14.0%kaena-tools/2.26@6459a28   |               |
| **runtime_version**                                | 2.28.23 (dd587)                      |               |
| throttling_nc0                                     | **throttle_active_nc0_time_ns**      | 3.73 **ms**   |
| **throttle_activity_0_active_time_nc0_percent**    | 3.08 **%**                           |               |
| **throttle_activity_0_avg_util_limit_nc0_percent** | 87.5 **%**                           |               |
| **throttle_activity_1_active_time_nc0_percent**    | 3.73 **%**                           |               |
| **throttle_activity_1_avg_util_limit_nc0_percent** | 87.5 **%**                           |               |
| **throttle_avg_util_limit_nc0_percent**            | 99.04 **%**                          |               |

| 0    | 0    | generic               | 64 **KiB**      |
| ---- | ---- | --------------------- | --------------- |
| 0    | 0    | Tensor                | 25.14 **MiB**   |
| 0    | 0    | Scalar                | 6.359 **MiB**   |
| 0    | 0    | GpSimd                | 2.564 **MiB**   |
| 0    | 0    | io                    | 72 **B**        |
| 0    | 0    | Syncill               | 0 **B**         |
| 0    | 0    | weight                | 224.004 **KiB** |
| 0    | 0    | profiler buffers      | 2.443 **GiB**   |
| 0    | 0    | Scalar table          | 492 **KiB**     |
| 0    | 0    | Vector                | 6.639 **MiB**   |
| 0    | 0    | Sync                  | 1.375 **MiB**   |
| 0    | 0    | shared scratchpad     | 1.5 **GiB**     |
| 0    | 0    | tensor                | 1.224 **GiB**   |
| 0    | 0    | ucode                 | 97.677 **MiB**  |
| 0    | 0    | GpSimd stdio          | 1.063 **KiB**   |
| 0    | 0    | collectives           | 110.08 **MiB**  |
| 0    | 0    | scratchpad            | 0 **B**         |
| 0    | 0    | xt cc                 | 0 **B**         |
| 0    | 0    | dma rings runtime     | 44 **KiB**      |
| 0    | 0    | dma rings Syncill     | 54.668 **MiB**  |
| 0    | 0    | dma rings io          | 1.972 **MiB**   |
| 0    | 0    | dma rings collectives | 5.575 **MiB**   |
| 0    | 0    | Total                 | 5.473 **GiB**   |

## Padding 64

Accuracy: 94.15%

```
***** train metrics *****
  epoch                    =        3.0
  eval_loss                =     0.1247
  eval_runtime             = 0:00:02.62
  eval_samples_per_second  =   1521.972
  eval_steps_per_second    =     95.123
  total_flos               =   735150GF
  train_loss               =     0.2482
  train_runtime            = 0:02:22.60
  train_samples_per_second =      168.3
  train_steps_per_second   =      5.259
```

## Padding 128

Accuracy: 94.15%

```
***** train metrics *****
  epoch                    =        3.0
  eval_loss                =     0.1247
  eval_runtime             = 0:00:02.98
  eval_samples_per_second  =   1340.214
  eval_steps_per_second    =     83.763
  total_flos               =  1470300GF
  train_loss               =     0.2553
  train_runtime            = 0:02:55.51
  train_samples_per_second =    136.737
  train_steps_per_second   =      4.273
```