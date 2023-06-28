# Step 5: Generate levels 
levels = [] 
for i in range(1, len(letters_by_tally)+1):
  levels.append(letters_by_tally[:i])

import json
out = open('greek-levels.json','w')
out.write(json.dumps(levels))

