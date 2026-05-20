import json
import os
import base64
import urllib.parse

def main():
    har_path = 'g:/infybytes/preview.themeforest.net.har'
    output_dir = 'g:/infybytes'
    
    print("Reading HAR file...")
    with open(har_path, 'r', encoding='utf-8', errors='ignore') as f:
        har = json.load(f)
        
    entries = har['log']['entries']
    print(f"Total entries: {len(entries)}")
    
    extracted_count = 0
    skipped_count = 0
    
    for entry in entries:
        url = entry['request']['url']
        parsed_url = urllib.parse.urlparse(url)
        
        # We only care about resources on the Lumo demo site
        if parsed_url.netloc != 'flex.creativemox.com':
            continue
            
        path = parsed_url.path
        # Remove the leading '/lumo' prefix if present
        if path.startswith('/lumo'):
            path = path[5:]
        if path.startswith('/'):
            path = path[1:]
            
        # Map empty path to index.html
        if not path or path == '/':
            local_filename = 'index.html'
        else:
            local_filename = path
            
        # Clean query parameters or trailing slashes
        if local_filename.endswith('/'):
            local_filename += 'index.html'
            
        full_path = os.path.join(output_dir, local_filename)
        
        # Ensure parent directory exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        response = entry['response']
        content = response['content']
        body = content.get('text')
        
        if body is None:
            skipped_count += 1
            continue
            
        encoding = content.get('encoding')
        
        try:
            if encoding == 'base64':
                file_data = base64.b64decode(body)
                with open(full_path, 'wb') as out_f:
                    out_f.write(file_data)
            else:
                # Text content
                with open(full_path, 'w', encoding='utf-8', errors='ignore') as out_f:
                    out_f.write(body)
            extracted_count += 1
        except Exception as e:
            print(f"Error saving {url}: {e}")
            skipped_count += 1
            
    print(f"Extraction complete! Extracted {extracted_count} files, skipped {skipped_count} files.")

if __name__ == '__main__':
    main()
