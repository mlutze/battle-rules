function calc_n(h, u, r, P, H) {
    let num = h * u * Math.pow(r, P);
    let denom = Math.pow(10, P) * H;
    return Math.round(num / denom);
}

function calc_t(S, d, b, P, H, h, r, A) {
    let num = d * Math.pow(10 + b, P) * H * S;
    let denom = h * Math.pow(r, P) * A;
    return S - Math.round(num / denom);
}

function calc_x(n, l, G) {
    let num = n + l;
    let denom = 2 * G;
    return Math.ceil(num / denom);
}

function calc_e(c, u, G) {
    let num = Math.sqrt(Math.pow(c, 2) * u);
    let denom = G;
    return num / denom;
}

function calc_s(A, H, F) {
    let num = 3 * A;
    let denom = H * F;
    return num / denom;
}