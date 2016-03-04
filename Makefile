# input file
GENOME = $(CURDIR)/genome.gbk

# scripts directory
SRC = $(CURDIR)/src
# notebooks directory
NOTEBOOKS = $(CURDIR)/notebooks

# output file
TABLE = $(CURDIR)/gene_table.tsv
$(TABLE): $(GENOME)
	python $(SRC)/get_genes.py $< > $@		

NREPORT1 = $(NOTEBOOKS)/gene_sizes.ipynb
RREPORT1 = $(NOTEBOOKS)/gene_sizes.html

$(RREPORT1): $(TABLE) $(NREPORT1)
	cd $(NOTEBOOKS) && jupyter nbconvert --to=html --template=html.tpl --ExecutePreprocessor.enabled=True $(NREPORT1)

all: $(RREPORT1)
clean:
	-rm $(TABLE)
	-rm $(RREPORT1)

.PHONY: all clean
