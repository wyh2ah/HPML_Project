# Len 32, Batch 32, --model-type=transformer --distribution-strategy=llm-training --optlevel=3



Acc 94.6%

```
***** train metrics *****
  epoch                    =        3.0
  eval_loss                =     0.1883
  eval_runtime             = 0:00:02.45
  eval_samples_per_second  =   1631.095
  eval_steps_per_second    =    101.943
  total_flos               =   367575GF
  train_loss               =     0.2818
  train_runtime            = 0:02:06.30
  train_samples_per_second =    190.019
  train_steps_per_second   =      5.938
```



# --model-type=transformer --optlevel=3

ACC 94.65%

```
***** train metrics *****
  epoch                    =        3.0
  eval_loss                =     0.1875
  eval_runtime             = 0:00:02.45
  eval_samples_per_second  =   1630.426
  eval_steps_per_second    =    101.902
  total_flos               =   367575GF
  train_loss               =     0.2819
  train_runtime            = 0:02:05.72
  train_samples_per_second =    187.911
  train_steps_per_second   =      5.872
```



# --model-type=transformer --optlevel=2

```
Accuracy: 0.9465 (94.65%)
```

```
***** train metrics *****
  epoch                    =        3.0
  eval_loss                =     0.1875
  eval_runtime             = 0:00:02.40
  eval_samples_per_second  =   1664.701
  eval_steps_per_second    =    104.044
  total_flos               =   367575GF
  train_loss               =     0.2819
  train_runtime            = 0:02:07.39
  train_samples_per_second =    188.396
  train_steps_per_second   =      5.887
```

# --model-type=transformer --optlevel=1

acc 94.3%

```
***** train metrics *****
  epoch                    =        3.0
  eval_loss                =     0.1854
  eval_runtime             = 0:00:02.52
  eval_samples_per_second  =   1585.061
  eval_steps_per_second    =     99.066
  total_flos               =   367575GF
  train_loss               =     0.2832
  train_runtime            = 0:02:12.10
  train_samples_per_second =     181.67
  train_steps_per_second   =      5.677
```