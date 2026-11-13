"""Shared comparison view for standalone and API-backed search."""
from time import perf_counter

import streamlit as st


def render_comparison(search, top_k):
    """Run search(query, mode, top_k) independently for each retrieval method."""
    st.subheader("Compare retrieval methods")
    st.caption("One question, two ranked answer lists. Similarity scores are not probabilities and should not be compared directly across models.")
    with st.form("comparison_search"):
        query = st.text_input("Career question", placeholder="How can I negotiate my first job offer?")
        submitted = st.form_submit_button("Compare answers")
    if not submitted:
        return
    query = query.strip()
    if not query:
        st.warning("Enter a question to compare results.")
        return
    outputs = {}
    for column, mode, label in zip(st.columns(2), ("tfidf", "sbert"), ("TF-IDF · Keywords", "SBERT · Meaning")):
        with column:
            st.markdown(f"### {label}")
            try:
                with st.spinner(f"Searching with {mode.upper()}..."):
                    start = perf_counter()
                    results = search(query, mode, top_k)
                    elapsed = (perf_counter() - start) * 1000
                if results is None:
                    st.warning("This method is unavailable. Check the model or API status.")
                    continue
                outputs[mode] = results
                st.metric("Search time", f"{elapsed:.1f} ms")
                if not results:
                    st.info("No results returned.")
                for rank, result in enumerate(results, 1):
                    with st.container(border=True):
                        st.markdown(f"**#{rank}**")
                        st.text(str(result["question"]))
                        st.caption(f"Similarity: {result['score']:.3f} · Source: {result.get('source', 'unknown')}")
                        st.text(str(result["answer"]))
            except Exception:
                st.error("Search failed for this method. Check the model or API connection and try again.")
    if len(outputs) == 2 and all(outputs.values()):
        left = {r["question"] for r in outputs["tfidf"]}
        right = {r["question"] for r in outputs["sbert"]}
        st.info(f"Shared questions in these result lists: {len(left & right)}. "
                f"Top answer agrees: {'Yes' if outputs['tfidf'][0]['question'] == outputs['sbert'][0]['question'] else 'No'}.")
    st.caption("Timing covers each search call; API mode includes network overhead. Model startup is excluded. These are individual measurements, not a benchmark.")
