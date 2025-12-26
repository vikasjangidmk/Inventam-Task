# Training Diagnosis — Sample

## Symptom: NaN gradients after epoch 2
### Evidence
- Loss became NaN at step 342, GPU utilization spiked.
### Root cause
- Learning rate set too high (5e-4); no gradient clipping; warmup not configured.
### Fix applied
- Learning rate reduced to 3e-5, gradient clipping norm=1.0, warmup_steps=1000.
