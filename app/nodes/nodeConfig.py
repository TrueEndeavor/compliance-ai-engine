from typing import TypedDict, Optional
from fastapi import File

class AgentState(TypedDict):
    marketing_file_bytes: bytes
    # sec_MisleadingUnsubstantiatedClaims :str 
    # sec_general_prohibitions:str
    # sec_misleading_examples:str
    sec_misleading_artifact:Optional[str]
    sec_typography_artifact:Optional[str]



