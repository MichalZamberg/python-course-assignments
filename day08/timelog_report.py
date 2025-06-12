import sys
from timelog_parser import parse_timelog, format_sessions, format_summary

def generate_report(input_file, output_file):
    sessions = parse_timelog(input_file)
    session_lines, activity_durations = format_sessions(sessions)
    summary_lines = format_summary(activity_durations)

    with open(output_file, 'w', encoding='utf-8') as out:
        for line in session_lines:
            out.write(line + '\n')
        out.write('\n')
        for line in summary_lines:
            out.write(line + '\n')

    print(f"Report written to '{output_file}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python timelog_report.py <input_log> <output_report>")
    else:
        generate_report(sys.argv[1], sys.argv[2])
