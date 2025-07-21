import sys
import json
import pickle
import base64

def main():
    try:
        # Read input from stdin
        input_data = sys.stdin.read()
        session_data = json.loads(input_data)
        
        # Serialize using pickle
        pickle_bytes = pickle.dumps(session_data)
        
        # Encode in base64
        encoded = base64.b64encode(pickle_bytes).decode('utf-8')
        print(encoded)
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)

if __name__ == '__main__':
    main()
