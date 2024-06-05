# This is a simple sentiment analysis model code
def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text.

    Parameters:
        text (str): The text to analyze.

    Returns:
        str: The sentiment of the text ('positive', 'negative', or 'neutral').
    """
    # Perform sentiment analysis using basic rules
    if "good" in text:
        return "positive"
    elif "bad" in text:
        return "negative"
    else:
        return "neutral"
