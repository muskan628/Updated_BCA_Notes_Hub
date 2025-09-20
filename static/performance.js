 document.querySelectorAll('.score-bar').forEach(bar => {
      let scoreText = bar.getAttribute('data-score'); // e.g. "15/20"
      let [obtained, total] = scoreText.split('/').map(Number);
      let percent = (obtained / total) * 100;

      bar.querySelector('.fill').style.width = percent + "%";
    });

    // Generate attempts summary
  let attempts = {};
  document.querySelectorAll('#marksTable tbody tr').forEach(tr => {
    let subject = tr.children[0].innerText;
    attempts[subject] = (attempts[subject] || 0) + 1;
  });

  let tbody = document.querySelector('#summaryBox tbody');
  for(let subject in attempts){
    let row = document.createElement('tr');
    row.innerHTML = `<td>${subject}</td><td>${attempts[subject]}</td>`;
    tbody.appendChild(row);
  }