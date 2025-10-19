// Demo seguro: NÃO armazenar credenciais reais.
// Quando o usuário envia, geramos um token de teste e exibimos mensagem educativa.

document.getElementById('loginForm').addEventListener('submit', function (e) {
  e.preventDefault();
  const email = document.getElementById('email').value;
  // NÃO usar a senha para nada; apenas demonstrar que o formulário foi submetido.
  // const password = document.getElementById('password').value;

  // Gerar token de teste (pseudo-anônimo)
  const token = 'TEST-TOKEN-' + Math.random().toString(36).slice(2,10).toUpperCase();

  // Exibir mensagem educativa para o usuário
  const result = document.getElementById('result');
  result.hidden = false;
  result.innerHTML = `
    <strong>Atenção — simulação educativa</strong>
    <p>Você submeteu um formulário em uma página de demonstração. Nenhuma credencial real foi armazenada.</p>
    <p><em>Token de teste gerado:</em> <code>${token}</code></p>
    <p>Objetivo: demonstrar fluxo e incentivar boas práticas (MFA, verificação de URL, cuidado com e-mails).</p>
  `;

  // Em ambiente realizado para análise, registrar somente indicadores (no console aqui)
  console.log('[DEMO] submissão simulada — email:', email, ' token:', token);

  // limpar o campo senha apenas por UX
  document.getElementById('password').value = '';
});
