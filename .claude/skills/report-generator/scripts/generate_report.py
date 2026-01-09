import argparse

def generate_report(title, summary, findings, sources):
    """
    Generates a formatted report.

    Args:
        title (str): The title of the report.
        summary (str): The summary of the report.
        findings (list): A list of key findings.
        sources (list): A list of sources.

    Returns:
        str: The formatted report.
    """
    report = f"# {title}\n\n"
    report += f"## Summary\n\n{summary}\n\n"
    report += "## Key Findings\n\n"
    for finding in findings:
        report += f"- {finding}\n"
    report += "\n"
    report += "## Sources\n\n"
    for source in sources:
        report += f"- {source}\n"
    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a report.")
    parser.add_argument("--title", type=str, default="The Impact of AI on Software Development", help="The title of the report.")
    parser.add_argument("--summary", type=str, default="This report summarizes the key findings from articles...", help="The summary of the report.")
    
    args = parser.parse_args()

    # Hardcoded data for demonstration
    findings = [
        "AI is increasingly used for code completion and suggestion.",
        "Machine learning models are being employed for test case generation.",
        "AI-powered tools can help in identifying and fixing bugs more efficiently."
    ]
    sources = [
        "'The Role of AI in Modern Software Engineering' - aihub.com/article1",
        "'Machine Learning in Test Automation' - devworld.com/ml-testing"
    ]

    report = generate_report(args.title, args.summary, findings, sources)
    print(report)