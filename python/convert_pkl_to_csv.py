#!/usr/bin/env python3
import sys
import json
import pickle
import csv
import io

def main():
    try:
        # Read JSON input (session data) from stdin
        input_data = sys.stdin.read()
        session_data = json.loads(input_data)

        # Generate pickle bytes from the session data
        pickle_bytes = pickle.dumps(session_data)

        # "Load" the pickle to simulate reading a PKL file
        data = pickle.loads(pickle_bytes)
        
        # Ensure that the session data contains recognized texts
        if 'recognizedTexts' not in data or not isinstance(data['recognizedTexts'], list):
            raise ValueError("Session data must contain a 'recognizedTexts' list.")

        # Prepare CSV output in memory
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Write header row
        writer.writerow(["timestamp", "text", "session_id", "total_recognitions"])
        
        # Write each recognition record to the CSV
        for entry in data['recognizedTexts']:
            writer.writerow([
                entry.get("timestamp", ""), 
                entry.get("text", ""),
                data.get("sessionId", ""),
                data.get("totalRecognitions", "")
            ])
        
        # Output the CSV content
        sys.stdout.write(output.getvalue())
        
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)

if __name__ == '__main__':
    main()
