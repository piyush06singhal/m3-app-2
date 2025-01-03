from ._anvil_designer import mainFrameTemplate
from anvil import *
import anvil.server

class mainFrame(mainFrameTemplate):
    def __init__(self, **properties):
        """Initialize the form and its components."""
        self.init_components(**properties)
        self.video_url_textbox.text = ""  # Clear the URL textbox initially (optional)

    def analyze_button_click(self, **event_args):
        """Triggered when the 'Analyze' button is clicked."""
        video_url = self.video_url_textbox.text.strip()  # Get the video URL entered by the user

        # Check if the URL is empty
        if not video_url:
            self.result_label.text = "Please enter a valid YouTube URL."
            return

        try:
            # Disable the TextBox while processing to prevent new inputs
            self.video_url_textbox.enabled = False
            # Show a loading message or similar feedback
            self.result_label.text = "Analyzing the video, please wait..."

            # Call the analyze_video function on the server
            result = anvil.server.call('analyze_video', video_url)

            if 'error' in result:
                self.result_label.text = f"Error: {result['error']}"
            else:
                sentiment = result['sentiment']
                genre = result['genre']
                self.result_label.text = f"The Overall Video Sentiment Analysis is: {sentiment}\nThe Overall Video Genre is: {genre}"

                # Optionally, you can display a message indicating that no download is available
                self.result_label.text += "\nAnalysis complete."

        except Exception as e:
            # Handle any unexpected errors
            self.result_label.text = f"An unexpected error occurred: {str(e)}"

        finally:
            # Re-enable the TextBox after the processing is finished
            self.video_url_textbox.enabled = True
