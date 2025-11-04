"""
trust_matrix.py

This module defines the TrustMatrix class, which models emotional influence between agents in the S.A.S. framework. Each agent has a directional trust relationship with others, represented as a weighted matrix. Trust values range from 0.0 (no influence) to 1.0 (full influence).

Key Features:
- Set and retrieve trust levels between agents
- Apply trust-weighted emotional influence vectors
- Simulate emotional contagion, resistance, and alliance dynamics

This module enables multi-agent emotional modeling, allowing S.A.S. systems to simulate complex interactions, influence propagation, and trust-based decision logic.
"""

class TrustMatrix:
    def __init__(self, agent_count):
        # Initialize a square matrix of trust values between agents
        self.matrix = [[0.0 for _ in range(agent_count)] for _ in range(agent_count)]

    def set_trust(self, from_agent, to_agent, value):
        """Set trust level from one agent to another (0.0 to 1.0)."""
        self.matrix[from_agent][to_agent] = max(0.0, min(1.0, value))

    def get_trust(self, from_agent, to_agent):
        """Retrieve trust level from one agent to another."""
        return self.matrix[from_agent][to_agent]

    def influence_vector(self, source_vector, from_agent):
        """Apply trust-weighted influence from one agent to others."""
        influenced = []
        for to_agent in range(len(self.matrix)):
            trust = self.get_trust(from_agent, to_agent)
            influenced.append([v * trust for v in source_vector])
        return influenced


# 🔍 Example Usage
if __name__ == "__main__":
    tm = TrustMatrix(agent_count=3)
    tm.set_trust(0, 1, 0.8)
    tm.set_trust(0, 2, 0.3)

    source_vector = [0.6, 0.4, 0.2]  # tone, trust, volatility
    influences = tm.influence_vector(source_vector, from_agent=0)

    for i, vec in enumerate(influences):
        print(f"Agent 0's influence on Agent {i}: {vec}")
