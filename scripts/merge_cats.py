import os
from shutil import copyfile
import glob

from birds import BirdScraper

bird = BirdScraper()

main_cat = set([s.split(' ', 1)[0] for s in bird.species_names])

# Create new merged directory with main species
os.makedirs("../data/birds_merged/", exist_ok=True)
[os.makedirs(f"../data/birds_merged/{mc}", exist_ok=True) for mc in main_cat]

# Get all sub-specie names
path = "../data/birds/"
species = os.listdir(path)[1:]

# Move images to merged directory
for mc in main_cat:
	for s in species:
		idx = 0
		if mc in s:
			for file in glob.glob(f"../data/birds/{s}/*.jpg"):
				copyfile(file, f"../data/birds_merged/{mc}/{s}_{idx}.jpg")
				idx += 1

#[copyfile(f"../data/birds/{s}/{file}", f"../data/birds_merged/{mc}/") for file in glob.glob(f"../data/birds/{s}/*.jpg") for s in species for mc in main_cat if mc in s]




