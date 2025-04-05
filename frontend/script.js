async function analyzePassword() {
  const password = document.getElementById('passwordInput').value;
  const response = await fetch('http://localhost:5000/api/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ password })
  });
  const result = await response.json();
  document.getElementById('result').innerHTML = `
    <p>Strength: <strong>${result.strength}</strong></p>
    <p>${result.message}</p>
  `;
}

