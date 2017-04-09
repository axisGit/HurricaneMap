import os
[os.rename(f, f.replace('kmz', 'zip')) for f in os.listdir('.') if not f.startswith('.')]