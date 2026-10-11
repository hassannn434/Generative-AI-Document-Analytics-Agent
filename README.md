# 🤖 Enterprise AI Document Analytics Agent

A production-ready, locally optimized **Retrieval-Augmented Generation (RAG)** pipeline designed for secure corporate data extraction, dynamic document chunking, and semantic context retrieval. 

This application features a decoupled architecture that combines lightweight local text vectorisation with production-tier Large Language Models (LLMs) to ensure reliable performance without API timeout constraints.

🌐 **Live Production Link:** `https://generative-ai-document-analytics-agent-vcohtvguujguc2exlhabjg.streamlit.app/`

---

## 🛠️ System Architecture & Technology Stack

The pipeline architecture separates document loading, tensor embedding generation, vector indexing, and generative context synthesis into modular blocks:

[Uploaded PDF] ➔ [PyPDF Parser] ➔ [Recursive Text Splitter (1000/200)]
│
▼
[ChromaDB In-Memory Vector Store] ➔ [Local HuggingFace Embeddings (all-MiniLM-L6-v2)]
│
▼
[Semantic Query Match (k=3)] ➔ [Gemini-3.8-Flash LLM] ➔ [Streamlit UI Output]

*   **Application Interface Framework:** `Streamlit` (Handles asynchronous session states and isolated file-buffer uploads).
*   **Orchestration Framework:** `LangChain v1.0+ (Modular Architecture)` (Manages data loading schemas and modular retrieval loops via decoupled components).
*   **Vector Database Engine:** `ChromaDB` (In-memory token vector store optimized for high-performance localized similarity-score indexing).
*   **Localized Embedding Layer:** `HuggingFace (sentence-transformers/all-MiniLM-L6-v2)` (A 384-dimensional dense vector mapping engine that completely eliminates cloud API latencies and endpoint deprecation issues).
*   **Generative AI Layer:** Google GenAI `gemini-3.8-flash` (An enterprise-grade LLM used exclusively for final answer formatting based on strictly bounded retrieved documents).

---

## 🚀 Key Engineering Implementations

### 1. Token-Conscious Document Chunking Strategy
Instead of splitting text arbitrarily by paragraphs or characters, the processing engine utilizes a `RecursiveCharacterTextSplitter` configured with a **chunk size of 1000 tokens and a chunk overlap of 200 tokens**. This approach provides two key benefits:
*   **Context Preservation:** The 200-token overlap acts as a sliding window, keeping semantic concepts intact across adjacent chunk text frames.
*   **Context Window Optimization:** Restricting chunks to 1000 tokens keeps data well within the maximum context window limits of modern LLMs, preventing performance degradation during the synthesis stage.

### 2. High-Availability Hybrid Extraction Layer
The embedding layer was migrated from a network-dependent cloud service to a local execution architecture. Using the `all-MiniLM-L6-v2` transformer model running locally on the server container provides:
*   **Zero Cost Friction:** Generating vector representations of files does not consume external API credits or token allowances.
*   **Resiliency to Overlapping Network Demands:** Eliminates `404 Not Found` network path routing updates and network handshake failures during concurrent file uploads.

### 3. Traceable Source Attribution & Grounding
To address common LLM hallucination risks in corporate environments, this application implements strict technical guardrails:
*   **System Prompt Isolation:** The underlying model is strictly instructed to respond *only* using the verified contextual nodes extracted from the user's PDF. If the answer cannot be found in the text, it returns an explicit message stating that the information is unavailable.
*   **Verifiable Source Verification:** Streamlit interface expanders expose the raw text fragments and page index vectors directly from ChromaDB, allowing the user to verify exactly where the data came from.

---

## 📁 Directory Structure & File Mapping

```text
Generative-AI-Document-Analytics-Agent/
│
├── app.py               # Main application orchestration file (UI & Core RAG Logic)
├── requirements.txt     # Locked production environment dependency versions
└── README.md            # Technical portfolio documentation and system overview
```

---

## ⚙️ Installation & Local Replication Guide

Follow these steps in your command-line terminal to duplicate and run this application layer on your local machine:

```bash
# 1. Clone the repository from your active GitHub space
git clone https://github.com

# 2. Enter the root project folder directory
cd Generative-AI-Document-Analytics-Agent

# 3. Install the exact necessary system-wide dependencies
pip install -r requirements.txt

# 4. Start the local server stream instance loop
streamlit run app.py

##OUTPUT SCREENSHOT
<img width="1919" height="853" alt="image" src="https://github.com/user-attachments/assets/775ac4f0-731c-4309-a590-00d167b86e85" />


🛠️ Core Technology Stack

The engineering architecture is built using a completely decoupled framework to optimize token costs and eliminate runtime network dependencies:
• User Interface Layer: Streamlit – Manages the real-time web interface, user inputs, file-buffer configurations, and asynchronous app states.
• Pipeline Orchestration: LangChain v1.0+ – Handles structural loading blocks, recursive formatting schemas, and modular context-injection loops.
• Vector Database Index: ChromaDB – Acts as a high-performance, in-memory vector store optimized for localized document chunk mapping.
• Native Embedding Layer: HuggingFace (sentence-transformers/all-MiniLM-L6-v2) – A local 384-dimensional mathematical mapping tool that completely removes external cloud API latencies.
• Generative AI Model: Google GenAI gemini-3.8-flash – The final large language model endpoint used exclusively for context-grounded natural language synthesis.

🚀 Production Application & Use Cases

This application serves as a secure enterprise intelligence utility tailored to process highly unstructured corporate data without letting confidential files touch external tracking nodes:
• Financial Audit & Invoice Automation: Instantly cross-checks line-item values, tax tables, and procurement records across multi-page financial PDF files.
• Technical Literature & Research Synthesizer: Processes complex academic papers or technical engineering reports (such as your ML REPORT.pdf) to explain methods, metrics, and data points cleanly.
• Legal Contract Analysis: Queries standard master service agreements (MSAs) or statements of work (SOWs) for compliance parameters, risks, and termination dates.

🎯 Project Conclusion

The Enterprise AI Document Analytics Agent successfully achieves two main engineering goals:
1. Elimination of Cloud Friction: By migrating the text tokenization workflow from network-reliant endpoints to local Hugging Face pipelines, the system remains immune to API changes, network timeouts, and token credit billing.
2. Strict Anti-Hallucination Boundaries: By chaining a rigid semantic search layer (k=3 relevant document nodes) to Google's production LLM, the system forces data grounding. This ensures that the generated output relies entirely on true document context, making it reliable for real-world enterprise tasks.


* **Developer Name:** Hassan Mahadkar
* **Profile Focus:** Artificial Intelligence & Machine Learning Engineering (B.Tech Third Year Candidate)
* **Email: hassanmahadker1@gmail.com
* **LinkedIN: https://www.linkedin.com/in/hassan-mahadker-07489838b/
* **Contact[8879391649]

ThankYou!!!!!

