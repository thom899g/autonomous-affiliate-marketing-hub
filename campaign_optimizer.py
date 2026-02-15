import logging
from typing import Dict, List
from content_generator import ContentGenerator

class CampaignOptimizer:
    def __init__(self):
        self.contents = []
        
    def _log_error(self, message: str) -> None:
        """Log errors with timestamp."""
        logging.error(f"ERROR: {message}")

    def add_content(self, partner_name: str, content: str) -> None:
        """Add new content to optimize."""
        try:
            self.contents.append({
                'partner': partner_name,
                'content': content
            })
            logging.info(f"Added content for {partner_name}")
        except Exception as e:
            self._log_error(f"Error adding content: {e}")

    def optimize(self) -> Dict[str, float]:
        """Optimize all stored contents."""
        try:
            results = {}
            for item in self.contents:
                # Mock optimization logic (replace with actual algorithm)
                score = 0.95
                improvement = 15.0
                results[item['partner']] = {
                    'score': score,
                    'improvement': improvement
                }
                logging.info(f"Optimized content for {item['partner']} with score {score}")
            return results
        except Exception as e:
            self._log_error(f"Optimization failed: {e}")
            raise

# Example usage
if __name__ == "__main__":
    optimizer = CampaignOptimizer()
    
    # Generate content first
    generator = ContentGenerator()
    collector = DataCollector()
    collector.collect_from_csv('partners.csv')
    
    for partner in collector.data:
        content = generator.generate_content({
            'partner_name': partner[1],
            'affiliate_link': partner[2]
        })
        optimizer.add_content(partner[1], content)
    
    results = optimizer.optimize()
    print("Optimization Results:", results)