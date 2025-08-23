<!-- leave_feedback.html -->
<h1>Leave Feedback</h1>
<form method="post">
    {% csrf_token %}
        {{ form.as_p }}
            <button type="submit">Submit</button>
            </form>
<!-- leave_feedback.html with JavaScript validation -->
<h1>Leave Feedback</h1>
<form method="post" id="feedbackForm">
    {% csrf_token %}
        {{ form.as_p }}
            <button type="submit">Submit</button>
            </form>

            <script>
                document.getElementById('feedbackForm').addEventListener('submit', function(event) {
                        const commentField = document.querySelector('textarea[name="comment"]');
                                if (!commentField.value.trim()) {
                                            alert('Please enter your feedback.');
                                                        event.preventDefault();
                                                                }
                                                                    });
                                                                    </script>
                                                                    