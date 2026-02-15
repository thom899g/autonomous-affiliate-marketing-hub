import logging
from typing import Dict, List
from datetime import datetime

class PerformanceTracker:
    def __init__(self):
        self.performance_data = []
        
    def _log_error(self, message: str) -> None:
        """Log errors with timestamp."""
        logging.error(f"ERROR: {message}")

    def track_performance(self, partner_name: str, metrics: Dict[str, float]) -> None:
        """Track performance metrics for a partner."""
        try:
            self.performance_data.append({
                'partner': partner_name,
                'timestamp': datetime.now().isoformat(),
                **metrics
            })
            logging.info(f"Tracked performance for {partner_name}")
        except Exception as e:
            self._log_error(f"