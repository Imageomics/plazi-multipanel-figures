import sys
import os
import openai
import json
import csv
import itertools

#openai.organization = "org-YrwcpxNOQNBZq9oSVoxmp8Kx"
openai.api_key = os.getenv("OPENAI_API_KEY")
infile = sys.argv[1]
outfolder = sys.argv[2]
start = int(sys.argv[3])
end = int(sys.argv[4])

def parse_line(line):
    try:
        desc = line[3]
        md5 = line[5]
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": "You will be provided with a multi-panel figure caption from a scientific paper, and your task is to parse descriptions for each subpanel from the caption. Output the results in JSON format containing an array of subpanels, with properties 'id' and 'description'. In the 'description' output for each subpanel, include the description of what is depicted in that subpanel, possibly duplicating any information from the overall caption text that applies to that subpanel (which may apply across multiple sub-panels), and including the scientific name of any depicted species or any depicted view of an anatomical structure."
            },
            {
            "role": "user",
            "content": desc
            }
        ],
        temperature=0,
        #max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        json_text = response.choices[0].message.content
        data = json.loads(json_text)
        with open(f"{outfolder}/{md5}.json", 'w') as json_file:
            json.dump(data, json_file, sort_keys=True, indent=4)
    except Exception as e:
        print(f"Failed request or parsing for {line}")
        print(repr(e))

with open(infile) as file:
    tsv = csv.reader(file, delimiter="\t")
    for line in itertools.islice(tsv, start, end):
        parse_line(line)
