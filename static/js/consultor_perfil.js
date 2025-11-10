checkAuth();

const usuario = getUsuario();
document.getElementById('userInfo').textContent = `${usuario.nome} (${usuario.tipo})`;

if (usuario.tipo === 'admin') {
    document.getElementById('adminLink').classList.remove('hidden');
}

async function carregarPerfilConsultor() {
    try {
        const response = await apiRequest(`/api/consultores/${consultorId}`);
        const data = await response.json();
        
        const perfil = data.perfil;
        const estatisticas = data.estatisticas;
        const prospeccoes = data.prospeccoes;
        
        const perfilDiv = document.getElementById('perfilConsultor');
        perfilDiv.innerHTML = `
            <div class="space-y-3">
                <div>
                    <p class="text-gray-400 text-sm">Nome</p>
                    <p class="text-white font-medium">${perfil.nome}</p>
                </div>
                <div>
                    <p class="text-gray-400 text-sm">Email</p>
                    <p class="text-white font-medium">${perfil.email}</p>
                </div>
                <div>
                    <p class="text-gray-400 text-sm">Data de Nascimento</p>
                    <p class="text-white font-medium">${perfil.data_nascimento ? new Date(perfil.data_nascimento).toLocaleDateString('pt-BR') : '-'}</p>
                </div>
                <div>
                    <p class="text-gray-400 text-sm">Modelo do Carro</p>
                    <p class="text-white font-medium">${perfil.modelo_carro || '-'}</p>
                </div>
                <div>
                    <p class="text-gray-400 text-sm">Placa do Carro</p>
                    <p class="text-white font-medium">${perfil.placa_carro || '-'}</p>
                </div>
                <div>
                    <p class="text-gray-400 text-sm">Informações Básicas</p>
                    <p class="text-white font-medium">${perfil.informacoes_basicas || '-'}</p>
                </div>
            </div>
        `;
        
        document.getElementById('totalProspeccoes').textContent = estatisticas.total_prospeccoes;
        
        const tbody = document.getElementById('tabelaProspeccoes');
        if (!prospeccoes || prospeccoes.length === 0) {
            tbody.innerHTML = '<tr><td colspan="4" class="px-6 py-8 text-center text-gray-400">Nenhuma prospecção realizada ainda</td></tr>';
            return;
        }
        
        tbody.innerHTML = prospeccoes.map(prosp => `
            <tr class="hover:bg-dark-hover">
                <td class="px-6 py-4 text-gray-300">${prosp.data_prospeccao ? new Date(prosp.data_prospeccao).toLocaleDateString('pt-BR') : (prosp.data_ligacao ? new Date(prosp.data_ligacao).toLocaleDateString('pt-BR') : '-')}</td>
                <td class="px-6 py-4 text-gray-300">Empresa ID: ${prosp.empresa_id}</td>
                <td class="px-6 py-4 text-gray-300">${prosp.status_prospeccao || '-'}</td>
                <td class="px-6 py-4 text-gray-300">${prosp.resultado || '-'}</td>
            </tr>
        `).join('');
        
    } catch (error) {
        console.error('Erro ao carregar perfil do consultor:', error);
        document.getElementById('perfilConsultor').innerHTML = 
            '<p class="text-red-400">Erro ao carregar perfil</p>';
    }
}

carregarPerfilConsultor();
