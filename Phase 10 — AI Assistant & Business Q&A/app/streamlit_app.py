from __future__ import annotations

import os
from pathlib import Path

import pandas as pd
import streamlit as st

from query_engine import answer_query

st.set_page_config(page_title="RetainIQ AI Assistant", page_icon="📊", layout="wide")

st.sidebar.header("RetainIQ connection")
mysql_password = st.sidebar.text_input("MySQL password (optional)", type="password", help="Needed only for exact SQL-routed portfolio/comparison queries.")
st.title("RetainIQ AI Assistant")
st.caption("Grounded telecom retention intelligence powered by RetainIQ evidence + local Qwen3 4B")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            with st.expander("Evidence used"):
                st.dataframe(pd.DataFrame(msg["sources"]), use_container_width=True, hide_index=True)

question = st.chat_input("Ask a RetainIQ business question...")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Retrieving evidence and generating a grounded answer..."):
            result = answer_query(question, mysql_password=mysql_password or None)
        st.markdown(result["answer"])
        source_rows = []
        if result["sql_evidence"] is not None and not result["sql_evidence"].empty:
            source_rows.extend(
                result["sql_evidence"][['evidence_id','source_name','topic']].to_dict('records')
            )
        source_rows.extend(
            result["retrieved"][['evidence_id','source_name','topic','similarity']].to_dict('records')
        )
        if source_rows:
            with st.expander("Evidence used"):
                st.dataframe(pd.DataFrame(source_rows), use_container_width=True, hide_index=True)
        st.caption(f"Mode: {result['mode']}")
        st.session_state.messages.append({"role": "assistant", "content": result["answer"], "sources": source_rows})
