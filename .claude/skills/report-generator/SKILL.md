---
name: report-generator
description: "Generates well-structured reports from provided information, including a dedicated 'Sources' section for listing references. This skill is ideal for creating summaries, analyses, or overviews that require clear attribution of sources."
---

# Report Generator

## Overview

This skill generates reports from text-based information. It ensures that the output is well-structured and includes a "Sources" section, which is a clean list of references, as per the user's preferred style.

## Workflow

The report generation process follows these steps:

1.  **Information Gathering:** The user provides the information to be included in the report. This can be in the form of text, articles, or data.
2.  **Report Generation:** The skill processes the input and generates a report. The report will have a clear structure, including a title, summary, and the main body.
3.  **Source Listing:** A "Sources" section is appended to the report, listing all the references provided by the user.

## Example Usage

**User Request:**
"Please create a report summarizing the provided articles about the impact of AI on software development. Here are the sources:
- 'The Role of AI in Modern Software Engineering' - aihub.com/article1
- 'Machine Learning in Test Automation' - devworld.com/ml-testing"

**Generated Report:**

```
# The Impact of AI on Software Development

## Summary

This report summarizes the key findings from articles discussing the influence of Artificial Intelligence on modern software development practices.

## Key Findings

... (content based on the provided articles) ...

## Sources

- 'The Role of AI in Modern Software Engineering' - aihub.com/article1
- 'Machine Learning in Test Automation' - devworld.com/ml-testing
```

## Resources

This skill includes the following resources:

### scripts/
- `generate_report.py`: A Python script that takes text and a list of sources as input and generates a formatted report.