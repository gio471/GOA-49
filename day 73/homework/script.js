function selectTip(tipPercentage) {
    document.getElementById('customTip').value = '';
    calculateTip(tipPercentage);
}

function selectCustomTip() {
    let customTip = parseFloat(document.getElementById('customTip').value);
    if (!isNaN(customTip)) {
        calculateTip(customTip);
    }
}

function calculateTip(tipPercentage) {
    let bill = parseFloat(document.getElementById('bill').value);
    let people = parseInt(document.getElementById('people').value);

    if (isNaN(bill) || isNaN(people) || people === 0) {
        alert("Please enter valid bill and number of people.");
        return;
    }

    let tipAmount = (bill * (tipPercentage / 100)) / people;
    let totalAmount = (bill / people) + tipAmount;

    document.getElementById('tipAmount').textContent = `$${tipAmount.toFixed(2)}`;
    document.getElementById('totalAmount').textContent = `$${totalAmount.toFixed(2)}`;
}

function resetCalculator() {
    document.getElementById('bill').value = '';
    document.getElementById('people').value = '';
    document.getElementById('customTip').value = '';
    document.getElementById('tipAmount').textContent = '$0.00';
    document.getElementById('totalAmount').textContent = '$0.00';
}