[TOC]

# Baseline

**Summary metrics account for Logical NeuronCore config = 2**

| Group                                              | Name                                 | Value        |
| -------------------------------------------------- | ------------------------------------ | ------------ |
| overall_stats                                      | **event_count**                      | 488839       |
| **hardware_flops**                                 | 654.344 **GFLOPS**                   |              |
| **mm_arithmetic_intensity**                        | 69.75 **flops/byte**                 |              |
| **model_flops**                                    | 536.363 **GFLOPS**                   |              |
| **neuroncore_cycle_count**                         | 75289488                             |              |
| **peak_flops_bandwidth_ratio**                     | 223.78                               |              |
| **total_time**                                     | 53.78 **ms**                         |              |
| **trace_count**                                    | 2299198                              |              |
| **transpose_flops**                                | 117.976 **GFLOPS**                   |              |
| data_movement                                      | **dma_active_cycles**                | 64163388     |
| **dma_active_time**                                | 45.83 **ms**                         |              |
| **dma_active_time_percent**                        | 85.22 **%**                          |              |
| **dma_packet_time**                                | 491.21 **ms**                        |              |
| **dma_queue_count**                                | 118                                  |              |
| **dma_transfer_average_bytes**                     | 340.347 **KiB**                      |              |
| **dma_transfer_count**                             | 12258                                |              |
| **dma_transfer_time**                              | 124.97 **ms**                        |              |
| **dma_transfer_total_bytes**                       | 3.979 **GiB**                        |              |
| **dynamic_dma_packet_percent**                     | 55.18 **%**                          |              |
| **dynamic_dma_size_percent**                       | 37.8 **%**                           |              |
| **hbm_read_bytes**                                 | 4.334 **GiB**                        |              |
| **hbm_write_bytes**                                | 2.828 **GiB**                        |              |
| **input_queue_bytes**                              | 4.411 **MiB**                        |              |
| **inputs_and_weights_size_bytes**                  | 1.224 **GiB**                        |              |
| **mbu_estimated_percent**                          | 34.88 **%**                          |              |
| **mbu_min_read_util_percent**                      | 5.96 **%**                           |              |
| **output_queue_bytes**                             | 0 **B**                              |              |
| **psum_read_bytes**                                | 20.806 **MiB**                       |              |
| **psum_read_sbuf_write_bytes**                     | 12.481 **MiB**                       |              |
| **psum_read_sbuf_write_count**                     | 13146                                |              |
| **psum_write_bytes**                               | 54.788 **MiB**                       |              |
| **sbuf_read_bytes**                                | 2.853 **GiB**                        |              |
| **sbuf_write_bytes**                               | 3.973 **GiB**                        |              |
| **software_dynamic_dma_packet_count**              | 839872                               |              |
| **software_dynamic_dma_size**                      | 2.776 **GiB**                        |              |
| **spill_reload_bytes**                             | 2.37 **GiB**                         |              |
| **spill_save_bytes**                               | 1.516 **GiB**                        |              |
| **static_dma_packet_count**                        | 682236                               |              |
| **static_dma_size**                                | 4.569 **GiB**                        |              |
| **weight_queue_bytes**                             | 3.974 **GiB**                        |              |
| **weight_size_bytes**                              | 112 **KiB**                          |              |
| tensor_engine                                      | **hfu_estimated_percent**            | 13.26 **%**  |
| **matmul_instruction_count**                       | 73230                                |              |
| **mfu_estimated_percent**                          | 10.87 **%**                          |              |
| **mfu_max_achievable_estimated_percent**           | 31.17 **%**                          |              |
| **tensor_engine_active_time**                      | 9.81 **ms**                          |              |
| **tensor_engine_active_time_percent**              | 18.23 **%**                          |              |
| **tensor_engine_instruction_count**                | 147557                               |              |
| **tensor_engine_instruction_time**                 | 26.24 **ms**                         |              |
| vector_engine                                      | **vector_engine_active_time**        | 20.33 **ms** |
| **vector_engine_active_time_percent**              | 37.8 **%**                           |              |
| **vector_engine_instruction_count**                | 46324                                |              |
| **vector_engine_instruction_time**                 | 22.63 **ms**                         |              |
| scalar_engine                                      | **activate_instruction_count**       | 40741        |
| **activate_instruction_time**                      | 17.95 **ms**                         |              |
| **scalar_engine_active_time**                      | 16.57 **ms**                         |              |
| **scalar_engine_active_time_percent**              | 30.82 **%**                          |              |
| **scalar_engine_instruction_count**                | 49161                                |              |
| **scalar_engine_instruction_time**                 | 18.12 **ms**                         |              |
| sync_engine                                        | **sync_engine_active_time**          | 322.1 **us** |
| **sync_engine_active_time_percent**                | 0.6 **%**                            |              |
| **sync_engine_instruction_count**                  | 10362                                |              |
| **sync_engine_instruction_time**                   | 322.1 **us**                         |              |
| gpsimd_engine                                      | **gpsimd_engine_active_time**        | 1.98 **ms**  |
| **gpsimd_engine_active_time_percent**              | 3.68 **%**                           |              |
| **gpsimd_engine_instruction_count**                | 22589                                |              |
| **gpsimd_engine_instruction_time**                 | 1.98 **ms**                          |              |
| cc_engine                                          | **cc_cores_instruction_active_time** | 3.11 **us**  |
| **cc_cores_instruction_active_time_percent**       | 0.0058 **%**                         |              |
| **cc_cores_instruction_count**                     | 539                                  |              |
| **cc_cores_instruction_time**                      | 11.86 **us**                         |              |
| **cc_op_active_time**                              | 13.93 **ms**                         |              |
| **cc_op_active_time_percent**                      | 25.9 **%**                           |              |
| **cc_op_count**                                    | 5                                    |              |
| **cc_op_time**                                     | 13.93 **ms**                         |              |
| system                                             | **collectives_version**              | 2.28.27 ()   |
| **compiler_version**                               | 2.21.18209.0+043b1bf7                |              |
| **driver_version**                                 | 2.24.0 ()                            |              |
| **instance_type**                                  | trn1.2xlarge                         |              |
| **nc_idx**                                         | 0                                    |              |
| **nd_idx**                                         | 0                                    |              |
| **profiler_version**                               | 2.26.14.0%kaena-tools/2.26@6459a28   |              |
| **runtime_version**                                | 2.28.23 (dd587)                      |              |
| throttling_nc0                                     | **throttle_active_nc0_time_ns**      | 3.15 **ms**  |
| **throttle_activity_0_active_time_nc0_percent**    | 2.75 **%**                           |              |
| **throttle_activity_0_avg_util_limit_nc0_percent** | 87.5 **%**                           |              |
| **throttle_activity_1_active_time_nc0_percent**    | 3.09 **%**                           |              |
| **throttle_activity_1_avg_util_limit_nc0_percent** | 87.5 **%**                           |              |
| **throttle_avg_util_limit_nc0_percent**            | 109.67 **%**                         |              |
| **throttle_periodic_active_time_nc0_percent**      | 0.041 **%**                          |              |
| **throttle_periodic_avg_util_limit_nc0_percent**   | 25300 **%**                          |              |



| ND Idx | NC Idx | Usage Type            | Amount          |
| ------ | ------ | --------------------- | --------------- |
| 0      | 0      | generic               | 64 **KiB**      |
| 0      | 0      | Tensor                | 17.995 **MiB**  |
| 0      | 0      | Scalar                | 5.826 **MiB**   |
| 0      | 0      | GpSimd                | 2.553 **MiB**   |
| 0      | 0      | io                    | 64 **B**        |
| 0      | 0      | Syncill               | 0 **B**         |
| 0      | 0      | weight                | 240.004 **KiB** |
| 0      | 0      | profiler buffers      | 2.443 **GiB**   |
| 0      | 0      | Scalar table          | 492 **KiB**     |
| 0      | 0      | Vector                | 5.057 **MiB**   |
| 0      | 0      | Sync                  | 1.114 **MiB**   |
| 0      | 0      | shared scratchpad     | 1.5 **GiB**     |
| 0      | 0      | tensor                | 1.224 **GiB**   |
| 0      | 0      | ucode                 | 97.677 **MiB**  |
| 0      | 0      | GpSimd stdio          | 1.063 **KiB**   |
| 0      | 0      | collectives           | 110.08 **MiB**  |
| 0      | 0      | scratchpad            | 0 **B**         |
| 0      | 0      | xt cc                 | 0 **B**         |
| 0      | 0      | dma rings runtime     | 44 **KiB**      |
| 0      | 0      | dma rings Syncill     | 63.538 **MiB**  |
| 0      | 0      | dma rings io          | 1.847 **MiB**   |
| 0      | 0      | dma rings collectives | 5.575 **MiB**   |
| 0      | 0      | Total                 | 5.472 **GiB**   |



# Batch 16

```
***** train metrics *****
  epoch                    =        3.0
  eval_loss                =     0.1337
  eval_runtime             = 0:00:02.94
  eval_samples_per_second  =    679.083
  eval_steps_per_second    =     42.443
  total_flos               =  1470300GF
  train_loss               =     0.2154
  train_runtime            = 0:04:14.32
  train_samples_per_second =     94.369
  train_steps_per_second   =      5.898
```

**Summary metrics account for Logical NeuronCore config = 2**

| Group                                              | Name                                 | Value        |
| -------------------------------------------------- | ------------------------------------ | ------------ |
| overall_stats                                      | **event_count**                      | 723620       |
| **hardware_flops**                                 | 1.287 **TFLOPS**                     |              |
| **mm_arithmetic_intensity**                        | 94.82 **flops/byte**                 |              |
| **model_flops**                                    | 1.073 **TFLOPS**                     |              |
| **neuroncore_cycle_count**                         | 102717328                            |              |
| **peak_flops_bandwidth_ratio**                     | 223.78                               |              |
| **total_time**                                     | 73.37 **ms**                         |              |
| **trace_count**                                    | 3280551                              |              |
| **transpose_flops**                                | 213.983 **GFLOPS**                   |              |
| data_movement                                      | **dma_active_cycles**                | 86135712     |
| **dma_active_time**                                | 61.53 **ms**                         |              |
| **dma_active_time_percent**                        | 83.86 **%**                          |              |
| **dma_packet_time**                                | 683.86 **ms**                        |              |
| **dma_queue_count**                                | 118                                  |              |
| **dma_transfer_average_bytes**                     | 358.558 **KiB**                      |              |
| **dma_transfer_count**                             | 21501                                |              |
| **dma_transfer_time**                              | 393.48 **ms**                        |              |
| **dma_transfer_total_bytes**                       | 7.352 **GiB**                        |              |
| **dynamic_dma_packet_percent**                     | 40.41 **%**                          |              |
| **dynamic_dma_size_percent**                       | 25.99 **%**                          |              |
| **hbm_read_bytes**                                 | 6.481 **GiB**                        |              |
| **hbm_write_bytes**                                | 4.055 **GiB**                        |              |
| **input_queue_bytes**                              | 4.534 **MiB**                        |              |
| **inputs_and_weights_size_bytes**                  | 1.224 **GiB**                        |              |
| **mbu_estimated_percent**                          | 37.61 **%**                          |              |
| **mbu_min_read_util_percent**                      | 4.37 **%**                           |              |
| **output_queue_bytes**                             | 0 **B**                              |              |
| **psum_read_bytes**                                | 36.329 **MiB**                       |              |
| **psum_read_sbuf_write_bytes**                     | 20.956 **MiB**                       |              |
| **psum_read_sbuf_write_count**                     | 22346                                |              |
| **psum_write_bytes**                               | 95.314 **MiB**                       |              |
| **sbuf_read_bytes**                                | 4.148 **GiB**                        |              |
| **sbuf_write_bytes**                               | 6.135 **GiB**                        |              |
| **software_dynamic_dma_packet_count**              | 840896                               |              |
| **software_dynamic_dma_size**                      | 2.777 **GiB**                        |              |
| **spill_reload_bytes**                             | 4.516 **GiB**                        |              |
| **spill_save_bytes**                               | 2.743 **GiB**                        |              |
| **static_dma_packet_count**                        | 1239968                              |              |
| **static_dma_size**                                | 7.908 **GiB**                        |              |
| **weight_queue_bytes**                             | 7.348 **GiB**                        |              |
| **weight_size_bytes**                              | 112 **KiB**                          |              |
| tensor_engine                                      | **hfu_estimated_percent**            | 19.11 **%**  |
| **matmul_instruction_count**                       | 139846                               |              |
| **mfu_estimated_percent**                          | 15.94 **%**                          |              |
| **mfu_max_achievable_estimated_percent**           | 42.37 **%**                          |              |
| **tensor_engine_active_time**                      | 19.15 **ms**                         |              |
| **tensor_engine_active_time_percent**              | 26.11 **%**                          |              |
| **tensor_engine_instruction_count**                | 281477                               |              |
| **tensor_engine_instruction_time**                 | 50.75 **ms**                         |              |
| vector_engine                                      | **vector_engine_active_time**        | 27.99 **ms** |
| **vector_engine_active_time_percent**              | 38.15 **%**                          |              |
| **vector_engine_instruction_count**                | 64827                                |              |
| **vector_engine_instruction_time**                 | 31.51 **ms**                         |              |
| scalar_engine                                      | **activate_instruction_count**       | 52188        |
| **activate_instruction_time**                      | 22.88 **ms**                         |              |
| **scalar_engine_active_time**                      | 21 **ms**                            |              |
| **scalar_engine_active_time_percent**              | 28.63 **%**                          |              |
| **scalar_engine_instruction_count**                | 64551                                |              |
| **scalar_engine_instruction_time**                 | 23.14 **ms**                         |              |
| sync_engine                                        | **sync_engine_active_time**          | 0.53 **ms**  |
| **sync_engine_active_time_percent**                | 0.73 **%**                           |              |
| **sync_engine_instruction_count**                  | 19391                                |              |
| **sync_engine_instruction_time**                   | 0.53 **ms**                          |              |
| gpsimd_engine                                      | **gpsimd_engine_active_time**        | 3.6 **ms**   |
| **gpsimd_engine_active_time_percent**              | 4.9 **%**                            |              |
| **gpsimd_engine_instruction_count**                | 24320                                |              |
| **gpsimd_engine_instruction_time**                 | 3.6 **ms**                           |              |
| cc_engine                                          | **cc_cores_instruction_active_time** | 3.11 **us**  |
| **cc_cores_instruction_active_time_percent**       | 0.0042 **%**                         |              |
| **cc_cores_instruction_count**                     | 539                                  |              |
| **cc_cores_instruction_time**                      | 20.73 **us**                         |              |
| **cc_op_active_time**                              | 13.47 **ms**                         |              |
| **cc_op_active_time_percent**                      | 18.36 **%**                          |              |
| **cc_op_count**                                    | 5                                    |              |
| **cc_op_time**                                     | 13.47 **ms**                         |              |
| system                                             | **collectives_version**              | 2.28.27 ()   |
| **compiler_version**                               | 2.21.18209.0+043b1bf7                |              |
| **driver_version**                                 | 2.24.0 ()                            |              |
| **instance_type**                                  | trn1.2xlarge                         |              |
| **nc_idx**                                         | 0                                    |              |
| **nd_idx**                                         | 0                                    |              |
| **profiler_version**                               | 2.26.14.0%kaena-tools/2.26@6459a28   |              |
| **runtime_version**                                | 2.28.23 (dd587)                      |              |
| throttling_nc0                                     | **throttle_active_nc0_time_ns**      | 6.73 **ms**  |
| **throttle_activity_0_active_time_nc0_percent**    | 5.1 **%**                            |              |
| **throttle_activity_0_avg_util_limit_nc0_percent** | 87.5 **%**                           |              |
| **throttle_activity_1_active_time_nc0_percent**    | 4.07 **%**                           |              |
| **throttle_activity_1_avg_util_limit_nc0_percent** | 87.5 **%**                           |              |
| **throttle_avg_util_limit_nc0_percent**            | 98.74 **%**                          |              |

|      |      |                       |                 |
| ---- | ---- | --------------------- | --------------- |
| 0    | 0    | generic               | 64 **KiB**      |
| 0    | 0    | Tensor                | 34.35 **MiB**   |
| 0    | 0    | Scalar                | 7.696 **MiB**   |
| 0    | 0    | GpSimd                | 2.806 **MiB**   |
| 0    | 0    | io                    | 72 **B**        |
| 0    | 0    | Syncill               | 0 **B**         |
| 0    | 0    | weight                | 240.004 **KiB** |
| 0    | 0    | profiler buffers      | 2.443 **GiB**   |
| 0    | 0    | Scalar table          | 492 **KiB**     |
| 0    | 0    | Vector                | 7.304 **MiB**   |
| 0    | 0    | Sync                  | 2.224 **MiB**   |
| 0    | 0    | shared scratchpad     | 2 **GiB**       |
| 0    | 0    | tensor                | 1.224 **GiB**   |
| 0    | 0    | ucode                 | 97.677 **MiB**  |
| 0    | 0    | GpSimd stdio          | 1.063 **KiB**   |
| 0    | 0    | collectives           | 110.08 **MiB**  |
| 0    | 0    | scratchpad            | 0 **B**         |
| 0    | 0    | xt cc                 | 0 **B**         |
| 0    | 0    | dma rings runtime     | 44 **KiB**      |
| 0    | 0    | dma rings Syncill     | 127.049 **MiB** |
| 0    | 0    | dma rings io          | 1.737 **MiB**   |
| 0    | 0    | dma rings collectives | 5.575 **MiB**   |
| 0    | 0    | Total                 | 6.056 **GiB**   |



# Batch 32

```
***** train metrics *****
  epoch                    =        3.0
  eval_loss                =     0.1247
  eval_runtime             = 0:00:02.99
  eval_samples_per_second  =   1335.474
  eval_steps_per_second    =     83.467
  total_flos               =  1470300GF
  train_loss               =     0.2553
  train_runtime            = 0:02:54.60
  train_samples_per_second =     137.45
  train_steps_per_second   =      4.295
```

**Summary metrics account for Logical NeuronCore config = 2**

| Group                                              | Name                                 | Value        |
| -------------------------------------------------- | ------------------------------------ | ------------ |
| overall_stats                                      | **event_count**                      | 1282189      |
| **hardware_flops**                                 | 2.551 **TFLOPS**                     |              |
| **mm_arithmetic_intensity**                        | 108.42 **flops/byte**                |              |
| **model_flops**                                    | 2.145 **TFLOPS**                     |              |
| **neuroncore_cycle_count**                         | 160573760                            |              |
| **peak_flops_bandwidth_ratio**                     | 223.78                               |              |
| **total_time**                                     | 114.7 **ms**                         |              |
| **trace_count**                                    | 5912873                              |              |
| **transpose_flops**                                | 405.991 **GFLOPS**                   |              |
| data_movement                                      | **dma_active_cycles**                | 135839264    |
| **dma_active_time**                                | 97.03 **ms**                         |              |
| **dma_active_time_percent**                        | 84.6 **%**                           |              |
| **dma_packet_time**                                | 1.14 **s**                           |              |
| **dma_queue_count**                                | 118                                  |              |
| **dma_transfer_average_bytes**                     | 351.788 **KiB**                      |              |
| **dma_transfer_count**                             | 42059                                |              |
| **dma_transfer_time**                              | 445.1 **ms**                         |              |
| **dma_transfer_total_bytes**                       | 14.11 **GiB**                        |              |
| **dynamic_dma_packet_percent**                     | 33.87 **%**                          |              |
| **dynamic_dma_size_percent**                       | 18.87 **%**                          |              |
| **hbm_read_bytes**                                 | 11.683 **GiB**                       |              |
| **hbm_write_bytes**                                | 6.747 **GiB**                        |              |
| **input_queue_bytes**                              | 4.541 **MiB**                        |              |
| **inputs_and_weights_size_bytes**                  | 1.224 **GiB**                        |              |
| **mbu_estimated_percent**                          | 42.08 **%**                          |              |
| **mbu_min_read_util_percent**                      | 2.79 **%**                           |              |
| **output_queue_bytes**                             | 0 **B**                              |              |
| **psum_read_bytes**                                | 67.365 **MiB**                       |              |
| **psum_read_sbuf_write_bytes**                     | 37.906 **MiB**                       |              |
| **psum_read_sbuf_write_count**                     | 40632                                |              |
| **psum_write_bytes**                               | 176.361 **MiB**                      |              |
| **sbuf_read_bytes**                                | 6.975 **GiB**                        |              |
| **sbuf_write_bytes**                               | 10.808 **GiB**                       |              |
| **software_dynamic_dma_packet_count**              | 1274656                              |              |
| **software_dynamic_dma_size**                      | 3.355 **GiB**                        |              |
| **spill_reload_bytes**                             | 8.583 **GiB**                        |              |
| **spill_save_bytes**                               | 5.434 **GiB**                        |              |
| **static_dma_packet_count**                        | 2489194                              |              |
| **static_dma_size**                                | 14.428 **GiB**                       |              |
| **weight_queue_bytes**                             | 14.106 **GiB**                       |              |
| **weight_size_bytes**                              | 112 **KiB**                          |              |
| tensor_engine                                      | **hfu_estimated_percent**            | 24.25 **%**  |
| **matmul_instruction_count**                       | 272998                               |              |
| **mfu_estimated_percent**                          | 20.39 **%**                          |              |
| **mfu_max_achievable_estimated_percent**           | 48.45 **%**                          |              |
| **tensor_engine_active_time**                      | 37.99 **ms**                         |              |
| **tensor_engine_active_time_percent**              | 33.12 **%**                          |              |
| **tensor_engine_instruction_count**                | 552563                               |              |
| **tensor_engine_instruction_time**                 | 100.06 **ms**                        |              |
| vector_engine                                      | **vector_engine_active_time**        | 43.98 **ms** |
| **vector_engine_active_time_percent**              | 38.34 **%**                          |              |
| **vector_engine_instruction_count**                | 108117                               |              |
| **vector_engine_instruction_time**                 | 51.22 **ms**                         |              |
| scalar_engine                                      | **activate_instruction_count**       | 75056        |
| **activate_instruction_time**                      | 33.14 **ms**                         |              |
| **scalar_engine_active_time**                      | 30.36 **ms**                         |              |
| **scalar_engine_active_time_percent**              | 26.47 **%**                          |              |
| **scalar_engine_instruction_count**                | 95185                                |              |
| **scalar_engine_instruction_time**                 | 33.58 **ms**                         |              |
| sync_engine                                        | **sync_engine_active_time**          | 0.94 **ms**  |
| **sync_engine_active_time_percent**                | 0.82 **%**                           |              |
| **sync_engine_instruction_count**                  | 36994                                |              |
| **sync_engine_instruction_time**                   | 0.94 **ms**                          |              |
| gpsimd_engine                                      | **gpsimd_engine_active_time**        | 6.83 **ms**  |
| **gpsimd_engine_active_time_percent**              | 5.96 **%**                           |              |
| **gpsimd_engine_instruction_count**                | 31916                                |              |
| **gpsimd_engine_instruction_time**                 | 6.83 **ms**                          |              |
| cc_engine                                          | **cc_cores_instruction_active_time** | 3.11 **us**  |
| **cc_cores_instruction_active_time_percent**       | 0.0027 **%**                         |              |
| **cc_cores_instruction_count**                     | 539                                  |              |
| **cc_cores_instruction_time**                      | 16.95 **us**                         |              |
| **cc_op_active_time**                              | 16 **ms**                            |              |
| **cc_op_active_time_percent**                      | 13.95 **%**                          |              |
| **cc_op_count**                                    | 5                                    |              |
| **cc_op_time**                                     | 16 **ms**                            |              |
| system                                             | **collectives_version**              | 2.28.27 ()   |
| **compiler_version**                               | 2.21.18209.0+043b1bf7                |              |
| **driver_version**                                 | 2.24.0 ()                            |              |
| **instance_type**                                  | trn1.2xlarge                         |              |
| **nc_idx**                                         | 0                                    |              |
| **nd_idx**                                         | 0                                    |              |
| **profiler_version**                               | 2.26.14.0%kaena-tools/2.26@6459a28   |              |
| **runtime_version**                                | 2.28.23 (dd587)                      |              |
| throttling_nc0                                     | **throttle_active_nc0_time_ns**      | 16.24 **ms** |
| **throttle_activity_0_active_time_nc0_percent**    | 8.27 **%**                           |              |
| **throttle_activity_0_avg_util_limit_nc0_percent** | 87.5 **%**                           |              |
| **throttle_activity_1_active_time_nc0_percent**    | 5.88 **%**                           |              |
| **throttle_activity_1_avg_util_limit_nc0_percent** | 87.5 **%**                           |              |
| **throttle_avg_util_limit_nc0_percent**            | 98.14 **%**                          |              |

|      |      |                       |                 |
| ---- | ---- | --------------------- | --------------- |
| 0    | 0    | generic               | 64 **KiB**      |
| 0    | 0    | Tensor                | 67.436 **MiB**  |
| 0    | 0    | Scalar                | 11.453 **MiB**  |
| 0    | 0    | GpSimd                | 3.786 **MiB**   |
| 0    | 0    | io                    | 72 **B**        |
| 0    | 0    | Syncill               | 0 **B**         |
| 0    | 0    | weight                | 240.004 **KiB** |
| 0    | 0    | profiler buffers      | 2.443 **GiB**   |
| 0    | 0    | Scalar table          | 492 **KiB**     |
| 0    | 0    | Vector                | 12.594 **MiB**  |
| 0    | 0    | Sync                  | 4.402 **MiB**   |
| 0    | 0    | shared scratchpad     | 3.5 **GiB**     |
| 0    | 0    | tensor                | 1.225 **GiB**   |
| 0    | 0    | ucode                 | 97.677 **MiB**  |
| 0    | 0    | GpSimd stdio          | 1.063 **KiB**   |
| 0    | 0    | collectives           | 110.08 **MiB**  |
| 0    | 0    | scratchpad            | 0 **B**         |
| 0    | 0    | xt cc                 | 0 **B**         |
| 0    | 0    | dma rings runtime     | 44 **KiB**      |
| 0    | 0    | dma rings Syncill     | 272.058 **MiB** |
| 0    | 0    | dma rings io          | 1.654 **MiB**   |
| 0    | 0    | dma rings collectives | 5.575 **MiB**   |
| 0    | 0    | Total                 | 7.742 **GiB**   |

Host Used Memory          Total: 4.9GB          Tensors: 0.0B         Constants: 0.0B                             App. Memory: 4.9GB
 Device Used Memory        Total: 10.6GB         Tensors: 2.4GB        Constants: 220.6MB****



# Batch32 CC optim

```
***** train metrics *****
  epoch                    =        3.0
  eval_loss                =     0.1156
  eval_runtime             = 0:00:03.03
  eval_samples_per_second  =   1316.377
  eval_steps_per_second    =     82.274
  total_flos               =  1470300GF
  train_loss               =     0.2487
  train_runtime            = 0:02:54.40
  train_samples_per_second =    137.614
  train_steps_per_second   =        4.3
```

**Summary metrics account for Logical NeuronCore config = 2**

| Group                                              | Name                                 | Value        |
| -------------------------------------------------- | ------------------------------------ | ------------ |
| overall_stats                                      | **event_count**                      | 1252222      |
| **hardware_flops**                                 | 2.551 **TFLOPS**                     |              |
| **mm_arithmetic_intensity**                        | 109.11 **flops/byte**                |              |
| **model_flops**                                    | 2.145 **TFLOPS**                     |              |
| **neuroncore_cycle_count**                         | 159583184                            |              |
| **peak_flops_bandwidth_ratio**                     | 223.78                               |              |
| **total_time**                                     | 113.99 **ms**                        |              |
| **trace_count**                                    | 5817044                              |              |
| **transpose_flops**                                | 405.778 **GFLOPS**                   |              |
| data_movement                                      | **dma_active_cycles**                | 134427680    |
| **dma_active_time**                                | 96.02 **ms**                         |              |
| **dma_active_time_percent**                        | 84.24 **%**                          |              |
| **dma_packet_time**                                | 1.12 **s**                           |              |
| **dma_queue_count**                                | 118                                  |              |
| **dma_transfer_average_bytes**                     | 365.016 **KiB**                      |              |
| **dma_transfer_count**                             | 40237                                |              |
| **dma_transfer_time**                              | 422.06 **ms**                        |              |
| **dma_transfer_total_bytes**                       | 14.007 **GiB**                       |              |
| **dynamic_dma_packet_percent**                     | 34.32 **%**                          |              |
| **dynamic_dma_size_percent**                       | 19.03 **%**                          |              |
| **hbm_read_bytes**                                 | 11.49 **GiB**                        |              |
| **hbm_write_bytes**                                | 6.822 **GiB**                        |              |
| **input_queue_bytes**                              | 4.494 **MiB**                        |              |
| **inputs_and_weights_size_bytes**                  | 1.224 **GiB**                        |              |
| **mbu_estimated_percent**                          | 42.07 **%**                          |              |
| **mbu_min_read_util_percent**                      | 2.81 **%**                           |              |
| **output_queue_bytes**                             | 0 **B**                              |              |
| **psum_read_bytes**                                | 67.355 **MiB**                       |              |
| **psum_read_sbuf_write_bytes**                     | 36.587 **MiB**                       |              |
| **psum_read_sbuf_write_count**                     | 40359                                |              |
| **psum_write_bytes**                               | 176.341 **MiB**                      |              |
| **sbuf_read_bytes**                                | 6.891 **GiB**                        |              |
| **sbuf_write_bytes**                               | 10.615 **GiB**                       |              |
| **software_dynamic_dma_packet_count**              | 1271184                              |              |
| **software_dynamic_dma_size**                      | 3.343 **GiB**                        |              |
| **spill_reload_bytes**                             | 8.403 **GiB**                        |              |
| **spill_save_bytes**                               | 5.351 **GiB**                        |              |
| **static_dma_packet_count**                        | 2433125                              |              |
| **static_dma_size**                                | 14.224 **GiB**                       |              |
| **weight_queue_bytes**                             | 14.002 **GiB**                       |              |
| **weight_size_bytes**                              | 112 **KiB**                          |              |
| tensor_engine                                      | **hfu_estimated_percent**            | 24.39 **%**  |
| **matmul_instruction_count**                       | 272568                               |              |
| **mfu_estimated_percent**                          | 20.51 **%**                          |              |
| **mfu_max_achievable_estimated_percent**           | 48.76 **%**                          |              |
| **tensor_engine_active_time**                      | 37.86 **ms**                         |              |
| **tensor_engine_active_time_percent**              | 33.21 **%**                          |              |
| **tensor_engine_instruction_count**                | 550774                               |              |
| **tensor_engine_instruction_time**                 | 100.01 **ms**                        |              |
| vector_engine                                      | **vector_engine_active_time**        | 43.95 **ms** |
| **vector_engine_active_time_percent**              | 38.56 **%**                          |              |
| **vector_engine_instruction_count**                | 108081                               |              |
| **vector_engine_instruction_time**                 | 51.17 **ms**                         |              |
| scalar_engine                                      | **activate_instruction_count**       | 74886        |
| **activate_instruction_time**                      | 32.91 **ms**                         |              |
| **scalar_engine_active_time**                      | 30.03 **ms**                         |              |
| **scalar_engine_active_time_percent**              | 26.34 **%**                          |              |
| **scalar_engine_instruction_count**                | 95195                                |              |
| **scalar_engine_instruction_time**                 | 33.35 **ms**                         |              |
| sync_engine                                        | **sync_engine_active_time**          | 0.82 **ms**  |
| **sync_engine_active_time_percent**                | 0.72 **%**                           |              |
| **sync_engine_instruction_count**                  | 34418                                |              |
| **sync_engine_instruction_time**                   | 0.82 **ms**                          |              |
| gpsimd_engine                                      | **gpsimd_engine_active_time**        | 6.85 **ms**  |
| **gpsimd_engine_active_time_percent**              | 6.01 **%**                           |              |
| **gpsimd_engine_instruction_count**                | 31808                                |              |
| **gpsimd_engine_instruction_time**                 | 6.85 **ms**                          |              |
| cc_engine                                          | **cc_cores_instruction_active_time** | 3.11 **us**  |
| **cc_cores_instruction_active_time_percent**       | 0.0027 **%**                         |              |
| **cc_cores_instruction_count**                     | 539                                  |              |
| **cc_cores_instruction_time**                      | 13.7 **us**                          |              |
| **cc_op_active_time**                              | 15.61 **ms**                         |              |
| **cc_op_active_time_percent**                      | 13.7 **%**                           |              |
| **cc_op_count**                                    | 5                                    |              |
| **cc_op_time**                                     | 15.61 **ms**                         |              |
| system                                             | **collectives_version**              | 2.28.27 ()   |
| **compiler_version**                               | 2.21.18209.0+043b1bf7                |              |
| **driver_version**                                 | 2.24.0 ()                            |              |
| **instance_type**                                  | trn1.2xlarge                         |              |
| **nc_idx**                                         | 0                                    |              |
| **nd_idx**                                         | 0                                    |              |
| **profiler_version**                               | 2.26.14.0%kaena-tools/2.26@6459a28   |              |
| **runtime_version**                                | 2.28.23 (dd587)                      |              |
| throttling_nc0                                     | **throttle_active_nc0_time_ns**      | 16.9 **ms**  |
| **throttle_activity_0_active_time_nc0_percent**    | 9.04 **%**                           |              |
| **throttle_activity_0_avg_util_limit_nc0_percent** | 87.5 **%**                           |              |
| **throttle_activity_1_active_time_nc0_percent**    | 5.78 **%**                           |              |
| **throttle_activity_1_avg_util_limit_nc0_percent** | 87.5 **%**                           |              |
| **throttle_avg_util_limit_nc0_percent**            | 98.01 **%**                          |              |

|      |      |                       |                 |
| ---- | ---- | --------------------- | --------------- |
| 0    | 0    | generic               | 64 **KiB**      |
| 0    | 0    | Tensor                | 67.229 **MiB**  |
| 0    | 0    | Scalar                | 11.452 **MiB**  |
| 0    | 0    | GpSimd                | 3.761 **MiB**   |
| 0    | 0    | io                    | 72 **B**        |
| 0    | 0    | Syncill               | 0 **B**         |
| 0    | 0    | weight                | 240.004 **KiB** |
| 0    | 0    | profiler buffers      | 2.443 **GiB**   |
| 0    | 0    | Scalar table          | 492 **KiB**     |
| 0    | 0    | Vector                | 12.594 **MiB**  |
| 0    | 0    | Sync                  | 4.175 **MiB**   |
| 0    | 0    | shared scratchpad     | 3.5 **GiB**     |
| 0    | 0    | tensor                | 1.225 **GiB**   |
| 0    | 0    | ucode                 | 97.677 **MiB**  |
| 0    | 0    | GpSimd stdio          | 1.063 **KiB**   |
| 0    | 0    | collectives           | 110.08 **MiB**  |
| 0    | 0    | scratchpad            | 0 **B**         |
| 0    | 0    | xt cc                 | 0 **B**         |
| 0    | 0    | dma rings runtime     | 44 **KiB**      |
| 0    | 0    | dma rings Syncill     | 291.131 **MiB** |
| 0    | 0    | dma rings io          | 2.397 **MiB**   |
| 0    | 0    | dma rings collectives | 5.575 **MiB**   |
| 0    | 0    | Total                 | 7.761 **GiB**   |

# Batch 48

```
***** train metrics *****
  epoch                    =        3.0
  eval_loss                =     0.1292
  eval_runtime             = 0:00:02.99
  eval_samples_per_second  =   2002.073
  eval_steps_per_second    =     125.13
  total_flos               =  1473240GF
  train_loss               =     0.2845
  train_runtime            = 0:02:31.63
  train_samples_per_second =    158.591
  train_steps_per_second   =      3.304
```

**Summary metrics account for Logical NeuronCore config = 2**

| Group                                              | Name                                 | Value        |
| -------------------------------------------------- | ------------------------------------ | ------------ |
| overall_stats                                      | **event_count**                      | 1789392      |
| **hardware_flops**                                 | 3.816 **TFLOPS**                     |              |
| **mm_arithmetic_intensity**                        | 117.88 **flops/byte**                |              |
| **model_flops**                                    | 3.218 **TFLOPS**                     |              |
| **neuroncore_cycle_count**                         | 218188256                            |              |
| **peak_flops_bandwidth_ratio**                     | 223.78                               |              |
| **total_time**                                     | 155.85 **ms**                        |              |
| **trace_count**                                    | 8115415                              |              |
| **transpose_flops**                                | 598.021 **GFLOPS**                   |              |
| data_movement                                      | **dma_active_cycles**                | 182804208    |
| **dma_active_time**                                | 130.57 **ms**                        |              |
| **dma_active_time_percent**                        | 83.78 **%**                          |              |
| **dma_packet_time**                                | 1.54 **s**                           |              |
| **dma_queue_count**                                | 118                                  |              |
| **dma_transfer_average_bytes**                     | 349.109 **KiB**                      |              |
| **dma_transfer_count**                             | 60294                                |              |
| **dma_transfer_time**                              | 639.11 **ms**                        |              |
| **dma_transfer_total_bytes**                       | 20.074 **GiB**                       |              |
| **dynamic_dma_packet_percent**                     | 31.46 **%**                          |              |
| **dynamic_dma_size_percent**                       | 15.79 **%**                          |              |
| **hbm_read_bytes**                                 | 16.195 **GiB**                       |              |
| **hbm_write_bytes**                                | 9.23 **GiB**                         |              |
| **input_queue_bytes**                              | 4.556 **MiB**                        |              |
| **inputs_and_weights_size_bytes**                  | 1.224 **GiB**                        |              |
| **mbu_estimated_percent**                          | 42.72 **%**                          |              |
| **mbu_min_read_util_percent**                      | 2.06 **%**                           |              |
| **output_queue_bytes**                             | 0 **B**                              |              |
| **psum_read_bytes**                                | 96.718 **MiB**                       |              |
| **psum_read_sbuf_write_bytes**                     | 54.014 **MiB**                       |              |
| **psum_read_sbuf_write_count**                     | 58107                                |              |
| **psum_write_bytes**                               | 257.412 **MiB**                      |              |
| **sbuf_read_bytes**                                | 9.593 **GiB**                        |              |
| **sbuf_write_bytes**                               | 14.735 **GiB**                       |              |
| **software_dynamic_dma_packet_count**              | 1596768                              |              |
| **software_dynamic_dma_size**                      | 3.774 **GiB**                        |              |
| **spill_reload_bytes**                             | 12.063 **GiB**                       |              |
| **spill_save_bytes**                               | 7.917 **GiB**                        |              |
| **static_dma_packet_count**                        | 3478193                              |              |
| **static_dma_size**                                | 20.13 **GiB**                        |              |
| **weight_queue_bytes**                             | 20.07 **GiB**                        |              |
| **weight_size_bytes**                              | 112 **KiB**                          |              |
| tensor_engine                                      | **hfu_estimated_percent**            | 26.69 **%**  |
| **matmul_instruction_count**                       | 406160                               |              |
| **mfu_estimated_percent**                          | 22.51 **%**                          |              |
| **mfu_max_achievable_estimated_percent**           | 52.68 **%**                          |              |
| **tensor_engine_active_time**                      | 56.59 **ms**                         |              |
| **tensor_engine_active_time_percent**              | 36.31 **%**                          |              |
| **tensor_engine_instruction_count**                | 821614                               |              |
| **tensor_engine_instruction_time**                 | 149.19 **ms**                        |              |
| vector_engine                                      | **vector_engine_active_time**        | 60.33 **ms** |
| **vector_engine_active_time_percent**              | 38.71 **%**                          |              |
| **vector_engine_instruction_count**                | 147848                               |              |
| **vector_engine_instruction_time**                 | 70.19 **ms**                         |              |
| scalar_engine                                      | **activate_instruction_count**       | 97825        |
| **activate_instruction_time**                      | 43.16 **ms**                         |              |
| **scalar_engine_active_time**                      | 39.39 **ms**                         |              |
| **scalar_engine_active_time_percent**              | 25.27 **%**                          |              |
| **scalar_engine_instruction_count**                | 126050                               |              |
| **scalar_engine_instruction_time**                 | 43.79 **ms**                         |              |
| sync_engine                                        | **sync_engine_active_time**          | 1.36 **ms**  |
| **sync_engine_active_time_percent**                | 0.87 **%**                           |              |
| **sync_engine_instruction_count**                  | 56437                                |              |
| **sync_engine_instruction_time**                   | 1.36 **ms**                          |              |
| gpsimd_engine                                      | **gpsimd_engine_active_time**        | 10.08 **ms** |
| **gpsimd_engine_active_time_percent**              | 6.47 **%**                           |              |
| **gpsimd_engine_instruction_count**                | 38819                                |              |
| **gpsimd_engine_instruction_time**                 | 10.08 **ms**                         |              |
| cc_engine                                          | **cc_cores_instruction_active_time** | 3.11 **us**  |
| **cc_cores_instruction_active_time_percent**       | 0.002 **%**                          |              |
| **cc_cores_instruction_count**                     | 539                                  |              |
| **cc_cores_instruction_time**                      | 16.83 **us**                         |              |
| **cc_op_active_time**                              | 16.34 **ms**                         |              |
| **cc_op_active_time_percent**                      | 10.49 **%**                          |              |
| **cc_op_count**                                    | 5                                    |              |
| **cc_op_time**                                     | 16.34 **ms**                         |              |
| system                                             | **collectives_version**              | 2.28.27 ()   |
| **compiler_version**                               | 2.21.18209.0+043b1bf7                |              |
| **driver_version**                                 | 2.24.0 ()                            |              |
| **instance_type**                                  | trn1.2xlarge                         |              |
| **nc_idx**                                         | 0                                    |              |
| **nd_idx**                                         | 0                                    |              |
| **profiler_version**                               | 2.26.14.0%kaena-tools/2.26@6459a28   |              |
| **runtime_version**                                | 2.28.23 (dd587)                      |              |
| throttling_nc0                                     | **throttle_active_nc0_time_ns**      | 25.17 **ms** |
| **throttle_activity_0_active_time_nc0_percent**    | 9.44 **%**                           |              |
| **throttle_activity_0_avg_util_limit_nc0_percent** | 87.5 **%**                           |              |
| **throttle_activity_1_active_time_nc0_percent**    | 6.69 **%**                           |              |
| **throttle_activity_1_avg_util_limit_nc0_percent** | 87.5 **%**                           |              |
| **throttle_avg_util_limit_nc0_percent**            | 97.74 **%**                          |              |

| 0    | 0    | generic               | 64 **KiB**      |
| ---- | ---- | --------------------- | --------------- |
| 0    | 0    | Tensor                | 100.271 **MiB** |
| 0    | 0    | Scalar                | 15.241 **MiB**  |
| 0    | 0    | GpSimd                | 4.682 **MiB**   |
| 0    | 0    | io                    | 72 **B**        |
| 0    | 0    | Syncill               | 0 **B**         |
| 0    | 0    | weight                | 240.004 **KiB** |
| 0    | 0    | profiler buffers      | 2.443 **GiB**   |
| 0    | 0    | Scalar table          | 492 **KiB**     |
| 0    | 0    | Vector                | 17.423 **MiB**  |
| 0    | 0    | Sync                  | 6.759 **MiB**   |
| 0    | 0    | shared scratchpad     | 5 **GiB**       |
| 0    | 0    | tensor                | 1.226 **GiB**   |
| 0    | 0    | ucode                 | 97.677 **MiB**  |
| 0    | 0    | GpSimd stdio          | 1.063 **KiB**   |
| 0    | 0    | collectives           | 110.08 **MiB**  |
| 0    | 0    | scratchpad            | 0 **B**         |
| 0    | 0    | xt cc                 | 0 **B**         |
| 0    | 0    | dma rings runtime     | 44 **KiB**      |
| 0    | 0    | dma rings Syncill     | 401.105 **MiB** |
| 0    | 0    | dma rings io          | 1.659 **MiB**   |
| 0    | 0    | dma rings collectives | 5.575 **MiB**   |
| 0    | 0    | Total                 | 9.412 **GiB**   |

#  Batch 64 (swap)

```
***** train metrics *****
  epoch                    =        3.0
  eval_loss                =     0.1403
  eval_runtime             = 0:00:02.98
  eval_samples_per_second  =   2682.829
  eval_steps_per_second    =    167.677
  total_flos               =  1470300GF
  train_loss               =      0.313
  train_runtime            = 0:02:22.55
  train_samples_per_second =    168.351
  train_steps_per_second   =       2.63
```

ALLR CC speed remain the same

**Summary metrics account for Logical NeuronCore config = 2**

| Group                                              | Name                                 | Value        |
| -------------------------------------------------- | ------------------------------------ | ------------ |
| overall_stats                                      | **event_count**                      | 2491461      |
| **hardware_flops**                                 | 5.221 **TFLOPS**                     |              |
| **mm_arithmetic_intensity**                        | 128.23 **flops/byte**                |              |
| **model_flops**                                    | 4.291 **TFLOPS**                     |              |
| **neuroncore_cycle_count**                         | 275018784                            |              |
| **peak_flops_bandwidth_ratio**                     | 223.78                               |              |
| **total_time**                                     | 196.44 **ms**                        |              |
| **trace_count**                                    | 10694619                             |              |
| **transpose_flops**                                | 904.077 **GFLOPS**                   |              |
| data_movement                                      | **dma_active_cycles**                | 219593568    |
| **dma_active_time**                                | 156.85 **ms**                        |              |
| **dma_active_time_percent**                        | 79.85 **%**                          |              |
| **dma_packet_time**                                | 1.82 **s**                           |              |
| **dma_queue_count**                                | 118                                  |              |
| **dma_transfer_average_bytes**                     | 299.931 **KiB**                      |              |
| **dma_transfer_count**                             | 95909                                |              |
| **dma_transfer_time**                              | 897.4 **ms**                         |              |
| **dma_transfer_total_bytes**                       | 27.433 **GiB**                       |              |
| **dynamic_dma_packet_percent**                     | 13.86 **%**                          |              |
| **dynamic_dma_size_percent**                       | 9.71 **%**                           |              |
| **hbm_read_bytes**                                 | 19.596 **GiB**                       |              |
| **hbm_write_bytes**                                | 11.759 **GiB**                       |              |
| **input_queue_bytes**                              | 4.58 **MiB**                         |              |
| **inputs_and_weights_size_bytes**                  | 1.224 **GiB**                        |              |
| **mbu_estimated_percent**                          | 41.8 **%**                           |              |
| **mbu_min_read_util_percent**                      | 1.63 **%**                           |              |
| **output_queue_bytes**                             | 0 **B**                              |              |
| **psum_read_bytes**                                | 142.736 **MiB**                      |              |
| **psum_read_sbuf_write_bytes**                     | 78.348 **MiB**                       |              |
| **psum_read_sbuf_write_count**                     | 84075                                |              |
| **psum_write_bytes**                               | 349.476 **MiB**                      |              |
| **sbuf_read_bytes**                                | 12.277 **GiB**                       |              |
| **sbuf_write_bytes**                               | 18.713 **GiB**                       |              |
| **software_dynamic_dma_packet_count**              | 896368                               |              |
| **software_dynamic_dma_size**                      | 2.887 **GiB**                        |              |
| **spill_reload_bytes**                             | 16.893 **GiB**                       |              |
| **spill_save_bytes**                               | 10.447 **GiB**                       |              |
| **static_dma_packet_count**                        | 5572383                              |              |
| **static_dma_size**                                | 26.845 **GiB**                       |              |
| **weight_queue_bytes**                             | 27.429 **GiB**                       |              |
| **weight_size_bytes**                              | 112 **KiB**                          |              |
| tensor_engine                                      | **hfu_estimated_percent**            | 28.97 **%**  |
| **matmul_instruction_count**                       | 568534                               |              |
| **mfu_estimated_percent**                          | 23.81 **%**                          |              |
| **mfu_max_achievable_estimated_percent**           | 56.95 **%**                          |              |
| **tensor_engine_active_time**                      | 77.26 **ms**                         |              |
| **tensor_engine_active_time_percent**              | 39.33 **%**                          |              |
| **tensor_engine_instruction_count**                | 1152205                              |              |
| **tensor_engine_instruction_time**                 | 206.17 **ms**                        |              |
| vector_engine                                      | **vector_engine_active_time**        | 75.78 **ms** |
| **vector_engine_active_time_percent**              | 38.58 **%**                          |              |
| **vector_engine_instruction_count**                | 194981                               |              |
| **vector_engine_instruction_time**                 | 88.5 **ms**                          |              |
| scalar_engine                                      | **activate_instruction_count**       | 127641       |
| **activate_instruction_time**                      | 56.58 **ms**                         |              |
| **scalar_engine_active_time**                      | 51.54 **ms**                         |              |
| **scalar_engine_active_time_percent**              | 26.24 **%**                          |              |
| **scalar_engine_instruction_count**                | 164837                               |              |
| **scalar_engine_instruction_time**                 | 57.39 **ms**                         |              |
| sync_engine                                        | **sync_engine_active_time**          | 2.21 **ms**  |
| **sync_engine_active_time_percent**                | 1.13 **%**                           |              |
| **sync_engine_instruction_count**                  | 90696                                |              |
| **sync_engine_instruction_time**                   | 2.21 **ms**                          |              |
| gpsimd_engine                                      | **gpsimd_engine_active_time**        | 13.31 **ms** |
| **gpsimd_engine_active_time_percent**              | 6.78 **%**                           |              |
| **gpsimd_engine_instruction_count**                | 35779                                |              |
| **gpsimd_engine_instruction_time**                 | 13.31 **ms**                         |              |
| cc_engine                                          | **cc_cores_instruction_active_time** | 3.11 **us**  |
| **cc_cores_instruction_active_time_percent**       | 0.0016 **%**                         |              |
| **cc_cores_instruction_count**                     | 539                                  |              |
| **cc_cores_instruction_time**                      | 15.12 **us**                         |              |
| **cc_op_active_time**                              | 17.3 **ms**                          |              |
| **cc_op_active_time_percent**                      | 8.81 **%**                           |              |
| **cc_op_count**                                    | 5                                    |              |
| **cc_op_time**                                     | 17.3 **ms**                          |              |
| system                                             | **collectives_version**              | 2.28.27 ()   |
| **compiler_version**                               | 2.21.18209.0+043b1bf7                |              |
| **driver_version**                                 | 2.24.0 ()                            |              |
| **instance_type**                                  | trn1.2xlarge                         |              |
| **nc_idx**                                         | 0                                    |              |
| **nd_idx**                                         | 0                                    |              |
| **profiler_version**                               | 2.26.14.0%kaena-tools/2.26@6459a28   |              |
| **runtime_version**                                | 2.28.23 (dd587)                      |              |
| throttling_nc0                                     | **throttle_active_nc0_time_ns**      | 35.28 **ms** |
| **throttle_activity_0_active_time_nc0_percent**    | 11.2 **%**                           |              |
| **throttle_activity_0_avg_util_limit_nc0_percent** | 87.5 **%**                           |              |
| **throttle_activity_1_active_time_nc0_percent**    | 6.74 **%**                           |              |
| **throttle_activity_1_avg_util_limit_nc0_percent** | 87.5 **%**                           |              |
| **throttle_avg_util_limit_nc0_percent**            | 97.55 **%**                          |              |

|      |      |                       |                 |
| ---- | ---- | --------------------- | --------------- |
| 0    | 0    | generic               | 64 **KiB**      |
| 0    | 0    | Tensor                | 140.618 **MiB** |
| 0    | 0    | Scalar                | 19.925 **MiB**  |
| 0    | 0    | GpSimd                | 4.358 **MiB**   |
| 0    | 0    | io                    | 72 **B**        |
| 0    | 0    | Syncill               | 0 **B**         |
| 0    | 0    | weight                | 240.004 **KiB** |
| 0    | 0    | profiler buffers      | 2.443 **GiB**   |
| 0    | 0    | Scalar table          | 492 **KiB**     |
| 0    | 0    | Vector                | 23.182 **MiB**  |
| 0    | 0    | Sync                  | 10.945 **MiB**  |
| 0    | 0    | shared scratchpad     | 6 **GiB**       |
| 0    | 0    | tensor                | 1.226 **GiB**   |
| 0    | 0    | ucode                 | 97.677 **MiB**  |
| 0    | 0    | GpSimd stdio          | 1.063 **KiB**   |
| 0    | 0    | collectives           | 110.08 **MiB**  |
| 0    | 0    | scratchpad            | 0 **B**         |
| 0    | 0    | xt cc                 | 0 **B**         |
| 0    | 0    | dma rings runtime     | 44 **KiB**      |
| 0    | 0    | dma rings Syncill     | 637.865 **MiB** |
| 0    | 0    | dma rings io          | 1.674 **MiB**   |
| 0    | 0    | dma rings collectives | 5.575 **MiB**   |
| 0    | 0    | Total                 | 10.698 **GiB**  |

# Batch 4

**Summary metrics account for Logical NeuronCore config = 2**

| Group                                              | Name                                 | Value         |
| -------------------------------------------------- | ------------------------------------ | ------------- |
| overall_stats                                      | **event_count**                      | 374784        |
| **hardware_flops**                                 | 338.16 **GFLOPS**                    |               |
| **mm_arithmetic_intensity**                        | 46.43 **flops/byte**                 |               |
| **model_flops**                                    | 268.181 **GFLOPS**                   |               |
| **neuroncore_cycle_count**                         | 59250528                             |               |
| **peak_flops_bandwidth_ratio**                     | 223.78                               |               |
| **total_time**                                     | 42.32 **ms**                         |               |
| **trace_count**                                    | 1856932                              |               |
| **transpose_flops**                                | 69.974 **GFLOPS**                    |               |
| data_movement                                      | **dma_active_cycles**                | 52121652      |
| **dma_active_time**                                | 37.23 **ms**                         |               |
| **dma_active_time_percent**                        | 87.97 **%**                          |               |
| **dma_packet_time**                                | 386.15 **ms**                        |               |
| **dma_queue_count**                                | 118                                  |               |
| **dma_transfer_average_bytes**                     | 291.239 **KiB**                      |               |
| **dma_transfer_count**                             | 7946                                 |               |
| **dma_transfer_time**                              | 59.4 **ms**                          |               |
| **dma_transfer_total_bytes**                       | 2.207 **GiB**                        |               |
| **dynamic_dma_packet_percent**                     | 64.95 **%**                          |               |
| **dynamic_dma_size_percent**                       | 49.6 **%**                           |               |
| **hbm_read_bytes**                                 | 3.229 **GiB**                        |               |
| **hbm_write_bytes**                                | 2.151 **GiB**                        |               |
| **input_queue_bytes**                              | 4.399 **MiB**                        |               |
| **inputs_and_weights_size_bytes**                  | 1.224 **GiB**                        |               |
| **mbu_estimated_percent**                          | 33.29 **%**                          |               |
| **mbu_min_read_util_percent**                      | 7.57 **%**                           |               |
| **output_queue_bytes**                             | 0 **B**                              |               |
| **psum_read_bytes**                                | 13.09 **MiB**                        |               |
| **psum_read_sbuf_write_bytes**                     | 8.265 **MiB**                        |               |
| **psum_read_sbuf_write_count**                     | 8533                                 |               |
| **psum_write_bytes**                               | 34.525 **MiB**                       |               |
| **sbuf_read_bytes**                                | 2.142 **GiB**                        |               |
| **sbuf_write_bytes**                               | 2.863 **GiB**                        |               |
| **software_dynamic_dma_packet_count**              | 836768                               |               |
| **software_dynamic_dma_size**                      | 2.768 **GiB**                        |               |
| **spill_reload_bytes**                             | 1.275 **GiB**                        |               |
| **spill_save_bytes**                               | 858.521 **MiB**                      |               |
| **static_dma_packet_count**                        | 451615                               |               |
| **static_dma_size**                                | 2.812 **GiB**                        |               |
| **weight_queue_bytes**                             | 2.203 **GiB**                        |               |
| **weight_size_bytes**                              | 112 **KiB**                          |               |
| tensor_engine                                      | **hfu_estimated_percent**            | 8.71 **%**    |
| **matmul_instruction_count**                       | 39942                                |               |
| **mfu_estimated_percent**                          | 6.91 **%**                           |               |
| **mfu_max_achievable_estimated_percent**           | 20.75 **%**                          |               |
| **tensor_engine_active_time**                      | 5.15 **ms**                          |               |
| **tensor_engine_active_time_percent**              | 12.17 **%**                          |               |
| **tensor_engine_instruction_count**                | 80414                                |               |
| **tensor_engine_instruction_time**                 | 14.13 **ms**                         |               |
| vector_engine                                      | **vector_engine_active_time**        | 16.37 **ms**  |
| **vector_engine_active_time_percent**              | 38.68 **%**                          |               |
| **vector_engine_instruction_count**                | 36910                                |               |
| **vector_engine_instruction_time**                 | 18.16 **ms**                         |               |
| scalar_engine                                      | **activate_instruction_count**       | 35013         |
| **activate_instruction_time**                      | 15.33 **ms**                         |               |
| **scalar_engine_active_time**                      | 14.11 **ms**                         |               |
| **scalar_engine_active_time_percent**              | 33.35 **%**                          |               |
| **scalar_engine_instruction_count**                | 41304                                |               |
| **scalar_engine_instruction_time**                 | 15.47 **ms**                         |               |
| sync_engine                                        | **sync_engine_active_time**          | 236.38 **us** |
| **sync_engine_active_time_percent**                | 0.56 **%**                           |               |
| **sync_engine_instruction_count**                  | 5827                                 |               |
| **sync_engine_instruction_time**                   | 236.38 **us**                        |               |
| gpsimd_engine                                      | **gpsimd_engine_active_time**        | 1.17 **ms**   |
| **gpsimd_engine_active_time_percent**              | 2.75 **%**                           |               |
| **gpsimd_engine_instruction_count**                | 21364                                |               |
| **gpsimd_engine_instruction_time**                 | 1.17 **ms**                          |               |
| cc_engine                                          | **cc_cores_instruction_active_time** | 3.11 **us**   |
| **cc_cores_instruction_active_time_percent**       | 0.0073 **%**                         |               |
| **cc_cores_instruction_count**                     | 539                                  |               |
| **cc_cores_instruction_time**                      | 12.14 **us**                         |               |
| **cc_op_active_time**                              | 13.16 **ms**                         |               |
| **cc_op_active_time_percent**                      | 31.08 **%**                          |               |
| **cc_op_count**                                    | 5                                    |               |
| **cc_op_time**                                     | 13.16 **ms**                         |               |
| system                                             | **collectives_version**              | 2.28.27 ()    |
| **compiler_version**                               | 2.21.18209.0+043b1bf7                |               |
| **driver_version**                                 | 2.24.0 ()                            |               |
| **instance_type**                                  | trn1.2xlarge                         |               |
| **nc_idx**                                         | 0                                    |               |
| **nd_idx**                                         | 0                                    |               |
| **profiler_version**                               | 2.26.14.0%kaena-tools/2.26@6459a28   |               |
| **runtime_version**                                | 2.28.23 (dd587)                      |               |
| throttling_nc0                                     | **throttle_active_nc0_time_ns**      | 1.57 **ms**   |
| **throttle_activity_0_active_time_nc0_percent**    | 1.34 **%**                           |               |
| **throttle_activity_0_avg_util_limit_nc0_percent** | 87.5 **%**                           |               |
| **throttle_activity_1_active_time_nc0_percent**    | 2.38 **%**                           |               |
| **throttle_activity_1_avg_util_limit_nc0_percent** | 87.5 **%**                           |               |
| **throttle_avg_util_limit_nc0_percent**            | 99.33 **%**                          |               |

# Batch 2

**Summary metrics account for Logical NeuronCore config = 2**

| Group                                              | Name                                 | Value         |
| -------------------------------------------------- | ------------------------------------ | ------------- |
| overall_stats                                      | **event_count**                      | 344849        |
| **hardware_flops**                                 | 180.073 **GFLOPS**                   |               |
| **mm_arithmetic_intensity**                        | 24.97 **flops/byte**                 |               |
| **model_flops**                                    | 134.091 **GFLOPS**                   |               |
| **neuroncore_cycle_count**                         | 55708712                             |               |
| **peak_flops_bandwidth_ratio**                     | 223.78                               |               |
| **total_time**                                     | 39.79 **ms**                         |               |
| **trace_count**                                    | 1741569                              |               |
| **transpose_flops**                                | 45.973 **GFLOPS**                    |               |
| data_movement                                      | **dma_active_cycles**                | 49725976      |
| **dma_active_time**                                | 35.52 **ms**                         |               |
| **dma_active_time_percent**                        | 89.26 **%**                          |               |
| **dma_packet_time**                                | 364.84 **ms**                        |               |
| **dma_queue_count**                                | 118                                  |               |
| **dma_transfer_average_bytes**                     | 272.731 **KiB**                      |               |
| **dma_transfer_count**                             | 7043                                 |               |
| **dma_transfer_time**                              | 122.04 **ms**                        |               |
| **dma_transfer_total_bytes**                       | 1.832 **GiB**                        |               |
| **dynamic_dma_packet_percent**                     | 67.67 **%**                          |               |
| **dynamic_dma_size_percent**                       | 53.05 **%**                          |               |
| **hbm_read_bytes**                                 | 3.025 **GiB**                        |               |
| **hbm_write_bytes**                                | 1.976 **GiB**                        |               |
| **input_queue_bytes**                              | 4.387 **MiB**                        |               |
| **inputs_and_weights_size_bytes**                  | 1.224 **GiB**                        |               |
| **mbu_estimated_percent**                          | 32.91 **%**                          |               |
| **mbu_min_read_util_percent**                      | 8.05 **%**                           |               |
| **output_queue_bytes**                             | 0 **B**                              |               |
| **psum_read_bytes**                                | 9.187 **MiB**                        |               |
| **psum_read_sbuf_write_bytes**                     | 6.135 **MiB**                        |               |
| **psum_read_sbuf_write_count**                     | 6749                                 |               |
| **psum_write_bytes**                               | 24.43 **MiB**                        |               |
| **sbuf_read_bytes**                                | 1.952 **GiB**                        |               |
| **sbuf_write_bytes**                               | 2.655 **GiB**                        |               |
| **software_dynamic_dma_packet_count**              | 836000                               |               |
| **software_dynamic_dma_size**                      | 2.764 **GiB**                        |               |
| **spill_reload_bytes**                             | 1.075 **GiB**                        |               |
| **spill_save_bytes**                               | 679.807 **MiB**                      |               |
| **static_dma_packet_count**                        | 399351                               |               |
| **static_dma_size**                                | 2.446 **GiB**                        |               |
| **weight_queue_bytes**                             | 1.828 **GiB**                        |               |
| **weight_size_bytes**                              | 112 **KiB**                          |               |
| tensor_engine                                      | **hfu_estimated_percent**            | 4.93 **%**    |
| **matmul_instruction_count**                       | 28538                                |               |
| **mfu_estimated_percent**                          | 3.67 **%**                           |               |
| **mfu_max_achievable_estimated_percent**           | 11.16 **%**                          |               |
| **tensor_engine_active_time**                      | 2.89 **ms**                          |               |
| **tensor_engine_active_time_percent**              | 7.26 **%**                           |               |
| **tensor_engine_instruction_count**                | 57247                                |               |
| **tensor_engine_instruction_time**                 | 8.99 **ms**                          |               |
| vector_engine                                      | **vector_engine_active_time**        | 14.46 **ms**  |
| **vector_engine_active_time_percent**              | 36.34 **%**                          |               |
| **vector_engine_instruction_count**                | 33230                                |               |
| **vector_engine_instruction_time**                 | 15.9 **ms**                          |               |
| scalar_engine                                      | **activate_instruction_count**       | 32772         |
| **activate_instruction_time**                      | 14.11 **ms**                         |               |
| **scalar_engine_active_time**                      | 12.97 **ms**                         |               |
| **scalar_engine_active_time_percent**              | 32.59 **%**                          |               |
| **scalar_engine_instruction_count**                | 38228                                |               |
| **scalar_engine_instruction_time**                 | 14.24 **ms**                         |               |
| sync_engine                                        | **sync_engine_active_time**          | 218.97 **us** |
| **sync_engine_active_time_percent**                | 0.55 **%**                           |               |
| **sync_engine_instruction_count**                  | 5099                                 |               |
| **sync_engine_instruction_time**                   | 218.97 **us**                        |               |
| gpsimd_engine                                      | **gpsimd_engine_active_time**        | 0.77 **ms**   |
| **gpsimd_engine_active_time_percent**              | 1.92 **%**                           |               |
| **gpsimd_engine_instruction_count**                | 20522                                |               |
| **gpsimd_engine_instruction_time**                 | 0.77 **ms**                          |               |
| cc_engine                                          | **cc_cores_instruction_active_time** | 3.11 **us**   |
| **cc_cores_instruction_active_time_percent**       | 0.0078 **%**                         |               |
| **cc_cores_instruction_count**                     | 539                                  |               |
| **cc_cores_instruction_time**                      | 14.44 **us**                         |               |
| **cc_op_active_time**                              | 13.56 **ms**                         |               |
| **cc_op_active_time_percent**                      | 34.09 **%**                          |               |
| **cc_op_count**                                    | 5                                    |               |
| **cc_op_time**                                     | 13.56 **ms**                         |               |
| system                                             | **collectives_version**              | 2.28.27 ()    |
| **compiler_version**                               | 2.21.18209.0+043b1bf7                |               |
| **driver_version**                                 | 2.24.0 ()                            |               |
| **instance_type**                                  | trn1.2xlarge                         |               |
| **nc_idx**                                         | 0                                    |               |
| **nd_idx**                                         | 0                                    |               |
| **profiler_version**                               | 2.26.14.0%kaena-tools/2.26@6459a28   |               |
| **runtime_version**                                | 2.28.23 (dd587)                      |               |
| throttling_nc0                                     | **throttle_active_nc0_time_ns**      | 341.72 **us** |
| **throttle_activity_0_active_time_nc0_percent**    | 0.2 **%**                            |               |
| **throttle_activity_0_avg_util_limit_nc0_percent** | 87.5 **%**                           |               |
| **throttle_activity_1_active_time_nc0_percent**    | 0.66 **%**                           |               |
| **throttle_activity_1_avg_util_limit_nc0_percent** | 87.5 **%**                           |               |
| **throttle_avg_util_limit_nc0_percent**            | 99.74 **%**                          |               |
