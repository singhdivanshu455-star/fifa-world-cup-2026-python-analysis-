"""
===========================================================
 FIFA World Cup 2026 Final Analysis (Practice Project)
 Spain vs Argentina
-----------------------------------------------------------
Built to practice:
✔ Python
✔ Object-Oriented Programming (OOP)
✔ Pandas
✔ Matplotlib

Author: Divanshu Singh
===========================================================
"""

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Theme Colors
# ----------------------------
SPAIN_COLOR = "#C60B1E"
ARGENTINA_COLOR = "#75AADB"


class MatchAnalyzer:

    def __init__(self, team_a, team_b, stats):
        self.team_a = team_a
        self.team_b = team_b

        self.df = pd.DataFrame(
            stats,
            index=[team_a, team_b]
        )

    # ---------------------------------
    # Display Match Statistics
    # ---------------------------------
    def summary(self):

        print("\n" + "=" * 55)
        print(f"      {self.team_a} vs {self.team_b}")
        print("=" * 55)

        print(self.df.to_string())

    # ---------------------------------
    # Winner Prediction using xG
    # ---------------------------------
    def winner_prediction(self):

        winner = self.df["xG"].idxmax()

        print("\nWinner Prediction (Based on xG):")
        print(f"🏆 {winner}")

    # ---------------------------------
    # Visualization
    # ---------------------------------
    def plot_comparison(self):

        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        # Total Shots
        self.df["Shots"].plot(
            kind="bar",
            color=[SPAIN_COLOR, ARGENTINA_COLOR],
            ax=axes[0]
        )

        axes[0].set_title("Total Shots")
        axes[0].set_ylabel("Shots")
        axes[0].tick_params(axis="x", rotation=0)

        # xG
        self.df["xG"].plot(
            kind="bar",
            color=[SPAIN_COLOR, ARGENTINA_COLOR],
            ax=axes[1]
        )

        axes[1].set_title("Expected Goals (xG)")
        axes[1].set_ylabel("xG")
        axes[1].tick_params(axis="x", rotation=0)

        plt.suptitle(
            "FIFA World Cup 2026 Final Analysis",
            fontsize=14,
            fontweight="bold"
        )

        plt.tight_layout()

        plt.savefig("match_comparison.png", dpi=300)

        plt.show()

        print("\nChart saved successfully as:")
        print("match_comparison.png")

    # ---------------------------------
    # Timeline
    # ---------------------------------
    def timeline(self):

        timeline = [

            {
                "Minute": "0'",
                "Event": "Kickoff"
            },

            {
                "Minute": "90'",
                "Event": "0-0 after regulation time"
            },

            {
                "Minute": "90+'",
                "Event": "Argentina reduced to 10 players"
            },

            {
                "Minute": "106'",
                "Event": "Spain score the winning goal"
            },

            {
                "Minute": "120'",
                "Event": "Spain become World Champions"
            }

        ]

        timeline_df = pd.DataFrame(timeline)

        print("\nMatch Timeline\n")

        print(timeline_df.to_string(index=False))

    # ---------------------------------
    # Quick Insights
    # ---------------------------------
    def insights(self):

        print("\nKey Insights")
        print("-" * 40)

        if self.df.loc[self.team_a, "Shots"] > self.df.loc[self.team_b, "Shots"]:
            print(f"• {self.team_a} attempted more shots.")

        if self.df.loc[self.team_a, "xG"] > self.df.loc[self.team_b, "xG"]:
            print(f"• {self.team_a} generated higher expected goals (xG).")

        print("• Data visualization makes match analysis easier.")
        print("• This project demonstrates basic sports analytics using Python.")


# =========================================================
# Main Program
# =========================================================

if __name__ == "__main__":

    # -----------------------------------------------------
    # Sample Match Statistics (Practice Dataset)
    # -----------------------------------------------------

    match_stats = {

        "Shots": [20, 2],

        "xG": [1.94, 0.20]

    }

    analyzer = MatchAnalyzer(
        "Spain",
        "Argentina",
        match_stats
    )

    analyzer.summary()

    analyzer.winner_prediction()

    analyzer.timeline()

    analyzer.insights()

    analyzer.plot_comparison()