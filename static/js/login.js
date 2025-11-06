document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;
    
    try {
        const response = await fetch('/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, senha })
        });
        
        if (response.ok) {
            const data = await response.json();
            setToken(data.access_token);
            setUsuario(data.usuario);
            window.location.href = '/dashboard';
        } else {
            const error = await response.json();
            document.getElementById('errorMessage').textContent = error.detail || 'Erro ao fazer login';
            document.getElementById('errorMessage').classList.remove('hidden');
        }
    } catch (error) {
        document.getElementById('errorMessage').textContent = 'Erro de conexão com o servidor';
        document.getElementById('errorMessage').classList.remove('hidden');
    }
});

document.getElementById('registerForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const nome = document.getElementById('reg_nome').value;
    const email = document.getElementById('reg_email').value;
    const senha = document.getElementById('reg_senha').value;
    const tipo = document.getElementById('reg_tipo').value;
    
    try {
        const response = await fetch('/api/auth/registro', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nome, email, senha, tipo })
        });
        
        if (response.ok) {
            alert('Conta criada com sucesso! Faça login.');
            hideRegisterForm();
        } else {
            const error = await response.json();
            document.getElementById('regErrorMessage').textContent = error.detail || 'Erro ao criar conta';
            document.getElementById('regErrorMessage').classList.remove('hidden');
        }
    } catch (error) {
        document.getElementById('regErrorMessage').textContent = 'Erro de conexão com o servidor';
        document.getElementById('regErrorMessage').classList.remove('hidden');
    }
});

function showRegisterForm() {
    document.getElementById('registerModal').classList.remove('hidden');
}

function hideRegisterForm() {
    document.getElementById('registerModal').classList.add('hidden');
    document.getElementById('registerForm').reset();
    document.getElementById('regErrorMessage').classList.add('hidden');
}
