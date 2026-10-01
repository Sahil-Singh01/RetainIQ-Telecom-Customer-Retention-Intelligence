# Phase 10 Methodology

## Hybrid query strategy

I use RAG for project definitions and contextual evidence, and route a small set of exact comparison/portfolio questions to trusted MySQL reporting views. This reduces the risk of semantic retrieval over-selecting one entity when the user asks for a global comparison.

## Comparison-aware retrieval

When a question contains comparison markers such as highest, lowest, largest, top, compare, or versus, I retrieve a broader candidate pool and diversify by source document before sending evidence to the LLM.

## Grounding rules

The generator receives only retrieved/query evidence. It must distinguish observed metrics from calculations and assumptions, preserve evidence IDs, and acknowledge insufficient evidence instead of filling gaps with invented values.

## Local generation

The default local endpoint is Ollama's OpenAI-compatible API at `http://localhost:11434/v1`, with `qwen3:4b` as the default model.
