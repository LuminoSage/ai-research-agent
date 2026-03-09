from crewai import Task


def research_task(agent, query: str):
    return Task(
        description=(
            f"Research the following topic thoroughly using web search:\n\n"
            f"TOPIC: {query}\n\n"
            f"Your job:\n"
            f"1. Search for the most recent and relevant information.\n"
            f"2. Gather facts, statistics, key players, and current developments.\n"
            f"3. Collect at least 5 distinct pieces of information from different angles.\n"
            f"4. Note any controversies, challenges, or open questions around the topic.\n"
            f"5. Return ALL raw findings in detail — do not summarize yet."
        ),
        expected_output=(
            "A detailed collection of raw research findings including facts, "
            "statistics, quotes, sources, and key points about the topic. "
            "Minimum 400 words of raw research data."
        ),
        agent=agent,
    )


def analysis_task(agent, query: str):
    return Task(
        description=(
            f"Analyze the raw research findings about: {query}\n\n"
            f"Your job:\n"
            f"1. Identify the 4-6 most important themes or insights.\n"
            f"2. Find patterns, connections, and contradictions in the data.\n"
            f"3. Highlight what's most significant and why.\n"
            f"4. Note any gaps or areas needing more investigation.\n"
            f"5. Organize findings into a logical structure for the writer."
        ),
        expected_output=(
            "A structured analytical breakdown with clearly labeled sections: "
            "Key Themes, Important Insights, Patterns & Connections, Notable Gaps, "
            "and Recommended Focus Areas for the final report."
        ),
        agent=agent,
    )


def writer_task(agent, query: str):
    return Task(
        description=(
            f"Write a professional research report on: {query}\n\n"
            f"Using the analysis provided, create a well-structured report with:\n"
            f"1. An executive summary (2-3 sentences).\n"
            f"2. A detailed body with clear headings and subheadings.\n"
            f"3. Key takeaways in bullet points.\n"
            f"4. A conclusion with forward-looking insights.\n\n"
            f"The report should be clear, professional, and ready to present. "
            f"Use markdown formatting."
        ),
        expected_output=(
            "A complete, polished research report in markdown format with: "
            "Executive Summary, multiple detailed sections with headings, "
            "Key Takeaways, and Conclusion. Minimum 600 words."
        ),
        agent=agent,
    )