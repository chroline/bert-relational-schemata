def convert_conceptnet_uri(uri: str) -> str:
    # Split by slashes and take the last segment
    term = uri.strip().split("/")[-1]
    # Replace underscores with spaces
    return term.replace("_", " ")
