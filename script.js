document.getElementById('convertButton').addEventListener('click', async () => {
    const amount = document.getElementById('amount').value;
    const fromCurrency = document.getElementById('fromCurrency').value;
    const toCurrency = document.getElementById('toCurrency').value;

    const response = await fetch(`/convert?amount=${amount}&from=${fromCurrency}&to=${toCurrency}`);
    const result = await response.json();

    document.getElementById('result').innerText = `Resultado: ${result.convertedAmount} ${toCurrency}`;
});
