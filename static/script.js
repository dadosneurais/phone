async function buscar() {
    const telefone = document.getElementById("telefone").value.trim();
    const resultado = document.getElementById("resultado");
    resultado.textContent = "🔄 Buscando...";
  
    const res = await fetch('/api/buscar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ telefone })
    });
  
    const data = await res.json();
    resultado.textContent = "";
  
    if (data.nomes?.length) {
      data.nomes.forEach(nome => {
        const p = document.createElement("p");
        p.textContent = nome;
        resultado.appendChild(p);
      });
    } else {
      resultado.textContent = data.erro ? `❌ ${data.erro}` : "⚠️ Nenhum nome encontrado.";
    }
  }
  