import os

DATA_PATH= "/merklebot/job_data"

def create_text_file(path, content):
  with open(path, 'w') as f:
    f.write(content)


"""
Generate file tree
-path
  - f0.txt
  - dir1
    - f1-0.txt
    - f1-1.txt
    - dir2
      - f2-0.txt
      - dir3
        - f3-0.txt
  - dir4
    - f4-0.txt
"""
def generate_tree(path):
  create_text_file(f"{path}/f0.txt", "Content of f0.txt")
  
  os.makedirs(f"{path}/dir1/dir2/dir3", exist_ok=True)
  create_text_file(f"{path}/dir1/f1-0.txt", "Content of f1-0.txt")
  create_text_file(f"{path}/dir1/f1-1.txt", "Content of f1-1.txt")
  create_text_file(f"{path}/dir1/dir2/f2-0.txt", "Content of f2-0.txt")
  create_text_file(f"{path}/dir1/dir3/f3-0.txt", "Content of f3-0.txt")
  
  os.makedirs(f"{path}/dir4", exist_ok=True)
  create_text_file(f"{path}/ditr4/f4-0.txt", "Content of f4-0.txt")

if __name__=='__main__':
  generate_tree(DATA_PATH)
