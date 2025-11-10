checkAuth();

const usuario = getUsuario();
document.getElementById('userInfo').textContent = `${usuario.nome} (${usuario.tipo})`;

if (usuario.tipo === 'admin') {
    document.getElementById('adminLink').classList.remove('hidden');
}

let paginaAtual = 1;
const itensPorPagina = 20;

async function carregarConsultores(pagina = 1) {
    try {
        paginaAtual = pagina;
        const response = await apiRequest(`/api/consultores/?page=${pagina}&page_size=${itensPorPagina}`);
        const data = await response.json();
        
        const tbody = document.getElementById('tabelaConsultores');
        
        if (!data.items || data.items.length === 0) {
            tbody.innerHTML = '<tr><td colspan="4" class="px-6 py-8 text-center text-gray-400">Nenhum consultor encontrado</td></tr>';
            return;
        }
        
        tbody.innerHTML = data.items.map(consultor => `
            <tr class="hover:bg-dark-hover cursor-pointer" onclick="window.location.href='/consultor/${consultor.id}'">
                <td class="px-6 py-4 text-gray-300">${consultor.nome}</td>
                <td class="px-6 py-4 text-gray-300">${consultor.email}</td>
                <td class="px-6 py-4 text-gray-300">${consultor.placa_carro || '-'}</td>
                <td class="px-6 py-4">
                    <button onclick="event.stopPropagation(); window.location.href='/consultor/${consultor.id}'" 
                        class="text-blue-400 hover:text-blue-300">Ver Perfil</button>
                </td>
            </tr>
        `).join('');
        
        atualizarPaginacao(data);
    } catch (error) {
        console.error('Erro ao carregar consultores:', error);
        document.getElementById('tabelaConsultores').innerHTML = 
            '<tr><td colspan="4" class="px-6 py-8 text-center text-red-400">Erro ao carregar consultores</td></tr>';
    }
}

function atualizarPaginacao(data) {
    const info = document.getElementById('paginacaoInfo');
    const controles = document.getElementById('paginacaoControles');
    
    const inicio = (data.page - 1) * data.page_size + 1;
    const fim = Math.min(data.page * data.page_size, data.total_count);
    
    info.textContent = `Mostrando ${inicio} a ${fim} de ${data.total_count} consultores`;
    
    let botoesHTML = '';
    
    if (data.page > 1) {
        botoesHTML += `<button onclick="carregarConsultores(1)" class="px-3 py-1 bg-dark-card text-gray-300 rounded hover:bg-dark-hover">Primeira</button>`;
        botoesHTML += `<button onclick="carregarConsultores(${data.page - 1})" class="px-3 py-1 bg-dark-card text-gray-300 rounded hover:bg-dark-hover">Anterior</button>`;
    }
    
    const maxBotoes = 5;
    let inicioPagina = Math.max(1, data.page - Math.floor(maxBotoes / 2));
    let fimPagina = Math.min(data.total_pages, inicioPagina + maxBotoes - 1);
    
    if (fimPagina - inicioPagina < maxBotoes - 1) {
        inicioPagina = Math.max(1, fimPagina - maxBotoes + 1);
    }
    
    for (let i = inicioPagina; i <= fimPagina; i++) {
        if (i === data.page) {
            botoesHTML += `<button class="px-3 py-1 bg-blue-600 text-white rounded">${i}</button>`;
        } else {
            botoesHTML += `<button onclick="carregarConsultores(${i})" class="px-3 py-1 bg-dark-card text-gray-300 rounded hover:bg-dark-hover">${i}</button>`;
        }
    }
    
    if (data.page < data.total_pages) {
        botoesHTML += `<button onclick="carregarConsultores(${data.page + 1})" class="px-3 py-1 bg-dark-card text-gray-300 rounded hover:bg-dark-hover">Próxima</button>`;
        botoesHTML += `<button onclick="carregarConsultores(${data.total_pages})" class="px-3 py-1 bg-dark-card text-gray-300 rounded hover:bg-dark-hover">Última</button>`;
    }
    
    controles.innerHTML = botoesHTML;
}

carregarConsultores();
