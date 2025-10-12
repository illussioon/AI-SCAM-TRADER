const coins = ['the-open-network', 'solana', 'ethereum', 'bitcoin', 'litecoin'];
    const url = `https://api.coingecko.com/api/v3/coins/markets?vs_currency=rub&ids=${coins.join(',')}&price_change_percentage=24h`;

    async function loadPrices() {
      try {
        const res = await fetch(url);
        const data = await res.json();

        const tbody = document.querySelector('#crypto-table tbody');
        tbody.innerHTML = '';

        data.forEach(coin => {
          const change = coin.price_change_percentage_24h;
          const cls = change >= 0 ? 'up' : 'down';
          const symbol = change >= 0 ? '▲' : '▼';
          const row = `
            <tr>
              <td>${coin.name} (${coin.symbol.toUpperCase()})</td>
              <td>${coin.current_price.toLocaleString('ru-RU')} ₽</td>
              <td class="${cls}">${symbol} ${change.toFixed(2)}%</td>
            </tr>
          `;
          tbody.insertAdjacentHTML('beforeend', row);
        });
      } catch (err) {
        console.error('Ошибка загрузки:', err);
      }
    }

    // Загрузка сразу и автообновление каждые 60 сек
    loadPrices();
    setInterval(loadPrices, 60000);