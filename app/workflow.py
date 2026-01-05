from langgraph.graph import StateGraph,START,END
from nodes.nodeConfig import AgentState
from nodes.sec_misleading import sec_misleading

def run_workflow(pdfbytes,
                #  sec_MisleadingUnsubstantiatedClaims,
                #  sec_general_prohibitions,
                #  sec_misleading_examples
                 ):
    graph = StateGraph(AgentState)
    graph.add_node('sec_misleading',sec_misleading)

    graph.add_edge(START,'sec_misleading')
    graph.add_edge('sec_misleading', END)

    app = graph.compile()

    compliance_report_intialstate = AgentState(
        marketing_file_bytes = pdfbytes,
        # sec_MisleadingUnsubstantiatedClaims = sec_MisleadingUnsubstantiatedClaims,
        # sec_general_prohibitions = sec_general_prohibitions,
        # sec_misleading_examples = sec_misleading_examples,
        sec_misleading_artifact = ""
    )

    compliance_report_artifact = app.invoke(compliance_report_intialstate)

    return compliance_report_artifact
    