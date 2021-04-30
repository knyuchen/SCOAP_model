def and2_forward (a, b):
   CC0 = min (a[0], b[0]) + 1
   CC1 = a[1] + b[1] + 1
   return CC0, CC1

def nand2_forward (a, b):
   CC0 = a[1] + b[1] + 1
   CC1 = min (a[0], b[0]) + 1
   return CC0, CC1

def or2_forward (a, b):
   CC0 = a[0] + b[0] + 1
   CC1 = min(a[1], b[1]) + 1
   return CC0, CC1

def nor2_forward (a, b):
   CC0 = min (a[1], b[1]) + 1
   CC1 = a[0] + b[0] + 1
   return CC0, CC1

def xor2_forward (a, b):
   CC0 = min( (a[0]+b[0]), (a[1]+b[1])) + 1
   CC1 = min( (a[1]+b[0]), (a[0]+b[1])) + 1
   return CC0, CC1

def nand3_forward (a, b, c):
   CC0 = a[1] + b[1] + c[1] + 1
   CC1 = min (a[0], b[0], c[0]) + 1
   return CC0, CC1

def nor3_forward (a, b, c):
   CC0 = min (a[1], b[1], c[1]) + 1
   CC1 = a[0] + b[0] + c[0] + 1
   return CC0, CC1

def xor3_forward (a, b, c):
   CC0 = min( (a[0]+b[0]+c[0]), (a[1]+b[1]+c[0]), (a[1]+b[0]+c[1]) , (a[0]+b[1]+c[1])) + 1
   CC1 = min( (a[1]+b[0]+c[0]), (a[0]+b[1]+c[0]), (a[0]+b[0]+c[1]) , (a[1]+b[1]+c[1])) + 1
   return CC0, CC1



def and2_backward (z, b):
   CO = z[2] + b[1] + 1
   return CO

def nand2_backward (z, b):
   CO = z[2] + b[1] + 1
   return CO

def or2_backward (z, b):
   CO = z[2] + b[0] + 1
   return CO

def nor2_backward (z, b):
   CO = z[2] + b[0] + 1
   return CO

def xor2_backward (z, b):
   CO = z[2] + min(b[0], b[1]) + 1
   return CO

def nand3_backward (z, b, c):
   CO = z[2] + b[1] + c[1] + 1
   return CO

def nor3_backward (z, b, c):
   CO = z[2] + b[0] + c[0] + 1
   return CO


def xor3_backward (z, b, c):
   CO = z[2] + min((b[0] + c[0]), (b[1] + c[0]) , (b[0] + c[1]), (b[1] + c[1])) + 1
   return CO

point = dict();

point["A"] = [1, 1, 0]
point["B"] = [1, 1, 0]
point["C"] = [1, 1, 0]
point["D"] = [1, 1, 0]
point["E"] = [1, 1, 0]
point["F"] = [1, 1, 0]

point["g"] = [1, 1, 0]
point["h"] = [1, 1, 0]
point["k"] = [1, 1, 0]
point["l"] = [1, 1, 0]
point["m"] = [1, 1, 0]
point["p"] = [1, 1, 0]
point["q"] = [1, 1, 0]
point["r"] = [1, 1, 0]
point["s"] = [1, 1, 0]
point["u"] = [1, 1, 0]
point["w"] = [1, 1, 0]
point["Z"] = [1, 1, 0]


point["g"][0], point["g"][1] = or2_forward(point["C"], point["D"])
point["l"][0], point["l"][1] = xor2_forward(point["E"], point["F"])

point["h"][0], point["h"][1] = and2_forward(point["C"], point["g"])
point["k"][0], point["k"][1] = and2_forward(point["D"], point["g"])
point["s"][0], point["s"][1] = or2_forward(point["B"], point["l"])

point["m"][0], point["m"][1] = or2_forward(point["h"], point["k"])

point["p"][0], point["p"][1] = nor3_forward(point["A"], point["B"], point["m"])
point["q"][0], point["q"][1] = or2_forward(point["B"], point["m"])
point["u"][0], point["u"][1] = and2_forward(point["A"], point["m"])

point["r"][0], point["r"][1] = and2_forward(point["A"], point["p"])
point["w"][0], point["w"][1] = and2_forward(point["q"], point["s"])

point["Z"][0], point["Z"][1] = xor3_forward(point["r"], point["u"], point["w"])



point["r"][2] = xor3_backward(point["Z"], point["u"], point["w"])
point["u"][2] = xor3_backward(point["Z"], point["r"], point["w"])
point["w"][2] = xor3_backward(point["Z"], point["u"], point["r"])

point["p"][2] = and2_backward(point["r"], point["A"])
point["q"][2] = and2_backward(point["w"], point["s"])
point["s"][2] = and2_backward(point["w"], point["q"])

# try to solve m

point["m"][2] = min(nor3_backward(point["p"], point["A"], point["B"]), or2_backward(point["q"], point["B"]), and2_backward(point["u"], point["A"]))
point["A"][2] = min(nor3_backward(point["p"], point["m"], point["B"]), and2_backward(point["u"], point["m"]))
point["B"][2] = min(nor3_backward(point["p"], point["A"], point["m"]), or2_backward(point["q"], point["m"]), or2_backward(point["s"], point["l"]))

point["h"][2] = or2_backward(point["m"], point["k"])
point["k"][2] = or2_backward(point["m"], point["h"])
point["l"][2] = or2_backward(point["s"], point["B"])


point["g"][2] = min (and2_backward(point["h"], point["C"]), and2_backward(point["k"], point["D"]))

point["C"][2] = min(and2_backward(point["h"], point["g"]), or2_backward(point["g"], point["D"]))
point["D"][2] = min(and2_backward(point["k"], point["g"]), or2_backward(point["g"], point["C"]))


point["E"][2] = or2_backward(point["l"], point["F"])
point["F"][2] = or2_backward(point["l"], point["E"])
print(point)
