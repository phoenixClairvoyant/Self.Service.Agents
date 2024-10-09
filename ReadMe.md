The project is a research into the use of Llamaindex & crewAI for the development of an Agent agent application. The goal is to 
create a scalable and automated way to enable engineer self-service.



### End output: Use cases

- Generating a IAC for a new Azure Resource
- ADRs'
  - Help me generate an ADR using existing context
  - Check my current work aganist ADRs for compliance.
    - Check code against ADRs
    - Check designs/diagrams against ADRs
  - Given the work I want to do which ADRs are relevant for me to consider? Could we improve it?
  
- Playbooks
- What is required for me to be compliant with a playbook given this process?
- Generate scaffolding given a playbook process.
- Generate a new playbook given a set of playbook standards.


### Failure Modes and possible solutions:

#### 1. **Generating IAC for a New Azure Resource**

##### Failure Modes:
- **Inconsistent or non-compliant configurations**: The Agent might generate infrastructure-as-code (IAC) that does not align with company standards or security policies.
- **Outdated templates**: The agent may use outdated or deprecated services or versions, leading to suboptimal or insecure configurations.
- **Complexity mismatch**: The Agent might not correctly gauge the complexity of the resource and could generate overly complex or inefficient code.

**Possible solutions:**
- **Policy-based validation**: Implement a mechanism to validate the generated IAC against a predefined policy or schema before it is deployed. This can be done using tools like Azure Policy or OPA (Open Policy Agent).
- **Version control integration**: Ensure the Agent uses the latest templates and configurations by integrating it with a version-controlled repository of IAC templates and company standards.
- **Feedback loop**: Continuously refine the model’s output by tracking common errors or inefficiencies in the generated code and using this data for further training and improvements.


#### 2. **ADRs (Architectural Decision Records)**

**Help Generate an ADR Using Existing Context:**

##### Failure Modes:
- **Context misinterpretation**: The Agent may misunderstand the context of the project or the scope of the decision, leading to inaccurate ADRs.
- **Incomplete ADR**: The generated ADR may miss key sections such as alternatives considered or decision drivers.
- **Inconsistent style or format**: The ADR may not adhere to the company's documentation style or format.

**Possible solutions:**
- **Structured input prompts**: Ensure that the input prompt explicitly outlines all necessary components (e.g., context, alternatives, pros/cons) for generating a complete ADR.
- **Pre-defined templates**: Use templates with predefined sections for ADR generation to ensure consistency in structure and format.
- **Contextual awareness**: Implement a knowledge retrieval system (RAG) to pull in relevant prior decisions and contextual information to guide the Agent in generating more accurate ADRs.


**Check My Work Against ADRs for Compliance (Code & Design):**

##### Failure Modes:
- **Incorrect matching of ADRs to code**: The Agent may not correctly link the ADRs with the code or designs, leading to false positives or missed compliance issues.
- **Overly strict validation**: The Agent might flag deviations that are permissible under the company's ADRs, causing unnecessary friction in the workflow.
- **Inconsistent application of ADRs**: The agent may apply different interpretations of the same ADR across different checks.
- **Lack of context**: The agent may not have access to the context of the project or workstream, leading to incorrect ADRs being flagged.

**Possible solutions:**
- **Semantic analysis**: Use semantic similarity tools to ensure that the code or design is accurately matched with the relevant ADRs.
- **Multimodal RAG**: Use multimodal RAG to ensure that the code or design is accurately matched with the relevant ADRs.
- **Thresholds for compliance**: Set customizable thresholds for flagging compliance issues to prevent overly strict or lenient checks.
- **Contextual compliance checks**: Ensure that the Agent understands exceptions or edge cases documented within the ADRs and applies the rules accordingly.


**Given My Work, Which ADRs are Relevant for Me to Consider?**

##### Failure Modes:
- **Irrelevant ADRs**: The Agent may suggest ADRs that don’t align with the current project or workstream.
- **Missing critical ADRs**: The Agent may overlook important ADRs that should be considered for a given project.
- **Lack of prioritization**: The Agent may not prioritize ADRs, presenting a large, unordered list instead of focusing on the most relevant ones.

**Possible solutions:**
- **RAG-based filtering**: Use retrieval-augmented generation (RAG) to filter ADRs based on the project context, ensuring only the most relevant ADRs are returned.
- **Prioritization mechanisms**: Rank ADRs based on the relevance to the current project scope, potentially integrating priority tags or weights.
- **Continuous learning**: Allow feedback from engineers about which ADRs were most helpful to refine the Agent’s recommendations over time.

