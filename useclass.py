pipeline = ModularPipelineLayoutLM()

document = pipeline.load_document("example.pdf")

answer = pipeline.ask(
    document,
    "What is this document about?"
)

print(answer)