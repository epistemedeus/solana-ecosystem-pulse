import unittest

import pulse


class PulseTests(unittest.TestCase):
    def test_performance_metrics_reports_vote_and_non_vote_tps(self):
        metrics = pulse.performance_metrics(
            [
                {"samplePeriodSecs": 10, "numTransactions": 50_000, "numNonVoteTransactions": 8_000, "numSlots": 25},
                {"samplePeriodSecs": 10, "numTransactions": 40_000, "numNonVoteTransactions": 6_000, "numSlots": 20},
            ]
        )
        self.assertEqual(metrics["tps_recent"], 5000)
        self.assertEqual(metrics["non_vote_tps_recent"], 800)
        self.assertEqual(metrics["tps_rolling"], 4500)
        self.assertEqual(metrics["slot_time_ms_recent"], 400)

    def test_validator_metrics_computes_stake_weighted_values(self):
        votes = {
            "current": [
                {"votePubkey": "a", "nodePubkey": "n1", "activatedStake": 40_000_000_000, "commission": 5},
                {"votePubkey": "b", "nodePubkey": "n2", "activatedStake": 35_000_000_000, "commission": 7},
                {"votePubkey": "c", "nodePubkey": "n3", "activatedStake": 25_000_000_000, "commission": 10},
            ],
            "delinquent": [
                {"votePubkey": "d", "nodePubkey": "n4", "activatedStake": 1_000_000_000, "commission": 10}
            ],
        }
        metrics = pulse.validator_metrics(votes)
        self.assertEqual(metrics["active_count"], 3)
        self.assertEqual(metrics["delinquent_count"], 1)
        self.assertEqual(metrics["nakamoto_33_coefficient"], 1)
        self.assertAlmostEqual(metrics["delinquent_stake_pct"], 0.9901, places=4)
        self.assertEqual(metrics["top_validators"][0]["vote_account"], "a")

    def test_robust_z_waits_for_baseline(self):
        self.assertEqual(pulse.robust_z(10, [1, 2, 3]), (None, None))

    def test_robust_z_detects_outlier(self):
        score, median = pulse.robust_z(100, [8, 9, 9, 10, 10, 11, 11, 12])
        self.assertEqual(median, 10)
        self.assertIsNotNone(score)
        self.assertGreater(score, 3.5)

    def test_markdown_never_hides_missing_values(self):
        snapshot = {
            "schema_version": pulse.SCHEMA_VERSION,
            "generated_at": "2026-08-05T00:00:00Z",
            "status": "watch",
            "network": {},
            "validators": {"top_validators": []},
            "economy": {},
            "anomalies": [],
            "ecosystem": {"news": [], "agave_releases": []},
            "sources": [],
            "coverage": {"included": [], "not_included": ["missing metric"]},
        }
        report = pulse.markdown_report(snapshot)
        self.assertIn("n/a", report)
        self.assertIn("missing metric", report)


if __name__ == "__main__":
    unittest.main()
