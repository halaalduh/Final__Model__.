# Model files — v1-2026-11-21

The local archive includes the v1 checkpoints and `pipeline.json`. The seven detector checkpoints use project-relative paths in their saved training metadata. The edit removed machine-specific path prefixes. The learned parameters are byte-for-byte identical, and this package records the revised files in `SHA256SUMS`. The original Drive archive has its own checkpoint hashes.

The [technical report](../../../docs/REPORT.md#project-materials-and-provenance) documents the project inputs and contributions. Its [generative AI section](../../../docs/REPORT.md#13-use-of-generative-ai) describes how AI was used.

| file | model | MB |
|---|---|---|
| `classifier_1.pt` | ResNet-18, class-balanced sampling, seed 42 | 44.8 |
| `classifier_2.pt` | ResNet-18, class-balanced sampling, seed 43 | 44.8 |
| `classifier_3.pt` | ResNet-18, class-balanced sampling, seed 44 | 44.8 |
| `classifier_4.pt` | ResNet-18, class-weighted loss, seed 42 | 44.8 |
| `classifier_5.pt` | ResNet-18, class-weighted loss, seed 43 | 44.8 |
| `classifier_6.pt` | ResNet-18, class-weighted loss, seed 44 | 44.8 |
| `detector_1.pt` | YOLO26-s detector, seed 42 | 20.3 |
| `detector_2.pt` | YOLO26-s detector, seed 43 | 20.3 |
| `detector_3.pt` | YOLO26-s detector, seed 44 | 20.3 |
| `detector_4.pt` | YOLOv8n detector, seed 42 | 6.2 |
| `detector_5.pt` | YOLOv8n detector, seed 43 | 6.2 |
| `detector_6.pt` | YOLOv8n detector, seed 44 | 6.2 |
| `detector_7.pt` | YOLO26-m detector, seed 42 | 44.0 |

Check the local checkpoints against `SHA256SUMS`: `sha256sum -c SHA256SUMS` on Linux or `shasum -a 256 -c SHA256SUMS` on macOS, run from this folder, or `certutil -hashfile <file> SHA256` (Windows).

`pipeline.json` lists these files and holds every threshold; the code reads everything from it.
