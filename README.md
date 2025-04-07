# LeanFrame 🎞️🧠  
*A lightweight tool to extract video frames, remove similar frames, and reconstruct the video — perfect for reducing ML model load.*

## 🧩 What It Does

This tool helps preprocess videos by reducing redundant frames before sending them into machine learning pipelines. It works in **three simple steps**:

1. **Extract Frames from Video**  
   Breaks the input video into individual image frames.

2. **Remove Similar Frames**  
   Compares frames and removes visually similar or near-identical ones to reduce redundancy.

3. **Rebuild Video from Cleaned Frames**  
   Combines the remaining frames back into a video — now leaner and faster for ML models to process.

---

## 🎯 Why Use It?

Video models are heavy on compute. This tool:
- **Speeds up inference**
- **Reduces storage requirements**
- **Improves training efficiency** by eliminating duplicate data

---

## 📂 Files Overview

- `extract_frames.py` – Extracts all frames from a given video.
- `remove_similar_frames.py` – Compares and removes similar frames.
- `rebuild_video.py` – Reconstructs a video from the cleaned set of frames.
