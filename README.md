# Document Comparison

This is an early stage toy project for detecting differences between documents. A big part of my partner’s job is comparing insurance forms, and it varies whether the comparison is at word level or topic level. The repo contains a heuristic and an LLM based method for finding differences between documents. THIS PROJECT IS STILL IN DEVELOPMENT.

## Description

The simple_doc_comparison is better suited for finding word level differences between documents. For example, finding the differences between the sentences:

“The out-of-pocket maximum for this plan is $1000.”

“The out-of-pocket max for this plan is $1000.”

In this case the differences in max and maximum will be flagged. It is recommended to use this file if you know the documents you are comparing are very similar and short, as this method might produce a lot of output.

The demo.ipynb is better suited for comparing documents at a topic level, and for comparisons of complex documents. For example, you should use this file if you are finding the differences between benefits for BCBS Michigan and BCBS North Carolina. I use a langchain framework and embeddings to allow for semantic meaning to be captured, so more nuanced differences in the docs can be gleaned.

## Installation

To set up the Document Comparison on your local machine, follow these steps:

1. Clone the repository to your local machine.
2. Install the required packages:
pip install langchain pandas os textwrap difflib string
