# Source audit

Audit date: **2026-08-05**

## Local ACE attachments

- Scanned **78 PDF files** recursively under the ACE folder.
- Extracted the first three pages of each readable PDF for title, abstract, venue, and arXiv-ID matching.
- Collapsed repeated storage variants by arXiv ID/title (for example, numeric filenames such as `2503.pdf` and descriptive filenames for the same paper).
- Kept papers whose main contribution is dexterous-hand RL, cross-embodiment/unified action representations, or tactile/force sensing for dexterous manipulation.
- Kept adjacent foundation-model papers only when they provide an actionable latent, VLA, or tactile component; generic video generation, search, or humanoid-only papers are not forced into the list.

## Programmatic web sources

The arXiv discovery pass used [`../scripts/crawl_arxiv.py`](../scripts/crawl_arxiv.py) with these queries:

- `"dexterous hand"`
- `tactile dexterous manipulation`
- `cross-embodiment dexterous`

The crawl returned **408 unique arXiv records** after merging query overlap. The README keeps the records that match the three target themes and removes near-duplicates or hardware-only papers.

Conference verification pages:

- [CVPR 2026 Open Access](https://openaccess.thecvf.com/CVPR2026?day=all): official paper pages and abstracts are live.
- [ICML 2026 Papers](https://icml.cc/virtual/2026/papers.html): 193 scheduled program records were visible; no directly dexterous-hand-specific paper was found, so adjacent entries are labeled.
- [ECCV 2026 Papers](https://eccv.ecva.net/virtual/2026/papers.html): the official index returned 0 papers on the audit date; see [meeting dates](https://eccv.ecva.net/Conferences/2026/Dates).

## Link checks

All 94 arXiv links currently present in `README.md` returned HTTP 200 during the final link check. Conference links are intentionally kept as official pages even when a separate arXiv preprint could not be located.
