function update() {
    let inputs = getInputs();
    let outputs = getOutputs(inputs);
    setOutputs(outputs);
}

function getInputs() {
    let params = [
        "A", "H", "P", "S", "F", "G",
        "h", "r", "d", "b", "n", "l", "u", "c", "p"
    ];

    let obj = {};
    for (let param of params) {
        let node = document.getElementById("input-" + param);
        obj[param] = parseFloat(node.value);
    }
    return obj;
}

function getOutputs(obj) {
    let params = [
        "n", "t", "x", "m", "e", "s"
    ];

    let res = {};
    for (let param of params) {
        res[param] = calcByName(param, obj);
    }
    return res;
}

function setOutputs(obj) {
    for (let param in obj) {
        let node = document.getElementById("output-" + param);
        if (node === null) {
            console.error("no output-" + param)
        }
        node.value = obj[param];
    }
}

document.onchange = update