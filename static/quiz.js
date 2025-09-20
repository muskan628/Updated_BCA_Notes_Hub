 function startQuiz(subjectName, element) {
      // Update quiz title
      document.getElementById('quizSubject').innerText = subjectName + " Quiz";

      // Update quiz questions (placeholder)
      const questionsDiv = document.getElementById('quizQuestions');
      questionsDiv.innerHTML = "<p>Loading 20 MCQs for " + subjectName + "...</p>";

      // Move quiz container just below clicked card
      const quizContainer = document.getElementById('quizContainer');
      element.after(quizContainer);
      quizContainer.style.display = 'block';
    }

    function submitQuiz() {
      alert("Quiz submitted! (Backend integration pending)");
    }

    // Optional: Auto-start quiz if URL has ?subject=XYZ
    window.onload = function() {
      const params = new URLSearchParams(window.location.search);
      const subject = params.get('subject');
      if(subject) {
        // Find first subject card with this name
        const cards = document.querySelectorAll('.subject-card');
        cards.forEach(card => {
          if(card.querySelector('h3').innerText === subject) {
            startQuiz(subject, card);
          }
        });
      }
    }