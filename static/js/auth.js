function getToken() {
    return localStorage.getItem('token');
}

function setToken(token) {
    localStorage.setItem('token', token);
}

function removeToken() {
    localStorage.removeItem('token');
    localStorage.removeItem('usuario');
}

function setUsuario(usuario) {
    localStorage.setItem('usuario', JSON.stringify(usuario));
}

function getUsuario() {
    const usuario = localStorage.getItem('usuario');
    return usuario ? JSON.parse(usuario) : null;
}

function logout() {
    removeToken();
    window.location.href = '/';
}

async function apiRequest(url, options = {}) {
    const token = getToken();
    const headers = {
        'Content-Type': 'application/json',
        ...options.headers
    };
    
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }
    
    const response = await fetch(url, {
        ...options,
        headers
    });
    
    if (response.status === 401) {
        logout();
        return;
    }
    
    return response;
}

function checkAuth() {
    const token = getToken();
    if (!token) {
        window.location.href = '/';
    }
}

if (window.location.pathname !== '/' && !getToken()) {
    window.location.href = '/';
}
