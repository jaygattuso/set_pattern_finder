import os
import operator


def get_seq(f_path, start, end):
	with open(f_path, "rb") as data:
		bytes = data.read()
		return bytes[start:end]


def get_seq_reversed(f_path, start, end):
	with open(f_path, "rb") as data:
		bytes = data.read()
		bytes = bytes[::-1]
		return bytes[start:end]

def process(folder, start=0, end=16, show_all=False):
	seqs = {}
	for root, subs, files in os.walk(folder):
		for f in files:
			f_path = os.path.join(root, f)
			if os.path.isfile(f_path):
				filename, file_extension = os.path.splitext(f_path)
				if file_extension == "":
					seq = get_seq(f_path, start, end)
					if seq != "":
						if seq not in seqs:
							seqs[seq] = 1
						else:
							seqs[seq] += 1
						if show_all:
							print "".join("{:02x}".format(ord(c)) for c in seq), repr( seq), f_path

	if show_all:
		print 
	return seqs

def show_results(seqs):
	sorted_seqs = sorted(seqs.items(), key=operator.itemgetter(1), reverse=True)
	for s in sorted_seqs:
		byte_pattern = "".join("{:02x}".format(ord(c)) for c in s[0])
		if cap < s[1]:
			print "Count: {}\t Patterns: {} {}".format(s[1], byte_pattern, repr(s[0]))

	print

	print "Total unique patterns: {}".format(len(seqs))


### Folder of interest
folder = r""

### start offset
start = 0

### end offset 
end = 2



seqs = process(folder, start, end, show_all=True)
show_results(seqs, cap=10)
