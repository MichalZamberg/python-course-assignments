from datetime import datetime, timedelta
from collections import defaultdict

def parse_timelog(file_path):
    sessions = []
    current_session = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                if current_session:
                    sessions.append(current_session)
                    current_session = []
            else:
                time_str, label = stripped.split(' ', 1)
                time_obj = datetime.strptime(time_str, '%H:%M')
                current_session.append((time_obj, label))

    if current_session:
        sessions.append(current_session)
    
    return sessions

def format_sessions(sessions):
    formatted_lines = []
    activity_durations = defaultdict(int)

    for session in sessions:
        for i in range(len(session) - 1):
            start, label = session[i]
            end, _ = session[i + 1]
            duration = int((end - start).total_seconds() // 60)
            activity_durations[label] += duration
            formatted_lines.append(f"{start.strftime('%H:%M')}-{end.strftime('%H:%M')} {label}")
        formatted_lines.append("")  # Separate sessions

    return formatted_lines, activity_durations

def format_summary(activity_durations):
    """Generate summary report lines with total minutes and percentages."""
    total_minutes = sum(activity_durations.values())
    summary_lines = []

    for activity in sorted(activity_durations):
        minutes = activity_durations[activity]
        percentage = (minutes / total_minutes) * 100
        summary_lines.append(f"{activity:<25} {minutes:>3} minutes  {percentage:>3.0f}%")

    return summary_lines
