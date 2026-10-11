from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

# locally downloaded model requires high RAM and GPUf

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs= {
        "temperature": 0.7, 
        "max_new_tokens": 10
    }
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Pakistan?")

print(result.content)