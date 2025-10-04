# Jasonite

A tiny, fast, and safe JSON-backed document store.

- In-memory cache + atomic file writes
- Thread-safe
- Mongo-like queries ($eq, $ne, $gt, $gte, $lt, $lte, $in, $nin, $exists) with dotted paths
- CRUD + save/upsert + findAndModify / findAndRemove
- Sorting and Python-like slicing ("i:j:k")

## Install

```bash
pip install .
