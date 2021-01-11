inp_f = "tweet.csv"
out_f = "datasettwitter.csv"
c = open(out_f, "x")
c.close()
with open(inp_f, "r") as f:
  asd = f.readlines()
  for a in asd:
    try:
      line = a.split(", ")
      b = open(out_f, "a")
      x = line[0].replace("\"", "")
      y = ''.join(line[1:]).replace("\"", "").replace("\n", "")
      b.write(f'"{x}","{y}"\n')
      b.close()
    except:
      pass