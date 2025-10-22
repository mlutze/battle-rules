function calcByName(name, obj) {
    switch (name) {
        case "n":
            return calc_n(obj);
        case "t":
            return calc_t(obj);
        case "x":
            return calc_x(obj);
        case "e":
            return calc_e(obj);
        case "s":
            return calc_s(obj);   
    }
}

function calc_n(obj) {
    let {h, u, r, P, H} = obj;
    let num = h * u * Math.pow(r, P);
    let denom = Math.pow(10, P) * H;
    return Math.round(num / denom);
}

function calc_t(obj) {
    let {S, d, b, P, H, h, r, A} = obj;
    console.log(obj);
    let num = d * Math.pow(10 + b, P) * H * S;
    console.log("num: " + num);
    let denom = h * Math.pow(r, P) * A;
    console.log("denom: " + denom);
    return S - Math.round(num / denom);
}

function calc_x(obj) {
    let {n, l, G} = obj;
    let num = n + l;
    let denom = 2 * G;
    return Math.ceil(num / denom);
}

function calc_e(obj) {
    let {c, u, G} = obj;
    let num = Math.sqrt(Math.pow(c, 2) * u);
    let denom = G;
    return num / denom;
}

function calc_s(obj) {
    let {A, H, F} = obj;
    let num = 3 * A;
    let denom = H * F;
    return num / denom;
}