# Creator Platform Ingest Evaluation

- baseline_capture: /Users/cecilialiu/Documents/Codex/ai-content/.cache/content-pipeline/creator-captures/dy-api-patch-test-v2/capture.json
- candidate_capture: /Users/cecilialiu/Documents/Codex/ai-content/.cache/content-pipeline/creator-captures/dy-home-overview-v1/capture.json
- score: 4/4

## Checks
- [PASS] Douyin near-7-day play trend is captured: old_status=missing old_points=0; new_status=series_available new_points=7
- [PASS] Douyin account snapshot includes the required works aggregate fields: present=['总播放', '总收藏', '总点赞', '播放量中位数', '条均2s跳出率', '条均5s完播率', '条均播放时长', '累计视频数']; missing=[]
- [PASS] Douyin works coverage remains full after the homepage patch: old={'captured': True, 'total_count': 21, 'visible_count': 21, 'partial': False, 'enriched_visible_rows': 21}; new={'captured': True, 'total_count': 21, 'visible_count': 21, 'partial': False, 'enriched_visible_rows': 21}
- [PASS] Xiaohongshu note-detail enrichment did not regress while adding Douyin homepage support: old={'captured': True, 'visible_count': 10, 'selected_period': '近7日', 'data_window': None, 'enriched_visible_rows': 10}; new={'captured': True, 'visible_count': 10, 'selected_period': '近7日', 'data_window': None, 'enriched_visible_rows': 10}

## Remaining Gaps
- Xiaohongshu note list is still partial because the creator list is virtualized.
- Xiaohongshu content-analysis still misses 1 visible row in this capture.
- The skill captures data but does not yet auto-write back into ai-content docs.
