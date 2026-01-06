from langgraph.graph import StateGraph,START,END
from app.nodes.nodeConfig import AgentState
from app.nodes.sec_misleading import sec_misleading
from app.nodes.sec_typographycheck import sec_typographycheck

def run_workflow(pdfbytes
                #  sec_MisleadingUnsubstantiatedClaims,
                #  sec_general_prohibitions,
                #  sec_misleading_examples
                 ):
    graph = StateGraph(AgentState)
    graph.add_node('sec_misleading',sec_misleading)
    graph.add_node('sec_typographycheck',sec_typographycheck)

    graph.add_edge(START,'sec_misleading')
    graph.add_edge('sec_misleading','sec_typographycheck')
    graph.add_edge('sec_typographycheck',END)

    app = graph.compile()

    compliance_report_intialstate = AgentState(
        marketing_file_bytes = pdfbytes,
        # sec_MisleadingUnsubstantiatedClaims = sec_MisleadingUnsubstantiatedClaims,
        # sec_general_prohibitions = sec_general_prohibitions,
        # sec_misleading_examples = sec_misleading_examples,
        sec_misleading_artifact = "",
        sec_typography_artifact=""
    )

    compliance_report_artifact = app.invoke(compliance_report_intialstate)

    return compliance_report_artifact
    